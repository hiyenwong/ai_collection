---
name: quantum-fisher-privacy-duality
description: >
  Quantum Fisher Information (QFI) duality framework for privacy in distributed quantum sensing.
  Establishes fundamental tradeoff: F_Q(w^T θ) + F_Q(v^T θ) ≤ N for orthogonal sensing directions.
  Heisenberg-limited precision for one target direction forces zero QFI for all others — achieving
  parameter privacy by construction. Use when: designing privacy-preserving quantum sensor networks,
  analyzing information leakage in distributed quantum sensing, optimizing probe states for
  selective parameter estimation, or building quantum metrology systems with privacy guarantees.
  Activation: quantum Fisher information, QFI duality, distributed quantum sensing privacy,
  parameter privacy, quantum metrology privacy, GHZ state sensing, Heisenberg limit privacy,
  quantum sensor network security.
---

# Quantum Fisher Information Privacy Duality

Methodology from arXiv:2605.20765 — "Precision and Privacy in Distributed Quantum Sensing: A Quantum Fisher Information Duality" (Farokhi, 2026).

## Core Theorem

For any N-qubit probe state with local phase encoding:

```
F_Q(w^T θ) + F_Q(v^T θ) ≤ N
```

for all unit orthogonal sensing directions w and v.

### Equality Conditions
- **N = 2**: Equality for all equatorial states
- **N ≥ 2**: Equality for GHZ states

## Privacy Implication

**Heisenberg-limited precision = Privacy guarantee:**

If F_Q(w^T θ) = N (optimal precision for target parameter), then F_Q(v^T θ) = 0 for ALL
other independent directions. An adversary cannot estimate any alternative parameter.

## Design Principles

### 1. GHZ State Maximizes Privacy
- GHZ states saturate the bound for N ≥ 2
- Achieve Heisenberg scaling while simultaneously blocking all side-channel estimation

### 2. Direction Selection Matters
- Choose sensing direction w aligned with target parameter
- Any orthogonal direction v has zero Fisher information at the optimum
- Privacy is structural — no additional cryptographic protocol needed

### 3. Tradeoff is Fundamental
- Cannot simultaneously estimate multiple orthogonal parameters with Heisenberg precision
- Privacy emerges from quantum measurement limits, not encryption

## Applications

- Distributed quantum sensor networks with privacy-by-design
- Quantum IoT systems preventing parameter leakage
- Quantum metrology where only authorized parameters should be estimable
- Multi-party quantum sensing with selective information disclosure

## Verification

For a given probe state ρ and sensing directions w, v:
1. Compute QFI matrices for each direction
2. Verify F_Q(w^T θ) + F_Q(v^T θ) ≤ N
3. If F_Q(w^T θ) ≈ N, confirm F_Q(v^T θ) ≈ 0 for privacy guarantee