---
name: gradient-free-riemannian-langevin-sampler
description: 'We address the problem of efficiently sampling multimodal probability distributions, where standard Markov Chain Monte Carlo methods often suffer from poor mixing and mode trapping. To mitigate these. Based on arXiv:2607.07519.'
---

# Gradient-free Riemannian Langevin Sampler

**arXiv**: 2607.07519 | **Authors**: Ricardo Baptista, Olivier Zahm | **Utility**: 0.85

## Overview

We address the problem of efficiently sampling multimodal probability distributions, where standard Markov Chain Monte Carlo methods often suffer from poor mixing and mode trapping. To mitigate these issues, we propose Gradient-free Riemannian Langevin Sampler (GRiLS), a novel proposal that improves exploration without requiring gradient evaluations of the target density. Our approach introduces a Riemannian metric which reshapes the local geometry in order to facilitate transitions across modes. The resulting gradient-free MCMC algorithm is particularly suitable for complex, computationally expensive targets where derivatives are unavailable or impractical. The GRiLS proposal requires knowing the mean and covariance of the target density, which we estimate using an ensemble of interacting particles. Empirical results on multimodal benchmarks demonstrate that GRiLS achieves improved mixing compared to existing gradient-based and gradient-free MCMC approaches.

## Key Contributions

1. We address the problem of efficiently sampling multimodal probability distributions, where standard Markov Chain Monte Carlo methods often suffer from poor mixing and mode trapping.
2. To mitigate these issues, we propose Gradient-free Riemannian Langevin Sampler (GRiLS), a novel proposal that improves exploration without requiring gradient evaluations of the target density.
3. Our approach introduces a Riemannian metric which reshapes the local geometry in order to facilitate transitions across modes.
4. The resulting gradient-free MCMC algorithm is particularly suitable for complex, computationally expensive targets where derivatives are unavailable or impractical.

## Implementation Notes

- **Keywords**: langevin-dynamics
- **Categories**: cs.LG, math.ST
- **Published**: 2026-07-08

## Activation Criteria

Use this skill when working on tasks involving: langevin-dynamics.
