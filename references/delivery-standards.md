# Delivery Standards

Use this reference when building or polishing client-facing business websites. The focus is corporate, brand, B2B, service, proposal,招商,投标, and project showcase websites, not e-commerce storefronts.

## Information Architecture

Default structure:

1. Header navigation: logo, main sections, consultation/contact button.
2. Hero: brand or project name, value proposition, business summary, proof metrics, primary CTA.
3. Capability entrances: 3 to 6 products, services, scenarios, or capabilities.
4. Overview: positioning, service range, team, qualification, or operating model.
5. Business sections: each section includes scenario, capability, deliverables, proof, and image/diagram.
6. Proof: metrics, certificates, coverage, ROI, efficiency, quality, or delivery results.
7. Cases/scenarios: classify by industry, region, product, stage, or outcome.
8. Service process: timeline, steps, responsibility split, deliverables, or after-sales model.
9. News/insights: use real items only. If no source exists, create a structural placeholder.
10. Contact/conversion: phone, email, address, QR code, map, form, consultation CTA.

## First View

The first viewport must answer these in 5 seconds:

- Who is this?
- What does it do for customers?
- Why should customers believe it?
- What should customers do next?

Include a relevant image or visual system. Do not ship a decorative cover that hides the business.

## Layout

- Use a 12-column or equivalent grid.
- Desktop max width: 1120 to 1280px, commonly 1200px.
- Horizontal padding: desktop 48px, tablet 32px, mobile 20 to 24px.
- Section spacing: desktop 80 to 120px, compact sections 56 to 72px, mobile 48 to 64px.
- Align headings, copy, cards, media, and buttons on consistent visual axes.
- Card radius: 6 to 10px unless the existing system differs.
- Avoid cards nested inside cards and avoid floating-card page sections.

## Typography

- Chinese: `Noto Sans SC`, `PingFang SC`, `Microsoft YaHei`, system sans.
- English/numbers: `Inter`, `Arial`, system sans.
- Letter spacing: default 0. Avoid negative tracking.
- Desktop H1: 44 to 64px, line-height 1.08 to 1.18, weight 700 to 900.
- Desktop H2: 32 to 46px, line-height 1.15 to 1.25, weight 700 to 800.
- Desktop H3: 20 to 26px, line-height 1.25 to 1.35, weight 700.
- Body: 15 to 17px, line-height 1.65 to 1.85.
- Labels/dates: 12 to 13px, readable muted color.
- Button text: 14 to 15px, weight 700 to 800.
- Mobile H1: 28 to 36px. Mobile H2: 24 to 32px. Mobile body: 14 to 16px.

Text must not overflow, overlap, or hide behind fixed navigation.

## Color

- Choose colors from brand and industry context.
- Default background: white or very light neutral.
- Main text: deep neutral such as `#10211c`, `#17211d`, or `#1f2933`.
- Secondary text: readable neutral gray/blue/green.
- Primary color: one stable brand color for CTA, icons, data, and emphasis.
- Accent colors: at most 2 to 3 for categories, charts, or states.
- Lines: low-saturation 1px borders.
- Shadows: light and low-opacity, only for navigation, overlays, or priority cards.

Avoid a one-color palette, cheap purple-blue gradients, neon, large dark areas without reason, and decorative light blobs.

## Images And Visuals

- Use real relevant images where possible: product, plant, team, case, equipment, office, site, dashboard, or result.
- Hero image must relate directly to the business and preserve text readability with a mask/overlay if text sits on it.
- Stable ratios: hero 16:9 or full-bleed, card images 4:3, 16:10, or 3:2.
- Use `object-fit: cover`, but do not crop away the important subject.
- Keep icon style consistent: line or solid, not mixed.
- Visuals should explain: capability map, process axis, metric cards, case filters, network map, ROI calculator, or comparison table.

## Components

- Navigation: sticky/fixed, readable after scroll, mobile hamburger, active states, no content obstruction.
- Buttons: primary brand color, secondary outline/light. Desktop height 42 to 48px, mobile at least 40px.
- Cards: title, explanation, proof point or CTA. Unified height, gap, radius, and hierarchy.
- Metrics: large number, clear unit, small readable label. Mark unconfirmed data as sample or pending.
- Timelines/processes: aligned axis and nodes. Switch to single column on mobile.
- Forms: 3 to 6 fields, labels or aria-labels, accessible states, honest feedback.

## Interaction

- Use light business-grade interaction: scroll reveal, count-up, tabs, filters, anchor jumps, ROI calculator, mobile menu.
- Duration: 160 to 520ms. Avoid bouncy or distracting motion.
- Provide hover/focus states. Use `aria-expanded` for menus, image `alt`, and form labels.
- Anchor jumps must account for fixed header height with `scroll-margin-top` or JS offset.

## Accessibility

Target WCAG 2.1 AA as the baseline for any public or client site.

- Provide a "skip to main content" link as the first focusable element.
- Keep every interaction operable by keyboard: logical tab order, visible `:focus-visible` styles, and no widget traps focus. This is mandatory for pinned-scroll, horizontal-wall, and showcase motion presets — verify Tab and Escape can leave them.
- Color contrast: at least 4.5:1 for body text and 3:1 for large text and UI boundaries. Do not rely on color alone to signal state.
- Use landmark elements (`header`, `nav`, `main`, `footer`) with one clear label per region.
- Respect `prefers-reduced-motion` with a static or simplified fallback for every animated preset.
- Never hide primary content, proof, or CTAs behind canvas, WebGL, or scroll-linked animation — keep them in the DOM and readable by assistive tech.
- Images and icons carry meaningful `alt` or labels; purely decorative ones use `alt=""`.

## Performance Budget

Target Core Web Vitals on the deployed site: LCP < 2.5s, CLS < 0.1, INP < 200ms.

- Set explicit `width` and `height` (or `aspect-ratio`) on every image so the page reserves space and CLS stays near zero.
- Lazy-load below-the-fold images (`loading="lazy"`); load the hero/LCP image eagerly.
- Serve modern formats via `<picture>`: WebP/AVIF source with a PNG/JPEG fallback, and keep hero assets small.
- Defer or `async` non-critical scripts, and place analytics and motion scripts at the end of `<body>` so they never block first paint.
- Cap JavaScript for showcase motion (Three.js, GSAP, shaders): load it only on pages that use it, with a reduced-motion and no-JS fallback.
- Keep the LCP element (usually the hero) free of render-blocking CSS/JS and avoid layout-thrashing animation.

## Responsive

- At 1100px and below: reduce multi-column grids to two or one columns.
- At 720px and below: core content becomes single column and navigation becomes mobile menu.
- At 480px and below: buttons may become full width, media heights shrink, long titles wrap cleanly.
- No horizontal scroll on mobile.

## Copy

- Write like a business proposal, not an ad slogan.
- Each section answers one question: who, problem, capability, proof, process, action.
- Avoid empty phrases such as `行业领先`, `卓越品质`, `赋能未来` unless the source provides proof.
- Keep source-derived numbers, years, qualifications, customers, and cases exact.

## Code

- Use the existing stack and conventions.
- For static sites, keep semantic HTML, CSS variables, and small JS modules.
- For React/Vite/Next, separate data, components, pages/routes, SEO, and layout.
- Put assets in clear folders such as `assets/brand/`, `assets/cases/`, `assets/official/`, or `public/images/`.
- Do not reference missing images.
- Check console errors, broken links, image loading, mobile menu, anchors, form feedback, and responsive layout.

## SEO And GEO

- Use one descriptive title and meta description per indexable page.
- Keep important claims and summaries in crawlable text, not only images, canvas, or animation.
- Add canonical, Open Graph, Twitter Card, sitemap, robots, and structured data when the site is intended for public launch.
- Use JSON-LD only for facts visible on the page and confirmed by source materials.
- For private preview links, use `noindex` or access control; remove those controls before public launch.
- Keep AI-search/GEO readiness evidence-based: specific claims, useful summaries, clear headings, proof near claims, and no hidden keyword text.

## Analytics And Privacy

Add measurement only when the site is going live, and keep it honest.

- Prefer lightweight, privacy-respecting analytics (Plausible, Umami, Fathom) for marketing sites; use GA4 when the client already relies on it.
- Show a consent banner before loading tracking scripts when the audience includes EU/UK (GDPR) or California (CCPA) visitors; respect opt-outs and store consent.
- Track real business events (consultation submit, download, primary CTA), not vanity scrolls, and never send PII beyond what the visitor explicitly submitted.
- Exclude analytics from preview/noindex builds so staging traffic is not counted as production.
- Record the chosen tool, cookie/no-cookie behavior, and consent model in the handoff.
