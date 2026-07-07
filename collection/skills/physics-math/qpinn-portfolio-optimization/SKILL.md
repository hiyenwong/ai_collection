---
name: qpinn-portfolio-optimization
description: "Quantum Physics-Informed Neural Networks (QPINN) for portfolio optimization PDEs — uses parameterized quantum circuits with tensor rank decomposition to solve financial PDEs with 80x fewer parameters and higher accuracy than classical PINNs. Use when: solving financial PDEs for portfolio optimization, Merton problem, quantum-inspired PINNs, tensor rank decomposition for quantum circuits, parameter-efficient quantum PDE solvers."
---

# QPINN Portfolio Optimization

## Core Methodology

Quantum Physics-Informed Neural Networks (QPINN) for solving financial PDEs in portfolio optimization. Uses parameterized quantum circuits (PQC) implementing polynomial approximations via tensor rank decomposition, reducing quantum resource complexity from exponential to polynomial when tensor rank is moderate.

## Key Innovation

- **Tensor Rank Decomposition**: Parameterized quantum circuit implements polynomials based on tensor rank decomposition, reducing complexity from O(2^n) to O(poly(n)) when tensor rank is moderate
- **80x fewer parameters** than classical fully connected PINN while achieving higher accuracy on Merton portfolio optimization PDE
- **Two model variants**: QPINN (quantum circuit-based) and Quantum-inspired PINN (classical simulation with same structure)
- Both guarantee existence of PDE solution approximation as polynomial incorporating tensor rank decomposition

## Mathematical Framework

### Merton Portfolio Optimization PDE

The HJB equation for optimal fraction between risky and risk-free assets:

```
∂V/∂t + max_π [ (μ- r)π ∂V/∂x + ½σ²π² ∂²V/∂x² + rx ∂V/∂x ] = 0
```

### QPINN Architecture

1. **Quantum Feature Map**: Encode input (time t, wealth x) into quantum state via parameterized gates
2. **Tensor Rank Polynomial**: PQC implements polynomial ansatz via tensor rank decomposition
3. **Physics-Informed Loss**: PDE residual + boundary/initial conditions
4. **Training**: Gradient-based optimization of circuit parameters

### Tensor Rank Decomposition Circuit

For a function f(x) approximated as polynomial:
- Decompose coefficient tensor via tensor train (TT) decomposition
- Each TT-core corresponds to a layer of parameterized quantum gates
- Circuit depth scales linearly with tensor train rank, not exponentially with input dimension

## When to Use

- Solving HJB/Bellman PDEs for continuous-time portfolio optimization
- Resource-constrained quantum/hybrid settings where classical PINNs are too large
- Problems with moderate tensor rank structure (financial PDEs often have this)
- Needing provable approximation guarantees for PDE solutions

## Implementation Steps

1. Formulate the financial PDE (e.g., Merton HJB)
2. Choose polynomial ansatz with appropriate degree
3. Apply tensor train decomposition to coefficient tensor
4. Map TT-cores to parameterized quantum circuit layers
5. Construct physics-informed loss: PDE residual + IC/BC penalties
6. Train circuit parameters via gradient descent (or quantum-inspired classical simulation)
7. Validate against known analytical solutions

## Error Handling

- **High tensor rank**: If tensor rank is large, TT approximation error increases — increase bond dimension or switch to classical PINN
- **PDE stiffness**: Stiff PDEs may need adaptive collocation point sampling near boundaries
- **Quantum noise**: On real hardware, use error mitigation (zero-noise extrapolation, readout correction)

## Source

arXiv: 2604.03346 — "Learning PDEs for Portfolio Optimization with Quantum Physics-Informed Neural Networks" by Letao Wang, Abdel Lisser, Sreejith Sreekumar, Zeno Toffano

**Activation**: qpinn portfolio optimization, quantum PINN, quantum PDE solver, Merton portfolio quantum, tensor rank quantum circuit, quantum physics informed neural network
