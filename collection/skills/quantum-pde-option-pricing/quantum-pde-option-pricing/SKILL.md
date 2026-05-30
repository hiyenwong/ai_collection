---
name: quantum-pde-option-pricing
description: End-to-end quantum PDE framework for multi-asset option pricing under local and stochastic volatility models. Implements quantum algorithms for solving high-dimensional parabolic PDEs arising in European option pricing (Black-Scholes, Heston models).
category: quantum-finance
arxiv_id: "2605.26610"
authors: ""
date: "2026-05-30"
---

# Quantum PDE-Based Option Pricing

## Description
End-to-end quantum PDE framework for multi-asset European option pricing under local-volatility Black-Scholes and Heston stochastic volatility models. Takes classical contract and model data as input, solves pricing PDEs via finite-difference discretization on spatial grids, and returns classical estimates of selected option values. Achieves exponential speedup in dimension for N=2^n grid points per spatial dimension.

## Activation Keywords
- quantum option pricing
- quantum PDE solver
- Black-Scholes quantum
- Heston model quantum
- multi-asset option pricing
- quantum derivative pricing
- 量子期权定价
- 量子PDE求解
- 量子布莱克-斯科尔斯

## Core Methodology

### 1. PDE Discretization
- Discretize pricing PDEs using finite-difference methods on spatial grids
- For N=2^n grid points per spatial dimension, represent solution as quantum state
- Handle boundary conditions appropriate for option pricing (Dirichlet/Neumann)

### 2. Quantum Linear System Solving
- Use Quantum Linear System Algorithm (QLSA) to solve discretized system
- Complexity: O(polylog(N)) vs O(N) classically for d-dimensional problems
- Implement amplitude estimation for extracting option prices

### 3. Models Supported
- **Black-Scholes (local volatility)**: Standard GBM with deterministic volatility surface
- **Heston (stochastic volatility)**: Mean-reverting stochastic variance process
- Multi-asset extensions with correlation structure

### 4. End-to-End Pipeline
1. Input: Classical contract parameters (strike, maturity, payoff type)
2. Input: Model parameters (volatility, correlation, mean reversion)
3. Encode: Prepare initial state encoding payoff function
4. Solve: Apply QLSA to discretized PDE system
5. Extract: Use amplitude estimation to read option prices
6. Output: Classical price estimates with confidence bounds

## Tools Used
- Quantum computing frameworks (Qiskit, Pennylane)
- Classical PDE solvers for validation
- Amplitude estimation implementations

## Implementation Steps

### Step 1: Grid Setup
- Choose spatial discretization for asset price(s) and volatility
- Map continuous PDE to discrete linear system Au=b
- Ensure N=2^n for efficient quantum encoding

### Step 2: State Preparation
- Encode payoff function as initial quantum state
- Use amplitude encoding for efficient representation
- Handle multi-asset case via tensor product structure

### Step 3: Quantum Solver
- Apply QLSA (e.g., HHL variant) to solve Au=b
- Handle condition number scaling with grid resolution
- Implement error bounds for price estimates

### Step 4: Readout
- Use quantum amplitude estimation for price extraction
- Achieve quadratic speedup in precision (1/epsilon vs 1/epsilon^2)
- Return classical price with statistical confidence

## Error Handling
- **Condition number blowup**: Use preconditioning for ill-conditioned systems
- **State preparation error**: Verify encoding fidelity before solving
- **Readout precision**: Adjust amplitude estimation shots based on required accuracy
- **Model validation**: Cross-check with classical finite-difference solutions

## Key Insights from Paper 2605.26610
- Framework handles both local and stochastic volatility models
- End-to-end analysis includes all subroutines (encoding, solving, readout)
- Provides explicit complexity bounds for multi-asset case
- Addresses practical concerns: discretization error, condition number, state preparation

## Resources
- arXiv: https://arxiv.org/abs/2605.26610
- Related: Quantum algorithm for heat equation (exponential speedup for state preparation)
- Related: QPINN portfolio optimization (quantum physics-informed neural networks)
