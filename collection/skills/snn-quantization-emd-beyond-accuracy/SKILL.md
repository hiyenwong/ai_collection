---
name: snn-quantization-emd-beyond-accuracy
description: Earth Mover's Distance (EMD) framework for evaluating SNN quantization beyond accuracy. Shows uniform quantization causes firing distribution drift even when accuracy is preserved. Proposes LQ-Net style learned quantization for maintaining firing behavior.
version: 1.1
authors:
  - Evan Gibson Smith
  - et al.
paper: arXiv:2604.14487
date: 2026-04-15
tags:
  - spiking-neural-network
  - quantization
  - earth-mover-distance
  - firing-distribution
  - hardware-deployment
  - neuromorphic
  - model-compression
  - distribution-drift
category: ai_collection
---

# Quantization of Spiking Neural Networks Beyond Accuracy

## Summary

This work identifies a critical blind spot in SNN quantization: **accuracy alone is insufficient to evaluate quantization quality**. The paper introduces **Earth Mover's Distance (EMD)** as a diagnostic metric for measuring firing distribution divergence between full-precision and quantized SNNs. Key finding: uniform quantization preserves accuracy but causes significant firing distribution drift, which degrades downstream tasks (neuroscience analysis, hardware timing, energy estimates). An **LQ-Net style learned quantization** method is proposed that maintains both accuracy and firing fidelity.

**Key Innovation**: EMD reveals quantization damage invisible to accuracy metrics — a quantized SNN can achieve 98% accuracy while its firing patterns are fundamentally altered.

## Key Contributions

1. **EMD Diagnostic Metric**: Earth Mover's Distance between firing rate distributions of full-precision and quantized SNNs, capturing distributional shifts invisible to accuracy.

2. **Distribution Drift Discovery**: Uniform quantization (INT8, INT4) causes systematic drift in firing patterns even when task accuracy is preserved within 1%.

3. **Learned Quantization for SNNs**: LQ-Net style approach where quantization scales and zero-points are learned per-layer/per-channel, maintaining firing distribution fidelity.

4. **Multi-Level Evaluation Framework**: Accuracy, EMD, firing rate correlation, temporal correlation, and energy proxy metrics for comprehensive quantization assessment.

5. **Hardware Implications**: Distribution drift affects hardware timing predictability, energy estimation accuracy, and neuroscience model validity.

## Problem Statement

### Why Accuracy is Insufficient

Standard SNN quantization evaluation:
```
Full-Precision SNN → Quantize → Measure Accuracy → ✓ (if accuracy drop < 2%)
```

**Hidden problem**: The quantized SNN may achieve 98% accuracy using completely different firing patterns:
- Different neurons fire at different rates
- Spike timing shifts by multiple time steps
- Temporal correlations between neurons are disrupted
- Total spike count changes unpredictably

### Consequences of Hidden Distribution Drift

| Application | Impact of Distribution Drift |
|------------|------------------------------|
| Neuroscience modeling | Invalid brain model comparisons |
| Hardware timing | Unpredictable latency spikes |
| Energy estimation | 20-50% error in power estimates |
| Downstream SNN tasks | Cascading errors in hierarchical networks |
| Neuromorphic deployment | Timing violations on event-based hardware |

## Technical Approach

### Earth Mover's Distance for Firing Distributions

Given:
- P = firing rate distribution of full-precision SNN (histogram over neurons)
- Q = firing rate distribution of quantized SNN (same histogram bins)

$$\text{EMD}(P, Q) = \frac{\sum_{i=1}^{m} \sum_{j=1}^{m} f_{ij} d_{ij}}{\sum_{i=1}^{m} \sum_{j=1}^{m} f_{ij}}$$

Where:
- f_ij: optimal flow from bin i to bin j (computed via linear programming)
- d_ij: ground distance between bins i and j (|i - j| for ordered bins)

### Practical EMD Computation

For efficiency, use the 1D closed-form solution (since firing rates are 1D distributions):

$$\text{EMD}(P, Q) = \sum_{k=1}^{K} |CDF_P(k) - CDF_Q(k)|$$

Where CDF is the cumulative distribution function.

```python
def compute_emd(dist_fp, dist_quant, num_bins=50):
    """Compute EMD between firing rate distributions."""
    # Create histograms
    bins = np.linspace(0, max(dist_fp.max(), dist_quant.max()), num_bins)
    P, _ = np.histogram(dist_fp, bins=bins, density=True)
    Q, _ = np.histogram(dist_quant, bins=bins, density=True)
    
    # Normalize
    P = P / P.sum()
    Q = Q / Q.sum()
    
    # EMD = sum of |CDF differences|
    emd = np.sum(np.abs(np.cumsum(P) - np.cumsum(Q)))
    return emd
```

### Quantization Methods Compared

#### 1. Uniform Symmetric Quantization
$$w_q = \text{round}\left(\frac{w}{s}\right) \cdot s, \quad s = \frac{\max(|w|)}{2^{b-1}-1}$$

#### 2. Uniform Asymmetric Quantization
$$w_q = \text{round}\left(\frac{w - z}{s}\right) \cdot s + z$$
$$s = \frac{w_{max} - w_{min}}{2^b - 1}, \quad z = \text{round}\left(-\frac{w_{min}}{s}\right)$$

#### 3. LQ-Net Style Learned Quantization (Proposed)
Learn per-channel scale s_c and zero-point z_c:

$$w_{q,c} = \text{round}\left(\frac{w_c - z_c}{s_c}\right) \cdot s_c + z_c$$

Where s_c and z_c are trained via:
$$\frac{\partial w_{q,c}}{\partial s_c} = -\frac{w_c - z_c}{s_c^2} \cdot s_c + \frac{w_c - z_c}{s_c} \approx \text{STE}\left(\frac{w_c - z_c}{s_c}\right)$$

### Multi-Level Evaluation Framework

| Level | Metric | What It Measures |
|-------|--------|-----------------|
| L1: Task | Accuracy, F1 | Task performance |
| L2: Distribution | EMD, KL divergence | Firing rate distribution shift |
| L3: Correlation | Pearson r (firing rates) | Per-neuron rate preservation |
| L4: Temporal | Spike timing correlation | Temporal pattern preservation |
| L5: Hardware | Estimated energy, latency | Deployment characteristics |

## Experimental Results

### Quantization Impact (CIFAR-10, ResNet-SNN)

| Method | Bits | Accuracy | EMD↓ | Rate Corr↑ | Temporal Corr↑ |
|--------|------|----------|------|-----------|---------------|
| FP32 (baseline) | 32 | 93.1% | 0.000 | 1.000 | 1.000 |
| Uniform Sym | 8 | 92.8% | 0.142 | 0.873 | 0.791 |
| Uniform Sym | 4 | 91.5% | 0.387 | 0.624 | 0.483 |
| Uniform Asym | 8 | 93.0% | 0.098 | 0.912 | 0.856 |
| Uniform Asym | 4 | 92.1% | 0.291 | 0.718 | 0.612 |
| **LQ-Net (learned)** | **8** | **93.0%** | **0.031** | **0.978** | **0.962** |
| **LQ-Net (learned)** | **4** | **92.6%** | **0.127** | **0.884** | **0.821** |

### Key Finding
- **Uniform INT8**: Only 0.3% accuracy loss, but **14.2% EMD** — significant distribution drift!
- **Learned INT8**: Same accuracy, but only **3.1% EMD** — much better fidelity.

### Energy Estimation Error

| Quantization | True Energy | Estimated Energy | Error |
|-------------|-------------|-----------------|-------|
| FP32 | 1.0 mJ | 1.0 mJ | 0% |
| Uniform INT8 | 0.72 mJ | 0.85 mJ | +18% |
| **Learned INT8** | **0.73 mJ** | **0.74 mJ** | **+1.4%** |

## Implementation Guide

### Learned Quantization Training
```python
class LearnedQuantizer(nn.Module):
    def __init__(self, num_channels, bits=8):
        super().__init__()
        self.bits = bits
        # Learnable per-channel parameters
        self.scale = nn.Parameter(torch.ones(num_channels, 1, 1, 1))
        self.zero_point = nn.Parameter(torch.zeros(num_channels, 1, 1, 1))
    
    def forward(self, x):
        # Quantize-dequantize with STE
        x_norm = (x - self.zero_point) / (self.scale + 1e-8)
        x_clipped = torch.clamp(x_norm, -(2**(self.bits-1)), 2**(self.bits-1) - 1)
        x_round = torch.round(x_clipped)  # STE applied here
        x_dequant = x_round * (self.scale + 1e-8) + self.zero_point
        return x_dequant
```

### EMD Evaluation Pipeline
```python
def evaluate_quantization(model_fp, model_quant, val_loader):
    """Full multi-level quantization evaluation."""
    rates_fp, rates_quant = [], []
    temporal_fp, temporal_quant = [], []
    
    for x, y in val_loader:
        # Full precision
        spikes_fp = model_fp(x)
        rates_fp.append(spikes_fp.mean(dim=0).flatten())
        temporal_fp.append(spikes_fp.flatten())
        
        # Quantized
        spikes_quant = model_quant(x)
        rates_quant.append(spikes_quant.mean(dim=0).flatten())
        temporal_quant.append(spikes_quant.flatten())
    
    rates_fp = torch.cat(rates_fp)
    rates_quant = torch.cat(rates_quant)
    
    # L1: Accuracy already computed
    # L2: EMD
    emd = compute_emd(rates_fp.numpy(), rates_quant.numpy())
    # L3: Rate correlation
    rate_corr = pearsonr(rates_fp, rates_quant)[0]
    # L4: Temporal correlation (sampled)
    idx = torch.randperm(len(temporal_fp))[:10000]
    temp_corr = pearsonr(temporal_fp[idx], temporal_quant[idx])[0]
    
    return {'EMD': emd, 'rate_corr': rate_corr, 'temp_corr': temp_corr}
```

## Relevance

This work establishes **EMD as an essential metric** for SNN quantization evaluation. It reveals that:
- Accuracy metrics alone are **dangerously misleading** for SNN compression
- Distribution-preserving quantization is crucial for neuroscience applications
- Hardware deployment requires distribution fidelity for timing predictability
- The proposed learned quantization is a **drop-in replacement** for standard methods

## Triggers (激活词)

SNN quantization, earth mover distance, EMD, firing distribution, distribution drift, learned quantization, LQ-Net, model compression, hardware deployment, neuromorphic, accuracy vs fidelity, quantization evaluation, spike timing, energy estimation
