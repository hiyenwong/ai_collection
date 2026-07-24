---
name: spectral-theory-population-density-spiking-neurons
title: Spectral Theory for Population Density Dynamics of Spiking Neurons with Refractoriness
description: Rigorous operator-theoretic framework for neuronal population dynamics with finite refractory time, providing complete spectral characterization and exact transfer functions.
arxiv_id: 2607.20699
date: 2026-07-22
authors:
  - Luca Falorsi
  - Gianni Valerio Vinci
  - Maurizio Mattia
categories:
  - q-bio.NC
  - math-ph
  - math.SP
trigger_words:
  - spectral theory
  - population density
  - spiking neurons
  - refractoriness
  - Fokker-Planck operator
  - oscillatory modes
  - transfer function
---

# Spectral Theory for Population Density Dynamics of Spiking Neurons with Refractoriness

## Overview
This paper develops a rigorous operator-theoretic framework for neuronal population dynamics with a finite refractory time by augmenting the state space to include refractory history and formulating the problem as a non-self-adjoint boundary eigenvalue problem for the Fokker-Planck operator.

## Key Contributions

### 1. Mathematical Framework
- **State Space Augmentation**: Incorporates refractory history into the population density approach
- **Non-Self-Adjoint Boundary Eigenvalue Problem**: Formulates the Fokker-Planck operator as a boundary eigenvalue problem
- **Spectral Characterization**: Provides complete spectral characterization of the generator
- **Dissipativity Proof**: Proves dissipativity and existence of a contraction semigroup

### 2. Exceptional Points and Oscillatory Modes
- **Defective Eigenvalues**: Identifies defective eigenvalues as exceptional points
- **Mode Emergence**: Shows how oscillatory modes emerge from coalescing relaxational modes at exceptional points

### 3. Exact Transfer Function
- **Boundary Conditions**: Derives exact transfer function accounting for boundary conditions modulated by external input
- **Threshold-Noise Contributions**: Reveals additional threshold-noise contributions missed in previous heuristic derivations
- **Correction of Previous Work**: Corrects previous heuristic derivations in the literature

### 4. Network Stability Analysis
- **Mean-Field Approximation**: Uses the transfer function under mean-field approximation
- **Limit Cycle Onset**: Demonstrates that refractoriness can facilitate the onset of stable oscillations (limit cycles) in firing rate
- **Network Stability**: Provides insights into how refractoriness affects network stability

## Applications

### Computational Neuroscience
- **Spectral Decomposition Methods**: Provides rigorous foundation for spectral decomposition methods
- **Population Density Modeling**: Enables accurate modeling of neuronal populations with refractoriness
- **Network Dynamics**: Improves understanding of network stability and oscillatory behavior

### Mathematical Physics
- **Operator Theory**: Advances operator-theoretic approaches to neural dynamics
- **Spectral Theory**: Contributes to spectral theory applications in biological systems
- **Fokker-Planck Equations**: Extends Fokker-Planck equation analysis to include refractory periods

## Implementation Guidelines

### When to Use This Approach
- Modeling neuronal populations with significant refractory periods
- Analyzing network stability and oscillatory dynamics
- Developing spectral decomposition methods for neural systems
- Studying the effects of refractoriness on transfer functions

### Key Parameters to Consider
- **Refractory Time**: Finite refractory period duration
- **Noise Level**: Threshold noise contributions
- **Input Modulation**: How external inputs affect boundary conditions
- **Network Connectivity**: Mean-field coupling strength

## Verification Steps

1. **Spectral Analysis**: Verify the spectral decomposition of the Fokker-Planck operator
2. **Transfer Function Validation**: Compare derived transfer function with numerical simulations
3. **Oscillation Detection**: Check for limit cycle emergence in network simulations
4. **Exceptional Point Identification**: Locate defective eigenvalues in parameter space

## Related Skills
- `spiking-neural-network-analysis`
- `neural-dynamics-analysis-methodology`
- `fokker-planck-neural-dynamics`
- `spectral-analysis-brain-networks`

## References
- arXiv:2607.20699 [q-bio.NC]
- DOI: https://doi.org/10.48550/arXiv.2607.20699