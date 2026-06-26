# Interaction Presets

Use this reference when the user asks for trendy interaction, Anime.js, GSAP, scroll effects, cinematic motion, micro-interactions, or a more current website experience.

## Motion Principles

- Motion must explain hierarchy, sequence, cause/effect, or feedback.
- Keep business interactions restrained: 160-520ms for most UI transitions.
- Always respect `prefers-reduced-motion`.
- Avoid scroll hijacking, excessive parallax, layout-shifting animations, and motion that hides content.
- Use CSS-only motion first for simple states. Add a JS animation library only when sequencing, SVG, scroll sync, or complex stagger is useful.

## Motion Tiers

Use the lowest tier that achieves the business goal.

| Tier | Use For | Default? | Extra Requirements |
|---|---|---|---|
| `standard` | Corporate, B2B, service, proposal, and delivery-safe websites. | Yes | Must be readable without JavaScript. |
| `premium` | Stronger brand, SaaS, product, creative, and case-study pages. | Sometimes | Needs real visuals, screenshots, or case content. |
| `showcase` | High-impact campaign, AI, creative, launch, and premium proposal pages. | No | Needs explicit user intent, stronger QA, reduced-motion fallback, and performance checks. |
| `accessibility` | Reduced-motion and robust fallback behavior. | Always | Must be included whenever motion is added. |

If the user asks for "more cool", "炫酷", "高级动效", "潮流交互", or "showcase", present a short motion intensity choice:

```text
Option A - Premium business motion
Polished but still safe for most client websites.

Option B - Showcase motion
More cinematic and interactive; better for AI, creative, brand, or proposal demos; requires stronger QA and may need more assets.
```

## Library Selection

Official references:

- GSAP ScrollTrigger: https://gsap.com/docs/v3/Plugins/ScrollTrigger/
- Lenis: https://lenis.dev/
- Motion for React: https://motion.dev/docs/react
- Three.js: https://threejs.org/
- Anime.js: https://animejs.com/documentation/getting-started/installation/

### CSS-only business motion

- Use for: buttons, nav states, cards, small hover, reveal classes.
- Pros: fast, no dependency, compatible everywhere.
- Avoid for: complex timelines, SVG drawing, synchronized multi-target motion.

### Anime.js

- Use for: staggered card reveals, text/hero sequences, SVG line drawing, metric emphasis, lightweight timelines.
- Install with NPM in bundled projects: `npm install animejs`.
- Import in ES modules: `import { animate, stagger } from 'animejs';`.
- Static ESM option: `import { animate } from 'https://esm.sh/animejs';`.
- Static UMD option: load `https://cdn.jsdelivr.net/npm/animejs/dist/bundles/anime.umd.min.js`, then use `const { animate } = anime;`.
- Keep optional: do not add Anime.js to every site by default.

### GSAP

- Use for: mature scroll-linked animation, complex timeline choreography, production-heavy interactive pages.
- Prefer when the project already uses GSAP or needs ScrollTrigger-style behavior.
- Avoid adding it only for simple reveal effects.

### React Motion / Motion

- Use for: React/Vite/Next apps already using component animation.
- Good for route transitions, presence/exit states, shared layout, and reusable components.

### Three.js

- Use only for real 3D product, spatial, architectural, game-like, or visualizer needs.
- Must be full-bleed or meaningfully integrated, not a decorative card.

### Lenis

- Use for: smooth scroll feel, parallax sync, horizontal case walls, and premium narrative pages.
- Pair carefully with GSAP only when scroll behavior remains accessible.
- Avoid when the site is mostly forms, tables, or utilitarian content.

## Preset Recipes

### animejs-staggered-reveal

- Use for: hero proof cards, service cards, case grids.
- Effect: elements fade and move up with staggered delay.
- Good for: `ai-saas-data-cloud`, `bold-creative-agency`, `executive-b2b-trust`.
- Reduced motion: show elements immediately.

### animejs-svg-line-draw

- Use for: process diagrams, manufacturing flow, network map, timeline path.
- Effect: SVG path stroke draws as section enters viewport.
- Good for: `industrial-precision`, `sustainable-green-tech`, `ai-saas-data-cloud`.
- Requirement: meaningful SVG diagram, not abstract decoration.

### metric-count-up

- Use for: confirmed metrics, impact data, coverage, efficiency.
- Effect: number counts to final value once.
- Rule: unconfirmed metrics must be labeled `示例待确认` or omitted.

### case-filter-transition

- Use for: case grids by industry, region, service, or project type.
- Effect: active filter fades matching cards into a stable grid.
- Rule: no fake cases.

### sticky-cta-rail

- Use for: long proposal pages and service pages.
- Effect: sticky side/bottom CTA follows scroll without hiding content.
- Rule: mobile version must be compact and dismissible or non-obstructive.

### roi-calculator-feedback

- Use for: ROI, savings, emission, cost, or time calculators with transparent assumptions.
- Effect: slider/input updates metrics with smooth numeric feedback.
- Rule: formulas and assumptions must be visible or documented.

### premium-image-mask-reveal

- Use for: brand, luxury, editorial, and creative sites.
- Effect: image reveals through clip/mask while copy enters.
- Rule: do not crop away the subject.

### dashboard-panel-sequence

- Use for: SaaS, diagnostics, AI ops, analytics.
- Effect: dashboard panels enter in a logical product sequence.
- Rule: do not fake product screenshots if none exist.

### process-stepper

- Use for: service workflow, implementation process, after-sales support.
- Effect: users can click or scroll through steps.
- Rule: active state must be visible and accessible.

### gsap-scroll-storyline

- Use for: campaign pages, proposal storytelling, premium case pages.
- Effect: sections, imagery, and proof points progress in a controlled scroll sequence.
- Rule: use only for complex scroll-linked choreography; simple reveals should stay CSS-only or Anime.js.

### product-hotspot-tour

- Use for: product screenshots, equipment photos, SaaS UI previews, factory/process images.
- Effect: hotspots reveal feature explanations or proof points.
- Rule: hotspots must point to real, explainable features, not decorative dots.

### comparison-before-after

- Use for: renovation, optimization, workflow improvement, environmental impact, visual results.
- Effect: slider, toggle, or tab compares before and after states.
- Rule: label both states clearly and avoid unsupported performance claims.

## Premium And Showcase Recipes

### pinned-scroll-storytelling

- Use for: proposal narratives, campaign pages, premium case pages.
- Effect: sections pin while proof points, imagery, and CTA states change with scroll progress.
- Good for: `bold-creative-agency`, `premium-editorial-brand`, `ai-saas-data-cloud`.
- Rule: use only when the story has clear stages; provide normal stacked content on mobile.

### scroll-scrub-dashboard-morph

- Use for: AI products, SaaS analytics, data platforms, diagnostic tools.
- Effect: dashboard panels, charts, and labels morph as the user scrolls.
- Good for: `ai-saas-data-cloud`, `dark-data-command-center`, `fintech-secure`.
- Rule: morph real product states or clearly labeled concept UI; do not fake metrics.

### horizontal-case-wall

- Use for: creative agencies, case libraries, portfolio-heavy sites.
- Effect: pinned horizontal browsing of case cards or media tiles.
- Good for: `bold-creative-agency`, `premium-editorial-brand`.
- Rule: provide keyboard access, non-pinned mobile layout, and visible progress.

### shared-layout-transition

- Use for: React/Next product pages, card-to-detail transitions, service explorers.
- Effect: selected card expands into a detail panel or route with continuity.
- Good for: `ai-saas-data-cloud`, `bold-creative-agency`, `fintech-secure`.
- Rule: state changes must be accessible and not trap focus.

### threejs-product-orbit-hero

- Use for: hardware, architecture, spatial services, 3D products, data globes.
- Effect: full-bleed 3D hero or interactive orbit that communicates a real object/system.
- Good for: AI platforms, industrial tech, product-led sites.
- Rule: do not use 3D as a decorative card; provide static fallback and verify nonblank canvas.

### shader-liquid-reveal

- Use for: premium brand, creative campaign, editorial launches.
- Effect: WebGL/Canvas-style liquid reveal or distortion transition.
- Good for: `bold-creative-agency`, `premium-editorial-brand`, `minimal-luxury`.
- Rule: keep text outside the distortion zone or ensure contrast at every frame.

### magnetic-media-hover

- Use for: case previews, portfolio grids, premium media browsing.
- Effect: pointer proximity scales or follows media elements.
- Good for: creative and editorial sites.
- Rule: treat as pointer-only enhancement; touch devices need the same content without hover.

### interactive-orbit-network

- Use for: AI ecosystems, platform integrations, agent networks, coverage maps.
- Effect: real nodes, categories, and relationships animate or reveal on interaction.
- Good for: `ai-saas-data-cloud`, `dark-data-command-center`, `fintech-secure`.
- Rule: every node must correspond to a real integration, region, capability, or product concept.

## Anime.js Starter Snippet

Use only after deciding the project should include Anime.js.

```js
import { animate, stagger } from 'animejs';

const prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

if (!prefersReducedMotion) {
  animate('.js-reveal-card', {
    opacity: [0, 1],
    y: [24, 0],
    duration: 520,
    delay: stagger(80),
    ease: 'outCubic'
  });
}
```

For static pages without bundling, prefer the ESM CDN:

```html
<script type="module">
  import { animate, stagger } from 'https://esm.sh/animejs';

  if (!window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
    animate('.js-reveal-card', {
      opacity: [0, 1],
      y: [24, 0],
      duration: 520,
      delay: stagger(80),
      ease: 'outCubic'
    });
  }
</script>
```

## QA For Motion

- Confirm no animation causes horizontal scroll.
- Confirm animated content is visible when JavaScript fails.
- Confirm reduced-motion users can read everything without motion.
- Confirm text does not overlap during or after animation.
- Confirm forms and navigation remain usable while animations run.
- For `showcase` motion, also check bundle size, CPU load, mobile fallback, and whether the effect still supports the first-screen business message.
