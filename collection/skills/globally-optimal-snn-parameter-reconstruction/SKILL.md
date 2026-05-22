---
name: globally-optimal-snn-parameter-reconstruction
description: "Globally optimal Spiking Neural Network (SNN) training via parameter reconstruction methodology. Extends convexification of parallel feedforward threshold networks to parallel recurrent threshold networks, which subsume parallel SNNs as a structured special case. Proposes parameter reconstruction algorithm that eliminates surrogate gradient approximation errors. Use when training SNNs without surrogate gradients, seeking globally optimal solutions, or addressing SNN training approximation errors. Trigger: globally optimal SNN, parameter reconstruction, convexification, threshold networks, surrogate gradient alternatives."
---

# Globally Optimal SNN Training via Parameter Reconstruction

**Paper:** arXiv:2605.08022 (May 2026)
**Authors:** Himanshu Udupi, Xiaocong Yang, ChengXiang Zhai

## Problem

SNN training relies on **surrogate gradients** because the spike function is non-differentiable. This introduces approximation errors that **accumulate across layers**, degrading performance in deep SNNs.

## Solution: Parameter Reconstruction

Extend convexification of parallel feedforward threshold networks → parallel recurrent threshold networks. Parallel SNNs are a structured special case.

### Core Approach

1. **Convexification**: Transform the non-convex SNN training landscape into a convex formulation via parallel recurrent threshold network equivalence
2. **Parameter Reconstruction**: Reconstruct SNN parameters from the convexified solution, avoiding gradient approximation entirely
3. **Hybrid Mode**: Can be combined with surrogate-gradient training for additional gains

### Key Advantages

- **No approximation error**: Eliminates surrogate gradient bias
- **Data scalable**: Performance improves consistently with more data
- **Model-robust**: Works across various SNN architectures and configurations
- **Large-scale potential**: Demonstrated scalability to larger SNNs

## Implementation Patterns

### Pattern 1: Standalone Parameter Reconstruction

```
1. Formulate SNN as parallel recurrent threshold network
2. Apply convexification to training objective
3. Solve convex problem for optimal parameters
4. Reconstruct SNN parameters from convex solution
5. Deploy reconstructed SNN
```

### Pattern 2: Hybrid with Surrogate Gradients

```
1. Initialize SNN with surrogate gradient training (warm start)
2. Apply parameter reconstruction for refinement
3. Fine-tune with hybrid objective
```

## Comparison with Existing Methods

| Method | Approximation Error | Global Optimum | Scalability |
|--------|-------------------|----------------|-------------|
| Surrogate Gradient | Yes (accumulates) | No | Moderate |
| Parameter Reconstruction | No | Yes | High |
| Hybrid (PR + SG) | Reduced | Approximate | High |

## Activation Keywords

- globally optimal SNN training
- parameter reconstruction SNN
- SNN training without surrogate gradient
- convexification threshold network
- spiking neural network optimization
- 2605.08022

## Related Skills

- snn-learning-survey
- surrogate-gradient-snn-training
- spikingjelly-framework

## arXiv Reference

- **arXiv:** https://arxiv.org/abs/2605.08022
- **PDF:** https://arxiv.org/pdf/2605.08022v1
