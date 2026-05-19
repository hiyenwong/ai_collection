---
name: snn-internal-noise-analysis
description: Internal noise analysis in Spiking Neural Networks examining additive vs multiplicative noise effects on LIF neurons and trained SNNs. Covers noise injection points (input current, membrane potential, spike generation) and robustness assessment. Activation: snn noise, internal noise spiking neural networks, LIF noise analysis, multiplicative noise SNN.
version: 1.0.0
author: Research Synthesis
license: MIT
metadata:
  hermes:
    tags: [snn, noise-analysis, LIF, robustness, spiking-dynamics]
    source_paper: "General Aspects of Internal Noise in Spiking Neural Networks (arXiv:2604.13612)"
    citations: 0
---

# SNN Internal Noise Analysis

Systematic analysis of internal noise effects on SNNs — additive vs multiplicative noise at different processing stages.

## Paper Metadata
- **arXiv**: 2604.13612
- **Published**: 2026-04-19
- **Categories**: cs.NE, q-bio.NC

## Noise Injection Points

1. **Input current noise**: Added to synaptic input before integration
2. **Membrane potential noise**: Added during leaky integration
3. **Output spike noise**: Added at spike generation threshold

## Noise Types

### Additive Noise
- Independent of signal magnitude
- Sigma constant across all activity levels
- Models: thermal noise, readout noise

### Multiplicative Noise
- Proportional to signal magnitude
- Sigma scales with activity
- Models: synaptic variability, device mismatch

## Analysis Framework

```python
import numpy as np

class NoisyLIFNeuron:
    """LIF neuron with configurable noise injection."""
    
    def __init__(self, tau=20.0, v_thresh=1.0, v_reset=0.0, 
                 noise_type='additive', noise_stage='membrane', sigma=0.1):
        self.tau = tau
        self.v_thresh = v_thresh
        self.v_reset = v_reset
        self.noise_type = noise_type
        self.noise_stage = noise_stage
        self.sigma = sigma
        self.v = v_reset
    
    def step(self, I_input, dt=1.0):
        # Noise injection at input stage
        if self.noise_stage == 'input':
            if self.noise_type == 'additive':
                I_input += np.random.normal(0, self.sigma)
            else:  # multiplicative
                I_input *= (1 + np.random.normal(0, self.sigma))
        
        # Membrane dynamics
        dv = (-self.v + I_input) / self.tau * dt
        
        if self.noise_stage == 'membrane':
            if self.noise_type == 'additive':
                dv += np.random.normal(0, self.sigma) * dt
            else:
                dv *= (1 + np.random.normal(0, self.sigma))
        
        self.v += dv
        
        # Spike generation
        spike = 0
        if self.v >= self.v_thresh:
            spike = 1
            if self.noise_stage == 'spike':
                if np.random.random() < self.sigma:
                    spike = 0  # Noise-induced spike suppression
            self.v = self.v_reset
        
        return spike
```

## Key Findings

- **Multiplicative noise** is more disruptive than additive for trained SNNs
- **Membrane potential noise** has the strongest impact on firing patterns
- **Trained SNNs show robustness** but degrade non-uniformly across layers
- **Noise can be regularizing**: Moderate noise improves generalization

## Applications

- Neuromorphic hardware noise tolerance assessment
- Noise-aware SNN training
- Robust spiking network design
- Biological plausibility analysis

## Related Skills

- snn-learning-survey
- general-aspects-internal-noise-spiking
- noisy-snn-learning
