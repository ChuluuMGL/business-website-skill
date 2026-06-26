---
name: business-website-skill
description: Build client-ready corporate, brand, B2B, service,招商,投标, and proposal-grade business websites from source materials, existing static or React/Vite/Next sites, PPT/PDF/image assets, and reference sites. Use when an agent needs to create, refactor, polish, or QA a business website prototype or launch preview with phased discovery, evidence mapping, sitemap/outline, design direction options, implementation, and delivery checks. Not focused on e-commerce storefronts.
---

# Business Website Skill

## Purpose

Build business websites that are credible enough for client presentation or launch preview. Treat the site as an interactive proposal: clear value, concrete capabilities, source-backed evidence, cases or scenarios, process, and conversion entry points.

## Operating Rules

- Inspect real files and materials before writing copy or code.
- Do not invent qualifications, customers, years, metrics, addresses, contacts, awards, case results, news, or backend submissions.
- Use `待补充`, `待确认`, or `示例待确认` for missing facts while keeping the visual structure complete.
- Keep the existing stack unless the requested delivery shape requires a change.
- Ask for user choice only when the decision materially changes the site. If the user asks to proceed quickly, choose a conservative default and state assumptions.

## Phase Workflow

### Phase 0 - Intake

Collect the minimum context needed to avoid building the wrong site.

If the user has not specified the direction, present 2 to 3 choices:

- Site type: corporate website, brand website, B2B service website, proposal/招商 page, product/project showcase.
- Delivery shape: static HTML/CSS/JS, React/Vite, Next.js, or existing stack.
- Visual direction: restrained B2B trust, data/technology, premium brand, content-led professional.

Checkpoint: summarize selected/defaulted choices and any assumptions.

### Phase 1 - Evidence Map

Read provided websites, docs, PPT/PDF, images, spreadsheets, brand assets, and existing code. Separate facts into:

- Confirmed facts: safe to publish.
- Pending facts: needs user/client confirmation.
- Forbidden assumptions: must not be invented.
- Asset inventory: usable logos, photos, case images, PDFs, videos, icons, and missing assets.

Checkpoint: produce a brief evidence map before implementation when facts are sparse, regulated, or client-facing.

### Phase 2 - Site Blueprint

Design the information architecture before coding.

Include:

- Sitemap or pseudo-page map.
- Homepage section outline.
- Core CTA path.
- Required proof modules.
- Case/scenario taxonomy.
- Contact and form behavior.

Default structure:

1. Header navigation and consultation/contact CTA.
2. Hero with brand/project name, exact value proposition, business summary, proof points, and primary action.
3. Capability entrances with 3 to 6 business/product/service entries.
4. Company/project overview.
5. Business sections with scenario, capability, deliverable, proof, and visual.
6. Evidence metrics, qualifications, certificates, coverage, ROI, or quality proof.
7. Cases, customers, or application scenarios.
8. Service process or delivery workflow.
9. News/insights placeholders only when no real items exist.
10. Contact, map, QR, form, or consultation CTA.

Checkpoint: if the page count, CTA, or business modules are ambiguous, ask the user to choose from 2 to 3 blueprint options.

### Phase 3 - Design Direction

Read `references/style-presets.md` when the user asks for richer styles, trendy design, premium visual directions, or multiple preset looks.
Read `references/preview-guide.md` when the user asks to compare style previews, judge overlap, review visual quality, or inspect GIF interaction previews.

Offer 2 to 3 design directions when brand direction is unclear. Each option should include:

- Tone and audience.
- Layout strategy.
- Color direction.
- Image/visual approach.
- Best-fit use case.

Then implement the selected direction. If the user does not choose, default to a restrained, evidence-led B2B direction.

Read `references/delivery-standards.md` before significant layout, typography, color, image, component, interaction, or responsive decisions.
Read `references/interaction-presets.md` when the user asks for advanced interactions, Anime.js, GSAP, scroll effects, cinematic motion, micro-interactions, or a more current/trendy experience.

### Phase 4 - Implementation Plan

Before major edits, identify:

- File structure and stack entry points.
- Components or sections to create.
- Data/content files to update.
- Asset folders to use.
- Interactions to implement.
- Verification commands.

Use `assets/templates/static-business-site/` for a fast dependency-free starting point. Treat templates as structure only; replace placeholders with source-backed content.

### Phase 5 - Build

Implement narrowly and consistently with the project.

- Static sites: semantic HTML, CSS variables, responsive grids, small JS modules.
- React/Vite/Next: componentized sections, data-driven content, SEO/layout components, route-aware navigation when needed.
- Interactions: sticky navigation, mobile menu, anchor/route behavior, active states, CTA, tabs/filters/calculators/timelines only when useful.
- Forms: honest front-end feedback unless a real backend is connected.

### Phase 6 - QA

Read `references/qa-checklist.md` before final handoff.

Run:

- Static site: `python3 <skill-dir>/scripts/audit_static_site.py <site-root> [entry-html]`.
- React/Vite: `npm run lint` if present, then `npm run build`.
- Next.js: available typecheck/lint/build commands.

When possible, start a local server and inspect desktop and mobile. Verify no horizontal scroll, overlap, broken anchors, missing assets, fake facts, or false submit-success behavior.

### Phase 7 - Handoff

Final response should include:

- What changed.
- Where files are.
- How to run or preview.
- What validation passed.
- Any unresolved `待补充` or client-confirmation items.

## Reference Routing

- Read `references/example-patterns.md` when deciding architecture or reusable modules from prior project patterns.
- Read `references/benchmark-patterns.md` when improving strategy, conversion, trust, B2B buyer support, or overall maturity.
- Read `references/style-presets.md` when selecting a visual preset or combining multiple premium website styles.
- Read `references/interaction-presets.md` when selecting animation libraries, motion recipes, or interaction intensity.
- Read `references/preview-guide.md` when evaluating visual/interaction preset quality, overlap, or preview assets.
- Read `references/delivery-standards.md` before significant visual or responsive work.
- Read `references/qa-checklist.md` before final handoff or review.

## Public Safety

- Do not store client-private facts, contact details, credentials, `.env` values, server IPs, or deployment secrets in this skill.
- Keep templates generic and placeholder-based.
- Keep unsupported metrics as pending or unavailable; never convert unknown values to `0`.
