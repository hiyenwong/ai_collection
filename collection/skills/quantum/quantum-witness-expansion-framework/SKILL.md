---
name: quantum-witness-expansion-framework
description: Witness Expansion framework for unified quantum resource detection. Constructs nonlinear criteria for detecting quantum resources via polynomial functions of target states. Use when analyzing quantum resources like coherence, entanglement, magic states, or fermionic non-Gaussianity. Covers l2 coherence, partial-transpose moments, stabilizer entropy.
---

# Witness Expansion Framework

From arXiv:2606.27105

## Core Idea

Unified framework for constructing nonlinear criteria detecting quantum resources associated with free unitary groups. Based on polynomial functions estimable with multiple copies of the target state.

## Recovered Resources

- l2 norm of coherence
- Partial-transpose moments (entanglement)
- Stabilizer entropy (nonstabilizerness/magic)
- Fermionic antiflatness (fermionic non-Gaussianity)

## New Capabilities

- Detection criteria for qubit and qudit magic states
- First analytical criterion for mixed-state fermionic non-Gaussianity w.r.t. convex hull of pure fermionic Gaussian states
- Nontrivial for arbitrary number of qubits

## Implementation Pattern

```
Multiple State Copies -> [Polynomial Measurement] -> [Resource Criterion] -> [Detect/Quantify]
```

## Mathematical Framework

For free unitary group G, construct polynomial functions P(rho^tensor-k) where:
- k = number of copies
- P is invariant under G
- P detects resource when P(rho) > threshold

## When to Use

- Benchmarking quantum devices for resource content
- Detecting mixed-state quantum resources analytically
- Understanding fundamental structure of quantum resource theories
- Designing resource-efficient quantum protocols