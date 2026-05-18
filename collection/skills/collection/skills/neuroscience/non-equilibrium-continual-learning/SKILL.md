---
name: non-equilibrium-continual-learning
description: Non-equilibrium stochastic dynamics framework for understanding insight and repetitive learning in continual learning scenarios. Uses Kramers escape theory to model stability-plasticity dilemma. Activation: continual learning, non-equilibrium dynamics, kramers escape, insight learning.
version: 1.0.0
author: Research Synthesis
license: MIT
metadata:
  hermes:
    tags: [neuroscience, continual-learning, non-equilibrium, kramers-theory, insight-learning]
    source_paper: "Non-Equilibrium Stochastic Dynamics as a Unified Framework for Insight and Repetitive Learning (arXiv:2604.04154)"
    citations: 0
---

# Non-Equilibrium Dynamics for Continual Learning

## Overview
Non-equilibrium statistical physics framework for understanding continual learning. Models the learning system as a particle evolving under Langevin dynamics on a double-well energy landscape, explaining both sudden insight and gradual skill acquisition.

## Core Concepts
- Stability-Plasticity Dilemma
- Double-Well Energy Landscape
- Kramers Escape Theory

## Implementation Pattern

```python
import numpy as np

class KramersContinualLearning:
    def __init__(self, barrier_height=5.0, well_separation=4.0, temperature=0.5):
        self.E_b = barrier_height
        self.x0 = well_separation / 2
        self.T = temperature
        
    def double_well_potential(self, x):
        return self.E_b * ((x / self.x0)**2 - 1)**2
    
    def potential_gradient(self, x):
        return 4 * self.E_b * x * (x**2 - self.x0**2) / (self.x0**4)
    
    def kramers_escape_rate(self):
        omega_0 = np.sqrt(4 * self.E_b / self.x0**2)
        return omega_0 * np.exp(-self.E_b / self.T)
    
    def insight_vs_repetitive(self, task_similarity, learning_time):
        effective_barrier = self.E_b * (1 - task_similarity)
        rate = np.sqrt(4 * effective_barrier / self.x0**2) * np.exp(-effective_barrier / self.T)
        prob = 1 - np.exp(-rate * learning_time)
        mode = 'insight' if rate > 0.1 else 'repetitive'
        return mode, prob
```

## Applications
- Continual Learning Algorithms
- Educational Psychology
- Neuroscience of Learning

## References
- arXiv:2604.04154
- Kramers (1940)
- Hinton & Plaut (1987)
