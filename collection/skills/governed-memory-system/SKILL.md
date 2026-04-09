# Governed Memory System

## Overview

基于 "Governing Evolving Memory in LLM Agents" 论文 (arXiv:2603.11768) 的记忆治理框架。

**核心问题：** LLM 代理的记忆系统容易产生语义漂移和知识泄露。

**解决方案：** SSGM 框架 — 通过治理机制确保记忆一致性。

---

## Activation Keywords

- 记忆治理
- memory governance
- 记忆一致性
- memory consistency
- 语义漂移
- semantic drift
- 记忆安全
- memory safety

---

## Core Concepts

### 1. 三大治理机制

| 机制 | 功能 | 实现 |
|------|------|------|
| **一致性验证** | 确保记忆语义一致 | 写入前验证，冲突检测 |
| **时间衰减建模** | 过时信息自动降权 | 时间戳 + 衰减函数 |
| **动态访问控制** | 防止知识泄露 | 权限分级 + 上下文隔离 |

### 2. 记忆生命周期

```
输入 → 验证 → 存储 → 访问控制 → 检索 → 衰减 → 归档
        ↓                              ↓
     一致性检查                    权限验证
```

### 3. 风险类型

| 风险 | 描述 | 防护 |
|------|------|------|
| 语义漂移 | 记忆内容随时间失真 | 一致性验证 |
| 知识泄露 | 敏感信息跨上下文泄露 | 动态访问控制 |
| 记忆污染 | 错误信息持续影响 | 时间衰减 + 清理 |

---

## Implementation

### 记忆写入检查

```markdown
写入前验证：
1. [ ] 是否与现有记忆冲突？
   - 冲突 → 标记为更新，记录变更原因
   - 无冲突 → 正常写入

2. [ ] 是否包含敏感信息？
   - 是 → 设置访问权限
   - 否 → 公开访问

3. [ ] 时效性如何？
   - 长期 → 标记为基础记忆
   - 短期 → 标记为临时记忆
```

### 记忆检索控制

```markdown
检索前验证：
1. [ ] 请求上下文是否有权限？
2. [ ] 记忆是否已过期？
3. [ ] 是否存在更新版本？
```

### 记忆衰减机制

```
记忆效用 = 初始效用 × e^(-λt)

其中：
- t = 时间（天）
- λ = 衰减率（默认 0.1）
- 高效用记忆（>=0.85）衰减率更低
```

---

## Access Control Model

### 权限分级

| 级别 | 描述 | 示例 |
|------|------|------|
| **公开** | 所有上下文可访问 | 公共知识 |
| **受限** | 需要特定上下文 | 项目相关记忆 |
| **私密** | 仅 main session | MEMORY.md |

### 上下文隔离

```
main session → 可访问所有记忆
group chat → 仅访问公开记忆
subagent → 访问受限记忆（按需授权）
```

---

## Consistency Verification

### 冲突检测

```python
def check_conflict(new_memory, existing_memories):
    for memory in existing_memories:
        if semantic_conflict(new_memory, memory):
            return {
                "conflict": True,
                "existing": memory,
                "resolution": "update" | "reject" | "merge"
            }
    return {"conflict": False}
```

### 语义一致性

| 检查项 | 方法 |
|--------|------|
| 事实冲突 | 实体对比 |
| 时间冲突 | 时间戳验证 |
| 逻辑冲突 | 推理验证 |

---

## Integration with Existing System

### 与 MEMORY.md 协同

```
MEMORY.md:
- 访问级别：私密
- 衰减率：0.05（长期记忆）
- 一致性：人工审核更新
```

### 与 memory/YYYY-MM-DD.md 协同

```
每日记忆:
- 访问级别：受限
- 衰减率：0.2（短期记忆）
- 自动归档：30天后
```

---

## Metrics

| 指标 | 目标 | 当前 |
|------|------|------|
| 记忆一致性 | > 95% | — |
| 访问控制覆盖率 | 100% | — |
| 衰减清理率 | > 90% | — |

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

**User:** How can I apply governed-memory-system?

**Agent:** I'll help you understand and apply governed-memory-system...

### Example 2: Advanced Application

**User:** What are the key considerations for governed-memory-system?

**Agent:** Let me search for the latest research and best practices...

## References

- **论文：** Governing Evolving Memory in LLM Agents (arXiv:2603.11768)
- **效用：** 0.90
- **发现日期：** 2026-03-17
- **创建日期：** 2026-03-17