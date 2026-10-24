# Portfolio writing inventory and migration plan

Audit date: 24 October 2026. Sources: [portfolio homepage](https://ayhangurbangeldiyev.com/), [writing archive](https://ayhangurbangeldiyev.com/writing), [published sitemap](https://ayhangurbangeldiyev.com/sitemap.xml), and the linked English article responses. Four English articles and four corresponding Turkish article routes are discoverable. This is the public sitemap/archive inventory; it does not claim access to unpublished or unlinked content.

| Existing English article | English route | Turkish route | Published date shown on home |
| --- | --- | --- | --- |
| Loop and Harness Engineering: The Work Around the Model | `/writing/loop-and-harness-engineering` | `/tr/yazilar/loop-ve-harness-muhendisligi` | 24 October 2026 |
| Graph Engineering: Giving Agentic Systems a Shape | `/writing/graph-engineering-for-ai-agents` | `/tr/yazilar/graf-muhendisligi` | 24 October 2026 |
| Agentic Reverse Engineering: What Changes and What Does Not | `/writing/agentic-reverse-engineering` | `/tr/yazilar/ajanlarla-tersine-muhendislik` | 24 October 2026 |
| Designing Agentic Systems: Principles for AI That Acts | `/writing/designing-agentic-systems` | `/tr/yazilar/agentic-sistem-tasarimi` | 1 June 2026 |

All routes above are on `https://ayhangurbangeldiyev.com`. English article HTML was fetched. Turkish routes were discovered from the sitemap; their prose and language metadata were not audited. The web reader returned cache misses for the Graph and Reverse Engineering pages; direct HTTPS HTML fetches succeeded. Cached reader output for the older Designing article differed from the current homepage chrome; use live source metadata at migration time.

The Pages publication has a different article: [Before Adding a Second Agent](https://ayhan-gurbangeldiyev.github.io/writing/before-adding-a-second-agent/), published 5 September 2026. Related subject matter alone is not duplicate content. No portfolio article was copied or migrated in this change.

## Current state: keep independent originals

Keep the current originals on their current domains with self-canonicals. Future original technical articles should first publish on Engineering Notes. The portfolio can carry a short, genuinely distinct summary and link to the original; it should not mirror the full article. If existing canonicals on `.com` are inaccurate, fix them in a separately authorized change to that repository. This PR cannot change another site's canonical directives.

## Optional later migration: one URL per language, one original per article

1. Obtain authority to edit/deploy the `.com` repository. Export full content, metadata, diagrams and redirects before changes; record checksums and all existing URL variants. Recheck the inventory and existing canonicals live.
2. Choose destination slugs explicitly, for example `/writing/loop-and-harness-engineering/`. Preserve original publication dates, original author/provenance, disclosure and reference links. Set a substantive update date only when warranted.
3. Publish the reviewed version on Pages with a self-canonical. Create a **one-to-one HTTP 301 or 308 redirect** on `.com` from each old article route and its observed variants to that exact article. Do not redirect every article to the homepage or archive. Test headers, no loops, all fragments and assets; keep redirects long-term.
4. If server-level redirects are unavailable, prefer keeping the original until a viable migration exists. For necessary syndication, place an absolute cross-domain canonical on the duplicate pointing to the chosen original, plus a visible attribution link. Canonical is a hint, not a guaranteed redirect or indexing outcome. Avoid simultaneously placing both a contradictory canonical and redirect on a source page.
5. Treat Turkish translations as distinct language variants. If moved, retain real Turkish content at an explicitly chosen route with its own canonical and reciprocal `hreflang` to the English counterpart (plus `x-default` if appropriate). Do not canonicalize translations to English solely to consolidate domains; do not redirect Turkish readers to untranslated English without an explicit decision.
6. Update portfolio summary links, internal references, both sitemaps, any syndication metadata and social links. Validate 200/301 results and crawlability. Submit each changed sitemap in its verified Search Console property; monitor old URLs and indexing before removal.

## Decisions needed before a separate migration

- Move any of the four existing articles, or keep them as legacy originals?
- Preserve Turkish articles on `.com`, or introduce maintained translated routes here?
- Which host capabilities provide real HTTP redirects on `.com`?
- Which existing Medium material, if any, is an intentional syndication? Account/editor access would be needed to check or set those article canonicals; no claim of that audit is made here.

No migration decision is required to review this redesign. No redirects, duplicated articles or changes to `.com` are included.
