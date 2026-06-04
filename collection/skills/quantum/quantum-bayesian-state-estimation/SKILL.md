---
name: quantum-bayesian-state-estimation
description: "Quantum algorithms for Bayesian state estimation and transport dynamics prediction. Use when: (1) implementing Bayesian filtering/prediction on quantum computers, (2) solving Fokker-Planck equations via quantum algorithms, (3) encoding probability distributions in quantum state amplitudes, (4) implementing quantum Fourier transform for spectral-domain evolution, (5) using Wick rotation for quantum simulation of diffusion. Activation: quantum Bayesian estimation, Fokker-Planck quantum solver, quantum state prediction, amplitude-encoded probability distributions, 量子贝叶斯状态估计."
---

# Quantum Bayesian State Estimation

Implement Bayesian state estimation on gate-based quantum computers using amplitude-encoded probability distributions and quantum spectral methods.

## Core Insight

Probability densities can be encoded in quantum state amplitudes, enabling compact representation of high-dimensional distributions (exponential in number of qubits). The evolution is realized in the spectral domain using quantum Fourier transforms (QFT) and phase rotations.

## When to Use

- Bayesian filtering/prediction with high-dimensional state spaces
- Solving transport equations on quantum hardware
- Implementing quantum versions of Kalman filters
- State estimation where classical discretization is prohibitive

## Implementation Pattern

### 1. Amplitude Encoding

Encode probability density p(x) in quantum state amplitudes:

```
|ψ⟩ = Σ_x √p(x) |x⟩
```

The square root relationship between density and amplitude is key.

### 2. Drift Component (Exact Implementation)

The drift (advection) term admits an exact linear implementation in amplitude space:

```python
def implement_drift(state, velocity, dt):
    """Implement drift via phase-space translation."""
    # Shift operation in computational basis
    # |x⟩ → |x + v·dt⟩
    return quantum_shift(state, velocity * dt)
```

### 3. Diffusion Component (Wick Rotation Surrogate)

The diffusion term does NOT admit a linear representation in amplitude space due to the nonlinear √p(x) relationship. Solution: use Wick rotation to transform diffusion into dispersive phase evolution:

```python
def implement_diffusion_wick(state, diffusion_coeff, dt):
    """Implement diffusion via Wick-rotated unitary evolution."""
    # Transform: ∂_t p = D·∇²p → unitary e^{-i·D·∇²·dt}
    # This replaces classical diffusion with quantum dispersion
    
    # 1. QFT to spectral domain
    state = qft(state)
    
    # 2. Apply phase rotation: e^{-i·D·k²·dt}
    state = apply_phase_rotation(state, diffusion_coeff, dt)
    
    # 3. Inverse QFT back to position space
    state = iqft(state)
    
    return state
```

### 4. Full Fokker-Planck Evolution

```python
def evolve_fokker_planck(initial_state, drift_fn, diffusion, dt, n_steps):
    """Quantum evolution of Fokker-Planck equation."""
    state = initial_state
    
    for _ in range(n_steps):
        # Drift step (exact in amplitude space)
        state = implement_drift(state, drift_fn, dt)
        
        # Diffusion step (Wick-rotated unitary)
        state = implement_diffusion_wick(state, diffusion, dt)
    
    return state
```

### 5. Measurement and Extraction

```python
def extract_density(state, n_shots=10000):
    """Reconstruct probability density from quantum measurements."""
    # Measure in computational basis
    samples = measure(state, shots=n_shots)
    
    # Estimate p(x) from sample frequencies
    density = compute_histogram(samples, n_bins=2**n_qubits)
    density = density / n_shots
    
    return density
```

## Key Properties

| Aspect | Detail |
|--------|--------|
| State space scaling | O(2^n) with n qubits |
| Drift implementation | Exact linear operation |
| Diffusion implementation | Wick-rotated unitary surrogate |
| Complexity | O(poly(n)) per time step |
| Measurement cost | O(1/ε²) shots for ε accuracy |

## Verification Steps

1. Compare quantum solution against analytical Fokker-Planck solution
2. Verify probability conservation (Σ|ψ_x|² = 1 at all times)
3. Check convergence with increasing qubit count
4. Validate drift-only and diffusion-only components separately

## References

- Govaers (2026): "Quantum Prediction of Transport Dynamics in Discretized State Spaces" (arXiv:2604.xxxxx, quant-ph, cs.IT, stat.CO)
