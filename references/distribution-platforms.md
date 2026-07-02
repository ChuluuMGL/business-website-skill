# Distribution And Platform Packaging

Use this guide when preparing `business-website-skill` for public distribution beyond GitHub.

## Package Shape

This repository is a filesystem Agent Skill: `SKILL.md` plus references, scripts, presets, and templates. The main branch should stay lightweight. Human-facing preview PNG/JPG/GIF assets belong in GitHub Releases or another external asset host, not in the execution package.

Do not publish client materials, private brand files, customer names, addresses, phone numbers, analytics exports, credentials, cookies, tokens, or screenshots containing private account state. Keep examples synthetic unless the user explicitly provides publishable material.

## Sync Priority

GitHub is the source of truth. Treat every other platform as a subscriber, an index, or a wrapper.

1. **SKILL.md-native registries**: OpenClaw/ClawHub, SkillsMP, LobeHub Skills, SkillsLLM — best fit, since the repo already uses the portable Agent Skills shape.
2. **Local coding agents with skill support**: Gemini CLI, Kimi Code CLI — add install notes; no wrapper needed.
3. **Business-user wrappers**: Coze, then Dify or ChatGPT GPT Store — only when the audience wants a guided bot/workflow/knowledge base instead of a filesystem skill.
4. **Tool/plugin wrappers**: MCP, Kimi plugin, Coze plugin — only after a real callable API/tool exists around generation, auditing, deployment, or screenshot QA.

Do not build a standalone Chrome extension for distribution. Browser or Chrome automation is a QA capability, not a packaging format for this skill.

## Native Skill Targets

| Target | Fit | Packaging |
|---|---:|---|
| GitHub | High | Public repo plus Releases — primary source of truth, version history, issue tracking. |
| Claude Code | High | Clone into `.claude/skills/business-website-skill/`. `SKILL.md` is the core; references load only when relevant. |
| Codex / OpenAI-style | High | Skills directory plus optional `agents/openai.yaml`. Keep Codex UI metadata isolated. |
| OpenClaw / ClawHub | High | Publish as a text Agent Skill after security and size review. Best registry fit. |
| Gemini CLI | High | Install from GitHub or place under `.gemini/skills/` or `.agents/skills/`. |
| Kimi Code CLI | High | Place under `.kimi/skills/`, `.config/agents/skills/`, or pass `--skills-dir`. |

Wrapper/marketplace targets (Coze, Dify, ChatGPT GPT Store, MCP) are medium-fit: they need a separate bot, workflow, plugin, or callable API. Convert the phase workflow into guided intake → outline → implementation → QA steps for those audiences rather than shipping raw markdown.

## ClawHub Automation

ClawHub publishing is automated from version bumps. `.github/workflows/tag-on-bump.yml` creates the tag/release when `skill.json` version changes, then calls `.github/workflows/clawhub-publish.yml` via `workflow_call` when `CLAWHUB_PUBLISH_ENABLED=true` and the `CLAWHUB_TOKEN` secret is set. Manual dry-runs remain available from the ClawHub workflow's run button.

## Public Release Checklist

Before publishing to any public registry:

1. Run `python3 scripts/audit_static_site.py assets/templates/static-business-site index.html --strict-seo`.
2. Run `python3 -m json.tool skill.json`.
3. Confirm `assets/previews/` contains only lightweight documentation or release links.
4. Confirm `skill.json.compatibility.tested` only lists runtimes with completed end-to-end tests.
5. Confirm copyright reads `Chuluu` and the maintainer website is `https://github.com/ChuluuMGL`.
6. Review all scripts for destructive filesystem commands, network calls, token handling, and hidden data upload.
7. Add platform-specific install notes only after checking that platform's current packaging rules.

Registry and marketplace rules change often. Before publishing, verify the current docs for each target you plan to ship to (ClawHub, Claude Code, Gemini CLI, Kimi Code CLI, SkillsMP, LobeHub Skills, SkillsLLM, Coze, Dify, ChatGPT GPTs).
