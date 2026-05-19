---
name: conv-delay-learning-snn
description: "Convolutional delay learning in recurrent spiking neural networks for edge deployment. DelRec approach with convoluted recurrent connections achieving 99% parameter savings and 52x faster inference."
arxiv_source: "2604.15997"
version: v1.0.0
last_updated: 2026-04-20
---

# Convolutional Delay Learning in Recurrent SNNs

Combining Convolution and Delay Learning in Recurrent Spiking Neural Networks (DelRec with convolutional connections). Achieves 99% parameter reduction and 52x faster inference while maintaining accuracy on audio classification tasks.

## Core Innovation

This methodology extends recurrent SNN delay learning by:
- **Convolutional recurrent connections**: Replacing dense recurrent matrices with convolutional operations
- **Runtime delay learning**: Axonal delays learned alongside network parameters
- **Massive compression**: ~99% reduction in recurrent parameters
- **Speed improvement**: 52x faster inference time

## Technical Approach

### DelRec Foundation

DelRec (Delay Learning in Recurrent SNNs) learns axonal delays at runtime:
- Each synapse has an adjustable delay parameter
- Delays are optimized during training
- Enables temporal feature extraction

### Convolutional Extension

The convolutional variant replaces dense recurrent connections:
```
Traditional: W ∈ R^(N×N)  →  N² parameters
Convolutional: W_conv ∈ R^(k×k)  →  k² parameters (k << N)
```

### Implementation Guidelines

```python
class ConvDelRecSNN:
    def __init__(self, n_neurons, kernel_size=3, n_delays=5):
        self.n_neurons = n_neurons
        self.conv_kernel_size = kernel_size
        self.n_delays = n_delays
        # Convolutional recurrent weights
        self.recurrent_conv = nn.Conv2d(1, 1, kernel_size, padding=kernel_size//2)
        # Learnable delays
        self.delays = nn.Parameter(torch.randn(n_delays))
```

## Applications

- Audio classification on edge devices
- Temporal pattern recognition
- Resource-constrained SNN deployment
- Neuromorphic hardware optimization

## Activation Keywords

- conv delay learning snn
- convolutional recurrent snn
- delay learning
- edge deployment snn
- audio classification snn
