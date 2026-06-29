# Preview Guide

Use this guide when reviewing whether the built-in style and interaction presets are visually useful, distinct enough, and practical for client-facing business websites.

## Preview Assets

- Hosted preview release: `https://github.com/ChuluuMGL/business-website-skill/releases/tag/preview-assets-v1.3.0`
- Hosted style overview: `https://github.com/ChuluuMGL/business-website-skill/releases/download/preview-assets-v1.3.0/style-overview.png`
- Hosted AI concept moodboard: `https://github.com/ChuluuMGL/business-website-skill/releases/download/preview-assets-v1.3.0/ai-style-moodboard.jpg`
- Local preview note: `assets/previews/README.md`
- Regeneration script: `scripts/generate_preview_assets.py`

The generated style overview is deterministic and should stay close to the machine-readable presets. The AI concept moodboard is only a visual mood reference and should not be treated as a template or factual website output.

Preview PNG/GIF/JPG files are human-facing documentation assets hosted outside the main tree. Agents should use the markdown references, JSON preset catalogs, scripts, and templates; they do not need to load binary previews into context to execute the workflow.

## Skill UX Audit Summary

Current strengths:

- Clear staged workflow from intake to handoff.
- Strong public-safety rules against fake facts, fake metrics, and private data leakage.
- Practical style families for common business website categories.
- Machine-readable presets and preview assets for cross-agent use.
- Benchmark-first quality gate for public examples, premium redesigns, and high-taste client-facing work.

Improvements added in v1.2.0:

- Add `standard`, `premium`, and `showcase` motion tiers so "more cool" does not automatically mean over-animated.
- Add `references/agent-experience.md` for mode selection, minimal questions, checkpoints, and final handoff behavior.
- Add showcase interaction GIFs for high-impact work while preserving reduced-motion and fallback rules.
- Separate deterministic previews from AI concept moodboards so users can judge both implementation feasibility and visual ambition.

## Style Overlap Review

Some overlap is intentional because real client websites often combine a primary style with a secondary modifier. Use the difference in business context, evidence modules, and interaction intensity to keep them distinct.

| Similar Presets | Real Difference |
|---|---|
| `executive-b2b-trust` vs `fintech-secure` | Executive B2B is broad professional trust; fintech needs risk, compliance, security, and product proof. |
| `industrial-precision` vs `sustainable-green-tech` | Industrial focuses on engineering, equipment, certificates, and process; green tech focuses on impact, compliance, and environmental outcomes. |
| `ai-saas-data-cloud` vs `dark-data-command-center` | AI SaaS can be light and product-led; dark data should feel operational, monitoring-heavy, and data-dense. |
| `premium-editorial-brand` vs `minimal-luxury` | Editorial is narrative and content-led; minimal luxury is quieter, image-led, and selective. |
| `premium-editorial-brand` vs `bold-creative-agency` | Editorial is refined and essay-like; bold agency can use stronger contrast, case grids, and expressive motion. |
| `public-sector-civic` vs `executive-b2b-trust` | Public sector prioritizes accessibility, service clarity, eligibility/FAQ, and accountability over persuasion. |

For public examples or multiple demo sites, also use `references/design-taste-benchmarks.md`. A demo set fails overlap review when the sites share the same navigation shape, hero split, card grid, proof area, motion recipe, and footer path with only color and copy changes.

## Practicality Check

Rate each visual direction against the actual project:

- Buyer clarity: can the first screen explain the business in 5 seconds?
- Proof fit: does the style support evidence modules such as cases, metrics, credentials, process, or screenshots?
- Asset fit: can the client provide photos, screenshots, diagrams, or case visuals that match the style?
- Motion fit: does animation clarify sequence, feedback, or product value?
- Risk level: could the style feel too flashy, too dark, too generic, or too close to another preset?
- Benchmark fit: can the output name what it learned from references and what it deliberately changed?
- Screenshot fit: do hero, proof, mid-page module, footer, and mobile screenshots look intentional rather than patched?

## Interaction Overlap Review

The interaction presets share a few primitives: reveal, sequence, highlight, compare, and calculate. Keep them distinct by intent:

| Intent | Presets |
|---|---|
| Show entrance hierarchy | `css-only-business-motion`, `animejs-staggered-reveal`, `premium-image-mask-reveal` |
| Explain process or structure | `animejs-svg-line-draw`, `process-stepper`, `product-hotspot-tour` |
| Support evidence | `metric-count-up`, `comparison-before-after`, `dashboard-panel-sequence` |
| Improve navigation and conversion | `case-filter-transition`, `sticky-cta-rail` |
| Make assumptions interactive | `roi-calculator-feedback` |
| Tell a high-effort story | `gsap-scroll-storyline` |
| Create premium scroll experiences | `pinned-scroll-storytelling`, `horizontal-case-wall`, `scroll-scrub-dashboard-morph` |
| Create product/brand spectacle | `threejs-product-orbit-hero`, `shader-liquid-reveal`, `interactive-orbit-network` |
| Enhance creative browsing | `magnetic-media-hover`, `shared-layout-transition` |
| Preserve accessibility | `reduced-motion-safe-mode` |

## Motion Intensity Ladder

1. Static professional layout: no motion except hover/focus.
2. CSS polish: button, card, nav, and reveal states.
3. Anime.js sequence: stagger, SVG line draw, lightweight timeline.
4. Product interaction: filters, calculators, dashboard previews, hotspots.
5. Premium product motion: shared layout transitions, image masks, dashboard sequencing, magnetic media.
6. GSAP story page: pinned, scrubbed, horizontal, or cinematic scroll only when the project is content-rich enough.
7. Three.js/WebGL/spatial interaction: only for real 3D/product/platform/space needs.

Do not use a higher intensity level only to make the page feel trendy. Use it when the project has enough content, proof, and visual assets to justify it.

## Showcase Preview Set

The more visually ambitious GIFs are:

- `pinned-scroll-storytelling.gif`
- `scroll-scrub-dashboard-morph.gif`
- `horizontal-case-wall.gif`
- `shared-layout-transition.gif`
- `threejs-product-orbit-hero.gif`
- `shader-liquid-reveal.gif`
- `magnetic-media-hover.gif`
- `interactive-orbit-network.gif`

Use showcase motion only when at least two are true:

- The page is a proposal, campaign, brand launch, AI/product showcase, or creative case page.
- The user explicitly asks for premium/showcase/trendy/cinematic motion.
- The project has strong visuals, screenshots, product states, diagrams, or case materials.
- The team can spend time on browser, mobile, and performance QA.

Avoid showcase motion when the page is a public-sector, compliance-heavy, finance-heavy, form-heavy, or information-dense service website unless the user explicitly approves the tradeoff.

## Asset Footprint Policy

Preview files are optional for execution and hosted in GitHub Releases for human review. If a distribution needs a smaller checkout, keep `references/`, `assets/presets/`, `assets/templates/`, and `scripts/`, then regenerate previews with `scripts/generate_preview_assets.py`. A true full-clone reduction for historical blobs requires an explicit history-rewrite plan.
