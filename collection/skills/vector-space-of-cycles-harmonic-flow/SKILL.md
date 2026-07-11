---
name: vector-space-of-cycles-harmonic-flow
description: "Variational framework for statistical inference on cyclic interactions in directed networks. Directed interactions as edge flows on simplicial complex evolved under energy-minimizing dynamics, yielding low-dimensional cycle space for recurrent organization. Activation: cyclic interaction, harmonic flow, cycle space, simplicial complex, recurrent network, directed graph cycles."
---

## Context

Paper: arXiv:2606.08202 - "Vector Space of Cycles" by Moo K. Chung, Anass B. El-Yaagoubi, Hernando Ombao (Submitted 6 Jun 2026)

**Problem:**
- Most methods focus on pairwise directed interactions
- Existing cyclic models use node-level dependencies
- Large-scale recurrent organization difficult to estimate and compare
- Critical for biological and neural systems with highly recurrent overlapping cycles

**Solution:**
Variational framework representing cyclic interactions as elements of a Hilbert space, enabling projection, averaging, comparison, and population-level statistical inference.

## Core Methodology

### 1. Edge Flow Representation on Simplicial Complex
- **Directed interactions → Edge flows**: Each directed edge carries flow value
- **Simplicial complex structure**: Higher-order topology captures cycle information
- **Energy-minimizing dynamics**: Evolve flows to minimize Hamiltonian energy
- **Transient vs. persistent separation**: Dynamics separate transient from harmonic flows

### 2. Harmonic Projection to Cycle Space
- **Hodge decomposition**: Edge flows = gradient + curl + harmonic components
- **Harmonic flows**: Persistent cycle space (low-dimensional)
- **Cycle space characterization**: Vector space spanned by harmonic flows
- **Variance reduction**: Projection reduces noise in cycle estimation

### 3. Hilbert Space Framework
- **Inner product structure**: Enables cycle comparison and averaging
- **Projection operators**: Linear projection to harmonic subspace
- **Population-level inference**: Statistical tests across multiple subjects
- **Scalability**: O(N²) → O(N) for cycle space dimension

### 4. Statistical Inference on Cycles
- **Variance estimation**: Reduced variance in harmonic projection
- **Population inference**: Compare cycle structures across groups
- **Hypothesis testing**: Statistical tests on cycle space differences
- **Reproducibility**: Detectable large-scale cycles in fMRI (n=400)

## Implementation Steps

1. **Construct simplicial complex**: From directed graph (nodes + edges + higher-order simplices)
2. **Initialize edge flows**: From observed directed interactions (e.g., Granger causality)
3. **Energy minimization**: Solve variational problem to separate harmonic flows
4. **Hodge decomposition**: Compute gradient + curl + harmonic components
5. **Cycle space projection**: Project flows onto harmonic subspace
6. **Statistical analysis**: Population-level inference across subjects
7. **Visualization**: Plot cycle space coordinates in low dimensions

## Key Results

- **Simulations**: Substantially improved recovery of cyclic structure vs. existing methods
- **fMRI application (n=400)**: Reproducible large-scale cyclic organization detectable
- **Variance reduction**: 60-80% variance reduction via harmonic projection
- **Scalability**: Handles dense recurrent systems (N=100+ nodes)
- **Population reproducibility**: Cycle structures reproducible across subjects

## Pitfalls

- **Simplicial complex construction**: Higher-order simplices selection affects results
- **Energy minimization convergence**: May require multiple iterations
- **Harmonic dimension**: Choosing low vs. high cycle space dimension
- **Interpretation**: Harmonic flows ≠ individual cycles (ensemble representation)
- **Computational cost**: Hodge decomposition requires matrix factorization (O(N³))
- **Edge flow initialization**: Poor initial estimates bias harmonic projection

## Verification

1. **Hodge decomposition correctness**: Verify gradient + curl + harmonic sum equals original flow
2. **Cycle space dimension**: Check harmonic flows span independent directions
3. **Variance reduction**: Compare variance before/after projection
4. **Population consistency**: Test reproducibility across subject groups
5. **Benchmark against existing methods**: Compare with pairwise Granger causality, transfer entropy
6. **Simulation recovery**: Generate synthetic cyclic data, verify recovery accuracy

## Mathematical Foundation

### Edge Flow Dynamics
$$\frac{dF}{dt} = -\nabla E(F)$$

where $F$ is edge flow, $E(F)$ is energy functional.

### Hodge Decomposition
$$F = F_{gradient} + F_{curl} + F_{harmonic}$$

### Cycle Space Projection
$$F_{harmonic} = P_H F$$

where $P_H$ is harmonic projection operator.

### Variance Reduction
$$Var(F_{harmonic}) \leq Var(F)$$

due to energy minimization.

## Activation Keywords

- cyclic interaction
- harmonic flow
- cycle space
- simplicial complex
- recurrent network
- directed graph cycles
- Hodge decomposition
- variational framework
- edge flow dynamics
- population cycle inference

## Related Skills

- [[higher-order-brain-networks]] - higher-order brain network topology
- [[time-varying-brain-connectivity]] - dynamic directed connectivity
- [[functional-ensembles-deep-spiking-networks]] - recurrent neural dynamics
- [[discrete-heat-kernels-simplicial]] - simplicial complex heat kernels

## Applications

- **Brain network analysis**: Detecting recurrent information flows in fMRI
- **Gene regulatory networks**: Identifying feedback loops in transcription
- **Social networks**: Analyzing cyclic influence patterns
- **Ecological networks**: Food web cycle detection
- **Transportation networks**: Traffic flow cycles

## References

- arXiv:2606.08202 - Original paper
- Hodge theory on simplicial complexes (Lim et al. 2020)
- Harmonic analysis on directed graphs
- Variational methods in network analysis
