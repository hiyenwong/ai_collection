---
name: wavelet-variance-equipartition-quantum
description: "Wavelet Variance Equipartition methodology for assessing world-model quality and quantum kernel tensor-network simulability. Uses wavelet scaling exponents as physics-grounded diagnostic. Based on arXiv:2605.11557."
---

# Wavelet Variance Equipartition for Model Quality Assessment

Wavelet Variance Equipartition (WVE) methodology for physics-grounded assessment of learned representations and quantum kernel simulability (arXiv:2605.11557).

## Core Problem

World models and quantum machine learning models learn compact representations of complex environments, but lack physics-grounded metrics to assess the structural fidelity of their latent spaces. WVE provides a rigorous diagnostic.

## Key Innovation

### Wavelet Scaling Exponent as Diagnostic

- The wavelet scaling exponent α characterizes how variance distributes across scales
- **Equipartition condition**: optimal representations satisfy α ≈ 0 (uniform variance across scales)
- Deviations from equipartition indicate structural deficiencies in the learned representation

### Quantum Kernel TN-Simulability

- The same wavelet analysis determines whether a quantum kernel can be efficiently simulated by tensor networks
- If α indicates scale-invariant structure, the kernel admits efficient TN representation
- This bridges quantum advantage claims with classical simulability bounds

## Mathematical Framework

### Wavelet Variance Decomposition

Given a signal/representation f(x):

1. **Wavelet Transform**: Wₛf(a, b) = ⟨f, ψ_{a,b}⟩ where ψ is the mother wavelet
2. **Scale-wise Variance**: V(a) = E[|Wₛf(a, b)|²]
3. **Scaling Exponent**: V(a) ∝ a^{-2α-1}

### Equipartition Criterion

- α = 0: optimal (variance equally distributed across all scales)
- α > 0: variance concentrated at coarse scales (loss of fine detail)
- α < 0: variance concentrated at fine scales (noisy/overfitting)

### TN-Simulability Threshold

The wavelet scaling exponent determines tensor network bond dimension requirements:
- If α satisfies certain bounds → poly(n) bond dimension suffices
- Otherwise → exponential bond dimension required (quantum advantage possible)

## Implementation Patterns

### Pattern 1: Computing Wavelet Scaling Exponent

```python
import numpy as np
from scipy import signal

def compute_wavelet_scaling(x, scales=None, wavelet='morlet'):
    """Compute wavelet variance and scaling exponent."""
    if scales is None:
        scales = np.logspace(0, np.log2(len(x)//4), num=10, base=2)
    
    variances = []
    for a in scales:
        coeffs = signal.cwt(x, signal.morlet2, widths=[int(a)])
        variances.append(np.mean(coeffs**2))
    
    # Fit power law: V(a) ∝ a^{-2α-1}
    log_scales = np.log(scales)
    log_vars = np.log(variances)
    
    # Linear fit: log(V) = (-2α-1) * log(a) + c
    slope, intercept = np.polyfit(log_scales, log_vars, 1)
    alpha = -(slope + 1) / 2
    
    return alpha, scales, variances
```

### Pattern 2: Model Quality Assessment

```python
def assess_model_quality(representations, target_alpha=0, tolerance=0.1):
    """Assess structural fidelity of learned representations."""
    results = {}
    for layer_name, rep in representations.items():
        alpha, _, _ = compute_wavelet_scaling(rep)
        deviation = abs(alpha - target_alpha)
        results[layer_name] = {
            'alpha': alpha,
            'equipartition_score': max(0, 1 - deviation / tolerance),
            'optimal': deviation < tolerance
        }
    return results
```

### Pattern 3: Quantum Kernel TN-Simulability Test

```python
def check_tn_simulability(quantum_kernel_data, max_bond_dim=2**20):
    """Determine if quantum kernel is efficiently TN-simulable."""
    alpha, _, variances = compute_wavelet_scaling(quantum_kernel_data)
    
    # Estimate required bond dimension
    # Bond dimension χ ~ 2^{H(α)} where H is entropy of scale distribution
    scale_entropy = -np.sum([v*np.log2(v+1e-10) for v in np.array(variances)/sum(variances)])
    required_bond_dim = 2 ** scale_entropy
    
    return {
        'alpha': alpha,
        'scale_entropy': scale_entropy,
        'required_bond_dim': required_bond_dim,
        'tn_simulable': required_bond_dim <= max_bond_dim,
        'quantum_advantage_possible': required_bond_dim > max_bond_dim
    }
```

## Activation Keywords

- wavelet variance equipartition
- wavelet scaling exponent
- quantum kernel simulability
- world model quality assessment
- wavelet variance quantum
- 小波方差均分
- TN simulability

## Usage Guidelines

### When to Use

1. **Assessing latent space quality** of world models or VAEs
2. **Evaluating quantum kernel efficiency** claims
3. **Determining classical simulability bounds** for quantum ML
4. **Multi-scale representation analysis** in any learned model

### Wavelet Selection

| Use Case | Recommended Wavelet |
|----------|-------------------|
| Smooth signals | Morlet |
| Discontinuous | Haar |
| Oscillatory | Mexican hat |
| Compact support | Daubechies |

### Prerequisites

- Wavelet analysis basics
- Understanding of tensor network representations
- Linear algebra and functional analysis

## Related Skills

- `unitaria-quantum-linear-algebra` - Block encoding for quantum kernels
- `photonic-variational-trainability` - Variational circuit trainability
- `quantum-ml-patterns` - QML research patterns

## arXiv Reference

- arXiv: 2605.11557v1
- Title: "Wavelet Variance Equipartition as a Threshold for World-Model Quality and Quantum Kernel TN-Simulability"
- Published: 2026-05-12
- Categories: quant-ph
