# Business Website Skill

Build client-ready corporate, brand, B2B, service, and proposal-grade business websites from source materials.

This Agent Skill is designed for client-facing business website work: enterprise websites, brand websites, project showcase pages,招商/投标 pages, and presentation-ready prototypes. It is not focused on e-commerce storefronts.

## What It Does

- Turns source materials into a phased website plan.
- Separates confirmed facts from pending or forbidden assumptions.
- Produces sitemap/page outline and homepage section structure before implementation.
- Offers design direction choices when the user has not specified a visual route.
- Builds with the existing stack, or starts from a static HTML/CSS/JS template.
- Runs delivery checks for static sites and guides React/Vite/Next verification.

## Skill Contents

```text
business-website-skill/
├── SKILL.md
├── agents/openai.yaml
├── assets/templates/static-business-site/
├── references/
│   ├── delivery-standards.md
│   ├── example-patterns.md
│   └── qa-checklist.md
├── scripts/audit_static_site.py
├── skill.json
└── README.md
```

## Suggested Prompts

```text
Use $business-website-skill to build a client-ready B2B website from the materials in this folder.
```

```text
Use $business-website-skill to audit and polish this static company website before client delivery.
```

```text
Use $business-website-skill to create a proposal-grade landing page. Ask me for choices before implementation.
```

## Install

### Codex

Clone into a repo-scoped or user-scoped skills folder:

```bash
git clone git@github.com:ChuluuMGL/business-website-skill.git .agents/skills/business-website-skill
```

Then invoke:

```text
$business-website-skill
```

### Other Agent Skill Runtimes

Most Agent Skills-compatible tools can use this repository by placing it in their skills folder, for example:

- `.agents/skills/business-website-skill/`
- `.cursor/skills/business-website-skill/`
- `.trae/skills/business-website-skill/`
- `.claude/skills/business-website-skill/`

Exact support depends on the agent runtime.

## Static Template

The included template is generic and safe for public use:

```text
assets/templates/static-business-site/
├── index.html
├── index.css
└── index.js
```

It uses placeholder copy such as `待补充` and `示例待确认`. Replace placeholders with source-backed client facts before delivery.

## Static Site Audit

Run:

```bash
python3 scripts/audit_static_site.py assets/templates/static-business-site index.html
```

The script checks local assets, hash anchors, duplicate IDs, viewport metadata, missing image alt text, and CSS `url()` references.

## License

MIT
