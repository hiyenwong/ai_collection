---
name: cd-qaoa-portfolio
description: >
  Constrained Counterdiabatic QAOA (CCD-QAOA) methodology for portfolio optimization.
  Incorporates approximate adiabatic gauge potentials from nested commutators of the
  Ising-type portfolio Hamiltonian and Hamming weight-preserving XY mixer into variational ansatz.
  Achieves improved optimization under realistic budget and risk constraints.
  Use when: constrained portfolio optimization, QAOA enhancement, counterdiabatic quantum computing,
  quantum finance, variational quantum algorithms, budget constraints in quantum optimization.
---

# CD-QAOA Portfolio Optimization

Counterdiabatic extension of QAOA for constrained portfolio optimization using nested commutator gauge potentials.

## Core Methodology

### CCD-QAOA Algorithm

1. **Map portfolio problem to Ising Hamiltonian**: Encode asset selection weights and constraints into Ising-formulation
2. **Construct XY mixer**: Use Hamming weight-preserving XY mixer for budget constraint satisfaction
3. **Generate counterdiabatic terms**: Compute nested commutators [H_problem, H_mixer] and higher-order terms
4. **Variational ansatz**: Add counterdiabatic terms as additional parameterized gates
5. **Optimize parameters**: Classical optimizer minimizes energy expectation under risk constraints

### Key Insight

Counterdiabatic driving suppresses transitions away from instantaneous ground state during QAOA evolution, enabling faster convergence with fewer circuit layers.

### Nested Commutator Gauge Potentials

```
A_mu = sum_{k} alpha_k * [H_problem, H_mixer]^{(k)}
```

Where [·,·]^{(k)} denotes k-th order nested commutator.

## Implementation Workflow

### Step 1: QUBO Formulation

Convert portfolio optimization to QUBO:
```
min w^T @ Sigma @ w - mu * w^T @ r
subject to: sum(w_i) = B (budget), w_i in {0,1}
```

### Step 2: Ising Mapping

Map binary variables to Pauli-Z operators:
```
w_i = (1 - Z_i) / 2
H_problem = sum J_ij Z_i Z_j + sum h_i Z_i
```

### Step 3: Counterdiabatic Circuit Design

```python
from qiskit import QuantumCircuit
import numpy as np

def ccd_qaoa_layer(circuit, n_qubits, gamma, beta, alpha):
    # Standard QAOA terms
    circuit.rz(2 * gamma, target_qubits)  # Problem Hamiltonian
    circuit.rx(2 * beta, target_qubits)    # Mixer
    
    # Counterdiabatic terms from nested commutators
    for i in range(n_qubits):
        for j in range(i+1, n_qubits):
            circuit.rzz(2 * alpha, i, j)  # CD term
```

### Step 4: Classical Optimization Loop

```python
from scipy.optimize import minimize

def energy_expectation(params, circuit_template):
    gamma, beta, alpha = params
    # Run circuit, measure expectation
    return expectation_value

result = minimize(energy_expectation, x0, args=(circuit_template,))
```

## Parameter Selection

| Parameter | Range | Description |
|-----------|-------|-------------|
| gamma | [0, pi] | Problem Hamiltonian evolution time |
| beta | [0, pi/2] | Mixer Hamiltonian evolution time |
| alpha | [-1, 1] | Counterdiabatic strength |
| p_depth | 1-4 | Circuit depth (QAOA layers) |

## When to Use

- Portfolio optimization with hard budget constraints
- Quantum optimization where standard QAOA converges slowly
- NISQ devices where circuit depth must be minimized
- Combinatorial optimization with equality constraints

## References

- arXiv: 2605.06858 — Constrained Counterdiabatic QAOA for Portfolio Optimization
- Falla & Safro, 2026

## Related Skills

- quantum-portfolio-optimization
- qaoa-optimization
- quantum-finance
