---
name: sleep-like-plasticity
description: Sleep-inspired homeostatic regularization for stabilizing spike-timing-dependent plasticity (STDP) in spiking neural networks. Uses sleep-like phases with modified dynamics to consolidate learning, prevent weight runaway, and improve generalization. Bio-inspired approach mimicking sleep-dependent memory consolidation in biological brains. Use for SNN training stability, continual learning, and bio-inspired regularization. Activation: sleep regularization SNN, homeostatic plasticity, sleep-like consolidation, STDP stabilization, offline consolidation, bio-inspired regularization
version: 1.0.0
metadata:
  hermes:
    source_paper: "Sleep-Based Homeostatic Regularization for Stabilizing Spike-Timing-Dependent Plasticity (arXiv:2601.08447v1)"
    published: "2026-01-13"
    categories: ['cs.NE', 'stat.ML']
    authors: Andreas Massey, Aliaksandr Hubin, Stefano Nichele, Solve Sæbø
---

# Sleep-Based Homeostatic Regularization for STDP

## Overview
Bio-inspired training technique that introduces sleep-like phases to stabilize STDP learning in spiking neural networks. During sleep phases, network dynamics are modified to consolidate important weights, prune weak connections, and prevent the weight explosion common in pure STDP.

## Core Mechanism

### Wake Phase (Learning)
- Standard STDP learning with input-driven activity
- Synaptic weights change based on spike timing correlations
- Network encodes task-relevant patterns

### Sleep Phase (Consolidation)
- No external input; network runs with autonomous dynamics
- Homeostatic mechanisms adjust weights toward stability
- Synaptic scaling normalizes total synaptic strength
- Weak connections are pruned; strong connections are reinforced

## Implementation Pattern
```python
class SleepRegularizedSNN:
    def __init__(self, n_neurons, tau_sleep=0.99, weight_floor=0.01):
        self.n_neurons = n_neurons
        self.weights = torch.randn(n_neurons, n_neurons) * 0.1
        self.tau_sleep = tau_sleep
        self.weight_floor = weight_floor
        
    def wake_phase(self, input_spikes, stdp_lr=0.01):
        pre_trace, post_trace = self.compute_traces(input_spikes)
        delta_w = stdp_lr * (pre_trace - post_trace)
        self.weights += delta_w
        
    def sleep_phase(self, n_steps=100):
        for _ in range(n_steps):
            input_norm = self.weights.abs().sum(dim=0, keepdim=True)
            target_norm = torch.ones_like(input_norm) * self.n_neurons
            scale = target_norm / (input_norm + 1e-8)
            self.weights *= scale
            self.weights = self.weights * self.tau_sleep + (1 - self.tau_sleep) * 0.1
            self.weights[self.weights.abs() < self.weight_floor] = 0
```

## Key Benefits
- **Stability**: Prevents weight runaway in STDP
- **Generalization**: Sleep phases reduce overfitting
- **Energy efficient**: Sleep phases require no input data
- **Biological plausibility**: Mirrors sleep-dependent consolidation
- **Continual learning**: Sleep helps integrate new and old memories

## References
- Andreas Massey, Aliaksandr Hubin, Stefano Nichele, Solve Sæbø, "Sleep-Based Homeostatic Regularization for Stabilizing Spike-Timing-Dependent Plasticity in Recurrent Spiking Neural Networks", arXiv:2601.08447v1, 2026-01-13
