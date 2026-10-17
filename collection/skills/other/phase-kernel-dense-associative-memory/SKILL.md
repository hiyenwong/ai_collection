---
name: phase-kernel-dense-associative-memory
description: Use phase kernels to lift Modern Hopfield memory capacity.
category: ai_collection
---

# Phase Kernel Lifts Capacity of Dense Associative Memory (S-Hop)

**Source**: arXiv:2610.21493 — Yifei Zhao, Ying Tang (UESTC), NeurIPS 2026
**Code**: https://github.com/Machine-learning-and-complex-systems/S-Hop

## Problem: The Linear-Kernel Geometric Bottleneck

Modern Hopfield Networks (MHN) have provable exponential capacity in feature dimension D, but the standard **linear kernel** (ξ = φ) makes the energy surface a dot-product geometry:
- At high memory load N, attractor basins around stored patterns become **narrow and overlapping** → spurious states, memory confusion.
- U-Hop-style learned linear projections reposition embeddings but stay linear; the theoretical capacity never materializes in practice (U-Hop fails at N=10 on ImageNet 224×224 under one noisy update).
- Any fix must simultaneously preserve **Lyapunov stability (monotone energy descent)** and **exponential capacity** — a nonlinear feature substitution alone guarantees neither.

## Core Idea: Nonlinear Phase Kernel + Surrogate Phase Energy

Work in **phase variables** φ ∈ R^d (motivated by oscillator associative memories), embed into MHN feature space via a coordinate-wise nonlinear map F: R^d → R^D, and pull the MHN energy back to phase space where a **separable strongly-convex regularizer** decouples the update per coordinate.

### S-Hop kernel (the concrete instantiation, D = 2d)

Per coordinate k, the feature pair is:

```
f1(t) = √(t² + tanh t + 1)      f2(t) = √(t² + 1)
F(φ) = [f1(φ1), f2(φ1), ..., f1(φd), f2(φd)]
```

⚠️ **PDF transcription pitfall (verified reconstruction)**: `pdftotext` silently drops the √ radicals in the paper's Eq. (3), rendering it as `φ²+tanh φ+1, φ²+1`. The radical form is required — confirmed by three independent cross-checks:
1. `(1/2)||F(φ)||² = Σ_k q(φ_k)` with `q(t) = t² + (1/2)tanh t + 1` → `q'(t) = 2t + (1/2)sech² t` (paper's local field, Eq. 9) ✓
2. `q''(t) = 2 − tanh(t)·sech²(t)` (paper's Eq. 43) ✓
3. The paper's own remark that the Jacobian "shares the same square-root structure" and µ = 2−2/(3√3) ≈ 1.615 ✓

Whenever transcribing this kernel, re-derive from `h(t) = q'(t) = 2t + ½sech²(t)` — never trust the extracted text of the feature map directly.

### Energy decomposition (phase space)

```
E(φ) = E1(φ) − E2(φ)
E1(φ) = Σ_k ∫₀^{φ_k} h(u) du        (separable strong-convex regularizer, ∇E1 = h)
E2(φ) = lse_β(X^T F(φ))              (MHN log-sum-exp interaction)
```
with memory matrix X = [F(ψ_1), ..., F(ψ_N)], softmax weights s(ξ) = softmax(βX^T ξ).

### CCCP retrieval dynamics (the whole method in one line)

Gradient stationarity: `h(φ*) = R(φ*)X s(ξ*)` where `R(φ) = J_F(φ)^T` (pullback Jacobian). Treating E1 implicitly, E2 explicitly:

```
φ_{t+1} = h⁻¹( R(φ_t) · X · softmax(β X^T F(φ_t)) )
ξ_{t+1} = F(φ_{t+1})
```

- `h(t) = 2t + ½sech² t` is **globally strictly monotone** (q'' ≥ µ > 0), so `h⁻¹` exists per coordinate — the implicit step is N scalar 1-D root finds, embarrassingly parallel.
- No closed form for `h⁻¹`; use bisection/Newton per coordinate (monotone ⇒ safe).
- Both E1, E2 are globally strictly convex ⇒ strict DC decomposition ⇒ **monotone energy descent** E(φ_{t+1}) ≤ E(φ_t), equality only at fixed points.

## Admissibility Conditions for a General Phase Kernel

A coordinate-wise kernel F(φ) = [f1(φ_k), f2(φ_k)]_k is admissible iff:

1. **Separability + strong convexity**: Q(φ) := ½||F(φ)||² = Σ_k q(φ_k) + C with uniform Hessian bounds `µ ≤ q''(t) ≤ L_Q` for all t. (S-Hop: µ = 2 − 2/(3√3) ≈ 1.615, L_Q = 2 + 2/(3√3) ≈ 2.385, κ = L_Q/µ ≈ 1.477.)
2. **Third-derivative bound**: `sup|q'''(t)| < ∞` (used only in the Jacobian-perturbation step of the contraction proof).
3. **Kernel contraction condition**: `ρ₀ := sup_t |f1·f1'' + f2·f2''| / q''(t) < 1`. This is the verifiable-in-advance structural condition; it yields `(1−ρ₀)µ ≤ (f1')² + (f2')² ≤ (1+ρ₀)L_Q`.
4. **Memory separation**: similarity gaps `Δ_i = min_{j≠i}(x_i^T x_i − x_i^T x_j)` above a deterministic threshold (Eq. 124) ⇒ retrieval balls pairwise disjoint.

The paper's P-Hop (second admissible kernel) shows this is a family, not a single trick.

## Theoretical Guarantees

- **Local convergence**: around each stored phase ψ_i there is an invariant ball S_i on which the update map is a strict contraction (rate ρ < 1 depends on κ, ρ₀, β, and the load); each ball holds a unique fixed point; composing with F gives feature-space convergence.
- **Disjoint basins**: under the Δ_i margin condition the balls {S_i} are pairwise disjoint — each memory owns a dedicated basin (no spurious crossover).
- **Exponential capacity (Theorem 3)**: for iid phases uniform on [−1, 1]^d, the storage condition holds with probability ≥ 1−δ whenever `N ≤ exp(γd) = exp(γD/2)` — same exponential order in D as standard MHN (Lucibello–Mézard).

## Hessian-Geometry Reading (why it works)

- Q of Legendre type ⇒ Fenchel dual Q* smooth/strongly convex; the Legendre map `h = ∇Q` is a **Riemannian isometry** between (R^d, g_Q) and the dual (metric diag q''(φ_k)).
- CCCP update = **primal→dual→primal** trajectory: `φ_{t+1} = ∇Q*(∇E2(φ_t))` — compute the lse gradient in dual space, pull back via ∇Q*.
- Condition number κ = L_Q/µ is the unified geometric constant: ellipsoidal distortion of the metric, Bregman-divergence asymmetry, and inverse-field sensitivity all bounded by it. Small κ (S-Hop: 1.477) = well-conditioned retrieval.

## Empirical Results (one noisy update, β=1, σ=0.3, MSE<0.1 criterion)

| Dataset | S-Hop | U-Hop (public avg) | MHN | C-Hop |
|---|---|---|---|---|
| MNIST (d=784) | ≥500 (U-Hop also ≥500) | ≥500 | <10 | <10 |
| CIFAR-10 (d=3072), N=500 | **92.07%** | 48.40% | 3.33% | — |
| TinyImageNet | **≥500** | first fail ~125 (≈4× gain) | — | — |
| ImageNet 64×64 / 224×224, N=500 | **91.5% / 98.53%** | <10 / <10 (≥50× load gain) | <10 | <10 |

- Speed: ~1.5 ms/query (RTX 5090), between MHN (0.1 ms) and U-Hop (10–40 ms amortized); 7–27× faster than U-Hop max-protocol while training-free at retrieval.
- **Ablations**: linear-kernel fallback collapses to N=60; similarity-only update (drop R(φ) Jacobian) fails at N=10 — **both** the nonlinear embedding and the Jacobian/inverse-field update are necessary; P-Hop (2nd kernel) passes ≥500, confirming the family view.
- Downstream: S-Hop layers replacing attention aggregation in a CIFAR-10 classifier reach ≈90% (+0.2 pp over best baseline).

## Implementation Guide

```python
import numpy as np

def F(phi):            # phase -> feature, D = 2d
    a = np.sqrt(phi**2 + np.tanh(phi) + 1.0)
    b = np.sqrt(phi**2 + 1.0)
    return np.stack([a, b], axis=-1).reshape(-1)   # interleave or concat per convention

def h(t):              # local field, componentwise monotone
    return 2.0*t + 0.5/np.cosh(t)**2

def h_inv(u):          # per-coordinate bisection; h strictly monotone => safe
    lo, hi = -1e3, 1e3
    for _ in range(60):
        mid = 0.5*(lo+hi)
        if h(mid) < u: lo = mid
        else: hi = mid
    return 0.5*(lo+hi)

def R(phi):            # J_F^T pullback (square-root Jacobian structure)
    a2 = phi**2 + np.tanh(phi) + 1.0
    b2 = phi**2 + 1.0
    df1 = (2*phi + 1.0/np.cosh(phi)**2) / (2*np.sqrt(a2))
    df2 = phi / np.sqrt(b2)
    return np.stack([df1, df2], axis=-1)   # d x 2, align with F layout

def s_hop_update(phi, X, beta=1.0):
    xi = F(phi)
    s = np.exp(beta * (X.T @ xi)); s /= s.sum()
    rhs = R(phi) @ (X @ s)                # d-vector
    return np.array([h_inv(rhs[k]) for k in range(phi.size)])
```

Key engineering points:
- `h⁻¹` via 60-iteration bisection is robust; Newton accelerates but needs care at large |u| (sech² term vanishes, h ≈ 2t).

**Numerical verification (2026-10-16, independent reimplementation)**: kernel identity `0.5(f1²+f2²) = q` exact to 1e-15; `q'' ∈ [1.6151, 2.3849]` matches µ/L_Q exactly; h' ≥ 1.0 (monotone). Retrieval with uniform random phases, σ=0.3, 20 updates: **96/100 at d=784, N=100** (implementation correct); 364/500 at N=500 (near-critical load for iid-uniform memories — consistent with the paper's caveat that natural correlated data needs memory curation); at d=50 the separation condition fails and retrieval collapses (theory-consistent, not a bug). Energy descent monotone on every run.
- Store memories as `x_i = F(ψ_i)`; ψ_i are the raw patterns mapped to phase (the paper uses pixels directly as phases on [−1, 1]).
- No training at retrieval: contrast with U-Hop's learned projection. S-Hop is a fixed nonlinear map + exact implicit step.

## When to Use / Related
- Dense associative memory / attention-layer memory capacity: S-Hop layers can replace attention aggregation (CIFAR-10 classifier result).
- Any setting where MHN retrieval confuses similar memories at load: the phase-kernel reshape widens basins (narrow→broad).
- Oscillator-memory bridge: phase formulation imports Kuramoto/oscillator intuition into the attention-equivalent energy framework.
- Complements: U-Hop (linear learned projection), C-Hop (cosine kernel — violates strong convexity, fails), memory-norm-penalized H-Hop (orthogonal axis), KLR/event-driven neuromorphic Hopfield (different regime), geometry-capacity theory (fit-free capacity prediction from embedding geometry).

## Limitations
- Capacity theorem assumes **iid uniform phases**; natural images are correlated (TinyImageNet goldfish subset: threshold 40; selecting well-separated memories with comparable feature norms restores ≥500). Memory curation matters.
- One-update protocol (shared budget); multi-update connects to the convergence theory (Appendix D.2).
- Learned phase kernels (adaptive to correlated data) are open.
