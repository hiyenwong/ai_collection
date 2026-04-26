---
name: koopman-representation-learning
description: "Koopman operator theory for learning eigenfunctions from observations at arbitrary, non-vanishing time intervals. Addresses aliasing from oscillatory dynamics and sampling patterns, with phase alignment near true frequencies. Use for: Koopman operator learning, dynamical system analysis, data assimilation, irregular sampling, eigenfunction identification. Activation: Koopman operator, eigenfunction learning, dynamical systems, irregular sampling, data assimilation."
---

# Koopman Representation Learning

Koopman operator theory formulation for learning eigenfunctions from observations at arbitrary, non-vanishing time intervals with aliasing analysis and optimization-based approach.

## Overview

This methodology enables:
- Learning Koopman eigenfunctions from sparse/irregular observations
- Handling non-vanishing time intervals between samples
- Understanding and mitigating aliasing effects
- Phase alignment for accurate frequency identification

## Core Concepts

### Koopman Operator

```
Linear operator K acting on observable functions:

K g(x_t) = g(x_{t+Δt})

Where:
- x_t: system state at time t
- g: observable function
- Δt: time interval (can be non-vanishing)
```

### Eigenfunction Decomposition

```
K φ_j = λ_j φ_j

Where:
- φ_j: Koopman eigenfunctions
- λ_j = exp(ω_j Δt): eigenvalues
- ω_j: continuous-time eigenfrequencies
```

### Learning Problem

```
Given: Observations {(x_{t_k}, x_{t_{k+1}})} with arbitrary Δt_k = t_{k+1} - t_k
Find: Eigenfunctions φ and eigenvalues λ that minimize prediction error
```

## Mathematical Framework

### Optimization Formulation

```
min_{φ, ω} Σ_k ||φ(x_{t_{k+1}}) - exp(i ω Δt_k) φ(x_{t_k})||²

Subject to:
- φ are nonlinear functions (typically neural networks)
- ω are real-valued frequencies
- Δt_k are known observation intervals
```

### Aliasing Effects

```
Aliasing occurs when:
exp(i ω Δt) = exp(i (ω + 2πn/Δt) Δt) for integer n

This creates ambiguity:
- True frequency: ω
- Aliased frequencies: ω + 2πn/Δt

Manifestation: Multiple local minima in loss landscape
```

### Phase Alignment

```
Near the true frequency ω*:
- Phase alignment creates steep loss valley
- Gradients point toward true frequency
- Optimization converges to correct solution

Far from true frequency:
- Aliasing creates local minima
- Gradient directions are misleading
- Careful initialization required
```

## Algorithm

### Step 1: Initialization

```python
def initialize_frequencies(observations, method='fft'):
    """
    Initialize frequency estimates.
    
    Methods:
    - 'fft': Fast Fourier Transform on interpolated data
    - 'dmd': Dynamic Mode Decomposition
    - 'random': Random initialization with multiple restarts
    """
    if method == 'fft':
        # Interpolate to regular grid
        regular_data = interpolate(observations)
        frequencies = fft_frequencies(regular_data)
    elif method == 'dmd':
        frequencies = dmd_frequencies(observations)
    
    return frequencies
```

### Step 2: Eigenfunction Learning

```python
def learn_eigenfunctions(observations, frequencies, max_iter=1000):
    """
    Learn Koopman eigenfunctions via optimization.
    """
    # Initialize neural network for eigenfunctions
    eigenfunctions = NeuralNetwork(input_dim=state_dim, output_dim=n_modes)
    
    optimizer = Adam(eigenfunctions.parameters(), lr=1e-3)
    
    for iteration in range(max_iter):
        total_loss = 0
        
        for (x_t, x_tnext, dt) in observations:
            # Compute eigenfunctions
            phi_t = eigenfunctions(x_t)
            phi_tnext = eigenfunctions(x_tnext)
            
            # Compute loss for each mode
            for j, omega in enumerate(frequencies):
                # Koopman prediction
                phi_pred = phi_t[:, j] * np.exp(1j * omega * dt)
                
                # Prediction error
                loss_j = torch.mean(torch.abs(phi_tnext[:, j] - phi_pred)**2)
                total_loss += loss_j
        
        # Backpropagation
        optimizer.zero_grad()
        total_loss.backward()
        optimizer.step()
        
        # Check convergence
        if converged(total_loss):
            break
    
    return eigenfunctions, frequencies
```

### Step 3: Frequency Refinement

```python
def refine_frequencies(observations, eigenfunctions, frequencies):
    """
    Refine frequency estimates using learned eigenfunctions.
    """
    refined_freqs = []
    
    for j, omega in enumerate(frequencies):
        # Compute phase differences
        phase_diffs = []
        for (x_t, x_tnext, dt) in observations:
            phi_t = eigenfunctions(x_t)[:, j]
            phi_tnext = eigenfunctions(x_tnext)[:, j]
            
            # Phase difference
            phase_diff = np.angle(phi_tnext / phi_t)
            phase_diffs.append(phase_diff / dt)
        
        # Refined frequency is mean of phase differences
        omega_refined = np.mean(phase_diffs)
        refined_freqs.append(omega_refined)
    
    return refined_freqs
```

## Irregular Sampling Benefits

### Breaking Aliasing

```python
def demonstrate_irregular_sampling():
    """
    Show that irregular sampling breaks aliasing symmetry.
    """
    # Regular sampling: aliased frequencies have same loss
    regular_losses = []
    for dt in [0.1, 0.1, 0.1]:  # Regular
        loss = compute_loss(omega_true + 2*np.pi/dt, dt)
        regular_losses.append(loss)
    
    # Irregular sampling: aliased frequencies have different losses
    irregular_losses = []
    for dt in [0.09, 0.11, 0.10]:  # Irregular
        loss = compute_loss(omega_true + 2*np.pi/dt, dt)
        irregular_losses.append(loss)
    
    # True frequency minimizes total loss with irregular sampling
    return irregular_losses
```

### Phase Cancellation

```
Irregular sampling causes aliased modes to:
- Have different effective frequencies
- Not constructively interfere
- Allow identification of true frequency
```

## Use Cases

### 1. Multimodal Data Assimilation

```
Application: Combining sensor data with different sampling rates
Challenge: Non-vanishing intervals between observations
Solution: Koopman eigenfunctions learned from arbitrary intervals
```

### 2. Sparse Observations

```
Application: Climate data with infrequent measurements
Challenge: Large, non-uniform time gaps
Solution: Optimization-based eigenfunction learning
```

### 3. Complex Dynamical Systems

```
Application: Fluid dynamics, biological systems
Challenge: High-dimensional nonlinear dynamics
Solution: Neural network eigenfunction approximation
```

## Parameters

| Parameter | Description | Typical Range |
|-----------|-------------|---------------|
| n_modes | Number of eigenfunctions | 5-50 |
| hidden_dim | Neural network hidden size | 64-512 |
| learning_rate | Optimizer learning rate | 1e-4 to 1e-2 |
| max_iter | Maximum iterations | 1000-10000 |

## Comparison: Extended DMD

| Aspect | Koopman (This) | Extended DMD |
|--------|----------------|--------------|
| Time intervals | Arbitrary | Regular |
| Aliasing handling | Explicit | Implicit |
| Irregular sampling | Supported | Not supported |
| Phase alignment | Used | Not used |

## Activation Keywords

- Koopman operator
- eigenfunction learning
- dynamical systems
- irregular sampling
- data assimilation
- aliasing
- phase alignment
- non-vanishing intervals

## Related Skills

- `data-driven-moving-horizon-estimation`: State estimation
- `physics-informed-state-space-forecasting`: State space models
- `neural-dynamics-autoregressive-flow-matching`: Neural dynamics

## References

- Paper: arXiv:2604.11715 (April 2026)
- Authors: Cho, Sowers
- Theory: Koopman operator theory
- Comparison: Generator Extended DMD (gEDMD)

## Example Usage

```
"Learn Koopman eigenfunctions from irregular observations"
"Apply Koopman theory to multimodal data assimilation"
"Handle aliasing in dynamical system identification"
"Use phase alignment for frequency identification"
```

## Code Template

```python
import torch
import torch.nn as nn
import numpy as np

class KoopmanEigenfunctionNet(nn.Module):
    def __init__(self, state_dim, n_modes, hidden_dim=128):
        super().__init__()
        self.network = nn.Sequential(
            nn.Linear(state_dim, hidden_dim),
            nn.ReLU(),
            nn.Linear(hidden_dim, hidden_dim),
            nn.ReLU(),
            nn.Linear(hidden_dim, n_modes * 2)  # Real and imaginary parts
        )
        self.n_modes = n_modes
    
    def forward(self, x):
        output = self.network(x)
        real = output[:, :self.n_modes]
        imag = output[:, self.n_modes:]
        return torch.complex(real, imag)

def koopman_loss(observations, eigenfunctions, frequencies):
    """Compute Koopman prediction loss."""
    loss = 0
    for x_t, x_tnext, dt in observations:
        phi_t = eigenfunctions(x_t)
        phi_tnext_actual = eigenfunctions(x_tnext)
        
        for j, omega in enumerate(frequencies):
            # Koopman evolution
            phi_tnext_pred = phi_t[:, j] * torch.exp(1j * omega * dt)
            
            # Prediction error
            loss += torch.mean(torch.abs(phi_tnext_actual[:, j] - phi_tnext_pred)**2)
    
    return loss
```

## Notes

- Requires careful initialization to avoid aliasing
- Irregular sampling helps break aliasing symmetry
- Phase alignment near true frequencies enables convergence
- Neural network eigenfunctions approximate nonlinear observables
- Scales to high-dimensional systems
