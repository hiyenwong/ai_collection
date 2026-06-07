# QAOA Algorithm Details

## QAOA for Common Problems

### MaxCut

For graph G = (V, E), maximize cut edges:
- H_C = 1/2 Σ_{(i,j)∈E} (I - Z_i Z_j)
- Optimal cut = argmin ⟨ψ|H_C|ψ⟩

### Portfolio Optimization

Maximize return while minimizing risk:
- H_C = -Σ μ_i Z_i + λ Σ σ_ij Z_i Z_j
- μ_i = expected return, σ_ij = covariance

### Number Partitioning

Partition set S into two equal-sum subsets:
- H_C = (Σ s_i Z_i)²

## QAOA Variants

### Recursive QAOA (RQAOA)
- Fix variables iteratively based on correlations
- Reduces problem size at each step

### Adaptive QAOA
- Vary mixer Hamiltonian based on problem structure
- Can achieve better approximation ratios

### Multi-Angle QAOA
- Different parameters for each qubit/edge
- More expressive but more parameters to optimize

## Classical Baselines

Always compare QAOA against:
- Simulated annealing
- Goemans-Williamson (MaxCut: 0.878-approximation)
- Gurobi/CPLEX for exact solutions on small instances

## Implementation Notes

- Use Qiskit, Cirq, or PennyLane for circuit construction
- Start with simulator before hardware
- For real hardware: use error mitigation
- Track approximation ratio: C(θ)/C_opt
