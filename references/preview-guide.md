# Preview Guide

Use this guide when reviewing whether the built-in style and interaction presets are visually useful, distinct enough, and practical for client-facing business websites.

## Preview Assets

- Style overview: `assets/previews/style-overview.png`
- AI concept moodboard: `assets/previews/ai-style-moodboard.jpg`
- Individual style thumbnails: `assets/previews/styles/`
- Interaction GIFs: `assets/previews/interactions/`
- Regeneration script: `scripts/generate_preview_assets.py`

The generated style overview is deterministic and should stay close to the machine-readable presets. The AI concept moodboard is only a visual mood reference and should not be treated as a template or factual website output.

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

## Practicality Check

Rate each visual direction against the actual project:

- Buyer clarity: can the first screen explain the business in 5 seconds?
- Proof fit: does the style support evidence modules such as cases, metrics, credentials, process, or screenshots?
- Asset fit: can the client provide photos, screenshots, diagrams, or case visuals that match the style?
- Motion fit: does animation clarify sequence, feedback, or product value?
- Risk level: could the style feel too flashy, too dark, too generic, or too close to another preset?

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
| Preserve accessibility | `reduced-motion-safe-mode` |

## Motion Intensity Ladder

1. Static professional layout: no motion except hover/focus.
2. CSS polish: button, card, nav, and reveal states.
3. Anime.js sequence: stagger, SVG line draw, lightweight timeline.
4. Product interaction: filters, calculators, dashboard previews, hotspots.
5. GSAP story page: scroll-linked narrative only when the project is content-rich enough.
6. Three.js or spatial interaction: only for real 3D/product/space needs.

Do not use a higher intensity level only to make the page feel trendy. Use it when the project has enough content, proof, and visual assets to justify it.
