---
name: quantum-transport-statistics-framework
description: "Exact framework for evaluating heat, energy, and particle transport statistics in quadratic quantum systems. Combines full counting statistics with non-Markovian master equation approaches for Gaussian reservoir transport analysis."
tags: ["quantum", "statistics", "transport", "thermodynamics", "open-systems"]
related_skills: ["quantum-statistical-estimation", "quantum-dephasing-dynamics"]
---

# Quantum Transport Statistics Framework

Exact framework for evaluating transport statistics in quadratic quantum systems mediated between Gaussian reservoirs. Based on arXiv:2602.21190.

## Core Concept

Combines full counting statistics (FCS) with newly developed non-Markovian master equation approaches to evaluate heat, energy, and particle transport between Gaussian reservoirs mediated by a quadratic quantum system.

## Methodology

### Full Counting Statistics

1. **Counting field introduction**: Introduce counting field χ to track transfer of conserved quantities
2. **Generating function**: Compute moment generating function G(χ,t) = Tr[ρ(χ,t)]
3. **Cumulants**: Extract current, noise, and higher cumulants from derivatives of G(χ,t)

### Non-Markovian Master Equation

1. **System-reservoir coupling**: Model quadratic system coupled to Gaussian reservoirs
2. **Influence functional**: Derive exact influence functional for Gaussian environments
3. **Memory kernel**: Account for non-Markovian effects through time-nonlocal kernel
4. **Efficient computation**: Numerically efficient method avoiding full Hilbert space evolution

### Key Results

- Exact evaluation of all transport cumulants (current, noise, skewness, etc.)
- Valid for arbitrary system-reservoir coupling strength
- Applicable to fermionic and bosonic systems
- Computationally efficient compared to full numerical approaches

## Mathematical Framework

```
Current:     I = d/dχ log G(χ,t) |_{χ=0}
Noise:       S = d²/dχ² log G(χ,t) |_{χ=0}
Higher cumulants: C_n = dⁿ/dχⁿ log G(χ,t) |_{χ=0}
```

## Applications

- **Quantum thermoelectric devices**: Heat-to-work conversion efficiency
- **Mesoscopic transport**: Electron transport through quantum dots
- **Open quantum systems**: Decoherence and dissipation analysis
- **Quantum heat engines**: Performance bounds for nanoscale engines

## Implementation Considerations

- **Gaussian approximation**: Requires quadratic Hamiltonian structure
- **Reservoir assumptions**: Gaussian (non-interacting) reservoir states
- **Numerical stability**: Memory kernel discretization and convergence

## Activation

**Keywords**: quantum transport, full counting statistics, non-Markovian master equation, Gaussian reservoirs, heat transport, particle transport, energy transport, open quantum systems, quantum thermodynamics
**arXiv**: 2602.21190
**Categories**: quant-ph, cond-mat.mes-hall, cond-mat.stat-mech
