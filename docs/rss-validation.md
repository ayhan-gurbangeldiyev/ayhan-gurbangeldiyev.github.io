# RSS follow experience — plan and validation

25 October 2026. This is the implementation and pre-release validation record. Actual deployment and refreshed external-reader results are recorded in the associated PR/task delivery after publication.

## Step 1 — Audit the current feed

The existing `/feed.xml` is an Atom 1.0 feed with one real article, full content, author, original publication date and a stable entry ID. HTTP 200 and conditional `If-None-Match` → 304 were verified on the public site. The feed address and all original IDs/dates must remain stable.

The independent [Inoreader validator](https://www.inoreader.com/rss-feed-validator) could fetch and parse the pre-change public feed: **0 errors, 2 warnings, 2 notes**. Its warnings identified relative article image addresses and missing MIME type on the image's Media RSS content element. Its notes concerned GitHub Pages' generic `application/xml` header without a charset parameter and the absence of a WebSub hub. These were observed report results, not inferred from XML syntax alone.

## Step 2 — Make following understandable

- Add `/follow/` with a plain explanation, three steps, the stable feed URL, a copy control, a raw-feed link and a public reader preview.
- Send the human-facing RSS links in the masthead, footer, writing archive, About and article navigation to that guide. Keep HTML feed autodiscovery pointed directly at `/feed.xml`.
- Keep the URL selectable without JavaScript. Reveal the copy button only when its handler is available. Announce success through a live status region; on Clipboard API failure, focus/select the address and give manual copy instructions.
- Describe refresh behavior honestly: the chosen reader checks for updates on its own schedule. No email address, newsletter provider or new subscription database is required.
- Version CSS/JavaScript URLs per build so existing browser caches receive the new copy handler and styles after deployment. The subscription feed URL and entry IDs stay unchanged.

## Step 3 — Fix demonstrated reader compatibility gaps

The figure include now uses **absolute HTTPS URLs**. A `picture/source` prefers the original SVG on the website; its `img` points to a **PNG fallback** for readers that discard SVG or source elements. Both existing diagrams have 2× PNG exports (1920×1200 and 1920×1360), with the same complete alt text, caption and display dimensions. The original SVG remains available at the figure link.

The pinned `jekyll-feed` **0.17.0** template emits a Media RSS image element without a MIME type. The local root `feed.xml` is adapted from that MIT-licensed template to add an appropriate image MIME type, the publication icon and author profile URIs. This is a narrow template override, not another feed service. The existing plugin deliberately skips generation when this file exists and still supplies `{% feed_meta %}`; there is one feed at the original address. License: `assets/licenses/jekyll-feed.txt`.

Preserved: feed ID, post IDs, original publication/update timestamps, author name, post URLs, categories, full content and disclosure. Image MIME types are derived for supported image extensions or supplied by `image.type`. Unsupported types do not emit misleading media metadata. Full-content publishing remains explicit with `feed.excerpt_only: false`.

The two informational delivery notes are not silently treated as failures or fixed by moving hosting. UTF-8 is declared in the XML and parsed correctly; GitHub Pages controls response headers. WebSub is deferred because immediate push delivery is unnecessary for the current low-frequency publication and would add a hub/publish integration. The UI describes polling behavior instead.

## Step 4 — Validate, review and publish

Observed pre-release checks:

| Check | Result |
| --- | --- |
| Production safe Jekyll build and generated-output checks | Pass: **7 HTML pages, 161 local references, 1 Atom entry, 6 sitemap URLs** |
| `/preview` baseurl build | Pass with the same counts |
| Original live feed versus new output | Feed ID, entry ID, publication/update times and author name unchanged |
| New feed fields | Typed image media, feed icon, author URI, absolute HTTPS image URLs, existing full content |
| Local-only two-post fixture | Pass: **8 HTML pages, 201 local references, 2 entries, 7 sitemap URLs** |
| Fixture article content | Highlighted Python, `<`, `&`, `]]>` in code, footnotes, HTML-typed title decoding, meaningful update time and raster image fallback preserved |
| Fixture exclusion | No synthetic article in production output |
| Clipboard success | Correct 47-character feed URL sent to the API; actual keyboard paste into another field matched the URL |
| Clipboard denied | Address focused and fully selected; manual-copy status announced; button usable again |
| JavaScript disabled | Copy button hidden; address, raw feed link and instructions remain usable |
| Responsive | Seven pages × 320/768/1440px: **21 combinations, no horizontal overflow** |
| axe-core 4.14.0 | Seven pages in both themes: **14 runs, zero automated violations** |

The three decorative arrows on the unchanged homepage retain the existing manual contrast notes. The new follow page had no axe incomplete findings in either theme. Automated checks are not a complete screen-reader or cross-browser certification.

### External reader environments

- **Inoreader public viewer + validator:** recognized Atom, one entry, correct title, author, date and original article link. Its pre-release diagnostics provided the two concrete image fixes above. The public viewer intentionally shows article previews; it is not a signed-in full-article view. Recheck the actual published feed after the merge.
- **AICurate public RSS reader:** independently fetched the original feed directly, reported one loaded feed and one article, and showed the correct title/date/link/excerpt. It also intentionally displays previews. Refresh after deployment to verify the new feed remains ingestible.
- **FeedZero local-only mode:** discovered the publication and added the feed, but did not list its article during this test even after refresh. This result is **not counted as a pass**. No cloud sync or account was created, and no claim is made that the change fixes that application's behavior.

The public preview checks do not prove every reader's full-body rendering of code and diagrams. Full article markup is verified through the generated Atom fixture; actual PNG responses and the updated independent diagnostics are checked on the published site. No accounts or paid services are needed for these public checks.

### Release gate

Create a reviewable PR, retain the existing branch-based Pages deployment, merge the tested head, then verify the matching Pages build, public `/follow/`, raw feed, image files, sitemap, and a real HTTP 404. Re-run the generated-output checker against the live downloads. Refresh both external readers and record their actual results; do not count cached pre-change diagnostics as a new validation.

No Lighthouse, real-user Core Web Vitals or a universal reader-compatibility result is claimed. The practical goal is clear follow instructions, a stable feed, complete content, working image fallbacks and demonstrated parsing by independent reader environments.
