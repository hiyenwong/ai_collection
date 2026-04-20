---
name: self-sustained-neuron-population
description: Studies conditions for self-sustained neural activity emergence in biophysically grounded network models without external input
version: 1.0.0
author: Research Synthesis
license: MIT
metadata:
  hermes:
    tags: [self-sustained-activity, neural-populations, autonomous-dynamics, biophysical-models]
    source_paper: "Modeling of Self-sustained Neuron Population without External Stimulus (arXiv:2604.13719)"
    authors: "İhsan Ertuğrul Karakaş, Özden Özel, İlkay Ulusoy, Orhan Murat Koçak"
    published: "2026-04-15"
    category: "neuroscience"
---

# Self-Sustained Neuron Population Modeling

## Overview
Studies conditions for self-sustained neural activity emergence in biophysically grounded network models without external stimulus. Reveals how intrinsic network properties can maintain persistent activity, relevant for understanding autonomous brain dynamics.

## Key Concepts

### Self-Sustained Activity
- Persistent firing without external input
- Emerges from network connectivity structure
- Requires balance of excitation and inhibition

### Bifurcation Analysis
- Identifies parameter regimes for sustained activity
- Hopf bifurcation transitions
- Critical connectivity thresholds

## Implementation Pattern

```python
import numpy as np

class SelfSustainedNetwork:
    """Biophysically grounded neuron population model."""
    
    def __init__(self, n_neurons=100, connectivity=0.1):
        self.n = n_neurons
        self.v = np.random.randn(n_neurons) * 0.1
        self.w = self._generate_connectivity(connectivity)
    
    def _generate_connectivity(self, p):
        """Sparse random connectivity with E/I balance."""
        w = np.random.randn(self.n, self.n) * p
        mask = np.random.random((self.n, self.n)) > p
        w[mask] = 0
        # Balance excitation and inhibition
        w = w - np.mean(w)
        return w
    
    def step(self, dt=0.01):
        """Dynamics without external input."""
        # Wilson-Cowan style dynamics
        firing = 1 / (1 + np.exp(-5 * (self.v - 0.5)))
        input_current = self.w @ firing
        
        # Intrinsic dynamics
        dv = -self.v + input_current
        self.v += dt * dv
        
        return self.v.copy(), firing
    
    def check_self_sustained(self, steps=1000):
        """Check if activity sustains without input."""
        for _ in range(steps):
            v, firing = self.step()
        
        mean_firing = np.mean(firing)
        return mean_firing > 0.01  # Threshold for sustained activity
```

## Applications
- Autonomous neural dynamics
- Baseline brain activity modeling
- Epilepsy research
- Resting-state network analysis

## References
- Modeling of Self-sustained Neuron Population without External Stimulus
- Authors: İhsan Ertuğrul Karakaş, Özden Özel, İlkay Ulusoy, Orhan Murat Koçak
- arXiv: 2604.13719 (2026-04-15)

## Activation
- self-sustained neural activity
- autonomous dynamics
- neuron population modeling
- persistent firing
- 自持续神经元群体
- 无外部刺激

## Activation Keywords

- "self-sustained-neuron-population"
- "self sustained neuron population"
- "use self sustained neuron population"
- "self sustained neuron population help"
- "self sustained neuron population tool"

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

### Basic Self Sustained Neuron Population usage
```
User: "Help me with self sustained neuron population"
→ Understand requirements → Execute actions → Provide results
```

### Advanced usage
```
User: "I need detailed self sustained neuron population assistance"
→ Clarify scope → Provide comprehensive solution → Follow up
```
