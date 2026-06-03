---
name: snn-firing-distribution-quantization
description: Earth Mover's Distance (EMD) methodology for evaluating SNN quantization quality beyond simple accuracy. Captures firing pattern distribution shifts caused by low-precision representation. Updated 2026-04-19 with latest arXiv paper.
last_updated: 2026-04-18
description: "Earth Mover's Distance (EMD) methodology for evaluating SNN quantization beyond accuracy. Diagnoses firing distribution divergence caused by weight and membrane quantization. Activation: SNN quantization, firing distribution, EMD metric, membrane quantization, SEW-ResNet, deployment evaluation, spiking network quantization quality."
---

# SNN Firing Distribution Quantization Analysis

## Description

This skill provides guidance for evaluating Spiking Neural Network (SNN) quantization using Earth Mover's Distance (EMD) as a diagnostic metric for firing distribution divergence. Standard accuracy metrics alone cannot capture deployment-relevant differences in firing behavior between full-precision and quantized networks.

## Source Paper

- **Title**: "Quantization of Spiking Neural Networks Beyond Accuracy"
- **Authors**: Evan Gibson Smith, Jacob Whitehill, Fatemeh Ganji
- **Published**: 2026-04-15
- **arXiv**: [2604.14487](https://arxiv.org/abs/2604.14487)
- **Category**: cs.LG

## Problem Statement

Existing SNN quantization evaluation focuses almost exclusively on accuracy, overlooking whether a quantized network preserves the firing behavior of its full-precision counterpart. This is critical because firing activity governs:
- Effective sparsity
- State storage requirements
- Event-processing load
- Energy consumption on neuromorphic hardware

## Key Findings

### 1. Uniform vs. Non-Uniform Quantization
- **Uniform quantization** induces distinct firing distribution shifts compared to non-uniform approaches
- Networks can achieve equivalent accuracy but exhibit substantially different firing distributions
- These differences are invisible to standard metrics

### 2. Quantization Sensitivity Factors
| Factor | Impact |
|--------|--------|
| **Quantization method** | Uniform vs. non-uniform produces different firing patterns |
| **Clipping range** | Affects which neurons fire and when |
| **Bit-width** | Lower bits increase distribution divergence |

### 3. Architecture Tested
- SEW-ResNet architectures
- CIFAR-10 and CIFAR-100 datasets
- Weight quantization and membrane quantization

## Methodology

### Earth Mover's Distance (EMD) for Firing Distribution

EMD measures the minimum "cost" to transform one distribution into another, providing a meaningful metric for quantifying firing distribution divergence:

```python
import numpy as np
from scipy.stats import wasserstein_distance

def compute_firing_distribution(spike_trains, num_bins=100):
    """Compute firing rate distribution from spike trains."""
    all_spikes = np.concatenate(spike_trains)
    hist, bin_edges = np.histogram(all_spikes, bins=num_bins, density=True)
    return hist, bin_edges

def firing_emd(reference_dist, quantized_dist):
    """Compute EMD between reference and quantized firing distributions."""
    ref_hist, ref_bins = reference_dist
    q_hist, q_bins = quantized_dist
    
    # Use bin centers as support points
    ref_centers = (ref_bins[:-1] + ref_bins[1:]) / 2
    q_centers = (q_bins[:-1] + q_bins[1:]) / 2
    
    # Compute Wasserstein-1 distance
    emd = wasserstein_distance(
        ref_centers, q_centers,
        u_weights=ref_hist, v_weights=q_hist
    )
    return emd
```

### Quantization Evaluation Pipeline

```python
def evaluate_snn_quantization(model, test_loader, bits=8, method='uniform'):
    """Complete SNN quantization evaluation with EMD."""
    
    # 1. Collect reference (full-precision) firing distributions
    ref_spikes = collect_spiking_activity(model, test_loader)
    ref_dist = compute_firing_distribution(ref_spikes)
    ref_accuracy = compute_accuracy(model, test_loader)
    
    # 2. Apply quantization
    quantized_model = apply_quantization(model, bits=bits, method=method)
    
    # 3. Collect quantized firing distributions
    q_spikes = collect_spiking_activity(quantized_model, test_loader)
    q_dist = compute_firing_distribution(q_spikes)
    q_accuracy = compute_accuracy(quantized_model, test_loader)
    
    # 4. Compute EMD
    emd_score = firing_emd(ref_dist, q_dist)
    
    return {
        'accuracy_reference': ref_accuracy,
        'accuracy_quantized': q_accuracy,
        'accuracy_drop': ref_accuracy - q_accuracy,
        'emd': emd_score,
        'method': method,
        'bits': bits
    }
```

### Weight Quantization

```python
def quantize_weights_uniform(weights, bits=8):
    """Uniform weight quantization with clipping."""
    scale = 2 ** (bits - 1) - 1
    q_weights = np.clip(np.round(weights * scale), -scale, scale)
    return q_weights.astype(np.int8), scale

def quantize_weights_nonuniform(weights, bits=8):
    """Non-uniform (logarithmic) weight quantization."""
    magnitude = np.abs(weights) + 1e-8
    log_magnitude = np.log2(magnitude)
    q_log = np.round(log_magnitude * (2 ** (bits - 1))) / (2 ** (bits - 1))
    q_weights = np.sign(weights) * (2 ** q_log)
    return q_weights
```

### Membrane Quantization

```python
def quantize_membrane_potential(V_mem, V_max, bits=8):
    """Quantize membrane potential to integer representation."""
    q_V = np.round(V_mem / V_max * (2**bits - 1))
    return np.clip(q_V, 0, 2**bits - 1).astype(np.uint8)
```

## Deployment Considerations

### Why Firing Distribution Matters

| Metric | What It Captures | What It Misses |
|--------|------------------|----------------|
| **Accuracy** | Classification performance | Firing behavior, sparsity, energy |
| **EMD** | Firing distribution divergence | Classification performance |
| **Both together** | Complete deployment picture | - |

### Practical Recommendations

1. **Always measure EMD alongside accuracy** when quantizing SNNs
2. **Non-uniform quantization** often preserves firing behavior better than uniform
3. **Clipping range** tuning is critical — too aggressive causes distribution shift
4. **Layer-wise bit allocation** can optimize for both accuracy and firing preservation
5. **Validate on target hardware** — hardware-specific effects may differ from simulation

## Applications

- Neuromorphic chip deployment optimization
- SNN quantization for edge devices
- Energy-efficient spiking network deployment
- Quality assurance for quantized SNN models
- Research on SNN robustness to quantization

## Related Skills

- **quantized-snn-hardware-optimization**: Hardware optimization for quantized SNNs
- **spikingjelly-framework**: SNN training framework
- **snn-performance-analysis**: Performance analysis of SNNs

## Key References

- Smith, E.G., Whitehill, J., & Ganji, F. (2026). Quantization of Spiking Neural Networks Beyond Accuracy. arXiv:2604.14487
- Roy et al. (2019). "Towards spike-based machine intelligence with neuromorphic computing"
- Davies et al. (2018). "Loihi: A neuromorphic manycore processor with on-chip learning"

---

**Last updated**: 2026-04-18