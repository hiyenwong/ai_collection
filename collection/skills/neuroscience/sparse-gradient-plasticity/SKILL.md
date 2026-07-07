---
name: sparse-gradient-plasticity
description: 梯度突触可塑性稀疏实现方法论。实现真正稀疏且通用的梯度突触可塑性规则，保持在线学习能力。适用于脉冲神经网络、在线学习、突触可塑性研究。触发词：突触可塑性、梯度下降、稀疏实现、在线学习、sparse plasticity、gradient-based、online learning。
user-invocable: true
---

# Sparse Gradient Synaptic Plasticity

## 核心思想

实现真正稀疏且通用的梯度突触可塑性规则，避免手动推导梯度或牺牲在线能力。

**来源：** arXiv:2501.11407
**效用：** 0.92

---

## 实现

```python
import numpy as np

class SparseGradientPlasticity:
    def __init__(self, n_pre, n_post, sparsity=0.1):
        self.W = np.random.randn(n_post, n_pre) * 0.1
        self.mask = np.random.rand(n_post, n_pre) < sparsity
        self.W *= self.mask
        self.eta = 0.01
    
    def forward(self, x):
        return self.W @ x
    
    def update(self, pre, post, error):
        dW = self.eta * np.outer(error * post, pre)
        self.W += dW * self.mask
```

---

## Activation Keywords
- 突触可塑性
- 梯度下降
- 稀疏实现

## Tools Used
- numpy

## Instructions for Agents
1. 创建稀疏连接掩码
2. 实现在线梯度更新
3. 保持稀疏性约束

## Examples
在线学习任务中的突触权重更新。

## 参考文献
- arXiv:2501.11407