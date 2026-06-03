---
name: lean-qec-formal-verification
description: "End-to-end formal verification methodology for quantum error correction codes using Lean 4 theorem proving. Covers stabilizer code formalization, machine-checked distance certificates, SAT-based verified reductions for qLDPC and Bivariate Bicycle codes, and binary symplectic representation. Use when: (1) Formal verification of quantum error-correcting codes, (2) Proving code distance bounds at industrial scale, (3) Lean 4 theorem proving for quantum computing, (4) Verified compilation/reduction of QECC distance problems to SAT, (5) Designing fault-tolerant quantum architectures with machine-checked proofs, (6) Quantum-classical formal verification integration. Keywords: Lean 4, quantum error correction, stabilizer codes, formal verification, distance certificate, SAT encoding, qLDPC, theorem proving, fault tolerance."
---

# Lean-QEC Formal Verification Methodology

End-to-end formal verification for quantum error correction codes using Lean 4, delivering machine-checked distance certificates at industrial code sizes. Based on Lean-QEC (arXiv:2605.16523).

## Core Architecture

Lean-QEC formalizes the complete stabilizer code theory stack:

1. **Linear algebra of qubit states** — vector space representations over finite fields
2. **Pauli group** — n-qubit Pauli operators, commutation relations
3. **Stabilizer codes** — stabilizer formalism, code space characterization
4. **Binary symplectic representation** — efficient bit-level encoding of Pauli operators
5. **Classical coding theory** — linear codes, parity check matrices
6. **Code families** — CSS codes, Bivariate Bicycle (BB) codes, Generalized Bicycle codes

## Distance Verification Pipeline

The distance certification problem is NP-hard in general. Lean-QEC breaks the combinatorial barrier through:

### Step 1: Verified SAT Reduction

Translate the distance condition into a Boolean satisfiability (SAT) formula through a **verified reduction** in Lean 4. The reduction is machine-checked — the proof that the SAT formula is equivalent to the distance condition is verified by Lean's kernel.

### Step 2: BitVec-Flattened Encoding

Replace Lean's `Matrix` representation with `BitVec`-flattened encoding for computational efficiency. This enables scaling to larger code sizes within the theorem prover.

### Step 3: Error-Location Encoding

Reduce variable count from O(n) to O(√n) through error-location encoding instead of full error pattern enumeration.

### Step 4: Industrial-Scale Verification

Automatically generate Lean-checked distance proofs for qLDPC codes:
- [[90, 8, 10]] BB codes
- [[70, 6, 9]] BB codes
- Scaling up to 144 qubits (outside Lean kernel)

## Key Technical Insights

### Why Formal Verification for QECC?

Code distance values in literature come from either:
- Non-scaling hand proofs (limited scope)
- Unverified solvers (trust gap where guarantees matter most)

Formal verification closes this gap: the distance certificate is machine-checked, providing end-to-end trust from mathematical definition to numerical result.

### When to Apply This Approach

- **NISQ-era code design**: Verify distance bounds before hardware deployment
- **Fault-tolerant architecture**: Build verified components for larger FTQC systems
- **Code family exploration**: Systematically verify new code constructions
- **Cross-verification**: Independently validate distance claims from numerical solvers

### Integration with Broader Lean Ecosystem

Lean-QEC is designed as a reusable library to plug into broader Lean-based efforts toward end-to-end verification of fault-tolerant quantum computation.

## Verification Workflow

```
1. Define stabilizer code (generators in binary symplectic form)
2. Specify target distance d
3. Generate SAT formula encoding "exists error of weight < d not detected"
4. Run verified reduction in Lean 4
5. Solve SAT (external solver or within Lean)
6. Machine-check: if UNSAT → distance ≥ d certified
```

## Related Concepts

- Stabilizer formalism (Gottesman-Knill)
- CSS code construction (Calderbank-Shor-Steane)
- Bivariate Bicycle codes (Bravyi et al.)
- qLDPC codes (quantum Low-Density Parity-Check)
- Lean 4 theorem proving
- Boolean satisfiability (SAT) solving
- Binary symplectic representation of Pauli group

## Activation

- quantum error correction formal verification
- Lean 4 quantum computing
- stabilizer code distance proof
- machine-checked quantum verification
- qLDPC code certification
- fault-tolerant quantum architecture verification
