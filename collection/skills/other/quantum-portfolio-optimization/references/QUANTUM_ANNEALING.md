# Quantum Annealing Implementation

## Overview

Portfolio optimization using quantum annealing (D-Wave systems).

## QUBO Formulation

### Standard Portfolio QUBO

```
min Σ_i Σ_j Q_ij·x_i·x_j
```

Where:
- x_i ∈ {0, 1}: binary decision (include/exclude asset)
- Q_ij: QUBO coefficients encoding objective and constraints

### Objective Encoding

```python
def portfolio_qubo(
    returns: np.ndarray,
    cov_matrix: np.ndarray,
    risk_weight: float,
    budget_penalty: float,
    cardinality_penalty: float,
    max_assets: int
):
    """
    Formulate portfolio optimization as QUBO.
    
    Returns:
        Q: QUBO matrix
    """
    
    n = len(returns)
    Q = {}
    
    # Return terms (maximize → minimize -return)
    for i in range(n):
        Q[(i, i)] = -returns[i]
    
    # Risk terms (variance)
    for i in range(n):
        for j in range(i, n):
            if i == j:
                Q[(i, i)] += risk_weight * cov_matrix[i, i]
            else:
                Q[(i, j)] += risk_weight * 2 * cov_matrix[i, j]
    
    # Budget constraint: Σx_i = K (fixed number of assets)
    # Penalty: (Σx_i - K)²
    for i in range(n):
        Q[(i, i)] += budget_penalty * (1 - 2*max_assets)
    for i in range(n):
        for j in range(i+1, n):
            Q[(i, j)] += 2 * budget_penalty
    
    # Cardinality constraint: optionally use different encoding
    
    return Q
```

## D-Wave Implementation

```python
from dwave.system import DWaveSampler, EmbeddingComposite
from dimod import BinaryQuadraticModel

def quantum_annealing_portfolio(
    returns: np.ndarray,
    cov_matrix: np.ndarray,
    risk_weight: float = 0.5,
    max_assets: int = 10,
    num_reads: int = 1000
):
    """
    Portfolio optimization via quantum annealing.
    
    Args:
        returns: Expected returns
        cov_matrix: Covariance matrix
        risk_weight: Risk penalty λ
        max_assets: Budget constraint K
        num_reads: Annealing reads
    
    Returns:
        Optimal portfolio weights
    """
    
    n_assets = len(returns)
    
    # Formulate QUBO
    Q = portfolio_qubo(
        returns,
        cov_matrix,
        risk_weight,
        budget_penalty=10.0,
        cardinality_penalty=0.0,
        max_assets=max_assets
    )
    
    # Convert to BQM
    bqm = BinaryQuadraticModel.from_qubo(Q)
    
    # Connect to D-Wave
    sampler = EmbeddingComposite(DWaveSampler())
    
    # Execute annealing
    response = sampler.sample(
        bqm,
        num_reads=num_reads,
        annealing_time=200  # microseconds
    )
    
    # Extract best solution
    best_solution = response.first.sample
    energies = response.record.energy
    
    # Decode to weights
    selected_assets = [i for i, x in best_solution.items() if x == 1]
    
    # Equal weight or optimized weight
    weights = np.zeros(n_assets)
    weights[selected_assets] = 1.0 / len(selected_assets)
    
    return weights, selected_assets, response
```

## Hybrid Quantum-Classical

### Workflow

1. **Quantum annealing**: Solve discrete selection (which assets)
2. **Classical optimizer**: Optimize continuous weights (how much)

```python
def hybrid_portfolio_optimization(
    returns: np.ndarray,
    cov_matrix: np.ndarray,
    quantum_sampler,
    risk_weight: float,
    max_assets: int
):
    """
    Hybrid quantum-classical portfolio optimization.
    
    Step 1: Quantum annealing selects asset subset
    Step 2: Classical optimizer determines weights
    """
    
    n = len(returns)
    
    # Step 1: Quantum selection
    Q = selection_qubo(returns, cov_matrix, risk_weight, max_assets)
    bqm = BinaryQuadraticModel.from_qubo(Q)
    
    response = quantum_sampler.sample(bqm, num_reads=1000)
    selected = [i for i, x in response.first.sample.items() if x == 1]
    
    # Step 2: Classical weight optimization
    from scipy.optimize import minimize
    
    def objective(w):
        # Only optimize selected assets
        portfolio_return = np.dot(w, returns[selected])
        portfolio_risk = np.dot(w, np.dot(cov_matrix[selected][:, selected], w))
        return -portfolio_return + risk_weight * portfolio_risk
    
    # Constraints
    constraints = [
        {'type': 'eq', 'fun': lambda w: np.sum(w) - 1.0}  # Budget
    ]
    
    # Bounds
    bounds = [(0, 1) for _ in selected]
    
    # Initial guess
    init_weights = np.ones(len(selected)) / len(selected)
    
    # Optimize
    result = minimize(
        objective,
        init_weights,
        method='SLSQP',
        bounds=bounds,
        constraints=constraints
    )
    
    # Map back to full portfolio
    full_weights = np.zeros(n)
    full_weights[selected] = result.x
    
    return full_weights
```

## Advanced Constraints

### Turnover Constraint

Limit portfolio changes from previous state:

```python
def turnover_constraint_qubo(Q, prev_weights, turnover_penalty):
    """
    Add turnover constraint to QUBO.
    
    Limit: Σ|x_i - prev_i| ≤ turnover_limit
    """
    
    for i in range(len(prev_weights)):
        if prev_weights[i] == 1:
            # Asset was in portfolio
            Q[(i, i)] += turnover_penalty * -1  # Encourage keeping
        else:
            # Asset was not in portfolio
            Q[(i, i)] += turnover_penalty * 1   # Penalize adding
    
    return Q
```

### Sector Exposure Limits

```python
def sector_constraint_qubo(Q, sector_labels, sector_limits, penalty):
    """
    Add sector exposure constraints.
    
    For each sector s:
        Σ_{i in sector_s} x_i ≤ limit_s
    """
    
    sectors = set(sector_labels)
    
    for sector in sectors:
        assets_in_sector = [i for i, s in enumerate(sector_labels) if s == sector]
        limit = sector_limits[sector]
        
        # Penalty: (Σx_i - limit)² for each sector
        for i in assets_in_sector:
            Q[(i, i)] += penalty * (1 - 2*limit)
        
        for i in assets_in_sector:
            for j in assets_in_sector:
                if i < j:
                    Q[(i, j)] += 2 * penalty
    
    return Q
```

## Performance Optimization

### Chain Management

D-Wave embedding may chain multiple qubits:

```python
# Check chain strength
chain_strength = 2 * max(abs(Q.values()))

# Auto-tune chain strength
from dwave.system import FixedEmbeddingComposite

sampler = FixedEmbeddingComposite(
    DWaveSampler(),
    embedding=find_embedding(Q),
    chain_strength=chain_strength
)
```

### Annealing Schedule

Custom annealing schedule for better convergence:

```python
response = sampler.sample(
    bqm,
    num_reads=1000,
    annealing_schedule=[
        [0.0, 0.0],    # Start: pause
        [20.0, 0.2],   # Gradual ramp
        [40.0, 0.5],   # Mid-point
        [60.0, 0.8],   # Near end
        [100.0, 1.0]   # End: quantum state
    ]
)
```

## Resources

- D-Wave Ocean SDK documentation
- Portfolio optimization examples: https://github.com/dwavesystems/qubo-examples
- Hybrid workflow tutorials: https://docs.dwavesys.com/