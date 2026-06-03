---
name: hotstart-quantum-portfolio
description: "Hot-starting methodology for quantum portfolio optimization. Introduces compact Hilbert space QUBO formulation that restricts search space to discrete solutions near the continuous optimum, reducing required qubits and outperforming state-of-the-art techniques on both classical solvers and quantum annealers (D-Wave Advantage). Use when: designing quantum portfolio optimization, implementing warm-start QUBO, reducing qubit requirements for quantum optimization, integrating continuous relaxation insights into quantum algorithms, or solving discrete mean-variance portfolio problems."
---

# Hot-Starting Quantum Portfolio Optimization

## Core Concept

Standard QUBO formulations for discrete portfolio optimization waste qubits searching the entire solution space. This methodology restricts the search to a compact Hilbert space around the pre-computed continuous optimum, dramatically reducing qubit requirements while improving solution quality.

## Key Innovation

1. **Solve continuous relaxation** first (convex problem, efficiently solvable)
2. **Map continuous optimum** to nearest discrete solutions
3. **Construct compact Hilbert space** covering only the vicinity
4. **Encode as reduced QUBO** using fewer qubits
5. **Solve on quantum annealer** or gate-based optimizer

## Qubit Reduction Mechanism

For a portfolio with N assets and integer constraints:
- Standard QUBO: O(N × log(max_allocation)) qubits
- Hot-start QUBO: O(N × log(vicinity_size)) qubits, where vicinity_size ≪ max_allocation

The continuous optimum guides the search to a small neighborhood, enabling logarithmic reduction.

## Workflow

### Step 1: Solve Continuous Relaxation
```python
# Solve smooth convex mean-variance optimization
import cvxpy as cp
w = cp.Variable(N)
objective = cp.Minimize(mu @ w - gamma * cp.quad_form(w, Sigma))
constraints = [cp.sum(w) == budget, w >= 0]
problem = cp.Problem(objective, constraints)
problem.solve()
```

### Step 2: Define Vicinity Around Continuous Optimum
```python
# Round to nearest integers, define search window
w_continuous = w.value
w_floor = np.floor(w_continuous)
w_ceil = np.ceil(w_continuous)
# Define delta_i = w_ceil_i - w_floor_i for each asset
# This creates a compact binary decision space
```

### Step 3: Construct Reduced QUBO
```python
# QUBO formulation: min x^T Q x
# x represents binary decisions for rounding up/down
# Q encodes the objective function restricted to vicinity
Q = build_vicinity_qubo(Sigma, mu, w_continuous, gamma)
```

### Step 4: Solve on Quantum Hardware
```python
# Submit to D-Wave Advantage or simulate
from dwave.system import LeapHybridSampler
sampler = LeapHybridSampler()
result = sampler.sample_qubo(Q)
```

### Step 5: Post-Process and Validate
```python
# Convert binary solution back to portfolio weights
# Validate against financial criteria: diversification, risk exposure
portfolio_weights = decode_solution(result.best_sample, w_floor)
```

## When to Use

- Discrete portfolio optimization with integer quantity constraints
- Quantum annealing on limited-qubit hardware
- When continuous relaxation is convex/smooth and efficiently solvable
- Need to reduce qubit requirements for near-term quantum advantage

## Comparison to Alternatives

| Method | Qubit Count | Solution Quality | Runtime |
|--------|-------------|------------------|---------|
| Full QUBO | O(N log M) | Moderate | High |
| Warm-start (gate) | O(N log M) | Moderate | Medium |
| **Hot-start (this)** | **O(N log δ)** | **High** | **Low** |

Where M = max_allocation, δ = vicinity_size (typically δ << M).

## Error Handling

### Continuous Optimum Not Unique
If multiple continuous optima exist, create vicinities around each and solve multiple reduced QUBOs in parallel.

### Vicinity Too Small
If quantum solution consistently hits boundary, expand vicinity size by 1-2 bits per asset.

### Hardware Noise
On noisy quantum annealers, run multiple reads and take majority vote for binary decisions.

## Related Skills
- quantum-portfolio-optimization: General QAOA/QUBO portfolio patterns
- quantum-finance: Broader quantum computing in finance
- constraint-preserving-quantum-mixers: XY-mixer approaches for constrained optimization

## References
- arXiv: 2510.11153 - "Hot-Starting Quantum Portfolio Optimization" (Schlüter et al., 2025)
- Demonstrated on D-Wave Advantage quantum annealer with 5000+ qubits
