---
name: quantum-error-formal-verification
description: "Formal verification methodology for quantum error-correcting codes using proof assistants. Based on Lean-QEC (arXiv:2605.16523), the first Lean 4 formalization of stabilizer-code theory delivering machine-checked distance certificates for qLDPC codes. Use when: (1) formally verifying quantum error correction code parameters, (2) computing stabilizer code distances at scale, (3) building machine-checked proofs for quantum computing correctness, (4) translating combinatorial problems into Boolean satisfiability, (5) working with Lean 4 proof assistant for quantum systems. Activation: quantum error correction formalization, Lean QEC, stabilizer code verification, distance certificate, qLDPC formal proof, machine-checked quantum proof, formal quantum verification."
---

# Quantum Error Formal Verification

Methodology for end-to-end formal verification of quantum error-correcting codes (QECCs) using proof assistants. Based on Lean-QEC (Ehatamm et al., University of Maryland, arXiv:2605.16523).

## The Trust Problem

QECC distance d certifies how many errors a code corrects: ⌊(d-1)/2⌋. But computing distance lower bounds is NP-hard. In practice, distance values come from:

1. **Hand proofs** — enumerate all Pauli errors. Don't scale past 9 qubits.
2. **Unverified solvers** — ILP solvers, custom search. Leave trust gap at the guarantee point.

Neither is end-to-end: the first doesn't scale, the second leaves unverified computation.

## Lean-QEC Pipeline

```
Stabilizer Code Definition
    ↓
Linear Algebra Formalization (qubit states, Pauli group)
    ↓
Binary Symplectic Representation
    ↓
Distance Condition → Boolean Satisfiability (verified reduction)
    ↓
BitVec-Flattened Encoding (replaces Matrix representation)
    ↓
Error-Location Encoding (reduces variables: n → k·⌈log₂n⌉)
    ↓
Machine-Checked Distance Proofs
```

## Key Techniques

### 1. Verified SAT Reduction

Translate the distance condition into a Boolean satisfiability formula through a mathematically verified reduction. The proof assistant checks every step.

### 2. BitVec-Flattened Encoding

Replace the standard Matrix representation with BitVec encoding to break the combinatorial barrier. This enables scaling to industrial code sizes.

### 3. Error-Location Encoding

Instead of encoding each possible error location as a separate variable (n variables), encode the error location as a binary index (k·⌈log₂n⌉ variables). Dramatically reduces problem size.

### 4. CSS and Bivariate Bicycle Support

The formalization covers CSS codes and Bivariate Bicycle (BB) code families, including J90,8,10K and J70,6,9K BB codes, scaling up to 144 qubits.

## Reusable Library Components

The Lean-QEC formalization provides a reusable library covering:

- Linear algebra of qubit states
- Pauli group theory
- Stabilizer code formalism
- Binary symplectic representation
- Classical coding theory
- CSS code family
- Bivariate Bicycle code family

This library is designed to plug into broader Lean-based efforts toward end-to-end verification of fault-tolerant quantum computation.

## Application Pattern

When verifying quantum systems:

1. **Define** the stabilizer code formally in the proof assistant
2. **Reduce** the distance condition to SAT via verified transformation
3. **Encode** using BitVec + error-location compression
4. **Prove** machine-checked distance certificate
5. **Reuse** the library for related codes

## Why This Matters for Agent Systems

The methodology demonstrates a general pattern for trustworthy automated reasoning:

1. **Decompose** an NP-hard verification problem into SAT
2. **Verify** the reduction in a proof kernel
3. **Scale** using encoding optimizations
4. **Produce** certificates that can be independently checked

This pattern applies beyond quantum computing to any domain requiring trustworthy automated verification at scale.

## Related Papers

- arXiv:2605.16523 — Lean-QEC: End-to-End Formalization of Quantum Error Correction
- arXiv:2605.16509 — Quokka#: Quantum Computing with #SAT (complementary SAT-based approach)
