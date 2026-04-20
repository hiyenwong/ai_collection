---
name: astrocyte-resource-diffusion-neural-fields
description: Astrocytic resource diffusion stabilizes persistent activity in neural field models, bridging metabolic support and neural circuit models
version: 1.0.0
author: Research Synthesis
license: MIT
metadata:
  hermes:
    tags: [astrocytes, neural-fields, working-memory, metabolic-support, persistent-activity]
    source_paper: "Astrocytic resource diffusion stabilizes persistent activity in neural fields (arXiv:2604.10036)"
    authors: "Noah Palmer, Heather L. Cihak, Daniele Avitabile, Zachary P. Kilpatrick"
    published: "2026-04-11"
    category: "neuroscience"
---

# Astrocyte Resource Diffusion in Neural Fields

## Overview
This paper introduces astrocyte network support into spatially extended neural circuit models, demonstrating how astrocytic resource diffusion stabilizes working memory persistent activity. It bridges the gap between metabolic support mechanisms and neural circuit dynamics.

## Key Concepts

### Astrocyte-Neuron Metabolic Coupling
- Astrocytes provide metabolic support to neurons
- Resource diffusion across astrocyte network
- Stabilization of persistent activity states

### Neural Field Model with Astrocytic Support
```
Neural Field (Activity u) <---> Astrocyte Network (Resources r)
                                      |
                               Diffusion Process
```

## Implementation Pattern

```python
import numpy as np
from scipy.ndimage import gaussian_filter

class AstrocyteNeuralField:
    """Neural field model with astrocytic resource diffusion."""
    
    def __init__(self, grid_size=100, dx=0.1, dt=0.01):
        self.grid_size = grid_size
        self.dx = dx
        self.dt = dt
        self.u = np.zeros(grid_size)  # Neural activity
        self.r = np.ones(grid_size)   # Astrocytic resources
        self.w = self._mexican_hat_kernel()
    
    def _mexican_hat_kernel(self):
        """Excitatory center, inhibitory surround kernel."""
        x = np.linspace(-1, 1, self.grid_size)
        w_excite = np.exp(-x**2 / 0.1)
        w_inhibit = 0.5 * np.exp(-x**2 / 0.5)
        return w_excite - w_inhibit
    
    def step(self, stimulus=None):
        """One time step of coupled dynamics."""
        synaptic_input = np.convolve(self.u, self.w, mode='same') * self.dx
        modulated_input = synaptic_input * self.r
        
        du = -self.u + np.tanh(modulated_input)
        if stimulus is not None:
            du += stimulus
        self.u += self.dt * du
        
        # Astrocytic resource dynamics
        consumption = self.u * self.r
        diffusion = gaussian_filter(self.r, sigma=2) - self.r
        dr = -consumption + 0.1 * diffusion + 0.01 * (1 - self.r)
        self.r += self.dt * dr
        self.r = np.clip(self.r, 0, 1)
        
        return self.u.copy(), self.r.copy()
    
    def simulate_working_memory(self, stimulus_duration=100):
        """Simulate working memory with astrocytic stabilization."""
        history = {'u': [], 'r': []}
        
        for t_idx in range(stimulus_duration):
            stimulus = np.exp(-((np.arange(self.grid_size) - 50) ** 2) / 10)
            u, r = self.step(stimulus)
            history['u'].append(u)
            history['r'].append(r)
        
        for t_idx in range(200):
            u, r = self.step()
            history['u'].append(u)
            history['r'].append(r)
        
        return history
```

## Applications
- Working memory modeling
- Metabolic-neural interaction studies
- Neurodegenerative disease modeling
- Brain energy metabolism research

## References
- Astrocytic resource diffusion stabilizes persistent activity in neural fields
- Authors: Noah Palmer, Heather L. Cihak, Daniele Avitabile, Zachary P. Kilpatrick
- arXiv: 2604.10036 (2026-04-11)

## Activation
- astrocyte resource diffusion
- neural field models
- working memory stabilization
- metabolic support
- persistent activity
- 星形胶质细胞
- 神经场模型
- 工作记忆

## Activation Keywords

- "astrocyte-resource-diffusion-neural-fields"
- "astrocyte resource diffusion neural fields"
- "use astrocyte resource diffusion neural fields"
- "astrocyte resource diffusion neural fields help"
- "astrocyte resource diffusion neural fields tool"

## Tools Used

- `Read` - Read existing files and documentation
- `Write` - Create new files and documentation
- `Bash` - Execute commands when needed

## Instructions for Agents

1. Identify user's intent and specific requirements
2. Gather necessary context from files or user input
3. Execute appropriate actions using available tools
4. Provide clear results and suggest next steps

## Examples

### Basic Astrocyte Resource Diffusion Neural Fields usage
```
User: "Help me with astrocyte resource diffusion neural fields"
→ Understand requirements → Execute actions → Provide results
```

### Advanced usage
```
User: "I need detailed astrocyte resource diffusion neural fields assistance"
→ Clarify scope → Provide comprehensive solution → Follow up
```
