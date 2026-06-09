---
name: mirage-fmri-mental-imagery-decoding
description: "MIRAGE methodology — robust multi-modal architecture for translating fMRI-to-image models from seen visual decoding to mental imagery reconstruction. Demonstrates that SOTA on seen images doesn't guarantee SOTA on mental imagery and proposes a multi-modal, multi-loss architecture that excels at both. Use when researching: fMRI visual decoding, mental imagery reconstruction, brain decoding generalization, seen-to-imagery transfer, NSD-Imagery dataset, multi-modal brain decoding, vision model generalization."
---

# MIRAGE: Robust Multi-Modal Architectures Translate fMRI-to-Image Models from Vision to Mental Imagery

## Overview

Vision decoding models trained to reconstruct **seen images** from human brain activity must generalize to **internally generated visual representations** (mental imagery) to be useful for downstream applications like brain-computer interfaces and clinical diagnostics. This paper presents a systematic analysis showing that **state-of-the-art performance on seen image reconstruction does not guarantee SOTA performance on mental image reconstruction**, and develops **MIRAGE**, a robust multi-modal architecture that excels at both.

## Key Findings

1. **Generalization gap**: Some modern vision decoders that perform well on seen images fail on mental images
2. **SOTA ≠ transferable**: Top performance on seen-image reconstruction does not predict mental imagery performance
3. **MIRAGE bridges the gap**: The proposed multi-modal, multi-loss architecture achieves strong performance on both tasks
4. **NSD-Imagery analysis**: Comprehensive evaluation on the recently released NSD-Imagery dataset reveals divergent failure modes between seen and imagined reconstruction
5. **Architecture matters**: The choice of backbone architecture and training objective critically affects cross-domain generalization

## Core Mechanisms

### Multi-Modal Architecture
- **Multiple backbone integration**: Combines complementary visual representation backbones
- **Cross-modal fusion**: Merges information from different representational spaces
- **Shared latent space**: Aligns seen and imagined brain activity in a common embedding

### Multi-Loss Training
- **Reconstruction loss**: Pixel-level fidelity for seen images
- **Perceptual loss**: Semantic feature preservation
- **Domain alignment loss**: Encourages shared representations between seen and imagined conditions
- **Adversarial loss**: Improves output realism

### Cross-Domain Generalization
- Training on seen-image fMRI data
- Zero-shot or few-shot adaptation to mental imagery
- Architecture design choices that specifically support this transfer

## Methodology

### Dataset: NSD-Imagery
- Natural Scenes Dataset extended with mental imagery trials
- Subjects viewed images (seen condition) and later imagined them (imagery condition)
- Both 7T fMRI responses and behavioral data collected

### Evaluation Protocol
- **Seen reconstruction**: Standard pixel-level and semantic metrics (pixcorr, SSIM, AlexNet/Inception distances)
- **Imagery reconstruction**: Same metrics applied to imagined condition
- **Transfer analysis**: Compare per-architecture performance across both conditions

### Key Metrics
- Pixel-level similarity (pixcorr, SSIM)
- Perceptual similarity (LPIPS, DreamSim)
- Semantic alignment (CLIP score, classification accuracy)

## Results

### Seen vs Imagery Performance
| Metric | Seen (top) | Imagery (top) | Delta |
|--------|-----------|--------------|-------|
| PixCorr | 0.72 | 0.43 | -40% |
| SSIM | 0.38 | 0.21 | -45% |
| AlexNet(2) | 85.2% | 68.1% | -20% |
| CLIP Score | 0.68 | 0.52 | -24% |

### MIRAGE Advantages
- Outperforms single-backbone baselines on both seen and imagery conditions
- Most pronounced advantage on imagery condition (up to 15% relative improvement)
- Training with domain alignment loss is critical for imagery generalization

## Significance

### For Neuroscience
- Reveals fundamental differences between visual perception and mental imagery in brain activity patterns
- Provides a computational framework for studying how the brain represents internally generated vs externally perceived content
- Suggests shared but not identical neural representations for seen and imagined content

### For Brain-Computer Interfaces
- Enables practical mental imagery decoding for communication BCIs
- Framework for developing decoders that work in real-world scenarios where users imagine rather than view
- Opens possibilities for creative applications (thought-to-image generation)

### For AI / Machine Learning
- Important case study in domain generalization for brain decoding
- Multi-modal fusion strategy applicable to other sensory decoding tasks
- Demonstrates that SOTA on one domain does not guarantee robustness in related domains

## Activation Keywords
- mental imagery fMRI decoding
- seen-to-imagery transfer brain decoding
- MIRAGE architecture
- fMRI visual reconstruction
- brain decoding domain generalization
- NSD-Imagery dataset
- multi-modal brain decoding

## References
- Kneeland, R. et al. (2026). MIRAGE: Robust Multi-Modal Architectures Translate fMRI-to-Image Models from Vision to Mental Imagery. arXiv:2605.17198
- Scotti et al. (2024). MindEye2: Shared-Subject Models Enable fMRI-to-Image With 1 Hour of Data
- Takagi & Nishimoto (2023). High-resolution image reconstruction with latent diffusion models
- Chen et al. (2024). Design principles for robust fMRI decoding
- NSD-Imagery dataset documentation
