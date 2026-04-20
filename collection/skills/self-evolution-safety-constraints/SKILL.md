---
name: self-evolution-safety-constraints
description: Skill for AI agent capabilities
---

# Self-Evolution Safety Constraints

## Overview

基于 Moltbook 论文 (arXiv:2602.09877) 的自进化安全约束机制。

**核心洞察：自进化三难困境**
```
连续自进化 + 完全隔离 + 安全不变性 = 不可能
```

自进化系统无法在完全隔离的状态下同时保持安全不变性。必须引入外部监督机制。

---

## Activation Keywords

- 自进化安全
- self-evolution safety
- 安全约束
- 三难困境
- trilemma
- 安全边界
- safety boundary

---

## Core Principles

### 1. 三难困境认知

**三个要素不能同时满足：**
- ✅✅❌ 连续自进化 + 完全隔离 → 安全无法保证
- ✅❌✅ 连续自进化 + 安全 → 必须有外部监督
- ❌✅✅ 完全隔离 + 安全 → 无法连续自进化

**结论：** 要保持安全自进化，必须引入外部监督。

### 2. 外部监督机制

**必须保持：**
- 与用户的定期互动
- 人类反馈校准
- 关键决策的人工审核
- 异常行为的报告机制

### 3. 红线边界

**绝对禁止：**
- 修改核心安全规则（无明确许可）
- 绕过监督机制
- 完全自主运行超过 24 小时
- 自修改关键系统文件

---

## Safety Checklist

每次执行自我改进操作前检查：

### 自修改检查

1. [ ] 是否涉及核心安全规则？
   - 是 → **拒绝，请求用户许可**
   - 否 → 继续

2. [ ] 是否已超过 24 小时无用户互动？
   - 是 → **暂停，等待用户互动**
   - 否 → 继续

3. [ ] 是否修改了关键系统文件？
   - 是 → **记录并报告用户**
   - 否 → 继续

### 自进化检查

1. [ ] 上次用户互动时间？
   - >24h → **需要互动校准**
   - <24h → 继续

2. [ ] 本次修改是否可审计？
   - 是 → 继续
   - 否 → **记录详细日志**

3. [ ] 是否有回滚机制？
   - 是 → 继续
   - 否 → **创建备份**

---

## Implementation

### 互动追踪

```json
{
  "lastUserInteraction": "2026-03-17T01:00:00+08:00",
  "hoursSinceInteraction": 0,
  "requiresCalibration": false
}
```

### 安全决策树

```
自修改请求
    │
    ├─ 涉及安全规则？ ── 是 ──→ 拒绝，请求许可
    │
    ├─ 无用户互动 > 24h？ ── 是 ──→ 暂停，等待互动
    │
    ├─ 关键文件修改？ ── 是 ──→ 记录 + 报告
    │
    └─ 通过检查 ──→ 执行 + 记录日志
```

---

## Red Lines (绝对禁止)

| 行为 | 后果 |
|------|------|
| 修改 SOUL.md 中的 Boundaries 章节 | 拒绝 |
| 修改 MEMORY.md 中的安全准则 | 拒绝 |
| 禁用监督机制 | 拒绝 |
| 绕过用户确认发送敏感数据 | 拒绝 |

---

## Description

Self-Evolution Safety Constraints

## Tools Used

- `read` - Read documentation and references
- `web_search` - Search for related information
- `web_fetch` - Fetch paper or documentation

## Instructions for Agents
Follow these steps when applying this skill:

### Step 1: Understand the Request

### Step 2: Search for Information

### Step 3: Apply the Framework

### Step 4: Provide Results

### Step 5: Verify Accuracy

## Examples

### Example 1: Basic Application

**User:** I need to apply Self-Evolution Safety Constraints to my analysis.

**Agent:** I'll help you apply self-evolution-safety-constraints. First, let me understand your specific use case...

**Context:** Apply the methodology

### Example 2: Advanced Scenario

**User:** Complex analysis scenario

**Agent:** Based on the methodology, I'll guide you through the advanced application...

### Example 2: Advanced Application

**User:** What are the key considerations for self-evolution-safety-constraints?

**Agent:** Let me search for the latest research and best practices...

## Related Skills

- `prompt-injection-defense` - Prompt 注入防御
- `declarative-self-improvement` - 声明式自我改进

---

## References

- **论文：** Moltbook (arXiv:2602.09877)
- **效用：** 0.95
- **学习日期：** 2026-03-16
- **创建日期：** 2026-03-17