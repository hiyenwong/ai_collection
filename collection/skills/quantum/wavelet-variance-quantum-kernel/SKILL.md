---
name: wavelet-variance-quantum-kernel
description: >
  Use wavelet variance equipartition (scaling exponent α) as a physics-grounded
  diagnostic for world model quality and to assess quantum kernel simulability
  via tensor networks. Use when evaluating latent space quality of world models,
  determining classical simulability of quantum kernels, analyzing scale-invariant
  properties of learned representations, applying tensor network methods to quantum
  machine learning, or establishing Kolmogorov-like diagnostics for ML systems.
---

## Core Concept

The wavelet scaling exponent α serves as a critical diagnostic:

- **Optimal representations** satisfy variance equipartition: **α ≈ 1/2**
  (mirroring Kolmogorov's inertial range in turbulence)
- **α = 1/2** is a sharp transition boundary for classical simulability of
  amplitude-encoded quantum kernels via tensor networks

## Wavelet Variance Analysis

### Computing the Scaling Exponent

1. Apply wavelet transform to the representation/latent space
2. Compute variance at each scale j: V(j) = Var(W_j(x))
3. Fit log-log relationship: log V(j) ≈ α · j + C
4. The slope α characterizes the scale-dependence of variance

### Interpretation

- **α > 1/2**: Long-range correlations, structured but potentially overfit
- **α ≈ 1/2**: Optimal — variance equipartition, Kolmogorov-like scaling
- **α < 1/2**: Anti-correlated, noisy, under-structured

## Quantum Kernel Simulability

The same exponent α determines whether a quantum kernel can be efficiently
simulated classically via tensor networks:

- **α ≥ 1/2**: Tensor network simulation becomes efficient
- **α < 1/2**: Quantum advantage may persist (hard to simulate classically)

This provides a practical criterion:
1. Compute α for your quantum kernel's feature representation
2. If α ≥ 1/2: consider classical TN simulation as alternative
3. If α < 1/2: quantum advantage may be justified

## World Model Quality Assessment

Use α to evaluate learned world models:

1. Extract latent representations from the world model
2. Compute wavelet scaling exponent α
3. Compare to α = 1/2 benchmark
4. Models closer to 1/2 have more physically faithful latent spaces

## Practical Workflow

```python
import pywt
import numpy as np

def compute_scaling_exponent(data, scales=None):
    """Compute wavelet variance scaling exponent α."""
    if scales is None:
        scales = range(1, 8)
    
    variances = []
    for j in scales:
        coeffs = pywt.wavedec(data, 'db4', level=j)
        detail = coeffs[-1]  # finest scale detail coefficients
        variances.append(np.var(detail))
    
    # Fit log-log slope
    log_scales = np.log2(list(scales))
    log_vars = np.log2(variances)
    alpha = np.polyfit(log_scales, log_vars, 1)[0]
    return alpha
```

## Applications

- **World model evaluation**: Validate structural fidelity of learned environments
- **Quantum kernel analysis**: Determine if quantum advantage is necessary
- **Representation learning**: Guide regularization toward α ≈ 1/2
- **Tensor network compression**: Identify compressible quantum circuits

## Activation
- wavelet variance equipartition, quantum kernel simulability, tensor network quantum
- Kolmogorov scaling exponent, world model quality metric, scaling exponent α
- amplitude-encoded quantum kernel, tensor network simulation
- representation learning diagnostic, physics-grounded ML evaluation
