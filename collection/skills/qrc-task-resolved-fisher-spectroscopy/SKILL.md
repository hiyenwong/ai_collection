---
name: qrc-task-resolved-fisher-spectroscopy
description: Task-resolved Fisher spectroscopy for quantum reservoir computing: separates encoding vs measurement vs compression loss.
category: ai_collection
trigger: quantum reservoir computing diagnostics, Fisher information hierarchy, QFIM, many-body correlations, Walsh modes, shot allocation
---

# Task-Resolved Fisher Spectroscopy for QRC (arXiv:2609.29570)

**Source**: arXiv:2609.29570 (Yang Peng, CSU Northridge / Caltech IQIM, 26 Aug 2026, quant-ph + cs.LG)

## Problem

QRC benchmark capacity alone cannot tell WHERE task information is lost: (1) never encoded in the reservoir state, (2) encoded but not exposed by the chosen measurement, (3) exposed by the measurement but discarded by low-order classical feature compression, or (4) statistically inaccessible at finite shot budget. Task-resolved Fisher spectroscopy answers all four with one construction, using only stationary labeled records + measured bit strings (no input model, no tomography).

## Construction

### Task-score coordinates (target-defined, not hypothesis-defined)
- Recent input window z (length L), stationary distribution P_ref(z) (may be unknown; sampled).
- Center targets y_A, Gram-Schmidt orthonormalize under ⟨u,v⟩_ref = E_ref[uv] → **orthonormal task scores s_A(z)** with E_ref[s_A]=0, E_ref[s_A s_B]=δ_AB. Single target: s = (y−µ)/σ.
- For i.i.d. unbiased binary inputs: **Walsh modes** χ_A(z) = Π_{k∈A} z_{t−k+1} ARE the score family (closed form). Parity targets PC2/PC4 are already normalized scores.

### Exactly affine score perturbation (the key trick)
- Reweight histories: P_θ(z) = P_ref(z)(1 + Σ_A θ_A s_A(z)) (admissible θ-neighborhood exists since scores bounded).
- Ensemble-averaged reservoir state is EXACTLY affine in θ: ρ(θ) = ρ_ref + Σ_A θ_A Γ_A, with Γ_A = Σ_z P_ref(z) s_A(z) ρ̄(z). **No small-amplitude expansion involved** — works at arbitrary physical input level.
- Experimentally implemented by importance-weighting stationary labeled records.

### The hierarchy (the deliverable)
Score parameters θ as the Fisher parameters. With QFIM H_task, complete-bit-string CFIM F, and order-r moment matrix B_r = D_r^T C_r^+ D_r (C_r = feature covariance, D_r = response matrix (D_r)_{αA} = Cov_ref(f_α, s_A) via the response-covariance identity):

**0 ⪯ B_1 ⪯ B_2 ⪯ ⋯ ⪯ B_N = F ⪯ H_task**

- **H_task − F**: task info in the state NOT exposed by the measurement → change measurement setting.
- **F − B_r**: info in the complete record DISCARDED by keeping only ≤r-body correlations → raise feature order.
- **B_r − B_{r−1}**: marginal value of adding the next correlation order.

### Capacity connection (why this is practical)
Quadratic form of B_r in score coordinates = EXACT stationary capacity of the optimal linear readout:
C_r[y] = (c^(A))ᵀ B_r c^(A) / (c^(A))ᵀ c^(A) — one matrix evaluates every output and every linear combination in the target span. Scalar chain for single target: 0 ≤ C_1[y] ≤ ⋯ ≤ C_N[y] = F[y] ≤ H[y].

### Sampling overhead of compression
Generalized eigenproblem B_r v_j = λ_j^(r) F v_j (F-orthonormal): λ_j^(r) ∈ [0,1] is the fraction of full measured Fisher info retained at order r; **κ_j = 1/λ_j^(r) = extra independent samples needed** for the same estimator variance. Single target: κ = F[y]/C_r[y]. Explains orders-of-magnitude sampling overhead BEFORE wasting the measurement budget.

### Finite-measurement-budget extension
Features estimated from M repeats of the same history-conditioned state: P_r^(M) → B_r as M grows; usable capacity C_r^(M)[y] gives the approach from one-shot bit strings to ideal expectation-value features. Separates shot-allocation effects from representation effects.

## Key Experimental Findings (5-spin dissipative interacting reservoir)
1. **Interactions route 4th-order temporal information (PC4) into higher-body spin correlations**: low-order compression (r=1,2) incurs orders-of-magnitude sampling overhead even when the parity target is "accessible" — benchmark error hides this until shots are counted.
2. Record-defined task scores predict held-out capacities, required feature order, and measurement-budget dependence for CORRELATED inputs/outputs (constructed directly from operating distribution, no analytic Walsh forms needed).
3. **Optimizing the local measurement axis recovers otherwise hidden task information** — measurement choice is a tunable, not a fixed cost.
4. Delayed PC4 (same nonlinear order, +1 memory step) diagnosed via the same machinery — the hierarchy separates memory depth from nonlinear order.

## Reusable Diagnostic Protocol (any physical reservoir/analog computer)
1. Collect stationary labeled record: input histories + measured bit strings.
2. Build task scores from targets (Gram-Schmidt on operating distribution; Walsh modes if i.i.d. binary).
3. Importance-weight records along scores → affine family (validate positivity of reweighted probabilities).
4. Estimate B_r at increasing orders r; estimate F from full bit strings; H_task from state model (simulation) or skip if experiment-only (measurement-level quantities suffice).
5. Read losses: H−F (measurement loss), F−B_r (compression loss), eigen-overheads κ_j (sampling cost).
6. Decide: change measurement setting / raise feature order / allocate shots / reposition measurement axis.
7. Report capacity as quadratic form of B_r in score coordinates — exact, task-resolved, comparable across settings.

## Cross-References
- Foundations: QFIM/SLD formalism; measurement monotonicity F ⪯ H; IPC (information-processing capacity) literature for RC.
- Related in collection: [[metrological-quantum-reservoir-networks]], [[effective-rank-qnn-expressivity]], [[linear-reservoir-computing-bottleneck]], [[cavity-method-rnn-analysis]].
- **KG**: arXiv:2609.29570, quant-ph/cs.LG
