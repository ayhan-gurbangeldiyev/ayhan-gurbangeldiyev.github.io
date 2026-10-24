# Site audit — 24 October 2026

## Verified starting point

- Source: `ayhan-gurbangeldiyev/ayhan-gurbangeldiyev.github.io`, base commit `8a1e4a0e5855d4c2fa0bbdefc46663ff8b0aadd2`.
- GitHub Pages API: `build_type: legacy`, source `main`, path `/`, HTTPS enforced, no custom domain. Latest production build succeeded on 5 September 2026. No deployment settings were changed.
- Five tracked files: `_config.yml`, `index.md`, `README.md`, `assets/main.scss`, one Markdown post. No Gemfile, CI, custom layouts, sitemap plugin, or custom 404.
- Jekyll 3.10.0 / Minima; existing `jekyll-feed` and `jekyll-seo-tag`. The old CSS only addressed a mobile title/navigation collision.
- One published post: **Before Adding a Second Agent: What the Evidence Actually Shows**, 5 September 2026, 13:50 +03:00. Existing URL: `/writing/before-adding-a-second-agent/`.
- Production `/feed.xml` fetched directly and parsed as XML: one Atom entry, correct author, original publication date and article URL. Feed title used “Technical Notes”. No replacement feed service is needed.

## Issues and changes

| Finding | Response |
| --- | --- |
| Default theme gives little editorial hierarchy | Own layouts, restrained identity, featured selection, complete writing archive |
| No topic navigation | Explicit topic taxonomy, render only populated topics |
| No article navigation or diagrams | Server-rendered contents, progressive heading permalinks, two original figures |
| No reusable publishing conventions | Front matter template, editorial checklist, visual attribution record |
| No reproducible local build | Pin GitHub Pages 232, commit lockfile, local build plus generated-output checks; optional validation workflow example |
| No documented relationship to portfolio writing | Inventory all discovered English and Turkish article routes; defer migration |
| No explicit theme preference | System default, user choice, persistent preference, storage failure fallback |

## Preservation boundary

The existing post filename, title, author, timestamp, original paragraphs, inline references, and AI-assisted disclosure are preserved. Its permalink is now explicit to protect it from future global permalink changes. The additions are metadata, two conceptual figures, and a reference list. A redesign is not a substantive research update; no artificial `last_modified_at` is added. Existing categories are retained.

Only this Pages repository is edited. The `.com` repository, professional profile, live Pages settings, and production branch are untouched. Merge approval remains with the owner; the existing branch-based deployment will publish a future merge.

## Verified contact sources

Source: [official portfolio](https://ayhangurbangeldiyev.com/) and its HTML, fetched 24 October 2026. Identity: AI engineer working on agents, retrieval and production software. Selected public links:

- [GitHub](https://github.com/ayhan-gurbangeldiyev)
- [LinkedIn](https://www.linkedin.com/in/ayhan-gurbangeldiyev/)
- `mailto:info@ayhangurbangeldiyev.com`

The portfolio also links [Medium](https://ayhangurbangeldiyev.medium.com/), [YouTube](https://www.youtube.com/@ayhanaiengineer), [Bluesky](https://bsky.app/profile/ayhangurbangeldiyev.com), [X](https://x.com/ayhangurbangldv), and [Facebook](https://www.facebook.com/ayhangurbangeldiyev). These destinations were verified as portfolio links, not authenticated or endorsed accounts. They are omitted from the publication navigation to keep a focused set of technical/professional destinations. LinkedIn blocks the web reader; the href is confirmed from the official portfolio source.

## Evidence and limits

The live site was inspected before implementation. The user then requested that Ego Lite not be used; subsequent work uses web fetches, terminal checks, and the app's browser. Reference responsive intent is inferred from HTML/CSS, not a device test of those sites. Our own layout is tested separately. See `validation.md` for actual results, rather than inferring performance from design intent.

Dependency support: [GitHub Pages versions](https://pages.github.com/versions/) (`versions.json` fetched during audit), [GitHub Jekyll documentation](https://docs.github.com/en/pages/setting-up-a-github-pages-site-with-jekyll/about-github-pages-and-jekyll). GitHub currently recommends Actions deployment, but preserving the verified branch source avoids an unnecessary deployment migration. `ci-workflow.example.yml` is a validation-only example, not an active workflow: the available GitHub OAuth token has `repo` but not the additional `workflow` scope needed to push new workflow files. No expanded credential permissions were requested. Local build and integration validation are available immediately.
