---
name: working-memory-heterogeneous-delays
category: neuroscience
description: Working memory in recurrent spiking neural networks using heterogeneous synaptic delays (2026-04 update). Enables energy-efficient temporal pattern storage and recall in SNNs.
activation: ["working memory", "heterogeneous delays", "spiking motifs", "temporal patterns", "SNN memory", "delay networks"]
---

# Working Memory in Recurrent SNNs with Heterogeneous Synaptic Delays

## Overview
Based on Perrinet (2026) "Working Memory in a Recurrent Spiking Neural Networks With Heterogeneous Synaptic Delays" (arXiv:2604.14096v1, q-bio.NC).

Demonstrates that heterogeneous synaptic delays provide an efficient substrate for working memory in spiking neural networks, enabling energy-efficient neuromorphic edge deployment.

## Key Findings

### Architecture
- Recurrent SNN of N neurons with D=41 delays per synapse
- Weight tensor W ∈ R^(N×N×D) trained end-to-end with surrogate-gradient backpropagation through time
- Each synapse equipped with multiple delays (not just a single fixed delay)

### Working Memory Mechanism
- Stores M arbitrary target spike patterns by representing each as sequential chains of overlapping **Spiking Motifs**
- Contiguous windows of length D uniquely predict spikes at the next time step
- Recall emerges first near clamped initialization window and propagates forward in time

### Performance
- Synthetic benchmark: M=16 patterns, N=512 neurons, T=1000 steps
- Mean F1 score of 1.0 (perfect recall)
- Energy-efficient neuromorphic edge deployment enabled

## Implementation Guidelines

### Key Components
1. **Heterogeneous Delay Tensor**: W ∈ R^(N×N×D) where D is number of distinct delays
2. **Spiking Motif Chains**: Sequential overlapping windows of length D
3. **Surrogate Gradient BPTT**: End-to-end training with surrogate gradients through time

### Training Pipeline
```
1. Define N neurons, D delays, M target patterns
2. Initialize weight tensor W ∈ R^(N×N×D)
3. Clamp initialization window with target pattern
4. Train with surrogate-gradient BPTT
5. Recall emerges from initialization and propagates forward
```

### Hyperparameters
- N = 512 neurons (scalable)
- D = 41 delays per synapse
- M = 16 stored patterns
- T = 1000 time steps

## Applications
- Working memory in neuromorphic chips
- Energy-efficient temporal pattern storage
- Edge deployment of SNNs
- Cognitive modeling of working memory

## References
- arXiv:2604.14096v1 (2026-04-15)
- q-bio.NC category
