---
name: ng-nmm-brain-dynamics
description: "Next Generation Neural Mass Model (NG-NMM) framework for large-scale brain network spatiotemporal dynamics. Analyzes emergent patterns in whole-brain models using PING mechanism with 90 interconnected brain regions. Links anatomical connectivity to cross-frequency coupling and gamma oscillations. Based on arXiv:2512.03907."
category: ai_collection
tags: [neural-mass-models, brain-networks, spatiotemporal-dynamics, ping-mechanism, whole-brain-modeling, oscillations, gamma-rhythm]
---

# Next Generation Neural Mass Models for Brain Network Dynamics

## Overview

This skill implements the theoretical framework from **"Emergent Spatiotemporal Dynamics in Large-Scale Brain Networks with Next Generation Neural Mass Models"** (arXiv:2512.03907) by Rosa Maria Delicado, Gemma Huguet, and Pau Clusella.

Understanding the dynamics of large-scale brain models remains a central challenge due to the inherent complexity of these systems. This work explores the emergence of complex spatiotemporal patterns in a large-scale brain model composed of 90 interconnected brain regions coupled through empirically derived anatomical connectivity.

## Key Contributions

### 1. Next Generation Neural Mass Models (NG-NMM)

- Explicitly captures macroscopic gamma activity of coupled excitatory and inhibitory neural populations
- Implements PING (Pyramidal-Interneuronal Network Gamma) mechanism
- More biophysically grounded than classical neural mass models

### 2. Large-Scale Network Analysis

- 90 interconnected brain regions
- Empirically derived anatomical connectivity
- Homogeneous and heterogeneous state analysis

### 3. Dynamical Repertoire

- Broader dynamical repertoire than classical models
- Stability analysis via dispersion relations
- Lyapunov exponents for pattern characterization
- Frequency spectrum analysis

## Theoretical Framework

### Neural Mass Model Architecture

```
Each Brain Region (i = 1..90):
  ┌─────────────────────────────────────┐
  │  Excitatory Population (E)          │
  │    - Mean firing rate: ν_E          │
  │    - Post-synaptic potential: V_E   │
  │                                     │
  │  Inhibitory Population (I)          │
  │    - Mean firing rate: ν_I          │
  │    - Post-synaptic potential: V_I   │
  │                                     │
  │  PING Mechanism:                    │
  │    E → I (excitation)               │
  │    I → E (inhibition)               │
  └─────────────────────────────────────┘
           ↕ Anatomical Connectivity
```

### PING Mechanism (Pyramidal-Interneuronal Network Gamma)

The gamma oscillation generation through PING:

```
Phase 1: Pyramidal cells (E) fire
         ↓
Phase 2: Excite interneurons (I)
         ↓
Phase 3: Interneurons inhibit pyramidal cells
         ↓
Phase 4: Pyramidal cells recover, cycle repeats
```

**Key Parameters:**
- τ_E: Excitatory synaptic time constant (~2-4 ms)
- τ_I: Inhibitory synaptic time constant (~5-10 ms)
- g_EI: E→I coupling strength
- g_IE: I→E coupling strength
- g_EE: E→E self-excitation
- g_II: I→I self-inhibition

### Dynamical Equations

**Next Generation Model (simplified):**

```python
# Excitatory population dynamics
dV_E/dt = -(V_E - V_rest_E)/τ_mE + I_syn_E

# Inhibitory population dynamics
dV_I/dt = -(V_I - V_rest_I)/τ_mI + I_syn_I

# Synaptic currents
I_syn_E = g_EE * S_E * (V_E - V_syn_E) + g_IE * S_I * (V_E - V_syn_I)
I_syn_I = g_EI * S_E * (V_I - V_syn_E) + g_II * S_I * (V_I - V_syn_I)

# Synaptic dynamics (mean-field)
dS_E/dt = -S_E/τ_E + α_E * ν_E * (1 - S_E)
dS_I/dt = -S_I/τ_I + α_I * ν_I * (1 - S_I)

# Firing rate functions (sigmoid)
ν_E = ν_max_E / (1 + exp(-s_E * (V_E - θ_E)))
ν_I = ν_max_I / (1 + exp(-s_I * (V_I - θ_I)))
```

### Network Coupling

**Long-range connectivity between regions:**

```
dV_E^(i)/dt = [local dynamics] + Σ_j C_ij * S_E^(j) * (V_E^(i) - V_syn_E)

where C_ij is the anatomical connectivity matrix
```

## Implementation Guidelines

### Model Setup

```python
import numpy as np
from scipy.integrate import odeint

class NextGenNeuralMass:
    """
    Next Generation Neural Mass Model for brain region dynamics.
    Implements PING mechanism for gamma oscillations.
    """
    
    def __init__(self, n_regions=90, params=None):
        self.n_regions = n_regions
        
        # Default parameters
        self.params = {
            # Membrane time constants (ms)
            'tau_mE': 20.0,
            'tau_mI': 10.0,
            
            # Synaptic time constants (ms)
            'tau_E': 4.0,
            'tau_I': 16.0,
            
            # Synaptic reversal potentials (mV)
            'V_syn_E': 0.0,
            'V_syn_I': -80.0,
            'V_rest_E': -65.0,
            'V_rest_I': -65.0,
            
            # Coupling strengths
            'g_EE': 0.1,
            'g_EI': 0.4,
            'g_IE': 0.3,
            'g_II': 0.1,
            
            # Firing rate parameters
            'nu_max_E': 100.0,  # Hz
            'nu_max_I': 200.0,
            's_E': 0.5,
            's_I': 0.5,
            'theta_E': -50.0,
            'theta_I': -50.0,
            
            # Synaptic activation
            'alpha_E': 1.0,
            'alpha_I': 1.0,
        }
        
        if params:
            self.params.update(params)
        
        # Connectivity matrix (to be loaded empirically)
        self.connectivity = np.zeros((n_regions, n_regions))
        
        # State: [V_E, V_I, S_E, S_I] for each region
        self.state = None
    
    def firing_rate_E(self, V):
        """Excitatory firing rate (sigmoid)"""
        p = self.params
        return p['nu_max_E'] / (1 + np.exp(-p['s_E'] * (V - p['theta_E'])))
    
    def firing_rate_I(self, V):
        """Inhibitory firing rate (sigmoid)"""
        p = self.params
        return p['nu_max_I'] / (1 + np.exp(-p['s_I'] * (V - p['theta_I'])))
    
    def derivatives(self, state, t):
        """
        Compute derivatives for all regions.
        
        state: [V_E1, V_I1, S_E1, S_I1, V_E2, V_I2, ...]
        """
        n = self.n_regions
        p = self.params
        
        # Reshape state
        V_E = state[0::4]
        V_I = state[1::4]
        S_E = state[2::4]
        S_I = state[3::4]
        
        # Compute firing rates
        nu_E = self.firing_rate_E(V_E)
        nu_I = self.firing_rate_I(V_I)
        
        # Synaptic inputs from other regions
        I_conn_E = np.dot(self.connectivity, S_E)
        I_conn_I = np.dot(self.connectivity, S_I)
        
        # Local synaptic currents
        I_syn_E = (p['g_EE'] * S_E + p['g_IE'] * S_I) * (V_E - p['V_syn_E']) + \
                  p['g_EE'] * I_conn_E * (V_E - p['V_syn_E'])
        I_syn_I = (p['g_EI'] * S_E + p['g_II'] * S_I) * (V_I - p['V_syn_I']) + \
                  p['g_EI'] * I_conn_I * (V_I - p['V_syn_I'])
        
        # Derivatives
        dV_E = (-(V_E - p['V_rest_E']) + I_syn_E) / p['tau_mE']
        dV_I = (-(V_I - p['V_rest_I']) + I_syn_I) / p['tau_mI']
        dS_E = -S_E / p['tau_E'] + p['alpha_E'] * nu_E * (1 - S_E)
        dS_S_I = -S_I / p['tau_I'] + p['alpha_I'] * nu_I * (1 - S_I)
        
        # Flatten derivatives
        dstate = np.zeros_like(state)
        dstate[0::4] = dV_E
        dstate[1::4] = dV_I
        dstate[2::4] = dS_E
        dstate[3::4] = dS_I
        
        return dstate
    
    def simulate(self, t_span, initial_state=None):
        """
        Run simulation.
        
        Args:
            t_span: Time points for integration
            initial_state: Initial conditions (optional)
        
        Returns:
            solution array
        """
        if initial_state is None:
            # Small random perturbations from rest
            initial_state = np.zeros(4 * self.n_regions)
            initial_state[0::4] = self.params['V_rest_E']  # V_E
            initial_state[1::4] = self.params['V_rest_I']  # V_I
            initial_state[2::4] = 0.1  # S_E
            initial_state[3::4] = 0.1  # S_I
        
        solution = odeint(self.derivatives, initial_state, t_span)
        return solution
```

### Stability Analysis

```python
def analyze_stability(model, equilibrium_point):
    """
    Perform stability analysis around equilibrium.
    
    Returns:
        - eigenvalues: Stability eigenvalues
        - stable: Boolean indicating stability
        - oscillatory: Boolean indicating oscillatory instability
    """
    from scipy.linalg import eigvals
    
    # Compute Jacobian at equilibrium
    # (linearization required)
    J = compute_jacobian(model, equilibrium_point)
    
    eigenvalues = eigvals(J)
    
    # Stability: all eigenvalues have negative real parts
    stable = np.all(np.real(eigenvalues) < 0)
    
    # Oscillatory: complex eigenvalues with positive real parts
    oscillatory = np.any((np.real(eigenvalues) > 0) & (np.imag(eigenvalues) != 0))
    
    return eigenvalues, stable, oscillatory


def dispersion_relation(model, k_values):
    """
    Compute dispersion relation for spatial perturbations.
    
    Args:
        model: Neural mass model
        k_values: Wave number values to analyze
    
    Returns:
        Growth rates for each wave number
    """
    growth_rates = []
    
    for k in k_values:
        # Perturbation analysis
        # λ(k) determines stability of mode k
        lambda_k = compute_growth_rate(model, k)
        growth_rates.append(lambda_k)
    
    return np.array(growth_rates)
```

### Lyapunov Exponents

```python
def compute_lyapunov_exponents(model, t_span, n_exponents=10):
    """
    Compute largest Lyapunov exponents for the system.
    
    Positive exponents indicate chaos.
    """
    from scipy.integrate import solve_ivp
    
    # Initialize orthonormal basis
    n_dim = 4 * model.n_regions
    Q = np.eye(n_dim)[:, :n_exponents]
    
    lyapunov = np.zeros(n_exponents)
    
    def variational_equation(t, Y):
        """Combined state + tangent space evolution"""
        x = Y[:n_dim]
        
        # Jacobian at current state
        J = compute_jacobian_at_state(model, x)
        
        # Tangent vectors
        W = Y[n_dim:].reshape((n_dim, n_exponents))
        
        # Variational equation: dW/dt = J(x) * W
        dW = np.dot(J, W)
        
        return np.concatenate([model.derivatives(x, t), dW.flatten()])
    
    # Integration with periodic Gram-Schmidt reorthogonalization
    # ... (implementation details)
    
    return lyapunov
```

### Frequency Analysis

```python
def frequency_spectrum_analysis(solution, dt, region_indices=None):
    """
    Analyze frequency content of neural activity.
    
    Args:
        solution: Simulation output
        dt: Time step
        region_indices: Specific regions to analyze (None = all)
    
    Returns:
        Power spectral density for each region
    """
    from scipy.signal import welch
    
    if region_indices is None:
        region_indices = range(solution.shape[1] // 4)
    
    spectra = {}
    
    for idx in region_indices:
        # Extract V_E for region idx
        V_E = solution[:, idx * 4]
        
        # Compute power spectral density
        freqs, psd = welch(V_E, fs=1/dt, nperseg=1024)
        
        spectra[idx] = {'frequencies': freqs, 'psd': psd}
    
    return spectra


def cross_frequency_coupling(spectrum_low, spectrum_high):
    """
    Measure cross-frequency coupling between frequency bands.
    
    Used to detect amplitude modulation of gamma by slower rhythms.
    """
    # Modulation index calculation
    # ... (implementation)
    pass
```

## Analysis Workflows

### 1. Homogeneous State Analysis

```python
def find_homogeneous_states(model):
    """
    Find spatially uniform equilibrium states.
    
    Returns:
        List of (V_E, V_I, S_E, S_I) for each homogeneous state
    """
    from scipy.optimize import fsolve
    
    # Single region equations (without connectivity)
    def equations(vars):
        V_E, V_I, S_E, S_I = vars
        # ... (equations)
        return [f1, f2, f3, f4]
    
    # Find multiple solutions
    solutions = []
    for initial_guess in initial_guesses:
        sol = fsolve(equations, initial_guess)
        if is_valid_solution(sol):
            solutions.append(sol)
    
    return solutions
```

### 2. Pattern Formation Analysis

```python
def characterize_spatiotemporal_patterns(solution, n_regions):
    """
    Characterize emergent spatiotemporal patterns.
    
    Returns:
        - Pattern classification
        - Wavelength estimates
        - Propagation speed
        - Temporal frequency
    """
    # Extract V_E time series for all regions
    V_E_all = solution[:, ::4]  # Every 4th column
    
    # Spatial patterns
    spatial_patterns = extract_spatial_modes(V_E_all)
    
    # Temporal patterns
    temporal_patterns = extract_temporal_modes(V_E_all)
    
    # Classification
    pattern_type = classify_pattern(spatial_patterns, temporal_patterns)
    
    return {
        'type': pattern_type,
        'spatial': spatial_patterns,
        'temporal': temporal_patterns
    }
```

### 3. Cross-Frequency Coupling

```python
def analyze_cross_frequency_coupling(model, solution, dt):
    """
    Analyze how anatomical connectivity enables cross-frequency coupling.
    
    Key finding: Gamma amplitude modulated by slower rhythms.
    """
    # Filter signals into frequency bands
    delta = bandpass_filter(solution, 1, 4, 1/dt)
    theta = bandpass_filter(solution, 4, 8, 1/dt)
    alpha = bandpass_filter(solution, 8, 13, 1/dt)
    beta = bandpass_filter(solution, 13, 30, 1/dt)
    gamma = bandpass_filter(solution, 30, 100, 1/dt)
    
    # Compute coupling metrics
    coupling_metrics = {}
    for slow_band in [delta, theta, alpha, beta]:
        for fast_band in [gamma]:
            mi = modulation_index(slow_band, fast_band)
            coupling_metrics[f'{slow_band.name}-{fast_band.name}'] = mi
    
    return coupling_metrics
```

## Key Findings

### 1. Broader Dynamical Repertoire

NG-NMM provides:
- More homogeneous state types
- Richer heterogeneous patterns
- Better biological plausibility

### 2. Stability Analysis

- **Uniform perturbations**: Analyzed via Jacobian eigenvalues
- **Non-uniform perturbations**: Dispersion relations
- **Pattern emergence**: Linked to unstable modes

### 3. Anatomical Connectivity Effects

**Cross-Frequency Coupling:**
- Anatomical connectivity enables gamma modulation by slower rhythms
- Critical for understanding cognitive integration
- Links structure to function

**Mechanism:**
```
Slow rhythm (θ/α/β) in Region A
         ↓ (anatomical connectivity)
Modulates excitability of Region B
         ↓
Amplitude modulation of gamma in Region B
```

## Applications

### 1. Whole-Brain Dynamics

- Understanding resting-state networks
- Task-evoked activation patterns
- Disease state modeling

### 2. Cognitive Modeling

- Working memory (gamma synchronization)
- Attention (cross-frequency coupling)
- Consciousness (integrated information)

### 3. Clinical Applications

- Epilepsy seizure dynamics
- Parkinson's tremor mechanisms
- Alzheimer's disease modeling

### 4. Brain Stimulation

- Optimal stimulation targets
- Frequency-specific effects
- Network modulation strategies

## Comparison with Classical Models

| Feature | Classical NMM | Next Gen NMM |
|---------|--------------|--------------|
| Populations | Single or few | Explicit E/I |
| Gamma mechanism | Phenomenological | PING (biophysical) |
| Oscillations | Ad hoc | Emergent |
| Coupling | Simple | Cross-frequency |
| Biological basis | Abstract | Mechanistic |

## Parameters Reference

### Physiological Values

```python
# Recommended parameter sets

# Resting state (low activity)
RESTING_PARAMS = {
    'g_EE': 0.1, 'g_EI': 0.4,
    'g_IE': 0.3, 'g_II': 0.1,
    'tau_E': 4.0, 'tau_I': 16.0
}

# Active state (gamma oscillations)
ACTIVE_PARAMS = {
    'g_EE': 0.3, 'g_EI': 0.6,
    'g_IE': 0.5, 'g_II': 0.2,
    'tau_E': 2.0, 'tau_I': 10.0
}

# Seizure-like (high synchrony)
SEIZURE_PARAMS = {
    'g_EE': 0.8, 'g_EI': 0.2,
    'g_IE': 0.1, 'g_II': 0.05,
}
```

## Reference

**Title:** Emergent Spatiotemporal Dynamics in Large-Scale Brain Networks with Next Generation Neural Mass Models
**Authors:** Rosa Maria Delicado, Gemma Huguet, Pau Clusella
**arXiv:** 2512.03907
**Date:** December 3, 2025

## Related Skills

- `neural-mass-models`: Classical neural mass modeling
- `brain-networks`: Network connectivity analysis
- `oscillation-analysis`: Neural oscillation analysis
- `ping-mechanism`: PING gamma oscillation details
- `whole-brain-modeling`: Large-scale brain simulation

## Activation Keywords

- "next generation neural mass"
- "ng-nmm brain dynamics"
- "large scale brain networks"
- "ping mechanism gamma"
- "cross frequency coupling"
- "spatiotemporal patterns brain"
- "whole brain modeling"
- "neural mass model oscillations"
