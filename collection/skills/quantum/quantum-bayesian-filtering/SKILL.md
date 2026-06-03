---
name: quantum-bayesian-filtering
description: "Gate-based quantum algorithm for Bayesian state estimation using the Fokker-Planck equation. Encodes probability density in quantum state amplitudes with QFT and phase rotations, using Wick rotation-based unitary surrogate for diffusion. Applicable for high-dimensional filtering, Bayesian inference, transport dynamics prediction. Activation: quantum bayesian filtering, quantum state estimation, quantum fokker-planck, wick rotation diffusion, quantum transport prediction, gate-based bayesian"
---

# Quantum Bayesian Filtering

## Core Idea

Encode **probability density functions** as quantum state amplitudes, then use **Wick rotation** to convert the Fokker-Planck diffusion equation into a unitary Schrödinger evolution — enabling efficient quantum simulation of Bayesian filtering.

## Mathematical Foundation

### Fokker-Planck Equation (Classical)

$$\frac{\partial p(x,t)}{\partial t} = -\nabla \cdot [f(x)p(x,t)] + \frac{1}{2}\nabla^2 [G(x)p(x,t)]$$

### Wick Rotation to Unitary Dynamics

Replace $t \rightarrow -it$ (Wick rotation):
$$i\frac{\partial \psi(x,t)}{\partial t} = \hat{H}\psi(x,t)$$

where $\hat{H} = -\frac{1}{2}\nabla^2 + V(x)$ is the quantum Hamiltonian corresponding to the Fokker-Planck operator.

### Bayesian Update as Phase Rotation

Measurement likelihood $L(x) = p(y|x)$ becomes a **phase rotation**:
$$|\psi'\rangle = e^{i\lambda L(\hat{x})} |\psi\rangle$$

## Algorithm

### Step 1: State Preparation

Encode prior $p(x_0)$ into quantum register:
```python
# Amplitude encoding of prior distribution
# |ψ₀⟩ = Σ √p(x_i) |x_i⟩
```

### Step 2: Prediction Step (Quantum Diffusion)

Apply unitary $U = e^{-i\hat{H}\Delta t}$ for time evolution:
```python
def quantum_prediction(state, hamiltonian, dt):
    """Apply Wick-rotated Fokker-Planck evolution."""
    # Trotterized evolution
    return expm(-1j * hamiltonian * dt) @ state
```

### Step 3: Measurement Update (Phase Rotation)

```python
def quantum_update(state, likelihood, reg_qubits):
    """Apply Bayesian update as controlled phase rotation."""
    # Likelihood oracle: |x⟩|0⟩ → |x⟩|L(x)⟩
    # Phase kickback: |x⟩ → e^{iλL(x)}|x⟩
    pass
```

### Step 4: Quantum Fourier Transform

Use QFT for efficient convolution in frequency domain:
```python
def qft_convolution(prior_pdf, kernel, n_qubits):
    """Efficient convolution via quantum Fourier transform."""
    # Apply QFT, multiply in frequency domain, inverse QFT
    pass
```

## Key Advantages (arXiv:2604.24161)

| Aspect | Classical Filter | Quantum Filter |
|--------|------------------|----------------|
| Dimensionality | O(N) scaling | O(log N) qubits |
| Diffusion | PDE discretization | Unitary evolution |
| Convolution | FFT O(N log N) | QFT O(log² N) |

## When to Use

- **High-dimensional filtering**: Particle filter curse of dimensionality
- **Real-time state estimation**: Quantum parallel evaluation
- **Nonlinear dynamics**: When Fokker-Planck lacks closed-form solution
- **Quantum sensor fusion**: Combining quantum measurements with classical priors

## Implementation Notes

### Wick Rotation Validity
- Requires positive-definite diffusion matrix
- Boundary conditions must preserve unitarity
- Stochastic noise → coherent superposition mapping

### Gate Decomposition
- Hamiltonian simulation: Trotter-Suzuki decomposition
- Phase rotation: QROM + controlled-Rz gates
- State preparation: Quantum RAM or variational circuits

## Pitfalls

- **State preparation bottleneck**: Loading classical distributions into quantum states is expensive
- **Measurement collapse**: Extracting full PDF requires repeated measurements
- **Noise sensitivity**: Decoherence affects phase rotation accuracy
- **Normalization**: Quantum states are automatically normalized — classical probability conservation must be ensured separately
