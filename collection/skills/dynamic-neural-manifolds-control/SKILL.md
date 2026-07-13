---
name: dynamic-neural-manifolds-control
description: >
  Dynamic neural manifold architecture for flexible closed-loop control on
  neuromorphic hardware (SpiNNaker 2). Ring network with three control knobs
  (heterogeneous inhibition, gain modulation, transient currents) enables
  predictable subspace rotation and trajectory steering for explainable
  neuromorphic robotic control.
---

# Dynamic Neural Manifolds for Neuromorphic Closed-Loop Control

## Paper

**Title**: Dynamic neural manifolds for flexible closed-loop control on neuromorphic hardware  
**Authors**: Oskar von Seeler, Christian Tetzlaff, Andrew B. Lehr  
**arXiv**: 2607.07373v1 (2026-07-08)  
**Link**: https://arxiv.org/abs/2607.07373

## Core Insight

Sequential neural activity in biological circuits evolves along dynamic,
low-dimensional manifolds. The geometric features of these manifolds (subspace
orientation, trajectory speed, trajectory shape) can be controlled by three
simple circuit mechanisms acting as "control knobs":

1. **Heterogeneous inhibition** → subspace rotation (behavioral switching)
2. **Multiplicative gain** → trajectory speed (movement timing)
3. **Additive transient currents** → trajectory shape (bump width)

This maps low-level circuit architecture to high-level geometric features,
enabling explainable, predictable autonomous system design.

## Architecture

### Ring Network

N neurons arranged in a ring with asymmetric recurrent connectivity → stable
activity bump that progresses around the ring → oscillatory neural sequences.

```
x_i(t+1) = Σ_j W_ji · r_j(t) + I(t)
r_i(t+1) = F(r_i(t) + 1/τ · (-r_i(t) + p_i(t) · S(t) · x_i(t+1)))
```

### Three Control Knobs

| Control | Mechanism | Effect | Geometric Mapping |
|---------|-----------|--------|-------------------|
| Shape (I) | Additive current | Bump size / # active neurons | Trajectory radius |
| Speed (S) | Multiplicative gain | Bump propagation speed | Trajectory velocity |
| Subspace (p_inh) | Random silencing via inhibitory ensembles | Subspace rotation | Angle = arccos(1 - p_inh) |

### Closed-Loop Control

```
[External Policy] → [Control Parameters: I, S, p_inh]
    ↓
[SpiNNaker 2 Ring Network (500 neurons, 20% connectivity)]
    ↓
[Spike Output] → [Linear Readout] → [Motor Control]
    ↓
[Environment / Robot] → [Sensory Feedback] → [External Policy]
```

## SpiNNaker 2 Implementation

Key optimizations for neuromorphic hardware:

1. **Spike-based communication**: Rates converted to spikes (probability r(t)/2)
2. **Sparse connectivity**: 50% sparsity with circulant weight matrix compression
3. **Circulant structure**: Store single weight row + sparsity bitmask (8-bit signed + exponent)
4. **HostIF streaming**: Real-time control parameter streaming, arbitrary-length simulation
5. **Memory management**: 32 neurons/PE, 128 KB SRAM per core

### Closed-Loop Latency

```
t₀: neurons spike → t₀+1: spike streamer → t₀+2: host receives → t₀+3: new control
```

Full control loop: ~3 timesteps at 1ms resolution.

## Mathematical Properties

### Subspace Rotation Angle

When fraction p_inh of neurons are silenced by an inhibitory ensemble:

```
angle = arccos(1 - p_inh)
```

At p_inh = 0.8 (80% silenced): angle ≈ arccos(0.2) ≈ 78.5°

### Speed Control

Multiplicative gain S amplifies all inputs proportionally:
- S = 1: baseline speed
- S > 1: faster sequence propagation
- S < 1: slower propagation

### Shape Control

Additive current I modulates total active neurons:
- I > 0: larger bump, wider trajectory
- I < 0: smaller bump, narrower trajectory

## When to Use

- **Explainable neuromorphic control** where internal state must be interpretable
- **Real-time closed-loop robotic control** on SpiNNaker 2 or similar hardware
- **Motor control for multi-DOF systems** (humanoid robots, bio-inspired robots)
- **Behavioral switching** via subspace rotation
- **Biological neural dynamics testbed** for investigating how circuits translate
  spatiotemporal dynamics into goal-directed behavior

## Implementation Pattern

```python
import numpy as np

class DynamicManifoldRing:
    """Ring network with dynamic neural manifold control."""
    
    def __init__(self, n_neurons=500, connectivity=0.2, tau=10):
        self.N = n_neurons
        self.connectivity = connectivity
        self.tau = tau
        
        # Circulant weight matrix (asymmetric for bump propagation)
        self.w_row = self._init_circulant_weights(n_neurons, connectivity)
        self.sparsity_mask = self._init_sparsity(n_neurons, connectivity)
        
        # Control parameters
        self.speed = 1.0      # Multiplicative gain S
        self.shape = 0.0      # Additive current I
        self.subspace = 0     # Active inhibitory ensemble
        
        # State
        self.rates = np.zeros(n_neurons)
        self.inhibitory_ensembles = self._init_ensembles(n_neurons)
    
    def step(self, speed=1.0, shape=0.0, subspace=0, external_input=None):
        """One timestep with control parameters."""
        self.speed = speed
        self.shape = shape or 0.0
        self.subspace = subspace
        
        # Apply subspace inhibition
        p_i = self.inhibitory_ensembles[subspace]  # 1 = active, 0 = silenced
        
        # Synaptic input
        x = self._circulant_convolve(self.rates)
        if external_input is not None:
            x += external_input
        
        # Rate update with control
        self.rates = self._clamp(
            self.rates + (1.0 / self.tau) * (
                -self.rates + p_i * speed * x + shape
            )
        )
        
        return self.rates.copy()
    
    def _circulant_convolve(self, rates):
        """Efficient circulant matrix-vector product."""
        return np.fft.ifft(np.fft.fft(self.w_row) * np.fft.fft(rates)).real
    
    def _init_ensembles(self, n, n_ensembles=32, fraction=0.4):
        """Create inhibitory ensembles for subspace rotation."""
        ensembles = np.ones((n_ensembles, n))
        for e in range(n_ensembles):
            silenced = np.random.choice(n, size=int(n * (1 - fraction)), replace=False)
            ensembles[e, silenced] = 0
        return ensembles
    
    def get_manifold_state(self, n_pcs=2):
        """Project current state onto principal components."""
        from sklearn.decomposition import PCA
        # Would use full trajectory history for PCA
        pass
    
    def _clamp(self, x):
        return np.clip(x, 0, 1)
```

## Trigger Words

dynamic neural manifold, neuromorphic closed-loop control, SpiNNaker 2,
ring network, subspace rotation, bump attractor, heterogeneous inhibition,
multiplicative gain, trajectory control, explainable neuromorphic,
behavioral switching, motor control, Lehr 2024 2025
