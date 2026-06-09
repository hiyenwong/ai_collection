---
name: adaptive-directional-gradient-qc
description: Forward gradient estimation methodology for training parameterised quantum circuits (PQCs) efficiently. Based on arXiv:2606.09734 — forward-mode AD for quantum gradients, QUIVER adaptive optimiser with closed-form measurement-cost allocation.
version: 1.0
created: 2026-06-09
source: arXiv:2606.09734
category: quantum-machine-learning
tags:
  - quantum-computing
  - gradient-estimation
  - variational-quantum-circuits
  - optimisation
  - measurement-frugal
---

# Adaptive Directional Gradient Estimation for Quantum Circuits

## Background

Training parameterised quantum circuits (PQCs) on quantum hardware is bottlenecked by the measurement cost of gradient estimation. Under the standard parameter-shift rule, gradient cost scales linearly O(P) with the number of trainable parameters P, dominating the total shot budget at scale.

arXiv:2606.09734 introduces **forward gradient estimators** for PQCs based on the forward mode of automatic differentiation, yielding an unbiased gradient estimator by averaging random directional derivatives. This recovers SPSA, random coordinate descent, and parameter-shift as limiting cases — with **no ancilla qubits or controlled-gate overhead**.

## Core Methodology

### Forward Gradient Framework

The key insight: instead of computing all P partial derivatives independently (parameter-shift), estimate the gradient by:

1. **Sample random direction vectors** v ∈ ℝ^P from a chosen distribution
2. **Compute directional derivatives** ∇f(θ)·v using forward-mode AD
3. **Average K directional estimates** to recover the full gradient

The estimator interpolates between extremes:
- K=1, single random direction → equivalent to **SPSA** (Simultaneous Perturbation Stochastic Approximation)
- K=P, canonical basis directions → equivalent to **random coordinate descent**
- K=P², full basis coverage → recovers **parameter-shift rule** exactly

### QUIVER Optimiser (Quantum Iterative V-adaptive Estimator Rule)

QUIVER derives a **closed-form minimum measurement-cost allocation** for gradient estimation:

```
For parameter i with gradient estimate g_i and variance σ_i²:
  shots_i ∝ |g_i| / σ_i  (allocate more shots to high-signal, low-noise parameters)
```

This is computed iteratively — parameters with larger estimated gradients get more measurement budget, while noisy or near-zero-gradient parameters get fewer shots.

### Convergence Guarantee

Stochastic quantum forward gradient descent converges under standard assumptions, with an explicit second-moment expansion that characterizes the tradeoff between measurement cost and gradient accuracy.

## Implementation Steps

### Step 1: Forward Gradient Estimator

```python
import numpy as np
from typing import Callable, Tuple

def quantum_forward_gradient(
    cost_fn: Callable,
    theta: np.ndarray,
    k_samples: int = 10,
    direction_dist: str = "rademacher"
) -> np.ndarray:
    """Estimate gradient via forward-mode directional derivatives.
    
    Args:
        cost_fn: Quantum circuit cost function
        theta: Current parameters
        k_samples: Number of random directions to average
        direction_dist: 'rademacher' (±1) or 'gaussian'
    
    Returns:
        Gradient estimate (unbiased)
    """
    p = len(theta)
    grad_est = np.zeros(p)
    
    for _ in range(k_samples):
        # Sample random direction
        if direction_dist == "rademacher":
            v = np.random.choice([-1, 1], size=p)
        else:
            v = np.random.randn(p)
        
        # Forward-mode directional derivative
        # Evaluate cost at θ + εv and θ - εv
        eps = 1e-4
        f_plus = cost_fn(theta + eps * v)
        f_minus = cost_fn(theta - eps * v)
        directional_deriv = (f_plus - f_minus) / (2 * eps)
        
        # Unbiased gradient contribution
        grad_est += directional_deriv * v
    
    return grad_est / k_samples
```

### Step 2: QUIVER Adaptive Measurement Allocation

```python
def quiver_measurement_allocation(
    grad_est: np.ndarray,
    grad_variance: np.ndarray,
    total_shots: int
) -> np.ndarray:
    """QUIVER: closed-form optimal shot allocation per parameter.
    
    Args:
        grad_est: Current gradient estimates
        grad_variance: Variance estimates per parameter
        total_shots: Total measurement budget
    
    Returns:
        Shots to allocate per parameter
    """
    # Optimal allocation: proportional to |g_i| / σ_i
    signal_to_noise = np.abs(grad_est) / (np.sqrt(grad_variance) + 1e-10)
    weights = signal_to_noise / (signal_to_noise.sum() + 1e-10)
    shots_per_param = np.maximum(1, (weights * total_shots).astype(int))
    
    # Normalize to exact total
    shots_per_param = np.round(shots_per_param * total_shots / shots_per_param.sum()).astype(int)
    return shots_per_param
```

### Step 3: Integration with Quantum ML Frameworks

The forward gradient approach works with any PQC framework:
- **Qiskit**: Use `EstimatorPrimitives` with parameter binding
- **PennyLane**: Native forward-mode AD support via `jax` backend
- **Cirq**: Custom gradient circuits with directional parameter shifts

## Key Advantages

1. **No ancilla qubits required** — unlike some quantum gradient methods
2. **No controlled-gate overhead** — avoids doubling circuit depth
3. **Scales to 60+ qubits** — demonstrated on ECG5000 and MNIST
4. **Interpolates SPSA ↔ parameter-shift** — tunable accuracy/cost tradeoff
5. **Adaptive shot allocation** — QUIVER minimizes total measurements for target accuracy

## When to Use

- Training large PQC models (P > 100 parameters) where parameter-shift is prohibitive
- NISQ-era quantum ML with limited shot budgets
- QAOA and VQE optimisation where gradient accuracy vs. cost matters
- Any quantum neural network training where measurement efficiency is critical

## Activation Triggers

- "forward gradient", "directional derivative", "parameter-shift alternative"
- "quantum gradient estimation", "PQC training", "VQA optimization"
- "measurement-frugal quantum", "QUIVER optimiser", "SPSA quantum"
- "quantum automatic differentiation", "shot budget optimization"

## Pitfalls

1. **Direction sample count K**: Too few (K=1) gives high-variance estimates; too many approaches parameter-shift cost. Start with K ≈ √P.
2. **Distribution choice**: Rademacher (±1) directions give lower variance than Gaussian for most QML objectives.
3. **ε step size**: Must be small enough for linear approximation but large enough to overcome shot noise. Typical: 10⁻⁴ to 10⁻³.
4. **Variance estimation**: QUIVER requires running variance estimates; use exponential moving average over training steps.

## References

- arXiv:2606.09734 — "Adaptive directional gradients for parameterised quantum circuits" (June 2026)
- SPSA: Spall, "Multivariate stochastic approximation using a simultaneous perturbation gradient approximation" (1992)
- Parameter-shift: Schuld, "Evaluating analytic gradients on quantum hardware" (2019)
