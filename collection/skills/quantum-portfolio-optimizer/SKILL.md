---
name: quantum-portfolio-optimizer
description: "Quantum computing portfolio optimization skill. Uses QAOA, quantum annealing, and hybrid quantum-classical methods for financial portfolio optimization with higher-order moments (skewness, kurtosis) and real-world constraints (cardinality, turnover limits). Activation: quantum portfolio, quantum optimization, QAOA portfolio, 量子组合优化, quantum finance optimization, portfolio optimization quantum."
---

# Quantum Portfolio Optimizer

Quantum computing approach to portfolio optimization using QAOA, quantum annealing, and hybrid methods.

## Quick Start

```python
# Basic quantum portfolio optimization
from qiskit_optimization import QuadraticProgram
from qiskit_optimization.algorithms import QAOA

# 1. Define portfolio problem as QUBO
qp = QuadraticProgram("portfolio")
qp.binary_var_list(assets)  # n assets -> n binary variables

# 2. Set objective: maximize return - risk penalty
qp.minimize(linear=-expected_returns, quadratic=risk_covariance)

# 3. Add constraints (optional)
qp.linear_constraint(cardinality_constraint)  # max k assets

# 4. Solve with QAOA
qaoa = QAOA(quantum_instance, reps=3)
result = qaoa.solve(qp)
selected_assets = result.x
```

## Core Workflow

### Step 1: Problem Formulation

Convert portfolio optimization to QUBO (Quadratic Unconstrained Binary Optimization):

```
Objective: min Σ_i(-μ_i x_i) + λ Σ_iΣ_j(σ_ij x_i x_j)

Where:
- x_i ∈ {0,1}: binary selection variable for asset i
- μ_i: expected return of asset i
- σ_ij: covariance between assets i and j
- λ: risk penalty coefficient
```

**Higher-order moments extension** (from arxiv:2509.01496):
```
Add skewness S and kurtosis K terms:
min Σ_i(-μ_i x_i) + λ Σ_ij(σ_ij x_i x_j) - γ Σ_ijk(S_ijk x_i x_j x_k) + δ Σ_ijkl(K_ijkl x_i x_j x_k x_l)
```

### Step 2: Algorithm Selection

| Algorithm | Best For | Implementation |
|-----------|----------|----------------|
| **QAOA** | Gate-based QC, general problems | `qiskit_optimization.algorithms.QAOA` |
| **Quantum Annealing** | D-Wave, large sparse problems | `dwave.system.samplers.DWaveSampler` |
| **VQE** | Variational approach, NISQ | `qiskit.algorithms.VQE` |
| **Hybrid** | Practical applications | Classical optimizer + quantum sampling |

### Step 3: Constraint Handling

Real-world constraints from arxiv:2504.08843:

```python
# Cardinality constraint: select exactly k assets
qp.linear_constraint(
    constraint={'x_1': 1, 'x_2': 1, ...},
    sense='==',
    rhs=k,
    name='cardinality'
)

# Turnover constraint: limit change from current portfolio
qp.linear_constraint(
    constraint={f'delta_{i}': 1 for i in assets},
    sense='<=',
    rhs=max_turnover,
    name='turnover'
)

# Budget constraint
qp.linear_constraint(
    constraint={f'w_{i}': price[i] for i in assets},
    sense='<=',
    rhs=budget,
    name='budget'
)
```

### Step 4: Hybrid Quantum-Classical

For practical NISQ-era implementation:

```python
# Hybrid approach from arxiv:2407.19857
def hybrid_portfolio_optimization(returns, covariance, params):
    """
    1. Classical preprocessing: filter candidates, compute statistics
    2. Quantum optimization: solve reduced QUBO
    3. Classical postprocessing: refine allocation, validate constraints
    """
    # Pre-classical: reduce problem size
    top_assets = classical_filter(returns, top_n=20)
    
    # Quantum: solve reduced problem
    qp = build_qubo(top_assets, returns, covariance)
    quantum_solution = qaoa.solve(qp)
    
    # Post-classical: continuous allocation
    weights = refine_allocation(quantum_solution, constraints)
    
    return weights
```

## Tools Used

- `exec`: Run Python quantum optimization scripts
- `write`: Create optimization code and results
- `read`: Load existing configurations and data

## Key Papers (References)

| Paper | Contribution | arXiv ID |
|-------|--------------|----------|
| Higher-Order Portfolio Optimization with QAOA | Skewness, kurtosis terms | 2509.01496 |
| End-to-End Portfolio Optimization with Quantum Annealing | Practical hybrid approach | 2504.08843 |
| PO-QA Framework | Quantum algorithm framework | 2407.19857 |
| Quantum Computing for Finance: State of the Art | Comprehensive review | 2006.14510 |
| Reverse Quantum Annealing | Alternative annealing strategy | 1810.08584 |

## Activation Keywords

- quantum portfolio
- quantum optimization
- QAOA portfolio
- 量子组合优化
- quantum finance
- portfolio quantum
- quantum annealing portfolio
- higher-order portfolio

## Error Handling

### QUBO Conversion Issues
- Check covariance matrix is positive semi-definite
- Scale parameters appropriately (λ, γ, δ)
- Validate binary variable encoding

### Quantum Hardware Limitations
- For NISQ devices: reduce problem size first
- Use noise mitigation techniques
- Consider hybrid classical fallback

### Constraint Violation
- Add penalty terms to objective function
- Use penalty coefficients for soft constraints
- Validate solution post-processing

## Examples

### Example 1: Basic Portfolio Selection

**User**: "用量子计算优化一个5资产组合"

**Agent**: Creates QUBO formulation, runs QAOA simulation, returns optimal asset selection with expected return and risk metrics.

### Example 2: Higher-Order Optimization

**User**: "考虑偏度和峰度的量子组合优化"

**Agent**: Extends QUBO with skewness (3rd order) and kurtosis (4th order) terms, solves with deeper QAOA circuit, reports improved risk-adjusted returns.

### Example 3: Constrained Optimization

**User**: "量子组合优化加上基数约束（最多选3个资产）"

**Agent**: Adds cardinality constraint to QUBO, uses penalty method or constraint encoding, validates final selection meets constraint.

## Resources

- `references/algorithms.md`: Detailed algorithm comparison
- `references/qubo_formulation.md`: Mathematical formulation guide
- `scripts/portfolio_qaoa.py`: Ready-to-run QAOA implementation
- `scripts/hybrid_optimizer.py`: Hybrid quantum-classical workflow