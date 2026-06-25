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
│   ├── benchmark-patterns.md
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

## Install And Compatibility

The core skill follows the open Agent Skills shape: a folder with `SKILL.md`, plus optional `references/`, `scripts/`, and `assets/`. Most compatible agents only require the folder to be placed under their skills directory.

| Agent/runtime | Suggested install path | Status |
|---|---|---|
| Codex | `.agents/skills/business-website-skill/` or user skills folder | Supported |
| Claude Code | `.claude/skills/business-website-skill/` | Expected compatible |
| Cursor | `.cursor/skills/business-website-skill/` or project skills folder | Expected compatible |
| Trae | `.trae/skills/business-website-skill/` | Expected compatible |
| Antigravity | `.agent/skills/business-website-skill/` or configured skills folder | Expected compatible |
| OpenClaw | workspace or user skills root documented by OpenClaw | Expected compatible |
| Hermes | `~/.hermes/skills/business-website-skill/` or configured skills root | Expected compatible |

Only Codex-specific UI metadata lives in `agents/openai.yaml`. Other agents can ignore that file and use `SKILL.md` directly.

### Generic Install

```bash
git clone https://github.com/ChuluuMGL/business-website-skill.git .agents/skills/business-website-skill
```

Or with SSH:

```bash
git clone git@github.com:ChuluuMGL/business-website-skill.git .agents/skills/business-website-skill
```

Then invoke by name where supported:

```text
$business-website-skill
```

### Agent-Specific Examples

```bash
# Claude Code
git clone https://github.com/ChuluuMGL/business-website-skill.git .claude/skills/business-website-skill

# Cursor
git clone https://github.com/ChuluuMGL/business-website-skill.git .cursor/skills/business-website-skill

# Trae
git clone https://github.com/ChuluuMGL/business-website-skill.git .trae/skills/business-website-skill

# Antigravity
git clone https://github.com/ChuluuMGL/business-website-skill.git .agent/skills/business-website-skill

# Hermes
git clone https://github.com/ChuluuMGL/business-website-skill.git ~/.hermes/skills/business-website-skill
```

OpenClaw and other runtimes may use configurable workspace or global skill roots. Place the cloned folder under the root they scan.

## Compatibility Notes

- Keep `SKILL.md` uppercase. Some runtimes are case-sensitive.
- Keep the folder name kebab-case: `business-website-skill`.
- Keep public metadata in `skill.json`; agents that do not read it can ignore it.
- The Python audit script uses only the standard library.
- If a runtime does not support executable scripts, the workflow still works as instructions plus template assets; run `scripts/audit_static_site.py` manually.
- If a runtime does not support UI-style choice prompts, the skill tells the agent to present 2 to 3 text options.

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

## Current Maturity

This is a practical v1 skill. It is strongest at phased planning, evidence-safe business website structure, static prototypes, and delivery checks. The next maturity step is to add more templates, visual QA automation, and real-world example fixtures.

## License

MIT
