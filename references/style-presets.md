# Style Presets

Use this reference when the user asks for many styles, premium visual directions, current/trendy business websites, or multiple design options before implementation.

## Selection Rules

- Choose style from business context, not trend alone.
- Present 2 to 3 relevant options, then ask for a choice when direction materially affects output.
- Default to `executive-b2b-trust` for general business websites with limited brand input.
- Do not use dark/cinematic/trendy styles for regulated, industrial, or government-facing projects unless the brand supports it.
- Keep accessibility, copy clarity, and evidence hierarchy stronger than decoration.
- Treat presets as directions, not templates. A preset does not define the header, hero, proof module, section shapes, or motion by itself.
- For multiple demos or multiple client routes, do not reuse the same module stack with different colors. Change the structure, media treatment, proof pattern, and interaction signature.
- For high-taste work, pair this file with `references/design-taste-benchmarks.md` before implementation.
- For public examples, premium redesigns, or any request for "更有品位", "不一样", "不要同质化", or "像成熟模板", pair this file with `references/visual-system-discovery.md` and output named visual systems instead of only preset names.

## Preset Families

### executive-b2b-trust

- Best for: consulting, professional services, enterprise suppliers, corporate websites.
- Visual: light cool-blue background, navy trust blue with a muted gold accent, wide margins, confident typography, proof-first layout.
- Layout: hero plus proof panel, service matrix, credential band, case cards, process timeline.
- Motion: subtle reveal, CTA hover, count-up metrics.
- Avoid: flashy gradients, oversized decorative shapes, casual copy.

### industrial-precision

- Best for: manufacturing, energy, engineering, environmental technology, equipment.
- Visual: white/soft gray, deep green/blue/graphite, technical diagrams, real site/equipment images.
- Layout: product/capability grid, process axis, case map, certificates, technical parameters.
- Motion: scroll reveal, tabbed specifications, SVG process-line draw.
- Avoid: lifestyle stock photos, playful gradients, vague SaaS visuals.

### ai-saas-data-cloud

- Best for: AI tools, SaaS platforms, analytics, automation, diagnostics.
- Visual: light or dark hybrid, data panels, product UI screenshots, gradients only as accents.
- Layout: product hero, feature grid, workflow diagram, integrations, dashboard preview, pricing/CTA.
- Motion: staggered cards, dashboard counters, orbit/integration map, scroll-linked product reveals.
- Avoid: crypto-style neon, fake product UI, unreadable dark sections.

### premium-editorial-brand

- Best for: brand studios, cultural brands, strategy consultancies, thought leadership.
- Visual: editorial spacing, refined image crops, serif/sans pairing, strong article-like hierarchy.
- Layout: narrative hero, manifesto, capability essays, selected work, insights/resources.
- Signature element: publication-like proof frame, editorial index, or image-led case spread.
- Motion: page transitions, image mask reveal, subtle typography reveal.
- Avoid: dense cards, dashboard visuals, too many CTAs.

### minimal-luxury

- Best for: high-end products, founder brands, boutique services, luxury-adjacent offers.
- Visual: quiet palette, generous whitespace, sharp photography, thin rules, premium typography.
- Layout: full-bleed hero, product/service story, proof through craft, selective case details.
- Motion: slow fades, image parallax, refined hover states.
- Avoid: loud badges, crowded metrics, aggressive popups.

### dark-data-command-center

- Best for: diagnostics, AI ops, dashboards, monitoring, data-heavy services.
- Visual: dark base, high-contrast data cards, subtle grid, luminous but restrained accents.
- Layout: command center hero, live metrics, data panels, scenario tabs, technical workflow.
- Motion: metric tickers, panel reveals, animated traces, system status indicators.
- Avoid: illegible low-contrast text, one-note purple, sci-fi excess.

### sustainable-green-tech

- Best for: ESG, climate, energy, environmental protection, water treatment, circular economy.
- Visual: light natural base, green/teal/blue accents, real infrastructure/nature/process images.
- Layout: impact metrics, solution process, case evidence, compliance/qualification, map coverage.
- Motion: count-up impact metrics, process line, before/after reveal.
- Avoid: generic leaf decoration, unsupported impact claims.

### bold-creative-agency

- Best for: creative agencies, production studios, marketing services, campaign proposals.
- Visual: strong contrast, confident typography, curated motion, case visuals, editorial grids.
- Layout: statement hero, service packages, selected work, process, reports/insights, contact CTA.
- Motion: staggered work cards, text reveal, media preview hover, sticky service navigation.
- Avoid: portfolio drama that hides service clarity.

### public-sector-civic

- Best for: public service, NGO, education, civic campaigns, institutional projects.
- Visual: accessible palette, clear navigation, strong information hierarchy, human-centered images.
- Layout: mission, services, impact, process, resources, eligibility/FAQ, contact.
- Motion: minimal; prioritize accessibility and clarity.
- Avoid: trendy motion, unclear CTAs, unsupported public claims.

### fintech-secure

- Best for: finance, insurance, compliance, B2B fintech, enterprise payment services.
- Visual: white/navy/green/steel, trust signals, compliance cards, product screenshots.
- Layout: trust hero, risk/compliance proof, feature matrix, security section, case examples.
- Motion: subtle data reveal, security badge hover, comparison toggles.
- Avoid: flashy money visuals, unrealistic ROI claims.

## Combining Presets

Use one primary preset and one secondary modifier:

- Industrial company with AI product: `industrial-precision` + `ai-saas-data-cloud`.
- Consulting firm with reports: `executive-b2b-trust` + `premium-editorial-brand`.
- Creative agency with enterprise clients: `bold-creative-agency` + `executive-b2b-trust`.
- ESG SaaS: `sustainable-green-tech` + `ai-saas-data-cloud`.

## Visual System Starters

For higher-taste work, named visual systems replace plain presets — they change module shapes, proof treatment, and interaction behavior, not just color. The four starters (**Editorial Evidence Chroma**, **Executive Proof Dossier**, **Industrial Field Blueprint**, **Product Command Theater**) are defined in [`visual-system-discovery.md`](./visual-system-discovery.md) with thesis, layout grammar, signature element, proof treatment, motion, and avoid-when. Load that file when the request is "更有品位", "不一样", "不要同质化", or "像成熟模板".

## Output Format For User Choices

When offering choices, use:

```text
Option A - Executive B2B Trust
Best for: ...
Look: ...
Signature element: ...
Proof treatment: ...
Interaction: ...
Tradeoff: ...

Option B - AI SaaS / Data Cloud
...
```

Ask the user to choose A/B/C only when the choice affects the build.
