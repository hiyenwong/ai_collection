# ILOD Reference — Iterative Low-Order Decoding for QEC

## Summary
ILOD (Iterative Low-Order Decoding) maps QEC syndrome decoding to classical Ising Hamiltonian ground-state optimization. Instead of solving the full joint Hamiltonian with 8-10 body interactions, it alternates X/Z sub-Hamiltonians with Bayesian priors.

## Key Numbers
| Metric | Value |
|--------|-------|
| Toric code threshold | 4.73% (vs 4.83% joint) |
| Runtime scaling | (0.81)^d vs joint |
| Spin reduction | 2.5x for 2-body embedding |
| Color code convergence | Works at distances where joint fails |

## Mathematical Framework
- **Joint Hamiltonian**: H_joint = H_X + H_Z + H_XZ (cross-correlations)
  - Toric code: max 8-body terms
  - Color code: max 10-body terms
- **ILOD sub-Hamiltonians**:
  - H_X^(k) = H_X + λ * P_Z^(k-1)
  - H_Z^(k) = H_Z + λ * P_X^(k)
  - λ = Bayesian coupling strength (controls prior influence)

## Iteration Algorithm
```
P_X = P_Z = uniform
repeat:
  error_X = argmin H_X(error_X | P_Z)
  P_X = Bayesian_update(error_X)
  error_Z = argmin H_Z(error_Z | P_X)
  P_Z = Bayesian_update(error_Z)
until |error - prev_error| < threshold
```

## Hardware Relevance
- Reduces spin overhead for 2-body Ising hardware embedding (D-Wave, etc.)
- Particularly valuable for color codes where joint formulation doesn't converge at large distances
- Bayesian coupling λ is a tunable hyperparameter

## Source
arXiv:2606.12301 — "An iterative Ising decoder for quantum error correction codes"
Liu, Zeng, Li, Liu, Huang, Liu, Wang, Wu, Lao (2026-06-10)
