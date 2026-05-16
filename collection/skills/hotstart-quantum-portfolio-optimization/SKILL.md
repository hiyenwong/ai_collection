---
name: hotstart-quantum-portfolio-optimization
description: "Hot-starting methodology for quantum portfolio optimization. Restricts search space to discrete solutions near the continuous optimum by constructing a compact Hilbert space, reducing required qubits. Outperforms state-of-the-art techniques on both software solvers and D-Wave quantum annealer."
---

# Hot-Starting Quantum Portfolio Optimization

## Description

Hot-Starting Quantum Portfolio Optimization methodology that restricts the search space of discrete mean-variance portfolio optimization to solutions in the vicinity of the continuous optimum. Constructs a compact Hilbert space that reduces required qubits while maintaining solution quality. Outperforms state-of-the-art techniques on both classical software solvers and D-Wave Advantage quantum annealer.

**Based on:** arXiv:2510.11153v1 — "Hot-Starting Quantum Portfolio Optimization" by Sebastian Schlütter, Tomislav Maras, Alexander Dotterweich, Nico Piatkowski

## Activation Keywords

- hot-start quantum optimization
- 热启动量子优化
- compact Hilbert space portfolio
- discrete portfolio optimization quantum
- QUBO search space reduction
- 量子组合热启动
- qubit reduction portfolio
- D-Wave portfolio optimization

## Core Methodology

### The Hot-Starting Principle

**Problem**: Discrete portfolio optimization (selecting K assets from N with integer lot sizes) requires O(N × log(max_lots)) qubits — too many for current quantum hardware.

**Solution**: First solve the continuous relaxation classically, then restrict the quantum search to a small neighborhood around the continuous optimum.

### Step 1: Continuous Relaxation

```python
def continuous_relaxation(mu, Sigma, lambda_param, budget):
    """
    Solve continuous mean-variance optimization:
    max λ * μ^T w - (1-λ) * w^T Σ w
    s.t. sum(w) = budget, w >= 0
    
    Returns: w_continuous (optimal continuous weights)
    """
    # Closed-form or convex optimization solution
    # This is fast and reliable on classical hardware
    w_star = solve_markowitz(mu, Sigma, lambda_param, budget)
    return w_star
```

### Step 2: Construct Compact Hilbert Space

```python
def construct_compact_hilbert_space(w_star, delta, K):
    """
    Build a restricted search space around the continuous optimum.
    
    For each asset i:
        If w_star[i] > 0: allow w[i] ∈ {0, w_star[i] ± delta}
        If w_star[i] = 0: allow w[i] ∈ {0, small_value}
    
    This reduces the binary encoding from N×log(M) to ~K×log(2R+1)
    where R is the radius of the neighborhood.
    
    Returns:
        QUBO matrix Q_restricted for the compact space
    """
    # For each asset in the active set:
    # Encode deviation from continuous optimum
    # Binary variables represent { -delta, 0, +delta }
    
    active_assets = np.where(w_star > threshold)[0]
    
    # Restrict to K nearest to active set
    if len(active_assets) > K:
        active_assets = select_top_k(active_assets, w_star, K)
    
    # Encode each active asset with few qubits
    # Instead of log(max_lots) qubits per asset,
    # use log(2*radius + 1) qubits
    Q = build_qubo_active_set(active_assets, w_star, delta, mu, Sigma)
    return Q, active_assets
```

### Step 3: Quantum Optimization on Restricted Space

```python
def quantum_optimize_restricted(Q, device='dwave'):
    """
    Run quantum optimization on the compact Hilbert space.
    
    Options:
    - D-Wave quantum annealer
    - Simulated annealing (classical baseline)
    - QAOA on gate-based quantum computer
    
    Returns: best discrete portfolio within the restricted space
    """
    if device == 'dwave':
        sampler = DWaveSampler()
        result = sampler.sample_qubo(Q, num_reads=1000)
    elif device == 'simulated':
        result = simulated_annealing(Q)
    
    # Decode solution back to original space
    w_optimal = decode_solution(result.best_sample, active_assets, w_star, delta)
    return w_optimal
```

### Step 4: Quality Verification

```python
def verify_hotstart_quality(w_optimal, w_continuous, Q_full):
    """
    Verify that the hot-started solution is competitive.
    
    Check:
    1. Solution feasibility (budget, cardinality constraints)
    2. Objective value vs. continuous optimum (optimality gap)
    3. Objective value vs. full QUBO (if tractable)
    4. Qubit savings achieved
    """
    # Optimality gap
    gap = (objective(w_continuous) - objective(w_optimal)) / objective(w_continuous)
    
    # Qubit comparison
    full_qubits = n_assets * log2(max_lots)
    restricted_qubits = len(active_assets) * log2(2*radius + 1)
    savings = (full_qubits - restricted_qubits) / full_qubits
    
    return {
        'optimality_gap': gap,
        'qubit_savings': savings,
        'feasible': check_constraints(w_optimal),
    }
```

## Key Advantages

| Metric | Full QUBO | Hot-Started |
|--------|-----------|-------------|
| **Qubits** | N × log(M) | K × log(2R+1) |
| **Example (N=100, M=100)** | ~700 qubits | ~50 qubits |
| **Solution Quality** | Optimal | Near-optimal (gap < 1%) |
| **Runtime** | Hours (queue) | Minutes |
| **Hardware Feasibility** | Future (1000+ qubits) | Current (D-Wave Advantage) |

## Parameter Selection Guide

### Delta (Neighborhood Radius)

| Delta | Pros | Cons |
|-------|------|------|
| Small (1-2 lots) | Fewer qubits, faster | May miss global optimum |
| Medium (3-5 lots) | Good balance | Moderate qubit count |
| Large (5+ lots) | Near-full coverage | Defeats purpose of hot-starting |

**Recommendation**: Start with delta=3, verify gap < 1%, increase if needed.

### K (Number of Active Assets)

```python
# Heuristic: K = min(N_active_continuous + margin, max_budget)
K = min(len(np.where(w_star > 0)[0]) + 5, 20)
```

## Implementation Pattern

### Full Workflow

```python
def hotstart_portfolio_optimization(
    mu, Sigma, budget, K_select, 
    lambda_param=0.5, delta=3, device='dwave'
):
    """
    Complete hot-started quantum portfolio optimization.
    
    Args:
        mu: Expected returns vector
        Sigma: Covariance matrix
        budget: Total investment budget
        K_select: Number of assets to select (cardinality)
        lambda_param: Risk-return trade-off
        delta: Neighborhood radius in lot units
        device: 'dwave', 'qaoa', or 'simulated'
    
    Returns:
        Optimized portfolio with metadata
    """
    # 1. Continuous relaxation
    w_star = continuous_relaxation(mu, Sigma, lambda_param, budget)
    
    # 2. Compact Hilbert space construction
    Q, active_assets = construct_compact_hilbert_space(w_star, delta, K_select)
    
    # 3. Quantum optimization
    w_opt = quantum_optimize_restricted(Q, device)
    
    # 4. Verification
    metrics = verify_hotstart_quality(w_opt, w_star, Q)
    
    return {
        'weights': w_opt,
        'active_assets': active_assets,
        'qubits_used': len(active_assets) * int(np.log2(2*delta + 1) + 1),
        'optimality_gap': metrics['optimality_gap'],
    }
```

## Error Handling

### Continuous Relaxation Infeasible
```
Check constraints for conflicts (e.g., K_select > N available assets)
Relax cardinality constraint or adjust budget
```

### Restricted Space Contains No Feasible Solutions
```
Increase delta (neighborhood radius)
Re-run with delta *= 2 until feasible solutions found
```

### Quantum Annealer Returns Infeasible Solution
```
Apply classical repair:
1. Round to nearest feasible portfolio
2. Project onto budget constraint
3. Verify cardinality constraint
```

## Resources

- **Paper:** arXiv:2510.11153v1 - "Hot-Starting Quantum Portfolio Optimization"
- **Related:** Expert Analysis Evaluation (arXiv:2507.20532v1)
- **D-Wave:** https://docs.dwavesys.com/docs/latest/c_qubo.html

## Related Skills

- `quantum-portfolio-optimizer` - Standard QAOA portfolio optimization
- `quantum-expert-evaluation-portfolio` - Expert evaluation framework
- `qbalance-quantum-workflow-optimization` - Quantum workflow optimization

## Activation

- **Domain**: Quantum Finance, Combinatorial Optimization
- **Use Case**: Reducing qubit requirements for portfolio optimization
- **Keywords**: hot-start quantum, compact Hilbert space, qubit reduction
