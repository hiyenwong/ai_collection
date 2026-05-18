---
name: wavelet-variance-equipartition-quantum
description: >
  Wavelet variance equipartition (scaling exponent alpha) methodology for assessing
  world-model latent quality and quantum kernel tensor-network simulability.
  Use when: evaluating representation quality of learned latents, determining
  classical simulability of quantum kernels, or analyzing structure in feature spaces.
  Trigger words: wavelet variance, equipartition, scaling exponent, quantum kernel
  simulability, tensor network bond dimension, 小波方差
---

# Wavelet Variance Equipartition for Representation Quality

Physics-grounded diagnostic for assessing structural fidelity of
learned latent spaces using wavelet scaling exponent analysis.

## Core Theory

### Wavelet Scaling Exponent (alpha)
- Optimal representations satisfy variance equipartition: alpha ≈ 1/2
- This mirrors Kolmogorov's inertial range in turbulence

### Sharp Transition Boundary at alpha = 1/2

- **alpha > 1/2**: Area-law phase → efficient classical emulation
  - Matrix Product State (MPS) bond dimension chi grows polynomially
  
- **alpha < 1/2**: Volume-law phase → exponential simulation hardness
  - MPS bond dimension chi grows exponentially with qubit count n

### Application to World Models
- Spatial tokens: alpha ≈ 0.423 (near equipartition)
- Permutation-invariant feature channels: alpha ≈ -0.123 (unstructured disorder)
- Real-world latents fall deep into volume-law phase

### Shot Noise Wall
- Variance of scrambled transition probability: Var[X] = Theta(d^-2)
- Measurement budget required: M = Omega(d^2)
- This constrains quantum ML scalability

## Computation Steps

1. Compute wavelet transform of latent representation
2. Estimate scaling exponent alpha from variance decay
3. Classify: area-law (alpha > 1/2) vs volume-law (alpha < 1/2)
4. For quantum kernels: determine classical simulability boundary
5. For world models: assess structural fidelity of latents

## When to Use

- Evaluating quality of learned representations
- Determining if quantum advantage is achievable
- Analyzing structure in feature/token spaces
- Setting benchmarks for world model training

## Key Results

- alpha = 1/2 is sharp boundary for classical simulability
- VideoMAE latents show dichotomy: spatial ~0.423, channels ~-0.123
- Weingarten calculus gives exact variance: Var[X] = Theta(d^-2)
- Confirmed numerically: log-log slope = -1.881 (R² = 0.999)

## References

- arXiv: 2605.11557
- Authors: Chon-Fai Kam, Xavier Cadet, Miloud Bessafi, Frederic Cadet
