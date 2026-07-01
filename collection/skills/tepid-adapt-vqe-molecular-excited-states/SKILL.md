---
name: tepid-adapt-vqe-molecular-excited-states
description: "TEPID-ADAPT-VQE algorithm for simultaneous preparation of multiple molecular excited states with reduced circuit depth. Variationally diagonalizes truncated low-temperature Gibbs state for quantum chemistry applications. Activation: TEPID-ADAPT-VQE, excited states, molecular simulation, VQE, ADAPT ansatz, Gibbs state"
---

## TEPID-ADAPT-VQE Methodology

**Source**: arXiv:2606.29547 (2026-06-28)
**Title**: Quantum simulation of molecular excited-state manifolds and energies using the TEPID-ADAPT-VQE algorithm
**Authors**: Jason Saroni, Bharath Sambasivam, Ayush Asthana

## Overview

Truncated Eigenvalue Parametrized Initial Density Adaptive Variational algorithm for computing low-lying excited states and potential energy surfaces. Key advantage: simultaneous preparation of multiple excited states within a single optimization.

## Core Methodology

### TEPID-ADAPT Framework
1. **Gibbs State Diagonalization**: Variationally diagonalizes truncated low-temperature Gibbs state
2. **Simultaneous Preparation**: Multiple excited states prepared in single optimization (vs. separate runs)
3. **ADAPT Ansatz**: Adaptive derivative-assembled problem-tailored construction yields compact circuits
4. **Reduced Circuit Depth**: Suitable for near-term NISQ hardware

### Application Range
- H₂, LiH, linear H₄ molecules
- Bond lengths spanning weakly and strongly correlated regimes
- Potential energy surface mapping

## Key Advantages

- **Single optimization** for multiple states (not sequential)
- **Compact circuits** via ADAPT construction
- **Broad applicability**: weak to strong correlation regimes
- **Drug discovery relevance**: molecular excited states critical for photochemistry

## Implementation Pattern

```python
# Workflow
1. Define molecular Hamiltonian and basis set
2. Initialize truncated low-temperature Gibbs state
3. Build ADAPT ansatz iteratively:
   - Compute gradients for operator pool
   - Select operator with largest gradient
   - Append to circuit with optimized parameter
4. Variational optimization of Gibbs state parameters
5. Extract excited state energies from diagonalized state
```

## Pitfalls

- Truncation level of Gibbs state affects accuracy
- ADAPT ansatz growth may become large for complex molecules
- Strong correlation regimes require careful operator pool selection
