---
name: quantum-fisher-information-duality
description: "Quantum Fisher Information (QFI) duality framework for distributed quantum sensing. Establishes precision-privacy tradeoff: F_Q(w·θ) + F_Q(v·θ) ≤ N for orthogonal sensing directions. Heisenberg-limited precision for one direction forces zero QFI for others, enabling parameter privacy. Activation: quantum Fisher information, QFI duality, distributed quantum sensing, quantum privacy, parameter privacy, 量子费雪信息."
category: information-science
---

# Quantum Fisher Information Duality

QFI duality framework for distributed quantum sensor networks with local phase encoding. Based on arXiv:2605.20765.

## Core Theorem

For any N-qubit probe state with local phase encoding:

```
F_Q(wᵀθ) + F_Q(vᵀθ) ≤ N
```

For all unit orthogonal sensing directions w and v.

### Equality Conditions
- **N = 2**: Equality for all equatorial states
- **N ≥ 2**: Equality for GHZ states

## Key Insight: Precision-Privacy Tradeoff

**Heisenberg-limited precision** for direction w (F_Q = N²) saturates the bound and **simultaneously forces zero QFI** for all other independent directions.

This means: attaining Heisenberg-limited precision for the sensing target renders all alternative privacy-intrusive estimations **impossible**.

## When to Use

- Designing distributed quantum sensor networks
- Privacy-preserving quantum sensing protocols
- Multi-parameter quantum estimation
- Quantum cryptography with sensing components
- Quantum information security analysis

## Design Principles

1. **Maximize target QFI**: Use GHZ states or equatorial states to saturate the bound for the sensing direction of interest
2. **Minimize leakage QFI**: The duality ensures orthogonal directions receive zero Fisher information when target is maximized
3. **Privacy is automatic**: No additional cryptographic mechanism needed — the physics enforces the privacy guarantee

## Practical Implications

| Scenario | Strategy | Privacy Guarantee |
|----------|----------|-------------------|
| Single-parameter sensing | GHZ state | Perfect (zero leakage) |
| Multi-parameter estimation | Trade-off tuning | Bounded by duality |
| Adversarial sensing | Orthogonal encoding | Information-theoretic |

## Limitations

- Applies to local phase encoding only
- Requires entangled probe states for Heisenberg scaling
- N=2 case limited to equatorial states for tightness

## References

- arXiv:2605.20765 — "Precision and Privacy in Distributed Quantum Sensing: A Quantum Fisher Information Duality" (Farokhi, 2026)
- Related: quantum-statistical-estimation skill
