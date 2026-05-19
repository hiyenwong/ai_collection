---
name: lattice-field-theory-neurons
description: Simplified Lattice Field Theory (LFT) framework for interpreting Brain-Computer Interface recordings. Modifies Maximum Entropy models to account for time evolution, interpreting neural dynamics through Free Energy principle (FEP). Activation: lattice field theory, LFT neural networks, maximum entropy neural model, free energy principle.
version: 1.0.0
author: Research Synthesis
license: MIT
metadata:
  hermes:
    tags: [neuroscience, lattice-field-theory, brain-computer-interface, maximum-entropy, free-energy-principle]
    source_paper: "Lattice Field Theory for a network of real neurons (arXiv:2604.05251)"
    citations: 0
    related_skills: [brain-connectivity-analysis, neural-dynamics-analysis]
---

# Lattice Field Theory for Neural Networks

## Overview
This skill implements a simplified Lattice Field Theory (LFT) framework that interprets experimental recordings from Brain-Computer Interfaces (BCIs) in a physically grounded way. The method modifies Maximum Entropy models for neural networks to incorporate time evolution, interpreting neural dynamics through the Free Energy Principle (FEP).

## Core Concepts

### 1. Lattice Field Theory (LFT) Framework
- **Purpose**: Interpret spike raster data from chronic multi-site BCIs
- **Foundation**: Maximum Entropy models extended with temporal dynamics
- **Interpretation**: Alternative formulation of Free Energy Principle

### 2. Maximum Entropy Model Extension
- Traditional models capture static correlations
- LFT adds time evolution as a fundamental constraint
- Enables dynamic interpretation of neural population activity

### 3. Free Energy Principle Connection
- Neural activity minimizes variational free energy
- Provides normative framework for neural computation
- Connects to predictive coding and Bayesian brain hypotheses

## Implementation Pattern

```python
import numpy as np
from scipy.special import softmax

class LatticeFieldTheoryNN:
    """
    Lattice Field Theory framework for neural network analysis
    Interprets spike raster data using maximum entropy with temporal dynamics
    """
    
    def __init__(self, n_neurons, temperature=1.0):
        self.n_neurons = n_neurons
        self.T = temperature
        self.J = np.zeros((n_neurons, n_neurons))
        self.h = np.zeros(n_neurons)
        
    def free_energy(self, state):
        E = -0.5 * np.dot(state, np.dot(self.J, state)) - np.dot(self.h, state)
        p = (state + 1) / 2
        S = -np.sum(p * np.log(p + 1e-10) + (1-p) * np.log(1-p + 1e-10))
        return E - self.T * S
    
    def learn_from_spikes(self, spike_raster, learning_rate=0.01):
        empirical_corr = np.corrcoef(spike_raster.T)
        self.J += learning_rate * (empirical_corr - self.J)
        self.h += learning_rate * (np.mean(spike_raster, axis=0) - self.h)
    
    def predict_next_state(self, current_state, dt=0.1):
        force = np.dot(self.J, current_state) + self.h
        noise = np.random.normal(0, np.sqrt(2 * self.T * dt), self.n_neurons)
        next_state = current_state + dt * force + noise
        return np.where(next_state > 0, 1, 0)
```

## Applications
1. BCI Data Interpretation
2. Neural Dynamics Modeling
3. Free Energy Principle Validation

## References
- Bardella et al., Entropy 26 (6), 495 (2024)
- arXiv:2604.05251
- Friston, K. (2010). The free-energy principle
