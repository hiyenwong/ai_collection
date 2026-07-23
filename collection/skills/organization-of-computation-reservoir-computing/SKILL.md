---
name: organization-of-computation-reservoir-computing
description: Eigenspectral decomposition framework for analyzing how information processing capacity (IPC) is distributed across reservoir state-space modes, with degree-wise representation energy and noise-aware capacity metrics for physical reservoir computers.
source: "arXiv:2607.17858 - Organization of computation in reservoir computing (Mohab Abdalla, Damien Rontani, 2026)"
---

# Organization of Computation in Reservoir Computing

Analyze and quantify how task-relevant information is geometrically organized across the modes of a reservoir computer, moving beyond aggregate memory–nonlinearity tradeoffs.

## When to use

- Designing or benchmarking physical reservoir computers (photonic, electronic, spintronic, etc.) where experimental noise can mask low-energy modes.
- Diagnosing why a reservoir with high total IPC performs poorly on a specific task.
- Optimizing reservoir hyperparameters (spectral radius ρ, input scaling ι, bias β, sparsity κ) for a target degree of nonlinearity.
- Comparing software ESNs vs. physical reservoirs in terms of accessible, rather than theoretical, capacity.
- Trigger words: reservoir computing, echo state network, information processing capacity, IPC, representation energy, mode-task projection, eigenspectral decomposition, physical reservoir computing.

## Core methodology

1. **Build the reservoir state matrix** X ∈ ℝ^(N×T) from N reservoir nodes over T timesteps.
2. **Compute SVD**: X = Q Σ V^T. Left singular vectors Q form an orthonormal node-space basis; singular values σ_i quantify mode variance/energy.
3. **Project states onto modes**: x̃_i = q_i^T X.
4. **Define IPC targets** z_k as products of Legendre polynomials of delayed inputs (degree d, delay m).
5. **Compute mode–task score** s_{i,k} = (x̃_i · z_k)^2 / (||x̃_i||^2 ||z_k||^2) — the squared cosine similarity between mode i and target k.
6. **Compute mode usage** S_i = Σ_k s_{i,k} ≤ 1 (Bessel inequality bound).
7. **Degree-resolved mode usage**: S_{i,d} = Σ_{k ∈ Z_d(ε)} s_{i,k}.
8. **Representation energy** per degree: Φ_d = Σ_i η_i S_{i,d}, where η_i = σ_i^2 / Σ_j σ_j^2 is the energy fraction of mode i.
9. **Noise-aware capacity**: C̄_d^γ = C̄_d · Φ_d / (Φ_d + Φ_noise), giving the fraction of degree-d capacity recoverable in the presence of noise floor Φ_noise.

## Key findings

- Higher spectral radius ρ increases effective dimensionality (flatter energy fraction distribution).
- Higher input scaling ι affects mainly tail (low-energy) modes.
- Linear memory (degree d=1) tends to occupy high-energy modes; higher-order nonlinearities tend to occupy low-energy, smaller-variance modes.
- Total IPC can be misleading: a reservoir may have large theoretical nonlinear capacity but tiny representation energy Φ_d for that degree, making it fragile under noise.
- Effective physical reservoir design should maximize task-relevant features on accessible (high-energy, high-SNR) modes, not just maximize total IPC.

## Practical workflow

### Step 1 — Generate reservoir data

Use an ESN or physical reservoir with fixed recurrent/input weights. Record states X for a white-noise input u(t) ~ U(-1, 1).

### Step 2 — Compute SVD and energy fractions

```python
import numpy as np
U, s, Vt = np.linalg.svd(X, full_matrices=False)
Q = U                          # node-space modes
eta = s**2 / np.sum(s**2)      # energy fraction per mode
```

### Step 3 — Build IPC targets

Construct Legendre polynomial products over delayed inputs:

```python
from numpy.polynomial.legendre import legval
# For each target degree combination {d_m} and delay m
z_k = np.prod([legval(u[t-m], [0]*d + [1]) for m, d in ...])
```

### Step 4 — Compute mode-task scores and mode usage

```python
X_tilde = Q.T @ X                          # mode-projected states
s_ik = (X_tilde @ z_k)**2 / (np.sum(X_tilde**2, axis=1) * np.sum(z_k**2))
S_i = s_ik.sum()                           # per-mode usage
S_i_d = s_ik[mask_degree_d].sum()          # per-mode per-degree usage
```

### Step 5 — Compute degree-wise representation energy

```python
Phi_d = np.sum(eta * S_i_d)                # normalized representation energy
```

### Step 6 — Noise-aware capacity (optional)

Estimate Φ_noise from the noise covariance in the state matrix, then compute C̄_d^γ.

## Interpretation guide

| Observation | Interpretation |
|-------------|----------------|
| Φ_d ≈ C̄_d | Theoretical capacity is physically accessible. |
| Φ_d << C̄_d | Most of the theoretical degree-d capacity is in low-energy modes; likely degraded by noise. |
| Linear (d=1) dominates high-energy modes | Reservoir behaves as a fading-memory system; good for short-term memory tasks. |
| Nonlinear degrees clustered in low-energy modes | Need higher SNR or redesign to make nonlinear features experimentally accessible. |
| Increasing ρ spreads energy across modes | More dimensions are used, but also more noise-sensitive. |

## Limitations and extensions

- The framework is demonstrated with standard ESNs; extension to delay-embedded reservoirs, deep reservoirs, and physical reservoirs requires careful definition of state matrix X.
- Orthogonality of IPC targets is approximate for finite T; results improve with longer input sequences.
- Noise model is additive white noise on reservoir states; colored or readout noise requires adapted Φ_noise estimation.
- Future work: link task-specific performance (not just IPC) to mode organization; apply to experimental data.

## References

- Dambre et al. (2012). *Information processing capacity of dynamical systems*. Scientific Reports 2, 514.
- Abdalla & Rontani (2026). *Organization of computation in reservoir computing*. arXiv:2607.17858 [cs.NE].
