---
name: working-memory-rsnn-delays
description: >-
  Working memory implementation in recurrent spiking neural networks using heterogeneous
  synaptic delays. Each synapse equipped with D=41 delays modeled as weight tensor
  W ∈ R^(N×N×D), trained end-to-end with surrogate-gradient BPTT. Network stores arbitrary
  target spike patterns as sequential chains of overlapping Spiking Motifs. Achieves
  F1=1.0 on synthetic benchmark (M=16 patterns, N=512 neurons, T=1000 steps).
  Activation: working memory snn, recurrent spiking memory, heterogeneous delays,
  spiking motifs, temporal pattern storage, surrogate gradient BPTT.
version: 1.0.0
metadata:
  hermes:
    tags: [snn, working-memory, recurrent, delays, temporal-patterns, surrogate-gradient]
    source_paper: "Working Memory in a Recurrent Spiking Neural Networks With Heterogeneous Synaptic Delays (arXiv:2604.14096)"
    citations: 0
---

# Working Memory in RSNN with Heterogeneous Delays

## Overview

Implements working memory in recurrent spiking neural networks by equipping each synapse
with heterogeneous delays, enabling storage and recall of precise temporal patterns.

## Core Architecture

- **Weight tensor**: W ∈ R^(N×N×D) where D=41 delays per synapse
- **Training**: Surrogate-gradient backpropagation through time (BPTT)
- **Memory mechanism**: Sequential chains of overlapping Spiking Motifs
- **Motif length**: D contiguous windows that uniquely predict next time step spikes

## Key Results

| Metric | Value |
|--------|-------|
| F1 Score | 1.0 (perfect recall) |
| Patterns stored | M=16 |
| Neurons | N=512 |
| Time steps | T=1000 |
| Recall position | Emerges near clamped initialization, propagates forward |

## Implementation Pattern

```python
# Weight tensor with heterogeneous delays
W = torch.randn(N, N, D)  # D=41 delays per synapse

# Spiking Motif representation
# Each motif = contiguous window of length D
# Overlapping motifs form sequential chains

# Surrogate gradient BPTT training
# Use surrogate gradient function for non-differentiable spike generation
```

## Applications

- Temporal pattern memory in SNNs
- Sequence learning and prediction
- Neuromorphic working memory systems
- Event-based temporal processing

## Pitfalls

- Surrogate gradient choice critically affects training stability
- Delay dimension D must be tuned to pattern complexity
- Memory capacity scales with N×D but has practical limits
- Recall quality depends on initialization strategy
