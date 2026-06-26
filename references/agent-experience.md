# Agent Experience Guide

Use this guide when deciding how the agent should interact with the user while building or auditing a business website.

## Interaction Modes

Choose the mode from the user's wording and available materials.

| Mode | Trigger | Agent Behavior |
|---|---|---|
| `guided` | "先给方案", "先出大纲", unclear brand direction, high client stakes. | Stop after evidence map, sitemap, section outline, CTA path, and design options. |
| `auto` | "直接做", "快速搭建", "先跑通", enough source material. | Default conservatively, label unknown facts, build and validate. |
| `edit` | Existing website/codebase with a concrete change request. | Preserve stack and style unless the user asks for redesign. |
| `audit` | "审计", "看看问题", "优化建议", "交付前检查". | Lead with findings, risk, and prioritized fixes; do not rebuild by default. |
| `showcase` | "更炫", "高级动效", "潮流交互", "品牌发布", "AI/创意提案". | Offer premium/showcase motion choices and confirm risk before heavy animation. |

## Minimal Questions

Ask no more than 3 questions before work starts. If answers are missing and risk is low, default and continue.

Priority questions:

1. What is the site type and conversion goal?
2. Which stack or delivery shape should be used?
3. Which visual/motion direction should be used?

Use A/B/C choices when possible:

```text
Option A - Conservative B2B
Best for: fast client-safe delivery.

Option B - Premium Product
Best for: SaaS/AI/product-led websites with screenshots.

Option C - Showcase Motion
Best for: proposal demos, creative pages, or high-impact launches; requires stronger QA.
```

## Defaulting Rules

- If facts are missing: preserve the section and use `待补充` or `待确认`.
- If brand direction is missing: default to `executive-b2b-trust`.
- If the user asks for "高级" but the project is regulated, industrial, finance, or public-sector: choose premium restraint instead of showcase motion.
- If assets are weak: use structured layout, icons, diagrams, and proof modules instead of pretending there are rich visuals.
- If a requested effect risks performance or accessibility: offer a lower-tier alternative and explain the tradeoff in one sentence.

## Checkpoints

Use checkpoints to keep the user in control without slowing down simple builds.

| Checkpoint | When To Pause |
|---|---|
| Evidence map | Sparse materials, regulated claims, unknown metrics, client-facing facts. |
| Blueprint | Ambiguous page count, unclear CTA, multiple business lines. |
| Design direction | Brand direction unclear or user explicitly asks for style choices. |
| Motion tier | User requests premium/showcase motion or heavy animation libraries. |
| Handoff | Always summarize validation, files, preview method, and unresolved `待确认`. |

## Output Shape

For a build request, final handoff should be short and operational:

- What was built or changed.
- Where the files are.
- How to preview or run.
- What validation passed.
- What still needs client confirmation.

For an audit request, lead with findings ordered by severity before summarizing changes.

## Quality Gate

Before final handoff, verify:

- First screen explains business value in 5 seconds.
- Unknown facts are not written as real facts.
- CTA path is visible and specific.
- Mobile has no horizontal scroll or hidden content.
- Motion has reduced-motion fallback and does not block forms/navigation.
- Showcase effects have a clear business purpose, not just decoration.
