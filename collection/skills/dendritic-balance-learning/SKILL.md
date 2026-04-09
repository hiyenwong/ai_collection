---
name: dendritic-balance-learning
version: 1.0.0
description: |
  局部树突平衡学习框架。抑制性神经元学习平衡单个树突隔室的兴奋性输入，
  使突触可塑性学习高效表示。
  触发词：树突平衡、突触可塑性、表示学习、脉冲神经网络、dendritic balance、
  synaptic plasticity, representation learning, spiking neural network。
---

# Local Dendritic Balance Learning

## 核心方法论

### 问题定义

**挑战：** 成对 Hebbian 可塑性只在不现实的神经动力学和输入统计要求下工作。

**解决方案：** 电压依赖突触可塑性 + 局部树突兴奋/抑制平衡

---

## 关键概念

### 1. 传统 Hebbian 可塑性的局限

| 问题 | 说明 |
|------|------|
| **动力学要求** | 需要特定的神经动力学模式 |
| **输入统计** | 对输入分布有严格要求 |
| **高维输入** | 在复杂相关输入下失败 |
| **传输延迟** | 无法处理抑制性传输延迟 |

### 2. 局部树突平衡

**核心机制：**
- 抑制性神经元学习平衡单个树突隔室的兴奋性输入
- 通过调节兴奋性突触可塑性来学习高效表示

### 3. 电压依赖突触可塑性

**在体观察：** 突触可塑性依赖于突触后电压

---

## 应用场景

| 场景 | 说明 |
|------|------|
| **表示学习** | 学习高效神经编码 |
| **SNN 训练** | 脉冲神经网络学习规则 |
| **神经形态计算** | 生物启发的学习算法 |

---

## 相关技能

- `neuromodulated-synaptic-plasticity` - 神经调节突触可塑性
- `blend-behavior-guided-neural` - 行为指导神经建模

---

## 来源

- **论文：** Local dendritic balance enables learning of efficient representations in networks of spiking neurons
- **arXiv：** 2010.12395
- **效用评分：** 0.9
- **学习日期：** 2026-03-22

## Activation Keywords

- 树突平衡
- 突触可塑性
- 表示学习
- dendritic balance

## Tools Used

- **read**: Read skill documentation
- **exec**: Run simulation scripts
- **web_fetch**: Fetch papers

## Instructions for Agents

1. Understand dendritic balance mechanism
2. Apply to SNN representation learning
3. Ensure local E/I balance in dendrites

## Examples

```python
# Example: Train SNN with dendritic balance
learner = DendriticBalanceLearning(n_exc=100, n_inh=20)
```