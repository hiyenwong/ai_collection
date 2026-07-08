---
name: stationary-covariance-spectra-non-normal
description: "Free-probability framework for deriving closed functional equations of stationary covariance spectra in discrete-time non-normal random recurrent dynamics, enabling analysis of tail eigenvalues in critical regime."
metadata:
  arxiv_id: "2606.31944"
  authors: "Jacob A. Zavatone-Veth"
  published: "2026-06-30"
  categories: "q-bio.NC, cond-mat.dis-nn"
  conference: "arXiv"
---

## Context

Principal component analysis (PCA) characterizes structure in recurrent neural network dynamics. For stationary noise-driven dynamics, the variance distribution among principal components is determined by the spectrum of the stationary covariance matrix. While spectral properties are well-understood for linear networks with **normal** synaptic weight matrices, understanding for random **non-normal** dynamics remains incomplete.

This paper uses a **free-probability approach** to formally derive a closed functional equation for the moment generating function of the limiting stationary covariance spectrum.

## Core Methodology

### 1. Problem Setup
**Dynamics**: Discrete-time linear recurrent network with random non-normal Gaussian weights
```
x(t+1) = W x(t) + ξ(t)
```
where:
- `W` ∈ ℝⁿˣⁿ: random weight matrix with i.i.d. Gaussian entries (mean 0, variance σ²/n)
- `ξ(t)`: stationary noise process
- `n`: network size (→ ∞ in thermodynamic limit)

**Key quantity**: Stationary covariance matrix `C = lim_{T→∞} (1/T) Σ x(t)x(t)ᵀ`

### 2. Mathematical Framework

#### Free Probability Theory
Uses tools from random matrix theory:
- **R-transform**: Additive free convolution
- **S-transform**: Multiplicative free convolution
- **Stieltjes transform**: m(z) = ∫ ρ(λ)/(z-λ) dλ

#### Closed Functional Equation
For discrete-time dynamics, derives:
```
M(z) = f(M(z), σ², noise_statistics)
```
where M(z) is the moment generating function of the covariance spectrum ρ(λ).

**Key insight**: Discrete-time case yields a **closed scalar equation**, unlike continuous-time which produces an infinite hierarchy of Schwinger-Dyson equations.

### 3. Critical Regime Analysis

**Critical point**: σ² = 1 (edge of stability)
- σ² < 1: Stable fixed point, bounded covariance
- σ² = 1: Critical regime, diverging variance
- σ² > 1: Unstable dynamics, exponential growth

**Tail eigenvalue behavior**:
- At criticality, tail eigenvalues exhibit power-law scaling
- Free-probability approach predicts scaling exponents
- Validates against numerical simulations

### 4. Implementation Pipeline

#### Step 1: Generate Random Non-Normal Matrix
```python
import numpy as np
from scipy.linalg import schur

def generate_non_normal_weights(n, sigma):
    """Generate random non-normal Gaussian weight matrix."""
    W = sigma * np.random.randn(n, n) / np.sqrt(n)
    return W
```

#### Step 2: Simulate Dynamics
```python
def simulate_dynamics(W, T, noise_std=0.1):
    """Simulate discrete-time recurrent dynamics."""
    n = W.shape[0]
    x = np.zeros((n, T))
    
    for t in range(T-1):
        noise = noise_std * np.random.randn(n)
        x[:, t+1] = W @ x[:, t] + noise
    
    return x
```

#### Step 3: Compute Stationary Covariance
```python
def compute_stationary_covariance(x):
    """Compute empirical stationary covariance matrix."""
    # Discard transient (first 10%)
    x_stable = x[:, int(0.1*x.shape[1]):]
    C = np.cov(x_stable)
    return C
```

#### Step 4: Spectral Analysis
```python
from scipy.stats import gaussian_kde

def analyze_spectrum(C):
    """Analyze eigenvalue spectrum of covariance matrix."""
    eigenvalues = np.linalg.eigvalsh(C)
    
    # Estimate spectral density
    kde = gaussian_kde(eigenvalues)
    lambda_range = np.linspace(0, max(eigenvalues)*1.1, 500)
    rho = kde(lambda_range)
    
    return eigenvalues, lambda_range, rho
```

#### Step 5: Free Probability Calculation
```python
def free_probability_mgf(eigenvalues, z_values):
    """Compute moment generating function via free probability."""
    # Stieltjes transform
    m = np.zeros_like(z_values, dtype=complex)
    for i, z in enumerate(z_values):
        m[i] = np.mean(1.0 / (z - eigenvalues))
    
    # Moment generating function: M(z) = -z * m(z) - 1
    M = -z_values * m - 1
    
    return M, m
```

### 5. Key Results

#### Discrete vs Continuous Time
- **Discrete-time**: Closed functional equation for M(z)
- **Continuous-time**: Infinite hierarchy of Schwinger-Dyson equations (not closed)

#### Practical Implication
Discrete-time analysis is more tractable for:
- Critical regime characterization
- Tail eigenvalue predictions
- Comparison with neural data

## Pitfalls

### Non-Normality Requirement
**Problem**: Theory assumes non-normal weight matrices
**Solution**: Check if W Wᵀ = Wᵀ W. If not, non-normal theory applies. Most random matrices are non-normal with probability 1.

### Finite-Size Effects
**Problem**: Free probability is exact only as n → ∞
**Solution**: Use n ≥ 1000 for quantitative agreement. For smaller n, expect finite-size corrections scaling as 1/n.

### Critical Point Sensitivity
**Problem**: σ² = 1 is a sharp transition
**Solution**: Scan σ² ∈ [0.9, 1.1] to capture critical scaling. Use logarithmic spacing for better resolution near criticality.

### Noise Stationarity
**Problem**: Theory assumes stationary noise
**Solution**: Verify noise statistics are time-invariant. For non-stationary noise, theory may not apply.

## Verification

### Analytical Checks
- [ ] Verify closed equation reduces to known results for normal matrices (σ → 0)
- [ ] Confirm moment generating function satisfies consistency conditions
- [ ] Check that tail eigenvalue predictions match numerical simulations

### Numerical Validation
- [ ] Generate W with σ² = 1 (critical)
- [ ] Simulate dynamics for T = 10⁵ time steps
- [ ] Compute empirical covariance spectrum
- [ ] Compare with free-probability prediction
- [ ] Verify tail eigenvalue scaling (power-law exponent)

### Comparison with Baselines
- [ ] Compare against Marchenko-Pastur law (for Wigner matrices)
- [ ] Compare against free convolution predictions (for normal matrices)
- [ ] Verify improvement for non-normal case

## Key Results Summary

1. **Closed functional equation** for discrete-time non-normal dynamics
2. **Infinite hierarchy** for continuous-time case (not closed)
3. **Tail eigenvalue analysis** at criticality (σ² = 1)
4. **Practical framework** for comparing models to neural data

## References

- Author: Jacob A. Zavatone-Veth
- Title: Stationary covariance spectra of discrete-time non-normal random recurrent dynamics
- arXiv: 2606.31944
- Published: 2026-06-30
- Subjects: Neurons and Cognition (q-bio.NC); Disordered Systems and Neural Networks (cond-mat.dis-nn)

## Activation

stationary covariance spectra, non-normal dynamics, random recurrent networks, free probability, moment generating function, critical regime, tail eigenvalues, Schwinger-Dyson equations, random matrix theory, PCA, neural data analysis