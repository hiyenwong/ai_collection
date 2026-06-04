---
name: sample-optimal-gaussian-state-learning
description: "Sample complexity bounds and algorithms for learning bosonic Gaussian quantum states. Use when: (1) analyzing sample requirements for quantum state tomography, (2) designing efficient measurement strategies for Gaussian states, (3) computing sample complexity lower/upper bounds for continuous-variable systems, (4) determining when non-Gaussian measurements are required, (5) optimizing adaptive measurement schemes for quantum state learning. Activation: Gaussian state tomography, sample complexity quantum learning, bosonic state characterization, continuous-variable quantum learning, optimal quantum measurements, 高斯量子态学习."
---

# Sample-Optimal Learning of Bosonic Gaussian States

Implement efficient learning protocols for bosonic Gaussian quantum states with provable sample complexity bounds.

## Core Insight

For n-mode Gaussian states, the sample complexity depends critically on the measurement strategy:
- Gaussian measurements: Ω(n³/ε²) lower bound
- Arbitrary measurements: Ω(n²/ε²) lower bound
- Pure or passive Gaussian states: Õ(n²/ε²) achievable

Non-Gaussian measurements are provably required for optimal learning of passive Gaussian states.

## When to Use

- Quantum state tomography for continuous-variable systems
- Gravitational-wave detector characterization
- Dark-matter detection state estimation
- Any Gaussian state learning task with limited samples

## Sample Complexity Bounds

### General n-mode Gaussian States

| Measurement Type | Lower Bound | Upper Bound | Notes |
|-----------------|-------------|-------------|-------|
| Gaussian only | Ω(n³/ε²) | Õ(n³/ε²) | Nearly tight |
| Arbitrary | Ω(n²/ε²) | ? | Gap unknown |
| Pure Gaussian | Ω(n²/ε²) | Õ(n²/ε²) | Gaussian measurements suffice |
| Passive Gaussian | Ω(n²/ε²) | Õ(n²/ε²) | Requires non-Gaussian measurements |

### Single-Mode Case

For learning single-mode Gaussian states with non-entangling Gaussian measurements:
- Non-adaptive: Θ̃(E/ε²) where E is energy
- Adaptive: Energy-independent scaling achievable
- Adaptivity is indispensable for nearly energy-independent scaling

## Implementation Pattern

### 1. Gaussian State Parameterization

An n-mode Gaussian state is fully characterized by:
- First moments (displacement vector): 2n real parameters
- Second moments (covariance matrix): 2n² + n real parameters

```python
def gaussian_state_params(cov_matrix, displacement):
    """Parameterize Gaussian state by covariance and displacement."""
    # Covariance matrix: 2n × 2n, symmetric, positive definite
    # Displacement: 2n-dimensional real vector
    return {
        'cov': cov_matrix,
        'displacement': displacement,
        'n_modes': len(displacement) // 2
    }
```

### 2. Measurement Strategy Selection

```python
def select_measurement_strategy(state_type, n_modes, target_eps):
    """Choose optimal measurement strategy based on state properties."""
    if state_type == 'pure_gaussian':
        return 'gaussian_measurements'  # Õ(n²/ε²) achievable
    elif state_type == 'passive_gaussian':
        return 'non_gaussian_measurements'  # Required for optimality
    elif state_type == 'general_gaussian':
        if adaptivity_available:
            return 'adaptive_non_gaussian'  # Best scaling
        else:
            return 'gaussian_measurements'  # Õ(n³/ε²)
```

### 3. Adaptive Learning Protocol

```python
def adaptive_gaussian_learning(n_modes, n_samples, measurement_fn):
    """Adaptive protocol for Gaussian state learning."""
    estimates = []
    
    for round in range(n_rounds):
        # Choose measurement based on previous estimates
        measurement = adapt_measurement(estimates, round)
        
        # Perform measurements
        results = measure_states(measurement, n_samples // n_rounds)
        
        # Update estimate
        estimate = update_estimate(results, measurement)
        estimates.append(estimate)
    
    return combine_estimates(estimates)
```

## Key Theorems

1. **Gaussian measurement lower bound**: Ω(n³/ε²) samples needed with Gaussian measurements only
2. **Arbitrary measurement lower bound**: Ω(n²/ε²) is fundamental limit
3. **Pure state sufficiency**: Gaussian measurements suffice for pure Gaussian states
4. **Passive state necessity**: Non-Gaussian measurements provably required for passive states
5. **Adaptivity necessity**: Adaptive schemes needed for energy-independent scaling in single-mode case

## Verification Steps

1. Verify sample complexity matches bounds for known cases
2. Check that pure state learning converges with Gaussian measurements
3. Validate that passive state learning requires non-Gaussian measurements
4. Compare adaptive vs non-adaptive performance for single-mode case

## References

- Chen, Mele, Fanizza, Li, Mann, Huang, Chen, Preskill (2026): "Towards sample-optimal learning of bosonic Gaussian quantum states" (arXiv:2603.xxxxx, quant-ph, cs.IT, cs.LG, math-ph)
