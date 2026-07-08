---
name: stationary-covariance-spectra-non-normal-dynamics
version: 1.0.0
description: "Free probability framework for analyzing stationary covariance spectra in discrete-time non-normal random recurrent neural networks. Provides closed-form functional equations for eigenvalue distributions and critical regime behavior."
category: research
tags: ["neuroscience", "random-matrix-theory", "neural-dynamics", "free-probability", "recurrent-networks", "covariance-analysis"]
source: "arXiv:2606.31944"
authors: ["Jacob A. Zavatone-Veth"]
institutions: ["Harvard University"]
created: "2026-07-02"
---

# Stationary Covariance Spectra of Non-Normal Random Recurrent Dynamics

## Overview

This skill provides a theoretical framework for analyzing the stationary covariance structure of linear recurrent neural networks with non-normal (random) weight matrices using free probability theory. The core contribution is a closed functional equation for the moment generating function of the stationary covariance spectrum in discrete-time dynamics, enabling precise characterization of eigenvalue distributions and critical behavior near the stability boundary.

## Core Concepts

### Mathematical Framework

The framework analyzes two canonical models of random recurrent dynamics:

**Discrete-time:**
```
x_{t+1} = J x_t + z_t, where z_t ~ N(0, I_N)
```

**Continuous-time:**
```
dx/dt = -x(t) + J x(t) + z(t), where z(t) is white Gaussian noise
```

where J is a random matrix with i.i.d. Gaussian entries J_{ij} ~ N(0, g/N) for gain parameter g > 0.

### Key Results

#### 1. Discrete-Time Functional Equation

For discrete-time dynamics, the moment generating function F_d(z) of the limiting stationary covariance spectrum satisfies:

```
(1 - z) F_d(z) = F_d(g z F_d(z))
```

with boundary condition F_d(0) = 1.

This closed functional equation enables:
- Exact computation of spectral moments via recurrence relation
- Analytical characterization of spectral edges
- Precise description of critical regime behavior as g → 1

#### 2. Critical Regime Scaling

As the gain parameter approaches the stability boundary (g ↑ 1), let δ = 1 - g:

- **Maximum eigenvalue:** λ_+ ~ 2/δ² = 2/(1-g)²
- **Tail density:** ρ(x/δ²) ~ δ³ √(x(2-x))/(πx²) for 0 < x < 2
- **Ranked eigenvalue scaling:** λ_k ~ (8/π²)(N/k)² for N(1-g) ≪ k ≪ N

#### 3. Discrete vs Continuous Time

**Critical difference:** The discrete-time case yields a closed scalar equation due to gauge symmetry of the circular element in free probability. The continuous-time case leads to an infinite hierarchy of Schwinger-Dyson equations without scalar closure.

**Reason:** Σ_d contains only balanced terms J^k(J^T)^k (gauge-invariant), while Σ_c contains both balanced and imbalanced terms J^j(J^T)^k (gauge-dependent).

## Methodology

### Free Probability Approach

1. **Circular Element Approximation:** Replace random matrix J with circular element c in the N → ∞ limit
2. **Operator-Level Lyapunov Equation:** σ_d = 1 + c σ_d c*
3. **Resolvent Method:** Define R(z) = (1 - z σ_d)^{-1}
4. **Free Integration by Parts:** Use τ(cP) = g(τ ⊗ τ)∂_{c*} P with Leibniz rule
5. **Gauge Symmetry:** Exploit invariance under c → e^{iφ} c to eliminate non-invariant terms

### Spectral Recovery

Given F_d(z), recover the spectral density:

1. **Stieltjes Transform:** G(s) = F_d(1/s)/s
2. **Inversion Formula:** ρ(λ) = (1/π) lim_{ε→0} Im G(λ - iε)

### Numerical Solution

The functional equation can be solved numerically:
- Iterate the recurrence for moments: m_n = [m_{n-1} + Σ_{k=1}^{n-1} g^k m_k a^{(k)}_{n-k}] / (1 - g^n)
- Use Cauchy convolution coefficients a^{(r)}_k
- Compute spectral density via Stieltjes inversion

## Applications

### 1. Neural Data Analysis

Use as a **null model** for principal component spectra in:
- recordings of neural activity (e.g., calcium imaging, electrophysiology)
- comparisons with richer recurrent network models
- identifying non-trivial structure in neural population dynamics

### 2. Control Theory

The stationary covariance matrices coincide with **controllability Gramians**:
- Eigenvalues determine control costs along different dimensions
- Spectral characterization informs optimal control strategies

### 3. Non-Equilibrium Statistical Mechanics

Ornstein-Uhlenbeck processes with non-normal interactions provide:
- Canonical minimal examples of non-equilibrium steady states
- Framework for studying entropy production and correlations

### 4. Comparison with Neural Data

**Key finding:** Discrete-time model predicts ranked eigenvalue decay exponent of 2, while:
- Symmetric random matrix model predicts exponent 2/3
- Experimental neural recordings show exponents between 0.75-0.8
- Continuous-time model conjectured to have exponent 5/4 (unproven)

This demonstrates that temporal discretization substantially changes critical dynamics statistics.

## Implementation

### Moment Computation

```python
def compute_moments(g, n_moments=10):
    """Compute spectral moments via recurrence relation."""
    m = [1.0]  # m_0 = 1
    
    for n in range(1, n_moments + 1):
        # Compute Cauchy convolution coefficients
        a = compute_cauchy_convolution(m, n)
        
        # Recurrence: (1 - g^n) m_n = m_{n-1} + Σ g^k m_k a^{(k)}_{n-k}
        numerator = m[n-1]
        for k in range(1, n):
            numerator += (g**k) * m[k] * a[k]
        
        m.append(numerator / (1 - g**n))
    
    return m
```

### Spectral Density Computation

```python
def spectral_density(lambdas, F_d_values):
    """Compute spectral density via Stieltjes inversion."""
    # G(s) = F_d(1/s) / s
    # ρ(λ) = (1/π) Im G(λ - iε)
    epsilon = 1e-6
    s = lambdas - 1j * epsilon
    
    # Interpolate F_d at 1/s
    F_d_interp = interpolate_Fd(1/s, F_d_values)
    G = F_d_interp / s
    
    return (1/np.pi) * np.imag(G)
```

### Critical Regime Analysis

```python
def critical_tail_eigenvalues(g, N, k_values):
    """Compute eigenvalue scaling in critical regime."""
    delta = 1 - g
    
    # For N*delta ≪ k ≪ N
    lambda_k = (8 / np.pi**2) * (N / np.array(k_values))**2
    
    return lambda_k
```

## Key Insights

### 1. Gauge Symmetry is Crucial

The closed-form solution in discrete time exists because the stationary covariance contains only gauge-neutral terms. This symmetry allows elimination of an infinite number of correlation functions, reducing to a single scalar equation.

### 2. Discrete vs Continuous Time Matters

The choice between discrete and continuous time is not just a numerical convenience—it fundamentally changes the analytical tractability and the predicted spectral properties. This has implications for:
- Model selection in computational neuroscience
- Comparison of theoretical predictions with experimental data
- Understanding the role of temporal discretization in neural recordings

### 3. Free Probability Enables Exact Results

The free probability framework provides a systematic way to:
- Handle non-orthogonal eigenvectors of non-normal matrices
- Compute spectral properties in the large-N limit
- Derive exact functional equations rather than approximations

### 4. Connection to Neural Data

The predicted eigenvalue decay exponents differ from experimental observations, suggesting:
- Real neural networks have structure beyond random connectivity
- Simple null models are insufficient to capture neural population dynamics
- Additional constraints (symmetry, sparsity, structure) must be incorporated

## Limitations and Future Directions

### Current Limitations

1. **Linear dynamics only:** Nonlinear networks can exhibit chaotic behavior not captured here
2. **Gaussian weights:** Structured connectivity (sparse, clustered, low-rank) not analyzed
3. **Stationary regime:** Transient dynamics and non-stationary behavior not characterized
4. **Continuous-time gap:** Lack of closed-form solution for continuous-time case

### Future Extensions

1. **Nonlinear networks:** Extend to nonlinear activation functions using Gaussian equivalence theorems
2. **Structured connectivity:** Analyze sparse, clustered, or low-rank weight matrices
3. **Finite-size corrections:** Derive 1/N corrections to the asymptotic spectrum
4. **Continuous-time closure:** Find conditions under which the Schwinger-Dyson hierarchy truncates
5. **Empirical validation:** Compare predictions with large-scale neural recordings

## Related Work

- **Hu & Sompolinsky (2001):** Frequency-domain covariance for linear networks
- **Pachitariu et al. (2023):** Empirical eigenvalue spectra from mouse brain recordings
- **Clark (2025), Wakhloo (2025):** Gaussian equivalence theorems for nonlinear networks
- **Shen & Hu:** Extension of Hu-Sompolinsky to nonlinear networks via linearization

## References

- Mingo, J.A. & Speicher, R. (2017). *Free Probability and Random Matrices*. Springer.
- Collins, B., et al. (2007). "Moments and spectra of random unitary matrices." *Communications in Mathematical Physics*.
- Paper: arXiv:2606.31944 (Zavatone-Veth, 2026)

## Usage

This skill is applicable when:
- Analyzing principal component spectra of neural population data
- Building null models for recurrent neural network dynamics
- Studying non-normal random matrix theory in neuroscience contexts
- Comparing theoretical predictions with experimental eigenvalue distributions
- Understanding the role of temporal discretization in neural dynamics

## Activation

Keywords: `free probability`, `stationary covariance`, `non-normal dynamics`, `recurrent neural networks`, `random matrix theory`, `eigenvalue spectrum`, `principal component analysis`, `neural data analysis`, `null models`, `critical regime`, `gauge symmetry`
