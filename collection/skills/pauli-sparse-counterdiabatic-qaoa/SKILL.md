---
name: pauli-sparse-counterdiabatic-qaoa
description: "Counterdiabatic shortcuts for QAOA with Pauli-sparsity regularisation. Combines counterdiabatic driving with sparsity constraints to improve QAOA performance through approximate adiabatic evolution. arXiv: 2606.28536"
---

# Pauli-Sparse Counterdiabatic QAOA Shortcuts

Methodology from arXiv:2606.28536 — Pauli-Sparse regularised Counterdiabatic Shortcuts for Linear-Ramp QAOA.

## Core Innovation

Combines counterdiabatic (CD) driving — which adds extra terms to Hamiltonian to suppress non-adiabatic transitions — with Pauli-sparsity regularisation to make the resulting circuit implementable on near-term quantum hardware.

## Key Technical Components

1. **Counterdiabatic Shortcuts**: Adds gauge potential terms (AG) to the original Hamiltonian to drive the system along instantaneous eigenstates, effectively "shortcutting" slow adiabatic evolution
2. **Pauli-Sparse Regularisation**: The CD terms are often non-local and hard to implement. Regularisation constrains the gauge potential to be sparse in the Pauli basis, making it hardware-compatible
3. **Linear-Ramp Schedule**: Uses linear interpolation between initial and problem Hamiltonians, with CD correction throughout
4. **Approximate CD via Variational Optimization**: The sparse gauge potential is optimized variationally to best approximate the exact (but impractical) counterdiabatic terms

## Implementation Pattern

```
H(t) = (1-t/T) * H_B + (t/T) * H_P + AG(t)
Where: H_B = mixer, H_P = problem, AG = gauge potential

Steps:
1. Compute exact CD gauge potential (often non-local)
2. Project onto sparse Pauli basis via regularisation
3. Optimize variational parameters for best approximation
4. Apply linear-ramp schedule with CD correction
5. Execute on quantum hardware
```

## Advantages

- Faster convergence than standard QAOA (fewer layers needed)
- More implementable than exact CD (sparse Pauli terms)
- Works within QAOA framework without hardware changes
- Bridges adiabatic quantum computing and circuit-model approaches

## When to Use

- QAOA optimization on NISQ devices
- Problems requiring many QAOA layers (where CD can reduce depth)
- Combinatorial optimization where adiabatic evolution is effective but slow
- Cases where exact counterdiabatic terms are too complex for hardware

## Activation Keywords

counterdiabatic, QAOA, adiabatic-shortcut, Pauli-sparse, quantum-optimization, gauge-potential, variational-quantum, NISQ optimization

## Paper Reference

- **Title**: Pauli-Sparse regularised Counterdiabatic Shortcuts for Linear-Ramp QAOA
- **arXiv**: 2606.28536
- **Date**: 2026-06-30
- **Category**: quant-ph
