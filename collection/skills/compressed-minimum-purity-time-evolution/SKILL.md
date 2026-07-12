---
name: compressed-minimum-purity-time-evolution
description: "CoMPuTE method for late-time quantum dynamics simulation using compressed minimum-purity time evolution. Tracks reduced local density matrices via minimum-purity principle for efficient long-time quantum many-body simulations."
metadata:
  arxiv_id: "2606.11392"
  published: "2026-06-09"
  authors: "Moksh Bhateja, Jonas B. Rigo, Markus Schmitt"
  tags: [quantum-dynamics, time-evolution, tensor-networks, many-body-physics, density-matrix]
---

# Compressed Minimum-Purity Time Evolution (CoMPuTE)

## Overview

CoMPuTE addresses the challenge of simulating late-time quantum many-body dynamics where entanglement growth limits traditional methods (MPS/TEBD). The key insight: while microscopic states become complex, macroscopic observables exhibit effective simplicity (hydrodynamics/kinetic theory). CoMPuTE closes the hierarchy of equations of motion using a **minimum-purity principle** on reduced local density matrices.

## Core Methodology

### Minimum-Purity Principle

Given a set of reduced local density matrices {ρᵢ}, the next time step selects the **minimum-purity** consistent extension:

```
min Tr(ρ²)  s.t.  Tr_{j≠i}(ρ) = ρᵢ  ∀i
```

This selects the least biased (maximum entropy) extension consistent with local constraints, enabling tractable time evolution.

### Algorithm Steps

1. **Initialize**: Start with product state or simple initial state
2. **Local evolution**: Apply local Hamiltonian terms to each reduced density matrix
3. **Purity minimization**: Find minimum-purity global state consistent with local constraints
4. **Extract reduced states**: Compute new local density matrices from the extended state
5. **Iterate**: Repeat for desired time steps

### Key Advantages

- **Efficiency**: Avoids exponential entanglement growth by working with reduced states
- **Accuracy**: Benchmarked against exact solutions for mixed-field Ising model
- **Generality**: Works for equilibrium and out-of-equilibrium (Floquet) dynamics

## Applications

### Pattern 1: Energy Diffusion in 1D Systems

Use CoMPuTE for studying energy transport in 1D quantum spin chains:

```python
# Mixed-field Ising model: H = -J∑σᵢᶻσᵢ₊₁ᶻ - h_x∑σᵢˣ - h_z∑σᵢᶻ
# CoMPuTE accurately captures diffusive energy spreading
```

### Pattern 2: Floquet Dynamics

For periodically driven systems starting from pure states:

```python
# CoMPuTE tracks late-time Floquet steady states
# Useful for studying prethermalization and heating
```

### Pattern 3: Transport in Integrable Systems

⚠️ **Limitation**: CoMPuTE struggles with transport governed by non-local integrals of motion (e.g., XXZ chain at Δ=1). The local reduced density matrix approximation breaks down when increasingly non-local conserved quantities dominate.

## Implementation Notes

- **Local patch size**: Balance between accuracy and computational cost
- **Purity optimization**: Can use iterative projection or variational approaches
- **Error estimation**: Compare with exact diagonalization for small systems

## Pitfalls

- **Integrable systems**: CoMPuTE may fail for systems with non-local conserved quantities
- **Initial state sensitivity**: Results depend on initial state simplicity
- **Higher dimensions**: Extension to 2D+ remains an open challenge

## References

- arXiv:2606.11392 — "Compressed minimum-purity time evolution for late-time quantum dynamics"
- Related: tensor-network-many-body-trace-norms (complementary tensor network methods)
