---
name: snn-working-memory-heterogeneous-delays
description: Working memory implementation in recurrent spiking neural networks with heterogeneous synaptic delays. Enables precise temporal pattern storage and recall in SNNs.
version: 1.0.0
author: Research Synthesis
license: MIT
metadata:
  hermes:
    tags: [spiking-neural-network, working-memory, heterogeneous-delays, temporal-processing, neuroscience, snn]
    source_paper: "Working Memory in a Recurrent Spiking Neural Networks With Heterogeneous Synaptic Delays (arXiv:2604.14096v1)"
---

# SNN Working Memory with Heterogeneous Delays

## Overview
Working memory -- the ability to store and recall precise temporal patterns of neural activity -- remains an open challenge for spiking neural networks. This approach leverages heterogeneous synaptic delays in recurrent SNNs to create robust temporal memory traces, enabling precise pattern storage and recall.

## Core Concepts

### Heterogeneous Delays
- Different synapses have different transmission delays (sampled from a distribution)
- Delays create diverse temporal filters across the network
- Combined with recurrent connectivity, enables sustained activity patterns

### Memory Mechanism
- **Storage**: Input patterns encoded in spatiotemporal spike patterns
- **Maintenance**: Recurrent activity with heterogeneous delays sustains patterns
- **Recall**: Network dynamics naturally reconstruct stored patterns from partial cues

### Key Advantages
- Biologically plausible (real synapses have heterogeneous delays)
- No external clock or gating mechanism required
- Naturally handles variable-duration inputs
- Energy-efficient (spike-based computation)

## Implementation Pattern
```python
class DelayedRecurrentSNN:
    def __init__(self, n_neurons, delay_range=(1, 20), membrane_tau=20.0):
        self.n_neurons = n_neurons
        self.delays = np.random.randint(*delay_range, size=(n_neurons, n_neurons))
        self.max_delay = delay_range[1]
        self.weights = np.random.randn(n_neurons, n_neurons) * 0.1
        self.spike_buffer = [np.zeros(n_neurons)] * self.max_delay
        self.membrane = np.zeros(n_neurons)
        self.tau = membrane_tau
    
    def step(self, input_spikes):
        recurrent = np.zeros(self.n_neurons)
        for i in range(self.n_neurons):
            for j in range(self.n_neurons):
                delay = self.delays[i, j]
                if delay < len(self.spike_buffer):
                    recurrent[i] += self.weights[i, j] * self.spike_buffer[-delay][j]
        total_input = input_spikes + recurrent
        self.membrane = self.membrane * (1 - 1/self.tau) + total_input
        spikes = (self.membrane > 1.0).astype(float)
        self.membrane -= spikes
        self.spike_buffer.append(spikes)
        if len(self.spike_buffer) > self.max_delay:
            self.spike_buffer.pop(0)
        return spikes
```

## Applications
- Neuromorphic working memory systems
- Temporal sequence processing
- Brain-inspired AI memory modules
- Low-power edge AI with SNNs

## Activation Keywords
- SNN working memory, spiking neural network memory, heterogeneous synaptic delays, temporal pattern recall, recurrent spiking memory, 脉冲神经网络工作记忆, 异质延迟 SNN

## References
- Working Memory in a Recurrent Spiking Neural Networks With Heterogeneous Synaptic Delays
- Authors: Laurent U Perrinet
- Published: 2026-04-15
- arXiv: https://arxiv.org/abs/2604.14096v1