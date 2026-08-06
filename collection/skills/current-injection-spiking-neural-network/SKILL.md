---
name: current-injection-spiking-neural-network
description: "Current Injection Spiking Neural Network (CIS-Fuse) methodology for infrared and visible image fusion. Introduces the current injection spiking (CIS) operator that performs cross-modal fusion directly at the membrane-potential level, preserving subthreshold responses from both modalities before spike firing. Use when implementing energy-efficient multi-modal image fusion with spiking neural networks."
metadata:
  arxiv_id: "2607.19879"
  authors: "Rui Zhao, Zhuoyuan Li, Wenrui Li, Yanchen Dong, Yajing Zheng, Giuseppe Valenzise, Weisi Lin"
  published: "2026-07-22"
  categories: ["cs.CV"]
  tags: [spiking-neural-networks, image-fusion, infrared-visible, current-injection, membrane-potential, energy-efficient]
license: Complete terms in LICENSE.txt
---

# Current Injection Spiking Neural Network for Image Fusion

## Overview

CIS-Fuse addresses the fundamental tension in applying Spiking Neural Networks (SNNs) to Infrared and Visible Image Fusion (IVIF): binary spikes can discard complementary cues that remain below the firing threshold, while cross-modal fusion relies on fine-grained responses from both modalities. The solution integrates modalities at the membrane-potential level before spike firing.

## Core Innovation: Current Injection Spiking (CIS) Operator

### Membrane Potential Integration
The CIS operator injects one modality as a gated auxiliary current into the driving neuron of the other, allowing both modalities to jointly shape the output before spike generation. This preserves subthreshold responses that would be lost with traditional post-spike fusion.

### Adaptive Injection Strength
Each channel has a per-channel learnable injection strength that adaptively regulates the modulation magnitude, enabling flexible cross-modal interaction based on content.

## Architecture Components

### Bidirectional Cross-Modal Fusion (BCMF) Module
- **Dual-branch design**: Two branches with asymmetric stacking depths
- **Functional specialization**: Clear role separation between branches
- **Bidirectional flow**: Information flows in both directions between modalities

### Dual-Branch Architecture
- **Asymmetric depths**: Different processing depths for each modality
- **Specialized processing**: Each branch develops distinct functional characteristics
- **Efficient computation**: Leverages SNN sparsity for energy efficiency

## Performance Characteristics

### Fusion Quality
- Achieves fusion quality on par with state-of-the-art ANN-based methods
- Preserves complementary information from both modalities
- Maintains scene content richness

### Energy Efficiency
- Roughly an order of magnitude lower inference energy than similarly-sized ANN-based DCEvo
- Inherits natural energy efficiency of spike-based computation
- Sparse activation reduces computational load

## Implementation Guidelines

### For Image Fusion Tasks
1. **Input preprocessing**: Prepare infrared and visible images with appropriate normalization
2. **Network configuration**: Set up dual-branch architecture with asymmetric depths
3. **CIS operator integration**: Implement current injection at membrane-potential level
4. **Training strategy**: Use supervised learning with fused ground truth images

### For Energy-Efficient Deployment
1. **Hardware selection**: Choose neuromorphic hardware supporting membrane potential access
2. **Quantization**: Apply appropriate quantization for target hardware
3. **Sparsity optimization**: Leverage natural sparsity for memory and compute savings

## Applications Beyond IVIF

### Multi-Modal Sensing
- Extend to other sensor fusion tasks (e.g., radar-optical, audio-visual)
- Adapt injection mechanism for different modality characteristics

### Medical Imaging
- Apply to multi-spectral medical image fusion
- Leverage energy efficiency for edge medical devices

### Autonomous Systems
- Implement in resource-constrained autonomous platforms
- Combine with other SNN-based perception modules

## Pitfalls and Considerations

- **Hardware requirements**: Requires access to membrane potential during computation
- **Training complexity**: May require specialized training algorithms for SNNs
- **Modality balance**: Injection strength must be carefully tuned to avoid dominance by one modality

## References

- Original paper: [arXiv:2607.19879](https://arxiv.org/abs/2607.19879)
- Related work: Spiking neural networks, image fusion, neuromorphic computing

## Activation Keywords

- current injection spiking network
- membrane potential image fusion
- infrared visible SNN fusion
- CIS-Fuse spiking network
- cross-modal spiking fusion
- energy efficient image fusion SNN