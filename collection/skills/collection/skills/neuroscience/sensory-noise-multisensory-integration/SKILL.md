---
name: sensory-noise-multisensory-integration
description: "Methodology for studying how sensory noise shapes multisensory integration and decision-making. Covers neural variability, reliability-weighted cue combination, and optimal integration frameworks. Based on arXiv:2604.14096 (2026). Triggers: sensory noise, multisensory integration, neural variability, cue combination, decision-making, reliability-weighted, perceptual decision, 感觉噪声, 多感觉整合."
version: 1.0.0
metadata:
  hermes:
    source_paper: "Sensory Noise Shapes Multisensory Integration (arXiv:2604.14096)"
    tags:
      - neuroscience
      - sensory
      - multisensory
      - decision-making
      - neural-variability
---

# Sensory Noise and Multisensory Integration

## Overview

Research on how sensory noise shapes multisensory integration and decision-making processes. Investigates how neural variability influences the reliability-weighted combination of sensory cues and the optimality of perceptual decisions.

## Key Insights

- **Neural variability** acts as a signal, not just noise — it modulates how different sensory cues are weighted during integration
- **Reliability-weighted cue combination**: the brain integrates multiple sensory inputs proportional to their inverse variance (optimal integration)
- **Decision boundaries** are dynamically adjusted based on sensory noise levels
- **Cross-modal interactions** can enhance or suppress perceptual sensitivity depending on noise correlation structure

## Core Methodology

### Reliability-Weighted Integration Model

The optimal multisensory estimate combines cues weighted by their reliability (inverse variance):

```
w_i = (1/σ²_i) / Σ(1/σ²_j)
```

Where w_i is the weight for cue i, and σ²_i is the variance (noise level) of that cue.

### Implementation Pattern

```python
import numpy as np
from scipy.stats import norm

def optimal_multisensory_integration(cues, noise_variances):
    """
    Compute optimal multisensory estimate.
    
    Args:
        cues: array of sensory estimates from different modalities
        noise_variances: array of noise variances for each cue
    
    Returns:
        optimal_estimate, integrated_variance
    """
    reliabilities = 1.0 / np.array(noise_variances)
    weights = reliabilities / reliabilities.sum()
    
    optimal_estimate = np.sum(weights * cues)
    integrated_variance = 1.0 / reliabilities.sum()
    
    return optimal_estimate, integrated_variance

def predict_msre(cues, noise_variances):
    """
    Calculate Multisensory Response Enhancement (MRE).
    MRE = (P_multisensory - P_best_unisensory) / P_best_unisensory
    """
    p_uni = [1 - norm.cdf(0, c, np.sqrt(v)) for c, v in zip(cues, noise_variances)]
    p_multi, var_int = optimal_multisensory_integration(cues, noise_variances)
    p_multi_val = 1 - norm.cdf(0, p_multi, np.sqrt(var_int))
    
    return (p_multi_val - max(p_uni)) / max(p_uni)
```

## Applications

- Brain-computer interface decoding with multiple sensory inputs
- Neural prosthetics that account for sensory noise
- Computational models of perception
- Clinical assessment of multisensory integration deficits

## Activation Keywords

- sensory noise, multisensory integration, neural variability
- cue combination, reliability weighting, perceptual decision
- 感觉噪声, 多感觉整合, 神经变异性

## References

- arXiv:2604.14096 (2026)
- Related skills: eeg-hopfield-emotion-energy, neural-population-decoding