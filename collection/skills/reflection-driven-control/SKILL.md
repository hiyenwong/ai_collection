# Reflection-Driven Control

## Overview

基于 Reflection-Driven Control 论文 (arXiv:2512.21354) 的反思驱动控制机制。

**核心理念：** 将"自我反思"从事后修补提升为推理过程的**显式步骤**。

---

## Activation Keywords

- 反思驱动
- reflection-driven
- 自我反思
- self-reflection
- 风险检测
- risk detection
- 安全编码
- safe coding

---

## Core Concepts

### 1. 反思作为显式推理步骤

**传统方式：**
```
任务 → 执行 → 完成
```

**反思驱动方式：**
```
任务 → 评估风险 → 执行 → 反思验证 → 完成
        ↓               ↓
    检索指南        检测异常
```

### 2. 内部反思循环

```
┌─────────────────────────────────┐
│         决策路径监控             │
├─────────────────────────────────┤
│  Before → During → After        │
│    ↓        ↓        ↓          │
│  评估    监控    验证           │
│    ↓        ↓        ↓          │
│  风险？  异常？  偏差？         │
└─────────────────────────────────┘
```

### 3. 触发条件

| 阶段 | 触发条件 | 行动 |
|------|---------|------|
| Before | 检测到风险 | 检索安全指南 |
| During | 决策异常 | 注入约束 |
| After | 结果偏差 | 记录教训 |

---

## Implementation

### Before Action Checklist

```markdown
1. [ ] 评估风险等级 (low/medium/high)
2. [ ] 检索相关安全指南
3. [ ] 检查过往类似经验
4. [ ] 确认不确定性的处理方式
```

### During Action Monitoring

```markdown
1. [ ] 决策路径是否偏离预期？
2. [ ] 是否检测到异常模式？
3. [ ] 是否需要暂停重新评估？
4. [ ] 记录关键决策点
```

### After Action Reflection

```markdown
1. [ ] 结果是否符合预期？
2. [ ] 有哪些可以改进的地方？
3. [ ] 学到了什么新知识？
4. [ ] 是否需要更新相关技能？
```

---

## Risk Detection Patterns

### 高风险信号

| 信号 | 示例 | 行动 |
|------|------|------|
| 不确定关键词 | "可能"、"大概"、"也许" | 暂停，请求确认 |
| 操作外部系统 | 发送邮件、推文、API | 审核 + 确认 |
| 修改关键文件 | SOUL.md, MEMORY.md | 记录 + 报告 |
| 批量操作 | 删除多个文件 | 二次确认 |

### 异常模式检测

| 模式 | 描述 | 行动 |
|------|------|------|
| 循环行为 | 重复相同操作 3+ 次 | 标记异常 |
| 超出边界 | 操作不在预期范围 | 暂停评估 |
| 逻辑矛盾 | 前后决策冲突 | 重新评估 |

---

## Integration with Existing Skills

### 与 prompt-injection-defense 协同

```
外部输入 → 注入检测 → 反思检查 → 安全处理
```

### 与 self-evolution-safety-constraints 协同

```
自修改请求 → 安全检查 → 反思评估 → 执行/拒绝
```

---

## Example Usage

### 高风险任务处理流程

```markdown
任务：发送重要邮件

Before:
- 风险等级：high
- 安全指南：外部通信规则
- 过往经验：邮件确认流程

During:
- 监控内容是否包含敏感信息
- 检查收件人是否正确

After:
- 验证发送成功
- 记录到任务日志
```

---

## Metrics

| 指标 | 目标 |
|------|------|
| 风险检测率 | > 95% |
| 异常处理成功率 | > 90% |
| 事后反思覆盖率 | 100% |

---

## Description
Framework from arXiv papers. See paper reference for details.
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

**User:** How can I apply reflection-driven-control?

**Agent:** I'll help you understand and apply reflection-driven-control...

### Example 2: Advanced Application

**User:** What are the key considerations for reflection-driven-control?

**Agent:** Let me search for the latest research and best practices...

## References

- **论文：** Reflection-Driven Control for Trustworthy Code Agents (arXiv:2512.21354)
- **效用：** 0.90
- **学习日期：** 2026-03-15
- **创建日期：** 2026-03-17