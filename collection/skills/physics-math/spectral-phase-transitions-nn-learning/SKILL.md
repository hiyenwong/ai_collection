---
name: spectral-phase-transitions-nn-learning
description: "Spectral phase transitions and trainability in neural network learning dynamics methodology. Formulates NN training as stochastic evolution of random matrix ensembles, showing BBP (Baik-Ben Arous-Péché) transitions during SGD where isolated eigenvalues detach from random bulk. Derives phase diagram of trainability governed by step size and initial weight variance. Links spectral analysis to representation formation, optimisation hyperparameters, and generalization. Use when: analyzing neural network weight matrix spectra, understanding training dynamics through random matrix theory, BBP transition, spectral alignment, trainability phase diagrams, representation formation in high-dimensional learning."
---

# Spectral Phase Transitions in Neural Network Learning Dynamics

## Overview

Neural network training reformulated as the stochastic evolution of an initially random matrix ensemble, driven by SGD updates that reshape the spectral bulk while amplifying signal strength. The key insight is that a **Baik-Ben Arous-Péché (BBP) transition** occurs during training: isolated eigenvalues detach from the random bulk distribution, providing a dynamical framework for representation formation.

**arXiv**: 2606.28486 (Submitted 26 Jun 2026)
**Authors**: Chanju Park, Dario Bocchi, Francesco D'Amico, Biagio Lucini, Gert Aarts

## Core Methodology

### 1. Spectral Evolution Framework
- Model weight matrix **W** as evolving random matrix ensemble
- SGD updates reshape spectral bulk distribution while amplifying signal eigenvalues
- Track Marchenko-Pastur (MP) bulk distribution evolution during training
- Monitor emergence of outlier eigenvalues that detach from bulk

### 2. BBP Transition During Training
The Baik-Ben Arous-Péché (BBP) transition describes when isolated eigenvalues spike above the random bulk edge:
- **Below transition**: All eigenvalues confined within MP bulk (untrained regime)
- **Above transition**: Signal eigenvalues spike above bulk edge (learned representations)
- Transition threshold governed by signal-to-noise ratio in the weight updates

### 3. Linear Teacher-Student Model (Analytically Tractable)
- Solvable model where spectral evolution is fully analytical
- Phase diagram obtained in terms of:
  - **Step size (learning rate)** η
  - **Initial weight variance** σ²
- Trainability regions mapped as spectral phase boundaries
- Extension to nonlinear and stochastic settings beyond linear regime

### 4. Phase Diagram of Trainability
Three phases identified:
1. **Tractable training**: BBP transition occurs, representations form
2. **No signal emergence**: Step size too small or variance too large, eigenvalues stay in bulk
3. **Unstable**: Step size too large, spectral evolution diverges

## Key Equations

### Spectral Evolution
```
W(t+1) = W(t) - η ∇L(W(t))
```
The eigenvalue distribution ρ(λ, t) evolves as:
- Bulk follows MP-like distribution with time-dependent parameters
- Signal eigenvalues λ_i(t) grow above bulk edge λ+(t)

### BBP Transition Criterion
```
λ_signal / λ+ > 1  →  isolated eigenvalue regime
```
where λ+ is the upper edge of the MP bulk.

### Trainability Phase Boundary
```
η * σ² < η_crit  →  trainable
η * σ² > η_crit  →  divergent/no learning
```

## Practical Applications

### For Weight Matrix Spectral Analysis
1. Compute eigenvalue spectrum of layer weight matrices at checkpoints
2. Fit Marchenko-Pastur distribution to bulk
3. Identify outlier eigenvalues above λ+
4. Track BBP transition timing across layers

### For Hyperparameter Selection
1. Use phase diagram to select learning rate given initial variance
2. Monitor spectral alignment during training as convergence diagnostic
3. Early stopping when spectral structure stabilizes

### For Representation Analysis
- Spectral alignment as proxy for representation quality
- Compare spectral evolution across architectures
- Identify layers where representations form first

## Extensions Beyond Linear Regime

### Nonlinear Networks
- Random matrix theory for nonlinear activations (ReLU, tanh)
- Spectral evolution modified by activation function derivatives
- BBP transition generalized to feature map settings

### Stochastic Settings
- Mini-batch noise as additional spectral perturbation
- Batch size affects transition sharpness
- Connection to sharpness-aware minimization

## Key Results

1. **Robust spectral alignment**: Numerical simulations confirm emergence in realistic settings
2. **Unified perspective**: Links trainability, hyperparameters, spectral transitions, and representation learning
3. **Phase diagram**: Analytical trainability boundaries in (η, σ²) space
4. **BBP as learning signature**: Transition timing correlates with representation formation

## Relationship to Other Approaches

- **NTK regime**: Spectral analysis complements Neural Tangent Kernel theory
- **Lottery Ticket Hypothesis**: Sparse signal eigenvalues relate to winning tickets
- **Spectral Norm Regularization**: BBP transition provides principled regularization target
- **Mean-field theory**: Connects to mean-field analysis of wide networks

## Pitfalls

- Linear model results may not directly transfer to deep nonlinear networks
- Spectral analysis of individual layers may miss inter-layer dynamics
- MP distribution assumes i.i.d. entries; structured initialization deviates
- BBP transition sharpness depends on dimensionality

## References

- Baik, Ben Arous, Péché (2005) - Original BBP transition for sample covariance
- Marchenko-Pastur (1967) - Limiting spectral distribution
- Pennington, Schoenholz, Ganguli (2017) - Nonlinear random matrix theory for NNs
- Martin & Mahoney (2018) - Heavy-tailed self-regularization in NN weight matrices

## Activation Keywords

spectral phase transition, BBP transition, random matrix theory neural network, trainability phase diagram, spectral alignment, Marchenko-Pastur, weight matrix spectrum, representation formation, learning dynamics, stochastic gradient descent spectral
