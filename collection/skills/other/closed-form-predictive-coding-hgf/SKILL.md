---
name: closed-form-predictive-coding-hgf
description: >-
  Closed-form predictive coding via hierarchical Gaussian filters (HGF) methodology from arXiv:2605.20293.
  Restores precision-weighted prediction errors to predictive coding networks by expressing them as
  deep hierarchical Gaussian filters. Enables biologically plausible, local learning without
  backpropagation, with dynamic uncertainty estimates and Hebbian-compatible update rules.
  Activation: predictive coding, hierarchical Gaussian filter, free energy principle, precision-weighted
  prediction error, biologically plausible learning, HGF, predictive coding network.
---

# Closed-Form Predictive Coding via Hierarchical Gaussian Filters

Methodology from arXiv:2605.20293 (May 2026). Authors: Aleksandrs Baskakovs, Sylvain Estebe, Kenneth Enevoldsen, Kristoffer Nielbo, Chris Mathys, Nicolas Legrand.

## Overview

Predictive coding (PC) offers a local and biologically grounded alternative to backpropagation in training artificial neural networks. However, current PC networks suffer from two key problems: they are slower than backpropagation, and performance degrades sharply as network depth increases.

This paper traces both problems to a single simplification: current PC networks fix the precision matrix to the identity, discarding precision-weighted prediction errors that the variational derivation requires. The authors close this gap by expressing predictive coding networks as deep hierarchical Gaussian filters (HGFs) and restore precision-weighted message passing.

**Key insight**: The HGF framework provides closed-form variational updates for all parameters — activations, weights, and precisions — under a single free-energy objective, requiring no global error signal, no iterative relaxation, and no automatic differentiation.

## Core Methodology

### 1. Precision-Weighted Predictive Coding

Traditional predictive coding networks use fixed identity precision matrices, which loses the precision-weighting that makes PC theoretically grounded. This paper restores precision-weighting by expressing PC networks as hierarchical Gaussian filters.

### 2. Hierarchical Gaussian Filter (HGF) Framework

The HGF provides:
- **Dynamic uncertainty estimates** at every layer
- **Hebbian-compatible update rules** derived from closed-form variational inference
- **Simultaneous learning** of activations, weights, and precisions under a single free-energy objective
- **No global error signal** — all updates are local
- **No iterative relaxation** — inference resolves in closed form
- **No automatic differentiation** — all updates are analytic

### 3. Free-Energy Objective

The entire network optimizes a single free-energy objective:
- Prediction errors at each layer are precision-weighted (precision = inverse variance)
- Precision parameters are learned online alongside weights and activations
- This provides natural uncertainty quantification

## Key Results

- **FashionMNIST**: Approaches backpropagation in epoch-level wall-clock cost while converging in fewer epochs
- **Online learning**: Outperforms backpropagation on online (streaming) tasks
- **Data efficiency**: Better performance with fewer training samples
- **Concept drift**: Superior adaptation to changing data distributions
- **Depth scaling**: Maintains performance as network depth increases (unlike previous PC networks)

## Practical Implications

### For Computational Neuroscience

- Provides a biologically plausible learning algorithm that rivals backpropagation
- Precision-weighting connects predictive coding to attention and uncertainty estimation in the brain
- Local Hebbian-like updates align with observed synaptic plasticity mechanisms
- Offers a testable framework for how cortical microcircuits implement precision-weighted prediction errors

### For AI/ML

- A practical alternative to backpropagation for biologically inspired AI
- Natural uncertainty estimation built into the learning process
- Superior performance in streaming/online learning scenarios
- Better handling of non-stationary data distributions

## When to Use This Skill

- When implementing predictive coding networks for biologically plausible learning
- When studying free-energy principle applications in neural networks
- When building models that require online learning or uncertainty estimation
- When comparing biologically motivated learning rules to backpropagation
- When working with hierarchical Gaussian filters for neural computation

## Key Concepts

| Concept | Description |
|---------|-------------|
| Predictive Coding (PC) | Neural network training via local prediction errors instead of global backpropagation |
| Precision Matrix | Inverse covariance matrix; weights prediction errors by their uncertainty |
| Hierarchical Gaussian Filter (HGF) | Multi-level Bayesian filtering framework with precision-weighted message passing |
| Free-Energy Objective | Single variational objective optimizing all parameters simultaneously |
| Hebbian-Compatible | Learning rules that involve local, pre/post-synaptic activity correlations |
| Precision-Weighted Prediction Error | Prediction error scaled by its estimated precision (inverse variance) |

## References

- **Paper**: [arXiv:2605.20293](https://arxiv.org/abs/2605.20293)
- **Categories**: cs.LG, cs.AI, cs.NE
- **Submitted**: 19 May 2026
