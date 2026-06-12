---
name: convolution-delay-learning-snn
description: >-
  Combines convolutional recurrent connections with DelRec delay learning mechanism
  in recurrent spiking neural networks. Achieves 99% parameter savings and 52x faster
  inference vs standard recurrent SNN while maintaining accuracy on audio classification.
  Convolutional recurrent structure with learned axonal delays provides streamlined
  architecture for resource-constrained edge systems.
  Activation: convolution delay learning, DelRec, recurrent SNN audio, axonal delay learning,
  efficient SNN architecture, edge SNN.
version: 1.0.0
metadata:
  hermes:
    tags: [snn, convolution, delay-learning, DelRec, edge-computing, audio-classification]
    source_paper: "Combining Convolution and Delay Learning in Recurrent Spiking Neural Networks (arXiv:2604.15997)"
    citations: 0
---

# Convolution + Delay Learning in Recurrent SNNs

## Overview

Extends DelRec (recurrent delay learning in SNNs) by combining convolutional recurrent
connections with the delay learning mechanism, achieving dramatic efficiency gains.

## Key Results

| Metric | Improvement |
|--------|-------------|
| Parameter reduction | ~99% savings |
| Inference speedup | 52x faster |
| Accuracy | Maintained vs standard recurrent |

## Architecture

- **Convolutional recurrent connections**: Replace fully recurrent with conv recurrent
- **DelRec delay learning**: Axonal delays learned at runtime with other parameters
- **Combined approach**: Convolution + delay learning in unified framework

## Implementation Pattern

```python
# Convolutional recurrent SNN with delay learning
# W_conv: convolutional recurrent weights (smaller footprint)
# Delays: learned parameters updated during training
# Combined update: weights + delays via surrogate gradient
```

## Task Domain

- Audio classification (tested)
- Other temporal classification tasks
- Edge deployment scenarios

## Pitfalls

- Convolution kernel size affects temporal receptive field
- Delay learning rate must be balanced with weight learning
- Audio preprocessing affects overall pipeline performance
