---
name: lie-group-diffusion-quantum-synthesis
description: "Lie Group Diffusion Models for hardware-aware quantum circuit synthesis — jointly optimizing continuous gate parameters on SU(2) and discrete circuit topology using hybrid diffusion models."
trigger_words: "quantum circuit synthesis, lie group diffusion, hardware-aware compilation, quantum gate optimization, SU(2) gates, unitary synthesis, quantum compiler, circuit topology"
---

# Lie Group Diffusion Models for Quantum Circuit Synthesis

## Overview

This skill implements the methodology from arXiv:2606.29636 for **hardware-aware quantum circuit synthesis** using Lie Group Diffusion Models. The key insight is that quantum circuit synthesis has a natural hybrid structure: single-qubit gates are continuous variables on the Lie group SU(2), while entangling gate placement is discrete. This methodology jointly optimizes both.

## Core Methodology

### Problem Formulation

Given a target unitary U_target ∈ SU(2^n), find a quantum circuit C such that:
- C ≈ U_target (within fidelity threshold)
- C respects hardware connectivity constraints
- C has minimal depth and gate count

### Hybrid Structure

1. **Continuous component**: Single-qubit gates parameterized as elements of SU(2)
   - Each gate g = exp(i·θ·σ) where σ is a Pauli operator
   - Parameter space: θ ∈ ℝ³ for arbitrary single-qubit rotations

2. **Discrete component**: Entangling gate placement
   - Binary decision: place CNOT/cz between connected qubits or not
   - Constrained by hardware coupling map

### Lie Group Diffusion Process

#### Forward Process (noise addition)
```
q_t = forward_diffusion(q_0, t)
```
- For SU(2) gates: Add noise on the manifold using exponential map
  - q_t = exp(ξ_t) · q_0 where ξ_t ∈ su(2) (Lie algebra)
  - ξ_t ~ N(0, σ²(t)·I) projected onto su(2)

- For discrete topology: Mask entangling gates with probability p(t)

#### Reverse Process (denoising/synthesis)
```
q_{t-1} = reverse_diffusion(q_t, t, ε_θ(q_t, t))
```
- Neural network ε_θ predicts the denoised gate parameters
- For SU(2): Predict Lie algebra element ξ, then exp(ξ) gives rotation
- For discrete: Predict probability of each possible entangling gate

### Hardware-Awareness

The synthesis process incorporates hardware constraints:
- **Connectivity graph**: Only place entangling gates on physical couplings
- **Gate fidelities**: Weight gate selection by calibrated error rates
- **Crosstalk model**: Penalize simultaneous gates on neighboring qubits

## Implementation

### SU(2) Parameterization

```python
import numpy as np
from scipy.linalg import expm

def su2_to_params(U):
    """Convert SU(2) matrix to Lie algebra parameters."""
    # U = exp(i * θ · σ)
    # Extract θ from U using matrix logarithm
    log_U = np.real(np.log(np.linalg.det(U)) / 2j)
    theta = np.arccos(np.real(np.trace(U)) / 2)
    if np.sin(theta) < 1e-10:
        return np.array([0, 0, 0])
    axis = np.array([
        -np.imag(U[0,1]),
        np.imag(U[0,0] - U[1,1])/2,
        np.imag(U[0,0] + U[1,1])/2
    ]) / np.sin(theta)
    return theta * axis

def params_to_su2(theta):
    """Convert Lie algebra parameters to SU(2) matrix."""
    norm = np.linalg.norm(theta)
    if norm < 1e-10:
        return np.eye(2, dtype=complex)
    axis = theta / norm
    return expm(1j * norm * np.dot(axis, paulis))
```

### Diffusion Model Architecture

```python
class LieGroupDiffusionModel:
    """Diffusion model for quantum circuit synthesis on SU(2) manifolds."""
    
    def __init__(self, n_qubits, hardware_map, max_depth=20):
        self.n_qubits = n_qubits
        self.hardware_map = hardware_map  # adjacency matrix
        self.max_depth = max_depth
        
    def forward_process(self, circuit, t):
        """Add noise to circuit at time step t."""
        noisy_circuit = []
        for gate in circuit:
            if gate.type == 'single':
                # Add noise on SU(2) manifold
                noise = np.random.normal(0, self.sigma(t), 3)
                noisy_params = gate.params + noise
                noisy_circuit.append(SingleQubitGate(noisy_params))
            elif gate.type == 'entangling':
                # Mask with probability
                if np.random.random() < self.mask_prob(t):
                    continue  # Remove gate
                noisy_circuit.append(gate)
        return noisy_circuit
    
    def reverse_step(self, noisy_circuit, t):
        """Predict denoised circuit from noisy input."""
        # Neural network predicts denoised parameters
        pred = self.neural_net(noisy_circuit, t)
        return pred
```

### Training Loop

```python
def train_model(model, target_unitaries, n_steps=10000):
    """Train the Lie group diffusion model."""
    optimizer = Adam(model.parameters(), lr=1e-4)
    
    for step in range(n_steps):
        # Sample target unitary
        U_target = sample_target_unitary()
        
        # Sample random time step
        t = np.random.uniform(0, 1)
        
        # Forward process
        noisy_circuit = model.forward_process(U_target, t)
        
        # Predict denoised circuit
        pred_circuit = model.reverse_step(noisy_circuit, t)
        
        # Loss: fidelity between predicted and target
        loss = 1 - fidelity(pred_circuit, U_target)
        
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
```

## Workflow

### Step 1: Define Target Unitary
Specify the quantum operation to synthesize (e.g., Toffoli gate, QFT).

### Step 2: Load Hardware Constraints
Provide the target quantum device's connectivity map and gate fidelities.

### Step 3: Run Diffusion Synthesis
Generate circuit by iteratively denoising from pure noise:
```
circuit = sample_noise()
for t in reversed(time_steps):
    circuit = model.reverse_step(circuit, t)
    circuit = project_to_hardware(circuit, hardware_map)
```

### Step 4: Post-Processing
- Remove identity gates
- Merge adjacent single-qubit gates
- Optimize gate sequence for depth

### Step 5: Verification
Verify synthesized circuit against target:
```
fidelity = |Tr(U_target† · U_synthesized)| / 2^n
assert fidelity > 0.99
```

## Key Insights

1. **Manifold-aware noise**: Adding noise directly on SU(2) preserves unitarity
2. **Hybrid optimization**: Treating continuous and discrete aspects separately enables efficient search
3. **Hardware awareness**: Incorporating device constraints during synthesis avoids costly post-compilation

## Applications

- Quantum compiler optimization
- Hardware-specific circuit synthesis
- Quantum algorithm compilation
- NISQ-era circuit optimization

## Related Skills

- `quantum-compiler-routing` - Qubit mapping and routing
- `quantum-circuit-spectral-analysis` - Circuit analysis via harmonic analysis
- `pulse-level-quantum-computing` - Pulse-level quantum control

## References

- arXiv:2606.29636 — Lie Group Diffusion Models for Hardware-Aware Quantum Circuit Synthesis
