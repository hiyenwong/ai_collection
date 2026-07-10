---
name: heterogeneous-contract-control
description: >
  Heterogeneous assume-guarantee contract framework for co-design of layered control architectures.
  Decomposes safety-liveness specifications across discrete-time planning (MPC) and continuous-time
  safety layers using vertical refinement, timing compatibility, and explicit reference governors.
  Use when designing hierarchical control systems, layered control architectures (LCAs), assume-guarantee
  contracts for CPS, safety-liveness decomposition, MPC + low-level controller integration,
  reference governor design, hybrid energy storage systems, or compositional verification of
  multi-timescale control systems.
  Activation: layered control, heterogeneous contract, assume-guarantee contract, safety liveness,
  vertical refinement, explicit reference governor, MPC tracker integration, hybrid control architecture,
  contract-based design, time-scale separation, compositional control verification
---

# Heterogeneous Contract Framework for Layered Control

Based on: Takayama et al. (2026) "Safety by Invariance, Liveness through Refinement: Heterogeneous Contract Framework for Co-Design of Layered Control" — arXiv:2605.04222

## Core Problem

Layered control architectures (LCAs) combine a discrete-time (DT) planner (e.g., MPC) with a continuous-time (CT) safety layer. Three challenges:
1. No uniform specification language across discrete planning and continuous execution
2. No formal guarantees for interconnecting subsystems at heterogeneous time scales
3. Naive input-filtering laws that obstruct compositional separation

## Safety-Liveness Decomposition Principle

| Layer | Responsibility | Mechanism |
|-------|---------------|-----------|
| **CT Safety Layer** | Safety (unilateral) | Robust forward invariance via reference governor |
| **DT Planning Layer** | Liveness (bilateral) | MPC planning with convergence guarantees |

**Safety**: "Something bad never happens" — enforced by invariance at CT layer, regardless of DT commands.
**Liveness**: "Something good eventually happens" — requires both layers; bilateral via vertical refinement.

## Architecture Components

```
ΣH (DT Planner + ZOH)
  ├── Sampler: yk = hy(x(tk))
  ├── Planner (MPC): rk = π(yk, ẑk|k)
  └── Zero-Order Hold: r(t) = rk for t ∈ [tk, tk+1)

ΣL (CT Safety Layer)
  ├── Plant + Tracker: ẋ = f(x, κ(x,v), w)
  └── Reference Governor (ERG): r(t) → v(t)

Signal flow: r → v → x (sequential, no algebraic loops)
```

## Key Contracts

### High-Level Contract CH = (Ã_k^mis, (G_k^ref ∧ G_k^ISS))

- **Ã_k^mis**: Model mismatch assumption — ∥w̃_k∥ ≤ ε_E (abstraction error bound)
- **G_k^ref**: Reference feasibility — ∥r_k - r_{k-1}∥ ≤ r̄ (max reference gap)
- **G_k^ISS**: Input-to-state stability — convergence to goal with KL bound

### Low-Level Contract CL = ((A_k^env ∧ A_k^ref), (G_k^safe ∧ G_k^track))

- **A_k^env**: Disturbance bound — w(t) ∈ W
- **A_k^ref**: Reference rate — same as G_k^ref
- **G_k^safe**: Safety invariance — x(t) ∈ X_safe for all t
- **G_k^track**: Tracking guarantee — ∥h_r(x) - r∥ ≤ ε_L

## Critical Conditions

### Timing Compatibility
```
Ctss: Ts ≥ τ_LL
```
Sampling period must exceed low-level settling time.

### Vertical Refinement (Cross-Domain Handshakes)
```
Downward: G_k^ref ⇒ A_k^ref    (DT guarantee satisfies CT assumption)
Upward:   G_k^{track} ⇒ Ã_k^mis  (CT tracking implies model error bound)
```

### Recursive Well-Posedness (Definition 13)
1. Initial conditions satisfy A_0^ref and A_env
2. Local contracts: ΣH |= CH, ΣL |= CL
3. Recursive feasibility of MPC at every step
4. Vertical refinement condition C_r holds

## Explicit Reference Governor (ERG) as Contract Realizer

The ERG plays a **dual role**:
1. **Safety enforcement**: Robust forward invariance of X_safe
2. **Tracking guarantee**: Provides G_k^track for vertical refinement

**Advantage over CBF-QP**: ERG modifies only the reference signal v(t), preserving the low-level controller's stability certificates. CBF-QPs override control inputs and may perturb inner loop behavior.

### ERG Dynamics
```
v̇(t) = Δ(v(t), x(t)) · ρ(v(t), r(t))
```
where Δ is the Navigation Dynamics (ensures safety) and ρ is the Attraction Field (drives toward reference).

## Implementation Pattern

### Step 1: Define Contracts
Specify safe set X_safe = {x | Cx ≤ d}, goal y_goal, tolerance ε, disturbance bound W.

### Step 2: Design CT Layer
- Implement ISS tracking controller κ(x, v)
- Design ERG with safe set invariance guarantee
- Determine settling time τ_LL and tracking tolerance ε_L

### Step 3: Design DT Layer
- Build abstract model f̂ with error bound ε_E
- Design MPC with reference rate constraint r̄
- Ensure recursive feasibility via terminal constraints

### Step 4: Verify Composition
- Check Ctss: Ts ≥ τ_LL
- Verify downward refinement: G_k^ref ⊆ A_k^ref
- Verify upward refinement: G_k^{track} ⇒ Ã_k^mis(ε_E)
- Check error budget: ε_E + ε_T(ε_E) + δ < ε_H

## Theorem 1 (Correctness)

If the interconnection is recursively well-posed with tolerance ε_H, then:
- **Safety**: x(0) ∈ X_safe ⇒ x(t) ∈ X_safe for all t ≥ 0
- **Liveness**: ∃ T < ∞ such that ∥h_y(x(t)) - y_goal∥ ≤ ε for all t ≥ T

## Common Pitfalls

1. **Algebraic loops**: Without explicit ZOH modeling, DT and CT layers may create circular dependencies. ZOH enforces sequential information flow.
2. **CBF-QP interference**: Direct input modification can invalidate tracking models assumed by the planner. Use ERG instead.
3. **Time-scale mismatch**: Sampling too fast (Ts < τ_LL) violates timing compatibility and breaks vertical refinement.
4. **Unbounded reference steps**: Large ∥r_k - r_{k-1}∥ can violate tracking guarantees. Constrain via r̄.
5. **Abstraction gap**: Mismatch between planner model f̂ and plant dynamics f must be bounded by ε_E and absorbed into ISS analysis.

## Application Domains

- Hybrid Energy Storage Systems (HESS): Battery (slow) + Supercapacitor (fast)
- Autonomous vehicle control: Trajectory planning + Low-level tracking
- Power electronics: Energy management + Voltage regulation
- Robotics: Motion planning + Force/position control
