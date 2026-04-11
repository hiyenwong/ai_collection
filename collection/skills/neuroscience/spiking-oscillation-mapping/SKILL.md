---
name: spiking-oscillation-mapping
description: Analyze and map oscillatory states in balanced spiking neural networks. Characterizes transitions between silent, asynchronous-irregular, and oscillatory states based on synaptic and temporal parameters. Activation: spiking network oscillation, regime mapping, balanced network.
version: 1.0.0
author: Research Synthesis
license: MIT
metadata:
  hermes:
    tags: [neuroscience, spiking-neural-networks, oscillation, balanced-network, regime-mapping]
    source_paper: "Regime Mapping of Oscillatory States in Balanced Spiking Networks (arXiv:2604.04770)"
    citations: 0
---

# Spiking Network Oscillation Regime Mapping

## Overview
Systematic mapping of oscillatory regimes in balanced spiking neural networks. Characterizes how postsynaptic decay, conduction delay, and plasticity rate jointly shape transitions between silent, asynchronous-irregular (AI), and oscillatory (OSC) states.

## Core Concepts
- Balanced Spiking Networks
- Oscillatory States (SILENT, AI, SI, OSC)
- Parameter Space Exploration

## Implementation Pattern

```python
import numpy as np

class SpikingNetworkRegimeMapper:
    def __init__(self, N_exc=4000, N_inh=1000):
        self.N_exc = N_exc
        self.N_inh = N_inh
        
    def analyze_dynamics(self, spike_times, duration=1000):
        if len(spike_times) < 10:
            return {'regime': 'SILENT', 'firing_rate': 0}
        
        firing_rate = len(spike_times) / (self.N * duration / 1000)
        
        # Population activity binning
        bin_size = 5  # ms
        bins = np.arange(0, duration + bin_size, bin_size)
        pop_activity, _ = np.histogram(spike_times, bins=bins)
        
        # Coefficient of variation
        isi = np.diff(spike_times)
        cv_isi = np.std(isi) / np.mean(isi) if len(isi) > 1 else 0
        
        # Fano factor
        fano = np.var(pop_activity) / np.mean(pop_activity) if np.mean(pop_activity) > 0 else 0
        
        # Classify regime
        if firing_rate < 0.1:
            regime = 'SILENT'
        elif fano < 1.5 and cv_isi > 0.8:
            regime = 'AI'
        else:
            regime = 'OSC'
            
        return {'regime': regime, 'firing_rate': firing_rate, 'cv': cv_isi}
```

## Applications
- Cortical Dynamics Modeling
- Neuromorphic Computing
- Clinical Neuroscience

## References
- arXiv:2604.04770
- Brunel (2000)
