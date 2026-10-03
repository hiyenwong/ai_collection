---
name: koopman-supereigenfunction-d2c
description: Use for data-driven Koopman stability/safety certificates.
category: control
---

# Koopman Supereigenfunctions — Data-to-Certificates (D2C)

**Source**: arXiv:2610.00178 (Umesh Vaidya, Clemson, Sep 2026)
**Paradigm**: Skip model identification entirely — learn inequality-based certificates directly from trajectory data.

## Core Idea

Koopman eigenfunctions satisfy an *equality* K_f φ = λφ (exact representation), but control tools (Lyapunov, barrier functions, HJ) are *inequality*-based. **Supereigenfunctions** relax the spectral equality to a one-sided inequality:

```
K_f φ ≤ λφ        (exponential growth envelope, not exact evolution)
```

φ then bounds system behavior: φ(x(t)) ≤ e^{λt} φ(x₀). When λ < 0 this certifies exponential convergence; the rates recover Lyapunov exponents. Supereigenfunctions are nonnegative, globally defined, form a convex cone, and their non-uniqueness is a *design degree of freedom* (choose probes per task: stabilization / safety / uncertainty).

## Three Constructions (all data-driven)

### 1. Positive-resolvent (state-space D2C)
Pick a nonnegative probe g ∈ F₊ encoding the quantity of interest. For λ > ω (semigroup growth bound ‖U_t‖ ≤ Me^{ωt}):

```
φ_λ(x) = R(λ; K_f) g = ∫₀^∞ e^{-λt} g(s_t(x)) dt      (discounted risk-to-go)
(λI − K_f) φ_λ = g   ⟹   K_f φ_λ = λφ_λ − g ≤ λφ_λ
```

Finite rollout (T horizon): φ_{λ,T} = ∫₀^T e^{-λt} g(s_t(x)) dt with exact error ε_T = M e^{−(λ−ω)T} ‖g‖. Compute directly from short trajectory rollouts — no model, no finite-dimensional Koopman approximation. Componentwise version: stack probes g₁..g_m → K_f Φ(x) ⪯ ΛΦ(x).

### 2. Gramian (tangent bundle / contraction)
Directional certificate φ(x,v) = vᵀM_λ(x)v with

```
M_λ(x) = ∫₀^∞ e^{-2λt} Y(t,x)ᵀ Q(s_t(x)) Y(t,x) dt
```

Y(t,x) = variational (tangent) dynamics. Satisfies K_f^tan φ ≤ 2λφ ⟹ contraction metrics are a special case (λ < 0 ⟹ exponential decay of differential displacements). Convergence requires **λ > χ_max** (largest Q-weighted Lyapunov exponent) — λ acts as a design upper bound on directional growth.

### 3. MET/QR (intrinsic directions)
Benettin incremental QR on tangent cocycle A_k Q_k = Q_{k+1}R_k gives Oseledets directions q_i(x_k) and exponents χ̂_i = (1/NΔt) Σ log|R_k|_ii, rates λ̂_i = 2χ̂_i. Directional observable φ_i(x,v) = (q_i(x)ᵀv)² — anisotropic expansion/contraction certificates.

## Certificate-Based Control Synthesis (convex QP)

For control-affine ẋ = f + G u, stack certificates Ψ(x) with open-loop envelope K_f Ψ ⪯ ΛΨ. Enforce desired rates B = diag(β_i) via pointwise QP:

```
u*(x) ∈ argmin ½uᵀRu
  s.t.  (K_G Ψ)(x) u ⪯ −(Λ − B) Ψ(x),  u ∈ U
```

Same structure as CLF/CBF-QPs, but constraints derive from operator theory and are computable from data. Safety variant: forward-invariance of risk sublevel sets S_i(c_i) = {φ_i(x) ≤ c_i}.

## Safety via Risk Probes

Convert state constraints g_i(x) ≤ 0 into nonnegative risk r(x) = Σ ρ(g_i(x)); certificate φ_{λ,T}(x) = ∫₀^T e^{-λt} r(s_t(x)) dt is *discounted future risk*, a supereigenfunction of the drift.

- **Occupation bound**: r(x) ≥ r̄ > 0 on unsafe set ⟹ ∫₀^T e^{-λt} 1_U(s_t(x)) dt ≤ c/r̄ for φ_{λ,T}(x) ≤ c.
- **Hard safety** (zero-safe probe: r=0 on S, r>0 on U): φ_{λ,T}(x) = 0 ⟺ trajectory stays safe on [0,T].
- Probe choices trade off smoothness vs. strictness: indicator 1{s>0} (discontinuous, hard), hinge max(0,s) (continuous, vanishes at boundary), softplus log(1+e^{κs}) / exp(κs) (smooth, graded, strictly positive both sides).

## Uncertainty Propagation

Given initial set X₀, envelopes φ̄_i(t) = e^{λ_i t} sup_{X₀} φ_i define certified reachable sets R_φ(t; X₀) = {z: φ_i(z) ≤ φ̄_i(t) ∀i}. Two supereigenfunctions with rates ±0.1 sufficed to envelope Duffing double-well propagation (expansion in x, contraction in y).

## Implementation Checklist

1. Choose task → probe family {g_i} and discounts {λ_i} (λ must dominate growth for convergence; small λ = long-horizon risk, large λ = near-term risk).
2. Collect trajectories (or variational rollouts for Gramian/MET variants).
3. Estimate φ_{λ,T} by discounted accumulation; error decays as Me^{−(λ−ω)T}.
4. Envelope/comparison or QP-based control as needed. Online resolvent certificates need only local value + gradient (from short rollouts) — scales with state dimension.

## Pitfalls

- λ ≤ ω (or λ ≤ χ_max for Gramian): integral diverges — pick discount strictly above worst-case growth rate.
- Indicator probes break continuity (bad for gradient-based QPs); hinge probes lose margin near the safety boundary.
- Approximation error budget: ε_D2C = M e^{−(λ−ω)T}‖g‖ + ε₁ + |λ|ε₀ (rollout truncation + function/derivative approximation).
- Distinct from CLF/CBF: certificates reflect intrinsic dynamics (operator-derived), not heuristic candidates — but synthesis still needs QP feasibility in the operating region.
