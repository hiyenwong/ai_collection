---
name: higher-order-portfolio-qaoa
description: "Higher-order moment portfolio optimization using Quantum Approximate Optimization Algorithm (QAOA) with HUBO formulation. Extends beyond mean-variance to include skewness and kurtosis for more realistic portfolio modeling."
category: quantum-finance
---

# Higher-Order Portfolio QAOA

## Description
Higher-order moment portfolio optimization using Quantum Approximate Optimization Algorithm (QAOA). This methodology extends traditional mean-variance portfolio optimization to include skewness (3rd moment) and kurtosis (4th moment) using Higher-Order Unconstrained Binary Optimization (HUBO) formulation, which maps naturally to QAOA parametrized circuits without quadratic reduction overhead.

## Activation Keywords
- higher-order portfolio optimization
- qaoa portfolio skewness kurtosis
- hubo portfolio quantum
- quantum portfolio higher moments
- qaoa hubo formulation
- 量子组合优化高阶矩
- portfolio optimization with skewness

## Tools Used
- terminal: Run QAOA simulations and quantum circuit execution
- web_search: Find latest quantum finance papers
- write_file: Create portfolio optimization scripts

## Core Concepts

### Higher-Order Moments in Portfolio Optimization
Traditional portfolio optimization only considers mean (expected return) and variance (risk). Higher-order optimization adds:
- **Skewness** (3rd moment): Asymmetry of return distribution — positive skew preferred
- **Kurtosis** (4th moment): Tail heaviness — lower kurtosis means fewer extreme events

### HUBO vs QUBO
- **QUBO** (Quadratic Unconstrained Binary Optimization): Only pairwise interactions (2-body terms)
- **HUBO** (Higher-Order Unconstrained Binary Optimization): Includes 3-body, 4-body+ terms
- HUBO maps naturally to QAOA without reduction to quadratic form (reduction adds ancilla qubits)

### QAOA Circuit for HUBO
1. Encode portfolio assets as qubits
2. Use integer variable encoding for position sizing
3. Construct cost Hamiltonian with higher-order Pauli terms (ZZZ, ZZZZ, etc.)
4. Apply QAOA layers: alternating cost + mixer unitaries
5. Measure optimal portfolio configuration

## Usage Patterns

### Pattern 1: Higher-Order Portfolio Formulation
```python
# Cost Hamiltonian for portfolio with higher moments
H = -mu_i * Z_i              # Expected return (linear)
  + gamma * sigma_ij * Z_i Z_j   # Risk/variance (quadratic)
  + lambda_3 * S_ijk * Z_i Z_j Z_k  # Skewness (cubic)
  + lambda_4 * K_ijkl * Z_i Z_j Z_k Z_l  # Kurtosis (quartic)
```

### Pattern 2: Integer Encoding for Position Sizing
- Use binary encoding: `position_i = sum(b_ij * 2^j)` for j in [0, num_bits)
- Capital-based budget constraint: `sum(position_i * price_i) <= total_capital`
- More realistic than binary buy/no-buy decisions

### Pattern 3: Classical Baseline Comparison
1. Solve continuous relaxation with classical optimization
2. Apply integer programming-based discretization
3. Compare HUBO-QAOA solutions against this baseline
4. Evaluate: Sharpe ratio, Sortino ratio, maximum drawdown

## Instructions for Agents

### Step 1: Problem Formulation
- Define universe of N assets
- Calculate historical moments: mean, covariance, coskewness, cokurtosis tensors
- Set risk aversion parameter and budget constraint

### Step 2: QAOA Circuit Construction
- Map assets to qubits with integer encoding
- Build cost Hamiltonian with all moment terms
- Choose mixer Hamiltonian (standard XY or problem-specific)
- Set QAOA depth (p layers)

### Step 3: Optimization
- Use classical optimizer (COBYLA, SPSA) for QAOA parameters
- Evaluate circuit on quantum simulator or hardware
- Extract portfolio weights from measurement outcomes

### Step 4: Validation
- Backtest optimized portfolio on out-of-sample data
- Compare against mean-variance and integer programming baselines
- Report: Sharpe ratio, Sortino ratio, skewness, kurtosis of returns

## Error Handling

### QAOA Convergence Issues
- Increase circuit depth (p) if solution quality is poor
- Use warm-start from classical solution
- Try different mixer Hamiltonians

### HUBO Term Explosion
- Higher-order terms scale as O(N^k) for k-th moment
- Use truncation or regularization for large portfolios
- Consider mean-field approximation for very large N

### Hardware Limitations
- Current NISQ devices limit portfolio size (~10-20 assets)
- Use simulator for larger problems
- Consider hybrid decomposition approaches

## Examples

### Example: 10-Asset Portfolio with Skewness
Given 10 assets, construct HUBO with:
- 10 linear terms (expected returns)
- 45 quadratic terms (covariance)
- 120 cubic terms (coskewness)
- Budget constraint: sum of positions = 1

Run QAOA with p=3 layers, compare to classical integer programming baseline.

## Resources
- arXiv:2509.01496 - "Higher-Order Portfolio Optimization with QAOA" (Uotila et al.)
- Qiskit: Quantum computing SDK with QAOA implementations
- PennyLane: Differentiable quantum programming

## Related Skills
- quantum-portfolio-optimization
- qaoa-optimization
- quantum-finance-portfolio
