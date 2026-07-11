---
name: criticality-constrained-snn-pruning
category: ai_collection
trigger_words:
  - SNN pruning
  - criticality-constrained pruning
  - CQP pruning
  - surrogate-gradient criticality
  - neuromorphic deployment
  - energy-efficient SNN
  - continuous-relaxation trap
  - zombie-weight
  - criticality cliff
  - 临界性约束剪枝
  - 脉冲神经网络剪枝
  - 神经形态部署
description: >
  Criticality-Constrained Quadratic Pruning (CQP) methodology for energy-efficient SNN deployment on neuromorphic hardware.
  Combines weight magnitude with surrogate-gradient criticality into analytically exact importance metric.
  Identifies continuous-relaxation trap, zombie-weight failure mode, and criticality cliff phenomenon.
  Achieves 95.6% accuracy at 90% sparsity on MNIST; 73% energy reduction at 70% sparsity.
arxiv_id: "2606.30676"
authors: ["Muhammad Hamza"]
affiliation: "IIT Kharagpur"
date: "2026-06-26"
---

# Criticality-Constrained Iterative Pruning for Energy-Efficient SNNs (CQP)

## Overview

CQP is a native PyTorch pipeline that fuses weight magnitude with surrogate-gradient criticality into an analytically exact importance metric for SNN pruning. It addresses three critical failure modes in existing SNN pruning approaches:

1. **Continuous-Relaxation Trap**: OSQP-solver fractional masks overshoot intended sparsity by up to 12 percentage points, causing 44pp accuracy collapse upon binarization
2. **Zombie-Weight Failure Mode**: Adam's first-moment tensors resurrect pruned synapses, violating binary sparsity guarantee
3. **Gradient Staleness at High Sparsity**: Criticality scores become outdated as network operates at extreme sparsity levels

## Core Methodology

### Importance Metric

The CQP importance score combines two signals:

- **Weight magnitude** |w|: Standard magnitude-based pruning signal
- **Surrogate-gradient criticality**: Measures how much each synapse contributes to the surrogate gradient flow during backpropagation-through-time (BPTT)

Combined importance: I(w) = α|w| + β·criticality(w)

This analytically exact metric avoids the rounding artifacts endemic to QP-based approaches.

### Continuous-Relaxation Trap

**Problem**: When casting pruning as a Quadratic Program (QP) with continuous relaxation (e.g., via CVXPY/OSQP), the solver produces fractional masks. Binarizing these masks causes them to overshoot the target sparsity level by up to 12pp.

**Consequence**: This overshoot precipitates a 44pp accuracy collapse at moderate-to-high sparsity levels.

**Solution**: CQP bypasses QP relaxation entirely, using the analytically exact combined importance metric instead.

### Zombie-Weight Remediation

**Problem**: After pruning synapses to zero, Adam optimizer's first-moment estimate retains momentum from pre-pruning gradients. This "resurrects" pruned weights during fine-tuning.

**Solution**: Reset Adam's first-moment tensors to zero for pruned synapses, combined with gradient masking to enforce hard sparsity constraints.

### Iterative Schedule

The CQP pipeline follows an iterative schedule:

1. **Prune**: Remove synapses below importance threshold
2. **Fine-tune**: Train with gradient masking to enforce sparsity
3. **Recompute criticality**: Update importance scores with current weights
4. **Repeat**: Continue until target sparsity achieved

This eliminates gradient staleness that plagues single-shot pruning at high sparsity.

### Temporal Redundancy Analysis

Using KL-divergence analysis of spike-train distributions across timesteps, CQP identifies redundant simulation timesteps that contribute minimal information.

**Result**: Free 10% theoretical energy reduction without weight modification by truncating redundant timesteps.

## Key Findings

### Criticality Cliff

A criticality-threshold sweep reveals an empirical **criticality cliff**: accuracy falls from 87.0% to 14.4% as the threshold τ crosses 0.9. This constitutes a quantitative SNN-level analogue of the **Critical Brain Hypothesis** — the network operates optimally near a critical point, and excessive pruning pushes it into a subcritical regime.

### Performance Results

**MNIST (60,000 training examples)**:
- CQP at 90% sparsity: 95.6% accuracy
- Magnitude pruning at 90% sparsity: 93.4% accuracy
- Improvement: +2.2 percentage points

**Energy Efficiency**:
- At 70% sparsity: 73% compound reduction in per-inference energy
- Combines weight sparsification + temporal truncation

### Connection to Critical Brain Hypothesis

The criticality cliff phenomenon provides empirical evidence that SNNs exhibit critical dynamics analogous to biological neural networks. Near-critical operation maximizes information processing capacity while maintaining stability.

## Implementation Notes

### PyTorch Implementation

CQP is implemented as a native PyTorch pipeline:

- Surrogate-gradient criticality computed via BPTT
- Importance scores computed analytically (no QP solver needed)
- Gradient masking for hard sparsity enforcement
- Adam moment reset for zombie-weight remediation

### Surrogate Gradient Choice

The methodology uses standard surrogate gradient functions for SNN training (e.g., arctangent, rectangular, exponential). Criticality computation requires differentiable approximations of the spike function.

### Sparsity Schedule

Recommended iterative schedule:
- Start with low sparsity (e.g., 30%)
- Increase by 10-20% per iteration
- Fine-tune for 5-10 epochs between pruning rounds
- Stop at target sparsity or when accuracy degrades

## Practical Guidelines

### When to Use CQP

- Deploying SNNs on neuromorphic hardware (Loihi, TrueNorth, SpiNNaker)
- Need aggressive pruning (>70% sparsity) while preserving accuracy
- Training SNNs with surrogate gradient methods
- Energy-constrained edge deployment

### When Not to Use

- Very low sparsity targets (<30%) — magnitude pruning may suffice
- Non-surrogate-gradient SNN training (e.g., STDP, evolutionary methods)
- When QP-based pruning is specifically required (though CQP outperforms QP)

### Pitfalls

- **Zombie weights**: Always reset Adam moments after pruning
- **Gradient staleness**: Recompute criticality after each pruning round
- **Criticality cliff**: Monitor accuracy degradation near τ = 0.9; avoid over-pruning
- **Temporal redundancy**: Don't forget to analyze timestep redundancy for additional energy savings

## Activation Triggers

Use this skill when working with:
- SNN pruning or compression
- Neuromorphic hardware deployment
- Surrogate gradient training
- Energy-efficient neural networks
- Critical brain hypothesis
- Iterative pruning strategies
- Zombie-weight problems

## Related Concepts

- Surrogate gradient learning for SNNs
- Magnitude pruning vs. criticality-based pruning
- Critical Brain Hypothesis
- Neuromorphic computing (Loihi, TrueNorth, SpiNNaker)
- Backpropagation-through-time (BPTT) for SNNs
- Energy-efficient deep learning
- Sparse neural networks
