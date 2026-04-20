---
name: combining-convolution-delay-learning-recurrent-spiking
description: "Methodology from paper 'Combining Convolution and Delay Learning in Recurrent Spiking Neural Networks...' by Lúcio Folly Sanches Zebendo et al. (2026-04-17). Activation: neural, spiking, network, memory, learning, cs.NE"
version: 1.0.0
author: Research Synthesis
license: MIT
metadata:
  hermes:
    tags: [neuroscience, research, cs.NE]
    source_paper: "Combining Convolution and Delay Learning in Recurrent Spiking Neural Networks (arXiv:2604.15997v1)"
    published: 2026-04-17
---

# Combining Convolution and Delay Learning in Recurrent Spiking Neural Networks

## Source Paper
- **Title**: Combining Convolution and Delay Learning in Recurrent Spiking Neural Networks
- **Authors**: Lúcio Folly Sanches Zebendo, Eleonora Cicciarella, Michele Rossi
- **arXiv**: 2604.15997v1
- **Published**: 2026-04-17
- **Category**: cs.NE
- **PDF**: https://arxiv.org/pdf/2604.15997v1
- **Abstract URL**: http://arxiv.org/abs/2604.15997v1

## Abstract

Spiking neural networks (SNNs) are rapidly gaining momentum as an alternative to conventional artificial neural networks in resource constrained edge systems. In this work, we continue a recent research line on recurrent SNNs where axonal delays are learned at runtime along with the other network parameters. The first proposed approach, dubbed DelRec, demonstrated the benefit of recurrent delay learning in SNNs. Here, we extend it by advocating the use of convolutional recurrent connections in conjunction with the DelRec delay learning mechanism. According to our tests on an audio classification task, this leads to a streamlined architecture with smaller memory footprint (around 99% savings in terms of number of recurrent parameters) and a much faster (52x) inference time, while retaining ...

## Key Contributions

1. Spiking neural networks (SNNs) are rapidly gaining momentum as an alternative to conventional artificial neural networks in resource constrained edge ...
2. In this work, we continue a recent research line on recurrent SNNs where axonal delays are learned at runtime along with the other network parameters
3. The first proposed approach, dubbed DelRec, demonstrated the benefit of recurrent delay learning in SNNs

## Core Concepts

- **Primary**: cs.NE
- **Techniques**: neural, spiking, network, memory, learning
- **Application**: Neuroscience research and analysis

## Implementation Pattern

```python
# Based on 2604.15997v1
import numpy as np

class CombiningConvolutionDelay:
    """Based on arXiv:2604.15997v1"""
    def __init__(self): pass
    def fit(self, data): pass
    def predict(self, new_data): pass
```

## Applications

- Neuroscience research and analysis
- Research and analysis
- Further applications described in paper

## Limitations

See original paper for discussion.

## Activation Keywords

- neural, spiking, network, memory, learning
- cs.NE
- 2026 research

## References

- Lúcio Folly Sanches Zebendo et al. (2026). "Combining Convolution and Delay Learning in Recurrent Spiking Neural Networks." arXiv:2604.15997v1.
