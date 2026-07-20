---
name: cavity-method-rnn-analysis
description: >
  Two-site cavity method for analyzing large nonlinear recurrent neural networks.
  Derives linear equivalence of nonlinear RNNs, computes full covariance matrices
  for specific quenched realizations, and separates Gaussian from non-Gaussian
  contributions in recurrent network dynamics. Use when analyzing: (1) high-dimensional
  RNN covariance structure, (2) nonlinear-to-linear network equivalence, (3) cavity
  method applications to neural dynamics, (4) quenched disorder in recurrent networks.
---

# Cavity Method for RNN Analysis

## Overview

The two-site cavity method provides analytical tools for understanding large nonlinear
recurrent neural networks with random couplings. Key insight: at large N, the covariance
matrix of a nonlinear RNN takes the same form as a linear network with the same couplings,
driven by independent noise, with mean-field order parameters setting the effective
transfer function and noise spectrum.

## Core Methodology

### Problem Setup

Consider an RNN with dynamics:
```
dx_i/dt = -x_i + sum_j J_ij phi(x_j) + I_i
```
where J_ij are random couplings (quenched disorder), phi is a nonlinear activation,
and I_i is external input.

### Two-Site Cavity Method

Two complementary derivations:

**Derivation 1: Residual Decomposition**
1. Decompose each unit's activity: x_i = x_i^(lin) + delta_i
2. Show cross-covariances between residuals at distinct sites are strongly suppressed
3. Residuals act as independent noise within an effective linear network
4. The effective linear network has the same couplings J

**Derivation 2: Self-Consistent Matrix Equation**
1. Write matrix equation for the full covariance matrix C
2. Naive Gaussian closure gives WRONG equation
3. Cavity method separates Gaussian and non-Gaussian contributions
4. Both contributions enter at the same order — must include both

### Key Results

- Nonlinear RNN covariance ≈ Linear RNN covariance + effective noise
- Effective noise spectrum determined by mean-field order parameters
- Valid for typical quenched realizations at large N
- Extends linear equivalence from feedforward to recurrent networks

## When to Use

- Analyzing collective activity structure in large RNNs
- Computing full N×N covariance matrix (not just summary statistics)
- Understanding when nonlinear networks behave like linear ones
- Studying the role of quenched disorder in recurrent dynamics
- Deriving mean-field approximations for neural population activity

## Practical Steps

### Step 1: Identify Network Parameters
- Network size N, coupling distribution (mean, variance)
- Activation function phi and its statistics
- Input statistics (if any external drive)

### Step 2: Compute Mean-Field Order Parameters
- Effective gain: g_eff = E[phi'(x)]
- Effective noise variance: sigma_eff^2 = Var[phi(x)] - g_eff^2 * Var[x]

### Step 3: Solve Linear Equivalence
- Replace nonlinear network with linear network + effective noise
- Covariance: C = (I - g_eff * J)^(-1) * Sigma_noise * (I - g_eff * J)^(-T)

### Step 4: Validate Numerically
- Compare analytical prediction with direct simulation
- Check convergence as N increases
- Verify for different coupling distributions

## Pitfalls

- **Naive Gaussian closure fails**: Cannot simply assume joint Gaussianity of activities
- **Finite-size effects**: Theory valid for N → ∞; check N > 1000 for good agreement
- **Coupling structure**: Assumes i.i.d. random couplings; structured couplings require extensions
- **Stability**: Linear equivalence assumes the linearized network is stable

## References

- Paper: "Linear equivalence of nonlinear recurrent neural networks" (arXiv:2604.23489)
- Related: Mean-field theory of RNNs, statistical mechanics of disordered systems
- Cavity method origins: Statistical physics of spin glasses

## Activation Keywords
- cavity method
- two-site cavity
- linear equivalence rnn
- rnn covariance analysis
- quenched disorder neural network
- mean-field rnn
- nonlinear rnn analysis
- 空腔方法 RNN
- 非线性循环神经网络
