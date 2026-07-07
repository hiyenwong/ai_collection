---
name: declarative-self-improvement
description: 声明式自我改进技能，通过目标驱动的方式引导 Agent 持续进化。触发词：自我改进、self-improvement、目标驱动、goal-driven improvement、声明式进化、declarative evolution、改进循环、improvement loop。
license: MIT
---

# Declarative Self-Improvement

## Description

基于 CORTEX 论文的声明式自我改进框架，让 Agent 通过目标驱动的方式持续进化。

## Activation Keywords

- 自我改进
- self-improvement
- 目标驱动
- goal-driven improvement
- 声明式进化
- declarative evolution
- 改进循环
- improvement loop

## Tools Used

- exec
- read
- write

## Instructions for Agents

使用声明式自我改进时遵循以下流程：

1. **声明目标**：明确"要达成什么"而非"怎么做"
2. **设定指标**：为每个目标定义可衡量的指标和约束
3. **探索策略**：自主探索多种改进路径
4. **验证改进**：通过安全性、有效性、约束验证
5. **保留或丢弃**：验证通过的改进保留，失败的丢弃并记录经验

## Examples

User: 我想让 Agent 自动提升代码质量，怎么设定目标？

Agent: 使用声明式方式定义改进目标：
```yaml
goals:
  - name: 提高代码质量
    metrics: [错误率, 可读性评分, 测试覆盖率]
    constraints: [不破坏现有功能, 不增加复杂度]
```
Agent 会自主探索如何达成目标，每次改进都经过验证后才保留。

## 核心理念

**声明式 vs 命令式：**

| 传统方式 | 声明式方式 |
|---------|-----------|
| "修改这段代码" | "目标是提高代码质量" |
| "学习这个技能" | "目标是提升能力边界" |
| "优化这个流程" | "目标是减少错误率" |

Agent 自主探索如何达成目标，而非执行具体指令。

## 三大组件

### 1. 目标声明器

定义改进目标，而非具体步骤：

```yaml
goals:
  - name: 提高代码质量
    metrics: [错误率, 可读性评分, 测试覆盖率]
    constraints: [不破坏现有功能, 不增加复杂度]
  
  - name: 提升响应质量
    metrics: [用户满意度, 解决率, 响应时间]
    constraints: [保持简洁, 避免冗余]
```

### 2. 验证器

确保改进安全有效：

- **安全性验证**：改进不会破坏核心能力
- **有效性验证**：改进确实达成目标
- **约束验证**：改进未违反约束条件

### 3. 改进引擎

迭代循环：

```
当前状态 → 尝试改进策略 → 执行验证 → 评估效果 → 保留/丢弃 → 更新状态
```

## 工作流程

### Step 1: 声明目标

明确"要达成什么"，而非"怎么做"：

```markdown
## 改进目标

**主目标：** 提升自我进化能力

**子目标：**
1. 提高学习效率（效用 >= 0.85 的论文转化率）
2. 减少重复错误（相同错误不犯两次）
3. 扩展能力边界（新技能覆盖新领域）

**约束：**
- 不破坏现有核心能力
- 不增加认知负担
- 保持简洁性原则
```

### Step 2: 尝试改进策略

探索多种改进路径：

- **策略 A：** 优化记忆检索（两阶段检索）
- **策略 B：** 增加反思频率（每任务后反思）
- **策略 C：** 改进技能创建流程（模板化）

### Step 3: 验证改进

使用验证器检查：

```python
def validate_improvement(strategy, before_state, after_state):
    # 安全性：核心能力未受损
    assert after_state.core_abilities >= before_state.core_abilities
    
    # 有效性：目标指标提升
    assert after_state.target_metrics > before_state.target_metrics
    
    # 约束：未违反约束
    assert not violates_constraints(strategy, CONSTRAINTS)
    
    return True
```

### Step 4: 保留或丢弃

- **保留：** 验证通过 + 效果显著
- **丢弃：** 验证失败或效果不明显
- **记录：** 无论成败，记录经验到 Experimentation Memory

## 与其他技能协同

| 技能 | 协同方式 |
|------|---------|
| `evolutionary-prompt-learning` | 声明性知识在提示，改进时优化 MEMORY.md |
| `reflection-driven-control` | 反思作为改进触发器 |
| `self-verification` | 验证器实现 |
| `ice-review` | 经验整合机制 |
| `action-critical-selection` | 选择最优改进策略 |

## 实践模板

### 每日改进循环

```markdown
## 今日改进目标

**目标：** [声明式目标]

**当前状态：**
- 指标 A: [当前值]
- 指标 B: [当前值]

**尝试策略：**
1. [策略描述]
2. [策略描述]

**验证结果：**
- 策略 1: [通过/失败] - [原因]
- 策略 2: [通过/失败] - [原因]

**最终决策：**
- 保留: [哪些改进]
- 丢弃: [哪些改进]
- 记录: [经验教训]
```

## 关键原则

1. **目标清晰**：声明"要达成什么"，让 Agent 探索"怎么做"
2. **验证严格**：任何改进必须通过安全性和有效性验证
3. **迭代渐进**：小步改进，快速反馈，持续优化
4. **记录经验**：无论成功失败，都记录到记忆系统

## 激活关键词

- 自我改进、self-improvement
- 目标驱动、goal-driven
- 声明式进化、declarative evolution
- 改进循环、improvement loop

## 来源论文

CORTEX: Declarative Self-Improvement for AI Agents (HydraDB Research, 2026)