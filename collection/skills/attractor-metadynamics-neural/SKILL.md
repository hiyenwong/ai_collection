---
name: attractor-metadynamics-neural
description: 神经网络吸引子元动力学方法论。研究慢适应过程如何塑造吸引子景观演化。适用于神经动力学、连续学习。触发词：吸引子、元动力学、神经动力学、attractor、metadynamics。
user-invocable: true
---

# Attractor Metadynamics - 吸引子元动力学

## 核心思想

慢适应过程（突触/内在可塑性）持续塑造神经网络吸引子景观。

**来源：** arXiv:1404.5417
**效用：** 0.90

---

## 实现

```python
import numpy as np

class AttractorMetadynamics:
    def __init__(self, n=100):
        self.W = np.random.randn(n, n) * 0.1
        self.eta = 0.001
    
    def dynamics(self, x, dt=0.1):
        return x + (-x + np.tanh(self.W @ x)) * dt
    
    def plasticity(self, x, dt=0.1):
        self.W += self.eta * np.outer(x, x) * dt
```

---

## Activation Keywords
- 吸引子
- 元动力学
- 神经动力学

## Tools Used
- numpy

## Instructions for Agents
1. 理解慢快时间尺度
2. 跟踪吸引子演化

## Examples
研究持续学习中的记忆稳定性。

## 参考文献
- arXiv:1404.5417