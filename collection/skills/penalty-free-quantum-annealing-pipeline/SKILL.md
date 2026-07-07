# Penalty-Free Quantum Annealing Pipeline

## Description
Methodology for direct quantum annealer portfolio optimization without cardinality penalty encoding. Removes the penalty entirely from QUBO formulation, samples objective-only QUBO on hardware, and enforces cardinality classically through deterministic feasibility projector.

## Source
Paper: "A Penalty-Free Pipeline for Direct Quantum-Annealer Portfolio Optimization"
Author: Luis Lozano
arXiv: 2605.17628

## Activation
arxiv:2605.17628, penalty-free quantum annealing, QUBO portfolio optimization, D-Wave Pegasus, D-Wave Zephyr, chain-break reduction, cardinality constraint, quantum annealer, feasibility projector

## Usage Scenarios
- Direct quantum annealer portfolio optimization with cardinality constraints
- Reducing chain-break fractions on D-Wave hardware
- Bypassing penalty encoding limitations in QUBO formulation
- Topology-aware sparsification for quantum annealing
- Feasibility-aware post-processing for quantum solutions

## Core Patterns

### 1. Penalty-Free QUBO Formulation
```python
def create_penalty_free_qubo(expected_returns, covariance_matrix, risk_aversion):
    """Create objective-only QUBO without cardinality penalty.
    
    Traditional approach: QUBO = -returns + risk * covariance + penalty * cardinality
    This approach: QUBO = -returns + risk * covariance (penalty removed)
    
    The cardinality constraint is enforced classically after sampling.
    """
    n_assets = len(expected_returns)
    
    # Linear term: negative expected returns (maximize returns)
    Q_linear = -np.array(expected_returns)
    
    # Quadratic term: risk-scaled covariance
    Q_quadratic = risk_aversion * covariance_matrix
    
    # Objective-only QUBO (no penalty term)
    # This avoids the dense rank-one term from penalty encoding
    # that causes chain breaks on hardware
    
    return Q_linear, Q_quadratic
```

### 2. Deterministic Feasibility Projector
```python
def feasibility_projector(solution, target_cardinality, expected_returns):
    """Enforce cardinality constraint classically after quantum sampling.
    
    Takes quantum samples (which may violate cardinality) and projects
    them to valid cardinality-constrained solutions.
    """
    n_assets = len(solution)
    selected_indices = np.where(solution > 0.5)[0]
    
    if len(selected_indices) == target_cardinality:
        return solution  # Already feasible
    
    if len(selected_indices) > target_cardinality:
        # Remove lowest-return assets
        asset_returns = expected_returns[selected_indices]
        keep_indices = np.argsort(asset_returns)[-target_cardinality:]
        projected = np.zeros(n_assets)
        projected[selected_indices[keep_indices]] = 1.0
    else:
        # Add highest-return unselected assets
        unselected = np.setdiff1d(np.arange(n_assets), selected_indices)
        asset_returns = expected_returns[unselected]
        add_indices = np.argsort(asset_returns)[-target_cardinality + len(selected_indices):]
        projected = solution.copy()
        projected[unselected[add_indices]] = 1.0
    
    return projected
```

### 3. Chain-Break Analysis Protocol
```python
def analyze_chain_breaks(embedding_records, hardware='pegasus'):
    """Analyze chain-break fractions across quantum annealer embeddings.
    
    Key finding: Standard penalty encoding produces chain-break fractions
    from 83% (small universes) to 92% (full 49-industry universe).
    Penalty-free pipeline reduces to at most 0.04%.
    """
    metrics = {
        'chain_break_fraction': compute_mean_chain_break(embedding_records),
        'feasible_sample_rate': compute_feasible_rate(embedding_records),
        'post_processed_regret': compute_regret_vs_greedy(embedding_records),
        'hardware': hardware
    }
    return metrics
```

## Implementation Guidelines

### Pipeline Architecture
```
1. Formulate objective-only QUBO (returns + risk * covariance)
2. Embed on quantum hardware (Pegasus/Zephyr topology)
3. Sample from quantum annealer
4. Apply deterministic feasibility projector
5. Select best solution from post-processed samples
```

### Key Parameters
- **Risk aversion**: Controls trade-off between returns and risk in QUBO
- **Target cardinality**: Number of assets in portfolio (enforced classically)
- **Number of reads**: Quantum samples to collect (typically 1000-10000)
- **Annealing time**: Duration of quantum annealing process

### Hardware-Specific Notes
- **D-Wave Pegasus**: ~5000+ qubits, limited connectivity compared to Zephyr
- **D-Wave Zephyr**: ~7000+ qubits, improved connectivity
- **Chain breaks**: Primary failure mode for penalty-encoded formulations
- **Embedding quality**: Critical for solution quality; use topology-aware sparsification

## Pitfalls
- **No quantum advantage claimed**: This pipeline does not demonstrate quantum
  advantage over classical solvers; it demonstrates feasibility improvement
- **Classical projector dominates**: Post-processing step dominates solution quality
- **Sparsification trade-off**: Removing off-diagonal entries reduces chain breaks
  but may dilute the cardinality constraint signal
- **Scale limitations**: Tested up to 49 assets; results may not generalize to
  much larger universes

## Verification
1. Implement penalty-free QUBO formulation
2. Compare chain-break fractions with penalty-encoded baseline
3. Validate feasibility projector correctness
4. Benchmark against classical greedy reference (regret <= 0.03%)
