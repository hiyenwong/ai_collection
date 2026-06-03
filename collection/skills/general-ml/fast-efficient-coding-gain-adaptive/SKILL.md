---
name: fast-efficient-coding-gain-adaptive
description: Fast efficient coding and sensory adaptation in gain-adaptive recurrent networks — unified mechanistic model reconciling adapter-repulsion and prior-attraction phenomena via gain modulation.
tags: [neuroscience, efficient-coding, sensory-adaptation, gain-modulation, recurrent-networks, computational-neuroscience, tuning-curves, neural-dynamics]
created: 2026-05-27
source: "DOI: 10.1038/s41467-026-73032-0 | PMID: 42140911"
---

# Fast Efficient Coding and Sensory Adaptation in Gain-Adaptive Recurrent Networks

## Overview

This methodology from Prat-Carrabin, Harl & Gershman (Nature Communications, 2026) proposes a **gain-adaptive recurrent sensory network model** that unifies two seemingly contradictory sensory adaptation phenomena:
- **Adapter repulsion**: tuning curves shift away from adapting stimuli
- **Prior attraction**: tuning curves shift toward frequently encountered stimuli

The key insight is that gains modulating neural responses optimize an **efficient-coding objective** that balances accuracy and spiking cost — and the propagation of these modulated gains through recurrent connectivity produces rapid, context-appropriate tuning curve adaptation.

## Core Mechanism

### Gain-Adaptive Efficient Coding
- Neuronal gains are optimized online to balance **reconstruction accuracy** vs. **metabolic (spiking) cost**
- Objective: `max_gains [I(stimulus; response) - λ · E[spike_count]]`
- Gains adapt quickly (sub-second) in response to changing stimulus statistics

### Recurrent Gain Propagation
- Gain changes in early sensory neurons propagate through recurrent connections
- Creates emergent adaptation across the network without explicit global coordination
- Accounts for multi-stage cortical processing effects

### Unified Prediction Framework
| Condition | Prior Shape | Predicted Effect | Mechanism |
|-----------|-------------|-----------------|-----------|
| Peaked prior (narrow) | Unimodal | **Adapter repulsion** | High gain at adapter frequency → shift away |
| Broad prior (flat) | Diffuse | **Prior attraction** | Low gain → shift toward high-probability region |

## Key Findings

1. **Adapter repulsion under peaked priors**: When stimulus distributions are concentrated (peaked), repeated presentation causes tuning curves to repel from the adapter stimulus — explained by local gain saturation
2. **Prior attraction under broad distributions**: For wider stimulus distributions, the model predicts (and behavioral evidence confirms) attraction toward the high-probability region
3. **Reconciliation**: The same gain-modulation mechanism produces both effects depending on prior shape — no contradiction
4. **Fast adaptation**: The model operates on behaviorally-relevant timescales (hundreds of milliseconds to seconds)

## Implementation

```python
import numpy as np
from scipy.optimize import minimize

class GainAdaptiveNeuron:
    """Efficient-coding gain-adaptive neuron model."""
    
    def __init__(self, preferred_stimulus, tuning_width=1.0, lambda_cost=0.1):
        self.s0 = preferred_stimulus       # Preferred stimulus
        self.sigma = tuning_width           # Tuning width
        self.lam = lambda_cost             # Spiking cost weight
        self.gain = 1.0                    # Adaptive gain
    
    def tuning_curve(self, stimulus):
        """Gaussian tuning curve with adaptive gain."""
        base = np.exp(-0.5 * ((stimulus - self.s0) / self.sigma) ** 2)
        return self.gain * base
    
    def efficient_coding_objective(self, gain, stimuli, prior):
        """Objective: accuracy - lambda * expected spikes."""
        responses = gain * np.exp(-0.5 * ((stimuli - self.s0) / self.sigma) ** 2)
        # Mutual information approximation via Fisher information
        fisher_info = np.sum(prior * (responses ** 2))
        expected_spikes = np.sum(prior * responses)
        return -(fisher_info - self.lam * expected_spikes)
    
    def adapt_gain(self, stimuli, prior):
        """Update gain to maximize efficient coding objective."""
        result = minimize(self.efficient_coding_objective, [self.gain],
                         args=(stimuli, prior), method='L-BFGS-B',
                         bounds=[(0.01, 10.0)])
        self.gain = result.x[0]
        return self.gain

class RecurrentGainAdaptiveNetwork:
    """Recurrent network with gain-adaptive efficient coding."""
    
    def __init__(self, n_neurons, stimulus_range, recurrent_weight=0.3):
        self.n = n_neurons
        self.s_range = stimulus_range
        self.W_rec = recurrent_weight   # Recurrent connectivity strength
        self.neurons = [
            GainAdaptiveNeuron(s) for s in np.linspace(*stimulus_range, n_neurons)
        ]
    
    def propagate_gains(self, gains):
        """Propagate gain changes through recurrent connectivity."""
        # Gains interact via recurrent connections
        delta_gains = self.W_rec * (np.mean(gains) - gains)
        return gains + delta_gains
    
    def adapt(self, stimuli, prior, n_steps=10):
        """Iterate gain adaptation + recurrent propagation."""
        gains = np.array([n.gain for n in self.neurons])
        for _ in range(n_steps):
            # Update individual gains
            gains = np.array([
                n.adapt_gain(stimuli, prior) for n in self.neurons
            ])
            # Propagate through recurrent connections
            gains = self.propagate_gains(gains)
        return gains
```

## When to Use

- Modeling sensory adaptation phenomena in auditory/visual/olfactory cortex
- Building efficient neural encoding models with metabolic constraints
- Studying gain modulation mechanisms in sensory processing
- Computational modeling of adapter repulsion and prior attraction
- Reconciling conflicting findings in human/animal psychophysics experiments
- Neural population coding models under nonstationary stimuli

## Pitfalls

- The lambda (spiking cost) parameter must be tuned per neural population
- Model assumes quasi-stationary prior within adaptation timescale
- Recurrent weight strength determines balance between local and distributed adaptation
- Behavioral evidence for broad-prior attraction may require many trials to observe

## Key Parameters

| Parameter | Description | Typical Range |
|-----------|-------------|---------------|
| `lambda` | Spiking cost weight | 0.01–1.0 |
| `sigma` | Tuning curve width | 1–10 (stimulus units) |
| `W_rec` | Recurrent strength | 0.1–0.5 |
| `n_steps` | Adaptation iterations | 5–20 |

## References

- Prat-Carrabin A, Harl MV, Gershman SJ. "Fast efficient coding and sensory adaptation in gain-adaptive recurrent networks." *Nature Communications*, 2026. DOI: 10.1038/s41467-026-73032-0
- Atiani S et al. "Task difficulty and performance induce diverse adaptive patterns in gain and shape of primary auditory cortical tuning curves." *Neuron*, 2009.
- Wei XX, Stocker AA. "A Bayesian observer model constrained by efficient coding can explain 'anti-Bayesian' percepts." *Nature Neuroscience*, 2015.
