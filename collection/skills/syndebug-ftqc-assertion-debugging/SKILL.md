---
name: syndebug-ftqc-assertion-debugging
description: Use when debugging logic bugs in fault-tolerant QC programs.
category: ai_collection
version: "1.0.0"
trigger_words:
  - FTQC debugging
  - quantum program assertions
  - logical error rate
  - assert_classical
  - assert_entanglement
  - assert_superposition
  - QEC program bugs
  - stabilizer code debugging
source: arXiv:2610.22275
source_title: "SynDebug: A Framework to Debug Logic Bugs in Fault-Tolerant Quantum Computing Programs"
authors: "DiBrita, Lange, Patel (Rice University / ORNL)"
published: 2026-10-15
arxiv_id: 2610.22275
categories: quant-ph, cs.OS
---

# SynDebug: Assertion-Based Debugging for FTQC Programs

## Overview

arXiv:2610.22275 (DiBrita, Lange, Patel; SIGOPS ATC 2026). First systems-level
debugging framework for fault-tolerant quantum computing programs. Three
user-facing assertion primitives operate directly inside encoded FTQC
execution flows with **zero additional qubits** and 1.8% average circuit-depth
overhead (0% for entangling assertions), with no measurable logical-error-rate
increase. Works across stabilizer-code families (Surface, Color — hex/square-oct,
Tetrahedral, Golay, Steane, Shor), d ∈ {3,5,7}, integrating Stim + MQT QECC + Qiskit.

## When to Use

- Debugging FTQC/QEC-encoded programs whose outputs are semantically wrong but
  which execute without hardware faults (reversed gate order, swapped
  control/target, missing/duplicated gates, wrong parameters).
- Validating logical state preparation, entanglement structure, or arithmetic
  bookends inside encoded execution, before spending shots on full runs.
- Porting NISQ assertion techniques (Huang et al.) into QEC-aware stacks.
- NOT for: formal verification, syntax/compile-time errors, physical-noise
  debugging (QEC layer owns that), or amplitude/phase-sensitive properties.

## The Three Primitives and Their Quantum Semantics

| Primitive | Statistical test | After assertion |
|---|---|---|
| assert_classical(reg, value, basis) | one-sided binomial: H0 = match fraction ≥ q_null | continue if eigenstate |
| assert_superposition(reg) | same binomial, null = most-probable basis state, INVERTED | checkpoint (state destroyed) |
| assert_entanglement(a, b) | contingency-table χ² test of independence | checkpoint (state destroyed) |

**Eigenstate rule** (the physics that makes this cheap): measuring an observable
of which the state is an eigenstate leaves the state unchanged. A register in a
known Z-basis (or X-basis) state survives its assertion → execution continues.
A superposed/entangled register is destroyed → the assertion is a checkpoint
(remove it after the block passes). Prefer assert_classical(basis="X") on a |+…+⟩
control register over assert_superposition: it is stronger (verifies the exact
eigenstate) AND non-destructive.

## Noise Accounting

- Finite-shot noise: inside the binomial/χ² tests (they give confidence bounds).
- Physical noise: corrected by the QEC layer beneath SynDebug.
- Residual logical error rate p_L: fold into the null by LOWERING the expected
  match fraction, q_null = 1 − p_L. FPR = significance threshold (bounded by
  binomial discreteness: at n=100, q_null=0.98, α=0.05 the realized FPR is 0.015);
  shots-to-detection = statistical power of the chosen n.
- Noise model changes the shot budget only — never the API, translation, or
  spatial footprint.

## Systems Design (R1–R5)

1. **R1 Generality**: designed at the stabilizer-code abstraction level (logical
   Pauli operators of any CSS code) → hardware-agnostic (superconducting,
   neutral-atom, trapped-ion).
2. **R2 Zero spatial overhead**: NO dedicated debugging patch/ancilla. Assertion
   measurements use the standard logical-measurement service; ancilla internal to
   that service belong to the hardware primitive.
3. **R3 Minimal temporal overhead**: assertions ride existing QEC measurement
   rounds wherever possible (Table 3: 0% depth for all entangling cases; classical
   avg 1.8%, worst 14.3% for Surface d=3 |p0⟩).
4. **R4 Scalability**: only single-logical-qubit observables, linear in register
   size, sampled in parallel; never tomography, copying, or exponential simulation.
5. **R5 Usability**: developer states logical invariants; SynDebug performs physical
   translation, measurement insertion, statistics, reporting; instrumented counts
   of assertions per region let teams strip checkpoints progressively.

## Implementation Architecture (reusable pattern)

- **CodePatch** = (CSSCode, offset). Arithmetic addressing: data qubits
  [offset, offset+n), then X-ancilla, then Z-ancilla — no lookup tables.
- **PatchRegister** = bump allocator (_next_offset advances by n + |Hx| + |Hz| per
  patch) → non-overlapping patches, stable indices; prepare_logical_state takes
  a per-patch state string s ∈ {0,1,p,m}^L (|0⟩,|1⟩,|+⟩,|−⟩), composes
  non-fault-tolerant heuristic prep circuits, applies logical flips as physical
  X/Z gates on the logical-operator support.
- **QecProgram** = thin wrapper binding register + Stim circuit; compose() appends
  gate gadgets / syndrome rounds.
- Restricted to k=1 codes (1:1 patch↔logical qubit) for unambiguous addressing.
- Dual addressability: logical calls ("X_L on patch 2") translate to physical
  targets via the code's logical Pauli supports.

## Debugging Playbooks (case studies)

1. **Initialization**: assert_classical(register, integer) right after prep; or
   piecewise with later blocks removed to trade shot budget vs per-shot runtime.
2. **Entangling ops** (Algorithm 3): stabilizer_round → transversal_cnot →
   stabilizer_round → assert_entanglement([0],[1]). Buggy CNOT direction
   (control=|0⟩ → no-op, register stays |+0⟩ product) yields independent outcomes,
   χ² ≈ 0 → fails; correct Bell yields χ² ≈ n → passes.
3. **Shor-style workloads** (Algorithm 4): assert_classical bookends the controlled
   modular arithmetic (before + after); assert_entanglement validates each control
   qubit ↔ working-register correlation BEFORE the inverse QFT (phase kickback
   depends on exactly this entanglement structure).
4. **Complex invariants by chaining**: multi-control gates decompose recursively
   into smaller assert_entanglement checks.

## Numeric Verification (17/17 checks, logical-level reproduction)

- Correct CNOT(0→1) on |+0⟩ → (|00⟩+|11⟩)/√2 (Schmidt rank 2); buggy CNOT(1→0)
  is a no-op (rank 1). χ² test at n=400: correct χ²=400 (reject independence →
  entangled ✓), buggy χ²≈0 (independent → bug caught), 0/200 buggy runs false-pass,
  200/200 correct runs pass.
- assert_classical: clean prep at p_L=2% passes (391/400); corrupted 85%-match
  register fails; buggy-product register passes |0⟩ check while correct Bell fails
  it (50/50 marginals) — the two primitives jointly discriminate correct vs buggy.
- Eigenstate semantics: X-measurement on |+⟩ preserves state (continue);
  Z-measurement destroys it (checkpoint).
- Overhead arithmetic: (with−without)/with matches Table 2 (Golay 2.7%, Surface
  |p0⟩ 14.3%, Hex 0p1 6.7%); listed mean 1.39% < all-states average 1.8%.

## Pitfalls

- **One-sided binomial tail underflow**: computing the exact SF by iterating from
  (1−q)^n underflows for n ≳ 300 when q near 1 ((0.02)^400 = 0 in float64) and
  silently makes every assertion pass/fail vacuously. Use log-space PMF
  (lgamma) with smallest-first accumulation, or start iteration from the mode.
  ALWAYS run a known-value positive control (clean prep must PASS, corrupted must
  FAIL) before trusting the test implementation.
- Binomial discreteness means realized FPR ≤ α, not = α; report the achieved level.
- assert_superposition in the Z basis is inherently destructive — reserve it for
  points where a checkpoint is acceptable; use X-basis assert_classical for |+⟩
  eigenstates instead.
- SynDebug cannot validate arbitrary amplitudes/relative phases, nor catch bugs
  that preserve every asserted invariant; it complements (not replaces) formal
  verification.
- Overhead measured per ONE QEC round (worst case); relative overhead shrinks with
  more rounds.

Code: https://github.com/positivetechnologylab/SynDebug

## Related Skills
- [[qusema-semantic-oracle-bug-detection]] — testing quantum libraries with semantic oracles
- [[retromorphic-quantum-compiler-testing]] — compiler validation via retromorphic tests
- [[statistical-quantum-phase-estimation]] — statistical-test mindset for quantum routines
