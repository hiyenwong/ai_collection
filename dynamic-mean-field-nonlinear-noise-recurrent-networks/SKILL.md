---
name: dynamic-mean-field-nonlinear-noise-recurrent-networks
version: 1.0.0
category: ai_collection
tags: [mean-field-theory, recurrent-networks, nonlinear-noise, Ornstein-Uhlenbeck, neural-dynamics, bifurcation]
activation_keywords: [mean field, dynamic mean field, recurrent network, nonlinear noise, OU process, lognormal closure, bifurcation]
created: 2026-04-24
source: arXiv:2601.15462
---

# Dynamic Mean Field Theories for Nonlinear Noise in Recurrent Neuronal Networks

## Overview
Novel dynamical mean-field theory (DMFT) method for recurrent neuronal networks with strong, correlated noise passing through nonlinear transfer functions. Replaces nonlinear functions of Ornstein-Uhlenbeck (OU) noise with Gaussian-equivalent processes matched in mean and covariance.

## Core Innovation
- **Gaussian-Equivalent Process**: Replace f(OU_noise) with a Gaussian process matched in mean and covariance
- **Lognormal Moment Closure**: For expansive nonlinearities, derive closed dynamical mean-field equations
- Captures order-one transients, fixed points, and noise-induced transitions

## Technical Framework

### Problem Setup
1. Recurrent neuronal network with N neurons
2. Strong correlated noise (from recurrent connectivity)
3. Noise passes through nonlinear transfer function phi(x)
4. Standard DMFT fails when phi() is nonlinear and noise is strong

### Solution: Gaussian-Equivalent DMFT
1. Model input noise as Ornstein-Uhlenbeck process: dx = -x/tau * dt + sigma * dW
2. Replace phi(x_OU) with Gaussian equivalent x_eq ~ N(mu_eq, sigma_eq^2)
3. Match moments: mu_eq = E[phi(x_OU)], sigma_eq^2 = Var[phi(x_OU)]
4. For expansive phi: use lognormal moment closure for stability

### Key Equations
- Mean field: dm/dt = -m/tau + J * phi_mean(m, sigma)
- Variance field: d sigma^2/dt = -2*sigma^2/tau + sigma_ext^2 + J^2 * C(phi)
- Closed system using lognormal closure for C(phi)

## Key Results
- Accurately predicts transient dynamics of recurrent networks
- Captures bifurcation structure under varying noise levels
- Computationally efficient (vs. large-scale simulation)
- Applicable to networks with arbitrary transfer functions

## Applications
- Analyzing dynamics of cortical circuits with strong recurrent feedback
- Predicting bifurcations in neural population models
- Understanding noise-induced state transitions in brain networks
- Rapid prototyping of network models before simulation

## Authors
Shoshana Chipman, Brent Doiron

## References
- arXiv:2601.15462 (2026-01-21)
