---
name: globally-optimal-snn-parameter-reconstruction
description: >
  Globally optimal Spiking Neural Network (SNN) training via parameter reconstruction.
  Extends convexification of parallel feedforward threshold networks to parallel recurrent
  threshold networks, subsuming parallel SNNs as a structured special case. Eliminates
  surrogate gradient approximation errors by reconstructing optimal parameters directly.
  Use when training SNNs, optimizing spiking networks, avoiding surrogate gradient issues,
  or exploring convex SNN training methods. arXiv: 2605.08022
---

# Globally Optimal SNN Training via Parameter Reconstruction

**arXiv:** 2605.08022 (2026-05-08)
**Authors:** Himanshu Udupi, Xiaocong Yang, ChengXiang Zhai
**Categories:** cs.NE, cs.AI, cs.LG

## Core Problem

SNN training typically relies on surrogate gradients due to non-differentiability of spike functions, introducing approximation errors that accumulate across layers and degrade training quality.

## Key Innovation

Extends convexification theory from parallel feedforward threshold networks to **parallel recurrent threshold networks**, which subsume parallel SNNs as a structured special case. This enables a parameter reconstruction algorithm that achieves globally optimal solutions without surrogate gradient approximation.

## Methodology

### Theoretical Foundation

- Parallel recurrent threshold networks can be convexified, enabling global optimization
- SNNs are a structured special case of parallel recurrent threshold networks
- Parameter reconstruction maps the convex solution back to SNN parameters

### Parameter Reconstruction Algorithm

1. Formulate SNN training as convex optimization over threshold network parameters
2. Solve the convex problem to obtain globally optimal solution
3. Reconstruct SNN parameters from the convex solution
4. Optionally combine with surrogate-gradient training for hybrid optimization

### Key Advantages

- **No surrogate gradient error:** Eliminates approximation errors from non-differentiable spike functions
- **Consistent improvement:** Outperforms surrogate-gradient baselines across tasks
- **Data scalability:** Performance scales with data size
- **Configuration robustness:** Robust to model hyperparameter choices
- **Composability:** Works standalone or combined with surrogate-gradient training

## Applications

- Energy-efficient SNN deployment on neuromorphic hardware
- Large-scale SNN training without error accumulation
- SNNs requiring high training accuracy
- Research on theoretically grounded SNN training methods

## Comparison with Surrogate Gradient Methods

| Aspect | Surrogate Gradient | Parameter Reconstruction |
|--------|-------------------|-------------------------|
| Error | Approximation errors accumulate | No approximation error |
| Optimality | Local optima | Global optimum (convex) |
| Scalability | Degrades with depth | Scales with data |
| Hybrid use | N/A | Can combine with SG |

## Pitfalls

- Convexification applies to **parallel** recurrent threshold networks; sequential SNNs need restructuring
- Theoretical framework requires careful mapping between SNN architecture and threshold network formulation
- Computational cost of convex optimization may be higher than gradient-based methods for very large networks

## Activation Keywords

globally optimal SNN, parameter reconstruction SNN, convex SNN training, surrogate gradient alternative, recurrent threshold network convexification, 2605.08022

## References

- Paper: https://arxiv.org/abs/2605.08022
- PDF: https://arxiv.org/pdf/2605.08022
