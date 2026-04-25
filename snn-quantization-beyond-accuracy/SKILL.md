---
name: snn-quantization-beyond-accuracy
category: neuroscience
description: Quantization of Spiking Neural Networks beyond accuracy - evaluating SNN quantization using Earth Mover's Distance (EMD) and firing distribution preservation, not just task accuracy.
trigger: snn quantization beyond accuracy, emd spiking networks, firing distribution quantization, earth mover distance snn, quantization evaluation
---

# SNN Quantization Beyond Accuracy (EMD Framework)

## Paper
- **Title**: Quantization of Spiking Neural Networks Beyond Accuracy
- **Authors**: Evan Gibson Smith, Jacob Whitehill, Fatemeh Ganji
- **Date**: April 15, 2026
- **arXiv**: 2604.14487v1

## Overview
Evaluates SNN quantization not just by task accuracy but by preservation of firing distributions using Earth Mover's Distance (EMD), providing more nuanced assessment of quantization quality.

## Core Innovation
- **EMD metric** for quantization evaluation
- **Firing distribution preservation** as quality measure
- **Beyond accuracy**: captures subtle dynamics changes
- **Resource-constrained deployment** optimization

### EMD for SNN Quantization
```
EMD(P, Q) = min Σ γ_ij · d(x_i, y_j)
            γ

where:
  P = original firing distribution
  Q = quantized firing distribution
  d = ground distance between firing patterns
  γ = optimal transport plan
```

### Key Findings
1. Accuracy alone misses **firing pattern degradation**
2. EMD captures **temporal dynamics** changes
3. Different bit-widths affect different aspects
4. Optimal quantization balances accuracy and dynamics

## Applications
- Neuromorphic hardware deployment
- Edge AI with SNNs
- Quantization-aware training

## Related Skills
- snn-performance-analysis
- snn-firing-distribution-quantization
