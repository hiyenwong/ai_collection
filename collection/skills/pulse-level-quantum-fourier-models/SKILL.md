---
name: pulse-level-quantum-fourier-models
description: "Pulse-level Quantum Fourier Models (QFMs) for quantum machine learning. Use when: (1) implementing variational quantum algorithms at the pulse/hardware level, (2) optimizing QFM training landscapes, (3) designing pulse-parameterized quantum circuits, (4) analyzing expressibility and Fourier coefficient correlation of quantum models, (5) replacing gate-level parameterization with pulse-level control. Activation: pulse-level quantum computing, quantum Fourier models, QFM training optimization, pulse parameterized quantum circuits, quantum machine learning hardware control, 脉冲级量子傅里叶模型."
---

# Pulse-Level Quantum Fourier Models

Implement Quantum Fourier Models (QFMs) using pulse-level control parameters instead of abstract gate angles for improved training performance.

## Core Insight

Pulse-level parameterization fundamentally alters the local optimization landscape of QFMs. Independent pulse scalings replace a single logical gate angle with multiple independently tunable sub-angles, relaxing rigid monomial couplings and providing gradient descent with higher-dimensional escape routes.

## When to Use

- Training QFMs that converge poorly at the gate level
- Designing quantum ML models for near-term hardware
- Optimizing variational circuits with barren plateaus
- Implementing feature maps with exponential/ternary frequency structure

## Implementation Pattern

### 1. Pulse Parameterization

Instead of a single rotation angle θ per gate:

```python
# Gate-level: single parameter
U(θ) = RZ(θ)

# Pulse-level: multiple sub-angles
U_pulse(θ₁, θ₂, ..., θₙ) = RZ(θ₁) · RZ(θ₂) · ... · RZ(θₙ)
```

Each pulse scaling provides an independent optimization direction.

### 2. Expressibility Analysis

Compute expressibility and Fourier coefficient correlation (FCC):

```python
def compute_fcc(pulse_params, feature_map):
    """Fourier coefficient correlation for pulse-level QFM."""
    # Evaluate model at multiple input points
    outputs = [evaluate_qfm(pulse_params, x) for x in sample_inputs()]
    
    # Compute Fourier spectrum
    spectrum = fft(outputs)
    
    # Correlation of Fourier coefficients
    fcc = np.corrcoef(np.abs(spectrum))
    
    return spectrum, fcc
```

### 3. Training Pipeline

```python
def train_pulse_qfm(pulse_params, data, n_steps=100, lr=0.01):
    for step in range(n_steps):
        # Forward pass with pulse parameters
        predictions = [evaluate_qfm(pulse_params, x) for x, y in data]
        loss = compute_loss(predictions, [y for x, y in data])
        
        # Gradient computation via parameter-shift
        grads = parameter_shift_gradient(pulse_params, data)
        
        # Update pulse parameters independently
        for i in range(len(pulse_params)):
            pulse_params[i] -= lr * grads[i]
    
    return pulse_params
```

### 4. Key Properties

| Property | Gate-Level | Pulse-Level |
|----------|-----------|-------------|
| Parameters per gate | 1 | N (pulse sub-angles) |
| Optimization landscape | Rigid monomial couplings | Relaxed, decoupled |
| Training convergence | Limited | Significantly improved |
| Expressibility | Fixed | Slightly altered |
| Hardware mapping | Indirect | Direct |

## Mathematical Foundation

The QFM output is a Fourier series:
```
f(x) = Σ_k c_k · e^(i·k·x)
```

At gate level, Fourier coefficients are coupled through monomial dependencies on gate angles. Pulse-level parameterization breaks these couplings by introducing independent sub-angles for each pulse segment.

## Verification Steps

1. Compare expressibility histograms between gate-level and pulse-level parameterizations
2. Measure FCC before and after pulse optimization
3. Validate training convergence on benchmark Fourier series tasks
4. Check that optimized pulse sequences remain physically implementable

## References

- Strobl, Franz, Scheller, Kuehn, Mauerer (2026): "Beyond Gates: Pulse Level Quantum Fourier Models" (arXiv:2605.03xxx)
