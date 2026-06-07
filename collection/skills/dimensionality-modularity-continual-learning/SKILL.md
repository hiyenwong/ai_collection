---
name: dimensionality-modularity-continual-learning
description: "Framework for understanding when architectural modularity matters in continual learning based on representational dimensionality. Shows that modular networks only outperform monolithic ones in low-dimensional regimes where representational geometry is constrained. Triggers: continual learning dimensionality, modular vs monolithic networks, representational geometry, stability-plasticity tradeoff, structure matters continual learning."
---

# Dimensionality-Controlled Modularity in Continual Learning

> Framework establishing representational dimensionality as the key organizing variable governing when structural separation (modularity) becomes functionally relevant in continual learning systems.

## Metadata
- **Source**: arXiv:2604.27656
- **Authors**: Kathrin Korte, Joachim Winter Pedersen, Eleni Nisioti, Sebastian Risi
- **Published**: 2026-04-30
- **Categories**: cs.LG, cs.AI, cs.NE

## Core Methodology

### Key Innovation
This paper resolves a fundamental question in continual learning: **when does architectural modularity actually matter?** The answer: it depends on representational dimensionality.

### Main Findings

1. **High-dimensional regime**: Architecture has minimal impact. Representations are sufficiently unconstrained to accommodate multiple tasks without strong interference, regardless of whether the network is modular or monolithic.

2. **Low-dimensional (rich) regime**: Architectural separation becomes decisive. Modular networks exhibit:
   - **Graded alignment** of task-specific subspaces
   - **Overlap** for similar tasks (enabling transfer)
   - **Partial orthogonalization** for moderately dissimilar tasks
   - **Stronger separation** for dissimilar tasks (preventing interference)

3. **This graded geometry is absent** in single-network baselines.

### Technical Framework

- **Sequential task paradigm** inspired by transfer-interference studies
- **Task-partitioned modular recurrent network** vs. **single-module baseline**
- **Systematic variation** of:
  - Task similarity (low, medium, high)
  - Weight initialization scale → controls effective dimensionality of learned representations
- **Representational geometry analysis** via subspace alignment and overlap metrics

## Implementation Guide

### Designing Continual Learning Systems

1. **Assess representational dimensionality** of your problem:
   - High-dimensional tasks → modularity may not provide significant benefits
   - Low-dimensional tasks → modular architectures are likely advantageous

2. **Match architecture to dimensionality**:
   - For low-dimensional problems: use task-partitioned or modular designs
   - For high-dimensional problems: simpler architectures may suffice

3. **Adaptive geometry principle**: The optimal architecture depends on the effective dimensionality, not just task similarity or network size alone.

### Experiment Replication
```
Variables to control:
- Task similarity (manipulated via input distribution overlap)
- Weight initialization scale (controls learning regime)
- Network architecture (modular vs. monolithic)

Metrics to measure:
- Effective dimensionality of learned representations
- Subspace alignment between tasks
- Transfer and interference rates
```

## Applications
- Continual learning system design
- Neural architecture selection for sequential tasks
- Understanding stability-plasticity tradeoff mechanisms
- Representational geometry analysis in deep networks

## Pitfalls
- Don't assume modularity always helps — it's dimensionality-dependent
- Weight initialization scale is a critical but often overlooked hyperparameter
- High-dimensional regimes can mask architectural differences

## Related Skills
- cortex-continual-learning-ftn
- gradient-free-continual-learning-snn
- cortex-inspired-continual-learning-ftn
- neuromorphic-continual-nuclear-ics
- feedback-hebbian-continual-learning
