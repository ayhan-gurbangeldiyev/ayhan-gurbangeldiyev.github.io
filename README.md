# Engineering Notes

Independent technical writing by Ayhan Gurbangeldiyev on reliable and observable AI systems in practice.

- Publication: <https://ayhan-gurbangeldiyev.github.io/>
- Portfolio: <https://ayhangurbangeldiyev.com/>
- Feed: <https://ayhan-gurbangeldiyev.github.io/feed.xml>

## Local development

Use Ruby 3.3 and Bundler. Python 3 is required only for the generated-site checks. There is no npm build or remote font dependency. The `github-pages` gem is pinned to **232**, matching the Pages dependency set audited in October 2026 (Jekyll 3.10.0). Commit `Gemfile.lock` when deliberately updating dependencies.

```sh
bundle install
bundle exec jekyll serve --host 127.0.0.1
# Open http://127.0.0.1:4000
```

Production-equivalent validation:

```sh
JEKYLL_ENV=production bundle exec jekyll build --safe --strict_front_matter
python3 scripts/check_site.py _site
```

The checker verifies generated HTML links/fragments and assets, unique titles, semantic page structure, canonical and social metadata, Article JSON-LD, Atom entries, original date/URL, sitemap, custom 404, image dimensions and source-directory exclusion. It is not an external-link availability monitor or a substitute for browser/assistive-technology testing.

For a project subpath test:

```sh
bundle exec jekyll build --safe --strict_front_matter --baseurl /preview --destination _site-preview
python3 scripts/check_site.py _site-preview --baseurl /preview
```

Remove `_site-preview` after that test; it is not a production source directory.

## Add a note

Copy `templates/post.md` to `_posts/YYYY-MM-DD-descriptive-slug.md`. Replace placeholders, use the original publication timestamp and choose an explicit durable `permalink`. `description` and `excerpt` should be accurate, concise summaries. Keep legacy permalinks and original dates when editing old posts.

Set `article_type` to a useful label: Research note, Engineering deep dive, Build note, Decision record, Failure note, or Short note. Pick `topics` from `_data/topics.yml`; only topics containing actual posts are rendered. Categories remain available for legacy metadata. `featured: true` opts a post into the home feature; if several are true, the newest marked post is selected. The feature is not automatically assigned to the newest unmarked post.

Reading time is computed at 220 words/minute and is an estimate. `last_modified_at` is optional and is only for meaningful content changes. Article layouts provide author, date, summary, topics, h2 contents navigation and optional related posts. The related section is omitted until another post shares a topic. Headings and contents remain usable without JavaScript; JS adds visible permalink controls.

## Images and diagrams

Prefer original SVG for graphs, architecture and control flows. Store files in `assets/images/`; add an SVG title/description and a complete article alt text. Use the figure include:

```liquid
{% include figure.html src="/assets/images/single-vs-multi.svg" width=960 height=600 alt="Describe the meaningful flow and relationships." caption="Explain the diagram and distinguish conceptual from measured results." %}
```

Supply correct intrinsic dimensions. The include lazy-loads and links to the original vector for detail. Hero imagery loads eagerly; all images reserve their layout space. For photos/screenshots, consider optimized WebP/AVIF and preserve legibility. Do not invent measurements or label a conceptual graph as an experiment.

Set `cover` for an optional home feature visual. Use `image.path`, `image.width`, `image.height`, and `image.alt` for a social image. Default and article-specific social PNGs are 1200×630, exported from editable SVG masters. A local SVG rasterizer can regenerate those PNGs; no rasterizer is required for a normal Jekyll build. See [visual provenance](LICENSE-visuals.md) for sources and rights.

## RSS / Atom

The existing `jekyll-feed` plugin generates `/feed.xml`; it was already working before the redesign. It now uses the publication's Engineering Notes title, site author and accurate post metadata. The layout uses `{% feed_meta %}` once for HTML autodiscovery. Header, footer, writing archive and articles expose RSS links. Paste the feed URL into an Atom-compatible reader. No database, account, email list or external subscription service is needed.

`jekyll-feed` includes up to the configured 50 latest posts. Use original dates and URLs to avoid creating duplicate reader entries. The checker parses Atom XML, required entry data, authors and original date/permalink. It does not claim validation by every reader application.

## SEO and migration

`{% seo %}` from the existing `jekyll-seo-tag` owns titles, descriptions, canonicals, Open Graph, Twitter cards and JSON-LD; do not hand-add competing metadata. Site defaults supply a social image. Markdown posts use the `post` layout so the plugin emits BlogPosting data with author and dates. `jekyll-sitemap` 1.4.0 is supported by GitHub Pages 232 and generates `/sitemap.xml`; `robots.txt` advertises it. English is the current publication language.

Before publishing, check page title/summary, one h1, canonical origin and slug, author, original/update date, image/alt and working references. See the full [editorial/SEO checklist](docs/publishing-checklist.md).

For Search Console, an authorized owner must verify the `https://ayhan-gurbangeldiyev.github.io/` URL-prefix property (or use an existing verified property), then submit `sitemap.xml` under Sitemaps after deployment. Inspect the original article URL and monitor indexing. No Search Console verification/submission was performed in this redesign; there is no fabricated verification token.

Existing `.com` articles remain there. Future originals belong here. Do not copy full articles across domains without deciding the original and redirect/canonical strategy. The [migration inventory and plan](docs/content-migration.md) lists four English articles and four Turkish routes, and explains HTTP redirects, cross-domain canonical fallback and translation handling. This repository cannot update `.com` headers or redirects.

## Deployment and review

Verified Pages setting: **Deploy from a branch → `main` → `/`**. Merging an approved PR to `main` invokes the existing GitHub Pages Jekyll build. This change does not switch Pages to an Actions deployment, set a custom domain, or deploy the feature branch. Do not add `.nojekyll`.

Review the [validation record](docs/validation.md), then merge only when ready to publish. After deployment, verify `/`, the original article, `/feed.xml`, `/sitemap.xml`, a nonexistent route (custom 404), and social image URLs. Rollback: revert the redesign commit through a PR; no content or service migration is required.

The local build/check commands are ready to use. An optional [validation-only Actions example](docs/ci-workflow.example.yml) is provided for installation as `.github/workflows/validate.yml` by an appropriately scoped credential. It is not active in this PR: the available GitHub OAuth token lacks `workflow` scope. No account permissions were expanded. The example does not change the existing deployment source or publish a branch preview.

## Documentation

- [Starting audit](docs/site-audit.md)
- [Reference benchmark](docs/benchmark.md)
- [Design specification](docs/design-spec.md)
- [Editorial strategy and prioritized backlog](docs/editorial-strategy.md)
- [Publishing checklist](docs/publishing-checklist.md)
- [Content migration plan](docs/content-migration.md)
- [Validation results and limits](docs/validation.md)
