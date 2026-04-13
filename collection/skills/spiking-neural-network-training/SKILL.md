---
name: spiking-neural-network-training
description: "Training methodologies for energy-efficient spiking neural networks (SNNs). Covers surrogate gradient methods, spike-timing-dependent plasticity (STDP), and neuromorphic implementation. Activation: SNN, spiking neural network, surrogate gradient, STDP, neuromorphic."
---

# Spiking Neural Network Training Methods

## Overview

Spiking Neural Networks (SNNs) use discrete spikes for communication, offering energy efficiency over traditional ANNs. This skill covers training methods including surrogate gradients and STDP.

## Key Concepts

### Spiking Neuron Models

**Leaky Integrate-and-Fire (LIF)**:
```
τ_m * dv/dt = -(v - v_rest) + R * I(t)
if v >= v_th: emit spike, v = v_reset
```

### Surrogate Gradient Methods

Problem: Spiking is non-differentiable
Solution: Use continuous surrogate during backpropagation

## Methodology

### Surrogate Gradient Implementation

```python
import torch
import torch.nn as nn

class SurrogateGradient(torch.autograd.Function):
    """Surrogate gradient for spiking function."""
    
    @staticmethod
    def forward(ctx, input, alpha=1.0):
        ctx.save_for_backward(input)
        ctx.alpha = alpha
        return (input >= 0).float()
    
    @staticmethod
    def backward(ctx, grad_output):
        input, = ctx.saved_tensors
        alpha = ctx.alpha
        sigmoid_deriv = alpha * torch.sigmoid(alpha * input) *                        (1 - torch.sigmoid(alpha * input))
        return grad_output * sigmoid_deriv, None

spike_function = SurrogateGradient.apply
```

### STDP Implementation

```python
class STDPLayer(nn.Module):
    """STDP-based learning layer."""
    
    def __init__(self, in_features, out_features, 
                 A_plus=0.01, A_minus=0.01, tau_plus=20.0, tau_minus=20.0):
        super().__init__()
        self.A_plus = A_plus
        self.A_minus = A_minus
        self.tau_plus = tau_plus
        self.tau_minus = tau_minus
        self.weight = nn.Parameter(torch.randn(out_features, in_features) * 0.1)
    
    def forward(self, pre_spikes, post_spikes):
        """STDP weight update."""
        pass
```

## References

- Neftci, E. O., et al. (2019). Surrogate gradient learning in spiking neural networks. *IEEE Signal Processing Magazine*, 36(6), 51-63.
- Davies, M., et al. (2018). Loihi: A neuromorphic manycore processor. *IEEE Micro*, 38(1), 82-99.

## Activation Keywords

- SNN
- spiking neural network
- surrogate gradient
- STDP
- neuromorphic


## Instructions for Agents

使用此技能时遵循以下流程：

1. **理解问题**：分析输入需求和约束条件
2. **选择方法**：根据场景选择合适的技术方案
3. **执行操作**：按照方法论实施具体步骤
4. **验证结果**：检查结果是否符合预期

## Examples

### Example 1: Basic Usage

**User:** 请帮我应用此技能

**Agent:** 我将按照标准流程执行...

### Example 2: Advanced Usage

**User:** 有更复杂的场景需要处理

**Agent:** 针对复杂场景，我将采用以下策略...

## Tools Used

- `exec`
- `read`
- `write`
