#!/usr/bin/env python3
"""Check Jekyll's generated artifacts with Python's standard library only."""
import argparse
from collections import Counter
from datetime import datetime
from html.parser import HTMLParser
import json
from pathlib import Path
import re
import struct
from urllib.parse import unquote, urljoin, urlsplit
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

    check(bool(documents), 'No generated HTML found')
    check(len(titles) == len(set(titles)), 'Page titles are not unique')
    reference_count = 0
    for file, doc in documents.items():
        for tag, attrs in doc.nodes:
            value = attrs.get('href') if tag in ('a', 'link') else attrs.get('src') if tag in ('img', 'script') else None
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
            check(data.get('datePublished') == '2026-09-05T13:50:00+03:00', 'Article schema date changed')

    ns = {'a': 'http://www.w3.org/2005/Atom'}
    feed = ET.parse(root / 'feed.xml').getroot()
    check(feed.tag == '{http://www.w3.org/2005/Atom}feed', 'Feed is not Atom')
    check('Engineering Notes' in feed.findtext('a:title', '', ns), 'Feed title incorrect')
    entries = feed.findall('a:entry', ns)
    check(bool(entries), 'Feed has no entries')
    for entry in entries:
        for field in ('title', 'id', 'updated', 'published', 'content'):
            check(bool(entry.findtext('a:' + field, '', ns)), f'Feed entry missing {field}')
        for field in ('updated', 'published'):
            datetime.fromisoformat(entry.findtext('a:' + field, '', ns).replace('Z', '+00:00'))
        alternate = entry.find("a:link[@rel='alternate']", ns)
        check(alternate is not None and local_path(alternate.get('href', '')).is_file(), 'Feed article link broken')
    original = [e for e in entries if e.find("a:link[@href='" + origin + base + post_route + "']", ns) is not None]
    check(len(original) == 1, 'Original feed URL missing/duplicated')
    if original:
        check(original[0].findtext('a:published', '', ns) == '2026-09-05T13:50:00+03:00', 'Original feed date changed')
        check(original[0].findtext('a:author/a:name', '', ns) == 'Ayhan Gurbangeldiyev', 'Feed author incorrect')

    sitemap = ET.parse(root / 'sitemap.xml').getroot()
    sitemap_urls = [e.text for e in sitemap.iter('{http://www.sitemaps.org/schemas/sitemap/0.9}loc')]
    for route in ('/', '/writing/', '/topics/', '/about/', post_route):
        check(origin + base + route in sitemap_urls, f'Sitemap missing {route}')
    for url in sitemap_urls:
        check(url.startswith(origin + base + '/'), 'Sitemap has incorrect origin')
        check(local_path(url).is_file(), f'Sitemap URL does not exist: {url}')
        check(not any(s in url for s in ('/docs/', '/templates/', '/scripts/', '/404.html')), f'Private source/404 in sitemap: {url}')
    check('Sitemap: ' + origin + base + '/sitemap.xml' in (root / 'robots.txt').read_text(), 'robots sitemap mismatch')
    check((root / '404.html').is_file(), 'Custom 404 missing')
    for directory in ('docs', 'templates', 'scripts', 'vendor'):
        check(not (root / directory).exists(), f'Source-only directory published: {directory}')
    for svg in root.rglob('*.svg'):
        image = ET.parse(svg).getroot()
        check(bool(image.find('{http://www.w3.org/2000/svg}title').text), f'{svg.name}: no SVG title')
        check(bool(image.find('{http://www.w3.org/2000/svg}desc').text), f'{svg.name}: no SVG description')
    for name in ('engineering-notes-social', 'agent-coordination-social'):
        png = (root / 'assets/images' / (name + '.png')).read_bytes()
        check(png[:8] == b'\x89PNG\r\n\x1a\n' and struct.unpack('>II', png[16:24]) == (1200, 630), f'{name}: social image dimensions/format incorrect')
    if errors:
        raise SystemExit('\n'.join('FAIL: ' + error for error in errors))
    print(f'PASS: {len(documents)} HTML pages, {reference_count} local references, {len(entries)} Atom entries, {len(sitemap_urls)} sitemap URLs; metadata, dates, original permalink, diagrams and social assets valid.')


if __name__ == '__main__':
    main()
