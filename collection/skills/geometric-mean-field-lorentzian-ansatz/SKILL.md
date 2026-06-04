---
name: geometric-mean-field-lorentzian-ansatz
version: 1.0.0
description: Geometric origin of exact mean-field reductions using Möbius symmetry and the Lorentzian Ansatz — proving the Cauchy-Lorentz family uniquely emerges as invariant under projective transport, unifying Ott-Antonsen and Montbrió-Pazó-Roxin reductions.
triggers:
  - Lorentzian ansatz
  - mean-field reduction
  - Ott-Antonsen
  - Montbrió-Pazó-Roxin
  - coupled oscillators
  - Riccati dynamics
  - Möbius symmetry
  - Cauchy distribution
  - low-dimensional reduction
  - neural mass model
tags:
  - mean-field-theory
  - computational-neuroscience
  - dynamical-systems
  - mathematical-physics
  - coupled-oscillators
  - spiking-neural-network
  - neural-mass-models
---

# Geometric Origin of Exact Mean-Field Reductions: Möbius Symmetry and the Lorentzian Ansatz

**Source**: arXiv:2605.23669 (May 2026)  
**Authors**: Hugues Berry, Leonardo Trujillo  
**Categories**: physics.bio-ph, q-bio.NC

## Summary

Proves that the privileged role of the Lorentzian (Cauchy) family in low-dimensional reductions of coupled oscillator and spiking neuron systems is geometric rather than heuristic. The Cauchy-Lorentz family is the unique connected two-dimensional family of continuous probability densities invariant under projective transport induced by Riccati dynamics.

## Key Contributions

1. **Geometric Foundation**: Proves the Lorentzian Ansatz has geometric origin via Möbius (projective) symmetry, not just heuristic convenience
2. **Unification**: Provides unified geometric foundation for Ott-Antonsen (2008) and Montbrió-Pazó-Roxin (2015) reductions
3. **Explains Gaussian Failure**: Shows why Gaussian closures fail for these systems
4. **Structural Condition**: Identifies the structural condition underlying exact two-parameter reductions

## Core Mathematical Framework

### Riccati Dynamics → Projective Transport
- The transport induced by Riccati dynamics on probability densities
- Reformulation on the circle via stereographic projection
- Problem reduces to uniqueness of rotation-invariant probability measure

### Key Proof Structure
1. Start with Riccati dynamics on oscillator/spiking neuron populations
2. Transport action on space of probability densities
3. Reformulate on circle S¹ via stereographic projection
4. Uniqueness of rotation-invariant measure → standard Cauchy law
5. Full projective action → Lorentzian family
6. Therefore Cauchy-Lorentz is the unique invariant family

### The Uniqueness Theorem
- **Cauchy-Lorentz family**: The only connected 2D family of continuous probability densities invariant under the induced projective transport
- **On the circle**: Rotation-invariant measure is unique → Dirac delta at uniform angle
- **Under stereographic projection**: This gives the standard Cauchy distribution
- **Under full projective action**: Gives the Lorentzian family

## Implications for Neuroscience

### Neural Mass Models
- Justifies the use of Lorentzian distributions in mean-field models of spiking neurons
- Provides rigorous mathematical backing for firing rate models derived from spiking dynamics

### Why Gaussian Closures Fail
- Gaussian family is NOT invariant under the projective transport
- This explains systematic errors when Gaussian approximations are used for coupled oscillator systems

### Exact Reductions
- **Ott-Antonsen reduction**: Special case of the geometric principle for Kuramoto-type models
- **Montbrió-Pazó-Roxin reduction**: Special case for quadratic integrate-and-fire (QIF) neurons
- Both are manifestations of the same underlying Möbius symmetry

## Technical Details

### Riccati Dynamics
- Arises naturally in phase-reduced oscillator models
- Also in voltage dynamics of QIF neurons: dv/dt = v² + η(t)
- The distributional dynamics induce projective transformations on density space

### Möbius (Projective) Symmetry
- Group of fractional linear transformations on the real line
- Acts on probability densities via push-forward
- Cauchy-Lorentz family is the orbit of the Cauchy distribution under this group

## Applications

1. **Neural Mass Models**: Rigorous derivation of low-dimensional firing rate equations from spiking neuron models
2. **Kuramoto Model Analysis**: Exact mean-field descriptions for synchronization transitions
3. **QIF Network Dynamics**: Exact reduction for networks of quadratic integrate-and-fire neurons
4. **Brain Oscillation Modeling**: Theoretical foundation for modeling macroscopic brain rhythms

## Implementation Guidance

```python
import numpy as np
from scipy import stats

class LorentzianMeanField:
    """
    Exact mean-field reduction using Lorentzian ansatz.
    The Lorentzian (Cauchy) distribution is the unique invariant family
    under projective transport from Riccati dynamics.
    """
    def __init__(self, n_neurons=1000, J=1.0, tau_m=10.0):
        self.n = n_neurons
        self.J = J  # coupling strength
        self.tau_m = tau_m
        # Lorentzian parameters: [center, half-width]
        self.r = 0.0  # mean firing rate
        self.v = 0.0  # mean membrane potential
    
    def cauchy_distribution(self, x, center, hwhm):
        """Standard Cauchy (Lorentzian) distribution"""
        return (1.0/np.pi) * hwhm / ((x - center)**2 + hwhm**2)
    
    def mean_field_step(self, dt, eta_mean, eta_std, I_ext=0.0):
        """
        One step of exact mean-field dynamics.
        Parameters derived from Lorentzian invariance principle.
        """
        # Exact 2D reduction equations
        dr_dt = (self.v / (np.pi * self.tau_m) + 
                 eta_std * self.r / (np.pi * self.tau_m))
        dv_dt = (self.v**2 + eta_mean + 
                 self.J * self.r + I_ext - 
                 (np.pi * self.tau_m * self.r)**2)
        
        self.r += dr_dt * dt
        self.v += dv_dt * dt
        self.r = max(self.r, 0)  # firing rate non-negative
```

## Connections to Other Research

- **Ott-Antonsen (2008)**: Kuramoto model mean-field → special case of this geometric principle
- **Montbrió-Pazó-Roxin (2015)**: QIF neural mass → another special case
- **Next-Generation Neural Mass Models**: Provides theoretical justification
- **Dynamic Mean-Field Theory**: Geometric structure underlying mean-field closures
- **Statistical Physics of Neural Networks**: Connects to random matrix and field theory approaches
