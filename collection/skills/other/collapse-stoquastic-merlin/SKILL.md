---
name: collapse-stoquastic-merlin
description: >
  Collapse of Unentangled Stoquastic Merlin-Arthur Proof Systems methodology. Proves that
  unentanglement gives no additional power to stoquastic Merlin-Arthur verification:
  StoqMA(k) = StoqMA for any polynomial number of provers k. Separates the role of
  entanglement from interference: once destructive interference is ruled out by stoquasticity,
  the product-state constraint can be absorbed into a polynomially larger one-witness
  verification. Main tool: positive, value-based de Finetti theorem for separately symmetric
  extensions. Use when analyzing quantum complexity classes, studying the power of
  unentanglement in proof systems, or understanding the relationship between interference
  and entanglement in quantum verification. Trigger: stoquastic Merlin-Arthur, StoqMA,
  unentangled proof systems, quantum complexity class, de Finetti theorem quantum,
  quantum verification power, stoquastic Hamiltonian complexity.
---

# Collapse of Unentangled Stoquastic Merlin-Arthur Proof Systems

## Overview

This result resolves a fundamental question in quantum complexity theory: **does
unentanglement add power to stoquastic verification?** The answer is **no** — for any
polynomial number of provers, StoqMA(k) = StoqMA.

## Key Concepts

### Stoquastic Hamiltonians
- Hamiltonians with no sign problem (all off-diagonal entries are non-positive in the
  computational basis)
- No destructive interference → amplitudes can be interpreted as probabilities
- Ground state problem is in StoqMA

### Merlin-Arthur Proof Systems
- **StoqMA**: Stoquastic Merlin-Arthur — verification via stoquastic Hamiltonian
- **StoqMA(k)**: k-prover version where provers send unentangled quantum states
- Standard MA with quantum witnesses restricted to stoquastic verification

### Main Result

**Theorem**: For every polynomial k = k(n), StoqMA(k) = StoqMA.

This means unentangled multi-prover stoquastic verification collapses to single-prover.

## Proof Strategy

### Separation of Entanglement and Interference

The proof cleanly separates two fundamental quantum resources:

1. **Destructive interference**: Ruled out by stoquasticity
2. **Entanglement**: The product-state (unentangled) constraint

**Key insight**: When destructive interference is absent (stoquastic), the unentanglement
constraint becomes redundant — it can be absorbed into a larger single-witness system.

### De Finetti Theorem

**Main analytic tool**: Positive, value-based de Finetti theorem for separately symmetric
extensions.

This theorem shows that for stoquastic systems, approximately symmetric states can be
approximated by convex combinations of product states — but since the system is already
stoquastic, this approximation is exact in the relevant sense.

## Implications

| Aspect | Before | After |
|--------|--------|-------|
| **StoqMA(k) power** | Unknown | Equals StoqMA |
| **Entanglement role** | Unclear in stoquastic | Separated from interference |
| **Interference role** | Mixed with entanglement | Identified as key resource |

## Complexity Class Hierarchy

```
QMA(k) — unknown if QMA(k) = QMA (major open problem)
  ↓ [restrict to stoquastic]
StoqMA(k) = StoqMA  ← proven by this work
  ↓ [further restrict]
MA (classical)
```

## Activation Keywords
- stoquastic Merlin-Arthur
- StoqMA
- unentangled proof systems
- quantum complexity class
- de Finetti theorem quantum
- quantum verification power
- stoquastic Hamiltonian complexity
- quantum prover verification
- quantum interference vs entanglement
- 量子复杂度类
- stoquastic verification

## Tools Used
- **search_files**: Find relevant quantum complexity literature
- **read_file**: Read proof details and related work

## Resources
- arXiv:2605.16249 — "The Collapse of Unentangled Stoquastic Merlin-Arthur Proof Systems"
- Related: quantum-complexity-math-structure, quantum-ml-patterns
