---
name: logical-gate-set-tomography
description: Characterize noisy logical gate sets after QEC via logical GST. Use when auditing residual logical error mechanisms.
category: quantum
---

# Logical Gate Set Tomography (Logical GST)

**Source**: arXiv:2610.19034 — Wysocki et al. (Quantinuum + Sandia), 13 Oct 2026
**Domain**: Quantum error correction / characterization

## Core Insight

QEC suppresses noise, but predicting whether a computation succeeds requires knowing not just **how much** effective noise remains, but **what form it takes**. Logical GST extends gate set tomography from physical to logical operations: it produces detailed, self-consistent representations of noisy logical gates from which higher-level metrics (logical gate fidelity, diamond distance) are derived, and it explicitly tests for non-Markovian and coherent logical errors.

First application: full self-consistent characterization of a universal single-qubit logical gate set in the 7-qubit Steane code on Quantinuum H1 (trapped-ion, 20 qubits).

## Method Structure

1. **Run GST circuits at the logical level**: the gate set being tomographically reconstructed is the *encoded* gate set (logical X, Y, H-like rotations, etc. in the Steane code), not the physical gates.
2. **Fit a self-consistent logical gate model**: same pyGSTi-style estimation machinery, but the estimand is the logical error channel on the code space. Model violations then flag *logical* non-Markovianity or coherent error.
3. **Derive metrics**: logical gate fidelities, diamond distances, Pauli-stochastic vs coherent decomposition of logical error.
4. **Error attribution**: with a system emulator generating matched datasets, map which physical error sources produce which logical error mechanisms.

## Key Experimental Findings (H1, Steane code)

- Logical errors were **predominantly Pauli-stochastic**.
- **No evidence of logical non-Markovianity** in hardware data (within model-violation bounds).
- **Weak potential signatures of coherent logical error** detected.
- Emulator (higher-shot) datasets: mechanisms for weak-but-significant logical non-Markovianity + strong evidence of coherent logical error — showing hardware data alone can under-detect these.
- Attribution: specific physical error sources → specific logical error mechanisms (leakage, correlated measurement, etc.).

## When to Use

- Selecting/validating a QEC code + logical gate set for a fault-tolerant stack
- Deciding whether logical errors are Markovian enough to justify stochastic-decoder assumptions
- Diagnosing coherent logical errors that threshold-analysis formulas (which assume Pauli noise) miss
- Building error budgets for logical algorithms (e.g., is diamond distance of the logical gate set within tolerance)

## Implementation Notes

- Tooling: pyGSTi supports logical-level model construction; circuits are the *encoded* circuits (with QEC cycles inside each logical gate occurrence).
- Cost: long-sequence GST on logical gates is expensive — the paper's datasets used emulator augmentation for high-shot statistical power; plan hardware time accordingly.
- The Markovianity test doubles as a decoder validation: a decoder mismatched to the true (coherent/non-Markovian) error structure will show up as model violation.
- Compare diamond distance, not just fidelity — coherent components dominate distance metrics even at equal fidelity.

## Related

- [[composite-quantum-gates-error-cancellation]] — cancellation schemes whose design assumes coherent structure
- Randomized benchmarking gives scale; logical GST gives structure. Use RB for quick tracking, logical GST for deep audits.
