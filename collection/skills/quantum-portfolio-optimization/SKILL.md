---
name: quantum-portfolio-optimization
description: "Quantum Approximate Optimization Algorithm (QAOA) with counterdiabatic driving for portfolio optimization. Applies quantum computing to financial portfolio selection with budget and risk constraints. Activation: quantum portfolio, QAOA finance, quantum optimization trading, 量子投资组合, counterdiabatic QAOA."
---

# Quantum Portfolio Optimization (CCD-QAOA)

## Description

Implements Constrained Counterdiabatic Quantum Approximate Optimization Algorithm (CCD-QAOA) for portfolio optimization. Combines quantum approximate optimization with counterdiabatic driving to achieve better approximation ratios under realistic budget and risk constraints. Based on the methodology from arXiv:2605.06858.

## Activation Keywords

- quantum portfolio optimization
- QAOA portfolio
- counterdiabatic QAOA
- quantum finance optimization
- quantum trading algorithm
- 量子投资组合优化
- quantum constrained optimization
- XY-mixer portfolio
- adiabatic gauge potential

## Core Methodology

### Problem Formulation

Portfolio optimization maps to an Ising-type Hamiltonian:

```
H_portfolio = -\sum_i \mu_i z_i + \lambda \sum_{i,j} \Sigma_{ij} z_i z_j
```

Where:
- `z_i \in {0,1}`: binary decision (include asset i or not)
- `\mu_i`: expected return of asset i
- `\Sigma_{ij}`: covariance matrix
- `\lambda`: risk aversion parameter

### Constraints

**Budget constraint (cardinality)**: Select exactly K assets from N
```
\sum_i z_i = K
```

**Risk constraints**: Maximum allowable portfolio variance
```
z^T \Sigma z \leq \sigma_{max}^2
```

### CCD-QAOA Algorithm

#### Standard QAOA Ansatz

```
|\gamma, \beta\rangle = \prod_{p=1}^{P} e^{-i\beta_p H_M} e^{-i\gamma_p H_C} |+\rangle^{\otimes n}
```

Where:
- `H_C`: Cost Hamiltonian (portfolio objective)
- `H_M`: Mixer Hamiltonian (enables exploration)

#### Counterdiabatic Extension

Add counterdiabatic terms to the ansatz:

```
|\gamma, \beta, \alpha\rangle = \prod_{p=1}^{P} e^{-i\alpha_p H_{CD}} e^{-i\beta_p H_M} e^{-i\gamma_p H_C} |+\rangle^{\otimes n}
```

Where `H_{CD}` is the approximate adiabatic gauge potential:

```
H_{CD} \approx \sum_k c_k [H_C, [H_C, ...[H_C, H_M]...]]
```

(nested commutators)

#### XY-Mixer for Constraints

Use XY-mixer to preserve Hamming weight (budget constraint):

```
H_{XY} = \sum_{i<j} (X_i X_j + Y_i Y_j)
```

This mixer preserves `\sum_i z_i` = constant, naturally enforcing the budget constraint.

### Algorithm Steps

1. **Initialize**: Map portfolio problem to Ising Hamiltonian
2. **Choose mixer**: Select XY-mixer for budget constraint or Grover-mixer for unconstrained
3. **Compute gauge potentials**: Calculate nested commutators [H_C, H_M], [H_C, [H_C, H_M]], etc.
4. **Build ansatz**: Layer CD terms with standard QAOA layers
5. **Optimize parameters**: Use classical optimizer (COBYLA, SPSA, gradient-based) to minimize \langle H_C \rangle
6. **Sample solutions**: Measure quantum state to get candidate portfolios
7. **Post-process**: Select best portfolio from samples, verify constraints

### Implementation (Python/Qiskit)

```python
from qiskit import QuantumCircuit, transpile
from qiskit_algorithms import QAOA, SamplingVQE
from qiskit_algorithms.optimizers import COBYLA, SPSA
from qiskit.primitives import Sampler
from qiskit.circuit.library import TwoLocal
import numpy as np
from scipy.optimize import minimize

def build_portfolio_hamiltonian(returns, covariance, risk_lambda):
    """Build portfolio cost Hamiltonian from financial data."""
    n = len(returns)
    # H_C = -\sum \mu_i Z_i + \lambda \sum \Sigma_{ij} Z_i Z_j
    hamiltonian = {}
    for i in range(n):
        # Linear term (returns)
        hamiltonian[tuple([i])] = -returns[i]
        for j in range(i, n):
            # Quadratic term (risk)
            coeff = risk_lambda * covariance[i, j]
            if i == j:
                hamiltonian[tuple([i])] = hamiltonian.get(tuple([i]), 0) + coeff
            else:
                hamiltonian[tuple(sorted([i, j]))] = coeff
    return hamiltonian

def xy_mixer_circuit(n_assets, budget_k, gamma, beta, alpha):
    """Build QAOA circuit with XY-mixer and counterdiabatic terms."""
    qc = QuantumCircuit(n_assets)
    
    # Initialize in equal superposition (with budget constraint via state prep)
    # For XY-mixer: start with exactly k qubits in |1\rangle
    for i in range(budget_k):
        qc.x(i)
    qc.h(range(budget_k, n_assets))  # Simplified initialization
    
    p = len(gamma)  # QAOA depth
    for layer in range(p):
        # Cost Hamiltonian layer
        # e^{-i\gamma_p H_C}
        for i in range(n_assets):
            qc.rz(2 * gamma[layer], i)
        # Two-qubit cost terms would go here
        
        # XY-Mixer layer
        # e^{-i\beta_p H_{XY}}
        for i in range(n_assets):
            for j in range(i+1, n_assets):
                # XY interaction: e^{-i\beta (X_i X_j + Y_i Y_j)}
                # Decomposed into standard gates
                qc.rxx(2 * beta[layer], i, j)
                qc.ryy(2 * beta[layer], i, j)
        
        # Counterdiabatic term (if using CCD-QAOA)
        if alpha is not None and len(alpha) > layer:
            # Approximate adiabatic gauge potential
            # Simplified: single-qubit CD terms
            for i in range(n_assets):
                qc.rx(2 * alpha[layer], i)
    
    return qc

def optimize_portfolio_qaoa(returns, covariance, risk_lambda, budget_k, 
                             n_layers=3, n_shots=1000, use_cd=True):
    """Full CCD-QAOA portfolio optimization pipeline."""
    n_assets = len(returns)
    
    # Build cost Hamiltonian
    H_C = build_portfolio_hamiltonian(returns, covariance, risk_lambda)
    
    # Parameter initialization
    gamma = np.random.uniform(0, 2*np.pi, n_layers)
    beta = np.random.uniform(0, 2*np.pi, n_layers)
    alpha = np.random.uniform(0, np.pi, n_layers) if use_cd else None
    
    # Objective function (expectation value of cost)
    def objective(params):
        if use_cd:
            g, b, a = params[:n_layers], params[n_layers:2*n_layers], params[2*n_layers:]
        else:
            g, b = params[:n_layers], params[n_layers:]
            a = None
        
        # Build circuit and sample
        qc = xy_mixer_circuit(n_assets, budget_k, g, b, a)
        
        # Calculate expectation value (simplified)
        # In practice, use quantum simulator or hardware
        return calculate_expectation(qc, H_C, n_shots)
    
    # Optimize
    if use_cd:
        x0 = np.concatenate([gamma, beta, alpha])
    else:
        x0 = np.concatenate([gamma, beta])
    
    result = minimize(objective, x0, method='COBYLA')
    
    # Extract best solution
    best_params = result.x
    if use_cd:
        best_gamma = best_params[:n_layers]
        best_beta = best_params[n_layers:2*n_layers]
        best_alpha = best_params[2*n_layers:]
    else:
        best_gamma = best_params[:n_layers]
        best_beta = best_params[n_layers:]
        best_alpha = None
    
    # Sample final portfolio
    final_circuit = xy_mixer_circuit(n_assets, budget_k, best_gamma, best_beta, best_alpha)
    portfolio = sample_portfolio(final_circuit, H_C, n_shots)
    
    return portfolio, result.fun, best_params

def compare_qaoa_variants(returns, covariance, risk_lambda, budget_k):
    """Compare CCD-QAOA vs standard QAOA variants."""
    results = {}
    
    # 1. Standard XY-mixer QAOA
    results['XY-QAOA'] = optimize_portfolio_qaoa(
        returns, covariance, risk_lambda, budget_k, use_cd=False
    )
    
    # 2. CCD-QAOA (with counterdiabatic)
    results['CCD-QAOA'] = optimize_portfolio_qaoa(
        returns, covariance, risk_lambda, budget_k, use_cd=True
    )
    
    # 3. Penalty-based QAOA
    results['Penalty-QAOA'] = optimize_penalty_qaoa(
        returns, covariance, risk_lambda, budget_k
    )
    
    return results
```

### Key Insights from Research

1. **Counterdiabatic Driving Improves Performance**: CCD-QAOA consistently outperforms standard QAOA at fixed depth by adding gauge potential terms that suppress transitions away from the adiabatic path.

2. **XY-Mixer Naturally Enforces Budget**: The XY-mixer preserves Hamming weight, naturally encoding cardinality constraints without penalty terms that distort the energy landscape.

3. **Nested Commutators Approximate Gauge Potentials**: The adiabatic gauge potential can be approximated using nested commutators [H_C, H_M], [H_C, [H_C, H_M]], etc., with higher-order terms providing better approximations.

4. **Penalty Methods Degrade Performance**: Standard penalty-based approaches increase problem size and distort energy landscapes, often degrading performance.

5. **Depth vs Quality Tradeoff**: For a fixed QAOA depth, CCD-QAOA achieves better approximation ratios than standard approaches.

## Usage Examples

### Example 1: Portfolio Optimization with Budget Constraint

```python
import numpy as np

# Portfolio data (5 assets)
returns = np.array([0.08, 0.12, 0.06, 0.15, 0.10])
covariance = np.array([
    [0.04, 0.006, 0.002, 0.008, 0.004],
    [0.006, 0.09, 0.003, 0.012, 0.005],
    [0.002, 0.003, 0.01, 0.004, 0.003],
    [0.008, 0.012, 0.004, 0.16, 0.006],
    [0.004, 0.005, 0.003, 0.006, 0.06]
])

# Select 3 assets from 5 with risk aversion \lambda=0.5
portfolio, cost, params = optimize_portfolio_qaoa(
    returns=returns,
    covariance=covariance,
    risk_lambda=0.5,
    budget_k=3,
    n_layers=4,
    use_cd=True
)

print(f"Selected assets: {portfolio}")
print(f"Portfolio cost: {cost}")
```

### Example 2: Comparing QAOA Variants

```python
# Compare different QAOA approaches
results = compare_qaoa_variants(returns, covariance, 0.5, 3)

for method, (portfolio, cost, _) in results.items():
    print(f"{method}: cost={cost:.4f}, portfolio={portfolio}")

# Expected: CCD-QAOA achieves lowest cost (best portfolio)
```

### Example 3: Risk-Constrained Portfolio Selection

```python
def optimize_with_risk_constraint(returns, covariance, risk_lambda, 
                                   budget_k, max_variance):
    """Optimize portfolio with both budget and risk constraints."""
    # Add risk constraint as additional penalty in Hamiltonian
    H_risk = \lambda_risk * (z^T \Sigma z - \sigma_{max}^2)^2
    
    # Combined Hamiltonian: H = H_portfolio + H_risk
    # Use CCD-QAOA with XY-mixer for combined constraints
    pass
```

## Error Handling

### QAOA Converges to Poor Local Minimum
- **Solution**: Run multiple initializations with different random seeds
- **Alternative**: Use gradient-free optimizers (SPSA, COBYLA) instead of gradient-based
- **Increase depth**: Try higher QAOA depth (more layers)

### Constraint Violation in Results
- **XY-Mixer**: Ensure XY-mixer is used for cardinality constraints
- **Penalty Strength**: Increase penalty weight for soft constraints
- **Post-filtering**: Filter sampled solutions to keep only feasible ones

### Quantum Simulator Limitations
- **Small portfolios**: Limit to ~20 assets for statevector simulation
- **Sampling noise**: Increase shots for better expectation estimates
- **Hardware noise**: Use error mitigation techniques (zero-noise extrapolation)

## Resources

- **Paper**: arXiv:2605.06858 - "Constrained Counterdiabatic Quantum Approximate Optimization Algorithm for Portfolio Optimization"
- **Qiskit Documentation**: https://qiskit.org/documentation/
- **QAOA Tutorial**: https://qiskit.org/learning/courses/foundations-of-quantum-optimization
- **PennyLane QAOA**: https://pennylane.ai/qml/demos/tutorial_qaoa_intro

## Related Skills

- **quantum-portfolio-optimizer**: Basic QAOA portfolio optimization
- **quantum-optimization-qaoa**: General QAOA methodology
- **quantum-finance-portfolio**: QUBO-based quantum finance
