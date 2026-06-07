---
name: dark-signals-brain-hamiltonian
description: "Dark Signals framework — physics-informed complex-valued brain network dynamics using Hamiltonian mechanics. Augments observed fMRI/EEG signals with latent conjugate momenta via Hilbert transform, yielding Schrödinger-like equations for whole-brain dynamics. Activation: dark signals, hamiltonian brain, complex-valued brain dynamics, hilbert transform brain, brain network prediction, effective connectivity"
tags: ["brain-network", "neural-dynamics", "physics-informed", "complex-valued", "hamiltonian", "fMRI"]
related_skills: ["brain-connectivity-analysis", "geometric-brain-dynamics-mapping", "brain-dit-fmri-foundation-model"]
---

# Dark Signals in the Brain: Complex-Valued Brain Network Dynamics

Based on arXiv:2509.24715 (September 2025) — "Dark Signals in the Brain: Augment Brain Network Dynamics to the Complex-valued Field"

## Overview

This paper develops a **physics-informed, data-driven framework** that lifts whole-brain activity to the complex-valued field. The key insight: by augmenting observed brain signals (generalized coordinates) with latent "dark signals" that play the role of **conjugate momenta** in a Hamiltonian system, brain dynamics can be modeled more compactly and accurately.

## Core Concept

### Hamiltonian Formulation of Brain Dynamics

In Hamiltonian mechanics, a conservative system is described by:
```
H(q, p) = kinetic_energy(p) + potential_energy(q)
dq/dt = ∂H/∂p
dp/dt = -∂H/∂q
```

For brain networks:
- **q** = observed signals (fMRI BOLD, EEG)
- **p** = "dark signals" (latent conjugate momenta, unobserved)
- **H** = whole-brain Hamiltonian

### Hilbert Transform as Optimal Augmentation

The paper proves that the **Hilbert transform** provides the optimal augmentation:
```
z(t) = q(t) + i·H{q(t)}
```
Where H{·} is the Hilbert transform, yielding a complex-valued signal z(t).

This leads to a **Schrödinger-like equation**:
```
i·∂z/∂t = Ĥ·z
```
Where Ĥ is a complex-valued Hamiltonian operator governing brain dynamics.

## Key Results

| Metric | Real-Valued | Complex-Valued (Dark Signals) | Improvement |
|--------|------------|-------------------------------|-------------|
| Linear prediction (short-horizon) | r = 0.12 | **r = 0.82** | +0.70 |
| Nonlinear nonequilibrium dynamics | r = 0.47 | **r = 0.88** | +0.41 |
| Structure-function coupling | Baseline | **Strengthened** | Significant |
| Hierarchical timescales | Partial | **Fully recovered** | Complete |

## Mathematical Framework

### Complex-Valued Brain State

```python
import numpy as np
from scipy.signal import hilbert

def complex_augment(signals):
    """
    Augment real brain signals with dark signals via Hilbert transform.

    Args:
        signals: [T, N] real-valued brain signals (T timesteps, N regions)
    Returns:
        z: [T, N] complex-valued augmented signals
    """
    # Hilbert transform creates analytic signal
    z = hilbert(signals, axis=0)
    return z  # z = q + i·H{q}


def compute_hamiltonian(z, dt=1.0):
    """
    Estimate complex Hamiltonian operator from augmented signals.
    Ĥ ≈ i·(∂z/∂t)·z⁺  (pseudo-inverse)
    """
    # Numerical time derivative
    dz_dt = np.diff(z, axis=0) / dt

    # Hamiltonian estimation via least squares
    # dz/dt = -i·Ĥ·z  →  Ĥ = i·dz/dt·z⁺
    H_hat = 1j * np.linalg.lstsq(z[:-1], dz_dt, rcond=None)[0]
    return H_hat
```

### Schrödinger-like Dynamics

```python
def propagate_brain_dynamics(z0, H_hat, steps, dt=1.0):
    """
    Propagate complex-valued brain dynamics using estimated Hamiltonian.

    i·∂z/∂t = Ĥ·z  →  z(t+dt) = exp(-i·Ĥ·dt)·z(t)

    Args:
        z0: initial complex state [N]
        H_hat: estimated Hamiltonian [N, N]
        steps: number of timesteps
        dt: timestep size
    Returns:
        trajectory: [steps+1, N] complex-valued trajectory
    """
    # Matrix exponential propagator
    U = scipy.linalg.expm(-1j * H_hat * dt)

    trajectory = np.zeros((steps + 1, z0.shape[0]), dtype=complex)
    trajectory[0] = z0

    for t in range(steps):
        trajectory[t + 1] = U @ trajectory[t]

    return trajectory


def predict_future(observed, H_hat, horizon):
    """
    Predict future brain activity using complex-valued dynamics.
    """
    # Augment with Hilbert transform
    z = complex_augment(observed)

    # Use last state as initial condition
    z0 = z[-1]

    # Propagate
    future = propagate_brain_dynamics(z0, H_hat, horizon)

    # Return real part (observable signal)
    return np.real(future)
```

### Effective Connectivity from Complex Hamiltonian

```python
def extract_effective_connectivity(H_hat):
    """
    Extract directed effective connectivity from complex Hamiltonian.

    The imaginary part of Ĥ encodes directed connections:
    - Re(Ĥ_ij) = symmetric coupling
    - Im(Ĥ_ij) = directed influence (i → j)
    """
    # Symmetric (undirected) coupling
    symmetric = np.real(H_hat + H_hat.conj().T) / 2

    # Directed (asymmetric) influence
    directed = np.imag(H_hat - H_hat.conj().T) / 2

    return symmetric, directed


def connectivity_reconfiguration(H_rest, H_task):
    """
    Analyze how connectivity reconfigures from rest to task.

    The paper finds: global rescaling + targeted rewiring
    """
    # Global rescaling factor
    scale = np.linalg.norm(H_task) / np.linalg.norm(H_rest)

    # Normalized task connectivity
    H_task_normalized = H_task / scale

    # Targeted rewiring (residual after rescaling)
    rewiring = H_task_normalized - H_rest

    return scale, rewiring
```

## Applications

### 1. Brain State Prediction
- Short-horizon prediction of fMRI/EEG dynamics
- Correlation improves from 0.12 to 0.82 (linear regime)
- Nonlinear prediction improves from 0.47 to 0.88

### 2. Structure-Function Coupling
- Complex-valued model strengthens coupling between structural connectome and functional dynamics
- Better explains how anatomy constrains function

### 3. Hierarchical Timescales
- Recovers intrinsic timescale hierarchy across brain regions
- Sensory areas: fast dynamics; association areas: slow dynamics

### 4. Directed Effective Connectivity
- Biologically plausible directed connections
- Varies systematically with age
- Reconfigures from rest to task via global rescaling + targeted rewiring

## Implementation Pipeline

```python
class DarkSignalsBrainModel:
    """
    Complete dark signals pipeline for brain network analysis.
    """
    def __init__(self, structural_connectome=None):
        self.structural = structural_connectome
        self.H_hat = None
        self.scale = None
        self.rewiring = None

    def fit(self, fmri_data, dt=2.0):
        """
        Fit the complex-valued brain dynamics model.

        Args:
            fmri_data: [T, N] fMRI time series
            dt: TR (repetition time) in seconds
        """
        # Step 1: Complex augmentation via Hilbert transform
        z = complex_augment(fmri_data)

        # Step 2: Estimate Hamiltonian
        self.H_hat = compute_hamiltonian(z, dt)

        # Step 3: Extract connectivity
        self.symmetric, self.directed = extract_effective_connectivity(self.H_hat)

        return self

    def predict(self, observed, horizon):
        """Predict future brain activity."""
        return predict_future(observed, self.H_hat, horizon)

    def fit_task(self, rest_data, task_data, dt=2.0):
        """
        Fit rest and task conditions, analyze reconfiguration.
        """
        # Fit rest
        z_rest = complex_augment(rest_data)
        H_rest = compute_hamiltonian(z_rest, dt)

        # Fit task
        z_task = complex_augment(task_data)
        H_task = compute_hamiltonian(z_task, dt)

        # Analyze reconfiguration
        self.scale, self.rewiring = connectivity_reconfiguration(H_rest, H_task)

        return H_rest, H_task

    def analyze_age_effects(self, data_by_age):
        """
        Analyze how directed connectivity varies with age.
        """
        age_effects = {}
        for age_group, data in data_by_age.items():
            model = self.__class__()
            model.fit(data)
            age_effects[age_group] = model.directed
        return age_effects
```

## Pitfalls

1. **Signal Stationarity**: Hilbert transform assumes quasi-stationary signals. For non-stationary fMRI, use sliding window approach.
2. **Edge Effects**: Hilbert transform has edge artifacts. Use padding or discard boundary timesteps.
3. **Hamiltonian Rank**: The estimated Ĥ may be ill-conditioned. Use regularization (ridge regression) or SVD truncation.
4. **Interpretation**: The "dark signals" are mathematical constructs (conjugate momenta), not directly measurable physical quantities.
5. **Linear vs Nonlinear**: The Schrödinger-like equation is linear. For nonlinear dynamics, use kernel methods or neural ODEs.

## Verification Steps

1. Verify prediction correlation > 0.8 on held-out data
2. Check that directed connectivity is asymmetric (not symmetric)
3. Confirm hierarchical timescales match literature (sensory < association)
4. Validate structure-function coupling improvement over real-valued baseline
5. Test age-related changes in directed connectivity

## Related Work

- Geometric Basis Functions (GBF) for brain dynamics mapping
- Brain-DiT foundation model for fMRI
- Structure-function coupling analysis in connectomics

## References

- Zhang, J., Qian, C., Lu, W., Deco, G., Ding, W., & Feng, J. (2025). *Dark Signals in the Brain: Augment Brain Network Dynamics to the Complex-valued Field.* arXiv:2509.24715 [q-bio.NC].