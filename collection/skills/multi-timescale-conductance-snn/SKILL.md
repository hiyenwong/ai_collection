---
name: multi-timescale-conductance-snn
description: "Multi-Timescale Conductance Spiking Networks (MTCSN) — a sparse, gradient-trainable SNN framework with rich firing dynamics for enhanced temporal processing. Use when: building spiking neural networks for temporal processing, implementing conductance-based neuron models, training SNNs with gradient-based methods, sparse SNN architectures, neuromorphic temporal sequence processing. Based on arXiv:2605.11835 (2026). Trigger: multi-timescale spiking, conductance-based SNN, gradient-trainable SNN, sparse spiking network, temporal processing SNN, rich firing dynamics, MTCSN"
---

# Multi-Timescale Conductance Spiking Networks (MTCSN)

## Overview

A sparse, gradient-trainable Spiking Neural Network framework using multi-timescale conductance-based neuron models. Enables rich firing dynamics for enhanced temporal processing with parameter-efficient sparse architectures.

Based on: arXiv:2605.11835 (2026) "Multi-Timescale Conductance Spiking Networks: A Sparse, Gradient-Trainable Framework with Rich Firing Dynamics for Enhanced Temporal Processing"

## Core Architecture

### Multi-Timescale Conductance Neurons

Each neuron models conductance dynamics across multiple timescales:

- **Fast timescale**: Rapid response to input spikes (ms range)
- **Medium timescale**: Synaptic integration and short-term plasticity (10-100ms)
- **Slow timescale**: Homeostatic regulation and adaptation (seconds)

The membrane potential evolves via:
```
τ_m dV/dt = -(V - V_rest) + Σ g_i(t) · (E_i - V) + I_ext
```
where g_i(t) are conductance variables with different decay timescales.

### Sparse Connectivity

- Structured sparsity reduces parameters while preserving computational capacity
- Sparse recurrent connections maintain rich dynamics with fewer parameters
- Gradient-based training through surrogate gradient methods

### Gradient Training

- Surrogate gradient descent for backpropagation through spiking nonlinearity
- Compatible with standard deep learning frameworks (PyTorch)
- End-to-end differentiable training pipeline

## Key Advantages

1. **Rich firing dynamics**: Multi-timescale conductances capture diverse neuronal behaviors (bursting, adapting, regular spiking)
2. **Sparse efficiency**: Fewer parameters than dense SNNs with comparable or better performance
3. **Gradient-trainable**: Full end-to-end training without approximation
4. **Temporal processing**: Superior performance on time-series and sequence tasks

## Implementation Patterns

### Basic Neuron Model

```python
import torch
import torch.nn as nn

class ConductanceNeuron(nn.Module):
    def __init__(self, n_timescales=3):
        super().__init__()
        self.taus = nn.Parameter(torch.tensor([5.0, 50.0, 500.0]))  # ms
        self.conductances = nn.Parameter(torch.randn(n_timescales))
        self.rest_potential = -65.0
        self.threshold = -50.0
    
    def forward(self, spikes, dt=1.0):
        # Multi-timescale conductance integration
        dV = -(self.V - self.rest_potential) / self.tau_m
        for i, tau in enumerate(self.taus):
            dV += self.conductances[i] * self.g[i] / tau
        self.V = self.V + dV * dt
        spikes_out = self.V > self.threshold
        self.V[spikes_out] = self.rest_potential  # reset
        return spikes_out
```

### Sparse Recurrent Layer

```python
class SparseRecurrentSNN(nn.Module):
    def __init__(self, n_neurons, sparsity=0.1):
        super().__init__()
        # Create sparse connectivity mask
        mask = torch.rand(n_neurons, n_neurons) < sparsity
        self.weight = nn.Parameter(torch.randn(n_neurons, n_neurons) * mask.float())
        self.neurons = nn.ModuleList([ConductanceNeuron() for _ in range(n_neurons)])
    
    def forward(self, input_spikes, steps=100):
        history = []
        for t in range(steps):
            recurrent = torch.sparse.mm(
                self.weight.to_sparse(), 
                spikes[-1].unsqueeze(1)
            ).squeeze()
            output = self.neurons(input_spikes + recurrent)
            history.append(output)
        return torch.stack(history)
```

## When to Use

- Temporal sequence classification tasks
- Event-based sensor data processing (DVS cameras, audio)
- Neuromorphic hardware deployment
- Energy-efficient temporal pattern recognition
- When rich spiking dynamics matter more than rate coding

## Pitfalls

- Surrogate gradient choice significantly impacts training stability
- Multi-timescale parameters need careful initialization
- Sparse connectivity may require larger networks for equivalent capacity
- Gradient vanishing in long sequences — use skip connections or reservoir-style readout

## Resources

- Original paper: arXiv:2605.11835
- Related: spikingjelly-framework skill for SNN implementation
