---
name: snn-working-memory-heterogeneous-delays
category: ai_collection
description: Working memory implementation in recurrent spiking neural networks with heterogeneous synaptic delays. Demonstrates how delayed synapses enable temporal pattern storage without external input, enabling energy-efficient neuromorphic edge deployment.
source: arXiv:2604.14096v1
paper_title: "Working Memory in a Recurrent Spiking Neural Networks With Heterogeneous Synaptic Delays"
authors: "Laurent U Perrinet"
date: 2026-04-15
keywords: ["SNN", "working memory", "heterogeneous delays", "spiking motifs", "surrogate gradient", "neuromorphic"]
trigger: ["working memory snn", "heterogeneous delays", "spiking motifs", "temporal pattern storage", "recurrent snn memory", "synaptic delay memory"]
---

## Working Memory in Spiking Neural Networks with Heterogeneous Delays

### Core Problem
Working memory — the ability to store and recall precise temporal patterns of neural activity — remains an open challenge for spiking neural networks (SNNs). Traditional SNNs lack a natural mechanism for temporal pattern retention.

### Key Innovation
A recurrent SNN where each synapse has multiple heterogeneous delays (D=41), modeled as a weight tensor **W ∈ ℝ^(N×N×D)**, trained end-to-end with surrogate-gradient backpropagation through time (BPTT).

### Architecture
- **Network**: Recurrent SNN of N neurons (tested with N=512)
- **Synaptic delays**: Each synapse has D=41 discrete delays
- **Weight tensor**: **W ∈ ℝ^(N×N×D)** — each (i,j,d) entry represents connection from neuron j to neuron i with delay d
- **Neuron model**: Leaky Integrate-and-Fire (LIF)
- **Training**: Surrogate-gradient BPTT

### Working Memory Mechanism

#### Spiking Motifs
Each target spike pattern is stored as a **sequential chain of overlapping Spiking Motifs**:
- A motif is a contiguous window of length D in the spike pattern
- The motif uniquely predicts spikes at the next time step
- Overlapping motifs create a chain that reconstructs the full pattern

#### Recall Dynamics
- Recall emerges first near the **clamped initialization window** (first few time steps)
- Recall then **propagates forward in time** through the recurrent network
- The heterogeneous delays create a natural "memory buffer" that sustains activity

### Mathematical Formulation

```python
# Synaptic current with heterogeneous delays
I_i(t) = Σ_j Σ_d W[i,j,d] * spike_j(t-d)

# LIF neuron dynamics
τ_m * dV_i/dt = -V_i(t) + I_i(t) + I_ext
if V_i(t) >= V_th: spike_i(t) = 1, V_i(t) = V_reset

# Training with surrogate gradient
# Loss: Binary cross-entropy between output spikes and target pattern
# Gradient: ∂L/∂W[i,j,d] = ∂L/∂spike_i * ∂spike_i/∂V_i * ∂V_i/∂W[i,j,d]
# Surrogate: Replace ∂spike/∂V with smooth approximation (e.g., sigmoid derivative)
```

### Benchmark Results
- **Synthetic benchmark**: M=16 target patterns, N=512 neurons, T=1000 time steps
- **Performance**: Mean F1 score of **1.0** (perfect recall)
- **Energy efficiency**: Near-linear relationship between bump velocity and synaptic modulation
- **Memory capacity**: Scales with D (number of delays)

### Implementation Guide

```python
import torch
import torch.nn as nn

class HeterogeneousDelaySNN(nn.Module):
    def __init__(self, n_neurons, n_delays=41, tau_mem=20.0, dt=1.0):
        super().__init__()
        self.n = n_neurons
        self.d = n_delays
        self.tau_mem = tau_mem
        self.dt = dt
        
        # Weight tensor: [N, N, D]
        self.W = nn.Parameter(torch.randn(n_neurons, n_neurons, n_delays) * 0.1)
        
        # Spike history buffer for each delay
        self.spike_history = None
        
    def forward(self, n_timesteps, init_spikes=None):
        V = torch.zeros(self.n)  # Membrane potentials
        spike_history = torch.zeros(self.n, self.d)
        output_spikes = []
        
        for t in range(n_timesteps):
            # Compute synaptic current with heterogeneous delays
            I = torch.zeros(self.n)
            for d in range(self.d):
                if t - d >= 0:
                    I += torch.matmul(self.W[:, :, d], spike_history[:, d])
            
            # LIF dynamics
            dV = self.dt / self.tau_mem * (-V + I)
            V = V + dV
            
            # Spike (with surrogate gradient)
            spike = self.surrogate_spike(V)
            
            # Update history
            spike_history = torch.roll(spike_history, 1, dims=1)
            spike_history[:, 0] = spike
            
            V = V * (1 - spike)  # Reset after spike
            output_spikes.append(spike)
            
        return torch.stack(output_spikes)
    
    def surrogate_spike(self, V, threshold=1.0, alpha=10.0):
        # Fast sigmoid surrogate
        return (V >= threshold).float() + \
               (1 / (1 + alpha * torch.abs(V - threshold))) * \
               (V - V.detach())
```

### Practical Applications
1. **Neuromorphic edge deployment**: Low-power temporal pattern recall
2. **Robotic control**: Storing motor sequences for replay
3. **Speech processing**: Temporal pattern recognition
4. **BCI**: Decoding neural temporal patterns

### Key Insights
- Heterogeneous delays are a **biologically plausible** mechanism for working memory
- The system is **energy-efficient** — no constant external input needed
- Recall is **robust to noise** due to overlapping motif chains
- Memory capacity scales with delay diversity, not network size

### Paper Reference

- **Title**: Working Memory in Recurrent Spiking Neural Networks with Heterogeneous Delays
- **arXiv**: [2604.14096v1](https://arxiv.org/abs/2604.14096v1)
- **Date**: April 20, 2026
- **Venue**: arXiv preprint
- **Authors**: (see paper for full list)
- **Categories**: q-bio.NC, cs.NE
- **PDF**: https://arxiv.org/pdf/2604.14096v1.pdf


## References
- arXiv:2604.14096v1 (Original paper, 2026-04-15)
- arXiv:2604.13624v1 (Follow-up, 2026-04-15)
- arXiv:2604.15662 (Latest findings, 2026-04-18)
- arXiv:2604.15464 (Latest findings, 2026-04-18)
- Related: Working memory in biological neural circuits
- Related: Synaptic delay as computational resource