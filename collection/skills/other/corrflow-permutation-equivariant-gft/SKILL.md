---
name: corrflow-permutation-equivariant-gft
description: Equivariant flow matching on the correlation elliptope.
trigger: correlation matrix generation, permutation equivariance, elliptope sampling, correlation stress testing, generative models for covariance structure, GFT parametrization
category: ai_collection
---

# CorrFlow: Permutation-Equivariant Flow Matching on the Correlation Elliptope

**Source**: Marti, G. (ADIA), "CorrFlow: Exact and Permutation-Equivariant Flow Matching on the Correlation Elliptope", arXiv:2610.13606 (Oct 2026, PMLR/SymNGR 2026).

## Core Problem
Generating correlation matrices faces TWO distinct problems that financial image generators (CorrGAN/cCorrGAN, image DDPM) mix together:
1. **Validity**: every output must lie in the elliptope E_n+ (symmetric, positive definite, unit diagonal) — regardless of variable ordering
2. **Domain distribution**: the generator must learn where empirical data sits INSIDE that valid space

Image-based methods learn ordered matrix entries (after Ward clustering imposes a canonical order) and repair invalid draws afterward (Higham nearest-correlation projection). Repair is not cosmetic: post-repair RMS change is ~.018 per off-diagonal entry, and repaired image outputs remain perfectly separable from real data (classifier AUC 1.000).

## Component 1: Generalized Fisher Transform (GFT) — exact validity by construction

Archakov–Hansen (Econometrica 2021) parametrization:

```
γ(C) = vecl(log C) ∈ R^(n(n-1)/2)
```

- **Bijection** E_n+ → R^(n(n-1)/2): every FULL-RANK correlation matrix maps to an unconstrained vector, and every finite vector maps back to exactly one valid C. No clipping, no projection, no repair.
- Inverse: recover the missing diagonal of log C by **fixed-point iteration** `d_i ← d_i − log(C_ii)`, C = exp_m(G + diag(d)), until diag(C) = 1. Numerically: 8–390 iterations for well-conditioned to near-singular targets (verified to 1e-13).
- Matrix form Γ(C): the symmetric hollow (zero-diagonal) matrix holding the same coordinates. This is the permutation-covariant representation:

```
Γ(P C P^T) = P Γ(C) P^T   (exact, machine precision)
```

Unlike normalized-Cholesky coordinates (DiffeoCFM), GFT introduces NO privileged ordering.
- n=2 degenerate case recovers the classical Fisher z-transform: Γ_12 = atanh(ρ) exactly (verification anchor).

## Component 2: Permutation-Equivariant Graph Flow

Represent each off-diagonal entry as an EDGE of a complete graph:
- Node update: mean + second moment of incident edge states, graph-wide edge mean, context embedding of (t, y)
- Edge update: shared MLP on [edge state, h_i + h_j, h_i h_j, |h_i − h_j|, context]
- Mean aggregation normalizes by degree → scale does not grow with dimension; same weights evaluable at different n (no cross-size guarantee claimed)

**Equivariance chain** (Proposition 1): Γ-coordinate covariance (eq 2) + shared-scalar standardization S (per-edge (x−μ)/σ commutes with conjugation) + equivariant vector field

```
v_θ(P X P^T, t, y) = P v_θ(X, t, y) P^T
```

+ ODE uniqueness ⇒ flow map F_θ(P X0 P^T, y) = P F_θ(X0, y) P^T. Reordering variables only reorders the output — the model cannot learn a privileged asset order.

Training: rectified-flow objective on straight interpolation X_t = (1−t)X0 + tX1, X0 = hollow symmetric Gaussian noise, X1 = standardized Γ(C). Generation: 25 Heun steps (50 NFE), then S^-1 + inverse GFT. Conditioning y = (regime indicator, standardized performance score) is permutation-invariant.

## Empirical Result (Taiwan 80×80, 24,408 matrices, 5 seeds)

| Method | Valid before repair | F-SWD ↓ | Classifier AUC (real vs gen) |
|---|---|---|---|
| cCorrGAN (reimpl.) | .000 | 4.339 | 1.000 |
| Image DDPM | .001 | 4.610 | 1.000 |
| CorrFlow (0.17M params) | **1.000** | **.712** | .9981 |
| Historical replay | 1.000 | .886 | .951 |
| PCA-64 Gaussian | 1.000 | .953 | .9998 |

- CorrFlow beats historical lookup on aggregate distances but lookup retains higher local precision/recall (observed scenarios kept exactly). CorrFlow draws are all novel (no training duplicates; median nearest-training distance .845× the real-test reference).
- Temporal shift is real and spectral: train vs test matrices separable at AUC .950 (test period has stronger leading-eigenvalue concentration — fewer effective dimensions, less diversification).

## What the Guarantees Do NOT Solve (paper's own scope)
- Does NOT establish flow matching > diffusion in general; the claim is that learned dynamics live in exact, equivariant coordinates. Table 1 changes representation AND objective — no causal attribution of each.
- Low F-SWD/energy does NOT mean the full joint law is recovered (AUC .9981 ≠ .5).
- Permutation equivariance does NOT imply projective consistency (k-asset marginal law vs submatrix of n-draw).
- Correlation-only: omits volatilities, marginal tails, dynamics. Anonymous-asset exchangeable model; named assets need sector/country/liquidity node attributes.
- Overlapping 252-day windows: 24,408 matrices ≠ 24,408 independent episodes; target is the distribution of ESTIMATED correlations (mixes latent dependence + estimator noise).

## Reusable Patterns

1. **Constraint/distribution separation**: solve hard-constraint validity with an exact bijective coordinate map; spend neural capacity only on the domain distribution. Applies to any structured object with exact parametrizations (SPD manifolds, simplex, Stiefel).
2. **Symmetry via coordinates + architecture, not augmentation**: order-independent representation (GFT) + equivariant network + ODE uniqueness = exact guarantee, no permutation-augmented training needed.
3. **Repair-as-a-symptom audit**: if a generator needs post-hoc projection to reach the sample space, the learned dynamics live in the wrong space — measure the RMS distortion of the repair as a diagnostic (image models: .018/entry, AUC 1.000 after repair).
4. **Strong non-neural controls (PCA-Gaussian, historical replay) prevent attributing every gain to neural capacity.**
5. **Finite-budget honesty**: report seeds, equal-epoch caveats, and what longer training could change; claims scoped to "among fitted generators under this budget".

## Implementation Notes (verified numerically 2026-10-17)

```python
# GFT forward (symmetric matrix log via eigendecomposition)
w, V = np.linalg.eigh(C); M = V @ np.diag(np.log(w)) @ V.T
Gamma = M - np.diag(np.diag(M))  # hollow symmetric log-coords

# Inverse GFT: fixed point on missing diagonal
d = np.zeros(n)
for it in range(max_iter):
    C = mat_exp_sym(Gamma + np.diag(d))
    d = d - np.log(np.diag(C))   # drive diag(C) -> 1
    if np.max(np.abs(np.diag(C) - 1)) < 1e-13: break
```

- Verified: 5/5 round-trips to 1e-14 (incl. near-singular, mixed-sign, negative-cluster cases); Γ-conjugation equivariance 1e-16; 30/30 arbitrary hollow matrices → valid correlation matrices (worst condition 1e12 — extreme but valid, as the bijection promises); n=2 → atanh(ρ) exact to 1e-16.
- Near-singular targets need 60+ fixed-point iterations; keep max_iter ≥ 500 and a 1e-13 tolerance.

## Use When
- Building libraries of plausible correlation/covariance scenarios (stress testing, reverse stress testing, portfolio-risk analysis)
- Any generative model whose outputs must satisfy nonlinear manifold constraints exactly (not after repair)
- Domain data has label-permutation symmetry (exchangeable units: anonymous assets, sensors, neurons)
- Comparing generative models on structured data — adopt the 21 order-invariant summary metrics (correlation/eigenvalue quantiles, effective ranks, log-det, log condition number) + F-SWD + manifold precision/recall + classifier AUC

## Related
- Archakov & Hansen (2021) — GFT parametrization; Collas et al. (2025) DiffeoCFM (pullback geometry, Cholesky coords — order-dependent); Marti (2020) CorrGAN; Kubiak et al. (2024) correlation DDPM; Higham (2002) nearest-correlation repair.
