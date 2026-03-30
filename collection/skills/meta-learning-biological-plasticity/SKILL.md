---
name: meta-learning-biological-plasticity
description: Meta-Learning Biologically Plausible Plasticity Rules
---

# Meta-Learning Biologically Plausible Plasticity Rules

**Source:** arXiv:2210.16414v5 (February 2023)
**Utility:** 0.90
**Authors:** Navid Shervani-Tabar et al.

---

## Description

This skill meta-learns interpretable, biologically plausible plasticity rules
that improve online learning with fixed random feedback connections (Feedback
Alignment). It addresses the gap between backpropagation and biological
synaptic plasticity.

**Core Insight:** Random feedback alignment + meta-learned plasticity rules
enable effective online learning without symmetric backward connections.

---

## Tools Used

- `pytorch` - Neural network implementation
- `meta_learning_framework` - Meta-optimization (MAML-like)
- `feedback_alignment` - Random feedback connections
- `plasticity_rules` - Custom learning rule implementations

---

## Instructions for Agents

1. **Define plasticity rule search space** - Parameterized update functions
   satisfying biological constraints
2. **Setup random feedback architecture** - Fixed random backward weights
3. **Meta-learn plasticity parameters** - Optimize for online learning
   performance across tasks
4. **Validate biological plausibility** - Check locality, no symmetric
   backward connections
5. **Test on target domains** - Evaluate in low-data regime, deep models

---

## Examples

### Example 1: Training Deep Network with Biological Constraints

**User:** 如何在不使用反向传播的情况下训练深度神经网络？

**Agent:** 使用元学习的生物可塑性规则：

1. 设置固定随机反馈连接（替代反向传播的权重传输）
2. 定义局部可塑性规则（只依赖神经元局部信息）
3. 元学习优化规则参数
4. 结果：在线学习性能接近反向传播，但满足生物约束

**优势：** 无需对称反馈连接，适合在线学习。

### Example 2: Low-Data Regime Learning

**User:** 在数据有限的情况下，如何快速适应新任务？

**Agent:** 生物可塑性规则 + 元学习：

- 元学习阶段：在多个任务上优化可塑性规则
- 应用阶段：使用优化后的规则快速适应新任务
- 低数据环境下表现优于标准反向传播

---

## Activation Keywords

- 生物可塑性、biological plasticity
- 反馈对齐、feedback alignment
- 元学习可塑性规则、meta-learning plasticity
- 随机反馈、random feedback
- 在线学习、online learning
- 神经可塑性、synaptic plasticity

---

## Key Concepts

### 1. Feedback Alignment Problem

- **Backpropagation:** Requires symmetric forward/backward weights
- **Feedback Alignment:** Uses fixed random backward connections
- **Challenge:** Shallow models work, deep models learn slowly

### 2. Meta-Learning Approach

**Objective:** Discover plasticity rules that:
- Use only local information (biological constraint)
- Improve deep model training with random feedback
- Enable efficient online learning

**Method:**
1. Parameterize plasticity rule (weight update function)
2. Meta-optimize parameters across multiple tasks
3. Resulting rule generalizes to new tasks

### 3. Biological Plausibility Criteria

| Criterion | Backprop | Meta-Learned Rule |
|-----------|----------|-------------------|
| Symmetric feedback | ❌ Required | ✅ Not needed |
| Local computation | ❌ Global | ✅ Local |
| Online learning | ❌ Batch | ✅ Online |
| Weight transport | ❌ Required | ✅ Random fixed |

---

## When to Use

1. **Biologically constrained learning** - Models matching brain constraints
2. **Online learning systems** - Continual adaptation
3. **Low-data regimes** - Quick adaptation with few samples
4. **Neuromorphic hardware** - Local learning rules suitable for hardware

---

## Results (Paper)

| Setting | Standard FA | Meta-Learned Rules |
|---------|-------------|-------------------|
| Shallow models | OK | Better |
| Deep models | Slow | Faster convergence |
| Online learning | Poor | Good |
| Low-data regime | Poor | Good |

---

## Limitations

1. Still not as efficient as backpropagation for large datasets
2. Meta-learning phase requires multiple tasks
3. Random feedback quality affects performance
4. Deep model performance gap remains

---

## Related Skills

- `decolle-snn-learning` - Deep continuous local learning
- `neuromodulated-synaptic-plasticity` - Neuromodulation-based learning
- `noisy-snn-learning` - Learning with noise in SNNs