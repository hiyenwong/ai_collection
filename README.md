# OpenClaw AI Collection

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![OpenClaw](https://img.shields.io/badge/OpenClaw-v1.0+-brightgreen.svg)](https://docs.openclaw.ai)

一个精选的 **OpenClaw** 代理和技能集合，为 AI 助手提供强大的扩展能力。

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

## 快速导航

### 代理 (Agents)

| 代理 | 功能 | 模型 |
|------|------|------|
| [Fullstack Engineer](collection/agents/fullstack-engineer/) | 全栈工程师，现代 Web 开发 | Opus 4.5 / Sonnet 4.6 |
| [Stock Analyst](collection/agents/stock-analyst/) | 股票分析师，金融数据分析 | Sonnet 4.5 |
| [Tech Co-Founder](collection/agents/tech-cofounder/) | 技术联合创始人，产品构建 | Sonnet 4.5 |
| [Research Agent](collection/agents/research-agent/) | 研究专家，深度调研 | Opus 4.5 |

### 技能 (Skills)

| 技能 | 功能 | 触发关键词 |
|------|------|-----------|
| [OpenCode](collection/skills/opencode/) | 开源 AI 编程，多代理编排 | opencode, ultrawork |
| [Claude Code](collection/skills/claude-code/) | Anthropic 官方编程助手 | claude-code |
| [OpenSpec](collection/skills/openspec/) | 规格驱动开发，Gherkin 语法 | openspec, gherkin |
| [AkShare](collection/skills/akshare/) | 中国金融数据接口 | stock data, akshare |
| [Stock Analysis](collection/skills/stock-analysis/) | 股票技术分析 | 股票分析, technical indicators |
| [Skill Extractor](collection/skills/skill-extractor/) | 从对话提炼技能 | 提炼技能, skill extractor |

## 快速开始

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
├── CONTRIBUTING.md        # 贡献指南
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
│   │   ├── fullstack-engineer/
│   │   ├── stock-analyst/
│   │   ├── tech-cofounder/
│   │   └── research-agent/
│   └── skills/            # 技能包
│       ├── opencode/
│       ├── claude-code/
│       ├── openspec/
│       ├── akshare/
│       ├── stock-analysis/
│       └── skill-extractor/
│
├── templates/             # 创建新项目的模板
│   ├── agent-template.md
│   └── skill-template.md
│
└── resources/             # 外部资源和链接
```

## 文档

- [代理概述](./AGENTS.md) - 了解 OpenClaw 代理
- [技能概述](./SKILLS.md) - 了解 OpenClaw 技能
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

## 关于 OpenClaw

OpenClaw 是一个灵活的 AI 代理框架，支持多渠道、可扩展技能和自主子代理。

- **OpenClaw 文档**: https://docs.openclaw.ai
- **GitHub**: https://github.com/openclaw/openclaw
- **社区**: https://discord.com/invite/clawd

## 许可证

本仓库采用 MIT 许可证。个别代理和技能可能有各自的许可证。

---

由 OpenClaw 社区维护 🤖

[![Star History Chart](https://api.star-history.com/svg?repos=openclaw/ai-collection&type=Date)](https://star-history.com/#openclaw/ai-collection&Date)
