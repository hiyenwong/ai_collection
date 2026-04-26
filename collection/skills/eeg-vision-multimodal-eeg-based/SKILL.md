---
name: eeg-vision-multimodal-eeg-based
description: "Reconstructing visual stimuli from non-invasive electroencephalography (EEG) remains challenging due to its low spatial resolution and high noise, particularly under realistic low-..."
---

# EEG2Vision: A Multimodal EEG-Based Framework for 2D Visual Reconstruction in Cognitive Neuroscience

## Overview
Reconstructing visual stimuli from non-invasive electroencephalography (EEG) remains challenging due to its low spatial resolution and high noise, particularly under realistic low-density electrode configurations. To address this, we present EEG2Vision, a modular, end-to-end EEG-to-image framework that systematically evaluates reconstruction performance across different EEG resolutions (128, 64, 32, and 24 channels) and enhances visual quality through a prompt-guided post-reconstruction boosting mechanism. Starting from EEG-conditioned diffusion reconstruction, the boosting stage uses a multimodal large language model to extract semantic descriptions and leverages image-to-image diffusion to refine geometry and perceptual coherence while preserving EEG-grounded structure. Our experiments show that semantic decoding accuracy degrades significantly with channel reduction (e.g., 50-way Top-1 Acc from 89% to 38%), while reconstruction quality slight decreases (e.g., FID from 76.77 to 80.51). The proposed boosting consistently improves perceptual metrics across all configurations, achieving up to 9.71% IS gains in low-channel settings. A user study confirms the clear perceptual preference for boosted reconstructions. The proposed approach significantly boosts the feasibility of real-time brain-2-image applications using low-resolution EEG devices, potentially unlocking this type of applications outside laboratory settings.

## Source
- **arXiv:** 2604.08063v1
- **Date:** 2026-04-09
- **Authors:** Emanuele Balloni, Emanuele Frontoni, Chiara Matti et al.
- **Categories:** cs.CV

## Methods
- Computational neuroscience

## Applications
- Brain data analysis and neural modeling
- Neuroscience research and development

## References
Emanuele Balloni et al. arXiv:2604.08063v1

## Keywords
- neuroscience
- cs.CV
