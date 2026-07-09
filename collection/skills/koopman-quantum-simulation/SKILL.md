---
name: koopman-quantum-simulation
description: "Quantum Koopman method — data-driven framework for simulating nonlinear dynamics on quantum computers. Embeds nonlinear dynamics into learned linear representation via Koopman observables, then implements evolution using shallow quantum circuits with parallel spectral channels. Validated on superconducting processor for reaction-diffusion, fluid dynamics, and ocean currents."
---

# Quantum Koopman Simulation

## Core Concept

Nonlinear dynamics are **fundamentally limited** on quantum computers due to unitary evolution. The **Quantum Koopman Method** bypasses this by:

1. Learning a **linear embedding** of nonlinear dynamics from trajectory data (Koopman operator)
2. Projecting lifted dynamics onto a **finite-dimensional subspace**
3. Decomposing the non-unitary propagator into **parallel spectral channels**
4. Executing each channel as a **shallow quantum circuit**

## Implementation Pipeline

### Step 1: Learn Koopman Observables

```python
def learn_koopman_observables(trajectory_data, n_observables, n_features):
    """Learn Koopman observables from trajectory data.
    
    Uses Extended Dynamic Mode Decomposition (EDMD) or neural network
    to find observables that linearize the dynamics.
    """
    X = trajectory_data[:-1]  # state at time t
    Y = trajectory_data[1:]   # state at time t+1
    
    # Lift to observable space
    Psi_X = lift_to_observables(X, n_observables, n_features)
    Psi_Y = lift_to_observables(Y, n_observables, n_features)
    
    # Solve Koopman operator: K = Psi_Y @ pinv(Psi_X)
    K = Psi_Y @ np.linalg.pinv(Psi_X)
    
    return K, Psi_X.shape[1]  # operator + observable dimension
```

### Step 2: Decompose into Spectral Channels

```python
def decompose_spectral_channels(K, dt):
    """Decompose Koopman operator into parallel spectral channels.
    
    For non-unitary evolution: U = exp(K * dt)
    Decompose via eigendecomposition: K = V @ Lambda @ V_inv
    Each eigenvalue -> one quantum channel
    """
    eigenvalues, eigenvectors = np.linalg.eig(K)
    
    # Compute evolution operator
    U = eigenvectors @ np.diag(np.exp(eigenvalues * dt)) @ np.linalg.inv(eigenvectors)
    
    # Each column of U is a spectral channel
    channels = []
    for i in range(len(eigenvalues)):
        channel = {
            'eigenvalue': eigenvalues[i],
            'eigenvector': eigenvectors[:, i],
            'weight': U[:, i],
            'circuit_depth': estimate_circuit_depth(eigenvalues[i])
        }
        channels.append(channel)
    
    return channels
```

### Step 3: Quantum Circuit Implementation

```python
def build_quantum_koopman_circuit(channels, n_qubits):
    """Build parallel quantum circuits for Koopman evolution.
    
    Each spectral channel -> shallow circuit with parameterized gates.
    Total depth = O(log(n_observables)) per channel.
    """
    circuits = []
    for channel in channels:
        # Encode initial state
        qc = QuantumCircuit(n_qubits)
        
        # Apply spectral channel evolution
        # Eigenvalue -> rotation angle
        theta = np.angle(channel['eigenvalue'])
        for q in range(n_qubits):
            qc.rz(theta, q)
        
        # Eigenvector -> entangling pattern
        apply_eigenvector_pattern(qc, channel['eigenvector'])
        
        circuits.append(qc)
    
    return circuits
```

## Practical Boundary

The method identifies a **hardware-validated boundary** for quantum-amenable nonlinear dynamics:

| Nonlinearity Level | Limiting Factor | Quantum Performance |
|-------------------|-----------------|-------------------|
| **Weak** | Hardware noise | Limited by decoherence |
| **Moderate** | Koopman finite-dim approximation | Captures dominant patterns |
| **Strong** | Koopman representation insufficient | Classical methods better |

## Performance Characteristics

- **Classical overhead**: Polynomial in observable dimension
- **Quantum overhead**: Polynomial in circuit size and qubit count
- **Parallel circuits**: Up to 32 parallel circuits demonstrated (10 qubits each)
- **Shallow depth**: O(log(n_observables)) per channel

## Validated Applications

1. **Reaction-diffusion dynamics** (chemical pattern formation)
2. **Fluid motion on sphere** (atmospheric/ocean dynamics)
3. **Gulf Stream currents** (satellite-derived observations)

## When to Use

- Simulating **moderately nonlinear** dynamical systems on NISQ hardware
- Systems where Koopman linearization is effective
- Problems requiring **long-time evolution** where classical integration is expensive
- Real-world systems with trajectory data available for learning observables

## Activation
koopman quantum, quantum simulation nonlinear, koopman operator, quantum dynamics, data-driven quantum, spectral channels, reaction-diffusion quantum