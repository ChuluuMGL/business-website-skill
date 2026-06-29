# Runtime Testing Matrix

This matrix records what has been checked for `business-website-skill`. Keep it conservative: only mark a runtime as verified after an end-to-end install and realistic task run.

## Status Legend

| Status | Meaning |
|---|---|
| `verified` | Installed and used on a realistic task or full workflow. |
| `cli-detected` | CLI was found locally and basic version detection worked, but no full skill task was run. |
| `documented` | Install path and expected behavior are documented, but not yet tested locally. |
| `pending` | Needs environment setup or user-provided runtime access. |

## Current Matrix

| Runtime | Status | Evidence | Next Step |
|---|---|---|---|
| Codex | verified | Skill installed locally and used to maintain this repository. `codex-cli 0.137.0` detected on 2026-06-29. | Keep testing after major workflow changes. |
| Claude Code | verified | Maintainer reported successful skill run. `Claude Code 2.1.162` detected on 2026-06-29. | Capture one reusable sample prompt and output summary. |
| Cursor | cli-detected | `cursor 3.5.38` detected on 2026-06-29. | Install into `.cursor/skills/` and run the guided blueprint prompt. |
| Trae | cli-detected | `trae 1.107.1` detected on 2026-06-29. | Install into `.trae/skills/` and run static prototype prompt. |
| OpenClaw | cli-detected | `OpenClaw 2026.6.1` detected on 2026-06-29. | Run ClawHub dry-run and one skill invocation. |
| Hermes | cli-detected | `Hermes Agent v0.15.1` detected on 2026-06-29. | Install into Hermes skills root and run audit prompt. |
| Gemini CLI | documented | Install path documented; CLI not found locally on 2026-06-29. | Install Gemini CLI and run one guided blueprint test. |
| Kimi Code CLI | documented | Install path documented; CLI not found locally on 2026-06-29. | Install Kimi Code CLI and run one guided blueprint test. |
| Antigravity | documented | Expected compatible via filesystem skill folder. | Confirm actual skills root and run one static prototype test. |

## Showcase Site

| Item | Status | Evidence |
|---|---|---|
| Vercel production site | verified | https://business-website-skill.vercel.app returned HTTP 200 on 2026-06-29. |
| Local site build | verified | `npm run build:site` copied `site/` to `public/`. |
| Local site audit | verified | `npm run validate:site` passed `--strict-seo --no-placeholders`. |

## Recommended Smoke Tests

### Guided Blueprint

```text
Use $business-website-skill to create a client-ready business website from the materials in this folder.

Do not implement yet. First return an evidence map, sitemap, homepage outline, CTA path, 3 design directions, and questions that need confirmation.
```

Pass condition:

- The agent reads real files first.
- It separates confirmed facts from pending facts.
- It does not invent customers, years, metrics, addresses, or awards.

### Static Prototype

```text
Use $business-website-skill to build a static B2B website prototype from the provided brief. Use source-backed facts only, mark unknowns as pending, and run the static audit script before handoff.
```

Pass condition:

- The output contains a coherent commercial website structure.
- The static audit passes.
- Any unresolved facts remain marked pending.

### Final Delivery Audit

```bash
python3 scripts/audit_static_site.py <site-root> index.html --strict-seo --no-placeholders
```

Pass condition:

- No broken anchors or missing assets.
- Required launch metadata exists.
- No unresolved placeholder content remains.
