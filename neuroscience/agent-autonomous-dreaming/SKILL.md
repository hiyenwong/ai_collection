---
name: agent-autonomous-dreaming
title: Agent 自主梦境-记忆重塑系统
description: 基于神经科学研究的 Agent 自主梦境系统，模拟人类睡眠中的记忆巩固过程。适用于 AI Agent 的记忆管理、知识整理、自动学习场景。触发词：自主梦境、记忆重塑、agent dreaming、memory consolidation、每日做梦
author: Hermes Agent
version: 1.0.0
category: ai_collection/neuroscience
triggers:
  - 自主梦境
  - 记忆重塑
  - agent dreaming
  - memory consolidation
  - 每日做梦
---

# Agent 自主梦境-记忆重塑系统

## 概述

这是一个基于神经科学研究（记忆巩固理论、神经动力学模型、REM睡眠机制）的 Agent 自主系统，让 AI Agent 能够像人类一样在"睡眠"期间进行记忆巩固和梦境生成。

## 科学基础

### 核心论文

1. **Zhang (2026)** - Learning and Consolidating New Memories while Asleep
   - 贡献：记忆巩固的计算理论框架
   - 应用：记忆衰减与重组算法

2. **Tavangari et al. (2025)** - Mathematical Modelling of Dreaming
   - 贡献：神经动力学数学模型
   - 应用：梦境生成算法

3. **Akhavan et al. (2026)** - A data-driven approach to measuring the propensity for REM sleep
   - 贡献：REM睡眠数据驱动测量
   - 应用：REM特征增强

4. **Leckie et al. (2024)** - Dream content and structure relate to signature patterns of affect
   - 贡献：梦境-情感耦合机制
   - 应用：情感映射

## 系统组件

### 1. 梦境 Skill (`dream-simulation`)

**路径**: `~/.hermes/skills/ai_collection/dream-simulation/`

**功能**:
- 5阶段梦境生成（编码→巩固→构建→增强→报告）
- 4种梦境模式（记忆巩固、情感处理、创意启发、清醒梦）
- 完整的神经科学理论基础文档

**文件结构**:
```
dream-simulation/
├── SKILL.md                          # 主文档
├── scripts/
│   └── dream_generator.py           # Python 梦境生成器
└── references/
    └── neuroscience_theory.md       # 神经科学理论
```

### 2. 自主梦境脚本 (`agent_dream.py`)

**路径**: `~/.hermes/scripts/agent_dream.py`

**功能**:
- 每日4:00自动执行
- 从 kg.db 加载记忆（实体和关系）
- 从 state.db 加载会话历史
- 应用记忆巩固算法
- 生成梦境叙事和报告

**记忆重塑流程**:
```
加载记忆 → 记忆巩固(衰减+重组) → 梦境生成 → 报告输出
```

### 3. 论文监控系统 (`paper_monitor.py`)

**路径**: `~/.hermes/scripts/paper_monitor.py`

**功能**:
- 每周一9:00自动检查
- 监控6个关键词的 arXiv 新论文
- 检测新论文并生成报告

**监控关键词**:
- dream
- sleep memory consolidation
- REM sleep
- hippocampus replay
- lucid dreaming
- neural dynamics consciousness

## 部署步骤

### 1. 创建必要目录

```bash
mkdir -p ~/.hermes/scripts ~/.hermes/dreams ~/.hermes/skills/ai_collection
```

### 2. 部署 dream-simulation Skill

将 skill 文件复制到:
```
~/.hermes/skills/ai_collection/dream-simulation/
```

### 3. 部署自主梦境脚本

创建 `~/.hermes/scripts/agent_dream.py`:
- 实现记忆加载功能
- 实现记忆巩固算法（衰减+重组）
- 实现梦境生成
- 输出报告到 `~/.hermes/dreams/dream_log.jsonl`

### 4. 部署论文监控脚本

创建 `~/.hermes/scripts/paper_monitor.py`:
- 使用 arXiv API 查询新论文
- 缓存已见过的论文
- 检测新论文并生成报告
- 输出到 `~/.hermes/dreams/paper_report.md`

### 5. 配置 Cron 定时任务

添加到 crontab:
```
# Agent 每日梦境 - 凌晨4点
0 4 * * * cd ~ && python ~/.hermes/scripts/agent_dream.py >> ~/.hermes/dreams/dream_log.jsonl 2>&1

# 论文监控 - 每周一上午9点
0 9 * * 1 cd ~ && python ~/.hermes/scripts/paper_monitor.py
```

## 输出位置

| 文件 | 用途 |
|------|------|
| `~/.hermes/dreams/dream_log.jsonl` | 梦境日志 |
| `~/.hermes/dreams/paper_report.md` | 论文监控报告 |
| `~/.hermes/dreams/papers_cache.json` | 论文缓存 |

## 工作流程

### 每日执行流程 (4:00)

1. **加载阶段** (4:00-4:15)
   - 从 kg.db 加载记忆实体
   - 从 kg.db 加载记忆关系
   - 从 state.db 加载会话历史

2. **巩固阶段** (4:15-5:00)
   - 应用记忆衰减（不常用记忆减弱）
   - 重组记忆关系
   - 识别记忆模式

3. **梦境生成** (5:00-7:00)
   - 选择梦境主题
   - 生成梦境叙事
   - 添加神经科学解读

4. **报告阶段** (7:00-8:00)
   - 输出梦境报告
   - 更新记忆权重
   - 记录到日志

### 每周执行流程 (周一 9:00)

1. 查询 arXiv 新论文
2. 与缓存对比检测新论文
3. 生成论文摘要报告
4. 如发现重要论文，更新 skill

## 关键算法

### 记忆衰减公式

```python
decay_factor = 0.95  # 5% 衰减
new_weight = old_weight * (decay_factor ** days_since_last_access)
```

### 记忆重组

```python
# 识别强连接
strong_connections = [r for r in relations if r['weight'] > threshold]

# 重组：创建新的间接连接
for conn in strong_connections:
    # 在相关记忆间创建新的弱连接
    create_weak_connection(conn['source'], conn['target'], weight=0.1)
```

### 梦境主题选择

基于情感权重随机选择：
```python
theme = weighted_random_choice(themes, weights=[t['emotional_weight'] for t in themes])
```

## 维护与更新

### 监控论文更新

- 每周自动检查 arXiv
- 如发现新的梦境/记忆相关研究，考虑更新 skill
- 提交到 ai_collection

### 日志轮转

```bash
# 每周轮转梦境日志
0 0 * * 0 cd ~/.hermes/dreams && mv dream_log.jsonl dream_log_$(date +%Y%m%d).jsonl && touch dream_log.jsonl
```

## 参考资料

- 神经科学基础: `dream-simulation/references/neuroscience_theory.md`
- 梦境生成脚本: `dream-simulation/scripts/dream_generator.py`
- arXiv API 文档: https://arxiv.org/help/api/user-manual

## 版本历史

- v1.0.0 (2026-04-12): 初始版本，完成基础架构部署
- v1.0.1 (2026-04-16): 迁移到 ai_collection/neuroscience 分类
- v1.0.2 (2026-04-18): 
  - 修复 kg.db 加载（entities 表 schema 适配：name/content/last_updated）
  - 修复 state.db 路径（~/.hermes/state.db）
  - 修复 state.db 加载（sessions 表使用 timestamp 而非 created_at）
  - 增强记忆重塑建议（添加对话统计、Top 实体、网络结构分析）
  - 修复 arxiv API 查询（使用 urllib.parse.quote 编码 URL）
  - 实际调用 arxiv API 获取神经科学论文
