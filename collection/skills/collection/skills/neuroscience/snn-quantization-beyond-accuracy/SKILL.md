---
name: snn-quantization-beyond-accuracy
description: "Earth Mover's Distance (EMD) methodology for evaluating SNN quantization beyond accuracy. Provides distribution-aware metrics for assessing spiking pattern preservation in quantized models. Activation: snn quantization, spiking neural network quantization, emd evaluation, quantization beyond accuracy, spike pattern distribution."
version: 1.0.0
author: Research Synthesis
license: MIT
metadata:
  hermes:
    tags: [snn, quantization, emd, spiking-patterns, evaluation]
    source_paper: "Quantization of Spiking Neural Networks Beyond Accuracy (arXiv:2604.14487)"
    citations: 0
---

# SNN Quantization Beyond Accuracy

Evaluate SNN quantization using Earth Mover's Distance (EMD) to measure spike pattern distribution preservation, not just final accuracy.

## Paper Metadata
- **arXiv**: 2604.14487
- **Published**: 2026-04-19
- **Categories**: q-bio.NC, cs.NE

## Problem

Standard SNN quantization evaluation only reports accuracy drop. This ignores **spike pattern distribution changes** — quantized models may maintain accuracy while fundamentally altering temporal coding schemes, causing failures in timing-sensitive downstream tasks.

## Core Methodology

### Earth Mover's Distance for Spike Patterns

EMD measures the minimum "work" to transform one distribution into another. For SNN quantization:

1. **Extract spike distributions** from pre- and post-quantization models
2. **Compute EMD** between distributions (Wasserstein-1 distance)
3. **Interpret EMD**: low = preserved dynamics; high = altered coding scheme

### Evaluation Pipeline

```python
import numpy as np
from scipy.stats import wasserstein_distance

def evaluate_snn_quantization(original_spikes, quantized_spikes, num_bins=100):
    """Evaluate SNN quantization using distribution-aware metrics."""
    
    # 1. Convert spike trains to distributions
    hist_orig, bins = np.histogram(original_spikes, bins=num_bins, density=True)
    hist_quant, _ = np.histogram(quantized_spikes, bins=bins, density=True)
    
    # 2. Earth Mover's Distance (Wasserstein-1)
    emd = wasserstein_distance(
        u_values=np.random.choice(bins[:-1], size=len(original_spikes), p=hist_orig),
        v_values=np.random.choice(bins[:-1], size=len(quantized_spikes), p=hist_quant)
    )
    
    # 3. Additional metrics
    kl_div = np.sum(hist_orig * np.log((hist_orig + 1e-10) / (hist_quant + 1e-10)))
    
    return {
        'emd': emd,
        'kl_divergence': kl_div,
        'preservation_score': np.exp(-emd)
    }
```

## Key Insights

- **Accuracy is insufficient**: Models with identical accuracy can have drastically different spike dynamics
- **EMD reveals hidden degradation**: Quantization may preserve output but alter internal representations
- **Distribution-aware design**: Optimize for low EMD during quantization-aware training
- **Cross-layer analysis**: Different layers show different quantization sensitivity patterns

## Applications

- Quantization-aware training with EMD regularization
- Hardware-aware SNN deployment on edge devices
- Neuromorphic chip quantization validation
- Spiking pattern preservation in low-bit SNNs

## Related Skills

- snn-learning-survey
- quantized-snn-hardware-optimization
- snn-firing-distribution-quantization
