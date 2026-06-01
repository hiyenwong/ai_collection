---
name: predictive-coding-exponential-family
description: "Extended predictive coding framework using exponential-family distributions. Generalizes standard predictive coding (Gaussian assumption) to arbitrary exponential-family distributions via natural parameters and sufficient statistics. Use when: (1) Modeling non-Gaussian neural or sensory data, (2) Deriving predictive coding rules for Poisson, Gamma, or Dirichlet observations, (3) Extending predictive processing theories beyond Gaussian noise, (4) Building brain-inspired models with diverse observation likelihoods."
license: Complete terms in LICENSE.txt
metadata:
  arxiv_id: "2605.30882"
  published: "2026-05-30"
  tags: [predictive-coding, exponential-family, neuroscience, brain-inspired, bayesian-inference]
---

# Extended Predictive Coding via Exponential Family

## Overview

Standard predictive coding assumes Gaussian observation noise, which limits
applicability to neural systems with spike-counts (Poisson), reaction times
(Gamma), or probability distributions (Dirichlet). This framework generalizes
predictive coding to the full exponential family, enabling predictive processing
models for arbitrary data types.

## Core Concepts

### Exponential Family Form

Any distribution in the exponential family can be written as:

```
p(x|θ) = h(x) exp(η(θ)·T(x) - A(θ))
```

where η(θ) are natural parameters, T(x) are sufficient statistics, and A(θ)
is the log-partition function.

### Extended Predictive Coding Rule

The generalized prediction error is:

```
ε = T(x) - E[T(x)|η]  # prediction error in sufficient statistics
∇L = ∂A/∂η - T(x)     # gradient of negative log-likelihood
```

Update rules:
- **Perceptual inference**: η ← η - α · (∂A/∂η - T(x))
- **Learning**: θ ← θ - β · ε · ∂η/∂θ

### Key Distribution-Specific Forms

| Distribution | Sufficient Statistics T(x) | Prediction Error ε |
|-------------|---------------------------|-------------------|
| Gaussian | x, x² | x - μ |
| Poisson (spike counts) | x | x - exp(η) |
| Gamma (reaction times) | log(x), x | log(x) - ψ(α) + log(β), x - α/β |
| Dirichlet (proportions) | log(x₁), ..., log(xₖ) | log(xᵢ) - ψ(αᵢ) + ψ(Σα) |
| Bernoulli (binary) | x | x - σ(η) |

## Methodology

### Step 1: Identify Observation Distribution
Determine the appropriate exponential-family distribution for your data:
- Neural spike counts → Poisson
- Interspike intervals → Gamma/Inverse-Gaussian
- Population coding proportions → Dirichlet
- Binary decisions → Bernoulli

### Step 2: Derive Prediction Error
Compute ε = T(x) - E[T(x)|η] using the distribution's sufficient statistics.
This replaces the simple (x - μ) error in standard predictive coding.

### Step 3: Compute Parameter Updates
Use ∇_η log p = E[T] - T(x) for perception updates.
Use chain rule through η(θ) for learning updates.

### Step 4: Hierarchical Extension
For hierarchical models, propagate prediction errors upward:
```
ε_l = T(x_l) - E[T(x_l)|η_l]
η_{l-1} ← η_{l-1} + W^T · ε_l  # top-down prediction
η_l ← η_l + ε_{l-1} - W · ε_{l+1}  # bottom-up error
```

## Pitfalls

- **Log-partition computation**: A(θ) may not have closed form for complex exponential families. Use numerical approximation (Monte Carlo, Laplace) when needed.
- **Numerical stability**: Natural parameters can grow large; use log-space computations and clipping to avoid overflow in exp(η).
- **Non-conjugate priors**: The framework assumes conjugate structure for tractability. With non-conjugate priors, use variational approximation.
- **Gaussian is not always baseline**: When data is clearly non-Gaussian (e.g., sparse spike counts), starting with Gaussian predictive coding and then switching is wasteful — use the appropriate exponential family from the start.

## Activation Keywords
- predictive coding exponential family
- extended predictive coding
- non-gaussian predictive coding
- predictive processing beyond gaussian
- exponential family prediction error
