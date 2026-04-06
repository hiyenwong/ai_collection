# QAOA for Portfolio Optimization

Quantum Approximate Optimization Algorithm (QAOA) for financial portfolio problems.

## Algorithm Overview

QAOA is a hybrid quantum-classical algorithm designed for combinatorial optimization:
- Created by Farhi et al. (2014)
- Uses parameterized quantum circuits
- Alternates between cost and mixer Hamiltonians
- Parameters optimized classically

## Portfolio Formulation

### Mean-Variance Optimization
```
Objective: minimize w'Σw - λμ'w
Constraints: Σw_i = 1, w_i ≥ 0
```

### Higher-Order Moments (Quantum Advantage)
```
Objective: minimize Var + γ₁Skew + γ₂Kurtosis
```
Higher-order moments require complex classical computation, making quantum approach attractive.

## Implementation Steps

### Step 1: Encode Problem as Hamiltonian
```python
from qiskit import QuantumCircuit
from qiskit.algorithms import QAOA
from qiskit_optimization import QuadraticProgram

# Define portfolio problem
qp = QuadraticProgram()
qp.binary_var_list(30)  # 30 assets
qp.minimize(linear=[-mu_i], quadratic=[Sigma_ij])
```

### Step 2: Create QAOA Instance
```python
from qiskit.algorithms.optimizers import COBYLA

qaoa = QAOA(
    optimizer=COBYLA(maxiter=100),
    reps=3,  # QAOA depth
    quantum_instance=backend
)
```

### Step 3: Run Optimization
```python
result = qaoa.solve(qp)
optimal_portfolio = result.x
```

## Resource Estimates

| Portfolio Size | Qubits | Circuit Depth | Expected Quality |
|----------------|--------|---------------|------------------|
| 10 assets | 10-20 | ~100 | Good |
| 30 assets | 30-60 | ~500 | Moderate |
| 50 assets | 50-100 | ~1000 | Requires error correction |

## Limitations

1. **Qubit requirements**: Linear in number of assets
2. **Circuit depth**: Grows with problem complexity
3. **Convergence**: Not guaranteed to find global optimum
4. **NISQ constraints**: Noise limits effective depth

## Best Practices

1. Start with small portfolios (10-20 assets)
2. Use warm-start from classical optimizer
3. Increase QAOA depth gradually
4. Validate results against classical methods

## References

- Farhi, Goldstone, Gutmann (2014) - Original QAOA paper
- arxiv:2509.01496 - Higher-Order Portfolio Optimization with QAOA
- Qiskit Optimization Module documentation