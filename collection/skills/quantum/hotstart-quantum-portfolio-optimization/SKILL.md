---
name: hotstart-quantum-portfolio-optimization
description: "Hot-starting methodology for quantum portfolio optimization — restricting search space to discrete solutions near the continuous optimum by constructing a compact Hilbert space, reducing qubit requirements."
---

# Hot-Starting Quantum Portfolio Optimization

## Description
Methodology for hot-starting quantum portfolio optimization by restricting the search space to discrete solutions in the vicinity of the continuous optimum through compact Hilbert space construction. This approach reduces the number of required qubits and improves quantum optimization performance for mean-variance portfolio problems with cardinality constraints.

## Activation Keywords
- hot-start quantum optimization
- 热启动量子组合优化
- warm-start QAOA
- quantum portfolio hot-start
- compact Hilbert space optimization
- discrete mean-variance optimization
- quantum QUBO reduction
- 量子组合优化热启动

## Tools Used
- terminal: Run quantum circuit simulators, Qiskit/PennyLane scripts
- search_files: Locate quantum optimization codebases
- read_file: Read quantum circuit definitions
- write_file: Create QUBO formulations

## Usage Patterns

### Pattern 1: Hot-Start Portfolio Optimization
When solving discrete mean-variance portfolio optimization with quantum annealers or QAOA:
1. Solve the relaxed continuous optimization problem classically
2. Construct a compact Hilbert space around the continuous optimum
3. Map the restricted discrete search space to a reduced QUBO
4. Run quantum optimization on the reduced problem

### Pattern 2: Qubit Reduction via Search Space Restriction
When facing qubit limitations for portfolio optimization:
1. Identify the continuous optimal solution
2. Define a neighborhood radius k around each asset weight
3. Encode only the discrete points within this neighborhood
4. Achieve O(log(k)) qubit reduction per asset

### Pattern 3: Quantum-Classical Hybrid Pipeline
For production quantum finance workflows:
1. Classical pre-processing: solve relaxed problem
2. Quantum optimization: restricted search space
3. Classical post-processing: feasibility verification
4. Expert evaluation: financial viability assessment

## Instructions for Agents

### Step 1: Formulate the Continuous Relaxation
Given a portfolio optimization problem:
```
minimize: w^T Σ w - λ μ^T w
subject to: sum(w_i) = 1, w_i ∈ {0, 1/K, 2/K, ..., 1}
           cardinality: sum(I(w_i > 0)) ≤ C
```

Solve the relaxed continuous version (w_i ∈ [0, 1]) to get w*.

### Step 2: Construct Compact Hilbert Space
1. For each asset i, define discrete levels near w*_i:
   ```
   levels_i = {max(0, w*_i - δ), ..., min(1, w*_i + δ)}
   ```
   where δ controls the neighborhood size
2. Encode each asset with ceil(log2(|levels_i|)) qubits
3. Total qubits = Σ ceil(log2(|levels_i|)) ≪ N * ceil(log2(K+1))

### Step 3: Build Reduced QUBO
1. Map discrete levels to binary variables
2. Construct QUBO objective: x^T Q x
3. Add constraints as penalty terms:
   - Budget constraint: λ_1(sum(w_i) - 1)^2
   - Cardinality: λ_2(sum(I(w_i > 0)) - C)^2

### Step 4: Quantum Optimization
1. Run QAOA or quantum annealing on the reduced QUBO
2. Use appropriate ansatz depth for gate-based approaches
3. For annealers, set appropriate chain strengths

### Step 5: Expert Analysis Evaluation
After quantum optimization:
1. Check diversification: number of non-zero weights
2. Verify risk exposure: portfolio variance within bounds
3. Assess turnover: trading costs from rebalancing
4. Compare against classical benchmarks (Gurobi, simulated annealing)

## Error Handling

### Qubit Limitation
If still too many qubits after hot-starting:
- Reduce δ (neighborhood size)
- Use asset screening to pre-filter
- Apply hierarchical optimization (sector → asset)

### Solution Infeasibility
If quantum solution violates constraints:
- Increase penalty weights λ_1, λ_2
- Use constraint-native interfaces (D-Wave LeapHybridCQM)
- Apply feasibility-aware reassembly

### Barren Plateaus
If QAOA optimization fails to converge:
- Use warm-started initial parameters from classical solution
- Apply layerwise training
- Reduce circuit depth

## Examples

### Example 1: Mean-Variance Portfolio with Cardinality Constraint
```python
from qaoa import QAOA
import numpy as np

# Step 1: Solve continuous relaxation
w_cont = classical_mean_variance(mu, Sigma, cardinality=C)

# Step 2: Define discrete levels around continuous optimum
delta = 0.1  # neighborhood radius
discrete_weights = []
for w_i in w_cont:
    levels = np.arange(max(0, w_i - delta), min(1, w_i + delta), 0.05)
    discrete_weights.append(levels)

# Step 3: Build QUBO with reduced encoding
Q = build_qubo(Sigma, mu, discrete_weights, lambda_budget=10, lambda_card=5)

# Step 4: Run QAOA
qaoa = QAOA(Q, p=3, initial_params=warm_start_params(w_cont))
result = qaoa.optimize()
```

## Resources
- arXiv: 2510.11153 - Hot-Starting Quantum Portfolio Optimization
- arXiv: 2507.20532 - Quantum Portfolio Optimization with Expert Analysis Evaluation
- arXiv: 2605.17623 - Where the Quantum Lives in D-Wave Hybrid Portfolio Optimization

## Related Skills
- quantum-portfolio-optimizer
- qaoa-optimization
- quantum-ml-patterns
- quantum-finance-portfolio
