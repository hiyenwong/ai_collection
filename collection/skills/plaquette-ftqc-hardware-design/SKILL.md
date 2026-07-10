---
name: plaquette-ftqc-hardware-design
description: "Hardware-aware design platform for fault-tolerant quantum computers (FTQCs). Computes logical performance from device physics using Kraus operators, Hamiltonian-Lindblad dynamics, and quantum channels across four sampler classes."
tags: ["quantum", "fault-tolerance", "hardware-aware", "error-mitigation", "statistics"]
created: "2026-07-10"
source: "arxiv"
arxiv_id: "2607.08767"
---

## Overview

Plaquette is a theoretical framework and software suite that computes the logical performance of fault-tolerant quantum architectures directly from the physics of hardware imperfections. Bridges the gap between open-system device physics and FTQC logical performance.

## Key Problem

Hardware noise departs from stochastic Pauli models:
- Superconducting transmons: leak out of computational subspace
- Neutral atoms: scatter through intermediate states
- Trapped ions: heat via motion mode phonon absorption
- Miscalibrated controls: over-rotate coherently

## Four Sampler Classes

### 1. Stabilizer Sampling
- For Pauli noise models
- Standard approach, scalable
- May fall short for non-Pauli errors

### 2. XPauli Sampler (NEW)
- Handles leakage and environment sectors
- Near-Clifford accuracy for non-Pauli errors
- Matches full-state simulation within statistical uncertainty

### 3. Near-Clifford Samplers
- For coherent errors (over-rotations, crosstalk)
- Bridges gap between Clifford-only and full simulation

### 4. Full-State Simulation
- Exact reference calculations
- Limited to small systems
- Used for validation

## Workflow

1. **Specify Error Model**: Kraus operators, Hamiltonian-Lindblad dynamics, or experimentally reconstructed quantum channel
2. **Compile to Samplers**: Automatically compile into representations required by each sampler class
3. **Validate**: Compare XPauli/near-Clifford against full-state simulation
4. **Compute Logical Performance**: Get FTQC thresholds, error budgets, overhead estimates

## Platform-Specific Error Models

### Superconducting Qubits
- Leakage errors (|2⟩ state population)
- XPauli sampler captures leakage dynamics

### Neutral Atoms
- Intermediate-state scattering during gates
- Environment sector modeling

### Trapped Ions
- Motional mode heating (phonon absorption)
- Requires full Lindblad treatment for accuracy

## Core Findings

- Pauli twirling can fall short depending on error model
- Discrepancy size varies with platform and noise process
- Reliable thresholds require most accurate simulation available
- Direct path from open-system physics to FTQC logical performance

## Pitfalls

### Pauli Twirling Limitations
- Does not capture leakage or coherent errors accurately
- Can underestimate error rates significantly
- Use XPauli or near-Clifford samplers when noise is non-Pauli

### Sampler Selection
- XPauli: best for leakage and environment sectors
- Near-Clifford: best for coherent errors
- Full-state: only for small-system validation
- Stabilizer: only for purely Pauli noise

### Statistical Uncertainty
- XPauli matches full-state within statistical uncertainty
- Ensure sufficient sampling for reliable estimates
- Monitor convergence of logical error rate estimates

## Implementation

```python
# Conceptual workflow:
# 1. Define error model as Kraus operators or Lindbladian
# 2. Plaquette compiles to appropriate sampler representations
# 3. Run FTQC simulation with selected sampler
# 4. Extract logical error rates, thresholds, overheads
# 5. Compare across sampler classes for validation
```

## References

- arXiv:2607.08767 "Plaquette: A hardware-aware design platform for fault-tolerant quantum computers"
- Authors: Conchello Vendrell et al.
