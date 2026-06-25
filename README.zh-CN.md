# Business Website Skill

中文说明 | [English](README.md)

用于从客户资料、现有页面、PPT/PDF、图片素材和参考网站中，搭建可交付的企业官网、品牌官网、B2B 官网、服务型官网和商业提案级网站原型。

这个 Agent Skill 面向客户交付场景：企业展示、品牌官网、项目展示页、招商/投标页面、正式汇报预览和可上线前评审的网站原型。它不以电商店铺、购物车、支付结账为核心。

## 能做什么

- 把源资料转成阶段化的网站搭建计划。
- 区分已确认事实、待确认信息和禁止编造内容。
- 在实现前产出 sitemap、页面大纲和首页区块结构。
- 当用户没有明确视觉方向时，提供 2-3 个设计方向供选择。
- 优先沿用现有技术栈，也可以从静态 HTML/CSS/JS 模板快速开始。
- 提供静态站交付检查，并指导 React/Vite/Next 项目的验证流程。

## 适用场景

- 企业官网、集团官网、品牌官网。
- B2B 产品/服务官网。
- 专业服务公司官网。
- 项目展示页、招商页、投标/汇报型网站。
- 客户提案级网站原型。
- 已有官网的结构优化、视觉 polish 和交付前 QA。

## 不适合

- 电商店铺。
- 购物车和支付结账实现。
- 需要真实后端提交但没有后端接口的表单功能。
- 没有资料来源却要求编造客户、案例、资质或效果数据的网站。

## Skill 内容

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
├── README.md
└── README.zh-CN.md
```

## 核心工作流

Skill 会引导 Agent 按阶段推进，而不是直接开始写页面：

1. **Intake / 问诊**  
   明确网站类型、交付形态、技术栈、视觉方向和目标受众。

2. **Evidence Map / 证据地图**  
   读取资料，区分可发布事实、待确认信息、禁止编造项和可用素材。

3. **Site Blueprint / 网站大纲**  
   产出 sitemap、首页区块、核心 CTA、证据模块和案例分类。

4. **Design Direction / 设计方向**  
   在方向不明确时提供 2-3 个方案，例如稳重 B2B、数据科技感、高端品牌感。

5. **Implementation Plan / 实施计划**  
   明确文件结构、组件、素材目录、交互模块和验证命令。

6. **Build / 实现**  
   按项目技术栈构建页面、组件、样式和交互。

7. **QA / 验收**  
   检查断链、锚点、图片、移动端、表单反馈、事实真实性和响应式布局。

8. **Handoff / 交付说明**  
   输出修改内容、文件位置、运行方式、验证结果和待补充项。

## 推荐提示词

```text
Use $business-website-skill to build a client-ready B2B website from the materials in this folder.
```

```text
Use $business-website-skill to audit and polish this static company website before client delivery.
```

```text
Use $business-website-skill to create a proposal-grade landing page. Ask me for choices before implementation.
```

中文也可以这样说：

```text
使用 $business-website-skill，根据这个文件夹里的资料搭建一个可交付的企业官网原型。
```

```text
使用 $business-website-skill，先给我网站大纲和 3 个视觉方向，确认后再实现。
```

## 安装与兼容性

核心结构遵循开放的 Agent Skills 形态：一个包含 `SKILL.md` 的目录，并可选包含 `references/`、`scripts/`、`assets/`。多数兼容 Agent 只需要把整个目录放到它们会扫描的 skills 目录下。

| Agent/runtime | 建议安装路径 | 状态 |
|---|---|---|
| Codex | `.agents/skills/business-website-skill/` 或用户级 skills 目录 | 已支持 |
| Claude Code | `.claude/skills/business-website-skill/` | 预期兼容 |
| Cursor | `.cursor/skills/business-website-skill/` 或项目 skills 目录 | 预期兼容 |
| Trae | `.trae/skills/business-website-skill/` | 预期兼容 |
| Antigravity | `.agent/skills/business-website-skill/` 或已配置的 skills 目录 | 预期兼容 |
| OpenClaw | OpenClaw 文档指定的 workspace 或 user skills root | 预期兼容 |
| Hermes | `~/.hermes/skills/business-website-skill/` 或已配置的 skills root | 预期兼容 |

`agents/openai.yaml` 是 Codex 专用的 UI 元数据；其他 Agent 可以忽略这个文件，直接读取 `SKILL.md`。

### 通用安装

```bash
git clone https://github.com/ChuluuMGL/business-website-skill.git .agents/skills/business-website-skill
```

SSH：

```bash
git clone git@github.com:ChuluuMGL/business-website-skill.git .agents/skills/business-website-skill
```

支持显式调用的 Agent 可以这样调用：

```text
$business-website-skill
```

### 常见 Agent 安装示例

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

OpenClaw 和其他运行时可能使用可配置的 workspace/global skills root。把仓库克隆到对应扫描目录即可。

## 兼容性说明

- `SKILL.md` 必须保持大写；部分运行时大小写敏感。
- 目录名建议保持 kebab-case：`business-website-skill`。
- `skill.json` 是公开元数据；不读取它的 Agent 可以忽略。
- Python 审计脚本只依赖标准库。
- 如果某个运行时不支持执行脚本，仍可以把本 Skill 当作工作流说明和模板资源使用；审计脚本可手动运行。
- 如果某个运行时不支持弹窗式选项，Skill 会要求 Agent 用文字列出 2-3 个选项让用户选择。

## 静态模板

内置模板是通用、安全、可公开的结构模板：

```text
assets/templates/static-business-site/
├── index.html
├── index.css
└── index.js
```

模板使用 `待补充`、`示例待确认` 等占位文案。正式交付前必须替换成有来源的真实信息，或明确保留为待确认项。

## 静态站审计

运行：

```bash
python3 scripts/audit_static_site.py assets/templates/static-business-site index.html
```

脚本会检查：

- 本地资源是否存在。
- hash 锚点是否有效。
- 是否有重复 ID。
- 是否有 viewport meta。
- 图片是否缺少 alt。
- CSS `url()` 引用的资源是否存在。

## 当前成熟度

这是一个实用 v1 版本。当前最强的是：

- 阶段化建站流程。
- 证据安全和防编造约束。
- 商业官网信息架构。
- 静态原型模板。
- 交付前基础审计。

后续最值得补强的是：

- 更多行业模板。
- React/Vite/Next 起步模板。
- Playwright 视觉 QA。
- SEO/结构化数据模板。
- 各 Agent 的实测兼容矩阵。

## License

MIT
