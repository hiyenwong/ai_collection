---
name: minimal-network-brain-dynamics-mean-field
version: v1.0.0
last_updated: 2026-05-06
description: "Interacting branching model of neural network dynamics with hierarchy of analytical mean-field approximations. Characterizes nonequilibrium phase transitions between disorder and ordered phases, exhibits criticality and self-organized dynamics relevant to brain function. Based on arXiv:2512.22093."
category: ai_collection
tags: ["brain-network", "neural-dynamics", "mean-field", "branching-process", "criticality", "phase-transition", "self-organization"]
related_skills: ["neural-critical-dynamics-theory", "generative-brain-dynamics-models", "brain-state-transition-network-control", "spiking-neural-network-analysis"]
---

# Minimal Network of Brain Dynamics: Hierarchy of Analytical Mean-Field Approximations

## Overview

This skill implements an **interacting branching model** of neural network dynamics that incorporates key biological features including inhibition with several types of inhibitory interactions. It establishes a **hierarchy of analytical mean-field approximations** that characterizes nonequilibrium phase transitions between disorder and ordered phases, with stability analysis showing rich dynamical behavior including **criticality** and **self-organized dynamics** relevant to brain function.

**Paper:** "A Minimal Network of Brain Dynamics: Hierarchy of Analytical Mean-Field Approximations" — arXiv:2512.22093 (December 2025).

## Activation Keywords
- interacting branching model brain
- mean-field approximation neural dynamics
- nonequilibrium phase transition brain
- criticality brain network model
- self-organized brain dynamics
- branching process neural network
- analytical mean-field hierarchy
- 脑动力学平均场近似
- 分支过程神经网络
- 脑网络临界性

## Core Methodology

### Problem
Understanding how large-scale brain dynamics emerge from local neuronal interactions requires bridging microscopic spiking behavior and macroscopic population dynamics. Traditional mean-field approaches often oversimplify inhibitory interactions and miss critical phenomena.

### Solution: Interacting Branching Model with Mean-Field Hierarchy

The model treats neural activity as a **branching process** where:
- Each active neuron can "spawn" activity in downstream neurons
- Inhibition modulates branching probabilities
- Multiple inhibitory interaction types capture biological realism

### Key Components

#### 1. Branching Process Foundation
- **Offspring distribution**: Probability that an active neuron activates k downstream neurons
- **Branching ratio (σ)**: Expected number of secondary activations per active neuron
- **Critical point**: σ = 1 separates subcritical (dying out) and supercritical (explosive) regimes

#### 2. Inhibitory Interaction Types
The model incorporates multiple inhibition mechanisms:
- **Feedforward inhibition**: Inhibitory interneurons suppress downstream excitation
- **Feedback inhibition**: Activity-dependent inhibitory feedback loops
- **Lateral inhibition**: Competition between neighboring neural populations
- **Disinhibition**: Inhibition of inhibitory neurons (double negative)

#### 3. Mean-Field Approximation Hierarchy

**Level 1: Naive Mean-Field**
- Assumes independence between neurons
- d⟨n⟩/dt = (σ - 1)⟨n⟩ - γ⟨n⟩²
- Captures basic branching dynamics but misses correlations

**Level 2: Pair Approximation**
- Tracks pairwise correlations ⟨nᵢnⱼ⟩
- Accounts for local clustering effects
- More accurate near critical point

**Level 3: Cluster/Group Approximation**
- Tracks higher-order correlations
- Captures network structure effects
- Most accurate but computationally intensive

#### 4. Phase Transition Analysis

The model exhibits **nonequilibrium phase transitions**:
- **Disordered phase**: Low activity, stable fixed point at n ≈ 0
- **Ordered phase**: Sustained activity, non-zero fixed point
- **Critical point**: Power-law distributed avalanches, maximal dynamic range

#### 5. Stability Analysis
- Linear stability of fixed points
- Bifurcation analysis for parameter regimes
- Lyapunov exponents for chaotic regimes

## Mathematical Framework

### Branching Process Dynamics

Let n(t) be the number of active neurons at time t:

```
n(t+1) = Σᵢ ξᵢ(t)
```

where ξᵢ(t) ~ offspring distribution with mean σ and variance σ²

### Mean-Field Equation (Level 1)

```
dn/dt = (σ - 1)n - γn² + η(t)
```

- σ: branching ratio (control parameter)
- γ: saturation/inhibition strength
- η(t): noise term

### With Inhibition

```
dn_E/dt = (σ_EE - 1)n_E - σ_EI·n_I·n_E - γ_E·n_E²
dn_I/dt = σ_IE·n_E - (σ_II + 1)n_I - γ_I·n_I²
```

- n_E: excitatory population
- n_I: inhibitory population
- σ_XY: branching from Y to X type

### Critical Point

At criticality (σ = 1):
- Activity follows power-law: P(s) ~ s^(-3/2)
- Correlation length diverges
- System maximizes information processing capacity

## Implementation Workflow

### Step 1: Define Network Parameters
- Excitatory/inhibitory neuron ratios
- Connection probabilities
- Branching ratios for each interaction type
- Inhibition strengths

### Step 2: Choose Mean-Field Level
- Level 1 for quick analysis and parameter sweeps
- Level 2 for accurate critical point estimation
- Level 3 for detailed network structure effects

### Step 3: Solve Mean-Field Equations
- Fixed point analysis
- Linear stability analysis
- Numerical integration for time dynamics

### Step 4: Phase Diagram Construction
- Vary control parameters (σ, inhibition strength)
- Identify phase boundaries
- Locate critical points

### Step 5: Validation Against Simulation
- Compare mean-field predictions with Monte Carlo simulations
- Quantify approximation errors at each level
- Identify regimes where mean-field breaks down

## Code Implementation

```python
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

class BranchingNeuralModel:
    """Interacting branching model of neural network dynamics."""
    
    def __init__(self, sigma_EE=1.0, sigma_EI=0.3, sigma_IE=0.5, 
                 sigma_II=0.1, gamma_E=0.01, gamma_I=0.01):
        self.sigma_EE = sigma_EE  # E->E branching
        self.sigma_EI = sigma_EI  # I->E inhibition
        self.sigma_IE = sigma_IE  # E->I activation
        self.sigma_II = sigma_II  # I->I branching
        self.gamma_E = gamma_E    # E saturation
        self.gamma_I = gamma_I    # I saturation
    
    def mean_field_ode(self, y, t):
        """Level 1 mean-field ODEs."""
        n_E, n_I = y
        
        dn_E_dt = (self.sigma_EE - 1) * n_E - self.sigma_EI * n_I * n_E - self.gamma_E * n_E**2
        dn_I_dt = self.sigma_IE * n_E - (self.sigma_II + 1) * n_I - self.gamma_I * n_I**2
        
        return [dn_E_dt, dn_I_dt]
    
    def find_fixed_points(self):
        """Find equilibrium states."""
        # Trivial fixed point
        fixed_points = [(0, 0)]
        
        # Non-trivial fixed points (solve analytically or numerically)
        # For the excitatory-only case:
        if self.sigma_EE > 1:
            n_E_star = (self.sigma_EE - 1) / self.gamma_E
            fixed_points.append((n_E_star, 0))
        
        return fixed_points
    
    def stability_analysis(self, n_E, n_I):
        """Linear stability analysis at fixed point."""
        # Jacobian matrix
        J = np.array([
            [self.sigma_EE - 1 - 2*self.gamma_E*n_E - self.sigma_EI*n_I, 
             -self.sigma_EI*n_E],
            [self.sigma_IE, 
             -(self.sigma_II + 1) - 2*self.gamma_I*n_I]
        ])
        
        eigenvalues = np.linalg.eigvals(J)
        stable = np.all(np.real(eigenvalues) < 0)
        return stable, eigenvalues
    
    def simulate(self, n_E0=0.01, n_I0=0.005, t_max=100, dt=0.1):
        """Simulate mean-field dynamics."""
        t = np.arange(0, t_max, dt)
        y0 = [n_E0, n_I0]
        
        sol = odeint(self.mean_field_ode, y0, t)
        return t, sol[:, 0], sol[:, 1]
    
    def phase_diagram(self, sigma_range=(0.5, 2.0), inhibition_range=(0.1, 1.0), 
                      resolution=50):
        """Compute phase diagram."""
        sigmas = np.linspace(*sigma_range, resolution)
        inhibitions = np.linspace(*inhibition_range, resolution)
        
        phases = np.zeros((resolution, resolution))
        
        for i, sigma_EE in enumerate(sigmas):
            for j, sigma_EI in enumerate(inhibitions):
                self.sigma_EE = sigma_EE
                self.sigma_EI = sigma_EI
                
                stable, eigs = self.stability_analysis(0, 0)
                phases[j, i] = 0 if stable else 1  # 0=disordered, 1=ordered
        
        return sigmas, inhibitions, phases


# Example usage
model = BranchingNeuralModel(sigma_EE=1.2, sigma_EI=0.3, sigma_IE=0.5)

# Find fixed points
fps = model.find_fixed_points()
print(f"Fixed points: {fps}")

# Stability analysis
for fp in fps:
    stable, eigs = model.stability_analysis(*fp)
    print(f"FP {fp}: stable={stable}, eigenvalues={eigs}")

# Simulate
t, n_E, n_I = model.simulate()

# Phase diagram
sigmas, inhibitions, phases = model.phase_diagram()
```

## Applications

1. **Brain Criticality Analysis**: Test whether neural systems operate near critical points
2. **Phase Transition Modeling**: Study transitions between different brain states
3. **Inhibition Mechanism Analysis**: Understand how different inhibition types affect dynamics
4. **Self-Organization**: Model how brain networks self-organize to critical regimes
5. **Epilepsy Modeling**: Supercritical regimes as seizure-like states
6. **Neuromodulation**: Study how neuromodulators shift operating points

## Validation & Verification

### Mean-Field Accuracy
- Compare with direct Monte Carlo simulations
- Quantify error at each approximation level
- Identify parameter regimes where mean-field is valid

### Critical Signatures
- Power-law distributed activity avalanches
- Diverging correlation length near critical point
- Maximal dynamic range at criticality
- Long-range temporal correlations

### Biological Plausibility
- Match experimentally observed firing rates
- Reproduce known inhibition effects
- Consistent with neurophysiological data

## Resources
- **Paper:** https://arxiv.org/abs/2512.22093
- **Related concepts:** Branching processes, mean-field theory, nonequilibrium phase transitions, neural criticality

## Related Skills
- neural-critical-dynamics-theory (neural criticality theory)
- generative-brain-dynamics-models (brain dynamics modeling)
- brain-state-transition-network-control (brain state transitions)
- spiking-neural-network-analysis (SNN analysis methods)
- griffiths-phase-brain-criticality (Griffiths phase in brain criticality)
- hierarchical-brain-criticality (hierarchical critical dynamics)
