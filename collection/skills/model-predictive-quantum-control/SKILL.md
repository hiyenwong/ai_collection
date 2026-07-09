---
name: model-predictive-quantum-control
category: quantum
description: Model Predictive Control (MPC) methodology applied to quantum state preparation and quantum system control. Combines system identification with receding-horizon optimization for robust quantum operations under noise and uncertainty.
activation: model predictive control, MPC quantum, quantum state preparation, receding horizon control, quantum feedback, quantum system identification
---

# Model Predictive Control for Quantum Systems

## Overview

Model Predictive Control (MPC) is a powerful control framework that solves an optimal control problem at each time step over a finite prediction horizon, then applies only the first control action. Applied to quantum systems, MPC provides robust state preparation and gate operations that are resilient to noise, parameter uncertainty, and model mismatch.

## Core Methodology

### Quantum MPC Formulation
1. **System Model**: ẋ = -i[H(u)]x + noise (Schrödinger/Lindblad dynamics)
2. **Cost Function**: J = Σ ||x(t) - x_target||² + λ||u(t)||² over horizon N
3. **Constraints**: |u(t)| ≤ u_max (control amplitude limits)
4. **Receding Horizon**: Solve optimization, apply u(0), repeat

### Key Advantages Over Traditional Methods
- **Constraint handling**: Natural incorporation of control bounds
- **Robustness**: Feedback corrects for model mismatch and noise
- **Multi-objective**: Simultaneously optimize fidelity, energy, time
- **Adaptivity**: Online re-planning handles drift and disturbances

## Implementation Steps

### Step 1: Quantum System Identification
```python
def identify_quantum_model(data):
    """Learn quantum dynamics from experimental data"""
    # Use data-driven methods to learn H(u) and noise model
    # Options: subspace identification, Koopman operator, neural ODE
    pass
```

### Step 2: MPC Optimization
```python
def quantum_mpc_step(state, target, horizon, model):
    """Single MPC step for quantum control"""
    # Solve: min Σ ||x_k - x_target||² + λ||u_k||²
    # s.t. x_{k+1} = Φ(u_k) x_k, |u_k| ≤ u_max
    # Use gradient-based or direct transcription methods
    pass
```

### Step 3: Robust MPC Extensions
- **Tube MPC**: Pre-compute invariant tubes for disturbance rejection
- **Stochastic MPC**: Account for measurement noise in optimization
- **Learning MPC**: Update model online from measurement data

## Applications

1. **Quantum State Preparation**: High-fidelity preparation of target states
2. **Quantum Gate Calibration**: Robust gate design under parameter drift
3. **Error Correction**: Real-time feedback for quantum error correction
4. **Quantum Sensing**: Optimal control for enhanced sensitivity

## Pitfalls

- **Computational cost**: Real-time optimization requires fast solvers
- **Model accuracy**: Poor models lead to suboptimal or unstable control
- **Measurement backaction**: Quantum measurements disturb the state
- **Horizon selection**: Too short → myopic; too long → computationally expensive

## Research Frontiers (2026)

- MPC for multi-qubit systems with entanglement constraints
- MPC combined with quantum machine learning for model learning
- Distributed MPC for quantum network control
- MPC with formal safety guarantees for quantum operations

## References

- arXiv:2506.19200 - Model Predictive Control for Quantum State Preparation
- arXiv:2507.00316 - Optimal Control of Quantum Systems Using Reinforcement Learning
- arXiv:2506.15400 - Robust Quantum Control under Parameter Uncertainty