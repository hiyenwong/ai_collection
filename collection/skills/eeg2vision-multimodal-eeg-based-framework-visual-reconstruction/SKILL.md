---
name: eeg2vision-multimodal-eeg-based-framework-visual-reconstruction
description: "EEG2Vision: A Multimodal EEG-Based Framework for 2D Visual Reconstruction in Cognitive Neuroscience - Reconstructing visual stimuli from non-invasive electroencephalography (EEG) remains challenging due to its low spatial resolution and high noise, particularly under realistic low-density electrode co... From arXiv:2604.08063v1.  Activation: EEG-to-vision, visual reconstruction, multimodal EEG, cognitive neuroscience, diffusion model"
---

# EEG2Vision: A Multimodal EEG-Based Framework for 2D Visual Reconstruction in Cognitive Neuroscience

## Source

- **arXiv ID**: [2604.08063v1](http://arxiv.org/abs/2604.08063v1)
- **PDF**: [https://arxiv.org/pdf/2604.08063v1](https://arxiv.org/pdf/2604.08063v1)
- **Authors**: Emanuele Balloni, Emanuele Frontoni, Chiara Matti, Marina Paolanti et al.
- **Published**: 2026-04-09

## Abstract

Reconstructing visual stimuli from non-invasive electroencephalography (EEG) remains challenging due to its low spatial resolution and high noise, particularly under realistic low-density electrode configurations. To address this, we present EEG2Vision, a modular, end-to-end EEG-to-image framework that systematically evaluates reconstruction performance across different EEG resolutions (128, 64, 32, and 24 channels) and enhances visual quality through a prompt-guided post-reconstruction boosting mechanism. Starting from EEG-conditioned diffusion reconstruction, the boosting stage uses a multimodal large language model to extract semantic descriptions and leverages image-to-image diffusion to refine geometry and perceptual coherence while preserving EEG-grounded structure. Our experiments show that semantic decoding accuracy degrades significantly with channel reduction (e.g., 50-way Top-1 Acc from 89% to 38%), while reconstruction quality slight decreases (e.g., FID from 76.77 to 80.51). The proposed boosting consistently improves perceptual metrics across all configurations, achieving up to 9.71% IS gains in low-channel settings. A user study confirms the clear perceptual preference for boosted reconstructions. The proposed approach significantly boosts the feasibility of real-time brain-2-image applications using low-resolution EEG devices, potentially unlocking this type of applications outside laboratory settings.

## Methodology

### Core Approach
1. **Multimodal EEG Processing**: Combines multiple EEG frequency bands and spatial features
2. **Diffusion-Based Image Generation**: Uses latent diffusion models for visual reconstruction
3. **Low-Density Electrode Support**: Works with realistic, low-density EEG configurations

### Technical Implementation
- Multi-scale EEG feature extraction
- Cross-modal alignment between EEG and image embeddings
- Conditional diffusion model for image generation
- Modular architecture supporting various electrode densities

### Key Benefits
- Non-invasive visual decoding from brain signals
- Works with consumer-grade EEG devices
- Potential for brain-computer interface applications

## Activation Keywords

- EEG-to-vision
- visual reconstruction
- multimodal EEG
- cognitive neuroscience
- diffusion model

## Applications

- Neuroscience research
- Brain-computer interfaces
- Cognitive computing
- Neural decoding
- Artificial intelligence

## References

- Original Paper: http://arxiv.org/abs/2604.08063v1
- arXiv Category: q-bio.NC (Neurons and Cognition)

---

*Generated from arXiv paper on 2026-04-17*
