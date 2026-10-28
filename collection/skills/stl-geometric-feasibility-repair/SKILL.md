---
name: stl-geometric-feasibility-repair
description: Use for horizon-independent STL feasibility and repair.
category: systems-engineering
---

# Geometric STL Feasibility & Repair — Horizon-Independent

**Source**: arXiv:2610.00199 (Avinash Malik, Sep 2026, 31 pp)
**Problem solved**: STL control-synthesis feasibility checks normally discretize the time horizon → MILP with binary-variable blowup (Gurobi times out at N ≥ 1000 steps). This method evaluates feasibility **independently of horizon length** (< 0.25 ms at N = 10,000) and returns a **closed-form temporal repair** when infeasible.

## Core Method

### Step 1 — Temporal↔Spatial Bijection (Bhat–Bernstein settling-time inversion)
Model worst-case progress of spatial predicate μ under actuator bound c with finite-time (non-Lipschitz) dynamics:

```
μ̇ = −c·sgn(μ)|μ|^β ,   c > 0, β ∈ (0,1)
τ_s(μ₀) = μ₀^{1−β} / (c(1−β))                          (settling time)
μ₀(T, μ_target) = (μ_target^{1−β} + c(1−β)T)^{1/(1−β)}  (backward inversion)
```

This closed-form bijection maps a temporal window [a,b] into a **spatial level-set boundary** evaluated at time zero. Constant-velocity limit: β → 0⁺ gives μ₀ = μ_target + cT (linear reach budget I_F = v_max·T_F).

### Step 2 — Geometric Denotational Semantics (level-set functions)
Map STL formula ψ to differentiable spatial field ⟦ψ⟧: ℝ^d → ℝ. Feasible initial set = zero-superlevel set {x(0): ⟦ψ⟧(x(0)) ≥ 0}.

```
⟦⊤⟧ = +∞          ⟦μ(x) ≥ 0⟧ = μ          ⟦¬ψ⟧ = −⟦ψ⟧
⟦ψ₁ ∧ ψ₂⟧ = −(1/η) ln(e^{−η⟦ψ₁⟧} + e^{−η⟦ψ₂⟧})          (soft-min, Log-Sum-Exp)
⟦ψ₁ ∨ ψ₂⟧ = (1/η) ln(e^{η⟦ψ₁⟧} + e^{η⟦ψ₂⟧}) − (ln 2)/η  (soft-max)
```

### Step 3 — Temporal Operators as Spatial Set Inversions
- **Liveness F[a,b]ψ**: capture basin S_{b−a}(f) = {x: −f(x) ≤ (c(1−β)(b−a))^{1/(1−β)}}, then backward pre-image Pre_a(S) = {x: ∃u(·), Φ_a(x,u(·)) ∈ S}.
- **Safety G[a,b]ψ**: contracted buffer B_{b−a}(f) = {x: f(x) ≥ (c(1−β)(b−a))^{1/(1−β)}}, then Pre_a(B).

### Step 4 — Polyhedral Compilation (Theorem 1)
For affine predicates μ_i = g_iᵀx − h_i ≥ 0 and linear dynamics ẋ = Fx + Gu:
- Flow propagation keeps affine geometry: a_iᵀ = g_iᵀ e^{Fa}.
- Temporal inversions shift bounds h_i → b_eff,i(a,b).
- At nominal point x*, LSE gradient = softmax weights → dual vector y.
- Feasibility check collapses to one matrix-vector inclusion: **Ax(0) ≤ b_eff ⟺ ⟦ψ⟧(x(0)) ≥ 0**.

### Step 5 — Farkas Diagnosis + Closed-Form Repair
If infeasible, Farkas' lemma yields dual y ≥ 0 isolating the minimal conflicting predicate and the **spatial gap** r (e.g. 3.00 m). Map gap to time exactly:

```
ΔT* = r^{1−β} / (c(1−β))     (linear limit: ΔT* = r / v_max)
```

Repair = extend the liveness horizon by ΔT* (e.g. 4.17 m gap → 1.83 s delay → UAV mission becomes realizable). No iterative re-optimization.

## Guarantees (proven)

- **Soundness**: ⟦ψ⟧(x(0)) ≥ 0 ⟹ ∃u(·): robustness ρ(ψ,x,0) ≥ 0. Empirically 0% false positives over 10,000 Monte Carlo trials (6D drone).
- **Quantified completeness gap**: LSE smoothing margin δ = ln k/η (k = predicate count) — false negatives stay within predicted margin.
- **Horizon-independent complexity**: cost = single polyhedral inclusion, invariant in horizon length and nesting depth (verified up to p = 32 nested operators, k = 50 predicates, all < 0.25 ms; MILP hits 120 s timeout at N ≥ 1000).
- Speedup: 570× vs Gurobi MILP on the 6D drone case, same spatial-deficit answer (4.17 m).

## When to Use

- STL mission feasibility screening with actuator limits / tight deadlines (robotics, UAV mission planning)
- Diagnosing *why* a temporal spec is physically unrealizable + computing the exact deadline relaxation
- Any pipeline where horizon-discretized MILP is the bottleneck
- Online feasibility queries (sub-millisecond) inside synthesis loops

## Pitfalls

- Sound **under**-approximation: conservative rejections possible (bounded by ln k/η — raise η to shrink, at numerical cost).
- Polyhedral compilation assumes **affine predicates + linear dynamics** (ẋ = Fx + Gu). Nonlinear plants need local linearization first.
- c = ‖u‖∞ is a worst-case drift bound — loose actuator models make repairs conservative.
- Non-Lipschitz β dynamics are a *bounding device*, not the real plant: the certificate constrains the reachable margin, it does not synthesize the controller.
