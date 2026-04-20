---
name: working-memory-recurrent-spiking-neural-networks
description: "Methodology from paper 'Working Memory in a Recurrent Spiking Neural Networks With Heterogeneous Synaptic Delays...' by Laurent U Perrinet et al. (2026-04-15). Activation: neural, spiking, neuron, network, synaptic, q-bio.NC"
version: 1.0.0
author: Research Synthesis
license: MIT
metadata:
  hermes:
    tags: [neuroscience, research, q-bio.NC]
    source_paper: "Working Memory in a Recurrent Spiking Neural Networks With Heterogeneous Synaptic Delays (arXiv:2604.14096v1)"
    published: 2026-04-15
---

# Working Memory in a Recurrent Spiking Neural Networks With Heterogeneous Synaptic Delays

## Source Paper
- **Title**: Working Memory in a Recurrent Spiking Neural Networks With Heterogeneous Synaptic Delays
- **Authors**: Laurent U Perrinet
- **arXiv**: 2604.14096v1
- **Published**: 2026-04-15
- **Category**: q-bio.NC
- **PDF**: https://arxiv.org/pdf/2604.14096v1
- **Abstract URL**: http://arxiv.org/abs/2604.14096v1

## Abstract

Working memory -- the ability to store and recall precise temporal patterns of neural activity -- remains an open challenge for spiking neural networks (SNNs). We propose a recurrent SNN of $N$ neurons in which each synapse is equipped with $D = 41$ delays, modelled as a weight tensor $\mathbf{W} \in \mathbb{R}^{N \times N \times D}$ and trained end-to-end with surrogate-gradient backpropagation through time. The network stores $M$ arbitrary target spike patterns by representing each as a sequential chain of overlapping Spiking Motifs: contiguous windows of length $D$ that uniquely predict spikes at the next time step. On a synthetic benchmark of $M=16$ patterns ($N=512$ neurons, $T=1000$ steps), training achieves a mean F1 score of $1.0$, with recall emerging first near the clamped initia...

## Key Contributions

1. Working memory -- the ability to store and recall precise temporal patterns of neural activity -- remains an open challenge for spiking neural network...
2. We propose a recurrent SNN of $N$ neurons in which each synapse is equipped with $D = 41$ delays, modelled as a weight tensor $\mathbf{W} \in \mathbb{...
3. The network stores $M$ arbitrary target spike patterns by representing each as a sequential chain of overlapping Spiking Motifs: contiguous windows of...

## Core Concepts

- **Primary**: q-bio.NC
- **Techniques**: neural, spiking, neuron, network, synaptic
- **Application**: Neuroscience research and analysis

## Implementation Pattern

```python
# Based on 2604.14096v1
import numpy as np

class WorkingMemoryRecurrent:
    """Based on arXiv:2604.14096v1"""
    def __init__(self): pass
    def fit(self, data): pass
    def predict(self, new_data): pass
```

## Applications

- Neuroscience research and analysis
- Research and analysis
- Further applications described in paper

## Limitations

See original paper for discussion.

## Activation Keywords

- neural, spiking, neuron, network, synaptic, memory
- q-bio.NC
- 2026 research

## References

- Laurent U Perrinet et al. (2026). "Working Memory in a Recurrent Spiking Neural Networks With Heterogeneous Synaptic Delays." arXiv:2604.14096v1.
