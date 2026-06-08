---
name: gaussian-exponential-zero-noise-extrapolation
description: "Hybrid Gaussian-exponential zero-noise extrapolation methodology for periodic quantum circuits — combines Gaussian and exponential error models for more accurate expectation value estimation in NISQ-era quantum computing."
category: quantum
---

# Hybrid Gaussian-Exponential Zero-Noise Extrapolation

## Context

Based on arXiv:2605.29242 (Jun 2026). Proposes a hybrid Gaussian-exponential model for zero-noise extrapolation (ZNE) specifically designed for periodic quantum circuits, improving over standard exponential or polynomial extrapolation.

## Core Methodology

1. **Error model analysis**: Characterize error behavior in periodic quantum circuits — errors exhibit both Gaussian-like (short-depth) and exponential-like (long-depth) components
2. **Hybrid model construction**: Fit expectation values using a combined Gaussian-exponential model: f(λ) = A·exp(-αλ²) + B·exp(-βλ) + C, where λ is the noise scaling factor
3. **Zero-noise extrapolation**: Evaluate f(0) = A + B + C to estimate the noiseless expectation value
4. **Periodic circuit advantage**: The hybrid model captures the oscillatory behavior of errors in periodic circuits better than pure exponential or polynomial models
5. **Parameter estimation**: Use least-squares fitting on noisy expectation values at multiple noise scales

## Implementation Steps

1. Prepare the target quantum circuit
2. Apply noise amplification at multiple scale factors λ₁, λ₂, ..., λₙ (e.g., via gate folding or identity insertion)
3. Measure expectation values E(λᵢ) at each noise scale
4. Fit the hybrid Gaussian-exponential model to the data points
5. Extrapolate to λ = 0 to obtain the zero-noise estimate
6. Validate against known benchmarks or exact simulations

## Key Results

- Hybrid model captures both Gaussian and exponential error components in periodic circuits
- More accurate than standard exponential ZNE for circuits with oscillatory error behavior
- Maintains polynomial sample complexity
- Applicable to parameterized quantum circuits and variational algorithms

## Pitfalls

- Requires fitting more parameters than standard exponential ZNE — needs more data points
- Model may overfit if too few noise scales are used; use at least 5-7 scale factors
- Not suitable for circuits with purely exponential or purely polynomial error behavior
- Noise amplification must be accurate — gate folding errors propagate into the fit

## Verification

- Compare hybrid model fit quality (R²) against pure exponential and polynomial models
- Validate on circuits with known exact solutions
- Test robustness: vary number of shots and noise scales to assess convergence
- Verify that the extrapolated value improves circuit fidelity metrics

## Activation

- zero noise extrapolation, ZNE, gaussian exponential model, periodic circuits, error mitigation, NISQ
- 零噪声外推, 高斯指数模型, 周期量子线路, 误差缓解
