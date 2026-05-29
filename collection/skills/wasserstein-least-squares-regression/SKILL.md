---
name: wasserstein-least-squares-regression
description: Wasserstein least squares regression methodology for distribution-valued responses. Combines optimal transport theory with statistical regression for probability distribution-valued data. Based on arXiv:2605.30266 (May 2026).
tags: [statistics, optimal-transport, wasserstein, regression, probability]
---

# Wasserstein Least Squares Regression

**Source**: Martínez León & Niles-Weed, "Wasserstein Least Squares: A Canonical Regression Method for Probability Distributions", arXiv:2605.30266 (May 2026)

## Overview

Wasserstein least squares (WLS) is a regression method for vector-valued covariates and distribution-valued responses. Unlike other distributional regression methods, WLS has a direct interpretation in terms of random variables as a nonparametric analogue of the classic random-effects model.

## Core Theory

### Mathematical Foundation

WLS is the **canonical extension of Euclidean least squares** to the space of probability distributions from the perspective of convex analysis (using Lavenant 2024's strategy). This viewpoint yields:

1. **Multimarginal formulation**: Extends the theory of Wasserstein barycenters to regression
2. **Dual formulation**: Convex dual provides computational tractability
3. **Template deformation model**: Under this model, estimation achieves n^{-1/2} rate

### Key Results

- **Estimation rate**: Surprisingly, n^{-1/2} rate is achievable under template deformation model
- **Wasserstein barycenters**: Special case yields exponential improvement over previous rates (Ahidar-Coutrix et al., 2020)
- **Particle method**: Heuristic particle-based algorithm for practical computation

## Implementation Patterns

### Pattern 1: Distributional Regression Setup

When your response variable is a probability distribution (not a scalar), use WLS instead of:
- Standard least squares (ignores distributional structure)
- Quantile regression (only captures conditional quantiles, not full distribution)
- Functional data analysis (assumes smooth functions, not distributions)

### Pattern 2: Template Deformation Model

```
Response distribution = Deformed template + noise
Y_i = (Id + ε·ξ_i)# μ₀
```

where μ₀ is the template distribution and ξ_i are random deformation fields.

### Pattern 3: Multimarginal Formulation

The WLS problem can be cast as finding the multimarginal transport plan that minimizes:
```
min_π ∑ᵢ ∫ |xᵢ - ⟨x, β⟩|² dπ(x₁,...,xₙ)
```

### Pattern 4: Dual Problem

The dual formulation provides:
- Convex optimization structure
- Connection to optimal transport dual potentials
- Computational advantages for large-scale problems

## Applications

1. **Demographic analysis**: Population distribution modeling (validated on RAND Health and Retirement Study)
2. **Bayesian posterior regression**: When posterior distributions are responses
3. **Distributional uncertainty quantification**: Propagating input uncertainty through regression
4. **Wasserstein barycenter computation**: As a special case with improved rates

## Connection to Quantum/Other Domains

- **Quantum state regression**: WLS framework extends to quantum states (density matrices) via quantum Wasserstein distance
- **Optimal transport in ML**: WLS connects to distributionally robust optimization (DRO)
- **Statistics-geometry bridge**: Combines statistical inference with Riemannian geometry of Wasserstein space

## Activation Triggers

Use this skill when:
- Response variables are probability distributions or histograms
- Need to regress on distributional data (not just point estimates)
- Working with Wasserstein distances or optimal transport
- Building distributional regression models
- Computing Wasserstein barycenters with improved rates
- Analyzing demographic or population distribution changes

## Keywords
wasserstein, least-squares, optimal-transport, distributional-regression, probability-distributions, template-deformation, barycenter, convex-analysis, multimarginal-transport