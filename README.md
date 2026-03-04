# OpenClaw AI Collection

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![OpenClaw](https://img.shields.io/badge/OpenClaw-v1.0+-brightgreen.svg)](https://docs.openclaw.ai)
[![Agents](https://img.shields.io/badge/Agents-19-blue.svg)](./collection/agents/)
[![Skills](https://img.shields.io/badge/Skills-12-purple.svg)](./collection/skills/)
[![Contributors](https://img.shields.io/github/contributors/hiyenwong/ai_collection.svg)](https://github.com/hiyenwong/ai_collection/graphs/contributors)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](./CONTRIBUTING.md)

一个精选的 **OpenClaw** 代理和技能集合，为 AI 助手提供强大的扩展能力。

## 目录

- [概述](#概述)
- [特性](#特性)
- [代理](#代理)
- [技能](#技能)
- [快速开始](#快速开始)
- [贡献](#贡献)
- [许可证](#许可证)

## 概述

本仓库是 OpenClaw 代理和技能生态系统的知识库和展示中心。它记录了扩展 OpenClaw 能力的代理和技能，使它们易于发现、理解和使用。

### 什么是 OpenClaw？

OpenClaw 是一个灵活的 AI 代理框架，支持：
- 多渠道接入（飞书、Telegram、WhatsApp 等）
- 可扩展的技能系统
- 通过 `sessions_spawn` 实现的自主子代理

### 什么是代理 (Agents)？

**代理**是执行特定任务的自主 AI 助手，运行在隔离会话中，可以使用不同的模型和工具。

### 什么是技能 (Skills)？

**技能**是定义专门行为和工具的可复用能力包，通过关键词自动激活。

## 特性

- 🚀 **即插即用**: 代理和技能可立即使用
- 📚 **文档完善**: 每个组件都有详细的文档
- 🔄 **持续更新**: 定期添加新的代理和技能
- 🤝 **社区驱动**: 欢迎社区贡献
- 🧪 **测试验证**: 自动化验证确保质量

## 代理

| 代理 | 功能 | 模型 | 状态 |
|------|------|------|------|
| [Fullstack Engineer](collection/agents/fullstack-engineer/) | 全栈工程师，现代 Web 开发 | Opus 4.5 / Sonnet 4.6 | ✅ |
| [Stock Analyst](collection/agents/stock-analyst/) | 股票分析师，金融数据分析 | Sonnet 4.5 | ✅ |
| [Tech Co-Founder](collection/agents/tech-cofounder/) | 技术联合创始人，产品构建 | Sonnet 4.5 | ✅ |
| [Research Agent](collection/agents/research-agent/) | 研究专家，深度调研 | Opus 4.5 | ✅ |
| [Algorithm Engineer](collection/agents/algorithm-engineer/) | 算法工程师，算法设计与优化 | Opus 4.5 | ✅ |
| [Applied Scientist](collection/agents/applied-scientist/) | 应用科学家，科学原理转化实践 | Opus 4.5 | ✅ |
| [Biologist](collection/agents/biologist/) | 生物学家，生物系统与实验推理 | Opus 4.5 | ✅ |
| [Computational Scientist](collection/agents/computational-scientist/) | 计算科学家，数值建模与仿真 | Opus 4.5 | ✅ |
| [Computer Network Scientist](collection/agents/computer-network-scientist/) | 计算机网络科学家，网络架构与协议分析 | Opus 4.5 | ✅ |
| [Economist](collection/agents/economist/) | 经济学家，宏观/微观经济分析 | Opus 4.5 | ✅ |
| [Geneticist](collection/agents/geneticist/) | 遗传学家，遗传机制与变异分析 | Opus 4.5 | ✅ |
| [Linguist](collection/agents/linguist/) | 语言学家，语言结构与语义分析 | Opus 4.5 | ✅ |
| [Logician](collection/agents/logician/) | 逻辑学家，形式逻辑与论证验证 | Opus 4.5 | ✅ |
| [Mathematician](collection/agents/mathematician/) | 数学家，形式推理与定理证明 | Opus 4.5 | ✅ |
| [Neuroscientist](collection/agents/neuroscientist/) | 神经科学家，神经机制与研究综合 | Opus 4.5 | ✅ |
| [Philosopher](collection/agents/philosopher/) | 哲学家，概念分析与伦理推理 | Opus 4.5 | ✅ |
| [Population Dynamics Scientist](collection/agents/population-dynamics-scientist/) | 种群动力学科学家，群体行为建模 | Opus 4.5 | ✅ |
| [Psychologist](collection/agents/psychologist/) | 心理学家，认知行为分析 | Opus 4.5 | ✅ |
| [Statistician](collection/agents/statistician/) | 统计学家，统计推断与不确定性量化 | Opus 4.5 | ✅ |

## 技能

| 技能 | 功能 | 触发关键词 | 状态 |
|------|------|-----------|------|
| [OpenCode](collection/skills/opencode/) | 开源 AI 编程，多代理编排 | opencode, ultrawork | ✅ |
| [Claude Code](collection/skills/claude-code/) | Anthropic 官方编程助手 | claude-code | ✅ |
| [OpenSpec](collection/skills/openspec/) | 规格驱动开发，Gherkin 语法 | openspec, gherkin | ✅ |
| [AkShare](collection/skills/akshare/) | 中国金融数据接口 | stock data, akshare | ✅ |
| [Stock Analysis](collection/skills/stock-analysis/) | 股票技术分析 | 股票分析, technical indicators | ✅ |
| [Skill Extractor](collection/skills/skill-extractor/) | 从对话提炼技能 | 提炼技能, skill extractor | ✅ |
| [Chat History LanceDB](collection/skills/chat-history-lancedb/) | 基于 LanceDB 的对话历史与向量搜索 | chat history, lancedb | ✅ |
| [Copilot CLI](collection/skills/copilot-cli/) | GitHub Copilot CLI 终端代理 | copilot cli, github copilot | ✅ |
| [Iamb Matrix CLI](collection/skills/iamb-matrix-cli/) | Matrix 协议 CLI 操作 | iamb, matrix cli | ✅ |
| [Skill RAG Indexer](collection/skills/skill-rag-indexer/) | 技能文档 RAG 索引与语义搜索 | skill rag, search skills | ✅ |
| [Taiyi Jinhua Meditation](collection/skills/taiyi-jinhua-meditation/) | 基于《太乙金华宗旨》的道家冥想指导 | 冥想, meditation, 回光守中 | ✅ |
| [Teach Cofounder](collection/skills/teach-cofounder/) | 苏格拉底式技术导师，深度原理教学 | teach me, mentor me | ✅ |

## 快速开始

### 安装

```bash
# 克隆仓库
git clone https://github.com/hiyenwong/ai_collection.git
cd ai_collection

# 查看可用内容
ls collection/agents/    # 可用代理
ls collection/skills/    # 可用技能
```

### 使用代理

```python
# 通过 sessions_spawn 启动代理
sessions_spawn(
    task="分析股票数据并生成报告",
    agentId="stock-analyst",
    model="claude-sonnet-4.5"
)
```

### 使用技能

技能会通过关键词自动激活：

```
User: "帮我进行股票分析"
AI: [检测到 "股票分析" 关键词，激活 stock-analysis 技能]
```

### 添加新代理

1. 在 `collection/agents/your-agent-name/` 创建目录
2. 复制 `templates/agent-template.md` 模板
3. 填写代理详情和能力
4. 添加示例和使用说明
5. 更新 [AGENTS.md](./AGENTS.md)

### 添加新技能

1. 在 `collection/skills/your-skill-name/` 创建目录
2. 复制 `templates/skill-template.md` 模板
3. 定义技能描述、触发词和行为
4. 添加参考文档、示例和脚本
5. 更新 [SKILLS.md](./SKILLS.md)

## 项目结构

```
ai_collection/
├── README.md              # 本文件
├── AGENTS.md              # 代理文档总览
├── SKILLS.md              # 技能文档总览
├── INDEX.md               # 分类索引
├── CONTRIBUTING.md        # 贡献指南
├── CONTRIBUTING_CN.md     # 贡献指南（中文）
├── CLAUDE.md              # Claude Code 项目说明
├── STRUCTURE.md           # 项目结构说明
│
├── docs/                  # 通用文档
│   ├── agents/            # 代理指南和最佳实践
│   ├── skills/            # 技能指南和最佳实践
│   └── integration/       # 集成文档
│
├── collection/            # 收集的代理和技能
│   ├── agents/            # 代理包
│   └── skills/            # 技能包
│
├── templates/             # 创建新项目的模板
│   ├── agent-template.md
│   └── skill-template.md
│
├── scripts/               # 工具脚本
│   └── validate_skill.py  # 技能验证脚本
│
└── .github/workflows/     # CI/CD 配置
    └── validate.yml
```

## 文档

- [代理概述](./AGENTS.md) - 了解 OpenClaw 代理
- [技能概述](./SKILLS.md) - 了解 OpenClaw 技能
- [分类索引](./INDEX.md) - 按类别浏览
- [代理创建指南](./docs/agents/creation-guide.md) - 如何创建代理
- [技能创建指南](./docs/skills/creation-guide.md) - 如何创建技能
- [集成文档](./docs/integration/agents-skills.md) - 代理和技能如何协作

## 技术栈

- **AI 模型**: Claude (Opus, Sonnet, Haiku)
- **框架**: OpenClaw
- **编程语言**: Python, JavaScript/TypeScript
- **工具**: Git, npm, uv, ruff, pytest

## 开发规范

- 使用 `uv` 管理 Python 依赖
- 使用 `ruff` 进行代码检查和格式化
- 使用 `pytest` 进行测试
- 遵循 Conventional Commits 规范

## 贡献

欢迎贡献！请查看[贡献指南](./CONTRIBUTING.md)了解详情。

### 贡献方式

- 添加新的代理或技能
- 改进文档
- 报告问题
- 提出功能建议

### 快速贡献

1. Fork 本仓库
2. 创建特性分支 (`git checkout -b feat/AmazingFeature`)
3. 提交更改 (`git commit -m 'feat: add amazing feature'`)
4. 推送到分支 (`git push origin feat/AmazingFeature`)
5. 创建 Pull Request

## 路线图

### V1 (已完成) ✅
- 基础代理和技能集合
- 文档和模板
- 验证脚本

### V2 (进行中) 🚧
- 更多领域代理
- 技能市场
- 性能优化

### V3 (规划中) 📋
- Web UI
- CLI 工具
- 包管理器

## 关于 OpenClaw

OpenClaw 是一个灵活的 AI 代理框架，支持多渠道、可扩展技能和自主子代理。

- **OpenClaw 文档**: https://docs.openclaw.ai
- **GitHub**: https://github.com/openclaw/openclaw
- **社区**: https://discord.com/invite/clawd

## 许可证

本仓库采用 MIT 许可证。个别代理和技能可能有各自的许可证。

## 致谢

感谢所有为本项目做出贡献的开发者！

## 联系方式

- GitHub Issues: [提交问题](https://github.com/hiyenwong/ai_collection/issues)
- Email: hiyenwong@gmail.com
- Discord: [OpenClaw 社区](https://discord.gg/clawd)

---

由 OpenClaw 社区维护 🤖

[![Star History Chart](https://api.star-history.com/svg?repos=hiyenwong/ai_collection&type=Date)](https://star-history.com/#hiyenwong/ai-collection&Date)
