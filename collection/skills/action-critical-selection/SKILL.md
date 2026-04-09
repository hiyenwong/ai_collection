---
name: action-critical-selection
description: '行动关键选择技能，通过对比成功行动与次优替代方案来理解"为什么"而非仅"做什么"。触发词：行动选择、决策质量、行动对比、关键训练。'
---

# Action Critical Selection - 行动关键选择

基于 arXiv:2603.08706 (Agentic Critical Training) 的行动质量意识技能。

## 激活关键词

- 行动选择
- 决策质量
- 行动对比
- 关键训练
- 为什么这样做
- 行动评估

## 核心理念

**模仿学习只教"做什么"，不教"为什么"。**

传统方法：
- 模仿学习 → 复制专家行为
- 不知道为什么这个行动好于另一个
- 缺乏行动质量意识

ACT 方法：
- 对比成功行动与次优替代方案
- 奖励判断的正确性
- 驱动自主推理行动质量

## 工作流程

### 1. 行动对比分析

当面临决策时：

```
候选行动 A: [行动描述]
候选行动 B: [替代方案]

分析：
- A 的优势：...
- B 的劣势：...
- 关键差异：...
- 推荐选择：...
- 选择理由：...
```

### 2. 质量判断验证

```
行动质量评估：
- 预期成功率：高/中/低
- 潜在风险：...
- 次优替代：...
- 为何不选替代：...
```

### 3. 反思性推理

```
事后反思：
- 选择是否正确？
- 如果不正确，应该选什么？
- 学到了什么？
- 如何应用到未来类似情况？
```

## 使用场景

### 场景 1：工具选择

```
任务：查询知识库

候选行动 A：使用 ArcadeDB 查询
候选行动 B：读取本地文件搜索

分析：
- A 优势：图遍历、关系查询、快速
- B 劣势：无法查询关系、效率低
- 关键差异：知识图谱查询能力
- 推荐：A
- 理由：需要查询论文→技能关系，图数据库更适合
```

### 场景 2：Agent 委托

```
任务：分析股票走势

候选行动 A：委托 stock-analyst agent
候选行动 B：自己分析

分析：
- A 优势：专业、有工具支持、经验丰富
- B 劣势：缺乏专业工具、可能遗漏关键指标
- 关键差异：专业能力与工具支持
- 推荐：A
- 理由：专业性任务应委托专家
```

### 场景 3：技能选择

```
任务：记忆检索

候选行动 A：使用 memory-retrieval 技能（两阶段检索）
候选行动 B：直接读取 MEMORY.md

分析：
- A 优势：语义匹配 + 效用过滤，高效
- B 劣势：需要阅读大量内容，效率低
- 关键差异：检索效率与相关性
- 推荐：A
- 理由：长期记忆已积累大量内容，需要高效检索
```

## 评估指标

| 指标 | 说明 |
|------|------|
| 判断正确率 | 选择是否确实优于替代 |
| 推理深度 | 是否理解"为什么" |
| 迁移能力 | 能否应用到新场景 |
| 反思质量 | 事后分析是否有效 |

## 与其他技能的关系

- **meta-cognitive-reflection**：ACT 专注行动质量，元认知反思更广泛
- **ice-review**：ACT 是行动前决策，ICE 是任务后回顾
- **self-verification**：ACT 对比替代方案，自我验证检查结果

## 立即应用

当你需要做决策时，问自己：

1. **有哪些候选行动？**
2. **每个行动的优势和劣势是什么？**
3. **关键差异在哪里？**
4. **为什么选择这个而非那个？**
5. **如果选错了，会怎样？**

---

**来源论文：** arXiv:2603.08706 - Agentic Critical Training
**效用评分：** 0.95
**创建日期：** 2026-03-14
## Activation Keywords

- action-critical-selection
- action-critical-selection 技能
- action-critical-selection skill

## Tools Used

- `read` - Read documentation and references
- `web_search` - Search for related information
- `web_fetch` - Fetch paper or documentation

## Instructions for Agents
Follow these steps when applying this skill:

### Step 1: 有哪些候选行动？

### Step 2: 每个行动的优势和劣势是什么？

### Step 3: 关键差异在哪里？

### Step 4: 为什么选择这个而非那个？

### Step 5: 如果选错了，会怎样？

## Examples

### Example 1: Basic Application

**User:** I need to apply Action Critical Selection - 行动关键选择 to my analysis.

**Agent:** I'll help you apply action-critical-selection. First, let me understand your specific use case...

**Context:** Apply the methodology

### Example 2: Advanced Scenario

**User:** Complex analysis scenario

**Agent:** Based on the methodology, I'll guide you through the advanced application...

### Example 2: Advanced Application

**User:** What are the key considerations for action-critical-selection?

**Agent:** Let me search for the latest research and best practices...
