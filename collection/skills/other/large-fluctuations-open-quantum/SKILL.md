---
name: large-fluctuations-open-quantum
description: "Large fluctuation theory for open quantum systems — analyzing atypical measurement outcomes in driven dissipative steady states. Shows large-deviation functions develop lines and surfaces with discontinuous derivatives, unlike equilibrium analytic Wigner functions. Provides framework for rare event statistics in non-equilibrium quantum systems. Activation: large fluctuations, open quantum systems, large-deviation, non-equilibrium, driven dissipative, Wigner function, rare events, steady state statistics, atypical outcomes"
metadata:
  arxiv_id: "2606.11822"
  published: "2026-06-10"
  authors: "V. Yu. Mylnikov, S. O. Potashin, A. Kamenev"
  tags: [quantum, open-systems, large-deviation, non-equilibrium, statistical-physics, fluctuations]
---

## Large Fluctuations in Open Quantum Systems

### Core Insight

In equilibrium, probability distributions over phase space (e.g., Wigner functions) are analytic in phase-space coordinates. In driven dissipative quantum systems, this property is generically lost: large-deviation functions develop lines and surfaces where derivatives are discontinuous.

### Mathematical Framework

#### Large-Deviation Function

For steady-state probability distribution P(α) in phase space:

```
P(α) ~ exp(-N · Φ(α))
```

where Φ(α) is the large-deviation function and N is a large parameter (e.g., photon number, system size).

#### Key Phenomenon: Non-Analyticity

- **Equilibrium**: Φ(α) is smooth and analytic everywhere
- **Driven dissipative**: Φ(α) develops non-analytic structures:
  - Lines (1D) in 2D phase space where derivatives jump
  - Surfaces (2D) in higher dimensions
  - Caused by competing relaxation pathways

### Analysis Methodology

1. **Identify steady state** of driven dissipative system
2. **Compute large-deviation function** Φ(α) via path integral or Keldysh technique
3. **Locate non-analytic structures** (caustics, shock lines)
4. **Classify singularity type** (first-order, second-order transitions)
5. **Relate to physical observables** (measurement outcome probabilities)

### Physical Interpretation

Non-analytic large-deviation functions indicate:
- **Phase transitions in fluctuation space**: Different fluctuation mechanisms dominate in different regions
- **Optimal fluctuation paths**: Most likely trajectory to rare state changes abruptly
- **Dynamical phase coexistence**: Multiple competing steady-state configurations

### When to Apply

- Rare event analysis in quantum optics
- Quantum jump statistics in driven systems
- Non-equilibrium phase transitions
- Quantum thermodynamics of small systems
- Measurement-induced phase transitions

### Pitfalls

- Large-deviation asymptotics require large N — finite-size corrections significant
- Non-analyticity location depends sensitively on driving parameters
- Path integral formulation may have multiple saddle points
- Numerical evaluation of large-deviation functions challenging in high dimensions
