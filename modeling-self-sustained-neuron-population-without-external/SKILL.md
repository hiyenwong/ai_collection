---
name: modeling-self-sustained-neuron-population-without-external
description: "Modeling self-sustained neuron populations without external stimulus. Demonstrates how recurrent networks maintain persistent activity through internal dynamics alone. Explores mechanisms of sustained firing in absence of external drive. Activation: self-sustained activity, recurrent neural networks, persistent activity, population dynamics, spontaneous activity"
---

# Self-Sustained Neuron Population Modeling

## Overview

Research on modeling self-sustained neuron populations that maintain persistent activity **without any external stimulus**. Demonstrates how recurrent network architectures sustain ongoing neural dynamics through internal connectivity and feedback mechanisms alone, providing insights into working memory, spontaneous brain activity, and baseline cortical dynamics.

## Source Paper

- **Title**: Modeling of Self-sustained Neuron Population without External Stimulus
- **Authors**: İhsan Ertuğrul Karakaş, Özden Özel, İlkay Ulusoy, Orhan Murat Koçak
- **arXiv**: 2604.13719v1
- **Published**: 2026-04-15
- **Categories**: N/A
- **PDF**: https://arxiv.org/pdf/2604.13719v1

## Core Concepts

### Self-Sustained Activity Mechanisms

1. **Recurrent excitation**: Neurons excite each other through feedback loops
2. **Balanced inhibition**: Inhibition prevents runaway excitation
3. **Network structure**: Specific connectivity patterns sustain activity patterns
4. **Intrinsic dynamics**: Individual neuron properties contribute to stability

### Implementation

```python
import numpy as np

class SelfSustainedNetwork:
    """E-I balanced recurrent network with self-sustained activity."""
    
    def __init__(self, n_exc=800, n_inh=200, conn_prob=0.1):
        self.n_exc, self.n_inh = n_exc, n_inh
        self.W_ee = self._sparse(n_exc, n_exc, conn_prob, mean=0.5)
        self.W_ei = self._sparse(n_exc, n_inh, conn_prob, mean=0.5)
        self.W_ie = self._sparse(n_inh, n_exc, conn_prob, mean=-1.0)
        self.W_ii = self._sparse(n_inh, n_inh, conn_prob, mean=-0.5)
        self.r_exc = np.zeros(n_exc)
        self.r_inh = np.zeros(n_inh)
    
    def _sparse(self, r, c, p, mean=0, std=0.1):
        W = np.random.normal(mean, std, (r, c))
        W[np.random.random((r, c)) > p] = 0
        return W
    
    def step(self, dt=1e-3):
        # NO external input - purely self-sustained
        inp_e = self.W_ee @ self.r_exc + self.W_ie.T @ self.r_inh
        inp_i = self.W_ei.T @ self.r_exc + self.W_ii @ self.r_inh
        self.r_exc += (-self.r_exc + np.maximum(0, inp_e)) * dt / 0.02
        self.r_inh += (-self.r_inh + np.maximum(0, inp_i)) * dt / 0.01
        return np.maximum(self.r_exc, 0), np.maximum(self.r_inh, 0)
```

## Applications

- **Working memory models**: Persistent activity as memory substrate
- **Resting-state fMRI**: Understanding spontaneous brain activity
- **Neuromorphic computing**: Low-power always-on neural circuits
- **Epilepsy modeling**: Pathological sustained activity

## Activation Keywords

- self-sustained activity
- persistent neural activity
- recurrent network dynamics
- spontaneous activity
- E-I balance
- population dynamics
