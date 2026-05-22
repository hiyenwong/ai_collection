---
name: quantum-bayesian-transport-prediction
description: "Gate-based quantum algorithm for Bayesian state estimation using the Fokker-Planck equation on discretized state spaces. Implements probability density encoding in quantum amplitudes, QFT-based spectral evolution, and Wick rotation for unitary diffusion simulation. Use when: high-dimensional Bayesian filtering, quantum Fokker-Planck solver, transport dynamics prediction, quantum spectral methods. Activation: quantum Bayesian transport, quantum Fokker-Planck, quantum state prediction amplitudes, Wick rotation quantum diffusion, gate-based Bayesian filtering, 量子贝叶斯输运动力学."
category: ai_collection
---

# Quantum Bayesian Transport Prediction

Implement Bayesian state estimation on gate-based quantum computers by encoding probability densities in quantum amplitudes and evolving them via quantum Fourier transforms and Wick-rotated unitary surrogates.

## Source Paper

Felix Govaers. "Quantum Prediction of Transport Dynamics in Discretized State Spaces." arXiv:2604.24161 [quant-ph; cs.IT; stat.CO]. April 2026. Submitted to IEEE Transaction on Quantum Engineering.

## Core Insight

The Fokker-Planck equation governs the time evolution of probability density functions. By encoding the probability density p(x,v,t) in quantum state amplitudes |ψ⟩, we can represent high-dimensional distributions compactly (exponential in number of qubits). The evolution splits into:

1. **Drift term** → implemented exactly in amplitude space
2. **Diffusion term** → does NOT admit linear representation in amplitude space; solved via Wick rotation → unitary surrogate

## When to Use

- High-dimensional Bayesian filtering where classical discretization is prohibitive
- Quantum algorithms for transport equation solving
- State estimation with exponentially large state spaces
- Bayesian prediction steps requiring compact probability representation
- Applications needing both drift and diffusion in quantum state evolution

## Mathematical Foundation

### Fokker-Planck Equation

∂p(x,t)/∂t = -∇·[f(x)p(x,t)] + ½∇²[G(x)p(x,t)]

where f(x) is the drift field and G(x) is the diffusion coefficient.

### Quantum Amplitude Encoding

|ψ(t)⟩ = Σᵢ √p(xᵢ,t) |xᵢ⟩

The probability density is encoded in amplitudes (not probabilities directly), which means:
- p(xᵢ,t) = |⟨xᵢ|ψ(t)⟩|²
- State space dimension = 2ⁿ for n qubits (exponential scaling advantage)

### Drift Implementation (Exact)

The drift component -∇·[f(x)p] can be implemented exactly in amplitude space using:
- Circulant structure of finite-difference operators
- Quantum Fourier Transform (QFT) for spectral domain evolution
- Phase rotations corresponding to drift dynamics

### Diffusion Implementation (Wick Rotation Surrogate)

Key challenge: ∇²p does NOT have a linear representation in amplitude space because:
- p = |ψ|² (nonlinear relation)
- Diffusion ∝ ∇²|ψ|² ≠ linear operator on |ψ⟩

**Solution**: Apply Wick rotation t → -it:
- Transforms diffusion equation ∂p/∂t = D∇²p into Schrödinger-like equation i∂ψ/∂t = -iD∇²ψ
- This is a unitary evolution (dispersive phase evolution)
- Can be implemented efficiently via QFT + phase rotations

## Algorithm Steps

### Step 1: State Preparation

Initialize |ψ(0)⟩ to encode the prior probability distribution:
- For uniform prior: |ψ⟩ = H⊗ⁿ|0⟩ (Hadamard on all qubits)
- For structured prior: use amplitude loading algorithms (e.g., Grover-Rudolph)

### Step 2: QFT to Spectral Domain

Apply QFT to transform to momentum/frequency basis:
|ψ̃(k)⟩ = QFT |ψ(x)⟩

### Step 3: Drift Evolution (Exact)

Apply diagonal phase rotation corresponding to drift:
U_drift = exp(-i·H_drift·Δt)

where H_drift encodes the drift dynamics in the spectral domain.

### Step 4: Diffusion Evolution (Wick Rotation)

Apply Wick-rotated unitary for diffusion:
U_diffusion = exp(-D·k²·Δt) → via phase rotation in spectral domain

Note: This is an approximation (surrogate) — it captures the correct qualitative behavior but may not exactly match classical diffusion in all regimes.

### Step 5: Inverse QFT

Apply QFT† to return to position basis.

### Step 6: Measurement/Readout

For Bayesian filtering:
- Perform measurements to extract posterior estimates
- Use amplitude estimation for expectation values
- Or use the state directly for further quantum processing

## Quantum Circuit Complexity

| Component | Gate Complexity | Notes |
|-----------|----------------|-------|
| QFT | O(n²) | Standard QFT on n qubits |
| Drift phase rotation | O(poly(n)) | Depends on drift function complexity |
| Diffusion phase rotation | O(n) | Simple diagonal operation |
| Inverse QFT | O(n²) | Same as forward QFT |

**Total**: O(n²) per time step for the spectral evolution part.

## Implementation Considerations

### Wick Rotation Accuracy

The Wick rotation surrogate works well when:
- Diffusion coefficient is constant or slowly varying
- Time step Δt is small enough for the approximation to hold
- The dispersive phase evolution captures the essential dynamics

It may fail when:
- Diffusion is strongly state-dependent
- Boundary conditions are complex
- Long-time evolution accumulates significant approximation error

### Noise Sensitivity

- Amplitude-encoded states are sensitive to depolarizing noise
- QFT circuits accumulate phase errors with depth
- Error mitigation techniques (zero-noise extrapolation, Pauli twirling) recommended

### Comparison with Classical Methods

| Aspect | Classical | Quantum (this method) |
|--------|-----------|----------------------|
| State space | O(N) memory | O(log N) qubits |
| Drift | O(N) per step | O(poly(log N)) per step |
| Diffusion | O(N) per step | O(log N) per step (surrogate) |
| Accuracy | Exact | Approximate (Wick rotation) |

## Pitfalls

- **Wick rotation is a surrogate, not exact**: The diffusion term implemented via Wick rotation does NOT exactly reproduce classical diffusion — it produces a dispersive evolution that qualitatively matches transport dynamics
- **Amplitude vs probability encoding**: The probability is in the SQUARED amplitude, not the amplitude itself — this nonlinearity is why exact diffusion implementation fails
- **Readout bottleneck**: Extracting the full probability distribution requires O(2ⁿ) measurements, negating the exponential advantage for full distribution reconstruction
- **Best use case**: This method shines when the quantum state is used for further quantum processing (e.g., quantum decision-making, quantum optimization) rather than full classical readout

## Related Skills

- `quantum-bayesian-state-estimation` — overlapping topic, different source paper
- `quantum-bayesian-filtering` — existing skill in ai_collection with similar methodology
- `quantum-spectral-ml` — spectral methods for quantum machine learning