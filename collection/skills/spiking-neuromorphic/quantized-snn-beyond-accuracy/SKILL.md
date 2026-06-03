---
name: quantized-snn-beyond-accuracy
description: "Quantization of Spiking Neural Networks beyond accuracy - Earth Mover's Distance (EMD) methodology for evaluating SNN quantization effects on spike train distributions, firing patterns, and temporal dynamics. Use when optimizing SNNs for low-precision hardware, analyzing quantization trade-offs in neuromorphic systems. Triggers: SNN quantization, spiking network compression, low-precision SNN, Earth Mover's Distance, neuromorphic hardware optimization."
version: 1.0.0
author: Research Synthesis
license: MIT
metadata:
  hermes:
    source_paper: "Quantization of Spiking Neural Networks Beyond Accuracy (arXiv:2604.14096)"
    citations: 0
    published: "2026-04-15"
    tags:
    - spiking-neural-networks
    - quantization
    - earth-movers-distance
    - neuromorphic-hardware
    - model-compression
    - spike-train-analysis
---

# Quantization of Spiking Neural Networks Beyond Accuracy

## Overview

This skill provides a comprehensive methodology for evaluating and optimizing SNN quantization using Earth Mover's Distance (EMD) to capture changes in spike train distributions, firing patterns, and temporal dynamics that traditional accuracy metrics miss.

Based on the paper "Quantization of Spiking Neural Networks Beyond Accuracy" (arXiv:2604.14096, 2026-04-15).

## Core Principles

1. **Accuracy is insufficient** - Quantization can preserve accuracy while destroying temporal dynamics
2. **Earth Mover's Distance (EMD)** - Measures distributional shifts in spike patterns
3. **Multi-metric evaluation** - Combines accuracy, EMD, latency, and energy metrics

## Quantization-Aware Training Pipeline

```python
class QuantizedSNN:
    def __init__(self, model, bit_width=8):
        self.model = model
        self.bit_width = bit_width
        
    def quantize_weights(self):
        """Quantize weights to target bit width."""
        scale = (2**self.bit_width - 1) / (self.weight_max - self.weight_min)
        return torch.round(self.weights * scale) / scale
    
    def compute_emd(self, original_spikes, quantized_spikes):
        """Compute Earth Mover's Distance between spike distributions."""
        # Histogram spike counts per neuron
        orig_hist = torch.histc(original_spikes.sum(dim=0), bins=50)
        quant_hist = torch.histc(quantized_spikes.sum(dim=0), bins=50)
        
        # EMD via cumulative distribution difference
        emd = torch.abs(torch.cumsum(orig_hist, 0) - 
                       torch.cumsum(quant_hist, 0)).sum()
        return emd
```

## Evaluation Metrics

| Metric | Description | Target |
|--------|-------------|--------|
| Accuracy | Classification/regression performance | >95% of baseline |
| EMD | Distributional shift in spike patterns | <10% of baseline |
| Latency | Time-to-first-spike | <2x baseline |
| Energy | Estimated hardware energy consumption | Proportional to bit reduction |

## Quantization Strategies

### Strategy 1: Uniform Quantization
```python
weights_q = torch.round(weights / scale) * scale
```

### Strategy 2: Mixed Precision
- Input layer: 8-bit (preserve input sensitivity)
- Hidden layers: 4-bit (compress internal representations)
- Output layer: 8-bit (preserve decision boundaries)

### Strategy 3: Spike-Aware Quantization
Quantize based on spike timing importance:
```python
importance = spike_rate * gradient_magnitude
high_importance = 8-bit
low_importance = 4-bit
```

## Hardware Deployment

1. **Validate EMD** on target hardware simulator
2. **Profile energy** consumption with quantized model
3. **Deploy** to neuromorphic chip (Loihi, TrueNorth, SpiNNaker)
4. **Monitor** spike distribution drift in production

## Applications

- Edge AI with neuromorphic hardware
- Low-power always-on inference
- Real-time signal processing
- Bio-inspired robotics

## Activation Keywords

SNN quantization, spiking network compression, low-precision SNN, Earth Mover's Distance, neuromorphic hardware optimization

## Related Skills

- `conv-delay-learning-snn` - Convolutional delay SNNs
- `neuromorphic-low-power-ai` - Neuromorphic computing
- `snn-learning-rules-dynamics` - SNN learning fundamentals
