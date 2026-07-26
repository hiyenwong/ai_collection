---
name: bio-neuron-snn-learning
description: 生物神经元参数学习SNN方法论。联合优化突触权重和神经元内在参数，结合Lempel-Ziv复杂度实现可解释的时空脉冲数据分类。适用于脉冲神经网络、神经形态计算、可解释AI。触发词：生物神经元、SNN参数学习、Lempel-Ziv复杂度、神经形态计算、biological neuron、LZC、spiking neural network。
user-invocable: true
---

# Bio Neuron SNN Learning - 生物神经元参数学习

## 核心思想

用生物启发的神经元模型替代感知器抽象，联合优化突触权重和神经元内在参数，结合 Lempel-Ziv 复杂度实现可解释分类。

**来源：** arXiv:2508.11674
**效用：** 0.99

---

## 方法论

### 核心创新

| 创新 | 说明 |
|------|------|
| 联合优化 | 突触权重 + 神经元参数同时学习 |
| 生物模型 | LIF / 元神经元替代感知器 |
| 复杂度编码 | Lempel-Ziv 复杂度分类 |

### 实现框架

```python
import torch
import torch.nn as nn
import numpy as np

class BioNeuronSNN(nn.Module):
    """生物神经元参数学习SNN"""
    
    def __init__(self, n_input, n_hidden, n_output):
        super().__init__()
        
        # 突触权重
        self.W1 = nn.Parameter(torch.randn(n_input, n_hidden) * 0.1)
        self.W2 = nn.Parameter(torch.randn(n_hidden, n_output) * 0.1)
        
        # 可学习的神经元参数
        self.tau_m = nn.Parameter(torch.ones(n_hidden) * 20.0)  # 膜时间常数
        self.v_thresh = nn.Parameter(torch.ones(n_hidden) * 1.0)  # 阈值
        self.v_reset = nn.Parameter(torch.zeros(n_hidden))  # 重置电位
    
    def forward(self, x, duration=100):
        """前向传播"""
        batch_size = x.shape[0]
        n_hidden = self.W1.shape[1]
        
        v = torch.zeros(batch_size, n_hidden)
        spikes = []
        
        for t in range(duration):
            # 输入电流
            I = torch.matmul(x, self.W1)
            
            # LIF 动力学（可学习参数）
            dv = (-v + I) / torch.abs(self.tau_m)
            v = v + dv
            
            # 发放
            spike = (v > self.v_thresh).float()
            spikes.append(spike)
            
            # 重置
            v = v * (1 - spike) + self.v_reset * spike
        
        # 输出
        hidden_activity = torch.stack(spikes).sum(dim=0)
        output = torch.matmul(hidden_activity.float(), self.W2)
        
        return output, torch.stack(spikes)

def lempel_ziv_complexity(spike_train, threshold=0.5):
    """计算 Lempel-Ziv 复杂度"""
    binary = (spike_train > threshold).astype(int)
    sequence = ''.join(map(str, binary))
    
    n = len(sequence)
    substrings = set()
    complexity = 1
    current = sequence[0]
    
    for i in range(1, n):
        current += sequence[i]
        if current not in substrings:
            substrings.add(current)
            complexity += 1
            current = ''
    
    return complexity / (n / np.log2(n + 1))
```

---

## 应用场景

1. 神经形态计算
2. 可解释脉冲分类
3. 事件驱动检测

---

## Activation Keywords
- 生物神经元
- SNN参数学习
- Lempel-Ziv复杂度
- 神经形态计算

## Tools Used
- torch
- numpy

## Instructions for Agents
1. 定义可学习神经元参数
2. 联合优化权重和参数
3. 使用LZC增强可解释性

## Examples
训练生物启发的SNN进行时空数据分类。

## 参考文献
- arXiv:2508.11674