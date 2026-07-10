---
name: brain-criticality-milro-assessment
description: "Memory-Induced Long-Range Order (MILRO) assessment framework challenging the brain criticality hypothesis. Analyzes scale-invariant correlations in neural activity as stable phase rather than critical point. Keywords: brain criticality, MILRO, scale-free, neural correlations, memory-induced order"
---

# Brain Criticality Assessment: Memory-Induced Long-Range Order (MILRO)

> Critical assessment of the brain criticality hypothesis, proposing that scale-invariant correlations arise from memory-induced long-range order rather than criticality.

## Metadata
- **Source**: arXiv:2604.21071v1
- **Authors**: Chesson Sipling, Yuan-Hang Zhang, Massimiliano Di Ventra
- **Published**: 2026-04-22

## Core Methodology

### Key Innovation
Challenges the prevailing "brain criticality hypothesis" which proposes the brain operates near a critical point to optimize information processing. Instead, introduces the Memory-Induced Long-Range Order (MILRO) phase - a stable phase of neural activity where scale-invariant correlations emerge from coupling between neurons and slowly varying resources.

### Critical Hypothesis Comparison

| Aspect | Criticality Hypothesis | MILRO Hypothesis |
|--------|----------------------|------------------|
| **Mechanism** | Tuning to critical point | Coupling to slow resources (memory) |
| **Stability** | Unstable (sensitive to perturbations) | Stable (robust to perturbations) |
| **Scale-invariance** | Emerges at critical point | Natural property of MILRO phase |
| **Information processing** | Optimal at criticality | Optimal in stable MILRO phase |
| **Experimental prediction** | Fine-tuning required | No fine-tuning required |

### Theoretical Framework

**Memory-Induced Long-Range Order (MILRO):**

1. **Coupling Mechanism**
   - Neurons interact with slowly varying resource variables
   - Resources act as "memory" - accumulating and releasing over time
   - Example: Calcium concentrations, metabolic resources, adaptation currents

2. **Mathematical Formulation**
   ```
   dN/dt = f(N, R) + noise      (neuron dynamics)
   dR/dt = epsilon * g(N, R)    (slow resource dynamics)
   
   where:
   - N: neural activity
   - R: resource/memory variable  
   - epsilon << 1: slow timescale separation
   ```

3. **Scale-Invariant Correlations**
   - MILRO phase naturally exhibits power-law correlations
   - Correlation length diverges (long-range order)
   - Unlike critical points, MILRO is a stable phase

## Implementation Guide

### Prerequisites
```bash
pip install numpy scipy matplotlib
pip install powerlaw  # For scale-free analysis
pip install brian2    # For neural simulation
```

### Step-by-Step Implementation

**Step 1: Generate MILRO Model Data**
```python
import numpy as np
from scipy.integrate import odeint

def milro_model(y, t, N, tau_r, J, I_ext):
    """
    Memory-Induced Long-Range Order neural network model.
    
    Args:
        y: state vector [neuron activities, resource variables]
        t: time points
        N: number of neurons
        tau_r: resource timescale (slow)
        J: coupling strength matrix
        I_ext: external input
    """
    n = y[:N]      # neural activities
    r = y[N:]      # resource variables
    
    # Neuron dynamics (fast)
    dn = -n + np.tanh(J @ n + I_ext + r) + np.random.randn(N) * 0.1
    
    # Resource dynamics (slow)
    dr = (-r + np.tanh(n)) / tau_r
    
    return np.concatenate([dn, dr])

def simulate_milro(N=100, T=10000, dt=0.1, tau_r=100.0):
    """
    Simulate MILRO model neural network.
    """
    # Random connectivity
    np.random.seed(42)
    J = np.random.randn(N, N) / np.sqrt(N)
    
    # Initial conditions
    y0 = np.random.randn(2 * N) * 0.1
    t = np.arange(0, T, dt)
    I_ext = np.ones(N) * 0.5
    
    solution = odeint(milro_model, y0, t, args=(N, tau_r, J, I_ext))
    
    activity = solution[:, :N].T
    resources = solution[:, N:].T
    
    return activity, resources, t
```

**Step 2: Detect Scale-Invariant Correlations**
```python
import powerlaw

def compute_neural_avalanches(activity, threshold=1.0):
    """
    Detect neural avalanches from activity time series.
    """
    N, T = activity.shape
    active = (activity > threshold).astype(int)
    population_activity = active.sum(axis=0)
    
    avalanches = {'sizes': [], 'durations': []}
    in_avalanche = False
    current_size = 0
    current_duration = 0
    
    for t in range(T):
        if population_activity[t] > 0:
            if not in_avalanche:
                in_avalanche = True
                current_size = 0
                current_duration = 0
            current_size += population_activity[t]
            current_duration += 1
        else:
            if in_avalanche:
                in_avalanche = False
                avalanches['sizes'].append(current_size)
                avalanches['durations'].append(current_duration)
    
    return avalanches

def fit_powerlaw(data, discrete=True):
    """
    Fit power-law distribution to data.
    """
    fit = powerlaw.Fit(data, discrete=discrete)
    alpha = fit.power_law.alpha
    xmin = fit.power_law.xmin
    R, p = fit.distribution_compare('power_law', 'exponential')
    
    return alpha, xmin, fit, R, p
```

**Step 3: Distinguish Criticality from MILRO**
```python
def assess_criticality_indicators(activity, resources):
    """
    Assess whether system shows criticality or MILRO characteristics.
    """
    results = {}
    
    # 1. Avalanche size distribution
    avalanches = compute_neural_avalanches(activity)
    sizes = np.array(avalanches['sizes'])
    alpha, xmin, _, _, _ = fit_powerlaw(sizes)
    results['avalanche_exponent'] = alpha
    
    # 2. Resource dynamics correlation with activity
    resource_activity_corr = np.corrcoef(
        resources[:, :-100].flatten(), 
        activity[:, 100:].flatten()
    )[0, 1]
    results['resource_activity_correlation'] = resource_activity_corr
    
    return results
```

## Applications

1. **Brain Criticality Analysis**: Determine whether neural systems operate at criticality or in MILRO phase
2. **Computational Modeling**: Test resource-coupled neural network models
3. **Experimental Design**: Design experiments to distinguish criticality from MILRO

## Distinguishing Criticality from MILRO

| Observable | Criticality | MILRO |
|------------|-------------|-------|
| **Avalanche exponents** | Universal values | May deviate |
| **Correlation length** | ξ → ∞ at critical point | ξ large but finite |
| **Stability** | Marginally stable | Stable to perturbations |
| **Parameter tuning** | Requires fine-tuning | Robust to changes |

## Pitfalls

1. **Scale-Free ≠ Critical**: Scale-free avalanches can arise from multiple mechanisms
2. **Finite Size Effects**: Real brains are finite; hard to distinguish true criticality
3. **Multiple Mechanisms**: Subsampling, filtering can also produce scale-free statistics

## Related Skills

- griffiths-phase-brain-criticality
- brain-criticality-hypothesis-assessment

## References

```bibtex
@article{sipling2026milro,
  title={A Critical Assessment of the Brain Criticality Hypothesis},
  author={Sipling, Chesson and Zhang, Yuan-Hang and Di Ventra, Massimiliano},
  journal={arXiv preprint arXiv:2604.21071},
  year={2026}
}
```
