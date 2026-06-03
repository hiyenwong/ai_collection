---
name: laplace-neural-manifold-working-memory
version: 1.0.0
description: |
  Laplace 神经流形工作记忆表示。使用指数时间基函数和逆 Laplace 空间
  实现"什么"x"何时"的联合感受野。
  触发词：工作记忆、Laplace变换、神经流形、时间表示、working memory、
  Laplace neural manifold, temporal basis functions。
---

# Laplace Neural Manifold Working Memory

## 核心方法论

### 问题定义

**挑战：** 工作记忆需要表示任何刺激在任何时间延迟，需要神经元展示混合选择性。

**解决方案：** Laplace 神经流形 - "什么" x "何时" 的联合感受野

---

## 关键概念

### 1. 工作记忆表示

**要求：** 神经元需要具有刺激和时间的联合感受野

| 特性 | 说明 |
|------|------|
| **混合选择性** | 神经元同时编码刺激和时间 |
| **联合感受野** | "什么" x "何时" |
| **时间延迟** | 记住任何时间点的事件 |

### 2. Laplace 神经流形

**两个空间：**

| 空间 | 基函数 | 特点 |
|------|--------|------|
| **Laplace 空间** | 指数基函数 | 编码时间信息 |
| **逆 Laplace 空间** | 有界基函数 | 解码时间表示 |

---

## 应用场景

| 场景 | 说明 |
|------|------|
| **认知建模** | 工作记忆计算模型 |
| **序列记忆** | 时间序列记忆 |
| **决策制定** | 基于历史信息的决策 |

---

## 来源

- **论文：** "What" x "When" working memory representations using Laplace Neural Manifolds
- **arXiv：** 2409.20484
- **效用评分：** 0.91
- **学习日期：** 2026-03-22

## Activation Keywords

- 工作记忆
- Laplace变换
- 神经流形
- working memory

## Tools Used

- **read**: Read skill documentation
- **exec**: Run simulation scripts
- **web_fetch**: Fetch papers

## Instructions for Agents

1. Understand Laplace transform for time encoding
2. Apply to working memory modeling
3. Ensure conjunctive receptive fields

## Examples

```python
# Example: Model working memory
manifold = LaplaceNeuralManifold(n_scales=10)
```