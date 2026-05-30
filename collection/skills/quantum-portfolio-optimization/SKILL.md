---
name: quantum-portfolio-optimization
description: "Quantum portfolio optimization methodologies — QAOA for higher-order moments (skewness, kurtosis), quantum annealing for mean-variance optimization, and hybrid quantum-classical pipelines for NISQ-era finance. Use when: (1) portfolio optimization with quantum computing, (2) QAOA for financial problems, (3) quantum annealing for trading, (4) higher-order moment portfolio selection, (5) hybrid quantum-classical finance."
license: Complete terms in LICENSE.txt
metadata:
  arxiv_ids: "2509.01496, 2504.08843"
  published: "2025-04-10, 2025-09-01"
  authors: "Valter Uotila et al.; Sai Nandan Morapakula et al."
  tags: [quantum, finance, portfolio, qaoa, annealing, optimization]
---

# Quantum Portfolio Optimization

Quantum computing methodologies for portfolio optimization — covering QAOA formulations with higher-order moments and quantum annealing pipelines for NISQ-era financial decision making.

## Core Papers

### QAOA for Higher-Order Portfolio Optimization (arXiv: 2509.01496)
First quantum formulation for portfolio optimization with **higher-order moments** (skewness and kurtosis). Standard mean-variance ignores distribution asymmetry and tail risk. QAOA encodes cubic/quadratic terms into Ising Hamiltonians, enabling quantum advantage for complex risk modeling.

### End-to-End Quantum Annealing Pipeline (arXiv: 2504.08843)
Practical hybrid pipeline combining continuous mean-variance/Sharpe-ratio objectives with quantum annealing solver. Demonstrates feasibility on current NISQ devices.

## Usage Patterns

### Pattern 1: QAOA Higher-Order Portfolio Optimization
**QUBO formulation:**
```
H = -μ^T x + λ₁ x^T Σ x + λ₂ Σᵢⱼₖ Sᵢⱼₖ xᵢxⱼxₖ + λ₃ Σᵢⱼₖₗ Kᵢⱼₖₗ xᵢxⱼxₖxₗ
```

**Steps:**
1. Encode objective as Ising Hamiltonian
2. Map to QUBO with penalty constraints
3. Initialize QAOA (p=1-3 layers for NISQ)
4. Optimize angles classically (COBYLA/SPSA)
5. Sample final state for portfolio candidates

### Pattern 2: Quantum Annealing Pipeline
1. Classical preprocessing: returns, covariance, constraints
2. QUBO formulation: mean-variance + constraints
3. Minor-embed onto QA hardware topology
4. Run 1000-10000 annealing reads
5. Select best feasible solution

### Pattern 3: Hybrid Classical-Quantum
1. Classical optimization for initial solution
2. Quantum refinement in local neighborhoods
3. Validate against classical benchmarks

## QUBO Encoding (Python)
```python
import numpy as np

def portfolio_to_qubo(returns, covariance, risk_aversion=1.0, budget=None, penalty=10.0):
    n = len(returns)
    if budget is None: budget = n // 2
    Q = risk_aversion * covariance - np.outer(returns, np.ones(n)) * 0.5
    Q = Q + Q.T
    Q += penalty * np.ones((n, n))
    Q -= penalty * budget * np.eye(n)
    offset = penalty * budget**2
    return Q, offset
```

## Error Handling
- **Barren Plateaus**: Use problem-specific initialization, layerwise training
- **Embedding Failures**: Chain strength optimization, problem decomposition
- **Noisy Moments**: Shrinkage estimators, Bayesian priors

## Activation Keywords
- quantum portfolio optimization, QAOA finance, quantum annealing portfolio, higher-order moment portfolio, quantum finance optimization, 量子组合优化, QAOA 投资组合, 量子退火金融

## Related Skills
- `quantum-optimization-qaoa`, `quantum-finance-portfolio`, `quantum-neural-barren-plateau`
