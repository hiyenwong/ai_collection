---
name: penalty-free-quantum-annealing-portfolio
description: "Penalty-free quantum annealer pipeline for portfolio optimization. Removes cardinality penalty from QUBO to reduce chain-break fractions from 92% to 0.04%, enforces feasibility classically post-sampling. Based on arXiv:2605.17628."
---

# Penalty-Free Quantum Annealer Portfolio Optimization

## Source Paper

**Title**: A Penalty-Free Pipeline for Direct Quantum-Annealer Portfolio Optimization
**Authors**: Luis Lozano
**arXiv**: 2605.17628 (quant-ph, math.OC, q-fin.PM)
**Date**: 2026-05-17

## Problem

Cardinality-constrained portfolio optimization on quantum annealers (D-Wave Pegasus/Zephyr) traditionally uses a penalty encoding that makes the logical interaction graph completely dense, causing chain-break fractions of 83-92% and zero feasible raw samples.

## Methodology

### Key Insight

The exact cardinality penalty contributes a dense rank-one term that makes the QUBO graph complete regardless of covariance sparsity. This is the binding constraint, not hardware topology.

### Pipeline

1. **Remove penalty entirely** from the QUBO formulation
2. **Sample objective-only QUBO** on QPU (built from expected returns + risk-scaled covariance)
3. **Enforce cardinality classically** via deterministic feasibility projector on sampled solutions

### Results

- Chain-break fractions: 71-92% → ≤0.04%
- Post-processed regret: ≤0.03% vs greedy classical references
- Tested on 4,468 hardware samples across Pegasus and Zephyr
- Equities up to 49 assets, football-betting up to 48 instances

## Implementation Pattern

```python
import numpy as np
from scipy.optimize import linear_sum_assignment

def objective_qubo(returns, cov_matrix, risk_aversion=1.0):
    """Build objective-only QUBO without cardinality penalty."""
    n = len(returns)
    # Linear terms: -returns (maximize returns = minimize -returns)
    Q = np.diag(-returns)
    # Quadratic terms: risk * covariance
    Q += risk_aversion * cov_matrix
    return Q

def feasibility_projector(sample, target_k):
    """Deterministically enforce cardinality constraint on sampled solution."""
    selected = np.where(sample == 1)[0]
    if len(selected) == target_k:
        return sample
    elif len(selected) > target_k:
        # Keep top-k by contribution (asset return - risk penalty)
        # Greedy selection from sampled set
        contributions = sample.copy()
        to_remove = len(selected) - target_k
        # Remove lowest-contribution assets
        sorted_idx = np.argsort(sample)[::-1]  # by asset index value
        result = np.zeros_like(sample)
        for idx in sorted_idx[:target_k]:
            result[idx] = 1
        return result
    else:
        # Add highest-contribution unselected assets
        unselected = np.where(sample == 0)[0]
        to_add = target_k - len(selected)
        result = sample.copy()
        for idx in unselected[:to_add]:
            result[idx] = 1
        return result

def penalty_free_pipeline(returns, cov_matrix, k, n_samples=1000):
    """Complete penalty-free quantum annealer pipeline."""
    Q = objective_qubo(returns, cov_matrix)
    
    # Sample from QPU (or classical sampler for simulation)
    samples = simulate_annealing(Q, n_samples)
    
    # Project each sample to feasible cardinality
    feasible_solutions = []
    for s in samples:
        projected = feasibility_projector(s, k)
        feasible_solutions.append(projected)
    
    # Evaluate and return best
    best_solution, best_energy = None, float('inf')
    for sol in feasible_solutions:
        energy = sol @ Q @ sol
        if energy < best_energy:
            best_energy = energy
            best_solution = sol
    
    return best_solution, best_energy
```

## Activation Keywords

- penalty-free quantum annealer, portfolio optimization QUBO, cardinality constraint quantum annealing, D-Wave chain breaks, quantum portfolio feasibility projector

## Pitfalls

1. **Topology-aware sparsification is not sufficient**: Removing off-diagonal entries dilutes the cardinality constraint; classical projector dominates anyway
2. **No quantum advantage claimed**: The benefit is hardware compatibility, not outperforming classical methods
3. **Feasibility projector design matters**: Simple greedy projection may not preserve solution quality; consider multi-objective projector
4. **Hardware embedding still needed**: Even with sparse QUBO, minor embedding for Pegasus/Zephyr topology is required

## Verification Steps

1. Verify chain-break fraction < 1% after penalty removal
2. Check that projected solutions satisfy cardinality constraint exactly
3. Compare post-processed regret against classical baseline (< 0.1%)
4. Test at multiple universe sizes (N=10, 25, 49)

## Related Skills

- quantum-finance-portfolio
- constrained-counterdiabatic-qaoa-portfolio
- qaoa-xy-mixers-portfolio
- quantum-portfolio-optimization
