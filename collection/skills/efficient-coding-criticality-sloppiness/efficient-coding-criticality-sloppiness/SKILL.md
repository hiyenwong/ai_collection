---
name: efficient-coding-criticality-sloppiness
category: neuroscience
tags:
  - efficient coding
  - critical brain hypothesis
  - Fisher information
  - sloppiness
  - neural dynamics
  - computational neuroscience
  - criticality
  - power law
trigger: efficient coding, critical brain hypothesis, Fisher information optimization, neural criticality, sloppiness
description: Efficient coding under resource constraints drives neural systems towards criticality and sloppiness — a unified theoretical framework linking Fisher information maximization to critical brain dynamics.
arxiv: "2605.22598"
authors: He Xiao, Xinyue Zhao, Weikang Wang
date: 2026-05-21
---

# Efficient Coding Under Constraint Drives Neural Systems Towards Criticality and Sloppiness

**arXiv:2605.22598** | He Xiao, Xinyue Zhao, Weikang Wang | Submitted 21 May 2026

## Overview

This paper establishes a theoretical framework linking **efficient coding** to **criticality** in neural populations. Using a Gaussian population coding model, the authors demonstrate that maximizing Fisher information under resource constraints naturally leads to the emergence of soft modes, diverging correlation lengths, and power-law response — hallmarks of criticality. The framework unifies statistical and dynamical criticality perspectives and provides a mechanistic explanation for sloppiness in neural systems.

## Core Results from Paper

### Learning Dynamics
- Fisher information saturates after ~200 iterations
- Largest eigenvalue of precision matrix A grows; others compress toward zero
- IPR of softest mode ∼ N⁻¹ (delocalized, global mode)
- Dropout + graph Laplacian regularization prevent mode localization in heterogeneous networks

### Unifying Two Forms of Criticality
- **λ_min → 0** simultaneously produces:
  1. Diverging correlation length ξ ∝ 1/√λ_min (statistical criticality)
  2. μ_max → 1⁻ in transfer matrix T = I − dt·A (dynamical criticality — critical slowing down, bifurcation precursor)
- This is a key theoretical unification within a single minimal model

### Power-Law Avalanches from Quench Response
- Quench: rapid fluctuation δA in the precision matrix A
- Response magnitude ‖dx‖ ∝ 1/λ_soft in sloppy directions
- Distribution P(‖dx‖) shows heavy-tailed power law
- Critical condition: soft mode must be delocalized (IPR ∼ 1/N)
- Shuffled matrices do NOT produce power laws

### Implications
- **Criticality as consequence, not cause**: Emerges from efficient coding under metabolic constraints
- **Sloppiness as robustness feature**: Information immune to noise in sloppy directions
- **Predictive coding mapping**: Whitening matrix W relates to predictive coding error neurons
- **Effective couplings**: Precision matrix A ≠ synaptic weights — dense effective interactions arise from sparse structural connectivity

### Gaussian Population Coding

Neural population activity x(s) encodes a stimulus s:
- **Tuning curves**: f(s) = mean firing rates conditioned on s
- **Covariance structure**: C = Cov[x(s)] (stimulus-conditioned noise covariance)
- **Precision matrix**: A = C⁻¹ (inverse covariance)

### Fisher Information

Fisher information for the population:
```math
J(s) = f'(s)ᵀ A f'(s)
```

Spectral decomposition:
```math
A = Σ λᵢ uᵢ uᵢᵀ,  f'(s) = Σ vᵢ uᵢ
```
```math
J(s) = Σ λᵢ vᵢ²
```

### Constrained Optimization

The learning rule maximizes Fisher information under resource constraints:

**Objective**: Maximize `J(s) = g(s)ᵀ A g(s)` subject to `Tr(A) ≤ constant` where A = C⁻¹ = WᵀW (Cholesky decomposition).

With an entropy penalty term `ln det(A)`, the Lagrangian becomes:
```math
L = gᵀWᵀW g + α ln det(WᵀW) - β Tr(WᵀW)
```

### Hebb-like Learning Rule

Gradient ascent on the Lagrangian yields:
```math
ΔW ∝ η(ggᵀ)W + αηW⁻ᵀ - βηW
```
This maps onto a **predictive coding architecture** with error neurons and state neurons.

## Criticality Mechanisms

### Statistical Criticality

As Fisher information optimization proceeds:
- The smallest eigenvalue λ_min → 0 (soft mode emerges)
- Correlation length ξ ∝ 1/√λ_min diverges
- Power spectrum shows 1/f-like scaling near criticality

### Dynamical Criticality

Using gradient descent dynamics ẋ = -Ax + ξ(t):
- Largest eigenvalue of the dynamical system: μ_max = 1 - dt·λ_min
- As λ_min → 0, μ_max → 1⁻ (marginal stability)
- This is the precursor to a dynamical bifurcation
- Critical slowing down appears: recovery time τ ∝ 1/λ_min diverges

### Power-Law Avalanches

The **quench response** ‖dx‖ after a small perturbation:
- Near criticality, ‖dx‖ ∝ 1/λ_soft (large response in soft directions)
- Distribution P(‖dx‖) shows heavy tails / power-law scaling
- Shuffled covariance matrices do NOT produce power laws (validating the mechanism)

## Sloppiness

After optimization, the eigenvalue spectrum becomes **extremely anisotropic**:
- **Few stiff directions**: large λ, high Fisher information
- **Many sloppy directions**: λ ≈ 0, near-zero Fisher information

This explains neural **sloppiness**:
1. **Efficient encoding**: Only stimulus-relevant dimensions consume resources
2. **Biological robustness**: Information immune to perturbations in sloppy directions
3. **Flat energy landscape**: Facilitates generalization and degenerate solutions
4. **Parameter insensitivity**: Many parameter combinations produce equivalent coding performance

## Simulation Results

- **Convergence**: Fisher information saturates after ~200 iterations
- **Eigenvalue evolution**: Largest eigenvalue grows; others compress toward zero
- **Spatial structure**: With graph Laplacian regularization + dropout, soft modes become delocalized (IPR ∼ 1/N), corresponding to global critical fluctuations
- **Power-law verification**: Quench response follows power-law distribution for optimized matrices; shuffled matrices do not

## Key Predictions

1. **Criticality emerges from coding efficiency constraints** — not as an independent principle
2. **Sloppiness is a natural consequence** of resource-limited Fisher information optimization
3. **Statistical and dynamical criticality are unified** through the same eigenvalue mechanism
4. **Power-law avalanches** arise as a byproduct of soft-mode responses to perturbations
5. **Delocalized critical modes** require spatial coupling structure (graph Laplacian)

## Relationship to Other Theories

| Theory | Connection |
|--------|-----------|
| **Critical Brain Hypothesis** | Provides the *why*: criticality emerges from efficiency constraints |
| **Efficient Coding Theory** | Provides the *mechanism*: Fisher info maximization drives it |
| **Sloppy Models** | Explains *why*: few stiff, many sloppy parameter directions |
| **Predictive Coding** | Learning rule maps onto predictive coding architecture |
| **Hebbian Learning** | ΔW ∝ η(ggᵀ)W is a Hebb-like term |

## Activation Keywords

efficient coding, critical brain hypothesis, Fisher information, sloppiness, criticality, power-law avalanches, neural dynamics, computational neuroscience, population coding, Hebbian learning, predictive coding, soft modes, correlation length, bifurcation, critical slowing down

## Related Skills

- `brain-criticality-hypothesis-assessment` — Assessment framework for the critical brain hypothesis
- `griffiths-phase-brain-criticality` — Griffiths phase framework for brain criticality
- `neural-critical-dynamics-theory` — Theory of critical dynamics and information processing in neural systems
- `self-organized-criticality-brain-body-resonance` — Self-organized criticality for conscious integration
- `hierarchical-brain-criticality` — Hierarchical organization of critical brain dynamics
