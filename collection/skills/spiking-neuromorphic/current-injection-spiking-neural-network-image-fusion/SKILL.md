---
name: current-injection-spiking-neural-network-image-fusion
version: 1.0.0
description: Current Injection Spiking Neural Network (CIS-Fuse) for energy-efficient infrared and visible image fusion using membrane-potential level cross-modal integration
tags:
  - spiking-neural-networks
  - image-fusion
  - neuromorphic-computing
  - energy-efficiency
  - computer-vision
trigger_words:
  - CIS-Fuse
  - current injection spiking
  - infrared visible fusion
  - membrane potential fusion
  - SNN image fusion
---

# Current Injection Spiking Neural Network for Infrared and Visible Image Fusion

## Overview

This skill implements the **Current Injection Spiking (CIS) Neural Network** architecture, specifically **CIS-Fuse**, for efficient infrared and visible image fusion (IVIF). The key innovation is performing cross-modal fusion directly at the membrane-potential level rather than at the spike level, preserving subthreshold responses that would otherwise be lost in binary spike communication.

## Key Concepts

### Problem Statement
- Traditional SNNs communicate through sparse binary spikes, which can discard complementary cues that remain below the firing threshold
- Cross-modal fusion requires fine-grained responses from both modalities (infrared and visible)
- Direct application of SNNs to IVIF creates tension between energy efficiency and fusion quality

### Core Innovation: Current Injection Spiking (CIS) Operator
- Injects one modality as a gated auxiliary current into the driving neuron of the other modality
- Integration occurs at the membrane-potential level before spike firing
- Per-channel learnable injection strength adaptively regulates modulation magnitude
- Preserves subthreshold responses that contain complementary information

### Architecture Components
1. **Dual-Branch Architecture**: Asymmetric stacking depths with clear functional specialization
2. **Bidirectional Cross-Modal Fusion (BCMF) Module**: Built on CIS operators for bidirectional information flow
3. **Membrane Potential Integration**: Cross-modal fusion at pre-spike integration stage

## Performance Benefits

- **Energy Efficiency**: ~10x lower inference energy compared to similarly-sized ANN-based methods (e.g., DCEvo)
- **Fusion Quality**: Achieves state-of-the-art results on par with ANN-based methods
- **Parameter Efficiency**: Reduced model complexity while maintaining performance
- **Downstream Performance**: Improved results on detection and segmentation tasks

## Implementation Guidelines

### When to Use
- Energy-constrained edge devices requiring real-time image fusion
- Applications needing both high fusion quality and low power consumption
- Multi-modal sensing scenarios where complementary information must be preserved
- Neuromorphic computing platforms

### Architecture Design
```python
# Pseudocode for CIS Operator
class CurrentInjectionSpiking(nn.Module):
    def __init__(self, channels):
        super().__init__()
        self.injection_strength = nn.Parameter(torch.ones(channels))
        
    def forward(self, driving_neuron_potential, auxiliary_modality):
        # Gate the auxiliary current
        gated_auxiliary = self.injection_strength * auxiliary_modality
        # Inject into driving neuron membrane potential
        integrated_potential = driving_neuron_potential + gated_auxiliary
        # Generate spike based on integrated potential
        spike = generate_spike(integrated_potential)
        return spike, integrated_potential
```

### Training Considerations
- Use contrastive learning or supervised fusion objectives
- Optimize injection strength parameters end-to-end
- Consider asymmetric branch depths for functional specialization
- Validate on multiple IVIF benchmarks (TNO, RoadScene, etc.)

## Evaluation Metrics

### Primary Metrics
- **Fusion Quality**: PSNR, SSIM, MS-SSIM, VIF
- **Energy Consumption**: Total inference energy (pJ or nJ)
- **Parameter Count**: Model size comparison
- **Downstream Tasks**: Detection mAP, segmentation IoU

### Benchmarks
- **IVIF Datasets**: TNO, RoadScene, FLIR, M3FD
- **Comparison Baselines**: DCEvo, FusionDN, U2Fusion, RFN-Nest
- **Hardware Platforms**: Loihi, TrueNorth, SpiNNaker

## Research Impact

This methodology bridges the gap between energy-efficient neuromorphic computing and high-quality multi-modal fusion, demonstrating that SNNs can achieve competitive performance while maintaining their inherent energy advantages. The membrane-potential level integration principle can be extended to other multi-modal fusion scenarios beyond infrared-visible pairs.

## References

- **arXiv**: [2607.19879](https://arxiv.org/abs/2607.19879)
- **Authors**: Rui Zhao, Zhuoyuan Li, Wenrui Li, Yanchen Dong, Yajing Zheng, Giuseppe Valenzise, Weisi Lin
- **Keywords**: Spiking Neural Networks, Image Fusion, Infrared-Visible Fusion, Membrane Potential, Energy Efficiency, Neuromorphic Computing

## Activation Examples

- "Implement CIS-Fuse for thermal and visible image fusion"
- "Design energy-efficient SNN for multi-modal fusion using current injection"
- "Apply membrane potential integration for cross-modal fusion"
- "Compare CIS-Fuse with traditional ANN-based fusion methods"