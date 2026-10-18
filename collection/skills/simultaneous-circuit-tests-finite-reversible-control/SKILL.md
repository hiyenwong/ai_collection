---
name: simultaneous-circuit-tests-finite-reversible-control
description: Certification of finite reversible quantum-control models. Joint circuit tests with exact MILP feasibility.
category: ai_collection
---

# Simultaneous Circuit Tests for Finite Reversible Models of Quantum Control

**Source**: arXiv:2610.06984 (Josef Bruzzese, 2026-10-04, quant-ph)

## When to Use

- Certifying whether a finite-state / discrete-frame quantum controller (permutation transition tables) can reproduce a whole **collection** of circuit probabilities with ONE shared model — not refit per circuit.
- Distinguishing "a good fit for one table" from an **exclusion certificate** that eliminates every model in the class.
- Building exact benchmarks with provable per-gate error bounds and sharp certified horizons.
- Designing finite-shot statistical tests that reject a controller class with confidence guarantees.

**Activation**: simultaneous certification, finite reversible model, shared-table feasibility, exclusion certificate, individual vs joint separation, finite-frame catalogue, quantum control memory bound, certified horizon, finite-shot certification, MILP model-class test.

## Core Framework

### 1. The model class
- Hilbert space C^d, finite label set X (|X|=M), frame representatives F_i ∈ U(d) (i∈X; labels need not be injective).
- Command alphabet G with nominal unitaries U_g. A **stationary controller** assigns ONE permutation π_g ∈ S_X per command — the same table every time the command occurs.
- Preparation: fixed ρ, terminal effect E; context set K with compensated seeds ρ_k = F_{a_k}† ρ F_{a_k} so every branch represents the same physical state; prior η over contexts.
- Word w=(g_1..g_ℓ): ideal p(w)=tr(EU_w ρU_w†); model q_{π,η}(w)=Σ_k η_k tr(E F_{π_w(a_k)} ρ_k F_{π_w(a_k)}†).

### 2. The two radii (THE central distinction)
- **Joint radius** R(W) = min_{π∈Π, η∈P} max_{w∈W} |q(w) − p(w)| — one shared model for the whole collection.
- **Independent radius** R_ind(W) = max_{w∈W} min_{π,η} |q(w) − p(w)| — refit per circuit.
- Monotonicity: enlarging W cannot decrease R; enlarging the class Π or prior set P cannot increase it. R_ind ≤ R(W), and the inequality **can be strict**.

### 3. Exact shared-table feasibility (Theorem 3.1)
MILP over binary permutation variables x^g_ij (row/column sums 1, prohibited edges 0, calibration edges fixed) plus per-word mass flows:
- m^{w}_{k,0,i} = η_k·1_{i=a_k}; Σ_j f^{w}_{k,s,i,j} = m^{w}_{k,s−1,i}; Σ_i f = m_{k,s,j}; 0 ≤ f ≤ x.
- Terminal bands: −δ ≤ Σ_{k,j} r_{k,j} m^{w}_{k,|w|,j} − p(w) ≤ δ for all w ∈ W.
- **Feasible ⟺ R(W) ≤ δ.** Dropping integrality = relaxation only — a floating-point solver failing to find a solution is NOT a proof of infeasibility.

### 4. Exact separation example (4 frames)
Frames F_i = R_y(iπ/2), commands G=R_y(π/4) (ε_G = 2sin(π/16)), A=R_y(π/2) (ε_A=0). Only two allowed G-tables: id and cyclic shift s. For W={(G),(G,A)}: R_ind = (2−√2)/4 ≈ 0.146 < 1/4 < R(W) = √2/4 ≈ 0.354. Each circuit fits individually within 1/4; NO single allowed table fits both. Randomizing the table per run is a DIFFERENT model class (R_mix=(√2−1)/4 at λ=1/2), not an alternative prior.

### 5. Certified horizon by exhaustive exclusion
464-frame catalogue with right-phase equivariance (58 orbits × 8 phases); exact arithmetic in Q(√2,√3,√5,√7,i) via 32-element product basis. Repeated block (T,H):
- Existence: witness cycle (1,26,56,35,40,52,17,53,18,48,43,41,50,42,49,51,33) fits within 13/40 through **192 blocks**.
- Exclusion: DFS over admissible histories with three sound prunings — probability band (readout ∈ [p_n−1/3, p_n+1/3]), injection (permutation), matching-extension (residual bipartite perfect matching via augmenting paths). No surviving path through depth 193; 41,595 nodes visited.
- A different controller fits ALL 8,190 forward H,T words of length ≤ 12 (max err ≈ 0.302). Feasibility certificate ≠ optimality; repeated-block and short-word collections exercise different quantifiers.

### 6. Finite-window spectral obstruction (Theorem 6.2)
For irrational quantum oscillation p_n = a(1−cos 2nθ) vs any q-periodic (q ≤ M) permutation readout: |S_D(f)| ≤ κ_M/D with κ_M = max_q 1/|sin(qθ)|; combined with S_D(p) ≥ −C/D, any D > (κ_M+C)/(a/2−δ) certifies max_n |f(n)−p_n| > δ for EVERY model in class. Necessary accuracy condition: ε ≥ 1/κ_M.

### 7. Finite-shot certification (Prop 7.1)
m circuits, N shots each, radius r_N = √(log(2m/α)/2N). Reject class Q when dist_∞(p̂, Q) > r_N. Under any model in Q: false rejection ≤ α; if ideal p is true and R(W) > 2r_N: rejection with prob ≥ 1−α. Hardware noise ν is separate: sufficient condition becomes R(W) > ν + 2r_N; model-class uncertainty must be handled by ENLARGING the class, never by widening tolerance.

## Reusable Patterns

1. **Existence vs exclusion certificates**: exhibiting one fitting model proves nothing about the class; failing several candidate tables proves nothing either. Only exhaustive (or analytic) elimination over the fully-specified class counts.
2. **Shared-parameter testing**: any certification task where one fixed model must serve a family of experiments — replace per-instance refits with the joint radius R(W) = min max; strict individual-vs-joint separation is generic when transition structure couples instances.
3. **Sound pruning triple for class exhaustive search**: (a) per-step output band, (b) injectivity, (c) matching-extendability — each rejection provably removes no feasible model.
4. **Exact algebraic arithmetic**: product-basis representation of number fields with rational-bound sign certification; never treat floating-point optimization status as an exclusion proof.
5. **Spectral mismatch bound**: periodic (finite-state) trajectories cannot track irrational-frequency oscillations beyond window D ~ κ_M/δ — a generic finite-model-vs-quantum obstruction template.
6. **Symmetry that kills nuisance parameters**: right-phase equivariance makes all preparation contexts produce identical terminal rays, eliminating prior optimization entirely — look for group actions that quotient out nuisance dimensions.
7. **Sampling layer on exact certificates**: Hoeffding + union bound converts any exact separation into a finite-shot decision rule; fix the collection and rule BEFORE data collection.

## Limitations (paper's own honest scope)

- Results concern the stated finite model classes only — no universal memory bound, no claim about physical hardware discrepancy.
- Exclusion certificates are class-relative: removing symmetry or adding stochastic transitions/table redraws invalidates them; the witness remains a witness in any larger class.
- The register bound M counts evolving labels only; table storage, preparation contexts, probability precision, and readout conventions must be counted before physical interpretation.
- No efficient asymptotic onset from the spectral bound (small denominators can make windows large).

## Key Formulas

| Object | Formula |
|---|---|
| Joint radius | R(W) = min_{π,η} max_{w∈W} |q_{π,η}(w) − p(w)| |
| Independent radius | R_ind(W) = max_{w∈W} min_{π,η} |q_{π,η}(w) − p(w)| ≤ R(W) |
| Accumulated error | |q − p| ≤ min(1, Σ_s ε_{g_s}) |
| Phase-optimised distance | d_op(V,W) = min_{|z|=1} ‖V − zW‖_op; d²=2−|tr(V†W)| in d=2 |
| Mixed-table radius | R_mix = (√2−1)/4 at λ=1/2 (different class!) |
| Sampling radius | r_N = √(log(2m/α)/(2N)) |
| Spectral window | D > (κ_M + C)/(a/2 − δ), κ_M = max_{1≤q≤M} 1/|sin(qθ)| |
