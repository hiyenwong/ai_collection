---
name: receptive-fields-hyperbolic-geometry-scale-free-networks
description: "Receptive field emergence from hyperbolic geometry of scale-free networks. Demonstrates that neural receptive fields and population attractor dynamics naturally emerge from effective hyperbolic embedding of scale-free connectivity. Hippocampal place fields serve as experimental validation. Activation: hyperbolic geometry, receptive field, place field, scale-free network, hyperbolic embedding, attractor dynamics, hippocampal, grid cell."
---

# Receptive Fields via Hyperbolic Geometry of Scale-Free Networks

> Neural receptive fields and population attractor dynamics naturally emerge when scale-free brain networks are embedded in hyperbolic space, providing a geometric explanation for place fields, grid cells, and sensory tuning curves.

## Metadata
- **Source**: arXiv:2509.25453
- **Authors**: A. Cabezuelo, F. Morante, J.F. Mejias
- **Published**: 2025-09-30
- **Category**: q-bio.NC

## Core Methodology

### Key Innovation
How do neural receptive fields (place fields, orientation tuning, frequency selectivity) emerge from network connectivity? This work shows:
1. **Scale-free networks → hyperbolic geometry**: Networks with heavy-tailed degree distributions are naturally embedded in hyperbolic space (Poincaré disk model)
2. **Hyperbolic embedding → receptive fields**: Position in hyperbolic space maps to stimulus space; radial coordinate = tuning specificity, angular coordinate = preferred stimulus
3. **Population attractors**: Hyperbolic distance governs competitive dynamics → attractor states correspond to stimulus representations
4. **Hippocampal validation**: Place field properties match predictions from hyperbolic embedding of CA3/CA1 connectivity

### Technical Framework

**Hyperbolic Network Embedding**
- **Poincaré disk model**: {z ∈ ℂ : |z| < 1} with metric ds² = 4|dz|²/(1-|z|²)²
- **Node coordinates**: (rᵢ, θᵢ) where r = radial position (popularity), θ = angular position (similarity)
- **Hyperbolic distance**: d_hyp(u,v) = arccosh(cosh(r_u)cosh(r_v) - sinh(r_u)sinh(r_v)cos(Δθ))
- **Connection probability**: P(edge) ~ exp(-β × d_hyp(u,v)) (temperature parameter β controls clustering)

**Receptive Field Derivation**
1. **Stimulus encoding**: Stimulus s maps to angular coordinate θ(s) = 2π × s/s_max
2. **Neuron tuning**: Neuron i at (rᵢ, θᵢ) responds to stimulus s with rate:
   f(s) = f_max × exp(-d_hyp(zᵢ, z(s))²/2σ²)
3. **Tuning width**: σ depends on radial coordinate r → neurons near center (r≈0) are broadly tuned, periphery neurons are sharply tuned
4. **Scale-free prediction**: Degree k ~ exp(r) → high-degree hubs are broadly tuned, low-degree neurons are selective

**Population Attractor Dynamics**
- **Competitive network**: Recurrent connections wᵢⱼ ~ exp(-d_hyp(zᵢ, zⱼ))
- **Attractor equation**: τ dAᵢ/dt = -Aᵢ + Σⱼ wᵢⱼ f(Aⱼ) + Iᵢ(ext)
- **Fixed points**: Correspond to stimulus-specific attractor states
- **Basin structure**: Basin width proportional to hyperbolic neighborhood size
- **Multistability**: Number of attractors ~ network's angular resolution

**Hippocampal Place Field Validation**
- CA3 recurrent connectivity is scale-free (heavy-tailed in-degree)
- Hyperbolic embedding predicts:
  - Place field size distribution matches observed log-normal distribution
  - Place field overlaps decrease with angular distance (grid-like patterns at certain scales)
  - Environment remapping = angular coordinate reassignment

### Key Results
- Hyperbolic geometry explains receptive field properties without explicit training
- Place field size heterogeneity (observed experimentally) follows from degree heterogeneity
- Grid-like periodic patterns emerge from optimal angular packing in hyperbolic space
- Explains why sensory cortical RFs follow log-normal size distributions
- Predicts: disrupting scale-free topology → degraded receptive field formation

## Implementation Guide

### Prerequisites
- Python: numpy, scipy, networkx
- Optional: geomstats (for hyperbolic geometry), igraph (for embedding)
- Understanding of differential geometry basics (manifolds, metrics)

### Step-by-Step
1. **Build scale-free network**: Barabási-Albert or from empirical connectome
2. **Hyperbolic embedding**: Use HyperMap or igraph embedding algorithm
3. **Map stimulus space**: Assign angular coordinates to stimulus features
4. **Compute receptive fields**: Use hyperbolic distance for tuning curves
5. **Simulate attractors**: Competitive dynamics with hyperbolic-scaled weights
6. **Validate**: Compare predicted RF properties to experimental data

### Code Example
```python
import numpy as np
from scipy.spatial.distance import pdist, squareform

class HyperbolicReceptiveFieldModel:
    # Receptive field model from hyperbolic network embedding.
    
    def __init__(self, n_neurons, gamma=2.5, beta=1.5, temp=0.8):
        self.n = n_neurons
        self.gamma = gamma  # degree exponent
        self.beta = beta    # connection decay
        self.temp = temp    # temperature (clustering control)
    
    def hyperbolic_distance(self, r1, theta1, r2, theta2):
        # Poincaré disk hyperbolic distance.
        delta_theta = np.pi - np.abs(np.pi - np.abs(theta1 - theta2))
        return np.arccosh(
            np.cosh(r1) * np.cosh(r2) - 
            np.sinh(r1) * np.sinh(r2) * np.cos(delta_theta)
        )
    
    def embed_scale_free_network(self, seed=42):
        # Embed neurons in hyperbolic disk following PSO model.
        rng = np.random.RandomState(seed)
        # Radial: related to degree (target parameter)
        # High degree → small r (center), low degree → large r (periphery)
        R = 2 * np.log(self.n)  # disk radius
        kappa = rng.pareto(self.gamma - 1, self.n) + 1  # target degrees
        r = R - 2 * np.log(kappa / kappa.min())
        r = np.clip(r, 0, R - 0.01)
        theta = rng.uniform(0, 2 * np.pi, self.n)
        
        self.coords = np.column_stack([r, theta])
        self.kappa = kappa
        return self.coords
    
    def compute_connection_matrix(self):
        # P(edge) ~ exp(-beta * d_hyp) for hyperbolic distance.
        R = 2 * np.log(self.n)
        self.W = np.zeros((self.n, self.n))
        for i in range(self.n):
            for j in range(i+1, self.n):
                d = self.hyperbolic_distance(
                    self.coords[i, 0], self.coords[i, 1],
                    self.coords[j, 0], self.coords[j, 1]
                )
                p = 1 / (1 + np.exp(self.beta * (d - R) / 2))
                if np.random.random() < p:
                    self.W[i, j] = 1
                    self.W[j, i] = 1
        return self.W
    
    def compute_receptive_fields(self, n_stimuli=100):
        # Compute tuning curves from hyperbolic positions.
        stimuli = np.linspace(0, 2 * np.pi, n_stimuli)  # angular stimuli
        
        tuning_curves = np.zeros((self.n, n_stimuli))
        for i in range(self.n):
            r_i = self.coords[i, 0]
            # Radial position determines tuning width
            sigma = 0.3 + 0.5 * (r_i / (2 * np.log(self.n)))  # broader near center
            for s_idx, theta_s in enumerate(stimuli):
                d = self.hyperbolic_distance(r_i, self.coords[i, 1], 0, theta_s)
                tuning_curves[i, s_idx] = np.exp(-d**2 / (2 * sigma**2))
        
        self.tuning_curves = tuning_curves
        self.stimuli = stimuli
        return tuning_curves
    
    def simulate_attractor_dynamics(self, stimulus_idx, T=100, dt=0.1, tau=5.0):
        # Competitive attractor dynamics for given stimulus.
        # External input from receptive field
        I_ext = self.tuning_curves[:, stimulus_idx]
        
        # Recurrent weights (hyperbolic distance-based)
        W_rec = np.zeros((self.n, self.n))
        for i in range(self.n):
            for j in range(i+1, self.n):
                d = self.hyperbolic_distance(
                    self.coords[i, 0], self.coords[i, 1],
                    self.coords[j, 0], self.coords[j, 1]
                )
                w = np.exp(-d / 2)
                W_rec[i, j] = w
                W_rec[j, i] = w
        
        # Run dynamics: dA/dt = -A + tanh(W@A + I_ext)
        A = np.zeros(self.n)
        history = []
        for t in range(T):
            dA = (-A + np.tanh(W_rec @ A + 2.0 * I_ext)) / tau
            A = A + dt * dA
            A = np.clip(A, 0, None)  # ReLU-like
            history.append(A.copy())
        
        return np.array(history), A  # trajectory, final state

# Usage
model = HyperbolicReceptiveFieldModel(n_neurons=200, gamma=2.5)
coords = model.embed_scale_free_network()
W = model.compute_connection_matrix()
tuning = model.compute_receptive_fields(n_stimuli=360)
trajectory, attractor = model.simulate_attractor_dynamics(stimulus_idx=180)
```

## Applications
- **Hippocampal place cell modeling**: Predict place field properties from connectivity
- **Sensory cortex RF prediction**: Estimate tuning curves from structural connectivity
- **Neuromorphic engineering**: Design receptive fields via hyperbolic network layout
- **Grid cell formation**: Periodic angular packing in hyperbolic space → grid patterns
- **Neural prosthetics**: Predict degraded RFs from damaged connectivity
- **Developmental neuroscience**: How RFs emerge as scale-free connectivity develops

## Pitfalls
- Hyperbolic embedding quality depends on network being genuinely scale-free
- Small networks (< 100 nodes) may not show clean hyperbolic structure
- Poincaré disk is 2D; higher-dimensional hyperbolic spaces may be needed for complex stimuli
- The framework is geometric/phenomenological — doesn't specify biophysical mechanisms
- Validation requires comparison with actual electrophysiology data

## Related Skills
- neural-receptive-fields-hyperbolic-geometry
- hyperbolic-eeg-multimodal-learning
- non-euclidean-visual-space-information-geometry
- griffiths-phase-brain-criticality
- brain-network-controllability
