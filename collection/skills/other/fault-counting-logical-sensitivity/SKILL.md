---
name: fault-counting-logical-sensitivity
description: Use when measuring QEC logical error sensitivities to every noise param from one Monte Carlo run.
category: ai_collection
---

# Fault-Counting Logical Sensitivity (Differentiable QEC Estimator)

Extract **all** logical sensitivities ν_i = ∂p_L/∂p_i simultaneously from a **single** Monte Carlo dataset at ONE noise configuration — reusing the sampled fault configurations that finite-difference (FD) methods throw away.

Source: "Efficient Estimation of Logical Sensitivities Through Fault-Counting" (Fu, Staples, Thompson; arXiv:2610.10531, Oct 2026)

## Core Estimator (Score Function / Log-Derivative Trick)

For independently sampled fault mechanisms E ⊆ Ω with shot outcome L(E) ∈ {0,1} (logical error indicator):

```
ν_i = E_p[ L(E) · ∂ log Pr_p(E) / ∂p_i ]
    = E_p[ L(E) · ( Σ_{e∈E}  (1/W_e) ∂W_e/∂p_i
                  − Σ_{e∉E} (1/(1−W_e)) ∂W_e/∂p_i ) ]
```

Per-shot Monte Carlo estimator: `ν̂_i = (1/N) Σ_k L(E_k) ∂ log Pr(E_k)/∂p_i`. Only **failing shots contribute** — the weights of occurred/absent faults are the sufficient statistics.

## Why It Beats Finite Differences

FD needs 2s separate simulations (±h per error type, s types), with sampling noise amplified by step size a = h/p_i. Variance ratio (Bernoulli model):

```
Var(ν̂_FD) / Var(ν̂_Diff) ≈ 2s / (a² · E[M_i² | L])
```

where E[M_i²|L] = expected squared count of type-i faults conditioned on logical failure. Verified **1–2 orders of magnitude shot reduction** on circuit-level surface code (d = 3,5,7; unrotated; Stim). E[M_i²|L] ≥ 1/s when subdividing s faults → advantage **scales quadratically** with number of error types defined.

FD step-fraction bias: measurable at a = 0.2 and growing — Diff has no step parameter at all.

## The Decisive Trick: Post-Hoc Fault Aggregation

Store per-fault sensitivity components ν_f (fault-level parametrization: s = 268 / 1526 / 4544 at d = 3/5/7). Grouping is decided **after** sampling, not fixed in advance:
- **Error budgets** by type (gate / measurement / idle / SPAM) at every point of a p_L-vs-p curve
- **Spatial heatmaps**: per-qubit sensitivities (bulk > boundary, decaying from patch center) → target hardware improvement spending
- **Per-round** resolution
- **Scaling budgets**: ∂Λ⁻¹/∂p_i via ν_i at d and d+2

## Free By-Products From the Same Data

1. **Total derivative / effective distance**: ν̂ = Σ_i ν̂_i estimates dp_L/dp along uniform-noise path. From the ansatz p_L = A(p/p_th)^((d+1)/2): **d̂ = 2ν̂p/p̂_L − 1** — a local, unbiased distance diagnostic at every sampled point (→ d in low-p limit; → −1 as p_L plateaus at 1/2).
2. **Threshold contours in s-dim noise space** via sensitivity-guided Newton–Raphson:
   - Crossing function Δ(p) = log p_L(d₂,p) − log p_L(d₁,p); root = finite-distance threshold
   - ∇Δ comes from the **same two experiments** (one per distance) — no extra sims
   - Convergence rule: Newton step while |Δ| > 2σ_Δ; then refine shots until σ_Δ/|p·n| ≤ ε (normal-direction uncertainty normalized by tangent-origin distance)
   - After anchoring one contour point, the gradient gives the tangent direction → step h along tangent → re-anchor. **O(K^(s−1)) points vs O(K^s) grid** — factor K
   - Model-agnostic (explicit distance crossings; no critical-exponent fitting, which is known to miss finite-size corrections)

## Implementation Notes

- Toolchain: Stim circuit sampler + PyMatching / correlated PyMatching / Tesseract decoders; works with any decoder held fixed at p
- Decoder must stay **fixed at p** while noise is perturbed analytically (perturbation enters only through W_e)
- Applies to **any independently sampled stochastic mechanism**: Pauli circuit noise, leakage, erasure, high-weight correlated errors, non-Clifford errors — the estimator only needs ∂log Pr/∂p_i
- Second- and higher-order derivatives follow the same pattern (curvature of threshold contours; rare-event reweighting for harmful correlated configurations) — straightforward extension

## Failure Modes / Caveats

- FD remains the honest fallback when fault mechanisms are **not independently sampled** (correlated sampling breaks the product-form Pr)
- Per-fault storage is O(s) floats per shot window — aggregate streaming if s explodes
- Threshold contours are finite-distance crossings, approximating (not equal to) asymptotic thresholds — state the (d₁,d₂) pair used

## When to Use

- QEC error-budget analysis: which physical mechanism dominates logical failure (guide hardware roadmaps)
- Threshold surface mapping in multi-parameter noise models (e.g. 2Q-gate × idle × measurement trade-offs)
- Any Monte Carlo pipeline where gradient information per sample is discarded — the log-score trick is generic (REINFORCE-style) and transfers beyond QEC
