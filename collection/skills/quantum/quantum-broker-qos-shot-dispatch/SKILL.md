---
name: quantum-broker-qos-shot-dispatch
description: MILP QoS shot dispatch across heterogeneous quantum QPUs.
category: quantum-computing
---

# Quantum Broker: QoS-Aware Shot-Wise Dispatch

**Source**: arXiv:2610.28342 (Bisicchia et al., Univ. Pisa / Extremadura, IEEE TQE 2026) — verified numerically 2026-10-22 (26/26 checks passed).

**Use when**: distributing measurement shots of one quantum circuit across multiple heterogeneous cloud QPUs under cost/time/fidelity constraints; building provider-agnostic quantum execution managers; scheduling any statistically-independent divisible workload across heterogeneous priced resources.

## Core Idea

Quantum measurement shots are statistically independent, so a single circuit's shot budget S can be **split across heterogeneous QPUs** and the output counts merged — execution management becomes a **constrained dispatch optimization problem**, not a backend-selection problem.

## The MILP Dispatch Formulation

Decision variables per backend b:
- `x_b ∈ Z≥0` — shots assigned to backend b
- `y_b ∈ {0,1}` — backend-use indicator

Implicit constraints (always enforced):
- `Σ_b x_b = S` (exact shot conservation)
- `0 ≤ x_b ≤ S·y_b` (big-M coupling: used ⟺ allocated)

Linearized QoS terms:
- cost: `c_b·x_b` (one-shot cost coefficient × shots)
- execution time: `t_b·x_b`
- waiting time: `w_b·y_b` (queue delay activated by the binary)
- `max()` aggregates → auxiliary variable `m` with linking constraints `t_b·x_b + w_b·y_b ≤ m`
- min-shots requirements: `x_b ≥ L·y_b`

Scenario-1 example: `min 0.5·m + 0.5·Σc_b x_b` s.t. `Σc_b x_b ≤ 800`, `x_b ≥ 300y_b`, `max_b(t_b x_b + w_b y_b) ≤ 2000`.

**Verified optimum** (5 fake-IBM backends, d=4, S=4096): MILP splits [1425,1125,687,0,859] with objective 515.63, dominating every single-backend baseline (820–1373) — splitting reduces BOTH makespan (m=360s vs ~1700s) and cost.

## ⚠️ Linearization Gap & Post-Solve Validation

The MILP pre-filters backends with reliability `R̄_b = R_syn,b(S)` computed at the FULL budget S, but the true (nonlinear) reliability is **shot-dependent**:

```
R_syn = 1 − √((ε·d)² + (1/(2√s))²)
```
(quadrature of depth degradation εd and finite-sampling term 1/(2√s))

**Reproduced failure mode**: backend passes pre-filter (R̄=0.9592 ≥ τ=0.955) but at the allocated x_b=300 shots its true reliability is 0.9507 < τ → **solver-feasible but NOT QoS-feasible**. The framework therefore re-evaluates every MILP candidate against the original nonlinear profiler functions and REJECTS invalid dispatches (no repair in v1). A QoS-feasible allocation needs s≥589 shots on that backend. Nonlinear solver (dual annealing) avoids this by evaluating the original functions during search.

## Backend Profiling (Empirical Path)

1. Benchmark random circuits at increasing depth on live QPU + noise-free simulator.
2. Distributional fidelity = **squared Bhattacharyya coefficient**: `F_BC(p,q) = (Σ_x √(p(x)q(x)))²` ∈ [0,1] (NOT quantum-state fidelity).
3. Fit exponential decay `F_BC(n) ≈ α^n` per benchmark layer; per-depth retention `α_depth = α^(1/d_layer)`; error param `ε_depth = 1 − α_depth`.
4. Dispatch-time prediction for circuit depth d: `F_dispatch = clip((1−ε_depth)^d, 0, 1)`.

Timing/cost heuristics: IBM ≈ duration-estimator × shots; IonQ ≈ gate-ratio model (150µs 1Q / 600µs 2Q) × shots + readout; cost per provider (linear-in-time, base+per-shot, or free simulators).

## QQSpec — Declarative QoS DSL (EBNF)

Variables: `shots[b]`, `used[b]`, `cost[b]`, `execution_time[b]`, `waiting_time[b]`, `fidelity[b]`, `total_shots`, user `weight_name`. Aggregates `sum/max/min` over backends. Constraints are comparator expressions; objective is any expression.

```
# Scenario-1 example
min(fidelity) >= 0.9                 # eligibility pre-filter
sum(cost) <= 800                      # budget
max(execution_time + waiting_time) <= 2000
min(shots) >= 300                     # per-used-backend floor
objective: 0.5*max(execution_time+waiting_time) + 0.5*sum(cost)
```

**Scalarization warning** (from the authors): weighted cost+time objectives need normalization (e.g. C/C_ref) before the weights are meaningful; QQSpec does NOT normalize automatically.

## Result Merging Property

Merged empirical distribution = shot-weighted mixture `Σ_b (s_b/S)·p_b`. By concavity of the Bhattacharyya root, `F_BC(mixture, ideal) ≥ (Σ_b (s_b/S)·√F_b)² ≥ min_b F_b` — **merging heterogeneous noisy backends cannot be worse (in BC terms) than the worst component**. Verified: mix F=0.9895 vs components 0.974/0.956.

Splitting shots of the SAME backend preserves the empirical distribution exactly (statistical independence) — verified by MC (split=0.99982 vs single=0.99982).

## Architecture Pattern (Profiler–Reasoner–Executor)

- **Profiler**: modular, interchangeable (static metadata / empirical benchmarking / learned regressors); cached profiles + lightweight dispatch-time elaboration (extract circuit depth → predict QoS).
- **Reasoner**: pluggable solvers — MILP (fast, deterministic, linear surrogate, certified optimal for the surrogate) vs dual annealing (nonlinear profiles, higher quality, no optimality certificate). Planning-time vs dispatch-quality trade-off.
- **Executor**: provider-agnostic job submission, monitoring, count aggregation.

## Practical Lessons

- Pre-filtering nonlinear constraints at a reference point (full budget) + post-solve validation is a cheap two-phase pattern for MILP with nonlinear QoS — but rejected candidates are NOT repaired; budget for fallback to nonlinear search.
- Solver-feasible ≠ QoS-feasible: ALWAYS re-validate linearized solutions against the original evaluation functions.
- Backend eligibility can be empty at large depth (at d=10 no fake backend passed τ=0.9 with the paper's profiles) — report infeasibility rather than relaxing constraints.
- End-to-end merged fidelity across 18 executions: mean F_E2E = 0.907 vs best single-backend 0.919 — splitting trades a little fidelity for large cost/time gains.

## Verification Anchors (all reproduced 2026-10-22)

- F_BC: F(p,p)=1, disjoint=0, half-overlap=0.5, decreases with bias noise.
- Decay identity `(1−ε_depth)^d = α^(d/d_layer)` exact to 1e-12.
- R_syn: ↑shots → ↑score, ↑depth → ↓score, → 1−εd as s→∞, can go negative (score, not fidelity).
- MILP: beats 100k random feasible samples (515.63 < 523.04) and coarse-grid exhaustive (524.25); m tight at optimum.
- Linearization gap: 0.9507 < 0.955 ≤ 0.9592 reproduced; QoS-feasible minimum s=589.
