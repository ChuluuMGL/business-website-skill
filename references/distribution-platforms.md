# Distribution And Platform Packaging

Use this guide when preparing `business-website-skill` for public distribution beyond GitHub.

## Current Package Shape

This repository is a filesystem Agent Skill: `SKILL.md` plus references, scripts, presets, and templates. The main branch should stay lightweight. Human-facing preview PNG/JPG/GIF assets belong in GitHub Releases or another external asset host, not in the execution package.

Do not publish client materials, private brand files, customer names, addresses, phone numbers, analytics exports, credentials, cookies, tokens, or screenshots containing private account state. Keep examples synthetic unless the user explicitly provides publishable material.

## Native Or Near-Native Skill Targets

| Target | Fit | Packaging approach | Notes |
|---|---:|---|---|
| GitHub | High | Public repo plus Releases | Primary source of truth, version history, issue tracking, and installation docs. |
| Claude Code Skills | High | Copy or clone folder into `.claude/skills/business-website-skill/` | `SKILL.md` is the core file; long references should stay outside the main body and load only when relevant. |
| Codex / OpenAI-style skills | High | User or project skills directory plus optional `agents/openai.yaml` | Keep Codex-specific UI metadata isolated so other agents can ignore it. |
| OpenClaw / ClawHub | High | Publish as a text-based Agent Skill after security and size review | Best public registry fit for SKILL.md-style packages; avoid unnecessary binaries and shell side effects. |
| VS Code / GitHub Copilot Agent Skills | Medium-high | Package as instructions, scripts, and resources under a skill folder | Works best when the user already uses Copilot agent workflows. |
| Cursor, Trae, Antigravity, Hermes | Medium | GitHub install instructions plus runtime-specific adapters if needed | Treat as expected-compatible until an end-to-end run is recorded. |

## Wrapper Or Marketplace Targets

| Target | Fit | Recommended form | What changes |
|---|---:|---|---|
| Coze | Medium | Bot/workflow/knowledge package; plugin only if a generator API exists | Convert the phase workflow into bot instructions and optionally add a workflow for brief intake, outline, implementation, and QA. |
| Dify | Medium | App/workflow template or plugin package | Good for teams that want a guided web-building workflow; a true Dify plugin needs a packaged tool/API, not only markdown instructions. |
| ChatGPT GPT Store | Medium | Custom GPT with knowledge files and optional Actions | Works as a consulting/generation assistant, but it is not a native filesystem skill. |
| MCP registries | Low-medium | MCP server wrapping audits, template generation, and project scaffolding | Useful only if the scripts become callable tools. Current repo is not an MCP server. |

## Xiaohongshu Skill Boundary

`xiaohongshu-skill` usually refers to Xiaohongshu/RedNote automation or operations skills: account login, post search, topic research, content publishing, comment/like/favorite actions, or account analytics. This business website skill should not be listed as a Xiaohongshu operations skill because it does not operate Xiaohongshu accounts or publish notes.

Acceptable Xiaohongshu-adjacent options:

- Publish a Xiaohongshu note promoting the GitHub project as content marketing.
- Create a separate companion skill for turning completed website cases into Xiaohongshu note outlines, cover-copy directions, and compliant promotional captions.
- Keep any browser/account automation out of this repository unless it becomes a separate, explicitly scoped Xiaohongshu skill with risk controls.

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
