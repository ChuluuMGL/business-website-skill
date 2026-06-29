# Business Website Skill

> **面向 AI Agent 的商业官网搭建 Skill**  
> 一个开源 Agent Skill，用于从客户资料、现有网站、PPT/PDF、图片素材、brief 和参考网站中，创建可交付的企业官网、品牌官网、B2B 官网、服务型官网和商业提案级网站。
>
> 由 **月瑀科技 YUEYU TECH** 创建和维护，由 **ChuluuMGL** 发布。

中文 | [English](README.md)

[![AI Skill](https://img.shields.io/badge/AI%20Skill-business--website-0E5E43)](./SKILL.md)
[![Version](https://img.shields.io/badge/version-1.3.6-green)](./skill.json)
[![License: MIT](https://img.shields.io/badge/license-MIT-yellow)](./LICENSE)
[![By YUEYU TECH](https://img.shields.io/badge/by-YUEYU%20TECH-0E5E43)](https://www.yueyu.tech/)
[![Template](https://img.shields.io/badge/template-static--business--site-blue)](./assets/templates/static-business-site/)
[![Workflow](https://img.shields.io/badge/workflow-stage--gated-purple)](./SKILL.md)

---

## 这个 Skill 能做什么

`business-website-skill` 可以把杂乱的网站输入，整理成一套结构清晰、证据安全、可交付的网站生产流程。

| 输出 | 内容 |
|---|---|
| 证据地图 | 已确认事实、缺失信息、禁止编造项和可用素材清单。 |
| 网站蓝图 | 站点地图、首页区块、行动路径、证明模块、案例/场景分类。 |
| 设计方向选项 | 当品牌方向不明确时，提供 2-3 个视觉路线。 |
| 网站实现 | 根据项目情况使用静态 HTML/CSS/JS、React/Vite、Next.js 或现有技术栈。 |
| SEO/GEO 就绪检查 | 页面标题、描述、canonical 假设、社交分享元数据、JSON-LD 候选、可抓取文本和证据摘要模块。 |
| QA 结果 | 断链、锚点、响应式、移动端、事实真实性和交付说明。 |

它的目标不是生成普通落地页，而是帮助客户快速理解：你是谁、解决什么问题、为什么可信、客户下一步该做什么。

---

## 适用场景

| 场景 | 典型需求 |
|---|---|
| 企业官网 | “根据这个 PDF 和品牌素材做一个公司官网。” |
| B2B 服务官网 | “做一个包含能力、案例、流程和咨询入口的 B2B 官网。” |
| 品牌官网 | “把这个品牌资料包转成正式官网。” |
| 提案级落地页 | “为这个提案 / 招商项目做一个客户汇报页面。” |
| 项目展示页 | “做一个工业/技术/项目案例展示页。” |
| 现有网站优化 | “交付客户前，帮我审计并优化这个静态官网。” |
| 网站信息架构规划 | “先给我站点地图、页面大纲和设计方向。” |
| 跨 Agent 复用 | “安装到 Cursor、Claude Code、Trae、OpenClaw、Hermes 或 Codex。” |

---

## 工作流程

这个 Skill 采用类似专业网站策略和商业提案生产的阶段化工作流。

| 阶段 | 检查门 | 产物 |
|---|---|---|
| 0. 问诊 | 判断网站类型、技术栈、视觉方向和交付模式。 | 假设与用户选择 |
| 1. 证据地图 | 区分已确认事实、未知信息和禁止编造项。 | 证据地图 |
| 2. 网站蓝图 | 建立站点地图、首页大纲、证明模块和行动路径。 | 待确认蓝图 |
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
| `guided` | 需要先确认策略和结构。 | 先输出证据地图、站点地图、区块大纲和设计方向。 |
| `auto` | 需要快速得到完整初稿。 | 用保守假设推进，明确标注未知项，并直接实现。 |
| `edit` | 已有网站需要修改。 | 保留现有技术栈和视觉系统，除非用户要求重做。 |
| `audit` | 只需要审阅或诊断。 | 输出问题、风险和修改建议，不重建网站。 |

---

## 网站路线

这个 Skill 不会把所有网站塞进同一套模板，而是根据需求选择主路线：

| 路线 | 适合项目 |
|---|---|
| 企业/集团官网 | 公司介绍、业务、资质、动态、联系。 |
| B2B 服务官网 | 服务范围、场景、证明、流程、询盘行动入口。 |
| 品牌官网 | 品牌故事、定位、产品/服务叙事、视觉识别。 |
| 提案/招商/投标页 | 一次性汇报页面、招商项目、活动提案、投标语境。 |
| 项目展示页 | 案例详情、项目背景、解决方案、成果和媒体素材。 |
| 专业服务官网 | 咨询、代理、制作、运营和专家型服务公司。 |

---

## 包含文件

| 文件 / 目录 | 用途 |
|---|---|
| [`SKILL.md`](./SKILL.md) | Skill 核心元数据和 Agent 指令。 |
| [`NOTICE`](./NOTICE) | 版权、公司、维护者和发布说明。 |
| [`references/agent-experience.md`](./references/agent-experience.md) | Agent 工作模式、最少提问、阶段检查和交付行为。 |
| [`references/delivery-standards.md`](./references/delivery-standards.md) | 版式、字体、配色、图片、交互、响应式和文案标准。 |
| [`references/example-patterns.md`](./references/example-patterns.md) | 从静态站、React 官网和服务型网站提炼的可复用模式。 |
| [`references/benchmark-patterns.md`](./references/benchmark-patterns.md) | 商业官网标杆模式和成熟度检查。 |
| [`references/seo-geo-checklist.md`](./references/seo-geo-checklist.md) | SEO、GEO、AI 搜索就绪、结构化数据、可抓取性和上线索引检查。 |
| [`references/style-presets.md`](./references/style-presets.md) | 主流高级商业网站视觉风格预设。 |
| [`references/interaction-presets.md`](./references/interaction-presets.md) | 交互和动效预设，包括 Anime.js 使用建议。 |
| [`references/preview-guide.md`](./references/preview-guide.md) | 视觉预览、风格重合和动效强度评估说明。 |
| [`references/distribution-platforms.md`](./references/distribution-platforms.md) | 公开发布、市场上架和平台边界说明。 |
| [`references/qa-checklist.md`](./references/qa-checklist.md) | 最终 QA 清单和常见失败模式。 |
| [`assets/presets/design-styles.json`](./assets/presets/design-styles.json) | 机器可读的风格预设目录。 |
| [`assets/presets/interaction-presets.json`](./assets/presets/interaction-presets.json) | 机器可读的交互预设目录。 |
| [`assets/previews/README.md`](./assets/previews/README.md) | Release 托管的风格预览图和交互动效 GIF。 |
| [`assets/templates/static-business-site/`](./assets/templates/static-business-site/) | 无依赖静态官网起步模板。 |
| [`scripts/generate_preview_assets.py`](./scripts/generate_preview_assets.py) | 重新生成风格预览图和交互动效 GIF。 |
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
| Claude Code | `.claude/skills/business-website-skill/` | 维护者已测试 |
| Cursor | `.cursor/skills/business-website-skill/` 或项目 skills 目录 | 预期兼容 |
| Trae | `.trae/skills/business-website-skill/` | 预期兼容 |
| Antigravity | `.agent/skills/business-website-skill/` 或已配置的 skills 目录 | 预期兼容 |
| OpenClaw | OpenClaw 文档指定的 workspace 或 user skills root | 预期兼容 |
| Hermes | `~/.hermes/skills/business-website-skill/` 或已配置的 skills root | 预期兼容 |
| Gemini CLI | `.gemini/skills/business-website-skill/` 或 `.agents/skills/business-website-skill/` | 预期兼容 |
| Kimi Code CLI | `.kimi/skills/business-website-skill/` 或 `.agents/skills/business-website-skill/` | 预期兼容 |

`agents/openai.yaml` 是 Codex 专用 UI 元数据；其他 Agent 可以忽略这个文件，直接读取 `SKILL.md`。

兼容性状态保持保守：只有完成端到端实测的运行时才应写入 `skill.json` 的 `tested`。Claude Code 已由维护者测试；其他列出的运行时在验证前保持预期兼容。

### 可发布平台

GitHub 之外，建议按这个顺序处理：

1. 先把 GitHub 仓库提交到 OpenClaw / ClawHub、SkillsMP、LobeHub Skills、SkillsLLM 这类支持 `SKILL.md` 的目录或索引。
2. 给 Gemini CLI 和 Kimi Code CLI 补明确安装说明，因为它们都支持本地 Agent Skills。
3. 只有当目标用户是非技术业务用户，需要一个引导式 Bot 或 Workflow 时，再做 Coze 包装。
4. Dify、ChatGPT GPT Store、MCP 包装可以作为后续可选渠道，不是第一优先级。

不建议为了发布这个项目单独做 Chrome 插件。浏览器或 Chrome 自动化适合做 QA、截图、响应式检查和线上网站审计；这个 skill 本身应保持轻量的 `SKILL.md` 包。详见 [`references/distribution-platforms.md`](./references/distribution-platforms.md)。

### 更新同步

GitHub 是唯一源头。后续发布 GitHub Release 时，只要仓库 secret 配好 `CLAWHUB_TOKEN`，并把仓库 variable `CLAWHUB_PUBLISH_ENABLED` 设为 `true`，就可以自动发布到 ClawHub。目录/索引型平台可能会重新抓取 GitHub，但时间不保证。Coze、Dify、GPT Store、Gemini CLI 和 Kimi Code CLI 的本地安装不会自动收到 GitHub 更新，除非同步更新它们的包装、知识库或本地 skill。

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
2. 站点地图
3. 首页区块大纲
4. 行动路径
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
- 包含移动导航、行动入口、证明卡片、案例、流程和联系区块
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

### 高级或 Showcase 动效

```text
使用 $business-website-skill 让这个商业网站更高级、更有交互感。

实现前请先给我：
1. standard / premium / showcase 动效推荐
2. 适合使用 Anime.js、GSAP、Lenis、Motion 还是 Three.js
3. 性能和可访问性风险
4. 如果动效太重，最稳妥的降级方案
```

---

## 设计原则

- 从买方的决策问题出发，而不是从服务商的服务清单出发。
- 首屏必须在 5 秒内说明价值。
- 先区分事实和假设，再写文案。
- 使用商业证据：案例、指标、资质、流程、团队、认证、报告或执行证明。
- 设置一个主行动入口和一个次级研究型行动入口。
- 不编造客户、Logo、奖项、新闻和表单提交成功。
- 移动端要和桌面端一样可信。
- 视觉风格是商业信号：B2B 信任、技术清晰、高端品牌或内容专业感。

## SEO 与 GEO 就绪能力

这个 Skill 把 GEO 视为面向 AI 搜索和生成式摘要的证据型 SEO，不使用隐藏文本、虚假 FAQ、无来源 schema 或所谓 AI 专用标记。

公开上线检查包括：

- 可抓取文本说明核心业务、目标客户、证明、流程和下一步行动
- 页面标题、meta 描述、canonical、Open Graph、Twitter Card 和唯一主 `h1`
- 与页面可见内容一致的 JSON-LD
- 清晰的内部链接、站点地图 / robots 状态，以及没有误加 `noindex`
- 能回答真实买方问题的摘要、FAQ、证明和流程模块

静态网站上线前可以运行：

```bash
python3 scripts/audit_static_site.py assets/templates/static-business-site index.html --strict-seo
```

## 内置风格与交互预设

这个 Skill 已内置主流高级商业网站方向的预设说明：

| 风格族 | 适用场景 |
|---|---|
| Executive B2B Trust | 咨询、专业服务、企业级供应商。 |
| Industrial Precision | 制造、能源、工程、环保科技。 |
| AI SaaS / Data Cloud | AI 工具、SaaS 平台、数据分析、自动化。 |
| Premium Editorial Brand | 品牌工作室、思想领导力、文化/策略型网站。 |
| Minimal Luxury | 高端产品、创始人品牌、精品服务。 |
| Dark Data Command Center | 数据看板、诊断工具、AI/运营产品、数据密集服务。 |
| Sustainable Green Tech | ESG、能源、环保、气候科技。 |
| Bold Creative Agency | 创意、制作、营销、活动提案型网站。 |
| Public Sector Civic | 公共服务、NGO、教育、公益和机构型项目。 |
| Fintech Secure | 金融、保险、合规、支付和 B2B 金融科技网站。 |

交互预设分成四档：

| 档位 | 用途 |
|---|---|
| Standard | 适合大多数企业官网和 B2B 官网的安全实用动效。 |
| Premium | 更高级的产品、品牌、案例、SaaS 交互。 |
| Showcase | 更有冲击力的 AI、创意、活动、提案展示型动效。 |
| Accessibility | 所有动效都必须配套的低动效和降级行为。 |

Anime.js 是可选增强：只有在动效能帮助理解业务时才使用，而不是为了炫技。GSAP、Lenis、Motion、Three.js 则用于更高强度的动效，但前提是项目有足够内容、素材和 QA 时间。

### 视觉预览

下面这张确定性预览图由预设目录生成，适合判断这些方向是否足够区分、是否实用：

![商业网站风格预设总览](https://github.com/ChuluuMGL/business-website-skill/releases/download/preview-assets-v1.3.0/style-overview.png)

AI 概念情绪板只作为视觉氛围参考，不应当被当作可复用模板或真实网站输出：

![商业网站风格 AI 概念情绪板](https://github.com/ChuluuMGL/business-website-skill/releases/download/preview-assets-v1.3.0/ai-style-moodboard.jpg)

### 交互动效 GIF 预览

代表性 Standard/Premium 动效预览：

| 交互 | 预览 |
|---|---|
| Anime.js 卡片错峰进入 | ![Anime.js staggered reveal](https://github.com/ChuluuMGL/business-website-skill/releases/download/preview-assets-v1.3.0/animejs-staggered-reveal.gif) |
| Anime.js SVG 线条绘制 | ![Anime.js SVG line draw](https://github.com/ChuluuMGL/business-website-skill/releases/download/preview-assets-v1.3.0/animejs-svg-line-draw.gif) |
| 数字计数 | ![Metric count-up](https://github.com/ChuluuMGL/business-website-skill/releases/download/preview-assets-v1.3.0/metric-count-up.gif) |
| 案例筛选过渡 | ![Case filter transition](https://github.com/ChuluuMGL/business-website-skill/releases/download/preview-assets-v1.3.0/case-filter-transition.gif) |
| 数据面板分层进入 | ![Dashboard panel sequence](https://github.com/ChuluuMGL/business-website-skill/releases/download/preview-assets-v1.3.0/dashboard-panel-sequence.gif) |
| 产品热点导览 | ![Product hotspot tour](https://github.com/ChuluuMGL/business-website-skill/releases/download/preview-assets-v1.3.0/product-hotspot-tour.gif) |

Showcase 级动效预览：

| 交互 | 预览 |
|---|---|
| 滚动钉住叙事 | ![Pinned scroll storytelling](https://github.com/ChuluuMGL/business-website-skill/releases/download/preview-assets-v1.3.0/pinned-scroll-storytelling.gif) |
| Dashboard 滚动变形 | ![Scroll-scrub dashboard morph](https://github.com/ChuluuMGL/business-website-skill/releases/download/preview-assets-v1.3.0/scroll-scrub-dashboard-morph.gif) |
| 横向案例墙 | ![Horizontal case wall](https://github.com/ChuluuMGL/business-website-skill/releases/download/preview-assets-v1.3.0/horizontal-case-wall.gif) |
| Shared layout 过渡 | ![Shared layout transition](https://github.com/ChuluuMGL/business-website-skill/releases/download/preview-assets-v1.3.0/shared-layout-transition.gif) |
| Three.js 产品轨道 Hero | ![Three.js product orbit hero](https://github.com/ChuluuMGL/business-website-skill/releases/download/preview-assets-v1.3.0/threejs-product-orbit-hero.gif) |
| Shader / 液体揭示 | ![Shader liquid reveal](https://github.com/ChuluuMGL/business-website-skill/releases/download/preview-assets-v1.3.0/shader-liquid-reveal.gif) |
| 磁吸媒体 Hover | ![Magnetic media hover](https://github.com/ChuluuMGL/business-website-skill/releases/download/preview-assets-v1.3.0/magnetic-media-hover.gif) |
| 交互式 Orbit Network | ![Interactive orbit network](https://github.com/ChuluuMGL/business-website-skill/releases/download/preview-assets-v1.3.0/interactive-orbit-network.gif) |

完整 GIF 见 [预览资产 Release](https://github.com/ChuluuMGL/business-website-skill/releases/tag/preview-assets-v1.3.0)，重合度和实用性判断见 [`references/preview-guide.md`](./references/preview-guide.md)。

本地重新生成预览时，需要先安装 Pillow，然后运行 `python3 scripts/generate_preview_assets.py`。

### 预览资产策略

PNG/JPG/GIF 预览是托管在 [GitHub Releases](https://github.com/ChuluuMGL/business-website-skill/releases/tag/preview-assets-v1.3.0) 的人类展示资产。Agent 使用这个 Skill 时不需要把它们加载进上下文；真正的执行工作流依赖 `SKILL.md`、`references/`、`assets/presets/`、`assets/templates/` 和 `scripts/`。

主分支只保留轻量预览说明。如果要真正降低普通完整 `git clone` 的历史体积，还需要单独授权并执行 git 历史重写。

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

公开静态网站上线前：

```bash
python3 scripts/audit_static_site.py assets/templates/static-business-site index.html --strict-seo
```

脚本会检查：

- 本地资源引用。
- 哈希锚点。
- 重复 ID。
- 视口 meta。
- 图片 `alt` 属性。
- CSS `url()` 引用。
- title、meta description、`lang`、唯一 `h1`、canonical、Open Graph、Twitter Card、robots 提醒和 JSON-LD 有效性。

---

## 常见问答

**Q：这是电商网站生成器吗？**
A：不是。它面向企业官网、品牌官网、B2B 官网、服务型官网、提案/招商/投标页和项目展示页，不实现购物车或支付结账。

**Q：它会自动创建网站吗？**  
A：可以，前提是在支持文件编辑的 Agent 环境中使用。它可以创建静态原型，也可以在 React/Vite/Next 或现有技术栈中工作。

**Q：需要 MCP 服务器吗？**  
A：不需要。这是本地 Skill 包，不是 MCP Server。

**Q：能使用现有官网或品牌素材吗？**  
A：可以。现有网站、品牌文件夹、PPT/PDF、图片和客户 VI 的优先级高于备用静态模板。

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
| 脚本运行时 | 静态审计脚本只用 Python 标准库；预览生成脚本需要 Pillow |
| License | MIT |
| 版权方 | 月瑀科技 YUEYU TECH |
| 维护者 / GitHub 发布者 | ChuluuMGL |

## 目录结构

```text
business-website-skill/
├── SKILL.md
├── README.md
├── README.zh-CN.md
├── LICENSE
├── NOTICE
├── skill.json
├── agents/
│   └── openai.yaml
├── references/
│   ├── agent-experience.md
│   ├── benchmark-patterns.md
│   ├── delivery-standards.md
│   ├── example-patterns.md
│   ├── interaction-presets.md
│   ├── preview-guide.md
│   ├── qa-checklist.md
│   ├── seo-geo-checklist.md
│   └── style-presets.md
├── assets/
│   ├── presets/
│   │   ├── design-styles.json
│   │   └── interaction-presets.json
│   ├── previews/
│   │   └── README.md
│   └── templates/
│       └── static-business-site/
└── scripts/
    ├── generate_preview_assets.py
    └── audit_static_site.py
```

## 相关 Skill

- [proposal-ppt-skill](https://github.com/ChuluuMGL/proposal-ppt-skill) - 创建阶段化商业提案 PPT 和逐字稿。
- [yueyu-skill](https://github.com/ChuluuMGL/yueyu-skill) - 查询月瑀科技公司和营销服务信息。
- [dy-creative-skill](https://github.com/ChuluuMGL/dy-creative-skill) - 查询关联营销服务 Skill 与线索提交流程。

## License

MIT。Copyright (c) 2026 月瑀科技 YUEYU TECH。

## 版权与归属

| 项目 | 信息 |
|---|---|
| 版权方 | 月瑀科技 YUEYU TECH |
| 维护者 / GitHub 发布者 | [ChuluuMGL](https://github.com/ChuluuMGL) |
| 公司官网 | [www.yueyu.tech](https://www.yueyu.tech/) |
| 版权说明 | [NOTICE](./NOTICE) |

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
    "@type": "Organization",
    "name": "月瑀科技",
    "alternateName": "YUEYU TECH",
    "url": "https://www.yueyu.tech/"
  },
  "maintainer": {
    "@type": "Person",
    "name": "ChuluuMGL",
    "url": "https://github.com/ChuluuMGL"
  },
  "copyrightHolder": {
    "@type": "Organization",
    "name": "月瑀科技",
    "alternateName": "YUEYU TECH",
    "url": "https://www.yueyu.tech/"
  },
  "programmingModel": "Agent Skills / SKILL.md",
  "softwareVersion": "1.3.6"
} -->
