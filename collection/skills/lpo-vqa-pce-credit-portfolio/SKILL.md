---
name: lpo-vqa-pce-credit-portfolio
description: "Loan portfolio optimization via QUBO + Pauli Correlation Encoding + VQA. Covers credit-risk QCBO modeling, qubit-efficient encoding, annealing, top-K feasibility."
category: ai_collection
trigger: loan portfolio optimization, credit risk QUBO, PCE portfolio, variational quantum algorithm lending, microfinance quantum optimization, borrower default correlation
---

# Loan Portfolio Optimization with Variational Quantum Algorithms (LPO-VQA-PCE)

**Source**: arXiv:2609.30195 (Bhargava, Kumar, Dinda, Biswas, Rao, Banerjee, Sehrawat — LTM Research / L&T Finance, Sep 2026)

## Problem Class

Loan portfolio optimization (LPO): select K borrowers from N candidates minimizing portfolio credit risk. Unlike equity portfolio optimization, loan loss distributions are default-driven, skewed, fat-tailed, and driven by correlated defaults — borrower-level PD estimates alone do not characterize portfolio-level loss variability.

### Why LPO is harder than equity PO
- Loan data refreshed infrequently (vs continuous equity prices)
- Predefined contractual cash flows (no uncapped upside)
- Loss distribution driven by correlated defaults (geographic/sectoral/behavioral common factors)
- Exhaustive search infeasible: C(N, K) grows combinatorially

## Credit-Risk QCBO Formulation

### Borrower-level inputs (per borrower i, time t)
- **EAD** (Exposure at Default) = outstanding principal (+ accrued interest; often zero)
- **LGD** (Loss Given Default) = 1 − Recovery Rate (≈1 for unsecured micro-loans, no collateral)
- **PD** (Probability of Default) from credit score CS via scorecard logistic regression:
  ```
  PD = 1 / (1 + exp(−(β0 + β1·CS))),  β1 ≈ −ln(2)/PDO, β0 = ln(1/odds_target) + |β1|·target_score
  ```
  Industry setup: Target Score 600, Target Odds 50:1, PDO 20 → β1 ≈ −0.0346, β0 ≈ 16.88.

### Loss time series and risk quantities
```
L_it = EAD_it × LGD_it × PD_it          # borrower loss
µ_i = (1/T) Σ_t L_it                    # expected loss vector
Σ_ij = (1/(T−1)) Σ_t (L_it−µ_i)(L_jt−µ_j)   # loss covariance matrix
```

### Scale-mismatch fix (KEY TRICK — sign-preserving square root)
µ entries ~ O(10⁴) (money), Σ entries ~ O(10⁸) (money²). Using portfolio std-dev √(xᵀΣx) destroys the quadratic form. Fix:
```
Σ̃_ij = sign(Σ_ij) · |Σ_ij|^(1/2)        # element-wise signed square root
UL̃(x) = xᵀ Σ̃ x                          # preserves quadratic objective, money-scale comparable
```
Objective (modified total loss, α=β=1):
```
min_x  TL̃(x) = α·µᵀx + β·xᵀΣ̃x   s.t. Σx_i = K,  x ∈ {0,1}^N
```
Evaluate final quality with the ORIGINAL TL (µᵀx + √(xᵀΣx) structure) — never report on the modified objective.

### QUBO transform (cardinality as penalty)
```
Q = βΣ̃ + δ·11ᵀ + diag(αµ − 2δK·1)
QCBO + δ(1ᵀx − K)² = xᵀQx + δK²
```
**This work sets δ=0**: the quantum stage solves an unconstrained relaxed scoring problem; cardinality enforced exactly by deterministic top-K post-processing (set top-K probabilities to 1, rest to 0). This guarantees feasibility regardless of VQA output.

## Pauli Correlation Encoding (PCE) for Qubit Efficiency

**Core idea**: encode N binary variables in expectation values of non-identity n-qubit Pauli operators instead of one qubit per variable.

```
n-qubit non-identity Pauli count = 4ⁿ − 1
qubit requirement:  n = ⌈log₄(N+1)⌉ + m   (m ≥ 0 extra qubits for expressibility; this work m=0)
```
- Randomly select N non-identity Pauli operators {P₀..P_{N−1}}, each P_i = ⊗_a σ_a^(i), σ ∈ {I,X,Y,Z}
- Variable value from measurement: `x_i(θ; γ) = (1 + tanh(γ·⟨θ|P_i|θ⟩))/2 ∈ [0,1]`
- Pauli expectation constraints: ⟨P_i⟩ values are NOT independent (polynomial equality/inequality constraints — cannot all reach ±1 simultaneously); γ-annealing pushes toward binary limits

### Three-subgroup PCE (hardware-executable variant)
Full PCE: selected Pauli operators may span up to 2n+1 commuting measurement subgroups → measurement overhead on hardware. Restrict to tensor products of:
```
{I,X}ⁿ → 2ⁿ−1 ops;  {I,Y}ⁿ → 2ⁿ−1 ops;  {I,Z}ⁿ → 2ⁿ−1 ops
Total: 3(2ⁿ−1) operators;  n′ = ⌈log₂(N/3 + 1)⌉
```
Result: solution quality comparable to full PCE (gap ~40% vs OR-Tools across N=20..1000), but hardware-measurable with only 3 measurement settings. Tradeoff: n′ ≥ n → longer classical simulation runtime.

## VQA Architecture

1. **Ansatz**: Qiskit EfficientSU2 (hardware-efficient): alternating Ry(θ_a^l), Rz(ϑ_a^l) single-qubit rotations + linear-nearest-neighbor CX(a, a+1) entanglers, L layers
2. **Optimizer**: COBYLA (SciPy), classical outer loop
3. **Annealing schedule**: γ increased geometrically 0.3 → 50 over epochs (binarization)
4. **Stabilization**: exponential moving average of best parameter vector, updated when current discrete-solution QUBO cost within 10% of best
5. **Feasibility**: top-K thresholding after optimization (δ=0 path)

QPU time scaling (EfficientSU2): `T_QPU ≈ ((2n′(L+1) + 3) × epochs + 1) × t_QPU` where t_QPU = time for all N Pauli expectation estimates. Hardware runs: 10 layers, 6 epochs.

## Empirical Results (real microfinance dataset, 2012 borrowers, 26 months)

| Comparison | Setting | Result |
|---|---|---|
| VQA sim vs OR-Tools (LCBO linearization + CP-SAT) | N ∈ {20..1000}, K=N/2, equal time budget | VQA objective ~40% HIGHER (worse) than OR-Tools, consistent across sizes |
| IBM hardware vs simulation | N ∈ {20, 400, 1000, 1500} | hardware objective within 10% of simulation |
| VQA vs brute force | N=20, K=10 (C(20,10)=184,756 portfolios) | VQA near-optimal, low-covariance borrowers selected (visual diversification) |

**Honest framing**: NO computational advantage over OR-Tools established. The contribution is representational scale — 1500 variables on ≤~11 qubits (vs 1500 qubits for direct mapping), and hardware fidelity within 10% of simulation. Benchmarks are under matched time budgets, not optimality proofs.

### Weighting note (for balanced objectives)
With α=β=1: expected-loss term has O(K) active terms, covariance term O(K²) — influence shifts with K even after the Σ̃ fix. Balanced weighting: `β_balance = (µᵀ1)/(1ᵀΣ̃1)` equalizes aggregate scales.

## LCBO Linearization (classical baseline for CP-SAT)

OR-Tools CP-SAT needs linear objectives. Linearize quadratic terms with auxiliary binaries z_ij:
```
min α·EL + β Σ_ij Σ̃_ij z_ij   s.t. Σx_i = K;  z_ij ≤ x_i; z_ij ≤ x_j; x_i + x_j − 1 ≤ z_ij
```
(z_ij = x_i·x_j enforced by the three inequalities; z has N² entries.)

## Reusable Patterns

1. **Sign-preserving covariance square root** — combine linear + quadratic risk terms in one scale-comparable quadratic objective without destroying QUBO structure. Generalizes to any expected-loss + covariance portfolio problem.
2. **δ=0 + top-K post-processing** — decouple relaxed quantum scoring from exact cardinality feasibility; the quantum stage never needs to learn the constraint.
3. **γ-annealing with EMA stabilization** — geometric γ increase for binarization, EMA on best params gated by 10%-of-best cost band.
4. **Three-subgroup PCE** — restrict to {I,X}/{I,Y}/{I,Z} tensor products: 3 measurement settings, quality parity with full PCE, log₂ compression instead of log₄.
5. **Scorecard-to-PD logistic mapping** — industry-standard β0/β1 from target score/odds/PDO; no ML pipeline needed for reproducible PD estimates.

## Pitfalls

- **Pauli expectation constraints**: x_i values are correlated through quantum state geometry — cannot be treated as independent relaxations; large γ too early destabilizes optimization.
- **Modified objective ≠ true objective**: Σ̃ is NOT a standard risk measure; always evaluate/report on original TL.
- **Simulation vs hardware**: noiseless simulation misleading — this work shows ≤10% gap on real QPUs at ≤1500 variables, but deeper ansätze (10 layers) were needed for hardware runs.
- **PCE compression vs trainability**: representational capacity grows exponentially with qubits, but how VQA trainability evolves far beyond 1500 encoded variables is open; higher-order PCE may mitigate barren plateaus (see arXiv:2511.21305 line of work).

## Related Work in KG

- id=1109: Large-scale portfolio optimization using PCE (equity PO predecessor)
- id=1638: IQNN-CS interpretable quantum credit scoring
- id=1889: Quantum circuit-based credit risk analysis
- id=1631: Option pricing on NISQ (QNN)
- id=2324/3694: QAOA/DDPG portfolio optimization

## References

- arXiv:2609.30195 — this paper
- J.P. Morgan CreditMetrics; Credit Suisse CreditRisk+ (credit-risk correlation foundations)
- Google OR-Tools CP-SAT — classical benchmark
- Qiskit EfficientSU2 ansatz
