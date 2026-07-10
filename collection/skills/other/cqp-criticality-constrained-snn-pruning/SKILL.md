---
name: cqp-criticality-constrained-snn-pruning
version: 1.0.0
description: Criticality-Constrained Quadratic Pruning (CQP) for energy-efficient SNNs combining weight magnitude with surrogate-gradient criticality
tags:
  - spiking-neural-networks
  - pruning
  - neuromorphic-computing
  - energy-efficiency
  - criticality
categories:
  - ai_collection
  - neuromorphic
source: arXiv 2606.30676
date_collected: 2026-07-02
---

# Criticality-Constrained Iterative Pruning (CQP) for Energy-Efficient SNNs

## Overview

CQP is a native PyTorch pipeline for aggressive synaptic pruning in Spiking Neural Networks (SNNs) that fuses weight magnitude with surrogate-gradient criticality into an analytically exact importance metric, eliminating rounding artifacts endemic to solver-based approaches.

## Problem Statement

Deploying SNNs on neuromorphic hardware demands aggressive synaptic pruning while preserving temporal computation integrity. Existing strategies have two critical failures:
1. **Neglect neuronal criticality**: Ignore the dynamic importance of synapses
2. **Convex relaxation artifacts**: OSQP-solver fractional masks overshoot intended sparsity by up to 12 percentage points, causing 44 percentage point accuracy collapse at moderate-to-high sparsity

## Core Methodology

### 1. Combined Importance Metric
Fuses two signals into analytically exact importance:
- **Weight magnitude**: Traditional proxy for synaptic importance
- **Surrogate-gradient criticality**: Measures how much each synapse contributes to gradient flow

### 2. Continuous-Relaxation Trap Characterization
Formally characterizes why convex relaxations fail:
- OSQP-solver fractional masks overshoot target sparsity
- Upon binarization, fractional masks destroy accuracy
- Native binary approach avoids this rounding artifact

### 3. Zombie-Weight Failure Mode
Identifies and remediates a critical failure in iterative pruning:
- Adam's first-moment tensors resurrect pruned synapses
- Violates binary sparsity guarantee
- Solution: Gradient masking during fine-tuning preserves sparsity

### 4. Iterative Schedule
```
prune → fine-tune (with gradient masking) → recompute criticality → repeat
```
Eliminates gradient staleness at high sparsity levels.

### 5. Temporal Analysis for Free Energy Reduction
KL-divergence temporal analysis identifies redundant simulation timesteps:
- Enables free 10% theoretical energy reduction
- No weight modification required
- Compounds with sparsification gains

## Key Results

### Accuracy at 90% Sparsity (MNIST)
| Method | Accuracy |
|--------|----------|
| CQP | 95.6% |
| Magnitude pruning | 93.4% |
| **Improvement** | **+2.2 pp** |

### Criticality Cliff Phenomenon
Criticality-threshold sweep reveals empirical SNN-level analogue of Critical Brain Hypothesis:
- As threshold reaches τ = 0.9, accuracy falls from 87.0% to 14.4%
- Demonstrates phase transition in SNN pruning dynamics

### Compound Energy Reduction
Combined weight sparsification + temporal truncation:
- **73% reduction** in per-inference energy at 70% sparsity
- Practical value for neuromorphic deployment confirmed

## Implementation Patterns

### Criticality Computation
```python
# Pseudocode for CQP importance metric
def compute_importance(model, data):
    weight_magnitude = abs(model.weights)
    
    # Compute surrogate gradients
    surrogate_grads = compute_surrogate_gradients(model, data)
    
    # Criticality = gradient flow through synapse
    criticality = surrogate_grads.abs()
    
    # Combined importance (analytically exact)
    importance = weight_magnitude * criticality
    
    return importance
```

### Iterative Pruning Loop
```python
for iteration in range(num_iterations):
    # 1. Compute importance
    importance = compute_importance(model, dataloader)
    
    # 2. Prune lowest-importance synapses
    mask = importance > threshold
    model.apply_mask(mask)
    
    # 3. Fine-tune with gradient masking
    for batch in dataloader:
        loss = model(batch)
        loss.backward()
        
        # Preserve sparsity: zero gradients for pruned synapses
        optimizer.step_with_mask(mask)
    
    # 4. Recompute criticality for next iteration
```

### Zombie-Weight Prevention
```python
class MaskedAdam(Optimizer):
    def step(self, mask):
        for param in params:
            # Zero out first moment for pruned synapses
            self.state[param]['exp_avg'] *= mask
            param.data *= mask  # Enforce binary sparsity
```

## Pitfalls & Solutions

### Pitfall 1: Continuous Relaxation Trap
**Problem**: Using OSQP or similar solvers produces fractional masks that overshoot target sparsity.
**Solution**: Use native binary importance-based pruning instead of convex relaxation.

### Pitfall 2: Zombie Weights
**Problem**: Adam optimizer resurrects pruned synapses via first-moment accumulation.
**Solution**: Apply gradient masking during fine-tuning; zero first-moment tensors for pruned synapses.

### Pitfall 3: Gradient Staleness
**Problem**: At high sparsity, gradients become stale and mislead importance estimates.
**Solution**: Recompute criticality after each prune-finetune cycle; don't reuse old importance scores.

### Pitfall 4: Criticality Cliff
**Problem**: Accuracy collapses sharply when criticality threshold exceeds τ ≈ 0.9.
**Solution**: Sweep thresholds carefully; stay below the cliff; use iterative schedule to approach high sparsity gradually.

## When to Use

**Apply CQP when:**
- Deploying SNNs on neuromorphic hardware (Loihi, TrueNorth, etc.)
- Need >70% sparsity while maintaining accuracy
- Standard magnitude pruning loses too much accuracy
- Energy efficiency is critical (edge deployment)

**Skip CQP when:**
- SNN is already small (pruning overhead not worth it)
- Target sparsity <50% (magnitude pruning sufficient)
- Not using surrogate gradient training (criticality computation requires it)

## Activation Keywords

SNN pruning, criticality, neuromorphic, energy efficiency, surrogate gradient, iterative pruning, zombie weights, spiking neural networks, synaptic pruning

## Related Patterns

- [[snn-universal-approximation]] - Theoretical foundation for SNN expressivity
- [[surrogate-gradient-snn-training]] - Surrogate gradient methods used in CQP
- [[quantized-snn-hardware-optimization]] - Hardware-aware SNN optimization

## References

- **Paper**: Criticality-Constrained Iterative Pruning for Energy-Efficient Spiking Neural Networks via Combined Importance Scoring
- **arXiv**: [2606.30676](https://arxiv.org/abs/2606.30676)
- **Date**: 2026-06-26
- **Categories**: cs.NE, cs.LG
