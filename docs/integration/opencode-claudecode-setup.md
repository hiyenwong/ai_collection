# OpenCode & Claude Code 集成指南

本指南说明如何将 OpenClaw AI Collection 中的所有代理和技能集成到 OpenCode 和 Claude Code 中。

## 概述

**OpenClaw AI Collection** 包含 5 个专业代理和 7 个技能，可以通过以下方式集成：

1. **OpenCode**: 通过 `oh-my-opencode.json` 配置代理
2. **Claude Code**: 通过 `.claude/AGENTS.md` 注入代理上下文
3. **技能触发**: 通过激活关键词自动使用技能

## 支持的代理和技能

### 代理 (Agents)

| 代理 | 路径 | 主要用途 | 推荐模型 |
|------|------|----------|----------|
| fullstack-engineer | `collection/agents/fullstack-engineer/` | 全栈开发 | claude-opus-4.5 |
| algorithm-engineer | `collection/agents/algorithm-engineer/` | 算法与 ML | claude-opus-4.5 |
| tech-cofounder | `collection/agents/tech-cofounder/` | 产品构建 | claude-sonnet-4.5 |
| research-agent | `collection/agents/research-agent/` | 研究调研 | claude-opus-4.5 |
| stock-analyst | `collection/agents/stock-analyst/` | 股票分析 | claude-sonnet-4.5 |

### 技能 (Skills)

| 技能 | 路径 | 激活词 |
|------|------|--------|
| opencode | `collection/skills/opencode/` | opencode, ultrawork |
| claude-code | `collection/skills/claude-code/` | claude-code |
| openspec | `collection/skills/openspec/` | openspec, gherkin |
| skill-extractor | `collection/skills/skill-extractor/` | 提炼技能, extract skill |
| skill-rag-indexer | `collection/skills/skill-rag-indexer/` | 搜索技能, skill search |
| stock-analysis | `collection/skills/stock-analysis/` | 股票分析, technical indicators |
| akshare | `collection/skills/akshare/` | stock data, akshare |

## OpenCode 集成配置

### 1. 基础配置

在项目根目录创建 `.opencode/oh-my-opencode.json`：

```json
{
  "agents": {
    "fullstack_engineer": {
      "model": "anthropic/claude-opus-4.5",
      "systemPrompt": "Read collection/agents/fullstack-engineer/AGENT.md",
      "description": "Senior full-stack engineer for web applications"
    },
    "algorithm_engineer": {
      "model": "anthropic/claude-opus-4.5",
      "systemPrompt": "Read collection/agents/algorithm-engineer/AGENT.md",
      "description": "Algorithm specialist for ML and optimization"
    },
    "tech_cofounder": {
      "model": "anthropic/claude-sonnet-4.5",
      "systemPrompt": "Read collection/agents/tech-cofounder/AGENT.md",
      "description": "Technical co-founder for product building"
    },
    "research_agent": {
      "model": "anthropic/claude-opus-4.5",
      "systemPrompt": "Read collection/agents/research-agent/AGENT.md",
      "description": "Research specialist for deep investigation"
    },
    "stock_analyst": {
      "model": "anthropic/claude-sonnet-4.5",
      "systemPrompt": "Read collection/agents/stock-analyst/AGENT.md",
      "description": "Stock analyst for financial data and trading"
    }
  },
  "skills": [
    "openspec",
    "skill-extractor",
    "skill-rag-indexer",
    "stock-analysis",
    "akshare"
  ]
}
```

### 2. 使用代理

在 OpenCode 中调用特定代理：

```
Use fullstack_engineer to build a React dashboard with TypeScript
```

```
Use algorithm_engineer to optimize the sorting algorithm in src/utils/sort.js
```

```
Use tech_cofounder to quickly prototype an MVP for user authentication
```

### 3. Ultrawork 模式结合代理

```
Build a complete e-commerce platform using fullstack_engineer with ultrawork
```

这将使用 fullstack-engineer 的专业知识，同时启用 ultrawork 的多代理编排。

## Claude Code 集成配置

### 1. 创建代理上下文文件

在项目根目录创建 `.claude/AGENTS.md`：

```markdown
# OpenClaw AI Collection Agents

本项目中可用的专业代理：

## Fullstack Engineer
**位置:** `../collection/agents/fullstack-engineer/`
**用于:** 完整的 Web 应用开发、架构设计
**激活:** "使用 fullstack-engineer" 或 "Use fullstack-engineer"

## Algorithm Engineer
**位置:** `../collection/agents/algorithm-engineer/`
**用于:** 算法设计、优化、机器学习模型
**激活:** "使用 algorithm-engineer" 或 "Use algorithm-engineer"

## Tech Co-Founder
**位置:** `../collection/agents/tech-cofounder/`
**用于:** 产品原型、MVP 开发
**激活:** "使用 tech-cofounder" 或 "Use tech-cofounder"

## Research Agent
**位置:** `../collection/agents/research-agent/`
**用于:** 深度调研、文档编写
**激活:** "使用 research-agent" 或 "Use research-agent"

## Stock Analyst
**位置:** `../collection/agents/stock-analyst/`
**用于:** 股票分析、交易策略
**激活:** "使用 stock-analyst" 或 "Use stock-analyst"

## 技能 (Skills)

### OpenSpec
**位置:** `../collection/skills/openspec/`
**激活词:** openspec, gherkin, BDD
**用于:** 规格驱动开发

### Skill Extractor
**位置:** `../collection/skills/skill-extractor/`
**激活词:** 提炼技能, extract skill, skill extractor
**用于:** 从对话中提取技能模式

### Skill RAG Indexer
**位置:** `../collection/skills/skill-rag-indexer/`
**激活词:** 搜索技能, skill search, skill rag
**用于:** 语义搜索技能

### Stock Analysis
**位置:** `../collection/skills/stock-analysis/`
**激活词:** 股票分析, technical indicators, MACD
**用于:** 股票技术分析

### AkShare
**位置:** `../collection/skills/akshare/`
**激活词:** stock data, akshare
**用于:** 中国金融数据接口
```

### 2. 使用代理

在 Claude Code 会话中引用代理：

```
使用 fullstack-engineer 的方法来构建这个 React 应用
```

```
Use algorithm-engineer approach to optimize the data processing pipeline
```

### 3. 技能自动激活

技能会通过关键词自动激活：

```
用户: "帮我提炼一个技能"
AI: [检测到 "提炼技能"，激活 skill-extractor 技能]
```

## 快速开始

### 方法 1: 复制配置

```bash
# 1. 复制集成配置
cp docs/integration/opencode-config.json .opencode/oh-my-opencode.json

# 2. 复制 Claude Code 代理上下文
mkdir -p .claude
cp docs/integration/claude-code-agents.md .claude/AGENTS.md

# 3. 启动 OpenCode
opencode

# 或启动 Claude Code
claude-code
```

### 方法 2: 手动配置

```bash
# 1. 确保集合路径正确
export AI_COLLECTION="/path/to/ai_collection"

# 2. 在配置中引用完整路径
systemPrompt: "Read ${AI_COLLECTION}/collection/agents/fullstack-engineer/AGENT.md"

# 3. 启动工具
opencode  # 或 claude-code
```

## 使用示例

### 示例 1: 全栈开发

```
User: "使用 fullstack-engineer 构建一个任务管理系统"

OpenCode/Claude Code:
1. 读取 fullstack-engineer/AGENT.md
2. 应用其开发方法论
3. 遵循其架构原则
4. 使用其推荐的技术栈
```

### 示例 2: 算法优化

```
User: "使用 algorithm-engineer 优化这个排序函数"

OpenCode/Claude Code:
1. 读取 algorithm-engineer/AGENT.md
2. 分析当前实现
3. 提出优化方案
4. 实现并测试
```

### 示例 3: 产品原型

```
User: "使用 tech-cofounder 快速构建 MVP"

OpenCode/Claude Code:
1. 读取 tech-cofounder/AGENT.md
2. 应用其产品思维
3. 遵循 MVP 原则
4. 快速迭代
```

## 技能组合

### 开发 + 测试

```
使用 openspec 定义需求，然后实现并测试
```

结合规格驱动开发和 TDD。

### 研究 + 文档

```
使用 research-agent 调研技术方案，然后编写文档
```

深度研究 + 清晰文档。

### 分析 + 可视化

```
使用 stock-analyst 分析数据，生成图表
```

技术分析 + 可视化输出。

## 故障排除

### 代理未加载

**症状:** 代理的专业知识没有被应用

**解决方案:**
1. 检查 `systemPrompt` 路径是否正确
2. 确认 AGENT.md 文件存在
3. 查看错误日志
4. 尝试手动加载：`/agents load fullstack_engineer`

### 技能未激活

**症状:** 技能关键词没有触发

**解决方案:**
1. 检查激活关键词拼写
2. 查看 SKILL.md 中的关键词列表
3. 确认技能已正确安装
4. 尝试显式调用："使用 XX 技能"

### 路径问题

**症状:** "找不到 AGENT.md 文件"

**解决方案:**
1. 使用绝对路径
2. 或设置环境变量 `AI_COLLECTION`
3. 或将集合复制到项目目录

## 最佳实践

1. **明确指定**: 明确说明使用哪个代理或技能
2. **上下文充分**: 提供足够的任务上下文
3. **验证结果**: 检查代理/技能是否被正确应用
4. **组合使用**: 多个代理/技能可以协同工作

## 高级用法

### 多代理协作

```
使用 fullstack-engineer 进行架构设计，然后用 algorithm-engineer 优化核心算法
```

### 技能链式调用

```
先用 skill-extractor 提取技能模式，然后用 skill-rag-indexer 索引它
```

### 自定义代理组合

在配置中定义代理组合：

```json
{
  "agentTeams": {
    "fullstack_plus": {
      "agents": ["fullstack_engineer", "algorithm_engineer"],
      "workflow": "architecture -> implementation -> optimization"
    }
  }
}
```

---

*最后更新: 2026-02-20*
*相关文档: [AGENTS.md](../../AGENTS.md), [SKILLS.md](../../SKILLS.md)*
