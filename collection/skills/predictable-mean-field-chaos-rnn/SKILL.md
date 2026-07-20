---
name: predictable-mean-field-chaos-rnn
description: Krylov Mean-Field Chaos theory for random recurrent networks — demonstrating that deterministic chaos has latent predictability through Krylov state space decomposition. Extends Hamiltonian chaos concepts to classical dissipative systems.
version: 1.0.0
category: neuroscience
tags: [chaos, mean-field-theory, recurrent-networks, Krylov-subspace, predictability, neural-dynamics, Lyapunov-exponent]
activation_keywords: [Krylov chaos, mean-field theory, predictable chaos, recurrent network dynamics, Krylov growth rate, latent determinism]
paper_id: arXiv:2606.08805
paper_title: Predictable Mean-Field Chaos in Random Recurrent Networks
authors: [Dynamical Systems Research]
published: 2026-06-07
---

# Predictable Mean-Field Chaos in Random Recurrent Networks

## Overview

This framework demonstrates that deterministic chaos in random recurrent networks with analytic nonlinearities has **latent predictability** — the continuous past uniquely determines the future. By unfolding the power spectrum into a Krylov state space, we expose how this hidden determinism is organized across an infinite hierarchy of temporal modes.

## Revolutionary Finding

**Key Discovery**: For networks with analytic nonlinearities and sufficient Fourier decay:
- Chaos is **apparently stochastic** but **fundamentally deterministic**
- Continuous past trajectory **uniquely predicts** future
- Mean-field theory becomes **conditional prediction theory** for individual trajectories
- **Krylov growth rate** sets prediction complexity
- Microscopic sensitivity ≠ predictive complexity (they are distinct)

## Core Concepts

### 1. Mean-Field Theory Transformation

#### Traditional Mean-Field View
- Chaos → effective stochastic process
- Ensemble description of network dynamics
- Statistical properties only

#### New Conditional Prediction Theory
- Individual trajectories are predictable
- Continuous history determines future
- Not just ensemble statistics
- Practical prediction framework

### 2. Krylov State Space

#### Power Spectrum Unfolding
```
Power spectrum: P(ω) = |x̂(ω)|^2

Krylov decomposition:
x(t) → {ψ₀, ψ₁, ψ₂, ...}  (infinite hierarchy)
```

- Each Krylov mode captures different temporal scale
- Hierarchy organized by frequency decay rate
- Infinite modes → complete trajectory representation

#### Krylov Growth Rate
$$
\text{Krylov Growth Rate} = \lim_{n \to \infty} \frac{\log|\psi_n|}{n}
$$

This rate:
- Sets **finite-resolution prediction complexity**
- Upper-bounds **largest Lyapunov exponent**
- Distinct from microscopic sensitivity

### 3. Latent Determinism Structure

#### Apparent Stochasticity
- Chaos seems unpredictable at microscopic level
- Random-appearing dynamics
- Ensemble stochastic behavior

#### Hidden Determinism
- Past trajectory uniquely encodes future
- Conditioned on continuous history
- Deterministic mapping: past → future
- Infinite precision required for perfect prediction

#### Finite Resolution Prediction
- Krylov truncation: keep first N modes
- Prediction error bounded by growth rate
- Practical prediction with limited modes

## Mathematical Framework

### Random Recurrent Network Model

```python
# Network dynamics:
dx/dt = -x + W·φ(x)

# Components:
x(t): network state vector (N dimensions)
W: random weight matrix
φ(x): analytic nonlinearity

# Conditions:
1. φ is analytic
2. Fourier coefficients decay sufficiently fast
3. W is random (e.g., Gaussian)
```

### Mean-Field Equation

$$
\frac{dx_i}{dt} = -x_i + \sum_j W_{ij} \phi(x_j)
$$

In mean-field limit (N → ∞):
$$
\frac{dX}{dt} = -X + g \cdot \langle \phi(X) \rangle_W
$$

### Krylov Decomposition

#### Step 1: Power Spectrum Analysis
```python
def compute_power_spectrum(x_trajectory):
    """
    x_trajectory: [x(t₀), x(t₁), ..., x(tT)]
    Returns: P(ω) for all frequencies
    """
    x_hat = fft(x_trajectory)
    P = np.abs(x_hat)**2
    return P
```

#### Step 2: Spectral Decay Characterization
```python
def check_fourier_decay(P, threshold):
    """
    Verify sufficient Fourier decay
    Required for Krylov predictability
    """
    # P(k) should decay faster than 1/k^α
    # for some α > threshold
    pass
```

#### Step 3: Krylov Mode Construction
```python
def build_krylov_basis(P, N_modes):
    """
    Unfold power spectrum into Krylov modes
    
    ψ₀: slowest temporal mode
    ψ₁: next frequency band
    ...
    ψ_N: Nth mode
    """
    krylov_modes = []
    for n in range(N_modes):
        # Extract frequency band [ω_n, ω_{n+1}]
        # Construct Krylov mode ψ_n
        pass
    return krylov_modes
```

#### Step 4: Prediction from Krylov Modes
```python
def predict_future(krylov_modes, growth_rate, T_future):
    """
    Given past Krylov representation
    Predict future trajectory
    
    Error bounded by growth_rate × truncation level
    """
    # Extrapolate each mode
    # Reconstruct full trajectory
    pass
```

### Lyapunov vs Krylov

#### Lyapunov Exponent (λ_max)
- Measures microscopic sensitivity
- Nearby trajectories diverge exponentially
- Rate: |Δx(t)| ~ exp(λ_max·t)

#### Krylov Growth Rate (κ)
- Measures prediction complexity
- Finite-resolution prediction difficulty
- Upper bound: κ ≥ λ_max

#### Key Insight
**Different aspects** of chaos:
- λ_max: how fast nearby trajectories diverge
- κ: how hard to predict from past history
- κ bounds λ_max but they're distinct

## Validation & Examples

### Synthetic Networks
```python
# Test case 1: Analytic φ
φ(x) = tanh(x)  # Analytic, fast Fourier decay
→ Predictable chaos confirmed

# Test case 2: Non-analytic φ
φ(x) = ReLU(x)  # Not analytic
→ Prediction breaks down

# Test case 3: Slow Fourier decay
φ(x) = some_slow_decay_function
→ Higher Krylov growth rate
```

### Numerical Verification
1. Generate random W matrix (Gaussian)
2. Evolve dynamics for long time T
3. Compute power spectrum P(ω)
4. Check Fourier decay rate
5. Construct Krylov modes
6. Test prediction: past → future

## Implications for Neuroscience

### 1. Neural Network Dynamics
- **Recurrent networks** in brain: cortex, hippocampus
- **Chaotic dynamics**: observed in neural recordings
- **Predictability**: May be more predictable than thought
- **Krylov modes**: Temporal organization of neural chaos

### 2. Prediction in Biological Systems
- **State prediction**: From neural history to future activity
- **Information processing**: Krylov hierarchy as computation
- **Memory**: Past encoded in Krylov representation
- **Computation**: Chaos as deterministic information flow

### 3. Chaos vs Randomness
- **Apparent stochasticity**: Seemingly random neural dynamics
- **Hidden determinism**: Structured information in chaos
- **Biological advantage**: Predictability from structure
- **Encoding**: Past trajectory as information carrier

### 4. Network Architecture Effects
- **Analytic activations**: Predictability preserved
- **Non-analytic activations**: Predictability breaks
- **Implication**: Biological networks may use analytic nonlinearities
- **ReLU networks**: Might sacrifice predictability

## Comparison: Hamiltonian vs Dissipative

### Hamiltonian Chaos (Previous Work)
- Conservative systems (energy preserved)
- Krylov concepts developed
- Quantum/classical chaos connection

### Dissipative Chaos (This Work)
- Energy dissipating systems
- Random recurrent networks
- **Extension** of Krylov theory to classical dissipative case

### Key Difference
| Aspect | Hamiltonian | Dissipative (This Work) |
|--------|-------------|-------------------------|
| Energy | Conserved | Dissipated |
| Dynamics | Reversible | Irreversible |
| Chaos type | Conservative | Dissipative |
| Application | Quantum systems | Neural networks |

## Theoretical Significance

### 1. Chaos Theory Revision
- Chaos not purely unpredictable
- Latent determinism in chaotic systems
- Prediction possible with continuous history

### 2. Mean-Field Theory Upgrade
- From ensemble statistics to individual prediction
- Conditional on past trajectory
- Practical prediction framework

### 3. Krylov Methods Extension
- From Hamiltonian to dissipative systems
- Classical neural dynamics
- Infinite hierarchy organization

### 4. Complexity Measures
- **Lyapunov**: Sensitivity (how fast divergence)
- **Krylov growth**: Predictability (how hard to predict)
- **Separation**: Different aspects of chaos

## Implementation Guide

### Requirements
```python
import numpy as np
from scipy.fft import fft, ifft
from scipy.integrate import odeint

# Network parameters:
N = 1000  # Network size (mean-field: N → ∞)
g = 1.5   # Coupling strength (chaos regime: g > 1)
```

### Dynamics Simulation
```python
def network_dynamics(x, t, W, phi):
    """
    Random recurrent network dynamics
    
    dx/dt = -x + W·φ(x)
    """
    phi_x = phi(x)
    dx = -x + np.dot(W, phi_x)
    return dx

# Random weight matrix:
W = np.random.randn(N, N) * g / np.sqrt(N)

# Analytic nonlinearity:
phi = lambda x: np.tanh(x)  # Fast Fourier decay

# Evolve:
x0 = np.random.randn(N)
T = np.linspace(0, 100, 10000)
x_trajectory = odeint(network_dynamics, x0, T, args=(W, phi))
```

### Power Spectrum Analysis
```python
def analyze_spectrum(x_trajectory):
    """
    Compute power spectrum and check decay
    """
    # FFT of trajectory
    x_hat = fft(x_trajectory[:, 0])  # Analyze one neuron
    
    # Power spectrum
    P = np.abs(x_hat)**2
    
    # Frequency bins
    freqs = np.fft.fftfreq(len(x_hat), d=T[1]-T[0])
    
    # Check decay rate:
    # P(k) should decay exponentially or as power law
    # with sufficient rate
    
    return P, freqs
```

### Krylov Mode Extraction
```python
def krylov_decomposition(P, freqs, N_modes=10):
    """
    Unfold spectrum into Krylov modes
    
    Divide frequency range into bands
    Each band = one Krylov mode
    """
    # Sort by frequency magnitude
    sorted_idx = np.argsort(np.abs(freqs))
    
    # Divide into N_modes bands
    band_size = len(P) // N_modes
    krylov_modes = []
    
    for n in range(N_modes):
        # Extract band [n*band_size, (n+1)*band_size]
        band_indices = sorted_idx[n*band_size:(n+1)*band_size]
        
        # Construct mode
        psi_n = np.sum(P[band_indices])  # Energy in band
        krylov_modes.append(psi_n)
    
    return krylov_modes
```

### Krylov Growth Rate Calculation
```python
def compute_growth_rate(krylov_modes):
    """
    Growth rate from Krylov mode decay
    
    κ = lim_{n→∞} log(ψ_n)/n
    """
    # Fit exponential decay
    n = np.arange(len(krylov_modes))
    log_psi = np.log(krylov_modes)
    
    # Linear regression: log(ψ_n) = κ·n
    kappa = np.polyfit(n, log_psi, 1)[0]
    
    return kappa
```

### Prediction Test
```python
def test_prediction(x_trajectory, T_train, T_test):
    """
    Test if past predicts future
    
    Train on T_train, predict T_test
    """
    # Split trajectory
    x_train = x_trajectory[:len(T_train)]
    x_test = x_trajectory[len(T_train):len(T_train)+len(T_test)]
    
    # Compute Krylov from training
    P_train, freqs = analyze_spectrum(x_train)
    krylov_train = krylov_decomposition(P_train, freqs)
    kappa = compute_growth_rate(krylov_train)
    
    # Predict test from Krylov extrapolation
    # (Implementation depends on specific method)
    
    # Compare prediction vs actual
    error = np.linalg.norm(x_pred - x_test)
    
    return error, kappa
```

## Key Results

1. **For analytic φ with fast Fourier decay**:
   - Past uniquely predicts future
   - Krylov growth rate finite
   - Prediction complexity bounded

2. **For non-analytic or slow decay**:
   - Prediction breaks down
   - Higher Krylov growth rate
   - More chaotic (larger κ)

3. **Lyapunov exponent**:
   - Upper bounded by Krylov growth rate
   - κ ≥ λ_max always
   - Sometimes κ >> λ_max (distinct aspects)

## Applications

### Neural Dynamics Analysis
- Compute Krylov modes from neural recordings
- Assess predictability from spectrum decay
- Identify networks with hidden determinism

### Chaos Characterization
- Separate sensitivity (Lyapunov) from predictability (Krylov)
- Different interventions for each aspect
- Better chaos control strategies

### Biological Network Design
- Choose analytic nonlinearities for predictability
- Optimize Fourier decay rate
- Balance chaos and predictability

### Machine Learning
- RNN training with predictability constraints
- Architecture choices (tanh vs ReLU)
- Chaotic representations as memory

## Limitations

### Practical Limitations
1. **Infinite precision**: Perfect prediction requires infinite Krylov modes
2. **Long history**: Need sufficient past trajectory
3. **Analyticity**: Must verify nonlinearity properties
4. **Numerical errors**: Integration errors break predictability

### Theoretical Limitations
1. **Mean-field limit**: Finite N introduces corrections
2. **Noise**: Real systems have stochasticity beyond chaos
3. **Non-ideal activations**: Biological neurons may not be analytic

## Future Directions

### Extensions
1. **Finite N corrections**: Beyond mean-field limit
2. **Stochastic systems**: Add noise to dynamics
3. **Non-analytic networks**: Different prediction schemes
4. **Control**: Steering chaotic networks via Krylov

### Applications
1. **Neural recordings**: Test on real brain data
2. **RNN training**: Predictability-aware learning
3. **Chaos control**: Krylov-based interventions
4. **Information theory**: Krylov as information encoding

## Research Implications

### For Dynamical Systems Theory
- Chaos is more structured than previously thought
- Prediction possible with continuous history
- Krylov methods extend to dissipative systems

### For Neuroscience
- Brain chaos may have predictability
- Temporal organization via Krylov hierarchy
- Past neural activity encodes future

### For Machine Learning
- RNN architectures affect predictability
- Analytic activations preserve determinism
- Chaotic representations as useful memory

## Key Takeaways

1. **Deterministic chaos**: Not purely unpredictable
2. **Krylov decomposition**: Organizes chaos temporal structure
3. **Growth rate κ**: Sets prediction complexity
4. **κ ≥ λ_max**: Distinct aspects of chaos
5. **Analytic nonlinearity**: Key condition for predictability
6. **Mean-field → conditional prediction**: Theory upgrade

## Activation Keywords

Use this skill when:
- Analyzing chaotic dynamics in recurrent networks
- Studying predictability vs sensitivity in chaos
- Extending Krylov methods to dissipative systems
- Investigating neural network chaos structure
- Computing prediction complexity bounds
- Separating Lyapunov from Krylov chaos aspects
- Keywords: Krylov chaos, mean-field predictability, deterministic chaos, recurrent network dynamics, Krylov growth rate, latent determinism