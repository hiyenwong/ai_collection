---
name: cd-qaoa-portfolio-optimization
description: "Counterdiabatic QAOA (CD-QAOA) methodology for constrained portfolio optimization. Incorporates approximate adiabatic gauge potentials via nested commutators of the portfolio Hamiltonian and XY mixer for improved convergence, solution quality, and constraint satisfaction on NISQ devices. Trigger: quantum portfolio optimization, counterdiabatic QAOA, CD-QAOA, constrained quantum optimization, financial quantum computing, quantum trading."
---

# Counterdiabatic QAOA for Portfolio Optimization

## Core Idea

Standard QAOA for portfolio optimization suffers from slow convergence and poor constraint satisfaction. CD-QAOA augments the variational ansatz with approximate adiabatic gauge potentials (AGPs) generated from nested commutators of:
1. The Ising-type portfolio problem Hamiltonian (cost function)
2. The Hamming weight-preserving XY mixer Hamiltonian

This counterdiabatic term suppresses non-adiabatic transitions, enabling faster convergence to optimal portfolio weights under realistic budget/risk constraints.

## Key Technique: AGP Construction

```
AGP ≈ Σ_k α_k [H_problem, [H_problem, ...[H_problem, H_mixer]...]]
       (k nested commutators)
```

For portfolio optimization:
- **H_problem**: Ising encoding of Markowitz mean-variance + cardinality constraints
- **H_mixer**: XY mixer that preserves Hamming weight (fixed number of assets)
- **CD term**: Added to QAOA mixing layer as additional rotation gates

## Implementation Pattern

### Step 1: Encode Portfolio as QUBO

```python
# Minimize: w^T Σ w - μ w^T μ_return + λ (w^T 1 - K)^2
# Where K = cardinality constraint (number of assets)
```

### Step 2: Map QUBO to Ising

```python
# Binary x_i → (1 - Z_i)/2 for qubit Pauli-Z operators
# Portfolio weights → qubit states
```

### Step 3: Build CD-QAOA Ansatz

```python
# Standard QAOA layers:
#   U_C(γ) = exp(-iγ H_problem)
#   U_B(β) = exp(-iβ H_mixer)
#
# CD-QAOA adds:
#   U_CD(α) = exp(-iα AGP)
#   where AGP = [H_problem, H_mixer] (first-order)
#              or higher-order nested commutators
```

### Step 4: Variational Optimization

```python
# Optimize parameters {γ, β, α} jointly
# CD parameters α reduce required circuit depth p
# Achieves same quality with fewer layers than standard QAOA
```

## Advantages over Standard QAOA

| Metric | QAOA | CD-QAOA |
|--------|------|---------|
| Convergence speed | Slow | 2-3x faster |
| Constraint satisfaction | Often violated | Better maintained |
| Required circuit depth | High p needed | Lower p sufficient |
| NISQ feasibility | Limited | Improved |

## Activation Keywords

- cd-qaoa
- counterdiabatic qaoa
- quantum portfolio optimization
- constrained quantum optimization
- adiabatic gauge potential
- XY mixer
- quantum trading optimization

## Related Skills

- quantum-portfolio-optimizer
- quantum-optimization-qaoa
- quantum-finance
