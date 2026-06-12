---
name: qb-lif-quantized-burst-neurons-v2
description: "Quantized Burst-LIF (QB-LIF) v2 - Enhanced learnable-scale quantized burst neurons for efficient Spiking Neural Networks. Adaptive spike count control with binary activation for hardware deployment. Keywords: SNN, burst neurons, quantization, neuromorphic hardware."
---

# QB-LIF: Learnable-Scale Quantized Burst Neurons for Efficient SNNs v2

> Enhanced quantized burst neuron model with learnable-scale quantization that adaptively controls spike count while maintaining binary activation for energy-efficient SNN hardware deployment.

## Metadata
- **Source**: arXiv:2604.25688
- **Authors**: Dewei Bai, Hongxiang Peng, Jiajun Mei
- **Published**: 2026-04-28

## Core Methodology

### Key Innovation
Binary spike coding in SNNs fundamentally limits information capacity with 1-bit-per-timestep representation. QB-LIF v2 addresses this through learnable-scale quantized burst neurons that:
1. Generate multiple spikes per processing step (burst coding)
2. Adaptively control spike count through learnable quantization scales
3. Maintain temporal locality for efficient hardware implementation
4. Preserve binary activation for energy-efficient deployment

### Technical Framework
1. **Burst Neuron Model**: Extends LIF dynamics to generate variable spike counts
2. **Learnable Quantization**: Scale parameters adaptively control spike generation threshold
3. **Temporal Locality**: Maintains causality within single timestep for hardware compatibility
4. **Binary Preservation**: Outputs remain binary despite variable spike counts

## Implementation Guide

### Prerequisites
- PyTorch or JAX for SNN implementation
- SpikingJelly or snnTorch framework
- Understanding of LIF neuron dynamics

### Step-by-Step
1. Initialize QB-LIF neuron with learnable quantization scales
2. Set burst parameters controlling max spikes per timestep
3. Integrate into SNN replacing standard LIF layers
4. Train with surrogate gradients using custom backward pass
5. Quantize for deployment maintaining binary activation

### Code Example
```python
import torch
import torch.nn as nn

class QBLIFNeuron(nn.Module):
    def __init__(self, tau=2.0, v_threshold=1.0, learnable_scale=True, max_burst=4):
        super().__init__()
        self.tau = tau
        self.v_threshold = nn.Parameter(torch.tensor(v_threshold)) if learnable_scale else v_threshold
        self.max_burst = max_burst
        self.mem = 0
        
    def forward(self, x):
        # Membrane potential integration
        self.mem = self.mem * (1 - 1/self.tau) + x
        # Burst spike generation
        spike_count = torch.clamp((self.mem / self.v_threshold).floor(), 0, self.max_burst)
        self.mem -= spike_count * self.v_threshold
        return spike_count > 0  # Binary output
```

## Applications
- SNN hardware acceleration: FPGA and neuromorphic chip deployment
- Edge AI: Resource-constrained environments
- High-throughput neural computation

## Pitfalls
- Learnable scales may require careful initialization
- Burst coding increases synaptic operations
- Hardware compatibility varies across platforms

## Related Skills
- qb-lif-quantized-burst-neurons
- quantization-snn-beyond-accuracy
