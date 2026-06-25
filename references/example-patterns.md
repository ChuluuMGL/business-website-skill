# Example Patterns

Use these patterns as reusable lessons from the inspected local websites. Do not copy their facts, palettes, or client-specific content into new projects.

## Static Proposal Website Pattern

Observed in a local industrial B2B static proposal site:

- Files: `index.html`, `index.css`, `index.js`, local image assets.
- Structure: fixed header, top strip, desktop navigation, mega menu, mobile panel, hero, capability gateway, summary, business matrix, dashboard, ROI estimator, proof cards, news, contact, pseudo multi-page sections.
- CSS: root variables, `--max: 1200px`, consistent container width, `scroll-margin-top`, `overflow-x: hidden`, responsive grids, fixed header state.
- JS: active nav, hash navigation, pseudo page switching, mobile menu `aria-expanded`, solution tabs, case filters, counters, ROI slider/input, reveal observer, toast feedback.
- Best use: high-completion static prototype or client preview that should open with a browser or simple static server.

Reusable takeaways:

- Use a hero proof panel next to the value proposition when the client has strong numbers.
- Add a gateway section after hero so clients can scan the business in 3 to 6 entries.
- Use pseudo pages when the client expects an enterprise navigation map but delivery speed favors one HTML file.
- Use calculators and dashboards only when they connect to a real business decision.

## React Company Website Pattern

Observed in a local React company website project:

- Stack: Vite, React, TypeScript, Tailwind, `motion`, `lucide-react`, router, SEO component, local i18n JSON, contact modal context.
- Home composition: `SEO`, `Hero`, `Stats`, `Services`, `LogoMarquee`.
- Navigation: route-aware navbar, desktop dropdowns, external product links, language switch, contact modal, mobile menu.
- Content system: pages for services, methodology, reports, products, cases, learning, about, legal pages.
- Assets: public images and optimized variants.

Reusable takeaways:

- Use component composition when the site will grow beyond one page.
- Put repeated business content into data/localization files rather than hard-coding long copy across components.
- Add SEO schema and legal pages when a company site is intended for public launch.
- Keep contact modal and CTA behavior consistent across pages.

## Conversion-Focused Creative/Service Site Pattern

Observed in a local conversion-focused creative service website project:

- Stack: Vite, React, TypeScript, Tailwind, `motion`, `lucide-react`.
- Navigation emphasizes service pricing, account diagnosis, AI vision, matrix marketing, and reports.
- Hero uses strong CTA choices: explore quote/service package and free diagnosis.
- Mobile menu mirrors the desktop conversion paths.
- Rich motion and dark visual style are acceptable only when the brand and offer support it.

Reusable takeaways:

- Put the highest-value conversion route in the first screen and navigation.
- Service websites benefit from pricing/diagnosis/report entrances when those are real deliverables.
- Strong visual motion must not reduce readability or business clarity.

## Common Modules To Reuse

- Proposal hero with proof metrics and primary CTA.
- Business gateway with 3 to 6 capability entries.
- Evidence section with qualifications, case count, delivery scope, or metrics.
- Service/capability matrix with scenario, capability, deliverable, proof.
- Case grid with category filters.
- Process timeline or service system.
- ROI, savings, diagnosis, or quote calculator if source logic exists.
- Contact block plus honest form behavior.
- Footer with legal, contact, social/QR, and sitemap links.

## Common Failure Modes

- Treating the site as a visual poster instead of a business proposal.
- Copying a dark or gradient-heavy tech aesthetic into an industrial, government, energy, or B2B site where trust needs restraint.
- Using fake customers, fake news, fake numbers, or fake backend submission.
- Leaving desktop-only navigation, broken anchors, or mobile horizontal overflow.
- Shipping cards that have titles but no evidence, deliverable, scenario, or action.
