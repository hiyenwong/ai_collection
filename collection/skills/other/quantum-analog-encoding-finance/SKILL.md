---
name: quantum-analog-encoding-finance
description: >
  Quantum analog-encoding methodology for correlated Gaussian vectors and rough volatility simulation.
  Uses QSVT framework to prepare quantum states representing correlated Gaussian distributions with
  O(log N) gate complexity. Applicable to financial modeling (rough Bergomi), quantum ML data loading,
  and probabilistic simulation. Use when working with quantum state preparation for financial
  distributions, rough volatility models, or QSVT-based matrix functions.
---

# Quantum Analog-Encoding for Finance

## Description
Quantum algorithms for exact simulation of correlated Gaussian random vectors and their exponentiation
using QSVT. Achieves O(log N) gate complexity vs classical O(N) sampling.

## Activation Keywords
- quantum analog encoding
- rough volatility quantum
- QSVT finance
- quantum state preparation
- rough Bergomi model
- correlated Gaussian quantum
- quantum volatility simulation

## Core Methodology

### State Preparation
1. Encode covariance matrix Sigma into quantum data structure (O(polylog N) depth)
2. Prepare |x> = Sigma^{1/2}|+> via QSVT matrix square root
3. Complexity: O(log N) gates for N-dimensional state

### Exponentiation Map
1. Apply element-wise exponential via linear combination of unitaries (LCU)
2. Prepare exp(x)/||exp(x)|| with polylog complexity
3. Enables simulation of log-normal distributions

### QSVT Implementation
- Polynomial approximation of matrix functions
- Block-encoding of covariance matrix
- Singular value transformation for sqrt(Sigma)

## Usage Patterns

### Rough Bergomi Simulation
For rough volatility models where volatility follows:
dlog(V_t) = -lambda * log(V_t)dt + eta * dW_t^H

1. Prepare correlated Gaussian state |x>
2. Apply exponential map to get log-volatility state
3. Sample from quantum state for path simulation

### Quantum ML Data Loading
For loading probability distributions into quantum states:
1. Prepare covariance matrix block-encoding
2. Apply QSVT for distribution encoding
3. Use as input for quantum ML algorithms

## Key Parameters
- N: Dimension of Gaussian vector
- Sigma: Covariance matrix (must be efficiently block-encodable)
- epsilon: Precision parameter for polynomial approximation
- H: Hurst parameter for rough volatility (typically 0.02-0.1)

## Error Handling
### Matrix Not Block-Encodable
If Sigma cannot be efficiently block-encoded:
- Use sparse approximation
- Consider low-rank decomposition
- Fall back to classical simulation for small N

### Precision Issues
For high precision requirements:
- Increase polynomial degree in QSVT
- Trade-off: O(poly(1/epsilon)) complexity scaling

## Resources
- arXiv: 2604.22463
- Authors: Tassa Thaksakronwong, Koichi Miyamoto
- Category: quant-ph, q-fin.CP
