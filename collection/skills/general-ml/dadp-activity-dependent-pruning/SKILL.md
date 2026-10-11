---
name: dadp-activity-dependent-pruning
description: "DADP: Dynamic Activity-Dependent Pruning, a reverse Hebbian-inspired structural pruning method. Single global threshold dynamically allocates sparsity across network depth, retaining 73.67% accuracy at 99% sparsity on ResNet-18."
tags: [pruning, structural-plasticity, hebbian-learning, sparsity, model-compression, neural-networks]
source: "arXiv:2610.11853"
utility_score: 0.85
---

# DADP: Dynamic Activity-Dependent Pruning, A Reverse Hebbian-Inspired Structural Pruning Method

## Paper Metadata

- **arXiv ID**: 2610.11853
- **Title**: DADP: Dynamic Activity-Dependent Pruning, A Reverse Hebbian-Inspired Structural Pruning Method
- **Authors**: Bhushan Deshpande
- **Published**: 2026-10-08
- **Categories**: cs.LG
- **Link**: https://arxiv.org/abs/2610.11853

## Abstract Summary

Modern neural networks are heavily over-parameterized, incurring substantial compute and memory overhead during training and inference. Existing pruning methods rely on post-hoc magnitude thresholds or static initialization heuristics, often requiring manual per-layer sparsity targets or expensive retraining cycles. DADP is a biologically inspired structural plasticity mechanism that measures connection importance via the accumulated product of pre-synaptic activations and post-synaptic error gradients during training. Using a single global threshold instead of fixed layer budgets, DADP dynamically allocates sparsity across network depth while naturally inducing neuron- and channel-level pruning. Across MLP, VGG-16, ResNet-18, BiLSTM-CRF, and MiniBERT architectures, DADP matches or outperforms Magnitude, SNIP and RigL, retaining 73.67% accuracy (dense baseline: 76.06%) at 99% sparsity on ResNet-18. Matrix-based Shannon entropy and effective rank measurements confirm that DADP preserves latent feature diversity at extreme sparsities without representation collapse.

## Key Contributions

1. **Biologically inspired**: Reverse Hebbian mechanism measuring pre-synaptic activation × post-synaptic error gradient
2. **Dynamic sparsity allocation**: Single global threshold (no per-layer budgets) dynamically allocates sparsity across depth
3. **Structural pruning**: Naturally induces neuron- and channel-level pruning during training
4. **Extreme sparsity**: Retains 73.67% accuracy at 99% sparsity on ResNet-18
5. **Representation preservation**: Shannon entropy and effective rank confirm no representation collapse at extreme sparsities

## Research Implications

- **Training-time pruning**: Eliminates need for post-hoc pruning or expensive retraining
- **Automatic sparsity**: No manual per-layer sparsity targets required
- **Biological plausibility**: Connects to Hebbian learning principles from neuroscience
- **Scalability**: Works across MLP, CNN, RNN, and Transformer architectures
- **Feature diversity**: Preserves latent representation quality even at extreme compression

## Practical Applications

- Compress large models for deployment on resource-constrained devices
- Reduce training and inference compute costs
- Automatically determine optimal sparsity per layer
- Maintain model accuracy while achieving extreme compression
- Apply to diverse architectures without architecture-specific tuning

## Related Work

- Network pruning methods
- Magnitude-based pruning
- SNIP and RigL
- Neural architecture search
- Model compression techniques
