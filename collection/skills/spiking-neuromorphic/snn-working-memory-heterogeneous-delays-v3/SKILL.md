---
name: snn-working-memory-heterogeneous-delays-v3
description: Working memory implementation in recurrent spiking neural networks using heterogeneous synaptic delays. Uses multi-delay synapse weight tensors to store temporal patterns. Activation: snn, working-memory, spiking, delays, temporal-patterns, neuroscience, brain, neural
version: 1.0.0
author: Hermes Agent
license: MIT
metadata:
  hermes:
    source_paper: "Working Memory in a Recurrent Spiking Neural Networks With Heterogeneous Synaptic Delays (arXiv:2604.14096)"
    authors: "Laurent U Perrinet"
    published: 2026-04-15
    tags: ["snn", "working-memory", "spiking", "delays", "temporal-patterns"]
---

# Working Memory in Recurrent SNNs with Heterogeneous Synaptic Delays

## Overview
Recurrent SNN where each synapse has D=41 delays modeled as weight tensor W in R^(NxNxD). Enables storing and recalling precise temporal patterns without explicit training.

Based on: [Working Memory in a Recurrent Spiking Neural Networks With Heterogeneous Synaptic Delays](https://arxiv.org/abs/2604.14096) (2026-04-15)

## Key Insights
- Each synapse equipped with multiple delays (D=41) forms weight tensor W in R^(NxNxD)
- Heterogeneous delays enable temporal pattern storage without explicit training
- Self-organization through STDP-like plasticity rules
- Demonstrates working memory capability in spiking networks

## Applications
- Temporal pattern recognition
- Working memory modeling
- Neuromorphic computing
- Sequence learning

## Abstract
Working memory is the ability to store and recall precise sequences of events. We show that recurrent spiking neural networks with heterogeneous synaptic delays can naturally implement working memory. Each synapse is equipped with multiple delays, forming a weight tensor W ∈ R^(N×N×D). This enables storing and recalling temporal patterns without explicit training, demonstrating self-organization through STDP-like plasticity.

## Methodology

### Multi-Delay Synapse Model
Each synapse modeled as weight tensor W in R^(NxNxD) where D=41 delays.
- Neurons i to j connections have D distinct temporal pathways
- Delays distributed uniformly across [d_min, d_max]
- Enables temporal pattern storage via spike timing
    
### Pattern Storage and Recall
1. Encode temporal patterns as spike trains
2. Store via heterogeneous delay pathways
3. Recall triggered by partial pattern cues

## Reference
Laurent U Perrinet. Working Memory in a Recurrent Spiking Neural Networks With Heterogeneous Synaptic Delays. arXiv:2604.14096, 2026-04-15.
URL: https://arxiv.org/abs/2604.14096
