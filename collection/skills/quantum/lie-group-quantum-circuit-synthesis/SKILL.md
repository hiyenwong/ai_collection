---
name: lie-group-quantum-circuit-synthesis
description: "Hardware-aware quantum circuit synthesis using Lie group diffusion models on SU(2) manifold. Combines discrete skeleton selection with continuous gate parameter generation via heat kernel denoising. Use when: compiling quantum circuits, synthesizing hardware-aware quantum gates, optimizing circuit fidelity vs complexity. Source: arXiv:2606.29636 (2026-06-28)."
activation: quantum circuit synthesis, lie group diffusion, hardware-aware compilation, SU(2) manifold, quantum gate generation, circuit skeleton
---

# Lie Group Diffusion for Hardware-Aware Quantum Circuit Synthesis

## Problem Statement

Quantum circuit synthesis must satisfy two competing requirements:
1. **Continuous gate parameters**: Single-qubit gates live on the SU(2) Lie group manifold
2. **Discrete circuit structure**: Entangling gate topology depends on hardware connectivity

Traditional approaches either ignore manifold geometry (treating gates as Euclidean) or ignore hardware constraints (assuming all-to-all connectivity).

## Solution Architecture

The method uses a **two-component generative model**:

### Component 1: Circuit Skeleton Selector
- **Purpose**: Select discrete entangling gate structure
- **Input**: Target unitary, hardware connectivity graph
- **Output**: Circuit skeleton (which qubits connect, in what order)
- **Constraint**: Only generates skeletons valid for target hardware topology

### Component 2: SU(2) Lie Group Diffusion Model
- **Purpose**: Generate continuous single-qubit gate parameters
- **Key insight**: Single-qubit gates form SU(2) ≅ S³ (3-sphere), not Euclidean space
- **Method**: 
  - Forward process: Add noise using heat kernel on SU(2) manifold
  - Reverse process: Learn denoising that respects manifold geometry
  - Uses quaternion representation for numerically stable SU(2) operations

## Quaternion Representation of SU(2)

```python
import numpy as np

def gate_to_quaternion(U):
    """Convert 2x2 SU(2) matrix to quaternion (w, x, y, z)"""
    a = np.real(U[0,0])
    b = np.imag(U[0,0])
    c = np.real(U[0,1])
    d = np.imag(U[0,1])
    return np.array([a, b, c, d])

def quaternion_to_gate(q):
    """Convert quaternion back to SU(2) matrix"""
    w, x, y, z = q / np.linalg.norm(q)
    return np.array([[w+1j*z, y+1j*x],
                     [-y+1j*x, w-1j*z]])
```

## Heat Kernel Denoising on SU(2)

```python
def heat_kernel_denoise(noisy_quaternion, target_unitary, timestep):
    """Denoise on SU(2) manifold using heat kernel"""
    def geodesic_dist(q1, q2):
        dot = np.clip(np.dot(q1, q2), -1, 1)
        return np.arccos(abs(dot))
    
    target_q = gate_to_quaternion(target_unitary)
    noise_scale = np.sqrt(timestep)
    
    # Project gradient onto tangent space
    grad = target_q - noisy_quaternion
    grad -= np.dot(grad, noisy_quaternion) * noisy_quaternion
    
    # Update along geodesic
    step = noise_scale * grad / (np.linalg.norm(grad) + 1e-8)
    updated = noisy_quaternion + step
    return updated / np.linalg.norm(updated)
```

## Hardware-Aware Fidelity-Complexity Tradeoff

```python
def hardware_aware_score(circuit, hardware_topology):
    """Score circuit based on hardware constraints"""
    fidelity = compute_fidelity(circuit, target)
    native_penalty = sum(1 for g in circuit if not is_native(g, hardware_topology))
    swap_count = count_swaps(circuit, hardware_topology)
    complexity = len(circuit)
    return fidelity / (1 + native_penalty + swap_count + 0.1 * complexity)
```

## Training Pipeline

1. **Generate training data**: Sample random unitaries + compute optimal circuits
2. **Train skeleton selector**: Predict discrete structure from unitary features
3. **Train diffusion model**: Learn to denoise SU(2) quaternions conditioned on skeleton
4. **Fine-tune**: Optimize for hardware-specific fidelity metrics

## Application Scenarios

- **NISQ compilation**: Synthesize circuits respecting connectivity constraints
- **Gate decomposition**: Convert abstract unitaries to native gate sets
- **Circuit optimization**: Trade fidelity for circuit depth
- **Cross-platform compilation**: Port circuits between different quantum hardware

## Advantages Over Traditional Methods

| Method | Manifold Awareness | Hardware Awareness | Scalability |
|--------|-------------------|-------------------|-------------|
| Standard decomposition | ❌ Euclidean | ❌ | Good |
| Optimal control | ✅ | ❌ | Poor |
| RL-based | ✅ | ✅ | Limited |
| **Lie Group Diffusion** | ✅ | ✅ | **Good** |

## Trigger Patterns

- Compiling quantum circuits for specific hardware
- Optimizing quantum gate sequences
- Synthesizing parameterized quantum circuits
- Cross-platform quantum circuit compilation
- Hardware-aware quantum algorithm implementation