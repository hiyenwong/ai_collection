---
name: quantum-finance-portfolio
description: 量子计算在金融组合优化中的应用。涵盖 QUBO建模、量子退火、QRNG增强Monte Carlo、VaR/CVaR估计、风险度量。适用于投资组合优化、资产配置、量子金融建模。
category: quantum-finance
trigger_words: ["quantum portfolio", "quantum finance", "QUBO portfolio", "quantum optimization finance", "quantum annealing portfolio", "QRNG Monte Carlo", "quantum VaR", "quantum CVaR", "量子投资组合", "量子金融", "组合优化"]
---

# Quantum Finance Portfolio Optimization

## Overview
Quantum computing approaches for portfolio optimization, including QUBO formulations, quantum annealing, quantum-inspired algorithms, and quantum-enhanced risk analysis.

## Core Methodologies

### 1. QUBO Formulation for Portfolio Optimization
- Convert portfolio optimization to Quadratic Unconstrained Binary Optimization
- Map assets to binary variables (buy/sell decisions)
- Encode constraints (budget, sector limits) into QUBO matrix
- Minimize risk while maximizing expected return

### 2. Quantum Annealing for Portfolio Selection
- Use D-Wave quantum annealers for portfolio optimization
- Formulate as Ising model
- Leverage quantum tunneling to escape local minima
- Compare with classical simulated annealing baselines

### 3. QRNG-Enhanced Monte Carlo
- Use Quantum Random Number Generators (QRNG) for Monte Carlo simulations
- Improve convergence rates over pseudo-random numbers
- Applications in VaR/CVaR estimation, option pricing
- Quantum advantage in high-dimensional integration

### 4. Risk Metrics Computation
- Value at Risk (VaR) estimation using quantum algorithms
- Conditional Value at Risk (CVaR) optimization
- Portfolio risk decomposition using quantum linear algebra
- Stress testing scenarios with quantum sampling

## Implementation Patterns

### QUBO Matrix Construction
```
Q_ij = λ * σ_ij (risk covariance)
Q_ii = -μ_i (expected return)
```

### Quantum Annealing Pipeline
1. Problem formulation → QUBO matrix
2. Minor embedding → hardware topology
3. Annealing schedule → solution sampling
4. Post-processing → portfolio selection

### QRNG Integration
```python
import numpy as np
# Replace np.random with quantum random numbers
qrng_samples = get_quantum_random_numbers(n_samples)
monte_carlo_paths = simulate_paths(qrng_samples)
```

## Key Papers
- Hot-Starting Quantum Portfolio Optimization (arXiv:2510.11153)
- Quantum Portfolio Optimization: An Extensive Benchmark (arXiv:2509.17876)
- Quantum Computing for Financial Transformation (arXiv:2604.08180)

## Pitfalls
- QUBO formulations can become intractable for large portfolios
- Quantum annealing hardware has limited qubit connectivity
- QRNG advantages may be marginal for low-dimensional problems
- Need classical baselines for comparison
