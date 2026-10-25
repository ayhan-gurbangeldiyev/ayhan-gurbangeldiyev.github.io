#!/usr/bin/env python3
"""Check Jekyll's generated artifacts with Python's standard library only."""
import argparse
from datetime import datetime
from html.parser import HTMLParser
import json
from pathlib import Path
import re
import struct
from urllib.parse import unquote, urljoin, urlsplit
from urllib.robotparser import RobotFileParser
import xml.etree.ElementTree as ET


class Document(HTMLParser):
    def __init__(self, source):
        super().__init__(convert_charrefs=True)
        self.nodes, self.ids, self.titles, self.text = [], [], [], []
        self.in_title = False
        self.feed(source)

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        self.nodes.append((tag, attrs))
        if attrs.get('id'):
            self.ids.append(attrs['id'])
        if tag == 'title':
            self.in_title = True

    def handle_endtag(self, tag):
        if tag == 'title':
            self.in_title = False

    def handle_data(self, data):
        self.text.append(data)
        if self.in_title:
            self.titles.append(data)

    def find(self, tag, **attrs):
        return [a for t, a in self.nodes if t == tag and all(a.get(k) == v for k, v in attrs.items())]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('destination', nargs='?', default='_site')
    parser.add_argument('--url', default='https://ayhan-gurbangeldiyev.github.io')
    parser.add_argument('--baseurl', default='')
    args = parser.parse_args()
    root = Path(args.destination).resolve()
    origin = args.url.rstrip('/')
    base = args.baseurl.rstrip('/')
    errors, documents, routes, titles = [], {}, {}, []

    def check(condition, message):
        if not condition:
            errors.append(message)

    def local_path(url):
        path = unquote(urlsplit(url).path)
        if base:
            if not (path == base or path.startswith(base + '/')):
                return None
            path = path[len(base):]
        candidate = root / path.lstrip('/')
        if path.endswith('/') or candidate.is_dir():
            candidate /= 'index.html'
        return candidate

    for file in sorted(root.rglob('*.html')):
        rel = file.relative_to(root).as_posix()
        route = '/' + (rel[:-10] if rel.endswith('index.html') else rel)
        url = origin + base + route
        doc = Document(file.read_text())
        documents[file], routes[file] = doc, url
        title = ''.join(doc.titles).strip()
        titles.append(title)
        check(bool(title), f'{rel}: missing title')
        check(len(doc.find('h1')) == 1, f'{rel}: expected one h1')
        check(len(doc.ids) == len(set(doc.ids)), f'{rel}: duplicate IDs')
        check(bool(doc.find('html', lang='en')), f'{rel}: incorrect language')
        check(len(doc.find('main')) == 1, f'{rel}: missing main landmark')
        check(bool(doc.find('a', href='#main')), f'{rel}: missing skip link')
        check(bool(doc.find('meta', name='viewport')), f'{rel}: missing viewport')
        check(bool(doc.find('meta', property='og:locale', content='en_US')), f'{rel}: missing Open Graph locale')
        check(bool(doc.find('a', **{'class': 'home-link', 'href': base + '/'})), f'{rel}: missing Home control')
        masthead = re.search(r'<div class="masthead">(.*?)</div>', file.read_text(), re.S)
        check(masthead is not None and not Document(masthead.group(1)).find('span', **{'class': 'identity-mark'}), f'{rel}: old AG masthead still present')
        header_links = re.search(r'<nav class="header-links"[^>]*>(.*?)</nav>', file.read_text(), re.S)
        check(header_links is not None, f'{rel}: missing author/contact links')
        if header_links:
            links_doc = Document(header_links.group(1))
            check(len(links_doc.find('a')) == 5, f'{rel}: incorrect author/contact links')
            check(len(links_doc.find('svg', **{'aria-hidden': 'true'})) == 5, f'{rel}: missing decorative link icons')
        check(bool(doc.find('link', rel='icon', type='image/png', sizes='96x96')), f'{rel}: missing PNG favicon')
        descriptions = doc.find('meta', name='description')
        check(len(descriptions) == 1 and bool(descriptions[0].get('content')), f'{rel}: invalid description')
        canonical = doc.find('link', rel='canonical')
        check(len(canonical) == 1 and canonical[0].get('href') == url, f'{rel}: canonical mismatch {canonical}, expected {url}')
        for prop in ('og:title', 'og:description', 'og:url', 'og:image', 'og:image:alt'):
            check(len(doc.find('meta', property=prop)) == 1, f'{rel}: missing/duplicate {prop}')
        autodiscovery = doc.find('link', type='application/atom+xml')
        check(len(autodiscovery) == 1 and autodiscovery[0].get('href') == origin + base + '/feed.xml', f'{rel}: feed autodiscovery mismatch')
        for attrs in doc.find('img'):
            check('alt' in attrs, f'{rel}: missing image alt')
            check(bool(attrs.get('width')) and bool(attrs.get('height')), f'{rel}: missing image dimensions')
        for attrs in doc.find('a'):
            if attrs.get('target') == '_blank':
                check({'noopener', 'noreferrer'} <= set(attrs.get('rel', '').split()), f'{rel}: unsafe external target')
            check(not attrs.get('href', '').lower().startswith('javascript:'), f'{rel}: javascript link')

    home_file = root / 'index.html'
    if home_file in documents:
        home = documents[home_file]
        check(''.join(home.titles).strip() == 'Ayhan Gurbangeldiyev | GitHub Blog', 'Homepage title mismatch')
        check(bool(home.find('meta', property='og:site_name', content='Ayhan Gurbangeldiyev')), 'Preferred site name missing')
        blocks = re.findall(r'<script type="application/ld\+json">(.*?)</script>', home_file.read_text(), re.S)
        check(len(blocks) == 1 and json.loads(blocks[0]).get('name') == 'Ayhan Gurbangeldiyev', 'WebSite preferred name mismatch')
    check(bool(documents), 'No generated HTML found')
    check(len(titles) == len(set(titles)), 'Page titles are not unique')
    reference_count = 0
    for file, doc in documents.items():
        for tag, attrs in doc.nodes:
            value = attrs.get('href') if tag in ('a', 'link') else attrs.get('src') if tag in ('img', 'script') else attrs.get('srcset') if tag == 'source' else None
            if not value:
                continue
            url = urljoin(routes[file], value)
            parsed = urlsplit(url)
            if parsed.scheme not in ('http', 'https') or parsed.netloc != urlsplit(origin).netloc:
                continue
            reference_count += 1
            target = local_path(url)
            check(target is not None and target.is_file(), f'{file.relative_to(root)}: missing local target {value}')
            if target in documents and parsed.fragment:
                check(unquote(parsed.fragment) in documents[target].ids, f'{file.relative_to(root)}: broken fragment {value}')

    post_route = '/writing/before-adding-a-second-agent/'
    post_file = root / 'writing/before-adding-a-second-agent/index.html'
    check(post_file in documents, 'Original article permalink missing')
    if post_file in documents:
        post = documents[post_file]
        check('This article was drafted with AI assistance.' in ''.join(post.text), 'Original AI disclosure missing')
        dates = post.find('time', datetime='2026-09-05T13:50:00+03:00')
        check(bool(dates), 'Original publication timestamp changed')
        structured = re.findall(r'<script type="application/ld\+json">(.*?)</script>', post_file.read_text(), re.S)
        check(len(structured) == 1, 'Expected one structured data block from jekyll-seo-tag')
        for block in structured:
            data = json.loads(block)
            check(data.get('@type') in ('Article', 'BlogPosting'), 'Incorrect Article structured data type')
            check(data.get('author', {}).get('name') == 'Ayhan Gurbangeldiyev', 'Article schema author missing')
            check(data.get('author', {}).get('url') == origin + '/about/', 'Article schema author profile missing')
            check(data.get('datePublished') == '2026-09-05T13:50:00+03:00', 'Article schema date changed')

    ns = {'a': 'http://www.w3.org/2005/Atom'}
    feed = ET.parse(root / 'feed.xml').getroot()
    check(feed.tag == '{http://www.w3.org/2005/Atom}feed', 'Feed is not Atom')
    check(feed.findtext('a:title', '', ns) == 'Ayhan Gurbangeldiyev | GitHub Blog', 'Feed title incorrect')
    entries = feed.findall('a:entry', ns)
    check(bool(entries), 'Feed has no entries')
    entry_ids = [entry.findtext('a:id', '', ns) for entry in entries]
    check(len(entry_ids) == len(set(entry_ids)), 'Duplicate feed entry IDs')
    check(feed.findtext('a:id', '', ns) == origin + base + '/feed.xml', 'Stable feed ID changed')
    check(feed.findtext('a:icon', '', ns) == origin + base + '/assets/images/favicon.png', 'Feed icon missing')
    published_dates = []
    for entry in entries:
        for field in ('title', 'id', 'updated', 'published', 'content'):
            check(bool(entry.findtext('a:' + field, '', ns)), f'Feed entry missing {field}')
        for field in ('updated', 'published'):
            date = datetime.fromisoformat(entry.findtext('a:' + field, '', ns).replace('Z', '+00:00'))
            check(date.tzinfo is not None, f'Feed {field} missing time zone')
            if field == 'published':
                published_dates.append(date)
        alternate = entry.find("a:link[@rel='alternate']", ns)
        check(alternate is not None and local_path(alternate.get('href', '')).is_file(), 'Feed article link broken')
        content = entry.find('a:content', ns)
        check(content is not None and content.get('type') == 'html', 'Feed must carry full HTML content')
        if content is not None:
            body = Document(content.text or '')
            for img in body.find('img'):
                image_url = img.get('src', '')
                check(urlsplit(image_url).scheme == 'https', f'Feed image URL must be absolute HTTPS: {image_url}')
                target = local_path(image_url)
                check(target is not None and target.is_file(), f'Feed image missing: {image_url}')
                check(bool(img.get('alt')), 'Feed image missing meaningful alt text')
                check(bool(img.get('width')) and bool(img.get('height')), 'Feed image dimensions missing')
                check(not urlsplit(image_url).path.endswith('.svg'), 'Feed img needs a raster fallback for SVG')
        for media in entry.findall('{http://search.yahoo.com/mrss/}content'):
            check(media.get('medium') == 'image' and media.get('type', '').startswith('image/'), 'Feed image media type missing')
            check(local_path(media.get('url', '')).is_file(), 'Feed media URL missing')
    check(published_dates == sorted(published_dates, reverse=True), 'Feed posts are not newest first')
    original = [e for e in entries if e.find("a:link[@href='" + origin + base + post_route + "']", ns) is not None]
    check(len(original) == 1, 'Original feed URL missing/duplicated')
    if original:
        check(original[0].findtext('a:published', '', ns) == '2026-09-05T13:50:00+03:00', 'Original feed date changed')
        check(original[0].findtext('a:author/a:name', '', ns) == 'Ayhan Gurbangeldiyev', 'Feed author incorrect')

    sitemap = ET.parse(root / 'sitemap.xml').getroot()
    sitemap_urls = [e.text for e in sitemap.iter('{http://www.sitemaps.org/schemas/sitemap/0.9}loc')]
    for route in ('/', '/writing/', '/topics/', '/about/', '/follow/', post_route):
        check(origin + base + route in sitemap_urls, f'Sitemap missing {route}')
    for url in sitemap_urls:
        check(url.startswith(origin + base + '/'), 'Sitemap has incorrect origin')
        check(local_path(url).is_file(), f'Sitemap URL does not exist: {url}')
        check(not any(s in url for s in ('/docs/', '/templates/', '/scripts/', '/404.html')), f'Private source/404 in sitemap: {url}')
    check('Sitemap: ' + origin + base + '/sitemap.xml' in (root / 'robots.txt').read_text(), 'robots sitemap mismatch')
    check((root / '404.html').is_file(), 'Custom 404 missing')
    if root / '404.html' in documents:
        check(bool(documents[root / '404.html'].find('meta', name='robots', content='noindex,follow')), '404 must have noindex')
    about_file = root / 'about/index.html'
    if about_file in documents:
        about_schema = re.findall(r'<script type="application/ld\+json">(.*?)</script>', about_file.read_text(), re.S)
        check(len(about_schema) == 1 and json.loads(about_schema[0]).get('@type') == 'AboutPage', 'About page structured data type incorrect')
    robots = RobotFileParser()
    robots.parse((root / 'robots.txt').read_text().splitlines())
    for bot in ('Googlebot', 'bingbot', 'OAI-SearchBot'):
        check(robots.can_fetch(bot, origin + base + post_route), f'{bot} blocked from article')
    for directory in ('docs', 'templates', 'scripts', 'vendor'):
        check(not (root / directory).exists(), f'Source-only directory published: {directory}')
    for svg in root.rglob('*.svg'):
        image = ET.parse(svg).getroot()
        check(bool(image.find('{http://www.w3.org/2000/svg}title').text), f'{svg.name}: no SVG title')
        check(bool(image.find('{http://www.w3.org/2000/svg}desc').text), f'{svg.name}: no SVG description')
    for name in ('engineering-notes-social', 'agent-coordination-social'):
        png = (root / 'assets/images' / (name + '.png')).read_bytes()
        check(png[:8] == b'\x89PNG\r\n\x1a\n' and struct.unpack('>II', png[16:24]) == (1200, 630), f'{name}: social image dimensions/format incorrect')
    for name, size in (('favicon', 96), ('apple-touch-icon', 180)):
        png = (root / 'assets/images' / (name + '.png')).read_bytes()
        check(png[:8] == b'\x89PNG\r\n\x1a\n' and struct.unpack('>II', png[16:24]) == (size, size), f'{name}: icon dimensions incorrect')
    check((root / 'assets/icons/LICENSE.txt').is_file(), 'Bundled icon license missing')
    check((root / 'assets/licenses/jekyll-feed.txt').is_file(), 'Adapted feed template license missing')
    follow_file = root / 'follow/index.html'
    check(follow_file in documents, 'RSS follow guide missing')
    if follow_file in documents:
        follow = documents[follow_file]
        addresses = follow.find('input', id='feed-address')
        check(len(addresses) == 1 and addresses[0].get('value') == origin + base + '/feed.xml' and 'readonly' in addresses[0], 'Follow page feed address incorrect')
        copy_buttons = follow.find('button', id='copy-feed', type='button')
        check(len(copy_buttons) == 1 and 'hidden' in copy_buttons[0], 'Copy control must use progressive enhancement')
        check(bool(follow.find('p', id='copy-feed-status', role='status')), 'Copy status announcement missing')
        check(bool(follow.find('a', href=base + '/feed.xml')), 'Follow page raw feed link missing')
    if errors:
        raise SystemExit('\n'.join('FAIL: ' + error for error in errors))
    print(f'PASS: {len(documents)} HTML pages, {reference_count} local references, {len(entries)} Atom entries, {len(sitemap_urls)} sitemap URLs; metadata, dates, original permalink, diagrams and social assets valid.')


if __name__ == '__main__':
    main()
