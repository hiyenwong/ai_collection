---
name: higher-order-portfolio-qaoa
description: "Higher-order moment portfolio optimization using Quantum Approximate Optimization Algorithm (QAOA). Extends classical Markowitz mean-variance to include skewness and kurtosis via quantum Hamiltonian encoding. Use when: designing quantum portfolio optimization with risk beyond variance, implementing QAOA for multi-objective financial optimization, encoding higher-order statistical moments into quantum cost functions, or comparing quantum vs classical approaches for portfolio selection with non-Gaussian return distributions."
---

# Higher-Order Portfolio Optimization with QAOA

## Description

Extends portfolio optimization beyond Markowitz mean-variance (2nd moment) to include skewness (3rd moment) and kurtosis (4th moment) using QAOA. Higher-order moments capture asymmetry and tail risk in return distributions — critical for realistic portfolio modeling.

## Core Methodology

### Hamiltonian Encoding

The portfolio optimization objective is mapped to a QUBO Hamiltonian:

H = H_obj + λ · H_constraint

Where:
- **H_obj**: Objective Hamiltonian encoding return, variance, skewness, kurtosis
- **H_constraint**: Cardinality/budget constraints as penalty terms
- **λ**: Penalty strength for constraint satisfaction

### Higher-Order Moment Terms

- **Mean (μ)**: Σ w_i · μ_i → linear term in Hamiltonian
- **Variance (Σ)**: Σ w_i · w_j · σ_ij → quadratic terms (2-body interactions)
- **Skewness (S)**: Σ w_i · w_j · w_k · s_ijk → cubic terms (3-body interactions)
- **Kurtosis (K)**: Σ w_i · w_j · w_k · w_l · k_ijkl → quartic terms (4-body interactions)

### QUBO Reduction for Higher-Order Terms

Higher-order terms (3-body, 4-body) must be reduced to quadratic form for QAOA:
- Use ancilla qubits to replace cubic/quartic terms
- Apply penalty-based reduction: introduce auxiliary variable z ≈ x_i · x_j
- Trade-off: more ancilla qubits vs. lower-degree Hamiltonian

### QAOA Implementation

```
1. Initialize: |+⟩^⊗n or problem-informed state (e.g., Dicke state for cardinality)
2. For p layers:
   a. Apply mixer: e^{-i·β·H_mixer}
   b. Apply cost: e^{-i·γ·H_cost}
3. Measure and optimize (β, γ) via classical optimizer
```

### Mixer Selection

- **Standard X-mixer**: Allows transitions between all states; may violate constraints
- **XY-mixer**: Preserves Hamming weight; enforces cardinality constraints natively
- **Ring mixer**: Structured transitions for specific constraint patterns

## Key Insights

1. **Skewness preference**: Investors prefer positive skewness (asymmetric upside) — include as positive term in objective
2. **Kurtosis penalty**: High kurtosis means fat tails (crash risk) — penalize strongly
3. **QAOA depth**: Higher-order terms increase circuit depth; p=2-3 often sufficient for NISQ
4. **Ancilla overhead**: 3-body → 1 ancilla per term; 4-body → 2+ ancillas per term
5. **Classical comparison**: QAOA shows advantage for portfolios >50 assets with complex constraints

## Usage Patterns

### Pattern 1: Portfolio with Tail Risk Modeling
When portfolio returns are non-Gaussian (crypto, options, emerging markets):
1. Estimate μ, Σ, S, K from historical data
2. Map to Hamiltonian with weighted moment terms
3. Reduce higher-order terms to QUBO
4. Run QAOA with XY-mixer for cardinality constraints
5. Validate against classical benchmark (MILP, heuristic)

### Pattern 2: ESG-Constrained Direct Indexing
For portfolios with exclusion constraints:
1. Define cardinality K and exclusion masks
2. Use XY-mixer to preserve Hamming weight K
3. Encode ESG scores as linear bias terms
4. QAOA with p=1-2 layers on NISQ device

### Pattern 3: Quantum-Classical Hybrid Pipeline
For large-scale portfolios (>100 assets):
1. Classical pre-screening: filter to top-N candidates
2. QAOA on reduced universe
3. Classical post-processing: refine solution
4. Iterative refinement loop

## Implementation Notes

- **Penalty tuning**: λ must be large enough to enforce constraints but not overwhelm objective
- **Moment estimation**: Requires sufficient historical data; use robust estimators for S and K
- **QUBO size**: n + ancilla qubits; track qubit budget for target hardware
- **Validation**: Always compare against classical baselines (mean-variance, heuristic search)

## Activation Keywords
- higher order portfolio optimization
- skewness kurtosis portfolio
- QAOA portfolio
- quantum portfolio skewness
- qaoa higher moments
- 高阶矩组合优化
- 量子组合优化偏度峰度
- quantum finance portfolio
- QUBO portfolio optimization
- XY-mixer portfolio

## Related Skills
- quantum-portfolio-optimization (general QAOA portfolio)
- quantum-finance-portfolio (quantum finance overview)
- qaoa-optimization (general QAOA methodology)
