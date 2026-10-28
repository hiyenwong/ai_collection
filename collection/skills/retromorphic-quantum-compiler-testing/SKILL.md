---
name: retromorphic-quantum-compiler-testing
description: RetroQ retromorphic + Hadamard-test validation of quantum compiler passes. Use for QC compiler QA.
category: ai_collection
---

# Retromorphic Testing of Quantum Compiler Passes (RetroQ)

**Paper**: Retromorphic Testing of Quantum Compiler Passes (arXiv:2610.11195, Khan & Di Matteo, UBC, Oct 2026). Framework: github.com/... (RetroQ, PennyLane + Qiskit backends)

## Problem: Test Oracle for Compiler Passes

Verifying a quantum compiler pass ζ(F) is correct requires knowing the expected output of a possibly large, deeply entangled circuit — computationally intractable (test oracle problem). Existing unit tests across PennyLane/Qiskit/Cirq/pytket are dominated by **program-content assertions (40–62%)** and **program-metric assertions**, with test circuits that are tiny: 95%+ have depth 1–10, most under 50 qubits. Bugs that only manifest in larger circuits go uncaught.

## Method: Two-Stage Retromorphic Verification

Retromorphic testing exploits the forward/inverse dual-program structure: for quantum circuits every operation is unitary, so **the inverse is always available for free** (circuit adjoint). Model pass correctness as two predicates:
- **Semantic**: F ≡ F′ (identical outcomes up to tolerance and global phase)
- **Structural**: m(F′) ∗ m(F) for metric m (gate count, depth), ∗ ∈ {<, ≤, =, ≥, >}

**Stage 1 — Adjoint identity check**: build circuit `Init† · F† · F · Init`; all qubits must return to |0⟩. Then apply the pass two ways — ζ(F†) and ζ(F)† — and check both semantic return-to-|0⟩ and structural expectations against the untransformed baseline. Testing passes on adjoints matters: adjoints appear in uncomputation and reversible subroutines, and pass behavior differs on adjoint representations.

**Stage 2 — Controlled adjoint identity check (Hadamard test)**: embed F†·F inside a controlled operation with an auxiliary qubit in a Hadamard-test circuit; the auxiliary must measure ⟨Z⟩ = +1. Apply the pass inside the control three ways (control(ζ(F)†), ζ(control(F))†, …). **This catches global-phase bugs**: a GlobalPhase gate that is harmless in isolation becomes a physically significant *local* phase when the circuit is controlled — RetroQ observed ⟨Z⟩ = −1 instead of +1 (PennyLane single_qubit_fusion on adjoints).

## Five Bug Classes That Evade Existing Tests (found/replicated, 6 bugs total)

1. **Symbolic reasoning limitation** — Qiskit RemoveIdentityEquivalent fails to remove `ry(d*0)` (symbolically zero angle); also affects RZ/RX (Issue #6468 pattern).
2. **Abstraction gap** — PennyLane cancel_inverses *crashes* (numpy ambiguous truth-value) on QubitUnitary + adjoint pairs, because inverse-detection compares gate parameters with plain equality.
3. **Structural logic error** — Qiskit CommutativeInverseCancellation incorrectly commutes SWAP through Controlled-RZ (non-commuting!) then cancels the swaps (Issue #16164).
4. **Global phase management error** — pass emits GlobalPhase; harmless standalone, sign-flips expectation when nested in controlled context.
5. **Adjoint logic failure** — pattern-matching optimization fails to match H†Z†H† against an HZH pattern of self-adjoint gates.

## Reusable Protocol for Testing a Compiler Pass

1. Define target function F and its adjoint F† (framework-dependent).
2. Declare `Expectation(gate_count='decrease'|'unchanged'|'increase')` for the pass's intended structural effect.
3. Run Stage 1 (ζ(F†), ζ(F)† vs baseline) → catches structural + adjoint-handling defects.
4. Run Stage 2 (three controlled variants vs Hadamard baseline) → catches global-phase-in-control defects.
5. Compare failure reports: `{stage, detail, differences:{gate_count, expectation_value}}`.

**Known blind spot**: with Identity initialization, a pass could permute gate order while preserving |0⟩ return AND gate count (e.g. reorder SWAP·CRZ·SWAP); a non-trivial initialization state (e.g. Hadamards) would expose it. Choosing initialization functions is open future work.

**Generalization**: backend-agnostic (needs only F, F†, ζ) → applicable to quantum arithmetic modules, uncomputation subroutines, QEC encoding circuits, and hardware runs via statistical output checks.

## Testing-Taxonomy Findings (for audit work)

AST-based static analysis of assert statements in 200 test files: PennyLane is the only framework testing **gradient equivalence** (differentiable programming); pytket is metric-heavy (50.88%); Cirq is matrix-equivalence-heavy (21.35%); Qiskit output-equivalence coverage is 0.06% — nearly nobody verifies the compiled output is equivalent.
