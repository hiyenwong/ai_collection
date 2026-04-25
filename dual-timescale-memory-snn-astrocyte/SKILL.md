---
name: dual-timescale-memory-snn-astrocyte
description: "Dual-timescale memory in spiking neuron-astrocyte networks for efficient navigation. Combines long-term memory of successful actions with short-term suppression of recently visited locations using astrocyte-mediated modulation. Use when implementing bio-inspired navigation, working memory in SNNs, or astrocyte-neuron interactions. Triggers: dual timescale memory, astrocyte SNN, spiking navigation, neuron-astrocyte network, efficient exploration."
version: 1.0.0
author: Research Synthesis
license: MIT
metadata:
  hermes:
    source_paper: "Dual-Timescale Memory in a Spiking Neuron-Astrocyte Network for Efficient Navigation (arXiv:2604.14487)"
    citations: 0
    published: "2026-04-15"
    tags:
    - spiking-neural-networks
    - astrocyte
    - dual-timescale
    - memory
    - navigation
    - neuromodulation
---

# Dual-Timescale Memory in Spiking Neuron-Astrocyte Networks

## Overview

This methodology implements dual-timescale memory mechanisms inspired by biological neuron-astrocyte interactions for efficient spatial navigation and exploration.

Based on the paper "Dual-Timescale Memory in a Spiking Neuron-Astrocyte Network for Efficient Navigation" (arXiv:2604.14487, 2026-04-15).

## Core Principles

1. **Long-term memory** (LTM): Stores successful action outcomes via synaptic plasticity (STDP)
2. **Short-term memory** (STM): Suppresses recently visited locations via astrocyte-mediated calcium dynamics
3. **Neuromodulatory coupling**: Astrocytes modulate neuronal excitability based on recent activity history

## Mathematical Framework

### Astrocyte Calcium Dynamics

```
d[Ca2+]/dt = -[Ca2+]/τ_ca + α · Σ δ(t - t_spike)
```

Where:
- `τ_ca`: Calcium decay time constant (~1-10 seconds)
- `α`: Calcium influx per spike
- `t_spike`: Spike times of connected neurons

### Dual-Memory Integration

```
I_modulation = β_LTM · w_syn + β_STM · f([Ca2+])
```

Where:
- `w_syn`: Synaptic weight (LTM component)
- `f([Ca2+])`: Astrocyte-mediated suppression (STM component)
- `β_LTM`, `β_STM`: Scaling factors for each timescale

## Implementation

```python
class AstrocyteModulatedSNN:
    def __init__(self, num_neurons, tau_ca=5.0, alpha=0.1):
        self.tau_ca = tau_ca  # Astrocyte calcium time constant
        self.alpha = alpha    # Calcium influx per spike
        
    def update_calcium(self, spikes, dt):
        """Update astrocyte calcium concentration."""
        dca = -self.ca_conc / self.tau_ca + self.alpha * spikes.sum()
        self.ca_conc += dca * dt
        return self.ca_conc
    
    def modulation_current(self, calcium, synaptic_weights):
        """Compute astrocyte-mediated modulation."""
        ltm = synaptic_weights  # Long-term memory
        stm = torch.exp(-calcium)  # Short-term suppression
        return ltm + stm
    
    def forward(self, spikes, dt):
        calcium = self.update_calcium(spikes, dt)
        modulation = self.modulation_current(calcium, self.weights)
        output = self.neuron_update(spikes, modulation)
        return output
```

## Applications

- Autonomous robot navigation
- Spatial memory systems
- Exploration-exploitation tradeoff
- Neuromorphic edge AI
- Bio-inspired SLAM

## Activation Keywords

dual timescale memory, astrocyte SNN, spiking navigation, neuron-astrocyte network, efficient exploration, calcium dynamics

## Related Skills

- `snn-learning-rules-dynamics` - SNN learning fundamentals
- `working-memory-heterogeneous-delays` - Delay-based working memory
- `neuromorphic-low-power-ai` - Neuromorphic computing


## Related Paper (Latest)

- **Title:** Dual-Timescale Memory in a Spiking Neuron-Astrocyte Network for Efficient Navigation
- **arXiv ID:** 2604.15391v1
- **Published:** 2026-04-16
- **Authors:** Yuliya Tsybina, Evgenia Antonova, Sergey Shchanikov et al.
- **PDF:** https://arxiv.org/pdf/2604.15391v1
