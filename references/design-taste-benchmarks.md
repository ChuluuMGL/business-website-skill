# Design Taste And Benchmark Guide

Use this reference before creating public examples, premium visual directions, client-facing redesigns, or any website where the user asks for advanced, elegant, distinctive, high-taste, or non-generic design.

The goal is not to copy templates. The goal is to study proven patterns, extract the design logic, then adapt it to the client's real industry, evidence, assets, and conversion path.

## External References To Study

These references are examples of useful design or skill behavior. Use them as benchmark sources, not as content sources for client facts.

| Reference | What To Learn | Link |
|---|---|---|
| Anthropic `frontend-design` skill | Distinctive visual point of view, subject-specific design, one justified aesthetic risk, self-critique before code. | https://github.com/anthropics/skills/blob/main/skills/frontend-design/SKILL.md |
| `guizang-ppt-skill` | Opinionated style systems, constrained layouts, theme selection, visual preflight, validation scripts, previewable examples. | https://github.com/op7418/guizang-ppt-skill |
| `frontend-slides` | Show-don't-only-tell previews, compact style metadata, progressive disclosure, anti-generic constraints, and visual validation before final output. | https://github.com/zarazhangrui/frontend-slides |
| Zara Zhang deck site | Named visual system, signature graphic language, strong typography, evidence/card framing, and mobile identity preservation. | https://deck.zarazhang.com/ |
| ScrewFast | Astro/Tailwind business-site structure, product/service pages, docs/blog integration, SEO and content architecture. | https://github.com/mearashadowfax/ScrewFast |
| AstroWind | Production-ready Astro site architecture, SEO metadata, blog/resource sections, sitemap and responsive best practices. | https://github.com/onwidget/astrowind |
| Cruip Simple Light | SaaS and online-service landing-page rhythm, clear hero, sections, CTA hierarchy, and minimal React/Next implementation. | https://github.com/cruip/tailwind-landing-page-template |
| Launch UI | Modern Next/shadcn/Tailwind component families, hero variants, nav variants, stats, FAQ, CTA, footer, responsive components. | https://github.com/launch-ui/launch-ui |
| Page UI | Landing-page section patterns and conversion-oriented component blocks. | https://github.com/PageAI-Pro/page-ui |

When live research is available, verify current licenses, demos, and repository activity before borrowing implementation ideas. Do not copy brand assets, logos, screenshots, testimonials, copy, or unverified claims.

## Benchmark-First Workflow

For premium or public-facing work, add this gate between Phase 2 and Phase 3.

1. Define the design job.
   - Website type, audience, conversion goal, industry expectations, content depth, and asset quality.
   - One sentence for what the site must make the visitor believe or do.

2. Select 2 to 3 benchmarks.
   - At least one benchmark should match the industry or buying context.
   - At least one benchmark should match the desired layout or interaction quality.
   - At least one benchmark may be aspirational, but it must be adaptable with available assets.

3. Extract the design logic.
   - Header strategy: fixed, floating, editorial, mega-menu, command-bar, utility-first, or minimal.
   - Hero strategy: split product proof, full-bleed media, editorial statement, dashboard preview, technical diagram, case-led opening, or interactive demo.
   - Section morphology: grids, ledgers, split essays, timeline, tabs, bento, case wall, proof library, comparison table, map, calculator, or dossier.
   - Visual language: type pairing, spacing rhythm, image treatment, border/radius/shadow policy, color role, and proof emphasis.
   - Interaction signature: one or two purposeful interactions, not a page-wide generic reveal.

4. Write a divergence contract before coding.
   - Name what to borrow from each benchmark.
   - Name what not to copy.
   - Name how the output will differ from the skill's other demos.
   - Name the one memorable signature element.

5. Build from the contract.
   - Use the project's stack and assets.
   - Replace template facts with source-backed client facts.
   - Keep the benchmark visible as a quality reference, but do not clone it blindly.

6. Screenshot review before handoff.
   - Capture desktop and mobile screenshots at the hero, proof, one mid-page module, and footer.
   - Check alignment, spacing, boundaries, text wrapping, image cropping, and whether modules feel distinct.
   - If screenshots reveal blank zones, cramped boundaries, or repeated card grids, fix the layout before handoff.

## Taste Gate

Before writing code, create a compact taste plan:

```text
Subject:
Audience:
Page job:

Palette:
Type:
Layout concept:
Signature element:
Motion signature:

Borrowed from:
Avoiding:
Distinct from other demos by:
```

Reject the plan if it could be reused unchanged for a different industry. A water-treatment engineering website, an AI SaaS launch page, and a B2B service consultancy must not share the same hero structure, card rhythm, proof module, motion pattern, and footer shape.

For higher-stakes work, replace the compact taste plan with the full visual-system canvas in `references/visual-system-discovery.md`. A preset such as `ai-saas-data-cloud` or `industrial-precision` is not enough by itself. The selected direction needs a name, layout grammar, proof treatment, signature element, motion signature, and mobile behavior.

## Website Lessons From Deck References

Presentation and slide-system references can raise taste, but their logic must be adapted to responsive websites.

- Keep the "show, do not only tell" habit: when the user is comparing styles, create previewable systems, not abstract adjectives.
- Use a signature element that carries meaning: chroma bands, evidence ledgers, process rails, command surfaces, or case boards.
- Treat proof as design material: reports, certificates, dashboards, case photos, and source labels should be framed intentionally, not dropped into generic cards.
- Preserve identity on mobile: the responsive version should keep the signature element, not collapse into indistinguishable stacked cards.
- Do not copy fixed 16:9 slide staging into a website. Convert it into scroll-native sections, flexible containers, and breakpoints.

## Anti-Generic Rules

Avoid these defaults unless the benchmark and brief justify them:

- Centered hero, gradient background, three feature cards, logo strip, CTA band.
- Same header, same hero split, same card grids, same three proof cards across multiple demos.
- Decorative numbered chips when content is not a real sequence.
- Fake dashboards, fake metrics, fake customer logos, or fake testimonials.
- Generic `fade-up` on every section.
- Oversized empty zones under cards or beside visuals.
- Large low-contrast dark sections that reduce readability.
- Image panels that fight with copy or make text overlap.

## Distinctiveness Matrix

For a multi-demo site or template set, each demo must differ on at least 5 of these 9 axes:

1. Navigation structure.
2. Hero composition.
3. Section morphology.
4. Proof module.
5. Visual asset treatment.
6. Typography role.
7. Color role and density.
8. Interaction signature.
9. Footer and conversion path.

If two demos only differ in color, copy, and icon choices, they are the same design family and should be redesigned.

## Reference Mapping By Website Type

### B2B Service / Consulting

- Useful references: AstroWind, Cruip Simple Light, Page UI, selected agency/case-study sites.
- Borrow: clear service map, role-based paths, proof dossier, consulting process, FAQ, resource center.
- Distinct modules: operating dossier, service packages, evidence ledger, stakeholder paths.
- Interaction: service tabs, sticky consultation rail, case filter, process stepper.

### Industrial / Engineering / Green Tech

- Useful references: ScrewFast, technical product docs, engineering company sites, real project pages.
- Borrow: technical credibility, product/service pages, docs-like clarity, specification tables.
- Distinct modules: process line, equipment/spec matrix, compliance proof, project lifecycle, map or site conditions.
- Interaction: SVG process line draw, hotspot tour on equipment/site images, before/after comparison.

### AI SaaS / Data / Automation

- Useful references: Launch UI, Cruip, product-led SaaS examples, dashboard/product docs.
- Borrow: product proof, dashboard-led hero, integrations, workflow, FAQ, pricing/CTA readiness.
- Distinct modules: command center, agent workflow map, evidence boundary, integration orbit, launch preview.
- Interaction: dashboard panel sequence, shared-layout feature explorer, scroll-scrub product states.

### Premium Brand / Editorial / Creative

- Useful references: editorial portfolios, creative studios, high-end service pages.
- Borrow: typographic rhythm, image-led narrative, selected work, manifesto, restrained CTAs.
- Distinct modules: editorial essay sections, image mask reveal, case wall, studio process, selected proof.
- Interaction: image reveal, horizontal case wall, magnetic media hover, page transition.

## Layout Quality Rules

- Every section needs a clear boundary: background band, rhythm break, heading block, grid change, or media shift.
- Avoid hidden empty gaps. Whitespace must frame content; it must not look like a missing module.
- Visual panels and text blocks must share a baseline or an intentional offset.
- If a section has two columns, the taller column should not create an awkward blank rectangle in the shorter column.
- Cards should not be the default solution for every concept. Use ledgers, diagrams, timelines, split essays, comparison tables, media rows, and maps when they fit better.
- A demo with only synthetic illustrations must still feel industry-specific through structure, terminology, and proof placement.

## Motion Quality Rules

- Give each site one motion signature. Examples: dashboard morph, process line draw, case wall, image mask reveal, hotspot tour.
- Use generic reveal only as supporting motion.
- Motion must communicate sequence, product state, content relationship, or user feedback.
- If the motion would be just as suitable for any other website, it is probably not the signature.
- Always provide reduced-motion behavior and verify that content remains readable without JavaScript.

## Implementation Notes

- When adapting open-source templates, respect their licenses and attribution requirements.
- Prefer learning patterns over copying files.
- If copying code is allowed and useful, keep copied sections small, cite the source in comments or documentation where appropriate, and replace demo assets/copy.
- Do not introduce a heavy framework just to imitate a template if the current project is a simple static site.
- A benchmark can guide a static implementation even when the source template uses Astro, Next, or React.

## Handoff Evidence

For public examples and premium client work, include this in the final handoff:

- Benchmarks reviewed.
- Design logic borrowed.
- What was intentionally different.
- Screenshots or viewport checks performed.
- Remaining design risks, if any.
