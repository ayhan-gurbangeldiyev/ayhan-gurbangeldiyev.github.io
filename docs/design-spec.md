# Engineering Notes — design specification

## Identity and information architecture

**Ayhan Gurbangeldiyev — Engineering Notes**. Descriptor: “Field notes on building reliable AI systems.” The publication's subject is reliable and observable AI systems in practice. It offers decisions and evidence; the portfolio offers professional history and case studies.

Routes: `/`, `/writing/`, `/topics/`, `/about/`, existing article URL, `/feed.xml`, `/sitemap.xml`, `/404.html`. Header links to writing, topics, about, portfolio and RSS. Footer exposes only portfolio-verified professional/contact destinations. Topics use real article data with stable fragments; unpopulated topics have no public section or page.

25 October follow-up: the AG masthead mark is replaced with an explicit Home control. GitHub, LinkedIn, Portfolio, Email and RSS / Atom form a labeled icon row directly below the masthead and are repeated in the footer. These are local, attributed SVG icons rather than remote favicon requests. The browser/search favicon is a separate original document/graph mark with PNG and touch-icon exports.

Home order: compact masthead → short thesis and conceptual feedback-loop figure → front-matter-selected feature → latest notes → populated topics → short author introduction. One real post may appear in both the feature and chronological archive; no invented cards or unpublished backlog entries are displayed.

## Visual tokens

| Role | Light | Dark |
| --- | --- | --- |
| Background | `#f8f6f2` | `#171419` |
| Text | `#171419` | `#f2edf1` |
| Secondary text | `#625d65` | `#b8aebc` |
| Links | `#365d78` | `#9cbfd9` |
| Accent | `#d6b0c4` | `#d6b0c4` |

Rose is primarily a diagram/surface accent, not small text on light paper. System sans-serif fonts avoid remote font downloads. Monospace is reserved for dates, figure identifiers, small metadata and code. Main shell: 1160px maximum; prose: 72ch maximum, approximately 17px / 1.85 line height. Hero uses a restrained text size with an accompanying meaningful diagram rather than a full-screen marketing composition.

At small widths: masthead wraps, navigation remains visible without a menu script, columns stack, contents navigation moves above the article, and code/tables can scroll independently. Diagram links open original accessible SVGs for close inspection. All figures include text equivalents.

## Interaction and accessibility

System theme is the default. A native select chooses System/Light/Dark; an explicit preference is applied before CSS and persists locally. With storage blocked, the current-page choice works. Without JS, system theme, full navigation, contents links, all writing, footnotes and figures remain available. JS adds heading permalink controls and the writing filter; hidden controls are revealed only once functional.

Use one h1 per document, semantic landmarks, descriptive navigation labels, a keyboard skip link, visible focus, reserved image dimensions, reduced-motion handling and no animation dependency. Links open in the same tab, avoiding unannounced new windows. There is no tracking, autoplay, external font, JS framework, or subscription form.

## Article conventions

Title, summary, author, original date, computed reading time, real topics; meaningful updates only via `last_modified_at`. Kramdown renders code and footnotes. Contents are generated from rendered h2 headings on the server; heading links are progressively enhanced. The related section appears only for other posts sharing a topic. The current post has no fake related cards. References and original AI-assisted disclosure stay visible.

Technical SVGs intentionally use a self-contained light canvas for predictable contrast across feed readers and site themes. Social PNGs are rasterized from original SVG masters for broad crawler compatibility.
