---
name: quantum-bayesian-state-estimation
description: >
  Gate-based quantum algorithms for Bayesian state estimation using Fokker-Planck
  equation on discretized state spaces. Encodes probability density in quantum
  amplitudes, uses quantum Fourier transforms and Wick rotation for unitary
  propagation. Enables exponential state space scaling for high-dimensional
  filtering. Use when: quantum Bayesian estimation, Fokker-Planck quantum
  algorithm, quantum state prediction, quantum filtering, Bayesian transport
  dynamics, Wick rotation diffusion, quantum Fourier state estimation.
  Source: arXiv:2604.24161
---

# Quantum Bayesian State Estimation

## Description

Implements gate-based quantum algorithms for the prediction step of Bayesian
state estimation based on the Fokker-Planck equation on discretized
position-velocity state spaces. Probability density is encoded in quantum state
amplitudes, enabling compact representation of high-dimensional distributions.

## Core Methodology

### Step 1: Encode Probability in Quantum Amplitudes

Represent probability density p(x,v) as quantum state amplitudes:
```
|ψ⟩ = Σ_{x,v} √p(x,v) |x⟩|v⟩
```
This enables exponential compression — n qubits represent 2^n states.

### Step 2: Drift Component (Exact in Amplitude Space)

The drift term of the Fokker-Planck equation can be implemented exactly
using quantum Fourier transforms:

```python
# Quantum circuit steps:
# 1. QFT on position register
# 2. Phase rotation by drift coefficient
# 3. Inverse QFT
def drift_step(qc, position_qubits, drift_coefficient):
    qc.qft(position_qubits)
    for i, q in enumerate(position_qubits):
        qc.p(drift_coefficient * 2**i, q)
    qc.qft_dg(position_qubits)
```

### Step 3: Diffusion via Wick Rotation

The diffusion term does NOT admit a linear representation in amplitude space
(nonlinear relation between probability density and wave function). Solution:

**Wick rotation approach**: Transform diffusion into dispersive phase evolution
```
∂p/∂t = D ∇²p  →  ∂ψ/∂t = iD ∇²ψ
```

This yields a fully unitary propagation implementable on gate-based quantum
computers.

### Step 4: Full Quantum Propagation

```python
def quantum_fokker_planck(qc, pos_qubits, vel_qubits,
                          drift_coeff, diffusion_coeff, dt):
    # Drift step (exact)
    drift_step(qc, pos_qubits, drift_coeff * dt)
    drift_step(qc, vel_qubits, drift_coeff * dt)

    # Diffusion step (Wick rotated)
    qc.qft(pos_qubits)
    qc.qft(vel_qubits)
    # Phase evolution for diffusion
    for i, qi in enumerate(pos_qubits):
        for j, qj in enumerate(vel_qubits):
            qc.p(diffusion_coeff * dt * 2**(i+j), qi)
    qc.qft_dg(pos_qubits)
    qc.qft_dg(vel_qubits)
```

## Key Results

| Property | Classical | Quantum |
|----------|-----------|---------|
| State space | O(N) memory | O(log N) qubits |
| High-dimensional filtering | Tensor decompositions needed | Native exponential scaling |
| Drift implementation | Numerical integration | Exact in amplitude space |
| Diffusion implementation | Finite difference | Wick-rotated unitary |

## Implementation Notes

- The drift component reproduces classical transport dynamics accurately
- Diffusion requires Wick rotation — cannot be implemented directly as linear
  operator in amplitude space
- Numerical validation shows strong agreement with exact Fokker-Planck solution
- Suitable for high-dimensional filtering problems where classical methods
  require complex tensor decompositions

## Application Domains

- Bayesian state estimation
- Kalman filtering (quantum-enhanced)
- High-dimensional probability propagation
- Quantum-enhanced tracking systems
- Stochastic differential equations on quantum hardware

## References

- arXiv:2604.24161 — "Quantum Prediction of Transport Dynamics in Discretized
  State Spaces" (Felix Govaers, 2026)
- IEEE Transactions on Quantum Engineering (submitted April 2026)
