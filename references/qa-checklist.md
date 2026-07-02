# QA Checklist

Use this before final handoff.

## Source Integrity

- All years, metrics, customers, qualifications, addresses, contacts, and case names come from provided sources.
- Unsupported content is marked `待补充`, `待确认`, or `示例待确认`.
- No fake news, fake customer logos, fake awards, or fake submit-success language.
- Contact/legal/privacy details are either confirmed or visibly pending.

## Business Completeness

- First viewport explains the value in 5 seconds.
- The page includes value, capabilities, evidence, cases/scenarios, process, and conversion.
- Navigation labels match the visible sections or routes.
- CTA text states a concrete action.
- Each card has a title, explanation, and proof/action.

## Visual And Responsive

- Layout aligns to a consistent container and visual axis.
- Typography hierarchy is consistent and readable.
- Palette is brand-appropriate and not one-note.
- Images are relevant, loaded, and not badly cropped.
- Sections have clear boundaries and do not create awkward empty zones or cramped edges.
- Module types fit the content instead of defaulting to repeated card grids.
- Public examples or multi-demo sets differ in hero structure, proof module, section morphology, interaction signature, and footer/conversion path, not only color.
- Premium/client-facing work has a short benchmark record: references studied, design logic borrowed, and what was intentionally different.
- Desktop, tablet, and mobile have no horizontal scroll, overlap, hidden titles, or clipped buttons.
- Fixed navigation does not cover anchor targets.

## Interaction And Accessibility

- Mobile menu opens and closes and exposes `aria-expanded` or equivalent state.
- Buttons, links, tabs, filters, sliders, and forms have hover/focus states.
- Forms have labels or aria-labels and honest feedback.
- Images have meaningful `alt` unless decorative.
- Filters, tabs, calculators, counters, and anchor jumps work after resize and navigation.
- WCAG 2.1 AA is met: skip-to-content link, visible `:focus-visible`, keyboard operability with no focus traps (verified for pinned-scroll, horizontal-wall, and showcase presets), and text contrast at least 4.5:1 (3:1 for large text and UI boundaries).
- `prefers-reduced-motion` triggers a static or simplified fallback for every animated preset.

## SEO And GEO Readiness

- Each public page has a unique title, meta description, canonical URL, and one primary `h1`.
- Important content is readable in the DOM and not hidden behind animation, canvas, or client-only rendering.
- Open Graph/Twitter metadata exists when the page will be shared externally.
- JSON-LD matches visible page content and contains no unsupported organization, address, rating, customer, product, price, or review facts.
- Public pages are not blocked by `noindex`, login, robots rules, or missing crawlable content.
- The handoff states whether sitemap, robots, canonical domain, and structured-data validation are done or pending.

## Performance

- Deployed Core Web Vitals hit target: LCP under 2.5s, CLS under 0.1, INP under 200ms.
- Every image has explicit width/height (or aspect-ratio); below-fold images lazy-load; the hero/LCP image loads eagerly.
- Images are served as WebP/AVIF with a fallback; non-critical scripts are deferred or placed at the end of `<body>`.
- At launch, analytics (if used) is lightweight and privacy-respecting, gated behind a consent banner for EU/UK/CA audiences, excluded from noindex/preview builds, and tracks real conversions only.

## Technical Verification

- Static site: run `python3 <skill-dir>/scripts/audit_static_site.py <site-root> [entry-html]`.
- Public static launch: run `python3 <skill-dir>/scripts/audit_static_site.py <site-root> [entry-html] --strict-seo`.
- Final client delivery: run `python3 <skill-dir>/scripts/audit_static_site.py <site-root> [entry-html] --strict-seo --no-placeholders` after all placeholder content has been resolved.
- React/Vite: run `npm run lint` if present, then `npm run build`.
- Next.js: run typecheck/lint/build commands available in `package.json`.
- Start a local server and inspect desktop and mobile viewports when the site requires runtime rendering.
- Check browser console for errors and missing assets.
- For premium, public example, or client-facing redesigns, capture or inspect screenshots for hero, proof, one mid-page module, footer, and mobile. Resolve obvious alignment, spacing, boundary, cropping, and repeated-template issues before handoff.
- Keep unrelated user changes untouched.
