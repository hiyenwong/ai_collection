---
name: cyclic-symmetry-ancilla-distillation
description: >
  Fault-tolerant ancilla preparation methodology for quantum BCH codes using cyclic symmetry.
  Use when: designing fault-tolerant quantum error correction circuits, preparing ancilla states
  for high-rate QEC codes (BCH, cyclic codes), optimizing distillation circuits, reducing spatial
  overhead in FTQC architectures, working with quantum BCH codes up to 127 qubits, neutral atom
  quantum computing platforms, entanglement distillation for state preparation.
  Triggers: ancilla preparation, fault-tolerant state preparation, quantum BCH codes, cyclic
  symmetry distillation, quantum error correction state prep, FTQC resource optimization,
  entanglement distillation circuits, high-rate QEC codes.
  Source: arXiv:2605.19471
---

# Cyclic Symmetry Ancilla Distillation for Quantum BCH Codes

## Core Methodology

Two-stage fault-tolerant ancilla preparation leveraging cyclic symmetry of quantum BCH codes.

### Stage 1: Non-Fault-Tolerant Preparation

1. Prepare initial ancilla state using standard (non-FT) stabilizer measurement circuits
2. Accept that single faults may propagate to multi-qubit errors in this stage
3. Target state: code space of the chosen quantum BCH code [[n,k,d]]

### Stage 2: Entanglement Distillation with Cyclic Symmetry

1. **Exploit cyclic structure**: Quantum BCH codes are cyclic — codewords are invariant under cyclic shifts
2. **Symmetry-based filtering**: Design distillation circuit that verifies cyclic symmetry of prepared state
   - Compute cyclic shift operators S where S|ψ⟩ = |ψ⟩ for valid codewords
   - Measure eigenvalues of S; reject if eigenvalue ≠ 1
3. **Low-overhead distillation**: Combine multiple noisy copies, measure joint stabilizers
   - Key insight: cyclic symmetry determines WHICH non-FT circuits can produce FT states
   - Only circuits compatible with the code's cyclic structure survive distillation

### Design Framework

```
For quantum BCH code C with parameters [[n, k, d]]:
1. Identify generator polynomial g(x) over GF(2^m)
2. Compute cyclic shift symmetry group of C
3. Design distillation circuit that:
   a. Takes m noisy copies of ancilla state
   b. Measures cyclic-symmetry-compatible joint stabilizers
   c. Outputs single higher-fidelity state if all checks pass
4. Verify: logical error rate < threshold under circuit-level noise model
```

## Key Results (arXiv:2605.19471)

- Simulated on BCH codes up to [[127, k, d]] with lower spatial overhead than standard distillation
- Achieves better logical error rates under circuit-level noise vs. conventional methods
- Particularly suited for highly-connected platforms (neutral atoms, all-to-all connectivity)

## When to Use

- **High-rate QEC**: When code rate k/n is large (BCH codes offer better rates than surface codes)
- **Spatial overhead matters**: When physical qubit budget is constrained
- **Neutral atom systems**: Platform has all-to-all connectivity enabling efficient distillation circuits
- **Benchmarks needed**: When evaluating logical error rates under realistic circuit noise

## Pitfalls

- Requires quantum BCH codes specifically — not applicable to all QEC code families
- Distillation circuit depth increases with code distance d
- Neutral atom connectivity assumed; may need adaptation for limited-connectivity hardware

## Activation Keywords

fault-tolerant ancilla, quantum BCH codes, cyclic symmetry, entanglement distillation, FTQC, quantum error correction, state preparation, spatial overhead, logical error rate, neutral atom quantum computing
