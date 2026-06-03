---
name: quantum-optimal-control-irrep-distillation
description: "Quantum optimal control of Dicke manifold using irrep distillation methodology. Controls quantum states of many-body systems by exploiting symmetric subspace structure in Rydberg atom arrays. Irrep distillation captures how symmetric subspace couples to leakage error-spaces using only linear-scaling Hilbert dimension. Combines with gradient ascent pulse engineering (GrAPE) for control schemes with minimal local addressing. Benchmarks quantum speed limit and pulse fidelities. Activation: quantum optimal control, Dicke manifold, irrep distillation, Rydberg atom control, gradient ascent pulse engineering, GrAPE, many-body quantum control, quantum speed limit, GHZ state generation, symmetric subspace control, dipole-dipole interaction leakage."
license: Complete terms in LICENSE.txt
metadata:
  arxiv_id: "2606.02283"
  published: "2026-06-01"
  authors: "Ivy Pannier-Gunther, Vikas Buchemmavari, Pablo M. Poggi, Ivan H. Deutsch"
  tags: [quantum-optimal-control, dicke-states, rydberg-atoms, irrep-distillation, GRAPE, many-body-control, GHZ-states]
---

## Quantum Optimal Control of the Dicke Manifold via Irrep Distillation

### Core Problem

For N qubits, full Hilbert space dimension grows exponentially (2^N), making generic state preparation infeasible. The symmetric subspace (Dicke manifold) is physically motivated but dipole-dipole interactions cause leakage from the computational subspace.

### Irrep Distillation (IRD) Methodology

1. **Truncated Hilbert Space**: Performs quantum optimal control on a truncated space that captures leakage coupling with only linear-scaling Hilbert dimension
2. **Leakage Tracking**: IRD captures how the symmetric subspace couples to leakage error-spaces
3. **Higher-Order IRD**: Extended versions predict fidelities on larger system sizes from small-system benchmarks

### Control Implementation

- **GrAPE**: Gradient Ascent Pulse Engineering on control schemes with little or no local addressing
- **Target States**: GHZ states, Dicke states, extremal quantum states
- **Benchmarking**: Quantum speed limit (QSL) analysis, exact pulse fidelity testing on small systems

### Reusable Patterns

1. **Symmetry-exploiting truncation**: Restrict to symmetric subspace when physical system has permutation symmetry
2. **Leakage-aware optimization**: Include leakage channels in optimization, not just target subspace
3. **Linear-scaling approximation**: Use representation theory to reduce exponential scaling to linear
4. **Minimal-addressing control**: Design control pulses that work with limited local addressing capability

### When to Use

- Quantum optimal control of symmetric multi-qubit systems
- Rydberg atom array state preparation
- Mitigating leakage from dipole-dipole interactions
- Designing control pulses for GHZ and Dicke state generation
- Quantum speed limit analysis for many-body systems
