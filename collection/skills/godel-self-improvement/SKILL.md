# SKILL.md - Gödel Agent: Self-Referential Self-Improvement

---
name: godel-self-improvement
description: Self-referential framework for recursive self-improvement of AI agents. Use when optimizing agent capabilities, improving reasoning, or implementing self-modification.
user-invocable: true
disable-model-invocation: false
---

## 概述

Gödel Agent 是一个自引用代理框架，实现递归式自我改进。通过自我引用和自我修改，代理能够持续优化自身能力。

**来源论文：** arXiv:2410.xxxxx - Gödel Agent: A Self-Referential Agent Framework for Recursive Self-Improvement (ACL 2025)

**代码：** https://github.com/Arvid-pku/Godel_Agent

## 核心概念

### 1. 自引用 (Self-Reference)

代理能够：
- 读取自己的代码/提示
- 分析自己的行为模式
- 识别改进空间

### 2. 递归自我改进 (Recursive Self-Improvement)

```
当前状态 → 自我分析 → 识别改进 → 应用改进 → 新状态 → 循环
```

### 3. 安全边界

- 改进必须可验证
- 保持核心功能稳定
- 回滚机制

## 工作流程

### 阶段 1：自我分析

```json
{
  "current_capabilities": [...],
  "performance_metrics": {...},
  "identified_gaps": [...],
  "improvement_opportunities": [...]
}
```

### 阶段 2：改进设计

```json
{
  "proposed_changes": [...],
  "expected_impact": {...},
  "risk_assessment": "low/medium/high",
  "rollback_plan": "..."
}
```

### 阶段 3：验证与应用

```json
{
  "test_results": {...},
  "performance_delta": "+X%",
  "applied": true/false,
  "rollback_needed": false
}
```

## 应用场景

### 触发关键词

- 自我改进、self-improvement
- 代理优化、agent optimization
- 能力提升、capability enhancement
- 递归改进、recursive improvement
- 自引用、self-reference

### 使用示例

**场景 1：优化推理能力**

```
1. 分析当前推理模式
2. 识别推理瓶颈
3. 设计改进策略
4. 验证改进效果
5. 应用或回滚
```

**场景 2：优化记忆使用**

```
1. 分析记忆访问模式
2. 识别低效检索
3. 设计新索引策略
4. 测试性能提升
5. 应用改进
```

## 实施要点

### 1. 改进类型

| 类型 | 描述 | 风险 |
|------|------|------|
| 提示优化 | 修改系统提示 | 低 |
| 工作流调整 | 修改执行流程 | 中 |
| 技能更新 | 修改技能定义 | 中 |
| 架构变更 | 修改核心结构 | 高 |

### 2. 安全机制

- **验证层：** 改进前必须验证
- **回滚层：** 失败时回滚到前一状态
- **审计层：** 记录所有变更历史

### 3. 改进原则

1. **渐进式改进** - 小步迭代，不大幅改动
2. **可验证性** - 每个改进必须有验证方法
3. **可回滚性** - 保持回滚能力
4. **核心稳定** - 不改变核心安全边界

## 自我改进检查清单

### 改进前检查

- [ ] 改进目标是否明确？
- [ ] 改进是否可验证？
- [ ] 改进是否可回滚？
- [ ] 改进是否影响核心功能？
- [ ] 风险是否可接受？

### 改进后检查

- [ ] 验证是否通过？
- [ ] 性能是否提升？
- [ ] 是否引入新问题？
- [ ] 是否需要回滚？

## 与其他技能的关联

- **action-critical-selection** - 评估改进行动质量
- **reflection-driven-control** - 改进过程中的安全控制
- **ice-review** - 改进后回顾

## 效用评分

**效用：** 0.90

**原因：**
- ACL 2025 论文，学术认可
- 开源代码可用
- 递归自我改进是核心能力
- 安全边界定义清晰

---

**创建时间：** 2026-03-15
**论文来源：** arXiv:2410.xxxxx (ACL 2025)
**代码：** https://github.com/Arvid-pku/Godel_Agent
## Description
Framework from arXiv papers. See paper reference for details.
## Activation Keywords

- godel-self-improvement
- godel-self-improvement 技能
- godel-self-improvement skill

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

**User:** How can I apply godel-self-improvement?

**Agent:** I'll help you understand and apply godel-self-improvement...

### Example 2: Advanced Application

**User:** What are the key considerations for godel-self-improvement?

**Agent:** Let me search for the latest research and best practices...
