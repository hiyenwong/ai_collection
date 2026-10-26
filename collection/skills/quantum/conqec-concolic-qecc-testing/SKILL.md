---
name: conqec-concolic-qecc-testing
description: "Use when testing or debugging QEC decoder-recovery stacks."
category: ai_collection
version: 1.0
author: info-cron-2026-10-25
license: MIT
metadata:
  hermes:
    tags: [quantum-error-correction, concolic-testing, fsdr-witness, software-testing, fault-localization]
    related_skills: [syndebug-ftqc-assertion-debugging, failure-guided-quantum-fuzzing, qusema-semantic-oracle-bug-detection, agentic-verifiable-quantum-compilation]
---

# ConQEC: Concolic Testing for QECC Implementations

Methodology from arXiv:2610.31443 (Zihao Li, Ji Guan, Mingsheng Ying — CAS Institute of Software + UTS; accepted at ICSE 2027). First concolic testing framework for quantum error-correcting code (QECC) implementations. Scales concolic testing to thousand-qubit codes while returning replay-backed, fault-localizing bug witnesses. Artifact: github.com/Hikari-HN/conqec-qse-artifact.

## The Problem

QECC stacks are hybrid software-control pipelines: syndrome extraction produces classical bits → decoder software dispatches a correction → recovery applies it → logical check verifies. A code theorem can be correct while the implementation reads a stale syndrome register, aliases a decoder arm, or recovers at the wrong qubit. A final logical-check failure does not say WHERE the repair path first diverged.

Prior coverage gap:
- Formal tools (QSE PLDI'24, QECV, Veri-QEC, CAV'25 fault-tolerance verification) prove obligations but give no budgeted test generation or developer-facing bug reports.
- Quantum Concolic Testing (QCT, ISSTA'25) is amplitude-based: tracks 2^n state space → evaluated only below 5 qubits.

## Core Design: Two Ideas

**Idea 1 — Test = FSDR repair path + paired-replay evidence contract.** A test is a staged trace τ = ⟨F, σ̄_impl, d_impl, r_impl, ω⟩: injected Pauli fault F, syndrome evidence, decoder decision, recovery action, oracle result. A candidate becomes a bug witness w_bug = ⟨F, σ̄, d_impl, d_ref, r_impl, r_ref, ω, δ⟩ only after replaying the SAME fault on both implementation and reference contract. δ = earliest divergent stage. Acceptance rule: **ω = FAIL ∨ δ ≠ ⊥** — report even when the final oracle accidentally passes but a stage diverged (masked-bug detection).

**Idea 2 — Symbolic repair-path model, not a state vector.** S = ⟨f̂, Φ_F, {s_c}, D, R⟩:
- Fault atoms α_i (legal Pauli injection site + effect) with Boolean indicators f̂_i; legal domain Φ_F (e.g. at-most-one: Σf̂_i ≤ 1).
- Each check predicate as affine parity: s_c(f̂) = β_c ⊕ Σ_{i∈N(c)} f̂_i — a check flips iff an ODD number of selected faults touch it (N(c) = support, β_c = clean-run value). One model compactly represents the whole fault space; solve for targeted behavior without enumerating concrete faults.
- Decoder relation D(σ,d) and recovery relation R(σ,d,r) only when derivable from source/spec; otherwise do NOT invent them — those fields stay replay-observed.

## Five Bug Classes (stage-ordered; first applicable wins)

1. Syndrome extraction error: σ_prod ≠ σ_ref.
2. Measurement register misuse: σ_prod = σ_ref ∧ σ_use ≠ σ_prod (syndrome produced correctly but later software reads stale/wrong/offset register — invisible to final oracles).
3. Decoder misdispatch: σ_use = σ_ref ∧ d_impl ≠ ⊥ ∧ d_impl ≠ d_ref.
4. Unhandled syndrome: σ_use = σ_ref ∧ d_impl = ⊥ ∧ d_ref ≠ ⊥.
5. Recovery contract violation: d_impl = d_ref ∧ (r_impl ≠ r_ref ∨ ω = FAIL).

The produced/consumed/expected triple ⟨σ_prod, σ_use, σ_ref⟩ is the localization key: distinguishing the value a stage wrote from the value the next stage actually read catches register bugs that outcome checks cannot.

## Objective Layers (QECC analogues of classical coverage)

| Layer | Classical analogue | Obligation |
|---|---|---|
| O_B measurement outcome | branch coverage | (c, b): predicate c reaches value b |
| O_C stabilizer condition | condition coverage | (c, k): µ_c(F) = k — HOW MANY selected faults touch check c |
| O_TS transition sequence | path fragment | ordered pairs (σ,d), (d,r) |
| failure-directed | bug-directed path | D_impl(σ) ≠ D_ref(σ), D_impl(σ)=⊥, R_impl ≠ R_ref |

SMT query per objective: q_o = Φ_F(f̂) ∧ Φ_σ(f̂,σ) ∧ Φ_o, plus blocking clauses excluding already-replayed faults. UNSAT → drop objective; SAT → materialize concrete fault F = {α_i : ν(f̂_i)=1}, then validate by paired replay. Replay is the ONLY source of coverage credit and witness acceptance.

**Pair-mask insight**: two faults on both support qubits of a check cancel in parity — identical outcome to no fault. Outcome coverage cannot see this; the (c, k=2) condition layer can.

## Algorithm (loop)

1. Build symbolic model; run paired replay on clean seed F₀ = ∅ (catches bugs reachable without faults); init test set T, witness set W.
2. While budget remains and uncovered objectives exist: pick objective → SMT query for an unseen fault → materialize → paired replay on impl + ref → record traces, compute ω and δ → update covered obligations → accept witness if ω=FAIL ∨ δ≠⊥.

## Verified Results

- **Localization (195 mutants = 13 configs × 15 seeded mutations, 5 families)**: ConQEC 156/195 by budget B=2, 195/195 by B=4. Trace-order concolic (same symbolic machinery, branch order only): 0 by B=4 — the failure-directed guidance is the differentiator, not symbolic execution per se. Random: 15.7/195 at B=4. Largest witness: 1500 qubits / 1499 checks (repetition); 1058q surface/toric; 1000q Tanner/LDPC.
- **Hard-coverage separation (pair-mask, weight-2 faults, B=n/2)**: ConQEC 44.4/49.5/49.9% at n=10/100/1000 vs random 8.89/0.61/0.10%. Random dilution law: obligations grow ~n but legal pairs grow ~n², so uniform sampling coverage ≈ s/|F₂| decays ~1/n. Solve directly for µ_c(F)=k to escape dilution. Random stays competitive on shallow outcome coverage — directed effort only pays on condition/transition layers.
- **Scale/cost**: full campaigns complete at repetition n=3000 (2842.8s), surface d=41 = 3362q (957.5s); single objectives still complete at n=5000 / d=51. Phase split: solver/backend dominates (median 1.07s, p95 47.95s per query); paired replay median 0.194ms = 0.0016% of wall time. **Scaling boundary is repeated SMT solving, not replay** — optimize query count/cost, not the simulator.
- **Public artifacts**: Tesseract (173 non-REPEAT Stim subjects): 40,798 fault inputs → 326 order-only differences (caused by order-sensitive comparison — fix comparison semantics to avoid false diagnostics) + 36 logical disagreements. PyMatching historical parent/fixed regression: no-hint generation from public contract objectives reaches the regression at the 5th generated test; 24/32 candidate syndromes expose the parent/fixed difference.
- Stack: QSE symbolic-stabilizer backend (PLDI 2024), Julia QuantumSE, Z3 4.12.4.

## Transferable Patterns (beyond QECC)

1. **Parity/affine abstraction**: any system where an event flips a check iff an odd number of selected causes touch it (fault injection, feature flags, alarm systems, parity checks) admits the s_c = β_c ⊕ Σf̂_i symbolic model — exponential concrete space, linear-size formula.
2. **Produced vs consumed vs expected triple**: instrument each pipeline stage with the value it wrote AND the value the next stage read; compare both against the reference. Catches stale-register/stale-cache reads that end-to-end oracles mask.
3. **Solver-proposes/replay-disposes**: never trust solver output as evidence; promote to bug only after concrete paired replay (impl vs reference) and accept on failure-OR-divergence to catch masked bugs. Solver speed (1s/query) is the budget bottleneck; make replay sub-ms.
4. **Semantic over shallow coverage**: outcome/branch coverage is random-competitive; the return on directed solving is condition-level multiplicity (how many causes per check) and ordered transitions. Before investing in symbolic machinery, ask which layer your current random tests cannot reach.
5. **Obligation/domain dilution check**: count obligations O vs input-domain size |F|; if |F| grows superlinearly in the scale parameter while budget grows linearly, random coverage decays predictably (~s/|F|) — enumerate obligations and solve for each directly.
6. **No-hint differential regression replay**: generate candidate inputs from the public contract of a fixed bug, replay on parent vs fixed commits — finds the regression without being told the failing case.

## Limitations (as reported)

Seeded-mutant study measures generation/localization capability, not natural bug prevalence. Coverage experiment limited to repetition codes with weight-2 X faults. Scale results are empirical (backend + timeout dependent), not asymptotic. Tesseract logical disagreements establish behavioral difference, not fault assignment. REPEAT blocks (temporal history) and history-dependent bugs need history predicates — unhandled. Transition objectives require explicit decoder/recovery relations.

## Position in the Verification Stack

Complements, not replaces: formal verification (fvqkd-rocq-qkd-formal-verification proves protocol-level obligations; QSE/Veri-QEC prove code obligations), runtime assertion debugging (syndebug-ftqc-assertion-debugging), fuzzing (failure-guided-quantum-fuzzing, agentic-verifiable-quantum-compilation certifies failure rates), semantic oracle testing (qusema-semantic-oracle-bug-detection). ConQEC's niche: budgeted test GENERATION over discrete fault spaces with developer-facing stage localization.

## When to Use

- Testing/debugging a QEC stack (custom decoders, Stim/PyMatching/Tesseract adapters) where final logical failures don't localize the bug.
- Designing concolic or symbolic test generation for any hybrid control pipeline with parity-structured checks.
- Deciding coverage criteria beyond branch outcomes (condition multiplicity, ordered stage transitions).
- Building regression-replay harnesses that compare implementation stages against a reference contract without bug hints.
