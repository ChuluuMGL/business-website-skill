# Distribution And Platform Packaging

Use this guide when preparing `business-website-skill` for public distribution beyond GitHub.

## Current Package Shape

This repository is a filesystem Agent Skill: `SKILL.md` plus references, scripts, presets, and templates. The main branch should stay lightweight. Human-facing preview PNG/JPG/GIF assets belong in GitHub Releases or another external asset host, not in the execution package.

Do not publish client materials, private brand files, customer names, addresses, phone numbers, analytics exports, credentials, cookies, tokens, or screenshots containing private account state. Keep examples synthetic unless the user explicitly provides publishable material.

## Recommended Sync Priority

Use this order when deciding where to publish beyond GitHub:

1. **SKILL.md-native directories and indexes**: OpenClaw/ClawHub, SkillsMP, LobeHub Skills, and SkillsLLM. These are the best fit because the repo already uses the portable Agent Skills shape.
2. **Local coding agents with skill support**: Gemini CLI and Kimi Code CLI. Add installation notes and test runs; no separate wrapper is required.
3. **Business-user wrappers**: Coze first, then Dify or ChatGPT GPT Store. Use these only when the audience should interact with a guided bot, workflow, or knowledge base instead of installing a filesystem skill.
4. **Tool/plugin wrappers**: MCP, Kimi plugin, or Coze plugin only after there is an actual callable API/tool around generation, auditing, deployment, or screenshot QA.

Do not build a standalone Chrome extension for distribution. Browser or Chrome automation is useful as a QA capability, but it is not the right packaging format for this skill.

## Native Or Near-Native Skill Targets

| Target | Fit | Packaging approach | Notes |
|---|---:|---|---|
| GitHub | High | Public repo plus Releases | Primary source of truth, version history, issue tracking, and installation docs. |
| Claude Code Skills | High | Copy or clone folder into `.claude/skills/business-website-skill/` | `SKILL.md` is the core file; long references should stay outside the main body and load only when relevant. |
| Codex / OpenAI-style skills | High | User or project skills directory plus optional `agents/openai.yaml` | Keep Codex-specific UI metadata isolated so other agents can ignore it. |
| OpenClaw / ClawHub | High | Publish as a text-based Agent Skill after security and size review | Best public registry fit for SKILL.md-style packages; avoid unnecessary binaries and shell side effects. |
| Gemini CLI | High | Install from GitHub or place under `.gemini/skills/` or `.agents/skills/` | Gemini CLI supports Agent Skills and can install from Git repositories. |
| Kimi Code CLI | High | Place under `.kimi/skills/`, `.config/agents/skills/`, `.agents/skills/`, or pass `--skills-dir` | Kimi Code CLI supports Agent Skills separately from plugins. |
| VS Code / GitHub Copilot Agent Skills | Medium-high | Package as instructions, scripts, and resources under a skill folder | Works best when the user already uses Copilot agent workflows. |
| Cursor, Trae, Antigravity, Hermes | Medium | GitHub install instructions plus runtime-specific adapters if needed | Treat as expected-compatible until an end-to-end run is recorded. |
| SkillsMP, LobeHub Skills, SkillsLLM | Medium-high | Submit or wait for indexing from the GitHub repo | These are discovery directories; keep GitHub as source of truth and inspect each catalog's safety model. |

## Wrapper Or Marketplace Targets

| Target | Fit | Recommended form | What changes |
|---|---:|---|---|
| Coze | Medium | Bot/workflow/knowledge package; plugin only if a generator API exists | Best for non-technical business users. Convert the phase workflow into guided intake, outline, implementation guidance, and QA steps. |
| Dify | Medium | App/workflow template or plugin package | Good for teams that want a guided web-building workflow; a true Dify plugin needs a packaged tool/API, not only markdown instructions. |
| ChatGPT GPT Store | Medium | Custom GPT with knowledge files and optional Actions | Works as a consulting/generation assistant, but it is not a native filesystem skill. |
| MCP registries | Low-medium | MCP server wrapping audits, template generation, and project scaffolding | Useful only if the scripts become callable tools. Current repo is not an MCP server. |

## Useful Plugin Types

Plugins are useful when they provide capabilities the skill cannot encode as instructions:

- GitHub plugin: release management, repository sync, issues, and pull requests.
- Browser or Chrome automation: live-site QA, screenshots, responsive checks, console errors, and form interaction checks.
- Deployment plugin: Vercel, Netlify, Cloudflare Pages, or a similar deployment target.
- Image/design plugin: image generation, Canva, Figma, or brand-asset extraction when the user lacks source visuals.
- Performance/SEO tool: Lighthouse, PageSpeed, sitemap checks, structured-data validation, and broken-link scanning.
- Coze/Dify/Kimi plugin: only when wrapping a real executable tool or API, not just the markdown workflow.

## Public Release Checklist

Before publishing to any public registry:

1. Run `python3 /Users/chuluu/.codex/skills/.system/skill-creator/scripts/quick_validate.py .`.
2. Run `python3 scripts/audit_static_site.py assets/templates/static-business-site index.html --strict-seo`.
3. Run `python3 -m json.tool skill.json`.
4. Confirm `assets/previews/` contains only lightweight documentation or release links.
5. Confirm `skill.json.compatibility.tested` only lists runtimes with completed end-to-end tests.
6. Confirm copyright reads `月瑀科技 YUEYU TECH` and the website is `https://www.yueyu.tech/`.
7. Review all scripts for destructive filesystem commands, network calls, token handling, and hidden data upload.
8. Add platform-specific install notes only after checking that platform's current packaging rules.

## Platform Docs To Recheck

Registry and marketplace rules can change. Before publishing, verify the current docs:

- OpenClaw ClawHub: https://docs.openclaw.ai/clawhub
- OpenClaw Skills: https://docs.openclaw.ai/tools/skills
- Claude Code Skills: https://docs.anthropic.com/en/docs/claude-code/skills
- VS Code Agent Skills: https://code.visualstudio.com/docs/agent-customization/agent-skills
- Gemini CLI Agent Skills: https://geminicli.com/docs/cli/skills/
- Gemini CLI Extensions: https://google-gemini.github.io/gemini-cli/docs/extensions/
- Kimi Code CLI Agent Skills: https://moonshotai.github.io/kimi-cli/en/customization/skills.html
- Kimi Skills help: https://www.kimi.com/help/agent/what-are-skills
- SkillsMP: https://skillsmp.com/
- LobeHub Skills: https://lobehub.com/skills
- SkillsLLM: https://skillsllm.com/
- Coze Store overview: https://www.coze.com/open/docs/guides/store
- Coze bot publishing: https://www.coze.com/open/docs/guides/store_bot
- Coze plugin publishing: https://www.coze.com/open/docs/guides/store_plugin
- Dify plugin publishing: https://docs.dify.ai/en/develop-plugin/publishing/marketplace-listing/release-overview
- ChatGPT GPT creation: https://help.openai.com/en/articles/8554397-creating-and-editing-gpts
- ChatGPT Actions: https://help.openai.com/en/articles/9442513-configuring-actions-in-gpts

## Recommended Next Adapters

If broader distribution becomes a priority, add a small `adapters/` folder:

- `adapters/claude-code.md`: install path, invocation examples, and known behavior.
- `adapters/openclaw-clawhub.md`: ClawHub metadata, publishing checklist, and security review notes.
- `adapters/coze.md`: bot prompt, workflow fields, and knowledge-file mapping.
- `adapters/dify.md`: app/workflow/plugin split and package strategy.
- `adapters/cursor-trae-hermes.md`: expected paths, limitations, and manual verification log.
