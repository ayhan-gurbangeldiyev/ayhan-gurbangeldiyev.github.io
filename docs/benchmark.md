# Publication benchmark

Inspected 24 October 2026, before implementation. Sources were read through web extraction and direct HTML fetching. These are structural/editorial observations. Reference sites were not tested in mobile emulation, by keyboard, with a screen reader, or with Lighthouse. A viewport tag indicates responsive intent, not proven mobile usability. No design or prose was copied.

## Simon Willison

Sources: [home](https://simonwillison.net/), [tags](https://simonwillison.net/tags/).

The homepage leads with an active dated stream; entries, links, quotes, notes, and guides have separate routes. Short commentary keeps citations adjacent to claims and gives technical images descriptive labels. Search is directly available. Prominent tags make a large archive navigable. HTML advertises Atom at `/atom/everything/`; newsletter is a separate destination. Compact identity and recurring author commentary make the stream recognizably personal. The viewport tag supports mobile intent, but density requires device review. Diagrams are embedded where the subject warrants them rather than required on every entry.

**Apply:** honest publication dates, visible source links, topic discovery, and a useful feed. A one-post publication does not need his volume of content types or navigation.

## Lilian Weng / Lil’Log

Sources: [home](https://lilianweng.github.io/), [Why We Think](https://lilianweng.github.io/posts/2025-05-01-thinking/), [search](https://lilianweng.github.io/search/).

The home introduces a learning-notes identity and provides substantial summaries with reading time, date, and author. Posts, Archive, Search, Tags, and FAQ form a small navigation set. Long articles start with a linked contents outline, have section permalinks, equations and explanatory figures, and end with citations and references. This makes a dense synthesis inspectable. Search has its own page; its result behavior was not tested. HTML advertises RSS at `/index.xml`; viewport metadata and a theme control indicate responsive/theming support, not measured usability.

**Apply:** visible article metadata, navigable long-form writing, primary references and clear distinctions between synthesis and original research. Keep the archive smaller and typography more editorial for this publication.

## Eugene Yan

Sources: [home](https://eugeneyan.com/), [Patterns for Building LLM-based Systems & Products](https://eugeneyan.com/writing/llm-patterns/).

The home separates identity, latest writing, popular writing, talks and projects. Clear Writing/About routes prevent a mixed professional site from obscuring articles. The sampled technical article exposes topic tags and reading time, then organizes a long treatment around practical patterns with diagrams, links and explanations. This links professional identity to verifiable technical work. Email updates are prominent. No feed-autodiscovery link or dedicated search was verified in the fetched homepage; do not infer their absence across the site. Its viewport configuration was observed but not device-tested.

**Apply:** dated editorial rows and article-level taxonomy. Keep experience and project case studies on the existing portfolio rather than repeating them here. Avoid popularity claims without analytics.

## Julia Evans

Sources: [home](https://jvns.ca/), [Moving away from Tailwind, and learning to structure my CSS](https://jvns.ca/blog/2026/05/15/moving-away-from-tailwind--and-learning-to-structure-my-css-/).

The home is a recent-post list followed by a comprehensive category archive. About, talks and projects remain easy to identify. The sampled article uses short, named sections, direct links, concrete code and candid limits on the author's experience; previous/next links aid continued reading. Technical illustration is part of the broader zine identity, though the CSS sample relies primarily on code. HTML advertises Atom at `/atom.xml`; a weekly email digest is also linked. A dedicated search was not verified. Skip navigation and viewport metadata are present; no mobile or assistive-technology audit was performed.

**Apply:** authentic uncertainty, clear examples, semantic CSS components, useful topic navigation and a skip link. Diagrams should clarify the argument rather than imitate the zine style.

## Chip Huyen

Sources: [blog index](https://huyenchip.com/blog/), [Agents](https://huyenchip.com/2025/01/07/agents.html).

The index places dates and article titles first; the main navigation separates blog, books and other work. The sampled Agents article provides a detailed contents outline, an author/date line, an explicit note about its book origin, uncertainty about an emerging field, illustrated concepts and references. That provenance increases confidence without overstating authority. HTML advertises RSS at `/feed.xml`; the footer includes a Substack destination. Search and topic filtering were not verified on the sampled index. A viewport tag and collapsible-navigation input indicate mobile intent; interaction was not tested.

**Apply:** explain article provenance, place limitations near the argument, use meaningful figures and a compact chronological archive. Do not add an email service merely because mature publications have one.

## Shared direction

Prioritize readable writing, sources, contents navigation and durable URLs. Use a front-matter-selected feature, an honest one-post archive, populated topics, and RSS. Add a small local title/summary/topic filter rather than a search service. The visual system is independently drawn: warm paper, plum text, steel-blue links, dusty-rose diagram accents, local system fonts and a restrained graph vocabulary. See `design-spec.md`.
