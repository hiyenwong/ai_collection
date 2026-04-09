# SKILL.md - EvoScientist: Multi-Agent Evolving AI Scientists

---
name: evo-scientist
description: Multi-agent framework for end-to-end scientific discovery with persistent memory and self-evolution. Use when planning research, generating ideas, or executing experiments.
user-invocable: true
disable-model-invocation: false
---

## 概述

EvoScientist 是一个进化的多代理 AI 科学家框架，通过持久记忆和自我进化持续改进研究策略。

**来源论文：** arXiv:2603.08127 - EvoScientist: Towards Multi-Agent Evolving AI Scientists

## 核心组件

### 1. 三个专门代理

| 代理 | 角色 | 职责 |
|------|------|------|
| Researcher Agent (RA) | 想法生成 | 提出科学想法、研究方向 |
| Engineer Agent (EA) | 实验执行 | 实现代码、运行实验 |
| Evolution Manager Agent (EMA) | 知识提炼 | 从交互历史提炼可复用知识 |

### 2. 两个持久记忆模块

| 记忆模块 | 内容 | 用途 |
|---------|------|------|
| Ideation Memory | 可行研究方向 + 失败方向记录 | 避免重复失败、优先可行方向 |
| Experimentation Memory | 有效数据处理 + 模型训练策略 | 提高代码执行成功率 |

## 工作流程

```
1. RA 从 Ideation Memory 检索相关策略
2. RA 生成新想法
3. EA 从 Experimentation Memory 检索有效实现
4. EA 执行实验
5. EMA 分析结果，提炼知识
6. 更新两个记忆模块
```

## 应用场景

### 触发关键词

- 研究计划、idea generation
- 实验设计、experiment design
- 科学发现、scientific discovery
- 多代理协作、multi-agent collaboration

### 使用示例

**场景：规划一个新研究方向**

1. **Researcher Agent:**
   - 检索 Ideation Memory 中的可行方向
   - 基于历史成功案例生成新想法
   - 避免已记录的失败方向

2. **Engineer Agent:**
   - 检索 Experimentation Memory 中的有效代码模式
   - 设计实验流程
   - 执行验证

3. **Evolution Manager Agent:**
   - 分析实验结果
   - 提炼成功策略到记忆
   - 记录失败教训

## 实施要点

### 1. 持久记忆结构

```json
{
  "ideation_memory": {
    "feasible_directions": [...],
    "failed_directions": [...],
    "top_ranked_ideas": [...]
  },
  "experimentation_memory": {
    "effective_strategies": [...],
    "best_implementations": [...],
    "code_search_trajectories": [...]
  }
}
```

### 2. 自我进化机制

- 每次交互后更新记忆
- 定期提炼高价值知识
- 避免重复相同错误

### 3. 多代理协调

- RA 和 EA 独立运作
- EMA 作为中央协调器
- 通过共享记忆协作

## 与其他技能的关联

- **elastic-memory-orchestration** - 三层记忆架构
- **action-critical-selection** - 行动质量评估
- **ice-review** - 任务后回顾

## 效用评分

**效用：** 0.92

**原因：**
- 端到端科学发现能力
- 持久记忆避免重复失败
- 超越 7 个 SOTA 系统

---

**创建时间：** 2026-03-15
**论文来源：** arXiv:2603.08127
## Description
Framework from arXiv papers. See paper reference for details.
## Activation Keywords

- evo-scientist
- evo-scientist 技能
- evo-scientist skill

## Tools Used

- `read` - Read documentation and references
- `web_search` - Search for related information
- `web_fetch` - Fetch paper or documentation

## Instructions for Agents

1. **Understand the Request**: Analyze what the user needs related to this skill's domain.
2. **Search for Information**: Use web_search to find relevant papers or documentation.
3. **Apply the Framework**: Follow the methodology described in the skill's key concepts.
4. **Provide Results**: Summarize findings and actionable recommendations.
5. **Verify Accuracy**: Cross-check key facts before presenting to user.

## Examples

### Example 1: Basic Usage

**User:** How can I apply evo-scientist?

**Agent:** I'll help you understand and apply evo-scientist...

### Example 2: Advanced Application

**User:** What are the key considerations for evo-scientist?

**Agent:** Let me search for the latest research and best practices...
