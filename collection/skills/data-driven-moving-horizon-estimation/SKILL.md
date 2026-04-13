---
name: data-driven-moving-horizon-estimation
description: "Data-Driven Moving Horizon Estimation (DDMHE) for linear systems with unknown parameters. State estimation using both offline and online data with sample complexity analysis and ultimate boundedness guarantees. Use for: state estimation, model-free estimation, linear system identification, moving horizon estimation, data-driven control. Activation: DDMHE, data-driven estimation, moving horizon estimation, sample complexity estimation, linear system state estimation."
---

# Data-Driven Moving Horizon Estimation (DDMHE)

State estimation methodology for linear systems with unknown parameters using offline and online data.

## Overview

DDMHE addresses state estimation for linear systems subject to Gaussian noise where model parameters are unknown. By formulating an optimization problem that incorporates both offline historical data and online measurements, DDMHE provides:

- **Model-Free Estimation**: No need for explicit system identification
- **Ultimate Boundedness**: Guaranteed bounded estimation error
- **Sample Complexity**: Explicit relationship between data and accuracy
- **Noise Characterization**: Clear relationship between noise covariances and error

## Problem Formulation

### System Model

```
x(t+1) = A x(t) + B u(t) + w(t)    (State equation)
y(t)   = C x(t) + v(t)              (Measurement equation)

Where:
- x ∈ R^n: State vector (unknown parameters A, B, C)
- u ∈ R^m: Control input
- y ∈ R^p: Measurement output
- w ~ N(0, Q): Process noise
- v ~ N(0, R): Measurement noise
```

### Challenge

Traditional MHE requires known system matrices (A, B, C). DDMHE estimates states **without** explicit knowledge of these matrices.

## Key Contributions

### 1. Unified Data-Driven Formulation

Combines offline and online data:
```
Offline Data: Historical trajectories {(u, y)} from system operation
Online Data: Current measurements from running system
```

### 2. Ultimate Boundedness Guarantee

**Theorem**: The expected 2-norm of estimation error is ultimately bounded.

```
E[||e(t)||₂] ≤ ε_∞ as t → ∞

where ε_∞ depends on:
- Noise covariances (Q, R)
- Horizon length (N)
- Data quality (sample complexity)
```

### 3. Sample Complexity Analysis

Explicit bounds on required data:
```
N_samples ≥ f(ε_desired, δ_confidence, system_properties)
```

### 4. Noise-Error Relationship

Direct relationship between noise characteristics and estimation error:
```
Error_bound ∝ trace(Q) + trace(R) + cross_terms
```

## Methodology

### Optimization Problem

```
Minimize: J = J_offline + J_online + J_regularization

Where:
J_offline = Σ ||y_hist - ŷ_hist||²_R⁻¹  (Fit to historical data)
J_online  = Σ ||y_curr - ŷ_curr||²_R⁻¹  (Fit to current data)
J_reg     = λ ||θ - θ_prior||²          (Regularization)
```

### Algorithm Steps

```python
def DDMHE(y_current, u_current, data_buffer, horizon):
    """
    Data-Driven Moving Horizon Estimation
    """
    # 1. Collect recent measurements
    Y_window = data_buffer.get_last(horizon)
    
    # 2. Formulate optimization
    #    Variables: state sequence, implicit model parameters
    problem = formulate_optimization(Y_window, u_current)
    
    # 3. Solve for optimal state estimate
    x_hat = solve_optimization(problem)
    
    # 4. Update data buffer
    data_buffer.append((y_current, u_current))
    
    return x_hat
```

### Implementation

```python
class DDMHEstimator:
    def __init__(self, n_states, n_inputs, n_outputs, horizon):
        self.n = n_states
        self.m = n_inputs
        self.p = n_outputs
        self.N = horizon
        self.data_buffer = []
        
    def estimate(self, y_new, u_new):
        """
        Estimate current state from new measurement.
        """
        # Update buffer
        self.data_buffer.append((y_new, u_new))
        if len(self.data_buffer) > self.N:
            self.data_buffer.pop(0)
        
        # Formulate optimization
        # Variables: x(0), ..., x(N), implicit system dynamics
        x_hat = self.solve_mhe_problem()
        
        return x_hat[-1]  # Return most recent estimate
    
    def solve_mhe_problem(self):
        """
        Solve the moving horizon estimation problem.
        
        This is a non-convex optimization in general.
        Can use:
        - Sequential quadratic programming
        - Gradient descent
        - Alternating minimization
        """
        # Simplified: use least-squares formulation
        # with Hankel matrix structure
        pass
```

## Theoretical Properties

### Ultimate Boundedness

**Definition**: The estimation error e(t) = x(t) - x̂(t) is ultimately bounded if:

```
lim sup E[||e(t)||] ≤ ε_∞ < ∞
 t→∞
```

**DDMHE Guarantee**:
```
ε_∞ = f(Q, R, N, data_quality)

As data_quality → ∞: ε_∞ → ε_MHE (standard MHE bound)
```

### Sample Complexity

**Theorem**: To achieve error bound ε with probability 1-δ:

```
T ≥ O( (n + m) log(1/δ) / ε² )

Where:
- n: state dimension
- m: input dimension
- T: number of offline samples
```

### Noise Sensitivity

The error bound depends on noise covariances:

```
ε_∞² ≈ α·trace(Q) + β·trace(R) + γ·trace(Q·R)

Where α, β, γ depend on system properties and horizon.
```

## Practical Considerations

### Horizon Selection

| Horizon | Computational Cost | Estimation Accuracy | Tracking Ability |
|---------|-------------------|---------------------|------------------|
| Short (N=5) | Low | Lower | Faster |
| Medium (N=20) | Medium | Good | Balanced |
| Long (N=50) | High | Higher | Slower |

### Data Requirements

**Minimum Data**: At least (n+m) samples per mode
**Recommended**: 10× minimum for robustness
**Online Updates**: Continuously incorporate new data

### Computational Aspects

```python
# Optimization complexity per step: O(N³(n+m)³)
# Can be reduced using:
# - Warm starting
# - Sparse structure exploitation
# - Approximate solvers
```

## Comparison with Other Methods

| Method | Needs Model | Online Learning | Guarantees | Computational Cost |
|--------|-------------|-----------------|------------|-------------------|
| Kalman Filter | Yes | No | Optimal (linear) | O(n³) |
| Standard MHE | Yes | No | Bounded | O(Nn³) |
| Subspace ID + KF | No | Offline only | Asymptotic | Batch |
| **DDMHE** | **No** | **Yes** | **Bounded** | **O(N³(n+m)³)** |

## Applications

### 1. Unknown System Estimation

When system model is unavailable:
```python
# No need for system identification
estimator = DDMHEstimator(n=4, m=2, p=2, horizon=20)

# Directly estimate from data
for y, u in measurements:
    x_hat = estimator.estimate(y, u)
```

### 2. Time-Varying Systems

Adapt to slow parameter variations:
```python
# Use sliding window of recent data
estimator.data_buffer = deque(maxlen=horizon)

# Old data automatically forgotten
```

### 3. Fault Detection

Detect changes through residual analysis:
```python
residual = y - C @ x_hat
if residual.norm > threshold:
    trigger_fault_detection()
```

### 4. Adaptive Control

Use estimates for control:
```python
# Estimate current state
x_hat = ddmhe.estimate(y, u)

# Compute control
u = controller.compute(x_hat, reference)
```

## Extensions

### 1. Nonlinear Systems

Use local linearization or kernel methods:
```python
# Kernel DDMHE
K = kernel_matrix(data_buffer)
x_hat = K @ weights
```

### 2. Distributed DDMHE

Multiple sensors/agents:
```python
# Consensus-based distributed estimation
x_hat_i = local_DDMHE(y_i, u)
x_hat = consensus_average(x_hat_i for all i)
```

### 3. Robust DDMHE

Handle outliers and attacks:
```python
# Use robust loss function
J = Σ ρ(||y - ŷ||)  # ρ = Huber or Tukey
```

## References

- **Paper**: "Data-Driven Moving Horizon Estimators for Linear Systems with Sample Complexity Analysis" by Duan et al. (arXiv:2604.08328v1, 2026)
- **Authors**: Peihu Duan, Jiabao He, Yuezu Lv, et al.
- **Category**: eess.SY (Systems and Control)

## Related Skills

- **discounted-mpc-robust-control**: MPC under plant-model mismatch
- **density-driven-multi-agent-control**: Multi-agent stochastic control
- **finite-time-reachability-partial-control**: Constrained reachability

## Activation Keywords

- DDMHE
- data-driven estimation
- moving horizon estimation
- sample complexity estimation
- linear system state estimation
- model-free state estimation
- data-driven MHE
- ultimate boundedness estimation
