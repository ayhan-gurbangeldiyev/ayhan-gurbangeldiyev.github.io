# Publishing checklist

## Evidence and editorial quality

- [ ] The problem, audience, constraints and article type are clear.
- [ ] Original observations, external research, examples and opinions are distinguishable.
- [ ] Every number has its context and source; baseline, model/tool versions and budgets are specified where applicable.
- [ ] No invented experience, experiment, benchmark or incident. Unrun experiments are proposals.
- [ ] Relevant failure modes, uncertainty and trade-offs are explained.
- [ ] Primary references open and support the claims; meaningful AI assistance is disclosed.
- [ ] Reproduction details, fixture/data provenance and code commits are included when needed.

## Metadata and presentation

- [ ] Filename date and original publication date agree; stable explicit permalink chosen.
- [ ] Title and summary are unique, useful and free of keyword padding.
- [ ] The introduction answers a real reader question with appropriate conditions; the original contribution and evidence type are clear. No fixed word count, forced FAQ or AI-specific rewriting is required.
- [ ] One or more real topic IDs from `_data/topics.yml`; article type is correct.
- [ ] Only deliberate featured choices; do not add artificial related content.
- [ ] `last_modified_at` is absent unless there was a meaningful content update.
- [ ] Canonical points to the intended original. Check `.com`/Medium overlap before publishing a copy.
- [ ] English pages use `lang: en`; translations need real translated content and a separate migration/localization review.
- [ ] Figures have text alternatives, intrinsic dimensions, captions, sources and licenses.
- [ ] Social image is a real 1200×630 PNG, with `image.alt` and a matching editable master when authored here.
- [ ] Long posts have useful h2 headings and contents navigation. Code language is specified; footnotes work.

## Validation and release

- [ ] `bundle exec jekyll build --safe --strict_front_matter` succeeds.
- [ ] `python3 scripts/check_site.py _site` succeeds (links, images, feed, sitemap, metadata).
- [ ] Desktop/mobile and light/dark reviewed, keyboard focus and skip link checked.
- [ ] RSS entry has correct URL, publication date, author and meaningful content.
- [ ] Any moved URL has a tested redirect plan and a recorded owner decision.
- [ ] Pull request reviewed before merging; a merge to `main` triggers existing Pages publishing.
- [ ] After production deploy, check article, feed, sitemap, social-image URLs and Search Console if authorized.
- [ ] Review actual indexing/canonicals and the account's generative AI inclusion setting; consult Search Console Generative AI and Bing AI Performance when sufficient data exists. Follow `search-visibility-2026.md`; do not claim indexing or citations from deployment alone.
