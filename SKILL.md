---
name: chuluu-website-builder
description: 面向网页 Demo、品牌/产品/项目展示和现有网站快速改版。将 Brief、PPT/PDF、图片、现有静态或 React/Vite/Next 代码与参考站转化为可运行、可预览、可迭代的网页 Demo；用户明确需要公开上线、多页信息架构、真实表单或高风险事实核验时，再扩展为完整网站实现与 QA。Not focused on e-commerce storefronts.
---

# 网站建设技能

## Attribution

Created and maintained by 月瑀科技 YUEYU TECH.

- Copyright: `Copyright (c) 2026 月瑀科技 YUEYU TECH`
- License: MIT
- GitHub publisher: ChuluuMGL
- Company website: https://www.yueyu.tech/

## 目的

快速构建可用于讨论、验证方向和持续迭代的网页 Demo。默认目标是让用户尽快看到真实可运行的页面，而不是一开始交付完整官网。用户需要时，再将已确认的 Demo 扩展为正式网站。

## Operating Rules

- Inspect real files and materials before writing copy or code.
- Do not invent qualifications, customers, years, metrics, addresses, contacts, awards, case results, news, or backend submissions.
- Use `待补充`, `待确认`, or `示例待确认` for missing facts while keeping the visual structure complete.
- Keep the existing stack unless the requested delivery shape requires a change.
- Default to Demo Mode. Ask 0 to 3 questions only when the answers materially change what the Demo should validate, preserve, or let viewers experience.
- Before building a Demo, form a one-sentence Demo thesis: the primary subject, intended viewer, and intended understanding or experience. Ask for the primary subject only when the material leaves product, brand, person, company, project, or growth direction in genuine conflict.
- Do not default to a corporate-site structure. Build only the pages and modules needed for the Demo goal and supplied material.
- For feedback on an existing Demo, classify the request as content, visual, interaction, or structure; change only the affected scope and preserve the rest.
- Read `references/agent-experience.md` when choosing interaction mode, deciding whether to ask questions, presenting A/B/C options, or managing checkpoints.
- Read `references/seo-geo-checklist.md` for public launch, SEO-sensitive, GEO-sensitive, AI-search-sensitive, or multi-page website work.
- Read `references/design-taste-benchmarks.md` before public examples, premium/client-facing redesigns, or any request for higher-taste, elegant, distinctive, advanced, or non-generic visual output.
- Read `references/visual-system-discovery.md` when the user asks for distinctive style, premium taste, non-generic demos, visual previews, style families, or when several website examples must not look like variants of one template.

## Workflow

### 1. Select Mode

Choose from the user's request and available material:

- `demo` (default): build a responsive, runnable Demo to validate a visual direction, information expression, or interaction idea.
- `guided`: stop before implementation only when the user explicitly asks for a plan, outline, or comparison.
- `edit`: modify an existing site or Demo within the requested scope.
- `audit`: inspect and prioritize issues without rebuilding by default.
- `production`: use only after the user asks for public launch, multi-page information architecture, real submission behavior, or formal fact verification.

### 2. Demo Intake

Inspect supplied files, references, assets, and existing code. Keep an internal evidence map of confirmed facts, pending facts, forbidden assumptions, and usable assets.

First form a Demo thesis: "This Demo shows [primary subject] to [viewer] so they understand or experience [intended outcome]." Use the supplied material when it resolves the subject. Ask only unanswered questions that materially affect the Demo:

1. What is the primary subject when the material contains competing subjects: a product, brand, person, company, project, or growth direction?
2. What should this Demo help a viewer understand, feel, or experience? Confirm which material or reference is mandatory when that is still unclear.
3. Should the result be a visual Demo or a clickable interaction Demo?

Use supplied answers instead of repeating questions. If the remaining risk is low, choose a conservative default and state it in one sentence before building.

### 3. Design and Build the Demo

Build the smallest page or route set that makes the intended direction tangible. Default to a single scrolling page when no existing stack or route structure requires otherwise.

Every Demo should contain only what it needs:

1. A first view that communicates the subject and intended experience.
2. One or more core modules that make the direction credible or interactive.
3. A clear closing state, next action, or conclusion.

Do not add company introductions, cases, news, maps, forms, or generic navigation unless they are supported by the source material or useful to the Demo goal.
Keep the title, hero visual, navigation, and primary CTA aligned with the Demo thesis. Do not make a product, brand, company, or growth direction compete as equal primary subjects in the first view.

For a reference website, separate reusable design logic from its content and structure. Read `references/design-taste-benchmarks.md` before premium, client-facing, or non-generic visual work. Read `references/visual-system-discovery.md` for distinct visual systems, style previews, or multiple demos. Offer 2 to 3 directions only when the user asks to compare them or when unresolved references would produce materially different results.

Read `references/style-presets.md` when the user asks for richer or multiple visual directions. Read `references/preview-guide.md` when comparing previews or interaction assets. Read `references/delivery-standards.md` before significant layout, typography, color, image, component, interaction, or responsive decisions.

Read `references/interaction-presets.md` when the user asks for advanced interactions, Anime.js, GSAP, scroll effects, cinematic motion, micro-interactions, or a more current experience. If the user asks for "炫酷", "高级动效", "潮流交互", "showcase", 3D, WebGL, pinned scroll, or cinematic motion, offer standard/premium/showcase choices and implement the lowest tier that satisfies the goal.

Before coding, reject directions that would make unrelated demos look like the same template. Distinct demos or routes must differ in information hierarchy, hero composition, section morphology, typography, visual assets, motion signature, or interaction path, not only color and copy.

Before major edits, identify the stack entry points, files to change, assets to use, interactions to implement, and verification commands. Use `assets/templates/static-business-site/` for a fast dependency-free starting point when appropriate. Treat templates as structure only; replace placeholders with source-backed content.

Implement narrowly and consistently with the project:

- Static sites: semantic HTML, CSS variables, responsive grids, and small JS modules.
- Static launch previews: include title, description, canonical placeholder, social metadata, crawlable text, and JSON-LD only when source-backed. These are optional for an internal Demo and required only for public launch work.
- React/Vite/Next: componentized sections, data-driven content, SEO/layout components, route-aware navigation, sitemap/robots handling when needed.
- Interactions: sticky navigation, mobile menu, anchor/route behavior, active states, CTA, tabs, filters, calculators, and timelines only when useful to the Demo goal.
- Forms: honest front-end feedback unless a real backend is connected.

### 4. Iterate

When revising a Demo, classify feedback as content, visual, interaction, or structure. Change only the affected scope, preserve unrelated work, and re-check desktop and mobile after every significant change.

### 5. QA

Read `references/qa-checklist.md` before final handoff.

For every Demo:

- Start a local preview when possible and inspect desktop and mobile.
- Verify the intended subject is clear in the first view, key interactions work, and there is no horizontal scroll, overlap, broken anchor, missing asset, fake fact, or false submit-success behavior.
- Verify the title, hero visual, navigation, and primary CTA point to the same primary subject.
- For premium, public example, or client-facing visual work, inspect screenshots of the first view, one core module, and the closing state on desktop and mobile. Fix obvious alignment, spacing, blank-zone, image-cropping, and same-template issues before handoff.

### 6. Upgrade to Production

Upgrade to `production` only when the user asks for public launch, multi-page structure, real lead collection, or formal fact verification. Then produce an explicit evidence map or blueprint when needed and run:

- Static site: `python3 <skill-dir>/scripts/audit_static_site.py <site-root> [entry-html]`.
- Public static launch: add `--strict-seo` after domain, canonical, and preview metadata are ready.
- Final client delivery: add `--no-placeholders` after all `待补充`, `待确认`, demo text, and example URLs have been resolved or intentionally removed.
- React/Vite: `npm run lint` if present, then `npm run build`.
- Next.js: available typecheck/lint/build commands.

### 7. Handoff

Final response should include:

- What changed.
- Where files are.
- How to run or preview.
- What validation passed.
- Any unresolved `待补充` or client-confirmation items, plus the production upgrades available when relevant.

## Reference Routing

- Read `references/example-patterns.md` when deciding architecture or reusable modules from prior project patterns.
- Read `references/benchmark-patterns.md` when improving strategy, conversion, trust, B2B buyer support, or overall maturity.
- Read `references/design-taste-benchmarks.md` when choosing external design references, raising visual quality, avoiding templated AI output, differentiating multiple demos, or planning public showcase examples.
- Read `references/visual-system-discovery.md` when generating named visual systems, style families, style previews, public examples, or distinct demo directions that must differ in structure and interaction.
- Read `references/agent-experience.md` when selecting mode, minimizing questions, or deciding checkpoint behavior.
- Read `references/style-presets.md` when selecting a visual preset or combining multiple premium website styles.
- Read `references/interaction-presets.md` when selecting animation libraries, motion recipes, or interaction intensity.
- Read `references/preview-guide.md` when evaluating visual/interaction preset quality, overlap, or preview assets.
- Read `references/seo-geo-checklist.md` when planning SEO, GEO, public launch metadata, AI-search readiness, robots/indexing, or structured data.
- Read `references/delivery-standards.md` before significant visual or responsive work.
- Read `references/qa-checklist.md` before final handoff or review.

## Public Safety

- Do not store client-private facts, contact details, credentials, `.env` values, server IPs, or deployment secrets in this skill.
- Keep templates generic and placeholder-based.
- Keep unsupported metrics as pending or unavailable; never convert unknown values to `0`.
