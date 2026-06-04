---
name: quantum-finance-analysis
version: v1.0.0
last_updated: 2026-04-06
description: "Quantum computing applications in finance and economics. Use when analyzing quantum portfolio optimization, quantum Monte Carlo for risk, quantum game theory, option pricing with quantum algorithms. Keywords: quantum finance, quantum portfolio, quantum Monte Carlo, quantum risk, quantum economics, quantum game theory, QAOA portfolio, quantum annealing finance."
---

# Quantum Finance Analysis

Skill for analyzing quantum computing applications in financial problems.

## Activation Keywords
- quantum finance
- quantum portfolio optimization
- quantum Monte Carlo finance
- quantum risk management
- quantum game theory
- quantum economics
- QAOA portfolio
- quantum annealing finance
- 量子金融
- 量子投资组合
- 量子蒙特卡洛

## Key Research Areas

### 1. Portfolio Optimization

**Quantum Approaches:**
- QAOA (Quantum Approximate Optimization Algorithm)
- Quantum Annealing (D-Wave, reverse annealing)
- Higher-order moments (skewness, kurtosis) beyond mean-variance
- Cardinality and turnover constraints

**Papers in kg.db:**
- `Higher-Order Portfolio Optimization with QAOA` (arxiv:2509.01496)
- `End-to-End Portfolio Optimization with Quantum Annealing` (arxiv:2504.08843)
- `PO-QA Framework` (arxiv:2407.19857)
- `Reverse Quantum Annealing Approach` (arxiv:1810.08584)
- `Large-scale portfolio optimization using Pauli Correlation Encoding` (arxiv:2511.21305) — PCE: 250+ assets on gate-based
- `A Quantum Reservoir Computing Approach to Stock Forecasting` (arxiv:2602.13094) — QRC: ≤6 qubits financial TS
- `Hot-Starting Quantum Portfolio Optimization` (arxiv:2510.11153)
- `Quantum Portfolio Optimization: An Extensive Benchmark` (arxiv:2509.17876)
- `Toward Quantum Utility in Finance: Asset Clustering` (arxiv:2509.07766)
- `Quantum Proper Scoring Rules` (arxiv:2605.05268)

**Pattern:**
```python
# QUBO formulation for portfolio
def portfolio_qubo(expected_returns, risk_matrix, lambda_risk, constraints):
    """
    Convert portfolio optimization to QUBO:
    H = -sum(r_i * x_i) + λ * sum(σ_ij * x_i * x_j)
    Subject to: sum(x_i) = K (cardinality)
    """
    pass
```

### 2. Quantum Monte Carlo for Risk

**Applications:**
- VaR (Value at Risk) estimation
- CVaR (Conditional VaR)
- Derivative pricing
- Scenario generation (equity, rate, credit risk)

**Speedup:** Quadratic speedup over classical Monte Carlo

**Papers:**
- `Quantum Monte Carlo for financial risk analytics` (arxiv:2303.09682)
- `Quantum-Enhanced Monte Carlo for Financial Risk Metrics` (arxiv:2502.02125)
- `Quantum Monte Carlo simulations for risk analytics` (arxiv:2303.09682v2)

**Pattern:**
```python
# Quantum amplitude estimation for VaR
def quantum_var_estimation(portfolio, confidence_level, num_qubits):
    """
    Use quantum amplitude estimation for VaR:
    - Encode loss distribution in quantum state
    - Apply amplitude estimation algorithm
    - Quadratic speedup vs classical MC
    """
    pass
```

### 3. Option Pricing

**Quantum Methods:**
- Quantum amplitude estimation
- Gate-based quantum computing
- Quadratic speedup over classical MC

**Papers:**
- `Option Pricing using Quantum Computers` (arxiv:1905.02666)
- `A Threshold for Quantum Advantage in Derivative Pricing` (arxiv:1611)

**Pattern:**
```python
# Quantum option pricing
def quantum_option_pricing(spot, strike, maturity, volatility, option_type):
    """
    Use quantum amplitude estimation:
    - Encode payoff function
    - Estimate expected payoff via QAE
    - Discount to present value
    """
    pass
```

### 4. Quantum Game Theory

**Applications:**
- Nash equilibrium in quantum games
- Quantum strategies in financial games
- Monetary economics (Quantum Barro-Gordon Game)
- Quantum entanglement in game theory

**Key Insight:** "Nashian game theory is incompatible with quantum physics" (arxiv:2112.03881)

**Papers:**
- `Theory of Quantum Games and Quantum Economic Behavior` (arxiv:2010.14098)
- `Quantum Game Theory in Finance` (arxiv:0406129)
- `Quantum Barro-Gordon Game in Monetary Economics` (arxiv:1708.05689)

### 5. Pauli Correlation Encoding (PCE) — NEW SCALABILITY PATTERN

**Problem:** Conventional quantum optimization assumes 1 qubit = 1 variable, limiting
problems to current qubit counts (~100-1000). PCE overcomes this.

**Key paper:** Soloviev & Krompiec, "Large-scale portfolio optimization using Pauli Correlation Encoding" (arXiv:2511.21305, 2025)

**How it works:**
1. Build market graph from asset return correlations
2. Partition graph into sub-portfolios of highly correlated assets (spectral clustering/METIS)
3. Encode multiple variables per qubit using Pauli operator products (Z_i, Z_i*Z_j)
4. Run VQA on each sub-portfolio independently
5. Aggregate solutions respecting global budget constraint

**Scalability:** O(sqrt(N)) qubits instead of O(N) for N assets. 250+ assets demonstrated.

**When to use:** Gate-based quantum advantage needed AND assets > available qubits.

### 6. Quantum Reservoir Computing (QRC) for Financial Time Series

**Key paper:** "A Quantum Reservoir Computing Approach to Quantum Stock Movement Forecasting" (arXiv:2602.13094, 2026)

**How it works:**
- Use small quantum system (3-6 qubits) as fixed nonlinear reservoir
- Encode financial features into quantum states via angle encoding
- Collect measurement outcomes (⟨Z_q⟩, ⟨Z_i Z_j⟩) as reservoir states
- Train only classical readout layer (ridge regression)
- Predict next-day returns, volumes, or trading signals

**Advantages:** No training on quantum hardware, NISQ-compatible, rich dynamics from entanglement.

### 7. Hybrid Quantum-Classical

**Practical Approach:**
- Use quantum for sampling/optimization
- Classical for post-processing
- Iterative refinement
- VQE/QAOA with classical optimizer

**Pattern:**
```
Hybrid workflow:
1. Formulate problem as QUBO/Hamiltonian
2. Run quantum annealer/QAOA
3. Extract solutions
4. Classical validation & refinement
5. Iterate until convergence
```

## Instructions for Agents

### Important: Fetching arXiv Paper Content

**`web_extract()` BLOCKS arxiv.org URLs** — returns "Blocked: URL targets a private or internal network address". This is a hard limitation.

**Working alternatives for paper content:**
1. Use arXiv API XML endpoint: `curl "https://export.arxiv.org/api/query?id_list=XXXX.XXXXX"` — returns title/abstract/authors
2. Use existing `.txt` files in workspace if papers were previously downloaded
3. Use the `arxiv-search` skill for metadata, then build skills from abstract-level understanding

### Analyzing Quantum Finance Papers

1. **Identify problem type:**
   - Portfolio optimization → QAOA/Annealing
   - Risk estimation → Quantum Monte Carlo
   - Option pricing → Amplitude estimation
   - Game theory → Quantum games

2. **Extract key methodology:**
   - QUBO formulation
   - Hamiltonian encoding
   - Number of qubits required
   - Speedup claims

3. **Assess practicality:**
   - NISQ-era feasibility
   - Hybrid approach needed?
   - Resource estimation (qubits, gates)

4. **Compare with classical:**
   - Classical baseline performance
   - Quantum advantage threshold
   - Problem size for quantum benefit

## Knowledge Graph Integration

Use kg.db to find related papers:

```bash
# Search quantum finance papers
sqlite3 kg.db "SELECT name FROM kg_entities 
WHERE entity_type='paper' 
AND (name LIKE '%quantum%' OR name LIKE '%finance%')"

# Run PageRank to find important papers
./kg_tool pagerank kg.db

# Find similar papers
SELECT e1.name, r.rel_type, e2.name 
## Resources

- arxiv category: `quant-ph` (Quantum Physics)
- arxiv categories: `q-fin` (Quantitative Finance) — often co-published with quant-ph
- arxiv keywords: `quantum finance`, `portfolio optimization`, `quantum reservoir computing`
- kg.db: Quantum finance paper collection (959+ entities, 3356+ relations)

- `https://arxiv.org/abs/2605.06853` — Hash-Based Commit-Reveal for Post-Quantum Blockchain (2026-05-07)
- `https://arxiv.org/abs/2605.18080` — 4-Qubit EWL Quantum Game Circuits with Dirac-Solow-Swan Hamiltonian (2026-05-18)

## Related Skills

- **pauli-correlation-portfolio-optimization**: PCE-specific implementation for 250+ asset optimization (class-level: quantum-finance-analysis)
- **quantum-reservoir-stock-forecasting**: QRC-specific forecasting patterns (class-level: quantum-finance-analysis)
- **quantum-portfolio-optimization**: QAOA with counterdiabatic driving, XY-mixers
- **stock-analysis**: Classical stock analysis methods
- **arxiv-search**: Find new quantum finance papers
- **quantum-game-recommender-systems**: EWL quantum circuits repurposed as innovation recommender systems
- **post-quantum-blockchain-economics**: Post-quantum blockchain migration economics
- **non-gaussian-entanglement-hierarchy**: Schmidt number-based non-Gaussian entanglement hierarchy

## Resources

- arxiv category: `quant-ph` (Quantum Physics)
- arxiv keywords: `quantum finance`, `portfolio optimization`
- kg.db: Quantum finance paper collection (302 entities, 268 relations)