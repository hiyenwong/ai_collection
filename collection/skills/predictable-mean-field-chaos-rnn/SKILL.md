---
name: predictable-mean-field-chaos-rnn
description: Predictable Mean-Field Chaos in Random Recurrent Networks methodology — Krylov state space analysis revealing latent determinism in mean-field dynamics for analytic nonlinearities with fast Fourier decay. Demonstrates that microscopic sensitivity and predictive complexity are distinct aspects of chaos. Use when: analyzing RNN chaos, mean-field theory, Krylov complexity, Lyapunov exponents, Hamiltonian chaotic dynamics, classical dissipative systems, or prediction theory in recurrent networks.
---

# Predictable Mean-Field Chaos in Random Recurrent Networks

## Background

Dynamical mean-field theory recasts deterministic chaos in random recurrent networks as an effective stochastic process. This skill provides theoretical and computational tools for analyzing when this stochasticity is only apparent, and the mean-field trajectory is uniquely determined by its continuous past.

## Core Innovation

For analytic nonlinearities with sufficiently fast Fourier decay, mean-field stochasticity is **only apparent**: the continuous past of a realized mean-field trajectory **uniquely determines its future**.

### Key Theoretical Result

Mean-field theory is not merely an ensemble description, but a **conditional prediction theory** for individual trajectories.

## Methodology

### Krylov State Space Unfolding

Unfolding the power spectrum into a **Krylov state space** exposes how latent determinism is organized across an infinite hierarchy of temporal modes.

### Complexity Bounds

The **Krylov growth rate**:
- Sets the complexity of finite-resolution prediction
- Upper-bounds the largest Lyapunov exponent in this class of networks

### Distinction Framework

**Microscopic sensitivity ≠ Predictive complexity**

Two distinct aspects of mean-field chaos:
- Microscopic sensitivity: exponential divergence of nearby trajectories
- Predictive complexity: information needed for finite-resolution prediction

## Technical Details

### Required Conditions

1. **Analytic Nonlinearities**: Activation functions must be analytic
2. **Fast Fourier Decay**: Fourier coefficients decay sufficiently rapidly
3. **Random Recurrent Structure**: Networks with random weight matrices

### Prediction Theory Structure

Mean-field predictions are:
- **Conditional**: Based on continuous past trajectory
- **Deterministic**: Past uniquely determines future (under conditions)
- **Hierarchical**: Organized by Krylov temporal modes

## Applications

### Research Use Cases

1. **RNN Chaos Analysis**: Characterize chaos in random recurrent networks
2. **Mean-Field Prediction**: Develop conditional prediction for trajectories
3. **Complexity Quantification**: Measure predictive vs. microscopic complexity
4. **Lyapunov Analysis**: Upper-bound Lyapunov exponents via Krylov growth
5. **Hamiltonian-Dissipative Bridge**: Extend Krylov ideas to classical dissipative systems

### Computational Neuroscience

- **Neural Population Dynamics**: Predict mean-field trajectories in large networks
- **Attractor Analysis**: Understand determinism in chaotic attractors
- **Complexity Measures**: Separate sensitivity from predictability

### Machine Learning

- **RNN Training**: Understanding chaos in trained recurrent networks
- **Prediction Bounds**: Set finite-resolution prediction complexity limits
- **Stability Analysis**: Quantify microscopic sensitivity vs. macroscopic predictability

## Theoretical Framework

### Krylov Growth Rate

The Krylov growth rate $λ_K$ satisfies:
```
λ_K ≥ λ_max (largest Lyapunov exponent)
λ_K = complexity of finite-resolution prediction
```

This inequality formalizes the distinction:
- Microscopic divergence: measured by Lyapunov exponent
- Macroscopic prediction: bounded by Krylov complexity

### Temporal Mode Hierarchy

Krylov state space reveals:
- Infinite hierarchy of temporal modes
- Organization of latent determinism
- Information flow across scales

## Implementation Considerations

### Analyticity Verification

1. Check activation function analyticity (e.g., sigmoid, tanh)
2. Verify Fourier coefficient decay rate
3. Confirm sufficient decay condition

### Krylov Analysis

1. Compute power spectrum of mean-field trajectory
2. Unfold spectrum into Krylov state space
3. Extract Krylov growth rate
4. Compare with Lyapunov exponent bounds

### Prediction Protocol

For finite-resolution prediction:
1. Determine required resolution
2. Compute Krylov complexity bound
3. Assess prediction feasibility
4. Implement conditional prediction algorithm

## Key Results

### Theoretical Proofs

1. **Uniqueness**: Continuous past determines future (under conditions)
2. **Hierarchy**: Krylov modes organize latent determinism
3. **Complexity Bound**: Krylov growth upper-bounds Lyapunov exponent
4. **Dissipative Extension**: Krylov ideas apply beyond Hamiltonian systems

### Empirical Validation

Simulations demonstrate:
- Mean-field trajectories are predictable from continuous past
- Krylov growth rate bounds Lyapunov exponents
- Finite-resolution prediction complexity matches theoretical bounds

## Related Skills

- `neural-dynamics-analysis`: General neural dynamics analysis framework
- `chaos-synchrony-ei-networks`: Chaos theory for excitatory-inhibitory networks
- `mean-field-neural-optimization`: Mean-field methods for neural optimization
- `rnn-task-degradation-analysis`: RNN initialization and performance analysis

## Pitfalls

### Theory Limitations

1. **Analyticity Requirement**: Many practical RNNs use non-analytic activations (ReLU)
2. **Fourier Decay**: Slow decay cases not covered by theory
3. **Resolution Dependence**: Prediction requires sufficient temporal resolution

### Computational Challenges

1. **Krylov Computation**: High computational cost for large networks
2. **Lyapunov Estimation**: Numerical Lyapunov exponents may be inaccurate
3. **Continuous Past**: Practical data is discrete, not continuous

## Key References

- **arXiv:2606.08805v1** - "Predictable Mean-Field Chaos in Random Recurrent Networks" (Yadav et al., 2026)
- **Hamiltonian Chaos**: Krylov growth theory for quantum/classical chaotic dynamics
- **Mean-Field Theory**: Dynamical mean-field theory for random networks

## Activation Keywords

- mean-field chaos
- RNN chaos analysis
- Krylov complexity
- Lyapunov exponent bounds
- conditional prediction
- deterministic chaos
- dissipative dynamics
- Fourier decay analysis
- temporal mode hierarchy
- microscopic sensitivity

## Summary

This methodology bridges mean-field theory and prediction theory, showing that for analytic nonlinearities with fast Fourier decay, mean-field chaos is predictable from continuous past. The Krylov growth rate provides a complexity bound distinct from microscopic sensitivity, extending Hamiltonian chaotic dynamics ideas to classical dissipative recurrent networks. This framework enables conditional prediction of mean-field trajectories and formalizes the distinction between exponential divergence (Lyapunov) and prediction complexity (Krylov).