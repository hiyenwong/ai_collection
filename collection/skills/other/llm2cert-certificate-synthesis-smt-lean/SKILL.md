---
name: llm2cert-certificate-synthesis-smt-lean
description: Use when LLM+Lean verifies Lyapunov/barrier certificates.
category: ai_collection
trigger_words: [lyapunov, barrier certificate, certificate synthesis, SMT, Lean, formal verification, safety verification, stability, counterexample-guided, proof repair, dynamical systems]
source_paper: "arXiv:2610.30524 (LLM2Cert, Cao/Song/Vertovec et al., Oct 2026)"
---

# LLM2Cert: LLM Certificate Synthesis with SMT/Lean Verification

Source: arXiv:2610.30524 — LLM-driven end-to-end synthesis AND verification of Lyapunov functions and barrier certificates for nonlinear dynamical systems. Verifies 81/105 DYNACERTBENCH instances (77.1%), vs 11-19/51 for prior pipelines under strict conditions. Code: github.com/FormalCert-AI/llm2cert.

## Core Idea

LLMs PROPOSE symbolic certificates; SMT solvers and Lean DISCHARGE the proof obligations. The candidate is **never relaxed** — only proofs are searched. Soundness is two-layer:
1. **Condition→theorem layer**: every certificate-condition-to-theorem implication is proven once in Lean and kernel-checked (stability/ROA/invariance/safety theorems).
2. **Candidate→condition layer**: a candidate is accepted only when EVERY obligation is discharged by an SMT `unsat` verdict or a kernel-checked Lean proof.

End-to-end guarantee chain: proposed candidate → LLM2CERT → verified candidate → Lean → theorem holds.

## Pipeline (5 stages)

1. **Proposal Agent**: proposes typed symbolic certificate W (+ policy π for controlled systems). Format check parses into typed expression tree; parse errors fed back.
2. **Obligation list**: instantiate the task's certificate theorem at the candidate → one obligation per theorem premise, RETAINING original domain/boundary/parameter constraints (no relaxation, no excluded neighborhoods, no δ-tolerance).
3. **Fast screening**: evaluate each obligation on finite sampled states. Violation → candidate rejected, violating samples returned as counterexamples. (Passing screening guarantees nothing — screening only rejects.)
4. **Verification Router** (per obligation): 
   - No compatible SMT encoding (e.g. radial unboundedness over unbounded domains) → direct Lean.
   - Else direct SMT: Z3, cvc5, Yices, dReal; counterexample query ∃z: P(z) ∧ ¬Q(z); timeout 30 s/obligation.
   - SMT outcomes: `unsat` = verified; `sat` = counterexample → next candidate; `δ-sat` (dReal) = INCONCLUSIVE (weakened query — neither refutes nor verifies) → escalate; timeout → escalate.
5. **Lean Proof-Repair Agent**: builds fixed Lean context + theorem statement from candidate/obligation; LLM generates ONLY the proof body (statements immutable). Each attempt elaborated in pinned Lean environment. Failed attempt → **structured repair feedback**: classified failure (unknown identifier / application type mismatch / unsolved goal), source location, remaining goal, and Mathlib lemma declarations matching unknown identifiers. Acceptance audit rejects `sorry` and any nonstandard axioms. Budget: ≤6 rounds, 900 s/obligation.

**Outer loop**: rejected/unresolved candidates return counterexamples + failure diagnostics to the Proposal Agent for candidate k+1. Budgets: ≤5 candidates, 2400 s/system total.

## Key Empirical Findings (DYNACERTBENCH, 105 instances)

- Feedback loop value: one-shot proposal 63/105 → full framework 81/105 (+17.1 pp overall; +15/27/21 pp on literature/extended/new tiers).
- **Backends are complementary, neither suffices alone**: SMT-only 57/105, Lean-only 60/105, routed full 81/105.
- Fixed-candidate analysis (81 certificates, 296 obligations): All-SMT 59/81, All-Lean 64/81, Routed 81/81. SMT verified 253/296 obligations (85.5%); only 43 (14.5%) needed Lean: 21 after δ-sat/timeout, 19 router-direct, 3 no-SMT-encoding.
- **Lean's exclusive value is on non-polynomial systems**: Lean 34/40 vs SMT 18/40 non-poly; on polynomial systems SMT covers everything Lean does, ~500× faster (1.65 s vs 512 s mean).
- **Structured repair feedback is decisive**: repairs 21/26 failed obligations vs 17/26 with raw compiler diagnostics vs 1/26 with generic retry; also fewer rounds (2.19) and less time (407 s).
- Prior pipelines' native certificates often fail strict recheck (of 19 native successes only 11 survive unrelaxed conditions — 4 were δ-sat-only, 4 SOS certificates failed strict recheck). Do NOT count δ-sat as verification.

## Reusable Design Patterns

1. **Propose-then-discharge with immutable obligations**: compile the candidate to a typed expression tree, derive obligations from theorem premises, then hold BOTH candidate and obligations fixed while searching only proofs. Prevents goal drift.
2. **Per-obligation capability routing**: route each proof obligation to the backend whose expressive fragment covers it; escalate δ-sat/timeout to the stronger (slower) backend. Route by syntactic class (nonlinear transcendental → Lean; polynomial/rational → SMT).
3. **Screening before proving**: cheap sampled falsification first; only survivors go to expensive solvers. Counterexamples are the feedback currency.
4. **Structured compiler feedback for proof repair**: classified error + location + remaining goal + candidate lemma declarations beats raw logs and generic retries by 20×.
5. **Soundness audit**: kernel-check every accepted proof; reject placeholders (sorry) and nonstandard axioms — LLM proof output is untrusted until kernel-checked.
6. **Benchmark design principle**: do not tailor benchmarks to solver limits (prior suites were dominated by low-dim polynomial systems "chosen to suit what solvers can handle rather than what engineering applications require"). DYNACERTBENCH = 80 literature systems + high-dimensional, control-constrained, nonlinearly-coupled extensions, spanning stability / region-of-attraction / forward-invariance / safety.

## Applicability Beyond Control

The pattern (LLM proposes symbolic object → obligations generated from a fixed theorem schema → cheap falsification screen → per-obligation SMT/Lean routing → structured proof repair → counterexample feedback) transfers to any domain with machine-checkable proof obligations: invariant synthesis for programs, protocol verification, type-class instance synthesis, geometry theorem certificates, differential privacy budget proofs.

## Pitfalls

- δ-sat is NOT verification (dReal's δ-weakened query says nothing about the original). Escalate, don't accept.
- SMT-only feedback can underperform even one-shot proposal (57 vs 63 on the benchmark) — the counterexamples from a weak backend can mislead candidate search. Complementarity, not replacement.
- All-Lean is expensive (~500 s/system even where it succeeds); routing keeps mean time near SMT's while covering Lean's exclusive wins.
- Implicit vs explicit closed-loop: verify against a specific feedback policy u=π(x) (∀x∃u admissibility is a different, weaker claim).
