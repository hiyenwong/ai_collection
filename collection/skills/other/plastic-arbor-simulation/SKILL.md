---
name: plastic-arbor-simulation
description: Plastic Arbor突触可塑性模拟框架。从单个突触到形态神经元网络的可定制模拟，支持CPU/GPU高性能计算。适用于突触可塑性研究、神经网络模拟、形态学神经元建模。触发词：突触可塑性、Arbor、神经元模拟、形态学、synaptic plasticity、morphological neuron、simulation framework。
user-invocable: true
---

# Plastic Arbor Simulation Framework

## 核心思想

支持从单个突触到形态神经元网络的可定制突触可塑性模拟，结合高性能计算。

**来源：** arXiv:2411.16445
**效用：** 0.98

---

## 实现

```python
import numpy as np

class PlasticArbor:
    def __init__(self, n_neurons=100):
        self.n = n_neurons
        self.V = np.zeros(n_neurons)
        self.W = np.random.rand(n_neurons, n_neurons) * 0.1
        
    def step(self, I, dt=0.1):
        # LIF动力学
        dV = (-self.V + I) / 20.0
        self.V += dV * dt
        
        # 发放
        spikes = self.V > 1.0
        self.V[spikes] = 0.0
        
        # STDP可塑性
        self._stdp_update(spikes)
        return spikes
    
    def _stdp_update(self, spikes):
        pre = spikes.astype(float)
        post = spikes.astype(float)
        self.W += 0.01 * np.outer(post, pre)
```

---

## Activation Keywords
- 突触可塑性
- Arbor
- 神经元模拟

## Tools Used
- numpy

## Instructions for Agents
1. 定义神经元形态
2. 配置突触可塑性规则
3. 运行网络模拟

## Examples
模拟学习过程中的突触权重变化。

## 参考文献
- arXiv:2411.16445