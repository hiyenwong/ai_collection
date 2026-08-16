---
name: lapis-laplacian-spiking-attention
description: "Lapis spiking attention mechanism."
metadata:
  arxiv_id: "2608.11865"
  published: "2026-08-12"
  authors: "Kaiwen Tang, Jiaqi Zheng, Zixuan Zhu, Yiqun Wang, Zhanglu Yan, Weng-Fai Wong"
  tags: [spiking-neural-networks, attention-mechanisms, time-to-first-spike, laplacian-kernel, energy-efficiency, vision-transformers]
license: Complete terms in LICENSE.txt
---

# Lapis: Laplacian Spiking Attention

## Overview
Lapis is a novel spiking attention mechanism that fundamentally rethinks how token relationships are computed in spiking neural networks. Instead of using traditional dot-product attention inherited from dense networks, Lapis leverages the native temporal representation of spikes through first-spike timing.

The core innovation is defining token relations directly from spike timing patterns rather than treating spikes as computational constraints imposed on standard attention mechanisms.

## Key Components

### 1. Time-to-First-Spike (TTFS) Coding
- Represents information by the latency of the first spike
- Each activation is encoded as its first-spike latency under TTFS coding
- Nearby activation values produce nearby firing times, creating natural temporal patterns

### 2. Temporal Distance Calculation
For query token i and key token j in head h:
- Let tQ,h_i and tK,h_j denote channel-wise first-spike latency vectors
- Compute temporal distance: D^h_ij = ||tQ,h_i - tK,h_j||_1
- Smaller distance indicates closer agreement between first-spike patterns

### 3. Laplacian Kernel Affinity
Convert temporal distance to positive affinity:
- A^h_ij = exp(-D^h_ij / τ^h)
- τ^h > 0 is a pre-head learnable temporal scale
- Exponential decay matches subthreshold dynamics of LIF membrane
- Provides leakage-based realization of temporal affinity

### 4. Implementation Advantages
- **No multiplication**: Eliminates all multiplication between query and key channels
- **Energy efficient**: Reduces estimated arithmetic energy by 14.5× relative to dense dot-product attention
- **Hardware friendly**: Row normalization reduces to bit shift under power-of-two rounding
- **Biologically plausible**: Membrane leakage dynamics naturally implement the exponential mapping

## Performance Results
- **CIFAR-10**: 96.56% top-1 accuracy (within 0.53 points of dot-product scoring)
- **ImageNet-1K**: 83.25% top-1 accuracy with 6-bit quantization
- **Energy**: 3.28 mJ per image (estimated arithmetic energy)

## When to Use This Skill
Use Lapis when:
- Implementing energy-efficient spiking vision transformers
- Designing attention mechanisms that leverage spike timing as information representation
- Optimizing arithmetic operations in SNNs to eliminate expensive multiplications
- Building biologically-inspired attention that aligns with neuronal membrane dynamics
- Working with TTFS coding schemes in spiking networks

## Implementation Guidelines

### Architecture Integration
1. Retain standard multi-head query, key, and value projections
2. Replace dot-product similarity with temporal-distance formulation
3. Implement Laplacian kernel using LIF membrane leakage dynamics
4. Apply power-of-two rounding for efficient row normalization

### Training Considerations
- Use matched backbone and training schedule as baseline
- TTFS coding window length affects performance (T=15 for Lapis-B, T=20 for Lapis-L)
- 6-bit weight quantization maintains accuracy while reducing energy

### Hardware Deployment
- Leverage spike sparsity for reduced computation
- Implement membrane accumulation for temporal distance calculation
- Use bit-shift operations for normalization instead of division

## Pitfalls to Avoid
- **Don't treat spikes as constraints**: Lapis treats spike timing as the primary information carrier, not just a sparsity constraint
- **Avoid dense similarity functions**: Traditional dot products or discrete operators miss the temporal structure
- **Don't ignore membrane dynamics**: The exponential decay should be implemented through actual leakage processes when possible
- **Beware of TTFS limitations**: Ensure your application can work with at most one spike per neuron per coding window

## References
- Original paper: https://arxiv.org/abs/2608.11865
- Related work on TTFS coding: Park et al. (2020), Göltz et al. (2021)
- Spiking Vision Transformers: Zhao et al. (2025), Yan et al. (2025)

## Activation Keywords
- lapis
- laplacian spiking attention
- first-spike timing attention
- membrane leakage attention
- ttfs attention
- spiking transformer attention
- energy-efficient spiking attention