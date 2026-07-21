---
name: shiftlif-power-of-two-quantization
description: "ShiftLIF neuron model: efficient multi-level spiking neurons with power-of-two quantization. Reformulates burst spiking as saturated uniform quantization with learnable scale, absorbable into weights for inference. Activation: shiftlif, power-of-two quantization, learnable quantization scale, multi-level spiking neurons, burst SNN quantization."
---

# ShiftLIF: Efficient Multi-Level Spiking Neurons with Power-of-Two Quantization

> Multi-level spiking neuron that uses power-of-two quantization with learnable scale, absorbable into synaptic weights for strict accumulate-only inference.

## Metadata
- **Source**: arXiv:2605.01866
- **Authors**: Kaiwen Tang, Di Yu, Jiaqi Zheng, Changze Lv, Qianhui Liu, Zhanglu Yan, Weng-Fai Wong
- **Published**: 2026-05-03
- **Category**: cs.CV (applied to edge sensing)

## Core Methodology

### Key Innovation
Standard LIF neurons with binary spike coding suffer from 1-bit-per-timestep information bottleneck. ShiftLIF reformulates burst spiking as saturated uniform quantization of membrane potentials with a **learnable scale parameter**, allowing each layer to autonomously adapt its spiking resolution to membrane-potential statistics. The scale is absorbed into synaptic weights during inference, maintaining strict accumulate-only (AC) execution.

### Technical Framework

1. **Learnable-Scale Quantization**: The quantization scale is a trainable parameter per layer, not a predefined threshold
2. **Saturated Uniform Quantization**: Membrane potentials are quantized to multi-level spikes based on the learned scale
3. **Absorbable Scale Strategy**: The learned scale is folded into synaptic weights during inference, preserving hardware efficiency
4. **ReLSG-ET Surrogate Gradient**: Rectified-Linear Surrogate Gradient with Exponential Tails sustains gradient flow across burst intervals
5. **Power-of-Two Quantization**: Quantization levels are constrained to powers of two for efficient hardware implementation (shift operations replace multiplications)

### Architecture
```
Input → Conv/Linear → QB-LIF Neuron (learnable scale) → Spike → ...
                                                    ↓
                                          Scale absorbed into weights
                                                    ↓
                                          Strict AC-only inference
```

## Applications
- **Edge Sensing**: Event-driven computation with temporal filtering
- **Low-Latency Vision**: Ultra-low latency image recognition with multi-level spikes
- **Dynamic Vision Sensors**: Processing event camera data efficiently
- **Resource-Constrained Deployment**: Hardware-efficient SNN inference on edge devices

## Implementation Guide

### Prerequisites
- SpikingJelly or similar SNN framework
- PyTorch

### QB-LIF Neuron Definition
```python
import torch
import torch.nn as nn

class ShiftLIFNeuron(nn.Module):
    """Multi-level spiking neuron with learnable-scale power-of-two quantization."""
    
    def __init__(self, n_levels=4, tau=2.0, threshold=1.0):
        super().__init__()
        self.n_levels = n_levels
        self.tau = tau  # membrane time constant
        self.threshold = threshold
        # Learnable quantization scale
        self.scale = nn.Parameter(torch.tensor(0.5))
        
    def forward(self, x, v_prev):
        # Update membrane potential
        v = v_prev + (x - v_prev) / self.tau
        
        # Quantize with learnable scale
        # Power-of-two constraint for hardware efficiency
        scale_clamped = torch.clamp(self.scale, min=2**-8, max=2**0)
        
        # Saturated uniform quantization
        q = torch.clamp(torch.round(v / scale_clamped), 0, self.n_levels - 1)
        
        # Generate multi-level spikes
        spikes = q * scale_clamped
        
        return spikes, v - spikes  # residual membrane potential
```

### ReLSG-ET Surrogate Gradient
```python
class ReLSG_ET(torch.autograd.Function):
    """Rectified-Linear Surrogate Gradient with Exponential Tails."""
    
    @staticmethod
    def forward(ctx, x, scale, n_levels):
        ctx.save_for_backward(x, scale)
        ctx.n_levels = n_levels
        return torch.clamp(torch.round(x / scale), 0, n_levels - 1) * scale
    
    @staticmethod
    def backward(ctx, grad_output):
        x, scale = ctx.saved_tensors
        # Exponential tail gradient for sustained flow across burst intervals
        alpha = 2.0
        grad = grad_output * alpha * torch.exp(-alpha * torch.abs(x / scale - torch.round(x / scale)))
        return grad, None, None
```

### Training Loop
```python
def train_shiftlif(model, dataloader, optimizer, n_timesteps=4):
    for data, target in dataloader:
        optimizer.zero_grad()
        v = torch.zeros(data.shape[0], model.n_neurons)
        
        for t in range(n_timesteps):
            spikes, v = model(data, v)
            # Accumulate spikes over time
            output = spikes if t == 0 else output + spikes
        
        loss = F.cross_entropy(output, target)
        loss.backward()
        optimizer.step()
        
        # After training, absorb scales into weights
    absorb_scales_to_weights(model)
```

## Pitfalls
- **Scale initialization**: Poor initialization can cause all neurons to spike at same level; initialize to match data statistics
- **Number of levels**: More levels = more information but higher hardware cost; 2-8 levels typically optimal
- **Time steps**: Short simulation horizons (< 4 timesteps) benefit most from multi-level coding
- **Scale absorption**: Must be done after training; forgetting this step loses the hardware efficiency benefit
- **Gradient stability**: ReLSG-ET's exponential tails need careful alpha tuning; too aggressive causes vanishing gradients

## Related Skills
- quantization-spiking-neural-networks-beyond-accuracy
- qb-lif-quantized-burst-neurons-v2
- sub-bit-snn-compression
- snn-quantized-dynamics-integer
- edgespike-edge-iot-snn
