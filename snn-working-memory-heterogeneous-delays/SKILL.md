---
name: snn-working-memory-heterogeneous-delays
description: Working memory implementation in recurrent spiking neural networks using heterogeneous synaptic delays. Leverages diverse axonal conduction delays to create temporally distributed representations, enabling persistent activity without continuous stimulation. Use for SNN-based working memory, temporal sequence processing, and delay-dependent neural computation. Activation: working memory SNN, heterogeneous delays, synaptic delay, recurrent SNN memory, temporal representation, delay-based memory
version: 1.0.0
metadata:
  hermes:
    source_paper: "Working Memory in a Recurrent Spiking Neural Networks With Heterogeneous Synaptic Delays (arXiv:2604.14096v1)"
    published: "2026-04-15"
    categories: ['q-bio.NC']
    authors: Laurent U Perrinet
---

# Working Memory in Recurrent SNNs with Heterogeneous Delays

## Overview
Recurrent spiking neural networks achieve working memory through heterogeneous synaptic delays. Different axonal conduction delays create temporally distributed activity patterns that sustain representations without requiring continuous input or explicit recurrent loops.

## Core Concept

### Heterogeneous Delay Mechanism
- Synaptic delays vary across connections (1-100ms range)
- Each delay creates a different temporal window for signal propagation
- Network naturally maintains activity traces across multiple timescales
- Memory emerges from the distribution of delays, not from explicit storage

### Memory Dynamics
1. **Encoding**: Input spike triggers cascade through delayed pathways
2. **Maintenance**: Distributed delays sustain activity without continuous firing
3. **Retrieval**: Current state reflects weighted combination of past inputs
4. **Capacity**: Memory span scales with delay distribution range

## Implementation Pattern
```python
import torch

class DelayedRecurrentSNN:
    """Recurrent SNN with heterogeneous synaptic delays."""
    def __init__(self, n_neurons, max_delay=50, dt=0.001):
        self.n_neurons = n_neurons
        self.max_delay = max_delay
        self.dt = dt
        # Random heterogeneous delays
        self.delays = torch.randint(1, max_delay + 1, (n_neurons, n_neurons))
        self.weights = torch.randn(n_neurons, n_neurons) * 0.1 / n_neurons
        # Delay line buffer
        self.buffer = torch.zeros(max_delay, n_neurons)
        self.membrane = torch.zeros(n_neurons)
        
    def step(self, input_spikes, threshold=1.0):
        """One timestep with heterogeneous delays."""
        # Read from delay lines
        delayed_input = torch.zeros(self.n_neurons)
        for t in range(1, self.max_delay + 1):
            idx = t - 1
            if idx < self.buffer.shape[0]:
                delayed = self.buffer[idx]
                mask = (self.delays == t).float()
                delayed_input += (self.weights * mask * delayed).sum(dim=1)
        
        # Update membrane potential
        self.membrane = self.membrane * 0.95 + input_spikes + delayed_input
        
        # Generate spikes
        spikes = (self.membrane > threshold).float()
        self.membrane = self.membrane * (1 - spikes)
        
        # Update delay buffer
        self.buffer = torch.roll(self.buffer, 1, dims=0)
        self.buffer[0] = spikes
        
        return spikes
```

## Key Properties
- **No continuous firing needed**: Memory maintained by delay structure
- **Multiple timescales**: Natural support for multi-temporal processing
- **Energy efficient**: Sparse spiking with sustained representation
- **Biological realism**: Matches axonal delay diversity in cortex

## Applications
- Working memory tasks (delayed match-to-sample)
- Temporal sequence prediction
- Speech and audio processing
- Robot control with temporal dependencies

## References
- Laurent U Perrinet, "Working Memory in a Recurrent Spiking Neural Networks With Heterogeneous Synaptic Delays", arXiv:2604.14096v1, 2026-04-15
