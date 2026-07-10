# Agent Experience Guide

Use this guide when deciding how the agent should interact with the user while building, iterating, or auditing a website Demo and its possible production version.

## Interaction Modes

Choose the mode from the user's wording and available materials.

| Mode | Trigger | Agent Behavior |
|---|---|---|
| `demo` | "做个 Demo", "先看效果", "按这个参考试试", materials or an idea to test. | Ask only missing high-impact questions, then build a responsive, runnable Demo and validate it. |
| `guided` | "先给方案", "先出大纲", "给我几个方向". | Stop after the requested outline, evidence note, or direction comparison. |
| `edit` | Existing website/codebase with a concrete change request. | Preserve stack and style unless the user asks for redesign. |
| `audit` | "审计", "看看问题", "优化建议", "交付前检查". | Lead with findings, risk, and prioritized fixes; do not rebuild by default. |
| `production` | "正式上线", "做成完整网站", "多页", or "真实表单". | Add the needed evidence, IA, launch, or integration workflow after confirming scope. |

## Minimal Questions

Ask no more than 3 questions before work starts. If answers are missing and risk is low, default and continue.

First form a Demo thesis: "This Demo shows [primary subject] to [viewer] so they understand or experience [intended outcome]." Infer it from the supplied material when possible. Ask the fewest of these questions needed for the request:

1. What is the primary subject when the material contains competing subjects: a product, brand, person, company, project, or growth direction?
2. What should a viewer understand, feel, or experience? Confirm which material or reference is mandatory when that remains unclear.
3. Should the Demo be primarily visual or require clickable interactions?

Do not ask a question already answered by the supplied files, current code, or user wording. Use A/B/C choices only when the answer would materially change the result:

```text
Option A - Visual Direction
Best for: validating brand, hierarchy, and information expression.

Option B - Clickable Experience
Best for: validating product flow, states, or interaction behavior.

Option C - Production Foundation
Best for: a Demo expected to become a multi-page or public website.
```

## Defaulting Rules

- If facts are missing: preserve the section and use `待补充` or `待确认`.
- If visual direction is missing: infer it from supplied material; otherwise default to restrained, clear typography and purposeful imagery rather than a generic corporate layout.
- If the user asks for "高级" but the project is regulated, industrial, finance, or public-sector: choose premium restraint instead of showcase motion.
- If assets are weak: use structured layout, icons, diagrams, and proof modules instead of pretending there are rich visuals.
- If a requested effect risks performance or accessibility: offer a lower-tier alternative and explain the tradeoff in one sentence.
- If the request is a revision: classify it as content, visual, interaction, or structure, change only the affected scope, and preserve unrelated work.

## Checkpoints

Use checkpoints to keep the user in control without slowing down simple builds.

| Checkpoint | When To Pause |
|---|---|
| Demo intake | The primary subject or missing answers would materially change the intended visual, information, or interaction experience. |
| Evidence map | Regulated claims, unknown metrics, real lead collection, public launch, or other high-risk facts. |
| Blueprint | The user requests multi-page work or a Demo is being promoted to a complete site. |
| Design direction | The user explicitly requests comparison or unresolved references would lead to materially different results. |
| Benchmark/taste gate | Premium redesigns, multiple demos, or user asks for high-taste, distinctive, or non-generic visual output. |
| Motion tier | User requests premium/showcase motion or heavy animation libraries. |
| Handoff | Always summarize validation, files, preview method, unresolved `待确认`, and relevant production upgrades. |

## Output Shape

For a Demo request, final handoff should be short and operational:

- What was built or changed.
- Where the files are.
- How to preview or run.
- What validation passed.
- What still needs client confirmation.
- Which production upgrades are available only when relevant.

For an audit request, lead with findings ordered by severity before summarizing changes.

## Quality Gate

Before final handoff, verify:

- The Demo makes its intended subject or experience clear in the first view.
- The title, hero visual, navigation, and primary CTA point to the same primary subject.
- Unknown facts are not written as real facts.
- The core module demonstrates the intended visual, information, or interaction direction.
- A revision preserves unrelated sections and works on desktop and mobile after the change.
- CTA path is visible and specific when the Demo has a conversion goal.
- Premium or public work has benchmark references, a divergence contract, and a distinct visual signature.
- Mobile has no horizontal scroll or hidden content.
- Motion has reduced-motion fallback and does not block forms/navigation.
- Showcase effects have a clear business purpose, not just decoration.
