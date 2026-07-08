---
name: quantum-lbm-surrogate
description: Hybrid quantum-classical surrogate model for Lattice Boltzmann Method (LBM) collision dynamics. Uses parameterized quantum circuits with data re-uploading to implement partial Fourier series, recovering complete BGK collision dynamics across full physically admissible range of relaxation without retraining. Use when building quantum surrogates for PDE solvers, fluid dynamics, or any physics simulation requiring non-unitary operation approximation.
version: 1.0.0
tags: [quantum, surrogate-model, LBM, fluid-dynamics, VQC, PDE, non-unitary, data-reuploading, physics-simulation]
source: arXiv:2606.31351
authors: [Lukas C. Birk, David M. Wawrzyniak, Josef M. Winter, Steffen J. Schmidt, Thomas Indinger, Christian F. Janßen, Nikolaus A. Adams]
published: 2026-06-30
category: quantum-computing
trigger_words: [quantum surrogate LBM, quantum fluid dynamics, quantum collision operator, quantum PDE solver, VQC expressibility, data re-uploading quantum, quantum BGK collision]
---

# Quantum LBM Surrogate Model

## Core Insight

Pure quantum solvers struggle with non-unitary operations. A hybrid approach uses a quantum machine learning surrogate to approximate non-linear collision dynamics of the Lattice Boltzmann Method (LBM), effectively offloading the non-unitary operations that challenge pure quantum solvers.

## Architecture

### 1. Parameterized Quantum Circuit (VQC) Surrogate
- **Expressivity source**: Parameterized quantum circuits implement partial Fourier series
- **Data re-uploading**: Extends the spectrum of representable frequencies
- **Complete BGK recovery**: Surrogate recovers complete Bhatnagar-Gross-Krook collision dynamics across the full physically admissible range of relaxation parameters WITHOUT retraining

### 2. Why This Works
- LBM collision operator is non-unitary (cannot be directly implemented on quantum hardware)
- VQC with data re-uploading can approximate arbitrary functions via Fourier series
- The surrogate learns the mapping: input distribution → post-collision distribution
- Once trained, it works across ALL physically valid relaxation parameters

## Implementation Pattern

```python
# Conceptual workflow
1. Generate training data from classical BGK collision operator
   - Sample across full range of relaxation parameters (τ ∈ [0.5, 2.0])
   - Include diverse flow configurations

2. Design VQC with data re-uploading
   - Encode input distribution states
   - Apply parameterized gates with trainable angles
   - Re-upload data multiple times to extend frequency spectrum
   - Measure output distribution

3. Train VQC to minimize surrogate error
   - Loss: ||f_post_collision - VQC_output||²
   - Use gradient-based or gradient-free optimization

4. Validate on benchmark problems
   - Taylor-Green vortex (energy dissipation)
   - Double shear layer (shear-driven instabilities)

5. Assess VQC metrics
   - Expressibility → surrogate accuracy
   - Entanglement capability → representational power
   - Effective dimension → generalization capacity
```

## Key Findings

### VQC Metric Relevance
- **Expressibility**: Directly correlates with surrogate accuracy for complex flow regimes
- **Entanglement capability**: Determines ability to capture multi-point correlations
- **Effective dimension**: Predicts generalization to unseen flow configurations
- **Key architectural parameters**: Circuit depth, number of re-uploads, entangling gate placement

### Validation Results
- **Taylor-Green vortex**: High accuracy in energy dissipation rates
- **Double shear layer**: Accurate shear-driven instability prediction
- **Nonlinear flow evolution**: Closely replicates classical solutions
- **Generalizability**: Works across full relaxation parameter range without retraining

## Pitfalls

- **Non-unitary barrier**: Pure quantum solvers cannot directly implement non-unitary collision
- **Training data quality**: Surrogate accuracy depends on representative training coverage
- **Circuit depth tradeoff**: Deeper circuits = more expressivity but more noise on NISQ
- **Data re-uploading cost**: Each re-upload increases circuit depth linearly
- **Metric-task mismatch**: Standard VQC metrics may not predict task-specific performance

## Practical Applications

### Fluid Engineering
- Aerodynamic simulation acceleration
- Turbulence modeling with quantum surrogates
- Real-time flow control optimization

### Beyond Fluids - General Pattern
- Any PDE with non-unitary/non-linear operators
- Plasma physics collision operators
- Radiative transfer equations
- Chemical reaction kinetics

### Financial Applications
- Option pricing with non-linear PDEs (Black-Scholes extensions)
- Risk model surrogates for Monte Carlo acceleration
- Volatility surface approximation

## Activation

Use when:
- Building quantum surrogates for classical PDE solvers
- Needing to approximate non-unitary operations on quantum hardware
- Designing hybrid quantum-classical physics simulations
- Assessing VQC expressibility for specific tasks
- Offloading non-linear dynamics to quantum ML surrogates
