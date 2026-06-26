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
- Desktop, tablet, and mobile have no horizontal scroll, overlap, hidden titles, or clipped buttons.
- Fixed navigation does not cover anchor targets.

## Interaction And Accessibility

- Mobile menu opens and closes and exposes `aria-expanded` or equivalent state.
- Buttons, links, tabs, filters, sliders, and forms have hover/focus states.
- Forms have labels or aria-labels and honest feedback.
- Images have meaningful `alt` unless decorative.
- Filters, tabs, calculators, counters, and anchor jumps work after resize and navigation.

## SEO And GEO Readiness

- Each public page has a unique title, meta description, canonical URL, and one primary `h1`.
- Important content is readable in the DOM and not hidden behind animation, canvas, or client-only rendering.
- Open Graph/Twitter metadata exists when the page will be shared externally.
- JSON-LD matches visible page content and contains no unsupported organization, address, rating, customer, product, price, or review facts.
- Public pages are not blocked by `noindex`, login, robots rules, or missing crawlable content.
- The handoff states whether sitemap, robots, canonical domain, and structured-data validation are done or pending.

## Technical Verification

- Static site: run `python3 <skill-dir>/scripts/audit_static_site.py <site-root> [entry-html]`.
- Public static launch: run `python3 <skill-dir>/scripts/audit_static_site.py <site-root> [entry-html] --strict-seo`.
- React/Vite: run `npm run lint` if present, then `npm run build`.
- Next.js: run typecheck/lint/build commands available in `package.json`.
- Start a local server and inspect desktop and mobile viewports when the site requires runtime rendering.
- Check browser console for errors and missing assets.
- Keep unrelated user changes untouched.
