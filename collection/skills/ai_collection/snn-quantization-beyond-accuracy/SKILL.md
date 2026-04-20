---
name: snn-quantization-beyond-accuracy
description: "Earth Mover's Distance (EMD) methodology for evaluating SNN quantization beyond accuracy. Captures distributional shifts in spike timing and firing patterns that accuracy metrics miss. Activation: snn quantization, earth movers distance, spike distribution, quantization evaluation, spiking neural network compression."
version: 1.0.0
metadata:
  hermes:
    source_paper: "Quantization of Spiking Neural Networks Beyond Accuracy (arXiv:2604.14487)"
    tags: [neuroscience, spiking, quantization, evaluation, earth-movers-distance]
---

# Quantization of Spiking Neural Networks Beyond Accuracy

## Source Paper
- **Title**: Quantization of Spiking Neural Networks Beyond Accuracy
- **arXiv**: 2604.14487
- **PDF**: https://arxiv.org/pdf/2604.14487

## Overview

Quantization is a natural complement to the sparse, event-driven computation of Spiking Neural Networks, reducing memory bandwidth and arithmetic costs. However, **traditional accuracy metrics fail to capture critical behavioral changes** in SNNs under quantization. This paper introduces Earth Mover's Distance (EMD) as a superior evaluation metric that captures distributional shifts in spike timing and firing patterns.

## Key Insight

Standard accuracy only measures final classification correctness, missing:
- Temporal coding shifts (when spikes occur)
- Firing rate distribution changes
- Information loss in spike timing precision
- Subtle behavioral degradation before accuracy collapse

## Core Concepts

### Earth Mover's Distance for SNN Evaluation
- EMD measures the "work" needed to transform one spike distribution into another
- Captures both rate and temporal coding differences
- More sensitive than accuracy for early quantization degradation
- Provides interpretable metric: "bits of information lost"

### Spike Distribution Analysis
- Compare pre/post-quantization spike train statistics
- Analyze inter-spike interval (ISI) distributions
- Measure firing rate histograms per layer
- Track temporal precision degradation

### Quantization-Aware Training for SNNs
- Incorporate EMD loss during training
- Adaptive quantization based on spike statistics
- Layer-wise quantization sensitivity analysis

## Implementation Pattern

```python
import numpy as np
from scipy.stats import wasserstein_distance

def compute_spike_emd(spike_train_a, spike_train_b, bin_size=1.0):
    """
    Compute Earth Mover's Distance between spike trains.
    
    Args:
        spike_train_a, spike_train_b: Binary spike trains (T x N)
        bin_size: Temporal bin size in ms
    
    Returns:
        emd: Earth Mover's Distance (distributional difference)
    """
    # Convert to spike time distributions
    times_a = np.where(spike_train_a.flatten())[0] * bin_size
    times_b = np.where(spike_train_b.flatten())[0] * bin_size
    
    if len(times_a) == 0 or len(times_b) == 0:
        return float('inf')
    
    # EMD between spike timing distributions
    emd = wasserstein_distance(times_a, times_b)
    return emd


def firing_rate_emd(rate_histogram_a, rate_histogram_b):
    """EMD between firing rate distributions."""
    bins = np.arange(len(rate_histogram_a) + 1)
    emd = wasserstein_distance(
        np.repeat(bins[:-1], rate_histogram_a),
        np.repeat(bins[:-1], rate_histogram_b)
    )
    return emd


def isi_distribution_emd(spike_train_a, spike_train_b):
    """EMD between inter-spike interval distributions."""
    def compute_isis(st):
        spike_times = np.where(st)[0]
        if len(spike_times) < 2:
            return np.array([0])
        return np.diff(spike_times)
    
    isis_a = compute_isis(spike_train_a)
    isis_b = compute_isis(spike_train_b)
    
    return wasserstein_distance(isis_a, isis_b)


def evaluate_quantization(model, data, quantization_bits):
    """Comprehensive quantization evaluation using EMD."""
    # Baseline (full precision)
    baseline_spikes = model.forward(data)
    
    # Quantized model
    model.quantize(quantization_bits)
    quantized_spikes = model.forward(data)
    
    # Multiple EMD metrics
    metrics = {
        'timing_emd': compute_spike_emd(baseline_spikes, quantized_spikes),
        'firing_rate_emd': firing_rate_emd(
            np.histogram(baseline_spikes.sum(axis=0), bins=50)[0],
            np.histogram(quantized_spikes.sum(axis=0), bins=50)[0]
        ),
        'isi_emd': isi_distribution_emd(baseline_spikes, quantized_spikes),
        'accuracy': compute_accuracy(baseline_spikes, quantized_spikes),
    }
    
    return metrics
```

## When to Use EMD Over Accuracy
- **Quantization sensitivity analysis**: Find which layers are most affected
- **Early warning detection**: EMD degrades before accuracy drops
- **Temporal coding preservation**: Verify timing-sensitive applications
- **Neuromorphic deployment**: Ensure hardware quantization doesn't alter behavior

## Quantization Strategy for SNNs
1. **Weight quantization**: 8-bit → 4-bit → 2-bit progressive analysis
2. **Activation quantization**: Spike count encoding (2-4 bits per timestep)
3. **Mixed precision**: Sensitive layers at higher precision
4. **EMD-guided selection**: Choose quantization levels that minimize EMD

## Related Skills
- [[spiking-neural-network-training]]
- [[quantization-spiking-neural-networks-beyond-accuracy]]
- [[sharpness-aware-surrogate-snn-training]]
