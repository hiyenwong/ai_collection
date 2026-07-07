---
name: exponential-family-predictive-coding
description: "Extended predictive coding framework using exponential family distributions beyond Gaussian assumptions. Reveals biological neural network properties: nonlinearity, heterogeneity, biological plausibility. Maintains FEP-PC correspondence up to second cumulant. Derives biologically plausible local plasticity rules from EFD variational free energy. Use when: predictive coding, free energy principle, exponential family, variational inference, biological plausibility, local plasticity rules, neural heterogeneity, non-negative firing rates. arXiv: 2605.30882"
---

## Extended Predictive Coding with Exponential Family Distributions

**Paper**: Extended predictive coding framework as variational free-energy minimisation under exponential-family assumption  
**arXiv**: 2605.30882  
**Authors**: Asaki Kataoka, Kenji Doya  
**Category**: q-bio.NC  
**Published**: 2026-05-29

## Core Concept

The Free-Energy Principle (FEP) → Predictive Coding (PC) correspondence has traditionally been limited to **Gaussian assumptions** with Laplace approximation. This paper extends the framework to the **Exponential Family of Distributions (EFD)**, revealing biological properties previously missing:

### Missing Properties Captured by EFD Extension

1. **Nonlinearity** of input-output properties within neural networks
2. **Heterogeneity** — different neurons have different response characteristics
3. **Biological plausibility** — no negative firing rates (Gaussian PC allows negative rates)

### Key Result

The FEP-PC correspondence is maintained **up to the second cumulant** of the posterior distribution when EFD is assumed for both variational posterior and prior.

## Mathematical Framework

### Traditional Gaussian PC Limitation
- Assumes Gaussian posterior and prior
- Uses Laplace approximation (matches only first two moments)
- Results in linear, homogeneous networks with potentially negative firing rates

### EFD Extension
- Uses exponential family: p(x|θ) = h(x) exp(η(θ)·T(x) - A(θ))
- Natural parameters η(θ) and sufficient statistics T(x)
- Captures skewness, kurtosis, and other higher-order moments
- Maintains FEP-PC correspondence through second cumulant

## Reusable Patterns

### Pattern 1: Biologically Plausible Local Plasticity Rules
- The EFD-based PC model can be trained using **local plasticity rules**
- Derived from EFD variational free energy gradient: `Δw_ij ∝ E_q[∂log q/∂w_ij · (log p(x|z) + log p(z) - log q(z))]`
- Each synapse updates based on local info (pre-synaptic activity, post-synaptic prediction error)
- **Hebbian-like**: Δw ∝ pre × error — no global error signal required

### Pattern 2: Heterogeneous Network Design
- Different neurons can have different distributional assumptions
- This creates heterogeneous input-output properties within the same network
- More biologically realistic than homogeneous Gaussian networks

### Pattern 3: Nonlinear Predictive Coding Layers
- Replace standard linear PC layers with EFD-based nonlinear layers
- Use the natural parameter space for prediction error computation
- Sufficient statistics become the nonlinear activation functions

### Pattern 4: Cumulant-Based Approximation
- Track prediction errors through cumulants (mean, variance, skewness, kurtosis)
- Higher cumulants capture non-Gaussian structure in neural representations
- Truncate at second cumulant for computational efficiency while preserving key properties

## EFD Family Selection Guide

See **[references/efd-family-selection-guide.md](references/efd-family-selection-guide.md)** for complete comparison table, selection heuristics, and local plasticity derivation.

Quick reference:
| EFD Family | Best For |
|-----------|----------|
| Poisson | Spike counts |
| Gamma | Positive continuous (firing rates) |
| Beta | Proportions/bounded variables |
| Von Mises | Circular (orientation tuning) |

## Implementation Guidance

1. For neural network design: Use EFD activations instead of ReLU/sigmoid
2. For learning rules: Implement local prediction error minimization
3. For variational inference: Use EFD families (Gamma, Beta, Poisson) instead of Gaussian
4. For biological modeling: Map natural parameters to neural membrane potentials

## Pitfalls

- The EFD extension maintains FEP-PC correspondence only up to **second cumulant** — higher cumulants require additional terms
- Not all exponential families are equally suitable — choose based on the data type (count data → Poisson, proportions → Beta, positive continuous → Gamma)
- Local plasticity rules derived from EFD may require careful initialization to avoid divergence
- Local plasticity converges to **different solutions** than backpropagation — don't expect identical benchmark performance
- The Gaussian PC is NOT wrong — it is a special case of the EFD framework

## Connections to Existing Skills

- `predictive-coding-light`: Base PC framework — this extends beyond Gaussian assumption
- `feedback-hebbian-continual-learning`: Local learning rules — complementary to EFD local plasticity
- `free-energy-moe-routing`: Free energy principle applications — shared FEP foundation
- `predictive-coding-exponential-family-plasticity`: Sub-skill focused on implementation details of local plasticity rules

## Related Skills (Consolidation Note)

Multiple skills cover arXiv:2605.30882 — this is the **umbrella** skill:
- `exponential-family-predictive-coding` ← **this skill, umbrella**
- `extended-predictive-coding-exponential-family` — duplicate, should be consolidated into this
- `extended-predictive-coding-free-energy-exponential-family` — duplicate in neuroscience/
- `predictive-coding-exponential-family-plasticity` — focused sub-skill on local plasticity implementation
