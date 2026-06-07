---
name: dynamic-mean-field-nonlinear-noise
description: "Gaussian-equivalent process methodology for analyzing nonlinear noise in recurrent neural circuits using Ornstein-Uhlenbeck noise matching and lognormal moment closure. Activation: mean field, nonlinear noise, recurrent networks, OU process."
---

# Dynamic Mean Field Theories for Nonlinear Noise

> Method for analyzing correlated nonlinear noise in recurrent neural circuits using Gaussian-equivalent processes and lognormal moment closure.

## Metadata
- **Source**: arXiv:2601.15462
- **Authors**: Shoshana Chipman, Brent Doiron
- **Published**: 2026-01-21
- **Category**: q-bio.NC

## Core Methodology

### Problem Statement
Strong, correlated noise in recurrent neural circuits passes through nonlinear transfer functions, complicating dynamical mean-field analyses of transients and bifurcations.

### Key Innovation
Replace nonlinear functions of Ornstein-Uhlenbeck (OU) noise with a **Gaussian-equivalent process** matched in mean and covariance, combined with **lognormal moment closure** for expansive nonlinearities.

### Applications
- Order-one transients in recurrent networks
- Fixed point analysis with noise
- Noise-induced shifts of bifurcation structure
- Strong-fluctuation regime analysis

## Implementation Guide

### Prerequisites
```python
import numpy as np
import scipy.integrate as integrate
from scipy.stats import norm, lognorm
```

### Gaussian-Equivalent Process
```python
def gaussian_equivalent_ou(noise_process, nonlinearity):
    """
    Replace nonlinear function of OU noise with Gaussian-equivalent.
    
    Matches mean and covariance of the nonlinear transformation.
    
    Args:
        noise_process: Ornstein-Uhlenbeck process
        nonlinearity: Nonlinear transfer function (e.g., ReLU, sigmoid)
    
    Returns:
        GaussianProcess with matched mean and covariance
    """
    mean = compute_mean(nonlinearity(noise_process))
    cov = compute_covariance(nonlinearity(noise_process))
    return GaussianProcess(mean=mean, covariance=cov)

def compute_mean(transformed_process):
    """Compute mean of transformed OU process."""
    return np.mean(transformed_process)

def compute_covariance(transformed_process):
    """Compute covariance of transformed OU process."""
    # Use empirical covariance or analytical approximation
    return np.cov(transformed_process.T)
```

### Lognormal Moment Closure
```python
def lognormal_moment_closure(moments, order=2):
    """
    Apply lognormal moment closure for expansive nonlinearities.
    
    Args:
        moments: List of moments [m1, m2, ...]
        order: Closure order
    
    Returns:
        Closed-form moment expressions
    """
    if order == 2:
        # Lognormal closure: E[x^n] in terms of mean and variance
        mu = moments[0]
        sigma2 = moments[1] - moments[0]**2
        return compute_lognormal_moments(mu, sigma2)
    
def compute_lognormal_moments(mu, sigma2):
    """
    Compute moments for lognormal distribution.
    
    E[X^n] = exp(n*mu + n^2*sigma^2/2)
    """
    moments = {}
    for n in range(1, 5):  # First 4 moments
        moments[n] = np.exp(n * mu + n**2 * sigma2 / 2)
    return moments
```

### Dynamic Mean Field Theory
```python
class DynamicMeanFieldTheory:
    """
    Dynamic mean field theory for recurrent neuronal networks
    with nonlinear noise processing.
    """
    def __init__(self, network_params):
        self.params = network_params
        self.tau = network_params.get('tau', 10.0)  # Time constant
        self.J = network_params.get('J', 1.0)  # Coupling strength
        
    def mean_field_equations(self, m, C, t):
        """
        Mean field equations for order parameters.
        
        Args:
            m: Mean activity
            C: Covariance
            t: Time
        
        Returns:
            dm/dt, dC/dt
        """
        # Self-consistent mean field equations
        dm_dt = (-m + self.phi(m, C)) / self.tau
        dC_dt = self.compute_covariance_dynamics(m, C)
        return dm_dt, dC_dt
    
    def phi(self, m, C):
        """
        Mean field transfer function with Gaussian-equivalent approximation.
        """
        # Apply moment closure
        moments = [m, C]
        closed_moments = lognormal_moment_closure(moments)
        
        # Compute effective input
        effective_input = self.J * m + np.sqrt(C) * np.random.randn()
        return np.maximum(effective_input, 0)  # ReLU-like
    
    def compute_transients(self, initial_state, T=100):
        """
        Compute order-one transients using mean field theory.
        """
        def dynamics(t, y):
            m, C = y[0], y[1]
            dm_dt, dC_dt = self.mean_field_equations(m, C, t)
            return [dm_dt, dC_dt]
        
        solution = integrate.solve_ivp(
            dynamics, [0, T], initial_state, dense_output=True
        )
        return solution
```

## Applications

### Noise-Induced Bifurcation Shifts
```python
def analyze_bifurcation_structure(drift, diffusion, noise_strength):
    """
    Analyze how noise affects bifurcation structure.
    
    Uses Gaussian-equivalent approximation to handle
    nonlinear noise terms.
    """
    # Compute effective drift with noise correction
    effective_drift = drift + noise_correction(diffusion, noise_strength)
    
    # Find fixed points and their stability
    fixed_points = find_fixed_points(effective_drift)
    stability = analyze_stability(effective_drift, fixed_points)
    
    return fixed_points, stability
```

### Strong-Fluctuation Regime Analysis
```python
def strong_fluctuation_analysis(network_activity, noise_params):
    """
    Analyze network in strong-fluctuation regime.
    
    Standard linearization fails here - requires
    Gaussian-equivalent treatment.
    """
    # Transform to Gaussian-equivalent process
    gaussian_equiv = gaussian_equivalent_ou(
        network_activity, 
        nonlinearity='relu'
    )
    
    # Apply mean field theory
    mft = DynamicMeanFieldTheory(network_params)
    transients = mft.compute_transients(gaussian_equiv.mean)
    
    return transients
```

## Comparison with Standard Linearization

| Approach | Applicability | Accuracy | Computational Cost |
|----------|--------------|----------|-------------------|
| **Gaussian-Equivalent + Lognormal Closure** | Strong fluctuations, nonlinear noise | High | Moderate |
| Standard Linearization | Weak noise, near-fixed points | Moderate | Low |
| Monte Carlo | Any regime | Exact (statistically) | High |

## Pitfalls
- **Closure approximation error**: Lognormal closure assumes specific distribution shape
- **Non-expansive nonlinearities**: Method designed for expansive (e.g., ReLU-like) functions
- **High-dimensional systems**: Moment closure becomes complex in high dimensions

## Related Skills
- neural-population-dynamics
- recurrent-neural-network-analysis
- spiking-neural-network-analysis

## References
- arXiv:2601.15462 - Dynamic Mean Field Theories for Nonlinear Noise in Recurrent Neuronal Networks
