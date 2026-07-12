---
name: branched-optimal-transport-brain-mapping
description: "Branched optimal transport framework for inferring stimulus-to-reaction propagation architectures in brain networks. Uses anisotropic branched OT where concavity of flux cost promotes aggregation and branching. Activation: branched optimal transport, stimulus reaction brain mapping, ramified transport brain, brain propagation architecture, optimal transport neuroscience."
---

# Branched Optimal Transport for Brain Mapping

> Variational framework for inferring stimulus-to-reaction routing architectures in the brain using anisotropic branched optimal transport, treating the transport network itself as unknown rather than fixed.

## Metadata
- **Source**: arXiv:2603.19751
- **Authors**: Cristian Mendico
- **Published**: 2026-03-20
- **Categories**: math.OC, q-bio.NC, q-bio.QM

## Core Methodology

### Key Innovation
Traditional brain state transition models control trajectories on a **fixed** network substrate. This work inverts the problem: the **transport network itself** is the inferred object, modeled as a graph/current connecting a stimulation source measure to a reaction target measure.

### Technical Framework

1. **Anisotropic Branched OT Formulation**
   - Model as variational problem: find optimal current (graph) connecting source measure μ (stimulation) to target measure ν (reaction)
   - Flux cost function is concave → promotes aggregation and branching
   - Support of optimal current defines stimulus-to-reaction routing architecture

2. **Existence Theory**
   - Proved existence of minimizers in both discrete and continuous formulations
   - Discrete: finite graph with edge currents
   - Continuous: measure-theoretic formulation on manifold

3. **Hybrid Stochastic Extension**
   - Combines ramified transport with path-space KL control cost
   - Induced graph dynamics incorporate stochasticity
   - Provides probabilistic interpretation of routing uncertainty

### Mathematical Structure
```
minimize: ∫ c(θ) d|J|(θ) + KL(Path || Reference)
subject to: div(J) = ν - μ (continuity equation)
where: J = optimal current, c = concave flux cost
```

## Applications
- Inferring brain reaction maps from stimulation experiments
- Mapping neural propagation pathways without pre-defined connectivity
- TMS/tDCS stimulation response prediction
- Understanding brain network plasticity through optimal routing

## Implementation Guide

### Prerequisites
- Optimal transport library (POT, geomloss)
- Graph optimization tools
- Numerical PDE solvers for continuous formulation

### Step-by-Step
1. Define source measure μ (stimulation region) and target measure ν (reaction region)
2. Choose concave flux cost function c(θ) (e.g., θ^α, α < 1)
3. Solve discrete branched OT on candidate graph
4. Validate with continuous formulation via level-set methods
5. Extend to stochastic version with KL control cost for uncertainty quantification

### Pitfalls
- Concave optimization is non-convex → multiple local minima possible
- Discrete approximation may miss fine-scale branching structure
- Stochastic extension adds computational complexity
- Requires careful regularization for numerical stability

## Related Skills
- optimal-transport-brain
- brain-network-controllability
- brain-stimulation-dynamics-state
- adaptive-flow-routing-brain-networks
