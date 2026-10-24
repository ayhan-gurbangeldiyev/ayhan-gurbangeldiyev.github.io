# Validation record — 24 October 2026

These are observed results, not promised Lighthouse or field-performance scores. Production deployment remains an owner review decision.

## Build and generated artifacts

Environment: local macOS ARM64, **Ruby 3.3.11**, Bundler 2.5.22, GitHub Pages gem 232, Jekyll 3.10.0, jekyll-feed 0.17.0, jekyll-seo-tag 2.8.0, jekyll-sitemap 1.4.0. The machine's system Ruby 2.6 could not resolve the supported dependency set; the successful build uses an isolated runtime and dependencies under the task's `work/`, without changing system Ruby. The repository uses ordinary Ruby/Bundler commands on a supported installation.

| Check | Result |
| --- | --- |
| `JEKYLL_ENV=production bundle exec jekyll build --safe --strict_front_matter` | Pass |
| `python3 scripts/check_site.py _site` | Pass: 6 HTML pages, 129 local references, 1 Atom entry, 5 sitemap URLs |
| Same build with `--baseurl /preview` and checker `--baseurl /preview` | Pass: same counts, correct subpath links and canonical URLs |
| Original article text comparison against base commit | All original nonempty body lines preserved in order |
| Original feed identity/date comparison | Entry ID, author, published and updated dates preserved; correct original link |
| Titles, summaries, canonical, OG image/alt, feed autodiscovery | Exactly one expected metadata set per page |
| Article JSON-LD | BlogPosting, correct author and original timestamp |
| XML | Atom and sitemap parsed; required entry data and sitemap destinations checked |
| Images | All referenced local assets exist; SVG XML/title/description and PNG 1200×630 dimensions checked |
| Source exclusions | No docs, templates, scripts or vendor files in published output |
| `git diff --check` | Pass |

Jekyll prints a non-fatal Faraday optional retry-middleware notice through GitHub metadata. The build succeeds without a GitHub API token; it does not need metadata API data. No dependency was added solely to silence that notice.

## Article infrastructure fixture

A synthetic two-post site was built outside the repository and outside production output, under `work/fixture-source` / `work/fixture-site`. Its purpose is rendering QA; it was not published as an article or described as an AI experiment. The generated checker passed for 7 HTML pages, 173 local references, 2 entries, and 6 sitemap URLs.

Additional assertions passed for Rouge-highlighted Python, Kramdown footnotes/backlinks, a meaningful updated date, inline `code`/emphasis in contents headings, a real related-post match, and a newly populated Retrieval & RAG topic. Assertions also confirm that the fixture is absent from production and that no empty related section appears on the actual single-post site.

## Browser checks

Tested in the Codex app's Chromium browser after the user requested no further Ego Lite use. No additional Ego Lite calls were made after that request.

- All six generated pages at **320, 768 and 1440 CSS pixels**: 18 route/width combinations, no horizontal page overflow. Home/article were also inspected at 390×844.
- Home and article inspected visually on desktop/mobile; screenshots saved beside the checkout in task outputs. All article SVGs successfully decoded at their declared 960px source widths. Prose uses 17px type and a 72ch maximum; code/table overflow is contained.
- Light/Dark selection works; an explicit dark choice survives reload. System mode responds to emulated light/dark system changes. Blocking `localStorage` access in the current QA document does not prevent the theme control changing the current theme; reloading removes the temporary block.
- Keyboard Tab exposes the skip link with a solid visible outline. Activating it moves focus to `main`. Native select and search are keyboard controls. A contents link reaches its heading; article navigation precedes prose in DOM order, matching the mobile visual order.
- Search finds the note for “evaluation”, reports one result; a nonexistent query hides it and announces no matches; clearing restores the archive.
- With page JavaScript disabled: complete article/disclosure, metadata, four server-rendered contents links and navigation remain; inactive theme/search controls stay hidden; the writing archive still shows its real note. Script execution was restored after testing.
- Unknown local URL returns **HTTP 404** and displays the designed 404 content through the QA preview server. This checks the page and status locally; GitHub's production 404 routing must still be checked after merge/deploy.
- Fresh page navigations, theme changes and search interactions produced no `Runtime.exceptionThrown` events in the bounded browser check. QA emulation/temporary overrides were cleared.

## Accessibility

**axe-core 4.14.0**, WCAG 2 A/AA, 2.1 AA, 2.2 AA and best-practice tags: all six pages at 1440px in both themes, **12 runs with zero automated violations**. Home also had a 390px light-mode run with zero automated violations.

Axe marked three decorative, `aria-hidden` right-arrow spans on home for manual contrast review in each theme. They inherit their link color: light blue/paper **6.50–6.78:1**, dark blue/paper **8.90–9.45:1**. Manual palette calculations also verify secondary text: **5.94:1 light** and **8.53:1 dark**. These notes were reviewed rather than treated as automated passes. Search uses the secondary-text color for a sufficiently visible control boundary. Semantic headings, focus and no-JS behavior were additionally reviewed; this is not a complete assistive-technology certification.

## Performance evidence and limits

The CSS is approximately **18.7KB raw / 4.5KB gzip**; the two production JS files total approximately **2.2KB raw / 1.0KB gzip**. These are local compression calculations, not actual Pages transfer headers. No framework bundle, external font, analytics, autoplay or third-party subscription code is loaded. Images reserve dimensions and article figures lazy-load; the hero is eager.

**Not run / not claimed:** Lighthouse, WebPageTest, real-user LCP/INP/CLS, Safari/Firefox or real-device tests, a full screen-reader session, independent feed-reader applications, Google indexing/Rich Results verification, or Search Console submission. The CWV goals (LCP ≤2.5s, INP ≤200ms, CLS ≤0.1) remain production field-data targets; no local result is presented as proof of meeting them.

The three original research-reference URLs were fetched successfully. LinkedIn account content could not be read through the web reader; its correct public href and the email address were verified from the official portfolio. Public English `.com` article HTML and sitemap were fetched, but Turkish prose and Medium article canonicals were not audited. Reference-site mobile behavior was not tested.

## CI and release boundary

The available GitHub credential has `repo`, `read:org`, `gist`; it lacks `workflow`. A validation-only workflow example is supplied in `docs/ci-workflow.example.yml`, without increasing account permissions. **No active CI workflow or remote CI run is claimed.** Local build and validation are complete. The existing `main` → `/` branch-based Pages deployment is unchanged. This feature branch is for PR review; the site has not been merged or published.
