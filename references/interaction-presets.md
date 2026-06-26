# Interaction Presets

Use this reference when the user asks for trendy interaction, Anime.js, GSAP, scroll effects, cinematic motion, micro-interactions, or a more current website experience.

## Motion Principles

- Motion must explain hierarchy, sequence, cause/effect, or feedback.
- Keep business interactions restrained: 160-520ms for most UI transitions.
- Always respect `prefers-reduced-motion`.
- Avoid scroll hijacking, excessive parallax, layout-shifting animations, and motion that hides content.
- Use CSS-only motion first for simple states. Add a JS animation library only when sequencing, SVG, scroll sync, or complex stagger is useful.

## Library Selection

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
