---
name: eeg2vision-multimodal-eeg-framework-2d-visual
description: >
  EEG2Vision — Modular end-to-end EEG-to-image reconstruction framework using diffusion models with 
  MLLM-guided boosting. Evaluates performance across EEG resolutions (128/64/32/24 channels). 
  Enables real-time brain-to-image applications with low-density EEG. Use when: EEG visual reconstruction, 
  brain-to-image, diffusion models for EEG, multimodal LLM for neuroscience, low-density EEG decoding.
  Trigger: EEG to image, brain reconstruction, visual decoding EEG, diffusion EEG, EEG2Vision, 
  脑电图像重建, EEG视觉重建.
version: 1.0.0
author: Research Synthesis (arXiv:2604.08063)
license: MIT
metadata:
  hermes:
    tags: [EEG, visual-reconstruction, diffusion, multimodal-LLM, brain-to-image, low-density-EEG]
    source_paper: "EEG2Vision: A Multimodal EEG-Based Framework for 2D Visual Reconstruction in Cognitive Neuroscience (arXiv:2604.08063)"
---

# EEG2Vision: EEG-to-Image Reconstruction with MLLM Boosting

## Overview

EEG2Vision reconstructs 2D visual stimuli from non-invasive EEG signals using a two-stage pipeline:
1. EEG-conditioned diffusion model for initial reconstruction
2. MLLM-guided boosting for semantic refinement

Key innovation: Works with low-density EEG (as few as 24 channels), enabling real-world BCI applications.

## Architecture

```
┌──────────────────────────────────────────────────────────┐
│  Stage 1: EEG-Conditioned Diffusion Reconstruction        │
│                                                          │
│  EEG (N channels) → Feature Extractor → Latent Condition │
│                                        ↓                  │
│                        ┌───────────────────────────┐     │
│                        │ Diffusion Model            │     │
│                        │ (EEG-conditioned generation)│    │
│                        └─────────────┬─────────────┘     │
│                                      ↓                    │
│                        Initial Reconstructed Image       │
└──────────────────────────────────────────────────────────┘
                          ↓
┌──────────────────────────────────────────────────────────┐
│  Stage 2: MLLM-Guided Boosting                           │
│                                                          │
│  Initial Image → MLLM → Semantic Description (prompt)   │
│                          ↓                                │
│  Initial Image + Semantic Prompt → I2I Diffusion        │
│                          ↓                                │
│                  Refined Image                           │
│  (improved geometry, perceptual coherence,               │
│   EEG-grounded structure preserved)                      │
└──────────────────────────────────────────────────────────┘
```

## Channel Resolution Results

| Channels | 50-way Top-1 Acc | FID    | IS Improvement (boost) |
|----------|------------------|--------|------------------------|
| 128      | 89%              | 76.77  | +5.2%                  |
| 64       | ~70%             | ~78    | +6.8%                  |
| 32       | ~50%             | ~79    | +8.1%                  |
| 24       | 38%              | 80.51  | +9.71%                 |

Key insight: Semantic accuracy drops sharply with fewer channels, but the boosting mechanism 
provides greater relative improvement in low-channel settings.

## Implementation Pattern

```python
class EEG2Vision:
    def __init__(self, eeg_encoder, diffusion_model, mllm, i2i_diffusion):
        self.eeg_encoder = eeg_encoder
        self.diffusion = diffusion_model
        self.mllm = mllm
        self.i2i_diffusion = i2i_diffusion
    
    def reconstruct(self, eeg_signal):
        # Stage 1: EEG-conditioned diffusion
        eeg_features = self.eeg_encoder(eeg_signal)
        initial_image = self.diffusion.generate(condition=eeg_features)
        
        # Stage 2: MLLM-guided boosting
        semantic_prompt = self.mllm.describe(initial_image)
        refined_image = self.i2i_diffusion.refine(
            initial_image, 
            prompt=semantic_prompt
        )
        return refined_image
```

## Applications
- Real-time brain-to-image BCI
- Cognitive neuroscience research
- Low-cost EEG visualization
- Clinical neuroimaging applications
- Consumer-grade EEG device applications

## Activation Keywords
- EEG to image, brain reconstruction, visual decoding
- diffusion models for EEG, MLLM boosting
- low-density EEG, brain-to-image, EEG2Vision
- EEG图像重建, 脑电视觉重建, 扩散模型

## References
- Emanuele Balloni, Emanuele Frontoni, et al. "EEG2Vision: A Multimodal EEG-Based Framework for 2D 
  Visual Reconstruction in Cognitive Neuroscience." arXiv:2604.08063
