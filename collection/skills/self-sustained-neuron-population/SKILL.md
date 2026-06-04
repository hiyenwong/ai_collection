---
name: self-sustained-neuron-population
description: "Modeling self-sustained neural activity in recurrent networks without external input. Hodgkin-Huxley neurons with STDP and stochasticity maintain autonomous sparse firing for 1800+ seconds after brief initialization. Use when studying autonomous brain dynamics, self-sustained activity, spontaneous neural reorganization, or biologically plausible network simulation."
version: 1.0.0
metadata:
  hermes:
    source_paper: "Modeling of Self-sustained Neuron Population without External Stimulus (arXiv:2604.13719)"
    tags: [neuroscience, self-sustained, hodgkin-huxley, stdp, autonomous-activity]
---

# Self-Sustained Neuron Population Modeling

## Overview

Self-sustained neural activity in the absence of ongoing external input is a fundamental feature of nervous system dynamics. Recurrent Hodgkin-Huxley networks with plastic and stochastic synapses sustain long-duration autonomous activity in a sparse firing regime after brief (200ms) initialization.

## Core Mechanism

A recurrent network of 200 neurons (160 excitatory, 40 inhibitory) with 80% connection probability maintains autonomous activity through:
- Excitatory and inhibitory STDP
- Probabilistic vesicle release
- Probabilistic synapse formation
- Receptor variability
- Voltage-dependent inhibition

## Key Results

| Parameter | Value |
|-----------|-------|
| Network size | 200 neurons (160E + 40I) |
| Connection probability | 80% |
| Duration sustained | 1800+ seconds |
| Mean firing rate | 1.13 ± 1.34 Hz |
| Neurons < 1 Hz | 67% |
| Fano factor | 1-2 |

## Implementation Pattern

```python
import numpy as np

class SelfSustainedNetwork:
    """Recurrent HH network with STDP maintaining autonomous activity."""
    
    def __init__(self, n_excitatory=160, n_inhibitory=40, conn_prob=0.8):
        self.n_total = n_excitatory + n_inhibitory
        self.n_exc = n_excitatory
        self.n_inh = n_inhibitory
        self.conn_prob = conn_prob
        
        # Initialize connectivity
        self.weights = self._init_connectivity()
        
    def _init_connectivity(self):
        """Probabilistic synapse formation."""
        W = np.zeros((self.n_total, self.n_total))
        mask = np.random.random(W.shape) < self.conn_prob
        W[mask] = np.random.normal(0, 1, size=mask.sum())
        return W
    
    def apply_stdp(self, pre_spike, post_spike):
        """Excitatory and inhibitory STDP rules."""
        # Asymmetric STDP window
        pass
    
    def initialize(self, duration_ms=200, target_neurons=30):
        """Brief transient stimulation to subset of excitatory neurons."""
        pass
    
    def run_autonomous(self, duration_s=1800):
        """Run without any external input."""
        # Monitor sparse, irregular activity
        # Track Fano factors, participation rates
        pass

# Usage: initialize then run autonomous
net = SelfSustainedNetwork()
net.initialize(duration_ms=200, target_neurons=30)
activity = net.run_autonomous(duration_s=1800)
# Network maintains sparse firing without external drive
```

## Applications

- **Autonomous brain dynamics modeling**: Study self-sustained cortical activity
- **Spontaneous reorganization**: Track qualitative changes in collective firing patterns
- **Neuromorphic systems**: Low-power always-on neural computation
- **Epilepsy research**: Understand transition between sparse and synchronized states

## References

- Original paper: arXiv:2604.13719v1
- Authors: Karakaş, Özel, Ulusoy, Koçak
- Published: 2026-04-15
