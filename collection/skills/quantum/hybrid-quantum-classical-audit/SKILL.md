# Hybrid Quantum-Classical Audit Protocol

## Description
Four-metric audit protocol for evaluating hybrid quantum-classical solvers, particularly D-Wave's hybrid portfolio optimization service. Decomposes wall-clock time into QPU access time, classical decomposition time, and reassembly time to understand where computation actually occurs.

## Source
Paper: "Where the Quantum Lives in D-Wave Hybrid Portfolio Optimization: An Operational Decomposition Audit"
Author: Luis Lozano
arXiv: 2605.17623

## Activation
arxiv:2605.17623, hybrid quantum-classical audit, D-Wave hybrid, operational decomposition, QPU time analysis, portfolio optimization audit, quantum advantage verification, wall-clock decomposition

## Usage Scenarios
- Auditing hybrid quantum-classical solver performance
- Determining actual quantum contribution to hybrid algorithms
- Evaluating quantum advantage claims in commercial services
- Comparing quantum-classical decomposition pipelines
- Benchmarking quantum vs classical wall-clock performance

## Core Patterns

### 1. Four-Metric Audit Protocol
```python
def audit_hybrid_solver(service_results, classical_anchor):
    """Four-metric audit protocol for hybrid quantum-classical solvers.
    
    Key finding: QPU access time is only 0.68% of wall-clock budget,
    with 99% being classical decomposition and feasibility reassembly.
    """
    metrics = {
        't_run': service_results['t_run'],          # Total wall-clock time
        't_charge': service_results['t_charge'],    # Billable compute time
        't_QPU': service_results['t_QPU'],          # Actual QPU access time
        'qpu_fraction': service_results['t_QPU'] / service_results['t_run'],
        'classical_fraction': 1 - (service_results['t_QPU'] / service_results['t_run']),
        'classical_anchor_performance': classical_anchor['objective'],
        'hybrid_performance': service_results['objective'],
        'performance_delta': abs(service_results['objective'] - classical_anchor['objective'])
    }
    return metrics
```

### 2. Density-Axis Collapse Analysis
```python
def analyze_density_collapse(covariance_matrix, cardinality_penalty):
    """Analyze how cardinality penalty contributes dense rank-one term.
    
    The penalty encoding adds a term that fully connects the logical graph
    regardless of input covariance density, causing BQM degradation.
    """
    # Original covariance density
    original_density = np.count_nonzero(covariance_matrix) / (n*n)
    
    # After penalty: dense rank-one term makes graph complete
    penalty_density = 1.0  # Complete graph
    
    # Density-axis collapse: ratio of densities
    collapse_factor = penalty_density / original_density
    
    return {
        'original_density': original_density,
        'penalty_density': penalty_density,
        'collapse_factor': collapse_factor,
        'chain_break_prediction': predict_chain_breaks(collapse_factor)
    }
```

### 3. CPU-Only Counterfactual Benchmark
```python
def run_cpu_counterfactual(instances, wall_clock_budget=5.0):
    """Run classical heuristic at same wall-clock budget as hybrid service.
    
    Key finding: TabuSampler on penalty-encoded BQM reaches objectives
    within mean absolute delta 0.001 of hybrid CQM.
    """
    results = []
    for instance in instances:
        # Run classical heuristic with same time budget
        classical_result = run_tabu_sampler(
            instance.bqm,
            time_limit=wall_clock_budget
        )
        
        # Compare with hybrid result
        delta = abs(classical_result.objective - hybrid_result.objective)
        results.append({
            'instance': instance.id,
            'classical_objective': classical_result.objective,
            'hybrid_objective': hybrid_result.objective,
            'delta': delta,
            'wall_clock_matched': True
        })
    return results
```

## Implementation Guidelines

### Audit Protocol Steps
1. **Collect all timing fields**: t_run, t_charge, t_QPU from SDK
2. **Compute QPU fraction**: t_QPU / t_run
3. **Run classical anchor**: Gurobi MIQP or simulated annealing
4. **Compute performance delta**: |hybrid - classical|
5. **Run CPU counterfactual**: Classical heuristic at same wall-clock budget
6. **Analyze density collapse**: Impact of penalty encoding on graph density

### Key Questions to Answer
- What percentage of wall-clock time is actual quantum computation?
- Does the hybrid service outperform classical heuristics at matched budgets?
- How does the cardinality penalty affect problem structure?
- What is the contribution of classical decomposition vs quantum sampling?

### Reporting Template
```
QPU Access Time: {t_QPU}s ({qpu_fraction:.2%} of wall-clock)
Classical Decomposition: {classical_time}s ({classical_fraction:.2%})
Performance vs Classical Anchor: {delta:.6f}
CPU Counterfactual Delta: {cpu_delta:.6f}
Density Collapse Factor: {collapse_factor:.1f}x
```

## Pitfalls
- **Misleading QPU fraction**: Low QPU time fraction doesn't automatically
  mean no quantum advantage; quantum may enable classical decomposition
- **Wall-clock matching**: Must ensure fair comparison by matching wall-clock
  budgets between hybrid and classical methods
- **Out-of-sample validation**: In-sample results may not generalize;
  always validate on unseen portfolio data
- **Sharpe ratio comparison**: QPU portfolios (1.94) may underperform
  simple 1/N baseline (2.22) on out-of-sample data

## Verification
1. Implement four-metric audit protocol on target hybrid service
2. Run CPU counterfactual at matched wall-clock budget
3. Compute density collapse factor for penalty-encoded formulation
4. Validate on out-of-sample portfolio data (e.g., Fama-French 49)
