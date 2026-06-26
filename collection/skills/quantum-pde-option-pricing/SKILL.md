---
name: quantum-pde-option-pricing
description: >
  End-to-end quantum PDE framework for derivative pricing. Use when:
  designing quantum algorithms for option pricing, solving high-dimensional
  financial PDEs on quantum hardware, comparing quantum vs classical pricing
  complexity, implementing Black-Scholes or Heston models on quantum circuits,
  or evaluating quantum advantage for financial derivative pricing.
  Covers: quantum PDE solvers, finite-difference discretization, gate complexity
  analysis, Clifford+T resource estimation, implied volatility extraction.
---

# Quantum PDE Option Pricing

End-to-end quantum PDE framework for European option pricing under local-
and stochastic-volatility models (arXiv: 2605.26610).

## Core Framework

1. **Classical Input**: Contract + model data (Black-Scholes / Heston)
2. **Discretization**: Finite-difference on spatial grids (N=2^n points per direction)
3. **Quantum PDE Solver**: Solve pricing PDE on quantum hardware
4. **Classical Output**: Option value estimates at selected points

## Gate Complexity

For d assets and N grid points per direction:
- **Black-Scholes (local vol)**: Õ(d² N^(2+d/2))
- **Heston (stochastic vol)**: Õ(d² N^(d+2))

Polynomial improvement over classical finite-difference baselines: N^(d/2) and N^d respectively.

## Implementation Steps

### 1. Problem Formulation
- Write PDE for option price V(S,t) under chosen model
- Black-Scholes: ∂V/∂t + ½σ²S²∂²V/∂S² + rS∂V/∂S - rV = 0
- Heston: Add stochastic variance with mean-reversion

### 2. Discretization
- Finite-difference on uniform grid
- Convert to matrix equation: dV/dt = AV
- Map to quantum state: |V(t)⟩ encoding discretized prices

### 3. Quantum State Preparation
- Encode initial/boundary conditions as quantum states
- Use quantum linear system algorithms for time evolution

### 4. Solution Recovery
- Single-point recovery via amplitude estimation
- Multi-point: repeated measurements or tomography

### 5. Resource Accounting
- Compile to Clifford+T via standard techniques
- Account for CNOT gates + single-qubit Pauli rotations

## Key Insight

The quantum advantage comes from the grid-size dependence:
quantum algorithms scale polynomially better than classical
for high-dimensional PDEs, making them particularly relevant
for multi-asset options where d > 2.

## Classical Benchmark

Compare against:
- Monte Carlo simulation
- Finite-difference methods (ADI, Crank-Nicolson)
- FFT-based methods (for simpler cases)

## Activation Keywords
- quantum pde option pricing
- quantum derivative pricing
- quantum black scholes
- quantum heston model
- 量子期权定价
- quantum financial pde
