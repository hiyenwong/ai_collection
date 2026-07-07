---
name: quantum-informed-chaos-ml
description: "Apply quantum statistical features and quantum-inspired methods to machine learning for predicting chaotic dynamical systems. Uses higher-order quantum statistical features to capture complex correlations in chaotic data. Use when: forecasting chaotic time series, modeling turbulent fluid dynamics, predicting weather/climate chaos, analyzing nonlinear dynamical systems, or benchmarking quantum advantage in ML tasks."
category: quantum-ml
---

# Quantum-Informed ML for Predicting Chaos

Foundations and practical methods for leveraging quantum statistical features in machine learning to predict and model chaotic dynamical systems.

## Overview

Chaotic systems exhibit extreme sensitivity to initial conditions, making long-term prediction notoriously difficult. This skill applies **higher-order quantum statistical features** — correlations and distributions derived from quantum state tomography principles — to enhance ML models' ability to capture the complex, nonlinear structure of chaotic attractors.

**Source Paper**: arXiv:2606.13422 — "Foundations of Practical Quantum Advantage in Quantum-Informed ML for Predicting Chaos"

## Core Methodology

### 1. Why Quantum Features for Chaos?

Classical ML models struggle with chaotic systems because:
- **Exponential state space**: Chaotic attractors have fractal dimensions that require exponential classical resources
- **Higher-order correlations**: Classical features capture 2-point correlations well, but chaos lives in multi-point correlations
- **Quantum expressivity**: Quantum states naturally encode exponential correlations through entanglement

Quantum-informed features provide:
- **Higher-order moments**: Beyond mean/variance — quantum purity, Rényi entropies, multipartite correlations
- **Phase-space encoding**: Wigner functions, Husimi Q-distributions capture quantum-classical correspondence
- **Entanglement-based features**: Quantify nonlocal correlations in chaotic trajectories

### 2. Quantum Statistical Feature Pipeline

```
Chaotic Time Series x(t)
    ↓ embedding (delay coordinates)
State Vector Reconstruction
    ↓ quantum state mapping
Density Matrix ρ
    ↓ quantum measurements
Higher-Order Features:
  - Purity: Tr(ρ²)
  - Von Neumann entropy: -Tr(ρ log ρ)
  - Rényi entropies: S_α(ρ) = (1/(1-α)) log Tr(ρ^α)
  - Mutual information between subsystems
  - Negativity (entanglement measure)
  - Out-of-time-order correlators (OTOCs)
    ↓ feature concatenation
ML Model (classical or quantum)
    ↓ prediction
Future State x(t+Δt)
```

### 3. Key Quantum Features

| Feature | Formula | Chaos Signal |
|---------|---------|-------------|
| **Purity** | Tr(ρ²) | Detects mixing rate of attractor |
| **Von Neumann entropy** | -Tr(ρ log ρ) | Measures chaos complexity |
| **Rényi-2 entropy** | -log Tr(ρ²) | Faster-to-compute chaos indicator |
| **OTOC** | ⟨W†(t) V† W(t) V⟩ | Lyapunov exponent proxy |
| **Mutual information** | I(A:B) = S(A) + S(B) - S(AB) | Cross-variable coupling strength |
| **Negativity** | ‖ρ^{T_A}‖_1 - 1 | Entanglement in phase space |

## Application Patterns

### Pattern 1: Lorenz System Prediction

```python
import numpy as np
from scipy.integrate import solve_ivp

# Lorenz attractor
def lorenz(t, state, sigma=10, rho=28, beta=8/3):
    x, y, z = state
    return [sigma*(y-x), x*(rho-z)-y, x*y - beta*z]

# Generate trajectory
sol = solve_ivp(lorenz, [0, 100], [1, 1, 1], dense_output=True)
t = np.linspace(0, 100, 10000)
trajectory = sol.sol(t)  # shape: (3, 10000)

# Embed into quantum-like state
def embed_to_density_matrix(trajectory_chunk, embed_dim=8):
    """Convert a trajectory chunk to a density matrix."""
    # Delay-coordinate embedding
    tau = 10
    embedded = []
    for i in range(0, len(trajectory_chunk) - tau*(embed_dim-1), tau):
        state = []
        for d in range(embed_dim):
            state.extend(trajectory_chunk[:, i + d*tau])
        embedded.append(state)
    embedded = np.array(embedded)
    
    # Normalize and form density matrix
    embedded = (embedded - embedded.mean(axis=0)) / embedded.std(axis=0)
    rho = embedded.T @ embedded / len(embedded)
    rho = rho / np.trace(rho)  # Normalize Tr(ρ) = 1
    return rho

# Compute quantum features
def quantum_features(rho):
    """Extract quantum statistical features from density matrix."""
    # Purity
    purity = np.trace(rho @ rho).real
    
    # Von Neumann entropy (via eigendecomposition)
    eigvals = np.linalg.eigvalsh(rho)
    eigvals = eigvals[eigvals > 1e-10]  # Remove numerical zeros
    vne = -np.sum(eigvals * np.log(eigvals))
    
    # Rényi-2 entropy
    renyi2 = -np.log(purity)
    
    return {'purity': purity, 'vne': vne, 'renyi2': renyi2}
```

### Pattern 2: OTOC-Based Chaos Detection

```python
def compute_otoc_proxy(trajectory, time_window=50):
    """
    Compute a classical proxy for OTOC from trajectory data.
    OTOC growth rate ≈ quantum Lyapunov exponent.
    """
    # Use two nearby trajectories
    x0 = trajectory[:, 0]
    x0_perturbed = x0 + np.random.randn(len(x0)) * 1e-8
    
    # Track separation over time
    separations = []
    for t in range(time_window):
        # Approximate separation using Jacobian
        delta = np.linalg.norm(trajectory[:, t+1] - trajectory[:, t])
        separations.append(delta)
    
    # Lyapunov exponent estimate
    separations = np.array(separations)
    separations = separations[separations > 0]
    lyap = np.polyfit(np.arange(len(separations)), np.log(separations), 1)[0]
    
    return lyap, separations
```

### Pattern 3: Hybrid Quantum-Classical Prediction

```python
def quantum_feature_augmented_prediction(trajectory, n_steps_ahead, model='lstm'):
    """
    Combine classical trajectory data with quantum statistical features
    for improved chaotic system prediction.
    """
    # Classical features
    X_classical = trajectory[:, :-n_steps_ahead].T  # past states
    y_classical = trajectory[:, n_steps_ahead:].T    # future states
    
    # Quantum features (sliding window)
    window_size = 100
    X_quantum = []
    for i in range(0, X_classical.shape[0] - window_size):
        chunk = trajectory[:, i:i+window_size]
        rho = embed_to_density_matrix(chunk)
        feats = quantum_features(rho)
        X_quantum.append([feats['purity'], feats['vne'], feats['renyi2']])
    
    X_quantum = np.array(X_quantum)
    
    # Combine features
    # Classical + Quantum → Prediction
    # Can use LSTM, transformer, or quantum neural network
    
    return X_classical, X_quantum, y_classical
```

## Implementation Steps

### Step 1: Data Preprocessing

1. Collect chaotic time series data (simulation or measurement)
2. Apply delay-coordinate embedding to reconstruct phase space
3. Normalize to zero mean, unit variance
4. Split into train/validation/test with temporal ordering

### Step 2: Quantum Feature Extraction

1. Choose embedding dimension (typically 2× attractor dimension + 1)
2. Compute density matrix from embedded trajectory chunks
3. Extract: purity, entropies, mutual information, OTOC proxies
4. Handle edge cases: near-pure states (purity ≈ 1), numerical stability

### Step 3: Model Training

```python
# Architecture options:
# A) Classical ML with quantum features (baseline)
#    - LSTM/GRU with quantum feature augmentation
#    - Transformer with quantum attention bias
# B) Quantum ML (when hardware available)
#    - Variational Quantum Circuit (VQC) for feature encoding
#    - Quantum kernel methods (QSVM)
# C) Hybrid
#    - Classical encoder → Quantum feature processor → Classical decoder
```

### Step 4: Evaluation Metrics

| Metric | Purpose |
|--------|---------|
| **RMSE** | Point prediction accuracy |
| **Lyapunov time** | How far ahead prediction remains useful |
| **Attractor reconstruction** | Does predicted trajectory match true attractor geometry? |
| **Power spectrum match** | Frequency-domain agreement |
| **Kolmogorov-Sinai entropy** | Information production rate match |

## Traps & Pitfalls

- **Density matrix positivity**: Ensure constructed ρ is positive semidefinite — project onto PSD cone if needed
- **Embedding dimension**: Too small → lose information; too large → curse of dimensionality. Use false nearest neighbors method
- **Numerical entropy**: Log of near-zero eigenvalues → -∞. Use cutoff (1e-10) or regularization
- **OTOC proxy accuracy**: Classical OTOC proxy is approximate — validate against exact computation for small systems
- **Quantum advantage claims**: Distinguish between *practical* advantage (better predictions) vs *asymptotic* advantage (theoretical scaling)
- **Data requirements**: Chaos prediction needs long, high-quality time series — noisy data corrupts quantum features

## Validation Checklist

- [ ] Density matrices are valid (Hermitian, PSD, Tr(ρ)=1)
- [ ] Quantum features are stable across trajectory segments
- [ ] Prediction horizon exceeds classical baseline by ≥10%
- [ ] Attractor geometry preserved (correlation dimension match)
- [ ] Features capture chaos: purity decreases with increasing chaos parameter

## Related Skills

- `quantum-research-analysis` — Analyze quantum computing papers
- `quantum-statistical-mechanics-gauge` — Statistical mechanics methods
- `quantum-info-deep-learning` — Quantum information + DL

## References

- arXiv:2606.13422 — "Foundations of Practical Quantum Advantage in Quantum-Informed ML for Predicting Chaos"
- Keywords: quantum advantage, chaos prediction, machine learning, OTOC, Lyapunov exponent, quantum statistical features
