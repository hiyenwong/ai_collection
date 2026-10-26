---
description: Use when bounding magic-state distillation input counts.
name: magic-distillation-code-limits
category: ai_collection
version: 1.0
author: quantum-cron-2026-10-26
license: MIT
metadata:
  hermes:
    tags: [magic-state-distillation, stabilizer-codes, fault-tolerant-quantum-computing, lower-bounds, postselection, complement-symmetry, resource-estimation, ccz, t-gate]
    related_skills: [syndrome-mediated-deterministic-t-gates, logical-catalyst-dyadic-phase, magic-rectangle-rigidity, borrowed-identity-magic-distillation, magna-magic-factory-tensor-network]
---

# The Limits of Magic-State Distillation

Methodology from arXiv:2610.31115 — "The limits of magic-state distillation" (Balada Gaggioli & Mareček; CTU Prague + LAAS-CNRS; quant-ph, 22 Oct 2026).

## One-Line Summary

Any stabilizer distillation protocol — however adaptive, postselected, or multistage — collapses to a single stabilizer-code projection (Thm 1), and for rational targets (CCZ, CS) a fault pattern is harmful exactly when its complement is (Thm 2). Exhaustive code search with exact arithmetic then gives **exact minimal noisy-input counts**: 9 inputs for quadratic T distillation, the 8-input CCZ factory is provably optimal, 10 for cubic CCZ, and n ≥ 2d (T) / n ≥ 2d+1 (rational targets) at every order.

## When to Use / Activation

- Bounding how many noisy magic states a factory must consume per accepted output (input-count floors for resource estimates).
- Deciding whether an adaptive/multistage/postselected protocol can beat a known code-based factory (answer: no, within stabilizer ops).
- Designing or certifying small magic-state factories (T, CS, CCZ, CCZ⊗2, CCCZ).
- Translating "tolerating input faults" into a finite combinatorial/code-search problem in other fault-tolerance settings.

## Core Reductions (the reusable machinery)

**Setup.** n noisy inputs ρ_T(p)^⊗n = Σ_e w_e ρ_e with fault pattern e ∈ F₂ⁿ, orthonormal |φ_e⟩ = Z^e|T⟩^⊗n, weights w_e = p^|e|(1−p)^(n−|e|). Protocol = stabilizer ops (Clifford gates, ancillas, Pauli measurements, feedforward, randomness, postselection, any stages) → accepted map Λ, independent of p. Damage h_e = Tr[(I−Π)Λ(ρ_e)] ≥ 0; **harmless** iff h_e = 0. Suppression order d (error O(p^d)) ⟺ every pattern |e| < d is harmless (given the fault-free pattern is accepted).

**Theorem 1 (protocol → code, "collapse").** For a target τ with stabilizer nullity ν(τ) = r (no Pauli fixes it), tolerating a pattern set H ∋ 0 ⟺ ∃ stabilizer code C on the n inputs + Clifford encoder U with Π_C|φ_0⟩ ≠ 0 and Π_C|φ_e⟩ ∈ CU|τ⟩ (or = 0) for all e ∈ H. Every Kraus branch is a code projection followed by a Clifford isometry. In Gram-matrix form: G_00 > 0 and G_00·G_ee = |G_0e|² — polynomial conditions checkable in exact arithmetic. (Extends Campbell–Browne and Beverland et al. normal forms to all fault patterns at once.)

**Theorem 2 (complement symmetry for rational targets).** If all Pauli expectations of τ are rational (dyadic; true for phase states CCZ, CS, CCCZ; NOT |T⟩), the field automorphism σ: √2 → −√2 commutes with stabilizer operations, fixes τ, and maps ρ_T(p) → ρ_T(1−p), hence ρ_e → ρ_(ē). Therefore **e harmless ⟺ ē harmless**: harmlessness is symmetric under reflection of |e| about n/2, so only patterns d ≤ |e| ≤ n−d need tolerating. This halves the constraint set and eliminates candidate codes en masse.

**Search.** Enumerate stabilizer codes on n inputs with Clifford-orbit symmetry reduction and exact arithmetic (largest run: 9×10¹¹ signed codes). Lower bounds by exhaustion; upper bounds from explicit factories found by ILP/SAT and certified in exact arithmetic. Higher-order designs compose two levels (quartic CCZ: 48 inputs, leading coefficient 864 vs prior 2816).

## Exact Results Table (n_min = fewest noisy T inputs per accepted output)

| Target | d | n_min | Note |
|---|---|---|---|
| T | 2 | **9** | no 8-input protocol exists; new 9-input factory, acceptance 1/128 (prior best 10) |
| T | 3 | 10 ≤ n ≤ 15 | LB new; UB Bravyi–Kitaev |
| T | 4 | 11 ≤ n ≤ 48 | |
| T | ≥6 | n ≥ max(2d, d+7) | analytic |
| CS | 1 | 3 | |
| CS | 2 | **8** | prior UB was 12 |
| CS | 3 | 9 ≤ n ≤ 35 | |
| CCZ | 1 | 4 | |
| CCZ | 2 | **8** | the standard 8-input factory is optimal over ALL stabilizer protocols |
| CCZ | 3 | **10** | 36-input factory, leading coeff 120 vs prior 47-input coeff 236 |
| CCZ | 4 | 11 ≤ n ≤ 48 | 48-input, coeff 864 vs 2816 |
| CCZ⊗2 | 1 | 8 | |
| CCZ⊗2 | 2 | 10 ≤ n ≤ 14 | |
| CCCZ | 1 | 6 | matches the 6-copy result |

General floors surviving arbitrary postselection (first bounds beyond max(d, ν)): **one T state needs n ≥ 2d; any non-stabilizer rational target needs n ≥ 2d+1.**

## How to Use in Resource Estimation

- Treat n ≥ 2d (T) / n ≥ 2d+1 (rational) as hard input floors; no protocol redesign can beat them.
- Don't search for cleverer small-d factories below the certified minima — the space (within stabilizer ops) is exhausted.
- Account for acceptance probability when comparing factories (counts are per ACCEPTED run; the 9-input T factory accepts 1/128 on ideal inputs).
- When a new "better" small factory is claimed, check it against Thm 1/2 collapse: reduce to a code, verify Gram conditions exactly.

## Limitations / Assumptions

- Clifford operations ideal; counts inputs, not gates or time; independent input faults; stabilizer protocols only (non-stabilizer distillation could in principle do better — open).
- ν(τ) = r assumption in Thm 1 (target fixed by no non-identity Pauli); deterministic-protocol bounds (e.g., Bravyi–Kitaev-style) are stronger but don't survive postselection.

## References

- arXiv:2610.31115; builds on Campbell & Browne (2012), Beverland et al. (2021), Bravyi–Kitaev 15-to-1, Jones 8-input CCZ factory, Meier et al. 10-input T.