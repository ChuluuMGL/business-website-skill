# Distribution launch drafts

Ready-to-post launch copy for business-website-skill. These are drafts — post them
from your own accounts (Reddit, Hacker News, Discord, X). Each leads with the
differentiator (evidence-driven, anti-hallucination) and links the live demos as
proof, since that is the skill's strongest hook.

- Repo: https://github.com/ChuluuMGL/business-website-skill
- Live demos: https://business-website-skill.vercel.app/#examples
- English site: https://business-website-skill.vercel.app/en/

## r/ClaudeAI (English)

**Title:** I built an Agent Skill that stops LLMs from inventing fake clients, metrics, and awards on business websites

**Body:**

Most "generate a website" prompts produce pages full of fabricated logos, inflated ROI %, and testimonial quotes that don't exist. I open-sourced an Agent Skill that treats a business website as an interactive proposal and forces an evidence-first workflow:

- **Evidence map** before any code: confirmed facts vs. missing facts vs. forbidden assumptions. Unconfirmed numbers stay as `pending`, never rounded to 0.
- **Benchmark-first taste gate** + **named visual systems**, so two demos for different industries don't look like color-swapped clones.
- **SEO/GEO + placeholder audit** built in (`audit_static_site.py --strict-seo --no-placeholders`), so handoff pages can't ship with "Lorem ipsum" or `example.com`.

Three live demos (all generated from synthetic briefs, all passing the strict audit):
B2B service / Industrial green-tech / AI SaaS — https://business-website-skill.vercel.app/#examples

Works with Claude Code, Codex (verified), and Cursor/Gemini CLI (expected). Feedback on the workflow and the anti-hallucination gates especially welcome.

## Hacker News (English)

**Title:** Show HN: An Agent Skill that builds business websites without inventing facts

**Body:**

business-website-skill is an open Agent Skill (SKILL.md format) that turns messy inputs — PDFs, brand folders, existing sites, briefs — into client-ready corporate/B2B/brand sites through a stage-gated workflow.

The core idea: an LLM building a marketing site will happily hallucinate credentials, customer logos, and metrics. This skill constrains it with an evidence map (confirmed / pending / forbidden), benchmark-first design taste gates, named visual systems, and a static-site + SEO/GEO + placeholder auditor that fails the build on leftover `TODO` / `example.com` / `待确认`.

Live demos and repo: https://business-website-skill.vercel.app/

It's stage-gated and stack-flexible (static HTML, React/Vite, Next.js). Curious how others handle the "don't fabricate facts" problem in agent-generated content.

## 独立开发者 / 个人品牌 圈（中文）

**标题：** 开源了一个 Agent Skill：让 AI 建商业官网时不再编造客户、数据和资质

**正文：**

大多数"生成网站"的提示词会产出满屏假 Logo、虚高 ROI、不存在的客户证言。我开源了 business-website-skill，把商业官网当成一份可交互的提案，强制走证据优先的流程：

- 动代码前先出**证据地图**：已确认 / 待确认 / 禁止编造。没确认的数字一律标"待确认"，绝不凑成 0。
- **标杆研究 + 命名视觉系统**，让两个不同行业的 demo 不会只是换了个颜色的同一个模板。
- 内置**静态审计 + SEO/GEO + 占位符拦截**（`audit_static_site.py --strict-seo --no-placeholders`），交付页不会带着 "Lorem ipsum" 或 example.com 上线。

三个真实 demo（均由合成 brief 生成、均通过严格审计）：B2B 服务 / 工业环保 / AI SaaS
👉 https://business-website-skill.vercel.app/#examples

个人品牌站、独立顾问官网也在支持范围内。欢迎拍砖，尤其欢迎对"反幻觉"那套机制的反馈。

## Discord / X short version (bilingual)

🇬🇧 Open-sourced an Agent Skill that builds business websites without fabricating facts — evidence map, benchmark-first taste gates, named visual systems, built-in SEO/GEO + placeholder audit. 3 live demos: https://business-website-skill.vercel.app/#examples

🇨🇳 开源了一个 Agent Skill：让 AI 建商业官网时先出证据地图、不编造客户和数据，内置 SEO/GEO + 占位符审计。3 个真实 demo：https://business-website-skill.vercel.app/#examples

## Posting checklist

- [ ] Verify the three demo links resolve before posting.
- [ ] One Show post per community, spaced a few days apart; don't cross-post identical text same-day.
- [ ] Reply to early comments honestly, including known limitations (e.g., ClawHub/marketplace availability, runtimes still in `expected`).
- [ ] If a "what about personal sites / SaaS?" question arises: both are in scope — the boundary is transactional e-commerce / app backends, not industries.
