---
name: quantum-proper-scoring-rules
description: >
  Apply proper scoring rules to quantum state estimation and forecasting. Generalize classical
  proper scoring rules to density operators using operator convex generators and Quantum Fisher Information.
  Derive minimax optimal bounds for quantum state tomography. Quantify economic value of quantum resources
  in forecasting tasks. Use when performing quantum state estimation, designing quantum scoring mechanisms,
  analyzing quantum forecasting, or applying information geometry to quantum systems. arXiv: 2605.05268
---

# Quantum Proper Scoring Rules

Generalize proper scoring rules from classical probability to quantum density operators.
Connect quantum estimation theory, resource theory, and economic forecasting.

## Core Framework

### Classical → Quantum Generalization

| Classical | Quantum |
|-----------|---------|
| Probability distribution p | Density operator ρ |
| Proper scoring rule S(p, q) | Quantum scoring rule S(ρ, σ) |
| Value function G(p) | Quantum Value Functional G(ρ) |
| Fisher Information I(p) | Quantum Fisher Information J(ρ) |
| Cramér-Rao bound | Quantum Cramér-Rao-McCarthy bound |

### Quantum Value Functionals

Defined via **operator convex generators** g:

```
G(ρ) = Tr[g(ρ)]
```

The proper scoring rule is the Bregman divergence induced by G:

```
S(ρ, σ) = G(σ) + Tr[∇G(σ)(ρ - σ)] - G(ρ)
```

where ∇G is the Fréchet derivative of G with respect to the operator argument.

## Key Results

### 1. Complete Duality Theory

There is a one-to-one correspondence between:
- **Operator convex functions** g
- **Quantum Value Functionals** G
- **Proper quantum scoring rules** S

### 2. Quantum Cramér-Rao-McCarthy Bound

For quantum state tomography under McCarthy-type incentives:

```
Minimax Risk ≥ 1 / (n · J(ρ))
```

where:
- n = number of measurements
- J(ρ) = Quantum Fisher Information
- The bound links minimax risk to the **curvature** of the generating function

### 3. Resource-Theoretic Advantages

Quantum resources (entanglement, coherence) provide economic value in forecasting:

```
Value(quantum forecast) - Value(classical forecast) = f(Quantum Fisher Information gap)
```

The advantage is quantified by the ratio of quantum to classical Fisher information.

## Common Quantum Scoring Rules

### Logarithmic Scoring Rule

```
S_log(ρ, σ) = -Tr[ρ log σ]
```

Generator: g(x) = x log x (von Neumann entropy)

### Quadratic (Brier) Scoring Rule

```
S_quad(ρ, σ) = Tr[(ρ - σ)²]
```

Generator: g(x) = x²

### Spherical Scoring Rule

```
S_sph(ρ, σ) = 1 - Tr[ρσ] / √(Tr[ρ²] · Tr[σ²])
```

## Implementation

### Quantum State Estimation

```python
import numpy as np
from scipy.linalg import logm

def quantum_log_score(rho_true, rho_est):
    """Compute quantum logarithmic scoring rule."""
    # S(ρ, σ) = -Tr[ρ log σ]
    log_sigma = logm(rho_est)
    return -np.real(np.trace(rho_true @ log_sigma))

def quantum_brier_score(rho_true, rho_est):
    """Compute quantum quadratic (Brier) scoring rule."""
    diff = rho_true - rho_est
    return np.real(np.trace(diff @ diff))

def quantum_fisher_info(rho, generators):
    """Compute Quantum Fisher Information for parametric family."""
    # Symmetric logarithmic derivative (SLD) approach
    # J_ij = Tr[ρ {L_i, L_j}] / 2
    # where ∂ρ/∂θ_i = (ρ L_i + L_i ρ) / 2
    n_params = len(generators)
    j_matrix = np.zeros((n_params, n_params))
    for i in range(n_params):
        for j in range(n_params):
            # Solve SLD equation numerically
            L_i = solve_sld(rho, generators[i])
            L_j = solve_sld(rho, generators[j])
            j_matrix[i, j] = np.real(np.trace(rho @ (L_i @ L_j + L_j @ L_i))) / 2
    return j_matrix
```

### Minimax Optimal Estimation

```python
def minimax_quantum_tomography(measurements, n_shots):
    """Perform minimax-optimal quantum state tomography."""
    # Under McCarthy-type incentives, the optimal estimator
    # minimizes the worst-case expected score
    
    # 1. Compute empirical density matrix
    rho_emp = empirical_state(measurements, n_shots)
    
    # 2. Project onto physical state space (positive, unit trace)
    rho_est = project_to_physical(rho_emp)
    
    # 3. Compute confidence via Quantum Fisher Information
    j_matrix = quantum_fisher_info(rho_est, measurement_operators)
    covariance = np.linalg.inv(j_matrix) / n_shots
    
    return rho_est, covariance
```

## Economic Interpretation

### Forecasting Markets

In quantum forecasting markets:

1. **Agents report** quantum states (density matrices)
2. **Scoring rules** incentivize honest reporting (properness)
3. **Market maker** aggregates reports using quantum Bregman divergences
4. **Resource value** = additional payoff from quantum vs classical forecasting

### Resource Valuation

The economic value of a quantum resource R:

```
V(R) = E[S(ρ_quantum, σ)] - E[S(ρ_classical, σ)]
```

This connects quantum resource theory to mechanism design and information economics.

## Applications

1. **Quantum state tomography**: Optimal estimation with guaranteed incentives
2. **Quantum benchmarking**: Score quantum devices against classical baselines
3. **Quantum machine learning**: Loss functions for quantum neural networks
4. **Quantum economics**: Pricing quantum computational resources
5. **Quantum cryptography**: Verification of quantum states in protocols

## Connection to Information Geometry

The quantum Fisher information defines a Riemannian metric on the space of density operators:

```
ds² = Tr[dρ · J(ρ)^{-1} · dρ]
```

This is the quantum analog of the Fisher-Rao metric, and the scoring rules are
Bregman divergences compatible with this geometry.

## Activation Keywords

- quantum proper scoring rules
- quantum state estimation scoring
- quantum Fisher information
- quantum state tomography minimax
- quantum forecasting
- quantum Bregman divergence
- operator convex quantum
- quantum Cramer-Rao bound
- quantum resource valuation
- 量子评分规则
- 量子费雪信息
- 量子态估计

## Related Skills

- `quantum-magic-state-analysis`: Quantum resource theory and computational advantage
- `quantum-ml-patterns`: Quantum machine learning with proper loss functions
- `quantum-statistical-estimation`: Quantum parameter estimation theory
