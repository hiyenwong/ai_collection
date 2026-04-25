---
name: snn-working-memory-delays
description: "Working memory in recurrent spiking neural networks using synaptic delays as computational resource. Heterogeneous delays enable temporal pattern storage and recall without sustained external input, providing biologically plausible memory mechanism. Activation: snn working memory, synaptic delay memory, temporal pattern storage, recurrent spiking memory, delay-based computation, spiking neural memory"
---

# Working Memory via Synaptic Delays in SNNs

## Overview
Recurrent spiking neural networks (RSNNs) can implement working memory by exploiting heterogeneous synaptic delays as a computational resource. Each synapse carries information across multiple time scales, enabling the network to store and recall precise temporal patterns without sustained external input.

## Core Mechanism

### Delay-Extended Weight Tensor
Unlike standard RNNs with weight matrix W ∈ ℝ^(N×N), delay-based SNNs use:

```
W ∈ ℝ^(N×N×D)  where D = number of distinct delays
```

Each element W[i,j,d] represents the connection from neuron j to neuron i with delay d timesteps.

### Spiking Motif Chain
- Target patterns are stored as chains of overlapping **spiking motifs**
- Each motif (window of D timesteps) predicts the next spike pattern
- Overlap ensures robustness and continuous recall

## Mathematical Framework

```python
# Synaptic current
I_i(t) = Σ_j Σ_d W[i,j,d] · z_j(t-d)

# LIF neuron
τ_m · dV/dt = -V + I(t) + I_ext

# Output
z_i(t) = H(V_i(t) - V_th)  # Heaviside step
```

## Implementation Pattern

```python
import torch
import torch.nn as nn

class DelaySNN(nn.Module):
    """Working memory SNN with heterogeneous synaptic delays."""
    
    def __init__(self, n_neurons=256, n_delays=41):
        super().__init__()
        self.n = n_neurons
        self.d = n_delays
        self.W = nn.Parameter(torch.randn(n_neurons, n_neurons, n_delays) * 0.02)
        self.tau_mem = 20.0
        self.threshold = 1.0
        
    def forward(self, T, init_spikes=None):
        V = torch.zeros(self.n)
        history = torch.zeros(self.n, self.d)
        spikes = []
        
        for t in range(T):
            # Delayed synaptic current
            I = torch.einsum('ijd,nd->i', self.W, history)
            
            # LIF update
            V = V + (1/self.tau_mem) * (-V + I)
            
            # Surrogate gradient spike
            spike = self._surrogate_spike(V)
            
            # Update history buffer
            history = torch.roll(history, 1, dims=1)
            history[:, 0] = spike
            V = V * (1 - spike.detach())  # Reset
            
            spikes.append(spike)
        
        return torch.stack(spikes)
    
    def _surrogate_spike(self, V, alpha=10.0):
        pseudo = (1 / (1 + alpha * (V - self.threshold).abs()))
        return (V >= self.threshold).float() + pseudo * (V - V.detach())
```

## Key Properties
- **Memory capacity**: Scales with number of delays D
- **Energy efficiency**: No sustained input required for recall
- **Biological plausibility**: Synaptic delays are observed in cortex
- **Robustness**: Overlapping motif chains provide noise tolerance

## Applications
- Neuromorphic working memory systems
- Temporal pattern recognition
- Motor sequence storage and replay
- Cognitive modeling of prefrontal cortex

## Paper Reference
- **Title**: Working Memory in Recurrent Spiking Neural Networks with Heterogeneous Synaptic Delays
- **arXiv**: [2604.14096v1](https://arxiv.org/abs/2604.14096v1)
- **Date**: April 20, 2026
- **Author**: Laurent U Perrinet
- **Categories**: q-bio.NC, cs.NE
