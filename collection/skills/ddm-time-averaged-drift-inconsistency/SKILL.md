---
name: ddm-time-averaged-drift-inconsistency
description: "Proving time-averaged drift approximations are mathematically inconsistent for inference in Drift Diffusion Models (DDMs), with implications for computational neuroscience decision-making models. Activation: drift diffusion model, DDM, evidence accumulation, decision-making, time-varying drift, computational neuroscience, inconsistency, statistical inference."
---

# Time-Averaged Drift Approximations are Inconsistent for DDM Inference

> Mathematical proof that widely-used time-averaged drift rate approximations in Drift Diffusion Models lead to inconsistent parameter estimates, with correct alternatives for computational neuroscience.

## Metadata
- **Source**: arXiv:2512.10250
- **Authors**: Sicheng Liu, Alexander Fengler, Michael J. Frank
- **Published**: 2025-12-11
- **Categories**: stat.ME, stat.AP, stat.CO

## Core Methodology

### Key Innovation
Demonstrates that when DDM drift rates vary within a trial and across trials, the common practice of using time-averaged drift as a proxy for the true drift process produces inconsistent (non-converging) parameter estimates even with infinite data. Provides correct likelihood-based alternatives.

### Technical Framework
1. **Standard DDM**: Evidence accumulation dX = v(t)dt + σdW, with drift v(t) and boundary a
2. **Time-Averaged Drift Problem**: Practitioners often replace v(t) with its time-average v̄, assuming it yields equivalent inference
3. **Inconsistency Proof**: Shows that time-averaged approximation systematically biases drift rate and boundary estimates — bias does not vanish with more data
4. **Correct Approach**: Use full likelihood computation accounting for time-varying drift structure

### Implementation Guide

#### Prerequisites
- Stochastic processes (Brownian motion, first-passage times)
- Numerical methods for PDEs (Fokker-Planck equation)
- Understanding of DDM parameter estimation

#### Step-by-Step
1. Specify the true time-varying drift model v(t)
2. Generate synthetic data from the true model
3. Compare parameter recovery: time-averaged vs. full likelihood
4. Quantify bias: show time-averaged estimates diverge from truth
5. Implement correct likelihood via numerical PDE solution

### Code Example
```python
import numpy as np

def simulate_ddm_time_varying(v_func, boundary, noise_std=1.0, dt=0.001, max_time=10.0):
    """Simulate DDM with time-varying drift rate."""
    t = 0.0
    x = 0.0
    while t < max_time:
        v = v_func(t)  # Time-varying drift
        x += v * dt + noise_std * np.sqrt(dt) * np.random.randn()
        if x >= boundary:
            return t, +1  # upper boundary hit
        elif x <= -boundary:
            return t, -1  # lower boundary hit
        t += dt
    return max_time, 0  # timeout

# Example: linearly increasing drift
v_func = lambda t: 1.0 + 0.5 * t
rt, choice = simulate_ddm_time_varying(v_func, boundary=1.5)
print(f"RT={rt:.3f}s, Choice={choice}")
```

## Applications
- **Decision Neuroscience**: Correct modeling of evidence accumulation in cognitive tasks
- **Psychophysics**: More accurate RT distribution fitting for perceptual decisions
- **Clinical Assessment**: Unbiased parameter estimation for patient populations
- **Reinforcement Learning**: Better drift-diffusion models of value-based decisions

## Pitfalls
- Full likelihood computation is computationally expensive
- Time-averaged approximation is deeply embedded in existing software (HDDM, PyDDM)
- Practitioners may not realize their drift rates are time-varying
- Requires careful model specification to avoid overfitting

## Related Skills
- computational-neuroscience-models
- neural-dynamics-decision-making
- bci-rehabilitation-protocols
