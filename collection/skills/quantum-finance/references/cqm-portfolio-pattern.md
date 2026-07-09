# CQM Portfolio Optimization Pattern (Penalty-Free)

## Problem
Standard QUBO with cardinality penalty `k*(Σx_i - C)²` creates dense all-ones matrix → complete logical interaction graph → chain breaks 83-92% on D-Wave Pegasus/Zephyr.

## Solution: Constrained Quadratic Model (CQM)

```python
import dimod
from dwave.system import LeapHybridCQMSampler

def penalty_free_portfolio(cov_matrix, expected_returns, n_assets, k_assets, budget=1.0):
    """Portfolio optimization using CQM with hard constraints (not penalty terms)."""
    x = dimod.Binary('x', n_assets)
    
    cqm = dimod.ConstrainedQuadraticModel()
    
    # Objective: minimize variance - maximize return
    # x @ cov @ x - 2 * mu @ x
    objective = x @ cov_matrix @ x - 2 * expected_returns @ x
    cqm.set_objective(objective)
    
    # Hard constraints (NOT penalty terms)
    cqm.add_constraint(sum(x) <= budget, label='budget')
    cqm.add_constraint(sum(x) == k_assets, label='cardinality')
    
    # Optional: individual asset bounds
    for i in range(n_assets):
        cqm.add_constraint(x[i] <= 0.1, label=f'max_weight_{i}')
    
    sampler = LeapHybridCQMSampler()
    sampleset = sampler.sample_cqm(cqm, time_limit=5.0)
    
    # Filter feasible solutions
    feasible = sampleset.filter(lambda d: d.is_feasible)
    return feasible.first.sample if feasible else sampleset.first.sample
```

## Key Metrics (from arxiv:2605.17628)
- Chain break fraction: <0.04% (vs 83-92% with penalty QUBO)
- Regret vs classical optimum: ≤0.03% at N≤49
- QPU access time: ~0.034s of 5s budget (0.7%)
- Tested range: N=10 to N=640 assets

## When to Use CQM vs QUBO
- **CQM**: When constraints are complex (cardinality, bounds, turnover)
- **QUBO**: Only for unconstrained or simple bound problems
- **Classical**: For N>500 where quantum contribution is negligible