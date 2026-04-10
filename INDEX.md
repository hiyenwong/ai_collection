# 索引 - 技能与代理

本索引提供按类别分类的技能和代理快速发现指南。

## 目录

- [代理索引](#代理索引)
  - [按功能分类](#按功能分类)
  - [按模型分类](#按模型分类)
- [技能索引](#技能索引)
  - [按功能分类](#按功能分类-1)
  - [按工具分类](#按工具分类)
- [标签云](#标签云)

---

## 代理索引

### 按功能分类

#### 开发构建

| 代理 | 描述 | 适用场景 |
|------|------|---------|
| [Fullstack Engineer](collection/agents/fullstack-engineer/) | 高级全栈工程师 | 完整的 Web 应用开发、架构设计 |
| [Tech Co-Founder](collection/agents/tech-cofounder/) | 技术联合创始人 | 产品原型、快速开发、文档优先 |
| [Algorithm Engineer](collection/agents/algorithm-engineer/) | 算法工程师 | 算法设计与实现、模型优化、复杂问题求解 |

#### 数据分析

| 代理 | 描述 | 适用场景 |
|------|------|---------|
| [Stock Analyst](collection/agents/stock-analyst/) | 股票分析师 | 股票数据分析、技术指标、市场洞察 |
| [Research Agent](collection/agents/research-agent/) | 研究专家 | 深度调研、信息综合、市场研究 |

### 按模型分类

#### Opus 4.5（复杂推理）

| 代理 | 用途 |
|------|------|
| Fullstack Engineer | 复杂架构设计 |
| Research Agent | 深度研究 |
| Stock Analyst | 复杂金融分析 |
| Algorithm Engineer | 算法设计与复杂问题求解 |

#### Sonnet 4.5/4.6（通用任务）

| 代理 | 用途 |
|------|------|
| Tech Co-Founder | 产品开发 |
| Stock Analyst | 标准分析 |

---

## 技能索引

### 按功能分类

#### 编程开发

| 技能 | 描述 | 激活词 |
|------|------|--------|
| [OpenCode](collection/skills/opencode/) | 开源 AI 编程，多代理编排 | opencode, ultrawork |
| [Claude Code](collection/skills/claude-code/) | Anthropic 官方编程助手 | claude-code |
| [OpenSpec](collection/skills/openspec/) | 规格驱动开发 | openspec, gherkin |

#### 数据处理

| 技能 | 描述 | 激活词 |
|------|------|--------|
| [AkShare](collection/skills/akshare/) | 中国金融数据接口 | stock data, akshare |
| [Stock Analysis](collection/skills/stock-analysis/) | 股票技术分析 | 股票分析, technical indicators |

#### 元技能

| 技能 | 描述 | 激活词 |
|------|------|--------|
| [Skill Extractor](collection/skills/skill-extractor/) | 从对话提炼技能 | 提炼技能, skill extractor |
| [Skill RAG Indexer](collection/skills/skill-rag-indexer/) | RAG 索引器，语义搜索 | skill rag search, 搜索技能 |

### 按工具分类

#### Python 脚本

- AkShare
- Stock Analysis

#### TypeScript / Node.js

- Skill RAG Indexer

#### Git 操作

- OpenCode
- Claude Code

#### 文档操作

- OpenSpec
- Skill Extractor
- Skill RAG Indexer

---

## 标签云

### 代理标签

```
#开发 #全栈 #后端 #前端 #架构
#数据分析 #股票 #金融 #研究 #调研
#产品 #原型 #快速开发 #文档
#算法 #机器学习 #深度学习 #优化
```

### 技能标签

```
#编程 #代码 #开发 #多代理 #编排
#规格 #BDD #测试 #文档
#金融 #股票 #数据 #API #中国
#元技能 #提炼 #自动化
#RAG #搜索 #索引 #推荐
```

---

## 快速查找

### 我想...

| 需求 | 推荐代理/技能 |
|------|--------------|
| 开发一个 Web 应用 | Fullstack Engineer + OpenCode |
| 快速构建产品原型 | Tech Co-Founder |
| 分析股票数据 | Stock Analyst + Stock Analysis |
| 进行深度研究 | Research Agent |
| 编写规格文档 | OpenSpec |
| 提炼新技能 | Skill Extractor |
| 实现复杂算法 | Algorithm Engineer |
| 开发 ML 模型 | Algorithm Engineer |

---

## 搜索技巧

### 按关键词搜索

- **开发相关**: coding, development, programming, 开发, 编程
- **数据相关**: data, analysis, statistics, 数据, 分析
- **金融相关**: finance, stock, trading, 金融, 股票
- **文档相关**: docs, specification, BDD, 文档, 规格

### 按场景搜索

- **快速原型**: Tech Co-Founder
- **生产级代码**: Fullstack Engineer
- **数据分析**: Stock Analyst, AkShare
- **深度研究**: Research Agent

---

## 最新更新

### 2026-02-20

**集成:**
- 新增: OpenCode + Claude Code 完整集成指南
- 新增: 代理配置模板 (opencode-config.json)
- 新增: Claude Code 代理上下文模板
- 更新: opencode 和 claude-code 技能的集成说明
- 支持: 所有 5 个代理和 7 个技能的一键安装

**代理:**
- 新增: Tech Co-Founder 代理
- 新增: Stock Analyst 代理
- 新增: Algorithm Engineer 代理
- 新增: 所有代理的 SOUL.md 灵魂宣言

**技能:**
- 新增: Skill Extractor 元技能
- 新增: Skill RAG Indexer 语义搜索
- 完善: Stock Analysis 技能文档和示例

**文档:**
- 新增: INDEX.md 分类索引
- 新增: 中文版贡献指南
- 新增: GitHub Actions CI/CD
- 新增: 技能验证脚本
- 新增: 各代理/技能使用示例

**工具:**
- 新增: validate_skill.py 验证脚本
- 新增: GitHub Actions 工作流

---

## 反馈与贡献

如果你发现索引有遗漏或错误，或者有新的分类建议，欢迎：

1. 提交 Issue
2. 发起 Pull Request
3. 在讨论区交流

---

*索引最后更新: 2026-02-19*
