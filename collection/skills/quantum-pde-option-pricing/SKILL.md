---
name: quantum-pde-option-pricing
description: "End-to-end quantum PDE framework for multi-asset option pricing under local and stochastic volatility. Solves high-dimensional parabolic PDEs via finite-difference discretization on quantum hardware, achieving polynomial improvement factors N^{d/2} (local-vol BS) and N^d (Heston) over classical baselines. Use when: quantum option pricing, multi-asset derivatives, quantum PDE solvers, Heston model quantum, volatility modeling, quantum finance algorithms."
---

# Quantum PDE-Based Option Pricing

## Description

End-to-end quantum algorithm for pricing multi-asset European options under local-volatility Black-Scholes and Heston (stochastic volatility) models. The framework takes classical contract and model data as input and returns classical estimates of selected option values through quantum computation of PDE solutions.

## Core Problem

Multi-asset option pricing under local and stochastic volatility leads to high-dimensional parabolic PDEs. Classical finite-difference methods scale exponentially with dimension (curse of dimensionality). This quantum framework achieves polynomial speedup while maintaining end-to-end classical-to-classical correctness.

## Methodology

### Step 1: PDE Formulation

- Local-volatility Black-Scholes: parabolic PDE with spatially varying diffusion coefficient
- Heston model: coupled system for asset price and variance (2d-dimensional for d assets)
- Boundary conditions from contract payoff structure

### Step 2: Finite-Difference Discretization

- Spatial grid with N = 2^n points per direction
- d assets → d-dimensional grid
- Discretized operator matrix A encodes the PDE
- Initial condition encodes the option payoff

### Step 3: Quantum Linear System Solution

- Solve the discretized linear system Ax = b on quantum hardware
- State preparation: encode initial conditions and boundary data into quantum states
- Hamiltonian simulation or HHL-based approach for system solution

### Step 4: Classical Output Extraction

- Single-point recovery: extract option value at specific asset price points
- Full smile reconstruction: recover prices across strikes for implied volatility surface

## Complexity Analysis

### Gate Complexity (CNOT + single-qubit rotations)

| Model | Complexity | Speedup vs Classical |
|-------|-----------|---------------------|
| Local-vol BS | O~(d²N^{2+d/2}) | N^{d/2} polynomial improvement |
| Heston | O~(d²N^{d+2}) | N^d polynomial improvement |

- N = 2^n grid points per spatial direction
- d = number of assets
- Tilde notation hides logarithmic factors
- Compiles to Clifford+T via standard compilation

### Resource Accounting

- Explicit gate count in elementary CNOT + Pauli-axis rotations
- Clifford+T resource estimates via standard compilation
- Numerical benchmarks against classical methods provided

## When to Use

- Multi-asset European option pricing
- Local-volatility and stochastic volatility models
- Heston model calibration and pricing
- Implied volatility smile/skew computation
- High-dimensional derivatives pricing (d ≥ 2)

## Activation Keywords

- quantum PDE option pricing
- quantum algorithm derivatives pricing
- quantum Black-Scholes
- quantum Heston model
- multi-asset quantum pricing
- finite-difference quantum algorithm
- quantum volatility modeling
- end-to-end quantum pricing pipeline
- 量子期权定价
- 量子偏微分方程

## Pitfalls

### End-to-End Classical-to-Classical

The framework is designed to take classical input and return classical output. The quantum speedup applies only to the PDE solve step, not to state preparation or measurement.

### Grid-Size Dependence

Speedup is polynomial in grid size N, not exponential. The improvement factor N^{d/2} or N^d becomes significant only for large N (fine grids).

### Single-Point Recovery

Complexity bounds are for single-point value recovery. Full surface reconstruction requires multiple invocations.

### NISQ Feasibility

The gate complexity O~(d²N^{2+d/2}) is beyond current NISQ devices. This is a fault-tolerant quantum algorithm with explicit resource estimates.

## Resources

- Paper: arXiv:2605.26610
- Authors: Nikita Guseynov, Nana Liu, Chi Seng Pun, Tushar Vaidya
- 49 pages, 10 figures, 10 tables
- Categories: quant-ph, q-fin.CP
