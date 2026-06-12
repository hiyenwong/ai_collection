---
name: adaptive-directional-gradient-qc
description: "Forward gradient estimation methodology for training parameterised quantum circuits (PQCs). Introduces QUIVER adaptive optimiser that recovers SPSA, random coordinate descent, and parameter-shift rule as limiting cases. Enables efficient training of 60-qubit quantum neural networks."
tags: ["quantum", "optimization", "machine-learning", "gradient-descent", "parameter-shift", "QUIVER"]
related_skills: ["quantum-neural-architecture", "qml-framework-agnostic-design"]
---

# Adaptive Directional Gradient Estimation for Parameterised Quantum Circuits

## Context

Training parameterised quantum circuits (PQCs) on quantum hardware is bottlenecked by the measurement cost of gradient estimation. Under the parameter-shift rule, gradient cost scales linearly with the number of trainable parameters, dominating the total shot budget at scale.

## Core Methodology

### 1. Forward Gradient Estimator Framework
Based on the forward mode of automatic differentiation, this framework yields an unbiased estimator of the gradient by averaging a freely tunable number of random directional derivatives.

### 2. Unified Gradient Framework
The framework recovers three existing methods as limiting cases:
- **SPSA** (Simultaneous Perturbation Stochastic Approximation) — single-direction extreme
- **Random coordinate descent** — intermediate case
- **Parameter-shift rule** — full-gradient extreme

All achieved with no ancilla qubits or controlled-gate overhead.

### 3. Convergence Proof
Stochastic quantum forward gradient descent converges under standard assumptions, with an explicit second-moment expansion that interpolates between the SPSA extreme and the parameter-shift extreme.

### 4. QUIVER Optimiser
**Q**uantum **I**terative **V**-adapt**e**r **R**ule:
- Adaptive optimiser for parameterised circuits
- Update rule derived from closed-form minimum measurement-cost allocation
- Outperforms iCANS and gCANS measurement-frugal optimisers on QAOA and VQE problems

### 5. Practical Results
- Trains Hamming-weight-preserving orthogonal quantum neural networks
- Up to 60 qubits and 1770 parameters
- Tested on ECG5000 and MNIST datasets
- Orders of magnitude more efficient than parameter-shift rule

## Implementation Steps

1. Implement forward gradient estimator for your PQC
2. Configure number of random directional derivatives (tunable parameter)
3. Use QUIVER update rule for minimum measurement-cost allocation
4. For small parameter counts: approach parameter-shift rule for precision
5. For large parameter counts: approach SPSA-like behaviour for efficiency

## Pitfalls

- **Parameter-shift overhead**: Linear scaling in number of parameters makes it infeasible for large circuits (>100 parameters)
- **SPSA noise**: Single-direction SPSA has high variance; use intermediate number of directions for best trade-off
- **No ancilla advantage**: The method works without ancilla qubits or controlled gates — simpler hardware requirements but may miss opportunities where ancillae are available
- **Convergence assumptions**: Standard convergence proofs assume bounded gradients and appropriate learning rate schedules

## Verification

1. Implement forward gradient estimator on a small PQC (2-4 qubits)
2. Compare gradient estimates against parameter-shift rule (ground truth)
3. Verify convergence on MNIST/ECG5000 benchmarks
4. Measure shot efficiency vs iCANS/gCANS baselines

## Activation

quantum gradient estimation, parameter-shift rule, SPSA, QUIVER, forward gradient, quantum neural network training, variational quantum circuits, PQC optimization, measurement-efficient training, arxiv:2606.09734
