# Business Website Skill

> **面向 AI Agent 的商业官网搭建 Skill**  
> 一个开源 Agent Skill，用于从客户资料、现有网站、PPT/PDF、图片素材、brief 和参考网站中，创建可交付的企业官网、品牌官网、B2B 官网、服务型官网和商业提案级网站。

中文 | [English](README.md)

[![AI Skill](https://img.shields.io/badge/AI%20Skill-business--website-0E5E43)](./SKILL.md)
[![Version](https://img.shields.io/badge/version-1.0.1-green)](./skill.json)
[![License: MIT](https://img.shields.io/badge/license-MIT-yellow)](./LICENSE)
[![Template](https://img.shields.io/badge/template-static--business--site-blue)](./assets/templates/static-business-site/)
[![Workflow](https://img.shields.io/badge/workflow-stage--gated-purple)](./SKILL.md)

---

## 这个 Skill 能做什么

`business-website-skill` 可以把杂乱的网站输入，整理成一套结构清晰、证据安全、可交付的网站生产流程。

| 输出 | 内容 |
|---|---|
| 证据地图 | 已确认事实、缺失信息、禁止编造项和可用素材清单。 |
| 网站蓝图 | sitemap、首页区块、CTA 路径、证明模块、案例/场景分类。 |
| 设计方向选项 | 当品牌方向不明确时，提供 2-3 个视觉路线。 |
| 网站实现 | 根据项目情况使用静态 HTML/CSS/JS、React/Vite、Next.js 或现有技术栈。 |
| QA 结果 | 断链、锚点、响应式、移动端、事实真实性和交付说明。 |

它的目标不是生成普通 landing page，而是帮助客户快速理解：你是谁、解决什么问题、为什么可信、客户下一步该做什么。

---

## 适用场景

| 场景 | 典型需求 |
|---|---|
| 企业官网 | “根据这个 PDF 和品牌素材做一个公司官网。” |
| B2B 服务官网 | “做一个包含能力、案例、流程和咨询入口的 B2B 官网。” |
| 品牌官网 | “把这个品牌 deck 转成正式官网。” |
| 提案级落地页 | “为这个 pitch / 招商项目做一个客户汇报页面。” |
| 项目展示页 | “做一个工业/技术/项目案例展示页。” |
| 现有网站优化 | “交付客户前，帮我审计和 polish 这个静态官网。” |
| 网站 IA 规划 | “先给我 sitemap、页面大纲和设计方向。” |
| 跨 Agent 复用 | “安装到 Cursor、Claude Code、Trae、OpenClaw、Hermes 或 Codex。” |

---

## 工作流程

这个 Skill 采用类似专业网站策略和商业提案生产的阶段化工作流。

| 阶段 | 检查门 | 产物 |
|---|---|---|
| 0. 问诊 | 判断网站类型、技术栈、视觉方向和交付模式。 | 假设与用户选择 |
| 1. 证据地图 | 区分已确认事实、未知信息和禁止编造项。 | 证据地图 |
| 2. 网站蓝图 | 建立 sitemap、首页大纲、证明模块和 CTA 路径。 | 待确认蓝图 |
| 3. 设计方向 | 品牌方向不明确时，给出 2-3 个视觉路线。 | 方向选项 |
| 4. 实施计划 | 明确文件、组件、素材、交互和检查方式。 | 构建计划 |
| 5. 构建 | 用静态文件、React/Vite/Next 或现有技术栈实现。 | 网站文件 |
| 6. QA | 检查事实、资源、锚点、版式、移动端、表单和交付状态。 | QA 结果 |
| 7. 交付 | 汇总文件、预览方式、验证结果和待确认项。 | 交付说明 |

默认行为是务实的：如果用户需要速度，Agent 会用保守假设推进，并把未知项标为待确认；如果用户需要控制，Agent 会先停在蓝图和设计方向阶段等待确认。

---

## 工作模式

| 模式 | 适用情况 | 行为 |
|---|---|---|
| `guided` | 需要先确认策略和结构。 | 先输出证据地图、sitemap、区块大纲和设计方向。 |
| `auto` | 需要快速得到完整初稿。 | 用保守假设推进，明确标注未知项，并直接实现。 |
| `edit` | 已有网站需要修改。 | 保留现有技术栈和视觉系统，除非用户要求重做。 |
| `audit` | 只需要审阅或诊断。 | 输出问题、风险和修改建议，不重建网站。 |

---

## 网站路线

这个 Skill 不会把所有网站塞进同一套模板，而是根据需求选择主路线：

| 路线 | 适合项目 |
|---|---|
| 企业/集团官网 | 公司介绍、业务、资质、动态、联系。 |
| B2B 服务官网 | 服务范围、场景、证明、流程、询盘 CTA。 |
| 品牌官网 | 品牌故事、定位、产品/服务叙事、视觉识别。 |
| 提案/招商/投标页 | 一次性汇报页面、招商项目、活动提案、投标语境。 |
| 项目展示页 | 案例详情、项目背景、解决方案、成果和媒体素材。 |
| 专业服务官网 | 咨询、代理、制作、运营和专家型服务公司。 |

---

## 包含文件

| 文件 / 目录 | 用途 |
|---|---|
| [`SKILL.md`](./SKILL.md) | Skill 核心元数据和 Agent 指令。 |
| [`references/delivery-standards.md`](./references/delivery-standards.md) | 版式、字体、配色、图片、交互、响应式和文案标准。 |
| [`references/example-patterns.md`](./references/example-patterns.md) | 从静态站、React 官网和服务型网站提炼的可复用模式。 |
| [`references/benchmark-patterns.md`](./references/benchmark-patterns.md) | 商业官网标杆模式和成熟度检查。 |
| [`references/qa-checklist.md`](./references/qa-checklist.md) | 最终 QA 清单和常见失败模式。 |
| [`assets/templates/static-business-site/`](./assets/templates/static-business-site/) | 无依赖静态官网起步模板。 |
| [`scripts/audit_static_site.py`](./scripts/audit_static_site.py) | 只使用 Python 标准库的静态站审计脚本。 |
| [`agents/openai.yaml`](./agents/openai.yaml) | Codex / OpenAI 风格 Skill UI 元数据。 |
| [`skill.json`](./skill.json) | 供目录、市场和其他 Agent 读取的机器可读元数据。 |

静态模板只作为结构起点。正式交付前必须把 `待补充`、`待确认` 和示例占位替换为有来源的真实信息。

---

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

`agents/openai.yaml` 是 Codex 专用 UI 元数据；其他 Agent 可以忽略这个文件，直接读取 `SKILL.md`。

### 让 AI Agent 帮你安装

可以直接对支持代码操作的 AI Agent 说：

> 帮我安装 business-website-skill，仓库地址：https://github.com/ChuluuMGL/business-website-skill

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

---

## 推荐提示词

### 先出蓝图，再确认

```text
使用 $business-website-skill 根据当前文件夹里的资料创建一个可交付的企业官网。

先不要实现。请先输出：
1. 证据地图
2. sitemap
3. 首页区块大纲
4. CTA 路径
5. 3 个设计方向
6. 需要我确认的问题
```

### 直接做静态原型

```text
使用 $business-website-skill 搭建一个静态 B2B 官网原型。

要求：
- 只使用有来源的事实
- 缺失信息标注待确认
- 可以从 static-business-site 模板开始
- 包含移动导航、CTA、证明卡片、案例、流程和联系区块
- 最终运行静态审计脚本
```

### 审计现有官网

```text
使用 $business-website-skill 审计并优化这个现有公司官网。

目标：
- 提升首屏业务价值表达
- 检查证据和未支撑表述
- 修复响应式布局问题
- 验证锚点、图片、移动菜单和表单反馈
- 返回 QA 问题并实现安全修改
```

---

## 设计原则

- 从买方的决策问题出发，而不是从服务商的服务清单出发。
- 首屏必须在 5 秒内说明价值。
- 先区分事实和假设，再写文案。
- 使用商业证据：案例、指标、资质、流程、团队、认证、报告或执行证明。
- 设置一个主 CTA 和一个次级研究型 CTA。
- 不编造客户、Logo、奖项、新闻和表单提交成功。
- 移动端要和桌面端一样可信。
- 视觉风格是商业信号：B2B 信任、技术清晰、高端品牌或内容专业感。

---

## 静态模板

内置模板是通用、安全、可公开的结构模板：

```text
assets/templates/static-business-site/
├── index.html
├── index.css
└── index.js
```

模板使用 `待补充`、`示例待确认` 等占位文案。正式交付前必须替换成有来源的真实信息，或明确保留为待确认项。

---

## 静态站审计

运行：

```bash
python3 scripts/audit_static_site.py assets/templates/static-business-site index.html
```

脚本会检查：

- 本地资源引用。
- hash 锚点。
- 重复 ID。
- viewport meta。
- 图片 `alt` 属性。
- CSS `url()` 引用。

---

## 常见问答

**Q：这是电商网站 builder 吗？**  
A：不是。它面向企业官网、品牌官网、B2B 官网、服务型官网、提案/招商/投标页和项目展示页，不实现购物车或支付结账。

**Q：它会自动创建网站吗？**  
A：可以，前提是在支持文件编辑的 Agent 环境中使用。它可以创建静态原型，也可以在 React/Vite/Next 或现有技术栈中工作。

**Q：需要 MCP 服务器吗？**  
A：不需要。这是本地 Skill 包，不是 MCP Server。

**Q：能使用现有官网或品牌素材吗？**  
A：可以。现有网站、品牌文件夹、PPT/PDF、图片和客户 VI 的优先级高于 fallback 静态模板。

**Q：会不会编造客户案例或数据？**  
A：不会。Skill 要求未知信息标注为 `待补充`、`待确认` 或 `示例待确认`。

**Q：其他 Agent 可以用吗？**  
A：可以，只要对应 Agent 支持 Skill 文件夹，或能读取 `SKILL.md` 风格的 Skill 包。不同客户端安装路径不同。

---

## 技术规格

| 项目 | 说明 |
|---|---|
| Skill 名称 | `business-website-skill` |
| 仓库 | `ChuluuMGL/business-website-skill` |
| 形态 | 本地 Skill 文件夹，包含 `SKILL.md`、references、scripts、assets 和 metadata |
| 主要输出 | 网站文件、证据地图、网站蓝图、QA 和交付说明 |
| 内置资产 | 静态商业官网起步模板 |
| 脚本运行时 | Python 标准库 |
| License | MIT |
| 作者 | ChuluuMGL |

## 目录结构

```text
business-website-skill/
├── SKILL.md
├── README.md
├── README.zh-CN.md
├── LICENSE
├── skill.json
├── agents/
│   └── openai.yaml
├── assets/
│   └── templates/
│       └── static-business-site/
├── references/
│   ├── benchmark-patterns.md
│   ├── delivery-standards.md
│   ├── example-patterns.md
│   └── qa-checklist.md
└── scripts/
    └── audit_static_site.py
```

## 相关 Skill

- [proposal-ppt-skill](https://github.com/ChuluuMGL/proposal-ppt-skill) - 创建阶段化商业提案 PPT 和逐字稿。
- [yueyu-skill](https://github.com/ChuluuMGL/yueyu-skill) - 查询月瑀科技公司和营销服务信息。
- [dy-creative-skill](https://github.com/ChuluuMGL/dy-creative-skill) - 查询大瑀创意科技营销服务和线索提交。

## License

MIT

---

<!-- Structured Data for SEO: JSON-LD -->
<!-- {
  "@context": "https://schema.org",
  "@type": "SoftwareApplication",
  "name": "business-website-skill",
  "alternateName": "商业官网搭建 Skill",
  "description": "开源 AI Agent Skill，用于从客户资料创建可交付的企业官网、品牌官网、B2B 官网、服务型官网和商业提案级网站。",
  "url": "https://github.com/ChuluuMGL/business-website-skill",
  "applicationCategory": "DeveloperApplication",
  "operatingSystem": "Any",
  "offers": {
    "@type": "Offer",
    "price": "0",
    "priceCurrency": "USD",
    "description": "Skill 开源免费，MIT 协议"
  },
  "author": {
    "@type": "Person",
    "name": "ChuluuMGL",
    "url": "https://github.com/ChuluuMGL"
  },
  "programmingModel": "Agent Skills / SKILL.md",
  "softwareVersion": "1.0.1"
} -->
