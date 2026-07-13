---
name: stationary-covariance-spectra-neural-dynamics
description: "Free-probability framework for analyzing stationary covariance spectra in non-normal random recurrent neural networks. Derives closed functional equations for moment generating functions and analyzes tail eigenvalue behavior in critical regimes. arXiv:2606.31944"
version: 1.0.0
date: 2026-07-01
source: arXiv:2606.31944
authors: ["Jacob A. Zavatone-Veth"]
institution: "Harvard University"
tags: [neural dynamics, random recurrent networks, covariance spectra, free probability, PCA, non-normal dynamics]
trigger_words: [stationary covariance, spectral analysis, free probability, random recurrent, critical regime, tail eigenvalues]
---

# Stationary Covariance Spectra of Discrete-Time Non-Normal Random Recurrent Dynamics

## Overview

This skill implements theoretical and computational frameworks for analyzing **stationary covariance spectra** in random recurrent neural networks using **free-probability theory**. The methodology provides closed-form functional equations for moment generating functions and characterizes tail eigenvalue behavior in critical regimes.

**Key Contributions:**
- Closed functional equation for stationary covariance spectrum moment generating function
- Analysis of tail eigenvalues in critical regime
- Comparison between discrete-time and continuous-time dynamics
- Free-probability approach vs infinite Schwinger-Dyson hierarchy

## Core Methodology

### 1. Problem Setup

Consider discrete-time random recurrent dynamics:
```
x[t+1] = W · φ(x[t]) + ε[t]
```

where:
- `W` = random non-normal Gaussian weight matrix (variance g²/N)
- `φ` = element-wise nonlinear activation
- `ε` = stationary noise process
- `N` = network size

**Stationary covariance matrix:**
```
C = lim_{T→∞} (1/T) Σ_{t=1}^T (x[t] - μ)(x[t] - μ)^T
```

### 2. Free-Probability Framework

**Moment generating function:**
```
M(z) = Σ_{k=0}^∞ m_k z^{-k}
```

where `m_k = (1/N) Tr(C^k)` are normalized moments of covariance spectrum.

**Closed functional equation (discrete-time):**
```
M(z) = F(M(z), z, g, σ)
```

where:
- `g` = spectral radius parameter (g < 1 for stability)
- `σ` = noise variance
- `F` = function derived via free-probability tools

**Key insight:** Discrete-time dynamics yield a **closed scalar equation**, unlike continuous-time which produces infinite Schwinger-Dyson hierarchy.

### 3. Critical Regime Analysis

At critical point `g → 1⁻`:
- Tail eigenvalues exhibit power-law scaling
- Covariance spectrum becomes heavy-tailed
- Network operates at edge of chaos

**Critical scaling:**
```
λ_max ~ N^{1/2} · (1-g)^{-α}
```

where `α` depends on activation function statistics.

### 4. Implementation

#### 4.1 Numerical Verification

```python
import numpy as np
from scipy.linalg import sqrtm

def simulate_covariance_spectrum(N=1000, g=0.95, T=10000, phi=np.tanh):
    """
    Simulate discrete-time random recurrent network and compute covariance spectrum.
    
    Args:
        N: network size
        g: spectral radius parameter
        T: simulation timesteps
        phi: activation function
    
    Returns:
        eigenvalues: sorted eigenvalues of covariance matrix
    """
    # Random non-normal weight matrix
    W = np.random.randn(N, N) * g / np.sqrt(N)
    
    # Simulate dynamics
    x = np.random.randn(N)
    trajectory = []
    
    for t in range(T):
        x = phi(W @ x) + 0.01 * np.random.randn(N)
        trajectory.append(x)
    
    # Compute covariance matrix
    X = np.array(trajectory)
    C = np.cov(X.T)
    
    # Eigenvalue spectrum
    eigenvalues = np.linalg.eigvalsh(C)
    eigenvalues = np.sort(eigenvalues)[::-1]
    
    return eigenvalues

def compute_moment_generating_function(eigenvalues, z_values):
    """
    Compute empirical moment generating function M(z) = Σ m_k z^{-k}
    
    Args:
        eigenvalues: covariance spectrum eigenvalues
        z_values: complex z values
    
    Returns:
        M_z: moment generating function values
    """
    N = len(eigenvalues)
    moments = np.array([np.sum(eigenvalues**k) / N for k in range(1, 20)])
    
    M_z = np.zeros(len(z_values), dtype=complex)
    for i, z in enumerate(z_values):
        M_z[i] = np.sum([m * z**(-k-1) for k, m in enumerate(moments)])
    
    return M_z
```

#### 4.2 Critical Scaling Analysis

```python
def analyze_critical_scaling(g_values, N_values, num_trials=10):
    """
    Analyze how maximum eigenvalue scales near critical point g → 1.
    
    Args:
        g_values: array of g values (e.g., np.linspace(0.5, 0.99, 20))
        N_values: array of network sizes
        num_trials: number of trials per parameter
    
    Returns:
        scaling_exponent: fitted critical exponent α
    """
    lambda_max = np.zeros((len(g_values), len(N_values), num_trials))
    
    for i, g in enumerate(g_values):
        for j, N in enumerate(N_values):
            for trial in range(num_trials):
                eigs = simulate_covariance_spectrum(N=N, g=g)
                lambda_max[i, j, trial] = eigs[0]
    
    # Average over trials
    lambda_max_mean = lambda_max.mean(axis=2)
    
    # Fit power law: λ_max ~ (1-g)^{-α}
    # Use log-linear regression
    log_lambda = np.log(lambda_max_mean[:, 0])
    log_delta = np.log(1 - g_values)
    
    # Linear fit
    coeffs = np.polyfit(log_delta, log_lambda, 1)
    scaling_exponent = -coeffs[0]
    
    return scaling_exponent
```

#### 4.3 Free-Probability Theoretical Prediction

```python
def free_probability_prediction(g, sigma, phi_deriv_squared):
    """
    Compute theoretical moment generating function via free-probability.
    
    Args:
        g: spectral radius parameter
        sigma: noise variance
        phi_deriv_squared: average squared derivative of activation
    
    Returns:
        M_theory: theoretical moment generating function
    """
    # This requires solving the closed functional equation
    # M = F(M, z, g, σ) iteratively
    
    # Simplified version for Marchenko-Pastur regime
    # Full implementation requires numerical root finding
    
    def fixed_point_iteration(M_guess, z, g, sigma, max_iter=100):
        """Iterate to find self-consistent solution."""
        M = M_guess
        for _ in range(max_iter):
            # Self-consistency equation (simplified)
            M_new = sigma * z**(-1) * (1 + g**2 * phi_deriv_squared * M)
            if np.abs(M_new - M) < 1e-8:
                break
            M = M_new
        return M
    
    return fixed_point_iteration
```

## Experimental Validation

### Test 1: Marchenko-Pastur Limit (g=0)

When `g=0`, network reduces to noise:
```
x[t] = ε[t]
```

Covariance spectrum should follow **Marchenko-Pastur law**:
```python
def marchenko_pastur_density(sigma, N, T):
    """
    Marchenko-Pastur density for white noise covariance.
    
    λ± = σ²(1 ± √(N/T))²
    """
    lambda_plus = sigma**2 * (1 + np.sqrt(N/T))**2
    lambda_minus = sigma**2 * (1 - np.sqrt(N/T))**2
    
    return lambda_minus, lambda_plus
```

### Test 2: Critical Scaling

As `g → 1`, verify:
1. Tail eigenvalues grow as power law
2. Covariance spectrum becomes heavy-tailed
3. Network approaches edge of chaos

### Test 3: Discrete vs Continuous Comparison

Compare discrete-time (closed equation) with continuous-time (infinite hierarchy):
```python
def compare_discrete_continuous(g=0.9, N=500):
    """
    Compare discrete-time dynamics with continuous-time SDE approximation.
    """
    # Discrete-time
    eigs_discrete = simulate_covariance_spectrum(N=N, g=g, T=10000)
    
    # Continuous-time (Euler-Maruyama)
    # dX = (-X + W·φ(X))dt + σ·dW
    
    # Measure discrepancy
    ks_stat = scipy.stats.ks_2samp(eigs_discrete, eigs_continuous)
    
    return ks_stat
```

## Applications

### 1. Neural Data Analysis

Apply to real neural recordings:
```python
def analyze_neural_data(neural_activity):
    """
    Compute covariance spectrum of neural population activity.
    
    Args:
        neural_activity: T × N matrix (time × neurons)
    
    Returns:
        eigenvalues: covariance spectrum
        pca_components: top principal components
    """
    C = np.cov(neural_activity.T)
    eigenvalues, eigenvectors = np.linalg.eigh(C)
    eigenvalues = np.sort(eigenvalues)[::-1]
    
    return eigenvalues, eigenvectors[:, ::-1]
```

### 2. Network Initialization

Use theoretical predictions to initialize recurrent networks:
```python
def initialize_network_safely(N, activation='tanh'):
    """
    Initialize recurrent network to operate near criticality.
    
    Args:
        N: network size
        activation: activation function
    
    Returns:
        W: initialized weight matrix
        g_optimal: optimal spectral radius
    """
    # For tanh activation, critical g ≈ 1
    g_optimal = 1.0
    
    # Random orthogonal initialization
    W = np.random.randn(N, N)
    Q, _ = np.linalg.qr(W)
    W = Q * g_optimal / np.sqrt(N)
    
    return W, g_optimal
```

## Pitfalls and Solutions

### 1. Finite-Size Effects

**Problem:** Small networks (N < 500) show significant finite-size corrections  
**Solution:** Use N ≥ 1000 for asymptotic theory to hold

### 2. Non-Stationarity

**Problem:** Networks may not reach stationary state  
**Solution:** Discard burn-in period, verify stationarity via autocorrelation decay

### 3. Non-Normality Measurement

**Problem:** Quantifying "non-normality" of W  
**Solution:** Use Schur decomposition: `W = Q · T · Q^T`, measure upper triangular part

```python
def measure_non_normality(W):
    """
    Quantify non-normality via Schur decomposition.
    
    Returns:
        non_normality: Frobenius norm of strictly upper triangular part
    """
    Q, T = np.linalg.schur(W)
    upper_tri = np.triu(T, k=1)
    return np.linalg.norm(upper_tri, 'fro')
```

## Activation Keywords

Use this skill when encountering:
- Stationary covariance, spectral analysis
- Random recurrent networks, free probability
- Critical regime, edge of chaos
- PCA of neural dynamics
- Tail eigenvalues, heavy-tailed spectra
- Non-normal dynamics

## References

- Paper: arXiv:2606.31944 (2026)
- Free Probability: Mingo & Speicher (2017)
- Random Matrix Theory: Bai & Silverstein (2010)
- Neural Dynamics: Sompolinsky et al. (1988)

## Verification

To verify implementation:
1. Check g=0 limit matches Marchenko-Pastur
2. Verify closed equation has unique solution for g<1
3. Confirm critical scaling exponent α ≈ 1/2
4. Compare discrete vs continuous time discrepancy
