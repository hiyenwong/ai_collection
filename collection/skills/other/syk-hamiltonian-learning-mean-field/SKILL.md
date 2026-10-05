---
name: syk-hamiltonian-learning-mean-field
description: Learn dense mean-field Hamiltonians from Gibbs states.
category: ai_collection
tags: [quantum-machine-learning, hamiltonian-learning, syk, gibbs-state, mean-field, strong-convexity, wick-expansion, kotecky-preiss, bogoliubov-kubo-mori, quantum-chaos]
---

# SYK Hamiltonian Learning via Mean-Field Structure

**arXiv 2610.02178** (2026-10-01) — Anshu, Arunachalam, Chen, Hwang (Harvard/IBM). First constant-temperature Hamiltonian-learning guarantee for a **dense, random, noncommuting mean-field ensemble**: the quartic Sachdev–Ye–Kitaev (SYK) model, where every interaction overlaps Θ(n³) others and locality/bounded-degree tools (Lieb–Robinson, [HKT22] degree-based high temperature) provably do not apply.

## When to Use
- Learning couplings of an all-to-all / dense random Hamiltonian from Gibbs-state (thermal) copies
- Quantum simulator calibration & verification when interaction graph is NOT local
- Testing whether "learnability" survives loss of locality — random mean-field disorder substitutes for it
- Extending classical disordered-magnet learning (Sherrington–Kirkpatrick) results to the quantum noncommuting setting

## Core Methodological Pattern

### 1. Maximum-entropy reduction (sample-efficient algorithm)
Learning reduces to **strong convexity of the log-partition function** Φ(h) = log Z(β, h) at the true coupling vector g:

1. Quartic Majorana expectations μ_{β,I} = Tr[ρ_β Γ_I] form a **sufficient statistic** — they uniquely determine g.
2. Solve the convex program L(h) = Φ(h) + βσ_n h·μ_{β,meas}; true g is the unique minimizer (∇Φ(g) = −βσ_n μ_β).
3. **Stability via strong convexity**: if ∇²Φ(g) ⪰ λ_n I and the Hessian is Lipschitz, then Φ stays (λ_n/2)-strongly convex in a ball of radius λ_n/poly(β) around g — convexity AT the random target suffices; no uniform bound needed.
4. Boundary argument converts ‖μ_meas − μ‖₂ ≤ min(λ_n²/(8βσ_n), λ_n ε/(16β_n poly(β))) into ‖g_meas − g‖₂ ≤ ε.

**Key substitutions replacing locality** (the transferable tricks):
- **Bogoliubov–Kubo–Mori (BKM) covariance** identity relates ∇²Φ to ordinary variance with loss controlled only by the **spectral diameter** — replaces the quasi-local-operator + local-twirl machinery of [AAKS20].
- **Local-quench ratio** R_{p,A} = Z_A(β,s,g)/Z(β,g) (a Petz Rényi power between Gibbs state and its Γ_A-conjugate) replaces energy-leakage bounds of [AKL16]; balancing the number of nonzero Gaussian pairings (Wick/Isserlis counting) against SYK normalization σ_n = √(6/n³) bounds thermal leakage.
- **Wick expansion + Kotecký–Preiss polymer expansion** controls partition-function moments; annealed→quenched passage via a commutation-index + Gaussian-concentration argument.

**Result**: N = n^{O(1+β)} ε⁻² log(n/ζ) copies at ANY fixed β > 0, w.h.p. over disorder. Extends to all even q.

### 2. First-order inversion (quasi-polynomial-time algorithm)
Directly invert the (rescaled) expectation map instead of solving the max-entropy program:
- After rescaling by βσ_n, U_{β,I}(g) = g_I − (βσ_n/2)Σ_{J1△J2=I} χ(I;J1,J2) g_{J1} g_{J2} + O(β²): **identity at linear order**, with a quadratic bias of L2 scale Θ(n^{-1/2}) per coordinate that must be canceled.
- **Low-degree polynomial proxy**: replace the random denominator Z(β,g) = Z_ann(β)(1+Δ_β) via Taylor (1+Δ)^{-1} ≈ 1−Δ, truncate β-expansion at degree K = O(log n) → proxy V_{β,I} is a Gaussian polynomial of degree O(log n).
- **Weighted moment bound** ‖Δ_β‖_{2,s} ≤ C_s n^{-1} for every fixed s (take s = 15 → Gaussian hypercontractivity controls all L_p up to p = 16) — stronger than the known second-moment estimate, needed because error terms like Δ_β² U_{β,I} enter quadratically.
- **Low-degree calibration** isolates and cancels the leading quadratic contribution; remainder handled by zero-freeness estimates for the truncated series.

**Result**: N = O_β(n^{13} log(n/ζ)) copies, runtime n^{O(log n)}, ℓ2 error n^{-c} at small constant β.

## Complexity Landscape (context table)
| Regime | Tool that fails | Replacement |
|---|---|---|
| Local Hamiltonians [AAKS20] | Lieb–Robinson locality | — works |
| Bounded degree, β = n^{-Ω(1)} [HKT22] | degree-dependent high-temp condition | fixed β needs mean-field |
| Dense SYK (this paper) | ALL of the above | BKM covariance + quench ratio + Wick/KP expansion |

## Why It Matters
- SYK is the canonical strongly-chaotic quantum model; learnability despite chaos reveals structure (conjectured NO replica-symmetry-breaking phase transition, vs SK model's β=1 transition).
- Quantum analogue of learning undirected graphical models — but without the graph.
- Direct applications: calibration/verification of analog quantum simulators, extraction of effective microscopic models from thermal data.

## Implementation Sketch (pseudo-algorithm)
```python
# Sample-efficient SYK learning
# 1. Measure quartic Majorana expectations from Gibbs-state copies
mu_meas[I] = mean(copy_measurement(Γ_I))   # Γ_I are ±1-valued → poly samples suffice
# 2. Solve convex program over compact set K ∋ g:
#    minimize_h  log Z(β, h) + β σ_n h·μ_meas
#    (strong convexity at g w.h.p. over disorder guarantees stability)
# 3. Output argmin as g_hat;  ||g_hat − g||₂ ≤ ε
```

## Related
- [[lindbladian-structure-learning]] — learning local Lindbladians (locality-based counterpart)
- [[sample-optimal-gaussian-state-learning]] — Gaussian analogue
- [[near-optimal-lindbladian-learning]] — open-system version
- [[hypergeometric-high-precision-evaluation]] — classical counterpart traditions
- SK model learning line [AJKPV24; GM24; CK25] — classical 2-local disordered magnets, learnable even past phase transition

**Activation keywords**: SYK, Sachdev-Ye-Kitaev, Hamiltonian learning, Gibbs state, mean-field, all-to-all, dense interactions, strong convexity, log-partition function, Bogoliubov-Kubo-Mori, Kotecky-Preiss, Wick expansion, polymer expansion, Petz Renyi power, thermal inverse problem, quantum simulator calibration
