# Quantum Finance Research Notes - 2026-05-23

## Penalty-Free Pipeline for Quantum-Annealer Portfolio Optimization
**arXiv: 2605.17628** | Luis Lozano | 2026-05-17 | quant-ph, math.OC, q-fin.PM

### Problem
Standard penalty-encoded QUBO for portfolio optimization fails on D-Wave hardware.

### Root Cause Analysis
- Cardinality penalty → dense rank-one term ∝ all-ones matrix
- Makes logical interaction graph COMPLETE regardless of covariance structure
- Chain-break fractions: 83% at N=24, 92% at N=49 on Pegasus/Zephyr
- Zero feasible samples produced

### Sparsification Also Fails
- Topology-aware sparsification removes off-diagonal entries
- But this dilutes the cardinality constraint
- Raw samples remain infeasible even when chains don't break
- For structurally favorable cases (betting with settlement-graph priors), classical feasibility projector alone explains results — not QPU

### Working Pipeline
1. Build **objective-only QUBO** from expected returns + risk-scaled covariance
2. Sample on D-Wave Advantage/Advantage2 hardware
3. Enforce cardinality constraint **classically** as post-processing
4. Result: mean chain-break drops from 71-92% → ≤0.04%
5. Equity post-processed regret ≤0.03% at all tested scales

### Results
- Equities: up to N=49 assets
- Betting: up to N=48 assets
- QPU returns lower-energy feasible portfolios than greedy heuristic (betting, N=39,48)
- This is energy comparison, not optimality proof

### Key Insight
The penalty encoding, not the sparse hardware topology, is the binding constraint for direct QPU portfolio optimization at currently accessible scales.

---

## Higher-Order Portfolio Optimization with QAOA
**arXiv: 2509.01496** | Valter Uotila, Julia Ripatti, Bo Zhao | 2025-09-01 | quant-ph

### Innovation
First quantum formulation for portfolio optimization with higher-order moments (skewness, kurtosis).

### Technical Details
- Higher-order moments → higher-order terms in cost Hamiltonian
- Produces HUBO (Higher-Order Unconstrained Binary Optimization) problem
- Natural formulation as parametrized circuit (no quadratic reduction needed)
- Realistic integer variable encoding
- Capital-based budget constraint

### Results
- 100 portfolio optimization problems tested
- HUBO solutions often correspond to better allocations than classical baseline
- Classical baseline: continuous variable solution with integer programming discretization

### Significance
Promising for computationally challenging portfolio optimization; higher moments are classically complex but natural for QAOA.

---

## Quantum End-to-End Learning for Contextual Combinatorial Optimization
**arXiv: 2605.20222** | Jaehwan Lee, Changhyun Kwon | 2026-05-13 | quant-ph, cs.LG

### Innovation
First quantum computing-based end-to-end learning framework for CCO using QAOA.

### Key Mechanism
- **Context re-uploading phase-separator**: jointly captures relations among contexts, uncertain coefficients, and optimal solutions
- Contextual encoder integrated within quantum surrogate policy
- Joint end-to-end training with stationarity guarantee
- Directly trains on task loss despite discreteness and nonconvexity
- Avoids calls to NP-hard optimization solvers

### Results
- Competitive performance with substantially fewer parameters than classical benchmarks
- Industrial-level potential for future quantum era

---

## Quantum and Classical ML in Decentralized Finance
**arXiv: 2510.15903** | Chi-Sheng Chen, Aidan Hung-Wen Tsai | 2025-09-14 | q-fin.ST, cs.LG, quant-ph

### Scope
Empirical comparison of QML vs CML in AMM/DeFi trading strategies.

### Models Tested
- Classical: Random Forest, Gradient Boosting, Logistic Regression
- Pure Quantum: VQE Classifier, QNN, QSVM
- Hybrid: QASA Hybrid, QASA Sequence, QuantumRWKV
- Transformer models

### Results
| Model Type | Avg Return | Avg Sharpe |
|-----------|-----------|------------|
| Classical ML | 9.8% | 1.47 |
| Hybrid Quantum | 11.2% | 1.42 |
| QASA Sequence | 13.99% | 1.76 |

### Significance
Hybrid quantum-classical approaches show promise for DeFi trading; QASA Sequence achieves best individual performance.
