---
name: dysco-latent-dynamics-extraction
description: DYSCO (Dynamics via Contrastive Learning) - Multi-view temporal contrastive learning for extracting governing equations from latent dynamics. Identifies dynamical systems from noisy high-dimensional observations with theoretical identifiability guarantees.
keywords:
  - contrastive learning
  - dynamical systems
  - latent dynamics
  - governing equations
  - system identification
  - neural recordings
  - representation learning
  - scientific discovery
  - multi-view learning
version: 1.0.0
arxiv_id: 2606.13260
authors: Paolo Muratore, Mackenzie Weygandt Mathis
published: 2026-06-11
categories: [cs.LG, q-bio.NC]
---

# DYSCO: Extracting Governing Equations from Latent Dynamics via Multi-View Contrastive Learning

## Overview

This paper presents **DYSCO**, a multi-view temporal contrastive learning algorithm that **jointly recovers latent trajectories and governing dynamics** from noisy, high-dimensional measurements. The framework enables **symbolic recovery of governing equations** within an affine gauge with theoretical identifiability guarantees.

**Key Innovation**: Multi-view contrastive learning + functional basis parameterization → disentangle signal from noise + recover symbolic dynamics

**Core Question**: How can we identify latent dynamical systems from noisy, high-dimensional observations (e.g., neural recordings)?

---

## Methodology

### 1. Multi-View Contrastive Learning Framework

**Core Idea**: Use multiple independent noisy views of same underlying process to separate signal from noise

```python
# Problem formulation
y_t^i = g_i(x_t) + ε_t^i  # i = 1, 2, ..., K views
# x_t: latent trajectory (unknown)
# g_i: observation function (nonlinear, unknown)
# ε_t^i: observation noise (Gaussian or Poisson)
```

**Key Assumption**: Views are independent conditioned on latent state

### 2. Contrastive Learning Objective

**Temporal contrastive loss**:
```python
L_contrastive = -log(exp(sim(x_t, x_{t+τ}) / τ)
                     / Σ_s exp(sim(x_t, x_s) / τ))
```

**Positive pairs**: `(x_t, x_{t+τ})` - temporally adjacent samples (same trajectory)

**Negative pairs**: `(x_t, x_s)` - samples from different trajectory segments

### 3. Functional Basis Parameterization

**Dynamics representation**:
```python
dx/dt = f(x) = Σ_{k=1}^K θ_k · φ_k(x)
# φ_k: basis functions (polynomial, neural network, etc.)
# θ_k: coefficients to identify
```

**Advantages**:
1. Structured parameterization → symbolic recovery
2. Sparse basis → interpretable equations
3. Flexible basis → adapts to dynamics complexity

### 4. Joint Optimization

**Loss function**:
```python
L_total = L_contrastive + L_reconstruction + λ·L_sparsity
# L_contrastive: disentangles signal from noise
# L_reconstruction: ensures latent encodes observations
# L_sparsity: encourages interpretable equations
```

---

## Mathematical Framework

### 1. Identifiability Theory

**Main Theorem**: Under multi-view assumption with independent noise:
```
The latent trajectory x_t and dynamics f(x) are identifiable
up to affine transformation:
x̂_t = A·x_t + b
f̂(x̂) = A·f(A^{-1}(x̂ - b))
```

**Key Result**: Extends identifiability to realistic noisy nonlinear observations

### 2. Affine Gauge Freedom

**Transformation family**:
```python
# Any affine transformation preserves dynamics structure
x̂ = A·x + b  (A invertible, b arbitrary)

# Governing equations transform accordingly
f̂(x̂) = A·f(A^{-1}(x̂ - b))

# Example: Simple rotation/translation
# x̂ = R·x + c  → f̂(x̂) = R·f(R^T(x̂ - c))
```

### 3. Noise Disentanglement Mechanism

**Why multi-view works**:
```python
# Single view: y_t = g(x_t) + ε_t
# Cannot separate signal g(x_t) from noise ε_t

# Multi-view: y_t^1 = g_1(x_t) + ε_t^1
#             y_t^2 = g_2(x_t) + ε_t^2

# Contrastive learning finds x_t by:
# - Maximizing agreement across views (signal)
# - Minimizing agreement within noise (independent)
```

**Mathematical guarantee**: Independent noise cancels out in contrastive objective

---

## Computational Implementation

### 1. DYSCO Architecture

```python
class DYSCO:
    def __init__(self, 
                 encoder_dim,      # Latent dimension
                 basis_functions,  # φ_k for dynamics
                 K_views):         # Number of views
        
        # Encoders for each view
        self.encoders = [Encoder(view_dim, encoder_dim) 
                        for _ in range(K_views)]
        
        # Dynamics parameterization
        self.dynamics = DynamicsBasis(encoder_dim, basis_functions)
        
        # Decoders for reconstruction
        self.decoders = [Decoder(encoder_dim, view_dim)
                        for _ in range(K_views)]
    
    def forward(self, observations):
        # observations: {y_t^i} for i = 1..K
        
        # Encode to latent
        latents = [encoder(obs) for encoder, obs 
                   in zip(self.encoders, observations)]
        
        # Aggregate multi-view (average for signal extraction)
        x_t = aggregate_latents(latents)
        
        # Predict dynamics
        dx_dt = self.dynamics(x_t)
        
        # Reconstruct observations
        reconstructions = [decoder(x_t) for decoder in self.decoders]
        
        return x_t, dx_dt, reconstructions
```

### 2. Training Procedure

```python
def train_dysco(model, data, epochs):
    """
    Multi-view contrastive learning for dynamics extraction.
    
    Parameters:
    - model: DYSCO instance
    - data: Multi-view observations {y_t^1, ..., y_t^K}
    - epochs: Training iterations
    """
    optimizer = torch.optim.Adam(model.parameters())
    
    for epoch in range(epochs):
        # Sample positive pairs (temporally adjacent)
        t = random_time_index()
        τ = random_delay()  # Small temporal shift
        
        pos_pairs = [(data[t], data[t+τ]) for view in data.views]
        
        # Sample negative pairs (different trajectory segments)
        s = random_different_index()
        neg_pairs = [(data[t], data[s]) for view in data.views]
        
        # Compute contrastive loss
        L_contr = contrastive_loss(pos_pairs, neg_pairs)
        
        # Reconstruction loss
        L_recon = reconstruction_loss(data, model.reconstruct(data))
        
        # Dynamics sparsity loss (L1 on coefficients)
        L_sparse = torch.norm(model.dynamics.coefficients, p=1)
        
        # Total loss
        L_total = L_contr + L_recon + λ·L_sparse
        
        optimizer.zero_grad()
        L_total.backward()
        optimizer.step()
```

### 3. Symbolic Equation Recovery

```python
def extract_governing_equations(model, basis_functions):
    """
    Extract symbolic governing equations from learned dynamics.
    
    Returns:
    - equation_str: Symbolic equation (e.g., "dx/dt = -x + x^3")
    """
    coefficients = model.dynamics.coefficients.detach()
    
    # Build equation string
    terms = []
    for k, (coeff, basis_func) in enumerate(zip(coefficients, basis_functions)):
        if abs(coeff) > threshold:  # Sparse selection
            terms.append(f"{coeff:.3f}·{basis_func.name}")
    
    equation_str = "dx/dt = " + " + ".join(terms)
    
    return equation_str
```

---

## Core Findings

### 1. Accurate Recovery Across Dynamical Regimes

**Tested dynamics**:
- **Chaotic**: Lorenz system, Rössler attractor
- **Oscillatory**: Van der Pol, Stuart-Landau
- **Metastable**: Double-well potential, Switching systems

**Results**: High accuracy for both latent trajectories and flow fields

### 2. Robustness to Observation Noise

**Noise types tested**:
- **Gaussian noise**: Additive white noise (σ = 0.1 to 1.0)
- **Poisson noise**: Neural recording realistic (spike-count noise)

**Key Finding**: Poisson noise robustness particularly relevant for neural data

### 3. Affine Indeterminacy Handling

**Practical approach**:
```python
# Identify dynamics up to affine transformation
# Use canonical normalization to fix gauge:
x̂_canonical = (x̂ - mean(x̂)) / std(x̂)
f̂_canonical = std(x̂)·f̂  # Scale-adjusted dynamics
```

---

## Applications

### 1. Neural Recording Analysis

**Use case**: Extract dynamics from calcium imaging / electrophysiology

```python
# Multi-view setup:
# View 1: Calcium fluorescence (ΔF/F)
# View 2: Electrophysiology (spike trains)
# View 3: Behavioral correlates

neural_dynamics = DYSCO(encoder_dim=50, basis='polynomial', K=3)
neural_dynamics.train(neural_data)

# Extract governing equations of neural dynamics
equations = extract_governing_equations(neural_dynamics)
```

### 2. Scientific Discovery Pipeline

**Automated equation discovery**:
```python
# Step 1: Multi-view data collection
views = collect_observations(experiment)

# Step 2: Train DYSCO
model = DYSCO.train(views)

# Step 3: Extract candidate equations
candidates = extract_governing_equations(model)

# Step 4: Validate experimentally
validate_dynamics(candidates, perturbation_experiment)
```

### 3. Chaotic System Identification

**Lorenz system recovery**:
```python
# True dynamics: dx/dt = σ(y-x), dy/dt = x(r-z)-y, dz/dt = xy-bz

# DYSCO recovery from noisy observations:
extracted = "dx/dt = 10.2(y-x), dy/dt = x(28.1-z)-y, dz/dt = xy-2.67z"

# High parameter accuracy (σ≈10, r≈28, b≈2.67)
```

---

## Technical Details

### 1. Encoder Architecture

```python
class Encoder(nn.Module):
    """
    View-specific encoder: y_t → x_t (latent)
    
    Architecture options:
    - MLP: Multi-layer perceptron (simple)
    - TCN: Temporal Convolutional Network (temporal)
    - Transformer: Self-attention based
    """
    def __init__(self, input_dim, latent_dim):
        self.network = nn.Sequential(
            nn.Linear(input_dim, 256),
            nn.ReLU(),
            nn.Linear(256, 128),
            nn.ReLU(),
            nn.Linear(128, latent_dim)
        )
    
    def forward(self, observation):
        return self.network(observation)
```

### 2. Basis Function Selection

**Polynomial basis** (for simple dynamics):
```python
basis_functions = [
    λ → 1,                    # constant
    λ → x_i,                  # linear
    λ → x_i·x_j,              # quadratic
    λ → x_i·x_j·x_k,          # cubic
]
```

**Neural network basis** (for complex dynamics):
```python
basis_functions = NeuralBasis(
    input_dim=latent_dim,
    hidden_dim=64,
    output_dim=K_basis
)
```

### 3. Sparsity Regularization

```python
# L1 regularization for sparse equation discovery
L_sparse = torch.norm(model.dynamics.coefficients, p=1)

# Alternative: Group sparsity for interpretable terms
L_group_sparse = torch.norm(torch.stack([
    torch.norm(coeff_group, p=2) 
    for coeff_group in coefficient_groups
]), p=1)
```

---

## Experimental Validation

### 1. Synthetic Dynamics Test

**Setup**:
```python
# Generate multi-view observations from known dynamics
true_dynamics = Lorenz(sigma=10, rho=28, beta=2.67)
observations = generate_multiview(true_dynamics, noise='Poisson')

# Train DYSCO
model = DYSCO.train(observations)

# Measure recovery accuracy
trajectory_error = MSE(model.latent, true_dynamics.trajectory)
flow_error = MSE(model.dynamics, true_dynamics.flow_field)
```

### 2. Neural Recording Test

**Dataset**: Motor cortex recording during reaching task

**Views**:
1. Calcium imaging (ΔF/F)
2. Electrophysiology (spike trains)
3. Kinematic data (hand position)

**Result**: Recovered latent dynamics correlates with motor planning

---

## Limitations & Extensions

### Current Limitations

1. **Affine indeterminacy**: Cannot recover exact coordinates without normalization
2. **View independence assumption**: Requires truly independent noise
3. **Stationarity**: Assumes dynamics don't change over time
4. **Basis selection**: Manual choice of basis functions

### Future Extensions

1. **Non-affine identifiability**: Additional constraints to fix gauge
2. **Non-independent noise**: Robustness to correlated noise across views
3. **Non-stationary dynamics**: Adaptive dynamics learning
4. **Automatic basis discovery**: Learn basis functions from data

---

## Related Methods

### System Identification

- **SINDy**: Sparse Identification of Nonlinear Dynamics (Brunton et al.)
- **Koopman operator**: Linear embedding for nonlinear dynamics
- **Deep Koopman**: Neural network Koopman approximation

### Contrastive Learning

- **SimCLR**: Contrastive learning for images
- **Time-Contrastive Learning (TCL)**: Temporal contrastive
- **Multi-view contrastive**: CMC (Contrastive Multiview Coding)

### Representation Learning

- **VAE**: Variational autoencoder for latent dynamics
- **Dynamic VAE**: Time-series VAE variants
- **Latent ODE**: Neural ODE in latent space

---

## Key References

1. **SINDy**: Brunton et al. (2016) - "Discovering governing equations from data"
2. **Multi-view learning**: Tian (2020) - "Contrastive multiview coding"
3. **Identifiability**: Hyvarinen & Morioka (2016) - "Unsupervised feature extraction"
4. **Neural ODE**: Chen et al. (2018) - "Neural ordinary differential equations"

---

## Activation Keywords

**Trigger phrases**:
- "extract governing equations"
- "latent dynamics identification"
- "multi-view contrastive learning"
- "system identification from neural recordings"
- "dynamics discovery"
- "DYSCO algorithm"
- "affine identifiability"
- "symbolic equation recovery"
- "noisy observation dynamics"
- "Poisson noise robustness"

---

## Notes

- **8,809 KB, submitted June 11, 2026** - First submission, new method
- **From Mathis Lab** (Caltech) - Known for behavioral neuroscience + ML
- **Cross-listed cs.LG + q-bio.NC** - Bridges ML and neuroscience
- **Neural recording relevance**: Poisson noise handling critical for spike data
- **Novel contribution**: First multi-view contrastive approach for dynamics extraction with theoretical guarantees

This skill enables **extracting symbolic governing equations from noisy high-dimensional observations** using **multi-view temporal contrastive learning**, with **identifiability guarantees** extending to realistic neural recording scenarios.