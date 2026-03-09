# Skills - 技能库

## 目录说明

这个目录存储所有可复用的技能，包括：
- `learned-skills.md` - 从实际工作事件中提炼的技能
- `external/` - 从外部技能库移植的技能

---

## 内部技能

### [learned-skills](./learned-skills.md)
从实际工作经历中提炼的可复用技能，包括：
- 上下文管理（会话历史优先检查、任务约定执行）
- 优先级判断（立即执行 vs 未来配置、用户意图理解）
- 沟通技巧（确认机制、复述确认）
- 工作流程（完整任务生命周期、迭代改进流程）
- 自动化（Cron 任务配置）

**提炼时间：** 2026-03-03
**技能数量：** 8

---

## 外部技能

### [akshare](./external/akshare.md)
中国金融数据接口，支持：
- A股、港股、美股数据
- 期货、基金、债券
- 宏观经济指标
- 外汇、加密货币

**来源：** `/Users/hiyenwong/projects/ai_projects/ai_collection/collection/skills/akshare/`
**移植时间：** 2026-03-03

---

### [stock-analysis](./external/stock-analysis.md)
股票分析系统，支持：
- 单股票分析
- 多股票比较
- 技术指标计算（KDJ、MACD、RSI、布林带等）
- 可视化和报告生成
- 基于模型的评分

**来源：** `/Users/hiyenwong/projects/ai_projects/ai_collection/collection/skills/stock-analysis/`
**移植时间：** 2026-03-03

---

### [teach-cofounder](./external/teach-cofounder.md)
技术导师技能，包括：
- 苏格拉底式引导
- 深度原理解释
- 渐进式教学
- 代码审查框架

**来源：** `/Users/hiyenwong/projects/ai_projects/ai_collection/collection/skills/teach-cofounder/`
**移植时间：** 2026-03-03

---

### [skill-extractor](./external/skill-extractor.md)
技能提取器，支持：
- 自动识别技能模式
- 技能提取框架
- 技能分类和验证
- 从对话中提炼技能

**来源：** `/Users/hiyenwong/projects/ai_projects/ai_collection/collection/skills/skill-extractor/`
**移植时间：** 2026-03-03

---

### [chat-history-lancedb](./external/chat-history-lancedb.md)
聊天历史数据库，支持：
- 消息存储和会话管理
- 向量语义搜索
- RAG 上下文检索
- 数据导入和导出

**来源：** `/Users/hiyenwong/projects/ai_projects/ai_collection/collection/skills/chat-history-lancedb/`
**移植时间：** 2026-03-03

---

## 协调能力

### [agent-coordinator](./agent-coordinator.md)
智能体协调器，支持：
- 问题分析和分类
- 能力映射和决策
- 多 agent 协作
- 结果整合

**创建时间：** 2026-03-03
**创建原因：** 建立问题分析和 agent 协调机制，选择最合适的能力回答问题

---

## 技能分类

### 按用途分类

**数据获取：**
- akshare - 金融数据接口

**数据分析：**
- stock-analysis - 股票分析

**教学辅导：**
- teach-cofounder - 技术导师

**技能管理：**
- skill-extractor - 技能提取器
- learned-skills - 从事件提炼的技能

**知识管理：**
- chat-history-lancedb - 聊天历史数据库

**协调能力：**
- agent-coordinator - 智能体协调器

### 按复杂度分类

**基础技能：**
- 会话历史优先检查
- 任务约定执行
- 确认机制

**中级技能：**
- akshare 数据获取
- stock-analysis 技术分析
- 优先级判断
- Cron 任务配置

**高级技能：**
- teach-cofounder 教学框架
- skill-extractor 技能提取
- chat-history-lancedb 向量搜索
- 完整任务生命周期
- 迭代改进流程

---

## 使用指南

### 查找技能

1. **按名称查找**
   - 浏览本文件，找到感兴趣的技能

2. **按用途查找**
   - 查看分类，找到合适的类别

3. **搜索关键词**
   - 使用 `grep` 或 `rg` 搜索技能文件

### 学习技能

1. **阅读文档**
   - 理解技能的目的和用途
   - 学习核心概念和方法
   - 查看示例代码

2. **实践应用**
   - 在实际工作中应用
   - 记录使用经验
   - 根据反馈调整

3. **持续改进**
   - 定期回顾技能文档
   - 根据新经验更新
   - 提取新的技能模式

### 贡献技能

如果你发现新的可复用模式：

1. **识别模式**
   - 确认模式可复用
   - 判断是否有价值

2. **提取技能**
   - 使用技能模板
   - 包含必要信息
   - 提供示例

3. **记录技能**
   - 保存到 appropriate 文件
   - 更新索引（本文件）
   - 添加相关标签

---

## 技能统计

- **总技能数：** 14
  - 内部技能：8
  - 外部技能：5
  - 协调能力：1

- **本月新增：** 14
  - 2026-03-03: 14

- **按用途分布：**
  - 数据获取：1
  - 数据分析：1
  - 教学辅导：1
  - 技能管理：2
  - 知识管理：1
  - 协调能力：1
  - 上下文管理：2
  - 优先级判断：2
  - 沟通技巧：2
  - 工作流程：2
  - 自动化：1

---

## 更新日志

### 2026-03-03
- 初始化技能库
- 从今日事件中提炼 8 个内部技能
- 移植 5 个外部技能：
  - akshare
  - stock-analysis
  - teach-cofounder
  - skill-extractor
  - chat-history-lancedb
- 创建智能体协调器（agent-coordinator）：
  - 问题分析和分类
  - 能力映射和决策
  - 多 agent 协作
  - 结果整合

---

## 相关资源

### OpenClaw 技能系统
- `/Users/hiyenwong/.nvm/versions/node/v24.11.1/lib/node_modules/openclaw/skills/` - 系统技能
- `/Users/hiyenwong/projects/ai_projects/ai_collection/collection/skills/` - 用户技能库

### 技能开发
- [skill-creator](~/.agents/skills/skill-creator/SKILL.md) - 技能创建指南

---

**最后更新：** 2026-03-03
**维护者：** Aerial 🎩
