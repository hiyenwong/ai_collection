---
name: thermodynamics-quantum-reservoir-computing
description: Non-equilibrium thermodynamic framework for quantum reservoir computing - links predictive performance to energetic costs via Holevo capacities and quantum informational dissipation
category: ai_collection
tags: [quantum-reservoir-computing, thermodynamics, neuromorphic, energy-efficiency, quantum-criticality, landauer-bound]
created: 2026-07-08
source: arXiv:2607.02157
---

# Thermodynamics of Quantum Reservoir Computing

## Core Methodology

Establishes non-equilibrium thermodynamic framework linking macroscopic predictive performance of driven open quantum systems to microscopic energetic costs.

### Key Technical Components

1. **Holevo Capacity Mapping**: Maps computational capacity onto Bogoliubov-Kubo-Mori (BKM) geometric manifold
   - BKM metric: g_BKM(ρ)[A,B] = Tr(ρ L_A L_B) where L_A is symmetric logarithmic derivative
   - Connects information geometry to thermodynamic costs

2. **Quantum Critical Resonance**: Proves computational peak in quantum critical region originates from spectral resonance
   - Energy gap closing forces reservoir transition frequencies to align with chaotic drive
   - Criticality = optimal predictive capacity

3. **Quantum Informational Dissipation**: New quantity measuring non-predictive historical data retention
   - QID(ρ) = S(ρ) - S(ρ_predicted) where S is von Neumann entropy
   - Quantifies "wasted" memory on irrelevant past information

4. **Generalized Landauer Bound**: Derives bound for continuous temporal processing
   - W_erase ≥ kT · QID per unit time
   - Links information retention to thermodynamic work cost

5. **Coherence Decomposition**: Separates dynamic vs static quantum coherences
   - Dynamic coherences strictly amplify predictive capacity
   - No additional mechanical work required for coherence-enhanced computation

## Fundamental Trade-off

**Critical resonance that unlocks optimal predictive capacity inherently maximizes informational dissipation and irreversible work required for environmental erasure.**

This reveals: you cannot have both maximum computation AND minimum energy cost at criticality.

## Applications

- Design principles for energy-efficient quantum neuromorphic hardware
- Benchmarking quantum reservoir computers against thermodynamic limits
- Understanding fundamental costs of quantum machine learning
- Optimizing quantum reservoir parameters for specific energy budgets

## Key Equations

```
Computational capacity: C(ρ) = χ(ρ) = S(ρ_avg) - Σ p_i S(ρ_i)
Thermodynamic cost: W ≥ kT · [QID(ρ) + ΔS_env]
Critical enhancement: C_critical / C_off-critical ~ ξ^z where ξ is correlation length
```

## Implementation Notes

- Requires open quantum system simulation (Lindblad master equation)
- BKM metric computation: expensive for large Hilbert spaces
- QID estimation: needs access to full density matrix, not just observables
- Critical point identification: scan driving frequency vs system gap

## Related Concepts

- [[quantum-reservoir-computing]]
- [[non-equilibrium-thermodynamics]]
- [[quantum-criticality]]
- [[information-geometry]]
- [[landauer-principle]]
- [[quantum-neuromorphic]]

## Activation Keywords

quantum reservoir thermodynamics, energy-efficient quantum ML, quantum critical computation, informational dissipation, BKM manifold, Holevo capacity, Landauer bound quantum, neuromorphic energy limits
