---
name: quantum-merlin-arthur-proof
description: Methodology for analyzing stoquastic Merlin-Arthur proof systems and the role of entanglement vs interference in quantum verification. Covers the collapse theorem StoqMA(k) = StoqMA, positive value-based de Finetti theorems for separately symmetric extensions, spectral relaxation of product-state constraints, and separation of entanglement from interference in stoquastic verification. Use when studying quantum proof systems, Merlin-Arthur protocols, stoquastic Hamiltonians, entanglement detection, de Finetti theorems, tensor optimization, or complexity classes (StoqMA, AM, PP, PSPACE). Trigger words: stoquastic, Merlin-Arthur, StoqMA, unentangled proof systems, de Finetti theorem, interference, entanglement detection, quantum verification, product states, symmetric extensions.
license: Complete terms in LICENSE.txt
---

# Quantum Merlin-Arthur Proof Systems

Methodology from "The Collapse of Unentangled Stoquastic Merlin-Arthur Proof Systems" (arXiv: 2605.16249).

## Core Result

**StoqMA(k) = StoqMA** for every polynomial number of provers k=k(n). Unentanglement gives no additional power to stoquastic Merlin-Arthur verification.

## Key Insights

1. **Entanglement vs Interference separation**: Once destructive interference is ruled out by stoquasticity, the product-state constraint can be absorbed into a polynomially larger one-witness stoquastic verification.

2. **Positive de Finetti theorem**: For entrywise nonnegative positive semidefinite contractions M on tensor products, the nonnegative product value of M is approximated to additive error ε by the largest eigenvalue of a spectral relaxation on symmetric subspaces.

3. **Spectral relaxation**: The relaxation is realized as an actual one-witness stoquastic verifier after replacing uniform permutation averages by dyadic inverse-invariant averages.

## Consequences

- StoqMA(k) = StoqMA ⊆ AM ∩ PP ⊆ PSPACE
- The positive de Finetti theorem is a standalone technique useful for nonnegative tensor-optimization and stoquastic-verification settings

## When to Use

- Analyzing quantum proof systems with stoquastic verifiers
- Studying the computational power of unentanglement
- Designing de Finetti-type theorems for nonnegative tensors
- Understanding the separation between entanglement and interference
- Complexity analysis of Merlin-Arthur protocols

## Pitfalls

- Stoquasticity (no destructive interference) is essential — results don't generalize to arbitrary quantum verifiers
- The de Finetti theorem applies specifically to nonpositive-semidefinite entrywise nonnegative matrices
- Dyadic approximation replaces permutation averages — precision matters for complexity bounds
- The containment StoqMA ⊆ AM ∩ PP requires the full collapse argument
