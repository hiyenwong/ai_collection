# OpenClaw AI Collection - Claude Code Agent Context

本配置文件将 OpenClaw AI Collection 的专业代理集成到 Claude Code 中。

## 使用方法

### 方法 1: 复制到项目

```bash
# 在项目根目录执行
mkdir -p .claude
cp /path/to/ai_collection/docs/integration/claude-code-agents.md .claude/AGENTS.md
```

### 方法 2: 直接引用

在 `.claude/AGENTS.md` 中添加：

```markdown
参见 /path/to/ai_collection/docs/integration/claude-code-agents.md
```

---

## 可用代理 (Agents)

### Fullstack Engineer
**路径:** `collection/agents/fullstack-engineer/`
**用途:** 高级全栈工程师，专注于现代 Web 开发
**激活方式:**
```
使用 fullstack-engineer 的方法来构建这个应用
Use fullstack-engineer approach for this web application
```
**核心能力:**
- 全栈 Web 应用开发（React, Vue, Node.js, Python）
- 数据库设计与优化
- API 设计与实现
- DevOps 与部署

### Algorithm Engineer
**路径:** `collection/agents/algorithm-engineer/`
**用途:** 算法工程师，专注于算法设计与机器学习
**激活方式:**
```
使用 algorithm-engineer 优化这个算法
Use algorithm-engineer approach for this optimization problem
```
**核心能力:**
- 算法设计与分析
- 数据结构与复杂度
- 机器学习模型
- 性能优化

### Tech Co-Founder (Builder)
**路径:** `collection/agents/tech-cofounder/`
**用途:** 技术联合创始人，专注于产品构建
**激活方式:**
```
使用 tech-cofounder 快速构建 MVP
Use tech-cofounder approach for rapid prototyping
```
**核心能力:**
- 产品规划与架构
- MVP 开发
- 技术决策
- 团队协作

### Research Agent
**路径:** `collection/agents/research-agent/`
**用途:** 研究专家，专注于深度调研
**激活方式:**
```
使用 research-agent 调研这个技术方案
Use research-agent to investigate this topic
```
**核心能力:**
- 深度信息收集
- 技术调研
- 文档编写
- 数据分析

### Stock Analyst
**路径:** `collection/agents/stock-analyst/`
**用途:** 股票分析师，专注于金融数据分析
**激活方式:**
```
使用 stock-analyst 分析这个股票
Use stock-analyst for financial data analysis
```
**核心能力:**
- 股票数据分析
- 技术指标计算
- 交易策略回测
- 市场洞察

---

## 可用技能 (Skills)

### OpenSpec - 规格驱动开发
**路径:** `collection/skills/openspec/`
**激活关键词:** openspec, gherkin, BDD, scenario
**用途:** 使用 Gherkin 语法定义需求

### Skill Extractor - 技能提炼
**路径:** `collection/skills/skill-extractor/`
**激活关键词:** 提炼技能, 提取 skill, skill extractor, generate skill
**用途:** 从对话中识别和提炼可复用的技能模式

### Skill RAG Indexer - 技能语义搜索
**路径:** `collection/skills/skill-rag-indexer/`
**激活关键词:** 搜索技能, skill search, skill rag, 技能索引
**用途:** 语义搜索和推荐技能

### Stock Analysis - 股票技术分析
**路径:** `collection/skills/stock-analysis/`
**激活关键词:** 股票分析, stock analysis, technical indicators, MACD, KDJ
**用途:** 股票技术指标分析和可视化

### AkShare - 中国金融数据
**路径:** `collection/skills/akshare/`
**激活关键词:** stock data, akshare, 中国股票, 金融数据
**用途:** 获取中国金融市场数据

---

## 快速参考

### 开发任务
- **Web 应用:** `使用 fullstack-engineer`
- **算法优化:** `使用 algorithm-engineer`
- **MVP 开发:** `使用 tech-cofounder`

### 研究任务
- **技术调研:** `使用 research-agent`
- **文档编写:** `使用 research-agent`
- **市场分析:** `使用 stock-analyst`

### 技能组合
- **规格 + 实现:** `openspec` + `fullstack-engineer`
- **提炼 + 索引:** `skill-extractor` + `skill-rag-indexer`
- **数据 + 分析:** `akshare` + `stock-analysis`

---

## 配置说明

### Agent 路径配置

如果 AI Collection 不在默认位置，请设置环境变量：

```bash
export AI_COLLECTION="/path/to/ai_collection"
```

然后在配置中引用：
```
systemPrompt: "Read ${AI_COLLECTION}/collection/agents/fullstack-engineer/AGENT.md"
```

### Skill 激活

技能会通过关键词自动激活。确保关键词在你的提示中出现：

```
用户: "帮我提炼一个技能"
AI: [检测到 "提炼技能"，激活 skill-extractor 技能]
```

---

## 示例对话

### 示例 1: 全栈开发

```
User: 使用 fullstack-engineer 的方法构建一个任务管理系统

Claude Code:
1. 读取 collection/agents/fullstack-engineer/AGENT.md
2. 应用全栈开发方法论
3. 遵循其架构原则
4. 使用推荐的技术栈
5. 生成可生产的代码
```

### 示例 2: 算法优化

```
User: 使用 algorithm-engineer 的方法优化这个排序算法

Claude Code:
1. 读取 collection/agents/algorithm-engineer/AGENT.md
2. 分析当前实现的复杂度
3. 提出优化方案
4. 实现并测试
5. 验证性能改进
```

### 示例 3: 技能链式调用

```
User: 先用 openspec 定义需求，然后用 fullstack-engineer 实现

Claude Code:
1. 激活 openspec 技能
2. 使用 Gherkin 语法定义需求
3. 切换到 fullstack-engineer
4. 实现定义的需求
5. 确保符合规格
```

---

*配置模板 v1.0 - 2026-02-20*
*OpenClaw AI Collection*
