---
name: quantum-gaussian-state-learning
description: >
  Sample-optimal learning of bosonic Gaussian quantum states. Provides sharp
  bounds on sample complexity for characterizing unknown n-mode Gaussian states:
  Omega(n^3/epsilon^2) for Gaussian measurements, Omega(n^2/epsilon^2) for
  arbitrary measurements. Proves non-Gaussian measurements required for optimal
  learning of passive Gaussian states. Use when: quantum state tomography,
  bosonic Gaussian states, quantum learning theory, sample complexity bounds,
  quantum sensing benchmarking, Wigner distribution learning, continuous-variable
  quantum systems. Source: arXiv:2603.18136
---

# Quantum Gaussian State Learning

## Description

Sample-optimal algorithms for learning bosonic Gaussian quantum states from
minimal copies. Establishes fundamental limits on the number of samples needed
to characterize unknown n-mode Gaussian states to epsilon trace distance.

## Sample Complexity Bounds

### General Case
- **Gaussian measurements**: Lower bound Ω(n³/ε²), matching best known upper
  bound up to doubly-log energy dependence
- **Arbitrary measurements**: Lower bound Ω(n²/ε²)

### Special Cases
- **Pure or passive states**: Upper bound Õ(n²/ε²)
- **Single-mode, non-entangling Gaussian measurements**: Õ(E/ε²) for
  non-adaptive schemes; adaptivity is indispensable for energy-independent
  scaling

## Key Theoretical Results

### 1. Measurement Type Matters

| State Type | Optimal Measurement | Sample Complexity |
|------------|-------------------|-------------------|
| Pure Gaussian | Gaussian measurements suffice | Õ(n²/ε²) |
| Passive Gaussian | **Non-Gaussian required** | Õ(n²/ε²) |
| General Gaussian | Arbitrary measurements | Ω(n²/ε²) |

### 2. Trace Distance vs Wigner Distribution

Sharp bounds established relating trace distance between Gaussian states to
total variation distance between their Wigner distributions:

```
d_TV(W_ρ, W_σ) ≤ d_trace(ρ, σ) ≤ C · d_TV(W_ρ, W_σ)
```

This enables learning via Wigner distribution sampling.

### 3. Adaptivity is Essential

For single-mode Gaussian states with non-entangling Gaussian measurements:
- Non-adaptive schemes: Ω(E/ε²) — energy-dependent
- Adaptive schemes: nearly energy-independent scaling
- **Conclusion**: adaptivity is indispensable

## Practical Algorithm Design

### Step 1: Determine State Type

```python
def choose_measurement_strategy(state_type, n_modes, energy_bound):
    if state_type == "pure":
        return "gaussian_measurements"  # sufficient
    elif state_type == "passive":
        return "non_gaussian_measurements"  # required for optimality
    else:
        return "arbitrary_measurements"
```

### Step 2: Compute Required Samples

```python
def required_samples(n_modes, epsilon, measurement_type="arbitrary"):
    if measurement_type == "gaussian":
        return Omega(n_modes**3 / epsilon**2)
    elif measurement_type == "arbitrary":
        return Omega(n_modes**2 / epsilon**2)
```

### Step 3: Wigner Distribution Learning

For learning the Wigner distribution to ε total variation distance:

```python
def learn_wigner_distribution(samples, n_modes):
    """
    Nearly tight sample complexity bound for learning Wigner distribution
    of any Gaussian state to epsilon TV distance.
    """
    # Use the established bounds to determine measurement strategy
    # Collect samples and estimate Wigner function
    pass
```

## Applications

- **Quantum sensing**: Gravitational-wave detection, dark-matter detection
- **Quantum communication**: Characterizing continuous-variable channels
- **Quantum computing**: Benchmarking Gaussian state preparation
- **Quantum metrology**: Optimal parameter estimation strategies

## Key Insights

1. **Non-Gaussian measurements are provably required** for optimal learning of
   passive Gaussian states — this is a fundamental theoretical result
2. **Adaptivity matters** — non-adaptive schemes cannot achieve
   energy-independent sample complexity
3. **Pure states are easier** — Gaussian measurements suffice for nearly
   optimal learning of pure Gaussian states
4. **Wigner-TV connection** provides a practical path to learning via phase
   space sampling

## References

- arXiv:2603.18136 — "Towards sample-optimal learning of bosonic Gaussian
  quantum states" (Senrui Chen, Francesco Anna Mele, Marco Fanizza, Alfred Li,
  Zachary Mann, Hsin-Yuan Huang, Yanbei Chen, John Preskill, 2026)
