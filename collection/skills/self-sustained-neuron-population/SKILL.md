---
name: self-sustained-neuron-population
description: Modeling self-sustained neural activity in recurrent networks without external stimuli. Covers dynamical systems analysis, attractor states, and autonomous neural dynamics. Activation: self-sustained, autonomous neural activity, recurrent network dynamics, attractor states, internal neural dynamics.
version: 1.0.0
metadata:
  hermes:
    source_paper: "Modeling of Self-sustained Neuron Population without External Stimulus (arXiv:2604.13719)"
    tags: [computational-neuroscience, recurrent-networks, attractor-dynamics, self-sustained]
---

# Self-Sustained Neuron Population Modeling

## Overview
Methodology for modeling populations of neurons that maintain activity autonomously without requiring external stimuli. This is fundamental to understanding working memory, persistent activity, and intrinsic brain dynamics.

## Source Paper
- **Title:** Modeling of Self-sustained Neuron Population without External Stimulus
- **arXiv:** 2604.13719v1
- **Authors:** İhsan Ertuğrul Karakaş, Özden Özel, İlkay Ulusoy, Orhan Murat Koçak
- **Published:** 2026-04-15

## Core Concepts

### Self-Sustained Activity
Neural populations that maintain elevated firing rates without continuous external input. Key mechanisms:
- **Recurrent excitation:** Positive feedback loops within the network
- **Balance of excitation/inhibition:** Preventing runaway activity
- **Attractor dynamics:** Stable fixed points in state space

### Dynamical Systems Framework
```
dx/dt = -x + W*f(x) + I_ext
```
Where:
- x: neural state vector
- W: recurrent weight matrix
- f: activation function
- I_ext: external input (can be zero for self-sustained)

### Key Analysis Methods
1. **Fixed point analysis:** Find states where dx/dt = 0
2. **Linear stability:** Eigenvalues of Jacobian at fixed points
3. **Bifurcation analysis:** How behavior changes with parameters
4. **Mean-field reduction:** Population-level dynamics

## Implementation

```python
import numpy as np

class SelfSustainedNetwork:
    def __init__(self, n_neurons, connection_prob=0.1, g=1.5):
        self.n = n_neurons
        W = np.random.randn(n_neurons, n_neurons) * g / np.sqrt(n_neurons)
        mask = np.random.random((n_neurons, n_neurons)) < connection_prob
        self.W = W * mask
        self.tau = 10.0

    def dynamics(self, x, I_ext=None):
        # Rate model dynamics
        if I_ext is None:
            I_ext = np.zeros_like(x)
        f_x = np.maximum(x, 0)
        dx = (-x + self.W @ f_x + I_ext) / self.tau
        return dx

    def find_fixed_points(self, n_init=100):
        # Find stable fixed points via gradient descent
        fixed_points = []
        for _ in range(n_init):
            x = np.random.randn(self.n) * 0.1
            for _ in range(10000):
                dx = self.dynamics(x)
                x = x + 0.01 * dx
                if np.linalg.norm(dx) < 1e-6:
                    fixed_points.append(x.copy())
                    break
        return fixed_points

    def simulate(self, x0, I_ext=None, T=1000, dt=0.1):
        # Simulate network dynamics
        if I_ext is None:
            I_ext = np.zeros(self.n)
        t_steps = int(T / dt)
        history = np.zeros((t_steps, self.n))
        x = x0.copy()
        for i in range(t_steps):
            history[i] = x
            dx = self.dynamics(x, I_ext)
            x = x + dt * dx
        return history
```

## Applications
- Working memory modeling
- Persistent activity in prefrontal cortex
- Autonomous neural computation
- Baseline activity maintenance

## Related
- [[working-memory-heterogeneous-delays]]
- [[attractor-metadynamics-neural]]
- [[computational-neuroscience-models]]
