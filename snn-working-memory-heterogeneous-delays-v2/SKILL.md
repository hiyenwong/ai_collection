---
name: snn-working-memory-heterogeneous-delays-v2
description: "Working memory -- the ability to store and recall precise temporal patterns of neural activity -- remains an open challenge for spiking neural networks (SNNs). We propose a recurre... Activation: spiking neural network, working memory, heterogeneous delay, neuromorphic, recurrent network"
---

# Working Memory in a Recurrent Spiking Neural Networks With Heterogeneous Synaptic Delays

## Overview

Working memory -- the ability to store and recall precise temporal patterns of neural activity -- remains an open challenge for spiking neural networks (SNNs). We propose a recurrent SNN of $N$ neurons in which each synapse is equipped with $D = 41$ delays, modelled as a weight tensor $\mathbf{W} \in \mathbb{R}^{N \times N \times D}$ and trained end-to-end with surrogate-gradient backpropagation through time. The network stores $M$ arbitrary target spike patterns by representing each as a sequential chain of overlapping Spiking Motifs: contiguous windows of length $D$ that uniquely predict spikes at the next time step. On a synthetic benchmark of $M=16$ patterns ($N=512$ neurons, $T=1000$ steps), training achieves a mean F1 score of $1.0$, with recall emerging first near the clamped initia

## Source Paper

- **Title**: Working Memory in a Recurrent Spiking Neural Networks With Heterogeneous Synaptic Delays
- **Authors**: Laurent U Perrinet
- **arXiv**: [2604.14096v1](https://arxiv.org/pdf/2604.14096v1)
- **Published**: 2026-04-15
- **Categories**: q-bio.NC
- **PDF**: [2604.14096v1](https://arxiv.org/pdf/2604.14096v1)

## Core Concepts

### Key Contributions

1. Working memory -- the ability to store and recall precise temporal patterns of neural activity -- remains an open challenge for spiking neural networks (SNNs).

2. We propose a recurrent SNN of $N$ neurons in which each synapse is equipped with $D = 41$ delays, modelled as a weight tensor $\mathbf{W} \in \mathbb{R}^{N \times N \times D}$ and trained end-to-end with surrogate-gradient backpropagation through time.

3. The network stores $M$ arbitrary target spike patterns by representing each as a sequential chain of overlapping Spiking Motifs: contiguous windows of length $D$ that uniquely predict spikes at the next time step.

4. On a synthetic benchmark of $M=16$ patterns ($N=512$ neurons, $T=1000$ steps), training achieves a mean F1 score of $1.0$, with recall emerging first near the clamped initialisation window and propagating forward in time.

## Practical Applications

### Temporal Pattern Memory
- Implement working memory for temporal sequence recall
- Deploy heterogeneous synaptic delays for precise timing
- Use recurrent SNNs for short-term memory tasks

### Implementation

```python
import numpy as np

class RecurrentSNNHeterogeneousDelay:
    def __init__(self, n_neurons, n_delays=41):
        self.N = n_neurons
        self.D = n_delays
        self.W = np.random.randn(n_neurons, n_neurons, n_delays) * 0.1
        self.membrane = np.zeros(n_neurons)
        self.spike_history = np.zeros((n_neurons, n_delays))
    
    def step(self, external_input):
        # Advance SNN by one time step with heterogeneous delays
        delayed_input = np.zeros(self.N)
        for d in range(self.D):
            delayed_input += np.sum(self.W[:, :, d] * self.spike_history[:, d:d+1], axis=1)
        self.membrane += delayed_input + external_input
        self.membrane *= 0.95  # Leak
        spikes = (self.membrane > 1.0).astype(float)
        self.membrane = np.where(spikes > 0, 0, self.membrane)
        self.spike_history = np.roll(self.spike_history, 1, axis=1)
        self.spike_history[:, 0] = spikes
        return spikes
```

## Implementation Steps

1. **Understand the core methodology** - Read the paper's method section carefully
2. **Reproduce baseline results** - Start with the paper's reported experiments
3. **Adapt to your domain** - Modify parameters for your specific use case
4. **Evaluate and iterate** - Compare against baselines, measure improvement

## Limitations

- Paper-specific limitations should be verified against full text
- Implementation details may require access to supplementary materials
- Hardware requirements vary by application scale

## Related Work

- Recurrent SNN architectures
- Heterogeneous delay modeling
- Temporal pattern learning

## Activation Keywords

- spiking neural network, working memory, heterogeneous delay, neuromorphic, recurrent network
