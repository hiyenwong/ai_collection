---
name: quantum-portfolio-optimization
version: v1.0.0
last_updated: 2026-04-06
description: Quantum computing methods for portfolio optimization - QAOA, quantum annealing, quantum Monte Carlo for financial risk analytics, option pricing, and derivative valuation. Use when: (1) User asks about quantum finance, quantum portfolio, quantum investment, (2) Discussing quantum algorithms in finance, (3) Analyzing quantum advantage in financial computations, (4) Implementing quantum-based risk management or derivative pricing, (5) User mentions QAOA, quantum annealing, quantum Monte Carlo in financial context.
---

# Quantum Portfolio Optimization

## Activation Keywords

- quantum portfolio optimization
- quantum finance
- quantum investment
- QAOA portfolio
- quantum annealing finance
- quantum Monte Carlo risk
- quantum option pricing
- 量子投资组合优化
- 量子金融
- quantum derivative pricing

## Tools Used

- `exec`: Run Qiskit/D-Wave quantum optimization scripts
- `read`: Load financial data and quantum circuit configurations
- `web_search`: Search arxiv for latest quantum finance papers
- `sqlite3`: Query kg.db for related papers

## Instructions for Agents

### Step 1: Identify Financial Problem
Classify the problem: portfolio optimization, VaR estimation, option pricing, or risk management.

### Step 2: Select Quantum Method
- Portfolio (small): QAOA on gate-based quantum computer
- Portfolio (large): Quantum Annealing (D-Wave)
- Risk/derivatives: Quantum Monte Carlo (amplitude estimation)

### Step 3: Formulate as QUBO (if applicable)
Encode: `min Σ(-μᵢxᵢ) + λΣ(σᵢⱼxᵢxⱼ)` with constraint penalty terms.

### Step 4: Execute and Post-Process
Run quantum algorithm; decode binary solution; validate constraints; refine with classical optimizer.

### Step 5: Report Results
Compare quantum vs classical performance; report quantum advantage threshold; provide implementation guidance.

## Overview

Quantum computing approaches for financial portfolio optimization, risk analytics, and derivative pricing. Leverages quantum algorithms (QAOA, quantum annealing, quantum Monte Carlo) to achieve speedups over classical methods.

## Core Methods

### 1. QAOA Portfolio Optimization

Quantum Approximate Optimization Algorithm for portfolio selection considering higher-order moments.

**Key Features:**
- Beyond mean-variance optimization
- Incorporates skewness and kurtosis
- Risk-adjusted return maximization
- Quadratic speedup potential

**Workflow:**
1. Encode portfolio constraints as Hamiltonian
2. Apply QAOA circuit with p layers
3. Measure optimal portfolio allocation
4. Decode quantum state to asset weights

### 2. Quantum Annealing Portfolio

End-to-end portfolio optimization using quantum annealing (D-Wave systems).

**Key Features:**
- Hybrid quantum-classical approach
- Handles real-world constraints:
  - Cardinality limits (max assets)
  - Turnover limits
  - Transaction costs
  - Sector exposure limits

**Workflow:**
1. Formulate as QUBO problem
2. Convert to Ising model
3. Submit to quantum annealer
4. Post-process with classical optimizer

### 3. Quantum Monte Carlo for Risk

Quantum amplitude estimation for Monte Carlo simulations in risk management.

**Key Features:**
- VaR (Value at Risk) estimation
- Expected Shortfall calculation
- Derivative pricing (options, swaps)
- Quadratic speedup vs classical MC
- Scenario generation across risk factors

**Workflow:**
1. Encode probability distribution as quantum state
2. Implement payoff function as quantum operator
3. Use amplitude estimation to compute expectation
4. Extract VaR/ES from estimated distribution

### 4. Quantum Option Pricing

Gate-based quantum computing for European/American option pricing.

**Key Features:**
- Amplitude estimation replaces classical MC
- Quadratic speedup (O(1/ε) vs O(1/ε²))
- Minimal circuit depth implementations
- Path-dependent options support

**Workflow:**
1. Encode asset price distribution
2. Implement option payoff function
3. Apply amplitude estimation
4. Extract expected payoff (option price)

## Practical Considerations

### Quantum Advantage Threshold

Resource requirements for quantum advantage in finance:
- **Gate count**: ~10⁸ - 10¹¹ gates
- **Qubit count**: 50-200 logical qubits
- **Problem size**: 100-500 assets
- **Circuit depth**: Minimized for NISQ era

### Hybrid Approaches

Current best practice: hybrid quantum-classical
- Quantum: Optimization core / Monte Carlo sampling
- Classical: Data preprocessing / Post-processing / Constraint handling

## Tools

### Quantum Libraries
- **Qiskit** (IBM): Gate-based quantum computing
- **D-Wave Ocean SDK**: Quantum annealing
- **Cirq** (Google): NISQ algorithms
- **Pennylane**: Quantum machine learning

### Financial Libraries
- **QuantLib**: Classical finance baseline
- **NumPy/SciPy**: Numerical operations
- **Pandas**: Data management

## References

For detailed implementations:
- [QAOA_IMPLEMENTATION.md](references/QAOA_IMPLEMENTATION.md): QAOA circuit construction
- [QUANTUM_ANNEALING.md](references/QUANTUM_ANNEALING.md): QUBO formulation
- [QUANTUM_MC.md](references/QUANTUM_MC.md): Amplitude estimation algorithms
- [OPTION_PRICING.md](references/OPTION_PRICING.md): Derivative pricing circuits

## Research Papers

Key papers in knowledge graph (kg.db):
1. Higher-Order Portfolio Optimization with QAOA (arxiv:2509.01496)
2. End-to-End Portfolio Optimization with Quantum Annealing (arxiv:2504.08843)
3. Quantum Monte Carlo for Financial Risk (arxiv:2303.09682)
4. Option Pricing using Quantum Computers (arxiv:1905.02666)
5. Threshold for Quantum Advantage in Derivative Pricing (arxiv:2012.03819)
6. **Quantum Portfolio Optimization: An Extensive Benchmark (arxiv:2509.17876)** - ⚠️ Challenges quantum advantage claims
7. **IonQ + Kipu Quantum 2026 Hardware Test** - ✅ 64 qubits > 36 qubits on S&P 500

## Key Debate: Quantum Advantage

**Theoretical benchmark (arxiv:2509.17876)**: Mixed-integer programming solves all instances in seconds; limited quantum advantage.

**Hardware experiment (IonQ/Kipu 2026)**: Increasing qubits (36→64) improves results on real S&P 500 data.

**Implication**: Hybrid quantum-classical pipelines may show advantages that pure theoretical comparisons miss.

## Limitations

- **Hardware**: NISQ devices have noise and limited qubits
- **Encoding**: Financial data encoding overhead
- **Scalability**: Current advantage threshold unclear
- **Validation**: Need benchmarking vs classical methods

## Best Practices

1. **Start hybrid**: Combine quantum + classical for production
2. **Minimize depth**: Reduce circuit depth for NISQ compatibility
3. **Benchmark**: Compare quantum vs classical performance
4. **Validate**: Test results against classical baselines
5. **Scale gradually**: Begin with small portfolios, expand

## Examples

### Example 1: Higher-Order Portfolio Optimization

```
User: "Use quantum computing to optimize a portfolio with 50 assets considering skewness and kurtosis"

Agent:
1. Identify method: QAOA with higher-order moments (arxiv:2509.01496)
2. Formulate QUBO with skewness/kurtosis terms
3. Implement QAOA circuit (p=3 layers, ~50-60 qubits)
4. Execute on quantum simulator
5. Decode optimal weights; report expected return and Sharpe ratio
```

### Example 2: Quantum Monte Carlo VaR

```
User: "Estimate portfolio VaR using quantum Monte Carlo"

Agent:
1. Encode portfolio loss distribution as quantum state
2. Apply quantum amplitude estimation (quadratic speedup)
3. Extract 95% VaR and CVaR estimates
4. Compare with classical Monte Carlo baseline
5. Report resource requirements for quantum advantage
```

## Related Skills

- **quantum-game-theory**: Non-Nashian quantum economics models
- **agentic-investment**: Multi-agent portfolio architecture
- **stock-analysis**: Classical technical analysis baseline