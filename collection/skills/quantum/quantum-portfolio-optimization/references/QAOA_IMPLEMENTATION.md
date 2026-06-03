# QAOA Implementation Guide

## Overview

Quantum Approximate Optimization Algorithm (QAOA) for portfolio optimization.

## Algorithm Structure

### Hamiltonian Encoding

Portfolio optimization Hamiltonian:

```
H_C = Σ_i w_i·r_i - λ·Σ_i w_i²·σ_i² + γ·Σ_i w_i³·s_i - δ·Σ_i w_i⁴·k_i
```

Where:
- w_i: weight of asset i
- r_i: expected return
- σ_i²: variance
- s_i: skewness
- k_i: kurtosis

### QAOA Circuit

```
|ψ(p,β,γ)⟩ = U_X(β_p)·U_C(γ_p)·...·U_X(β_1)·U_C(γ_1)|+⟩^n
```

Where:
- U_C(γ) = e^(-iγH_C): Cost Hamiltonian
- U_X(β) = e^(-iβΣX_i): Mixer Hamiltonian
- p: number of layers
- β, γ: variational parameters

## Python Implementation (Qiskit)

```python
from qiskit import QuantumCircuit
from qiskit.circuit import Parameter
from qiskit.algorithms import QAOA
from qiskit.algorithms.optimizers import COBYLA

def portfolio_qaoa(
    returns: np.ndarray,
    cov_matrix: np.ndarray,
    skewness: np.ndarray = None,
    kurtosis: np.ndarray = None,
    risk_weight: float = 0.5,
    skew_weight: float = 0.1,
    kurt_weight: float = 0.05,
    p: int = 3
):
    """
    QAOA portfolio optimization with higher-order moments.
    
    Args:
        returns: Expected returns (n_assets)
        cov_matrix: Covariance matrix (n_assets x n_assets)
        skewness: Skewness (n_assets), optional
        kurtosis: Kurtosis (n_assets), optional
        risk_weight: Risk penalty λ
        skew_weight: Skewness reward γ
        kurt_weight: Kurtosis penalty δ
        p: QAOA layers
    
    Returns:
        Optimal portfolio weights
    """
    
    n_assets = len(returns)
    
    # Encode as Hamiltonian (Ising model)
    # w_i = (1 + z_i)/2, where z_i ∈ {-1, 1}
    
    # Build cost Hamiltonian coefficients
    J = {}  # Two-qubit terms
    h = {}  # Single-qubit terms
    
    # Return terms: Σ_i r_i·w_i → Σ_i r_i·(1+z_i)/2
    for i in range(n_assets):
        h[i] = returns[i] / 2
    
    # Risk terms: Σ_ij w_i·w_j·σ_ij
    for i in range(n_assets):
        for j in range(i+1, n_assets):
            J[(i, j)] = -risk_weight * cov_matrix[i, j] / 4
    
    # Skewness terms (if provided)
    if skewness is not None:
        for i in range(n_assets):
            h[i] += skew_weight * skewness[i] / 8
    
    # Kurtosis terms (if provided)
    if kurtosis is not None:
        for i in range(n_assets):
            h[i] -= kurt_weight * kurtosis[i] / 16
    
    # Build QAOA circuit
    qaoa = QAOA(
        optimizer=COBYLA(maxiter=100),
        quantum_instance=quantum_instance,
        reps=p
    )
    
    # Construct operator
    from qiskit.opflow import PauliSumOp
    operator = PauliSumOp.from_dict(J, h)
    
    # Run optimization
    result = qaoa.compute_minimum_eigenvalue(operator)
    
    # Decode solution
    optimal_state = result.eigenstate
    weights = decode_weights(optimal_state, n_assets)
    
    return weights

def decode_weights(state: dict, n_assets: int) -> np.ndarray:
    """Decode quantum state to portfolio weights."""
    
    # Find most probable bitstring
    max_prob_state = max(state.items(), key=lambda x: x[1])
    bitstring = max_prob_state[0]
    
    # Convert {0,1} to {-1,1} then to weights
    z = [int(b) for b in bitstring]
    weights = [(1 + zi) / 2 for zi in z]
    
    # Normalize to sum to 1
    weights = np.array(weights) / sum(weights)
    
    return weights
```

## Parameter Optimization

### Classical Outer Loop

```python
from scipy.optimize import minimize

def optimize_qaoa_parameters(
    hamiltonian,
    p: int,
    backend='qasm_simulator'
):
    """
    Optimize QAOA parameters β, γ via classical optimizer.
    """
    
    def objective(params):
        beta = params[:p]
        gamma = params[p:]
        
        # Execute QAOA circuit
        expectation = execute_qaoa(hamiltonian, beta, gamma, backend)
        
        return expectation
    
    # Initial parameters
    init_params = np.random.uniform(0, 2*np.pi, 2*p)
    
    # Optimize
    result = minimize(
        objective,
        init_params,
        method='COBYLA',
        options={'maxiter': 200}
    )
    
    return result.x
```

## Constraints Handling

### Budget Constraint (Σw_i = 1)

Add penalty term:
```
H_budget = μ·(Σw_i - 1)²
```

### Cardinality Constraint (max K assets)

Use penalty:
```
H_cardinality = ν·Σw_i + λ·Σw_i²
```

Approximates cardinality via continuous relaxation.

## Performance Tips

1. **Layer count p**: Start with p=3, increase gradually
2. **Optimization**: Use gradient-free methods (COBYLA, SPSA)
3. **Warm start**: Initialize β, γ from previous runs
4. **Symmetry breaking**: Add small random perturbation
5. **Hybrid**: Use classical optimizer for outer loop

## References

- Farhi et al. (2014): Original QAOA paper
- Baker et al. (2019): QAOA for portfolio optimization
- Herman et al. (2023): Higher-order moments with QAOA