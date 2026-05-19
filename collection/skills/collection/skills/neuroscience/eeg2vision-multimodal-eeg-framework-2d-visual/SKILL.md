---
name: eeg2vision-multimodal-eeg-framework-2d-visual
description: EEG-to-image reconstruction framework using diffusion models with multimodal LLM-guided boosting for geometry and perceptual coherence refinement. Systematically evaluates 128/64/32/24-channel EEG configurations for low-density deployment.
version: 2.0.0
author: Research Synthesis
license: MIT
metadata:
  hermes:
    tags: [eeg, visual-reconstruction, diffusion-model, multimodal, brain-computer-interface, cognitive-neuroscience]
    source_paper: "EEG2Vision: A Multimodal EEG-Based Framework for 2D Visual Reconstruction in Cognitive Neuroscience (arXiv:2604.08898)"
    published: 2026-04-13
---

# EEG2Vision: Multimodal EEG-Based 2D Visual Reconstruction

## Overview

A modular, end-to-end EEG-to-image framework that systematically evaluates reconstruction performance across different EEG resolutions (128, 64, 32, and 24 channels) and enhances visual quality through a prompt-guided post-reconstruction boosting mechanism. Starting from EEG-conditioned diffusion reconstruction, the boosting stage uses a multimodal large language model to extract semantic descriptions and leverages image-to-image diffusion to refine geometry and perceptual coherence while preserving EEG-grounded structure.

## Core Problem

Reconstructing visual stimuli from non-invasive EEG remains challenging due to low spatial resolution and high noise, particularly under realistic low-density electrode configurations. Existing methods struggle with geometry coherence and perceptual quality when using fewer than 64 channels.

## Key Architecture

### Two-Stage Pipeline

**Stage 1: EEG-Conditioned Diffusion Reconstruction**
- Maps EEG signals to visual features via learned projection
- Uses diffusion model conditioned on EEG embeddings
- Produces initial image reconstruction grounded in neural data

**Stage 2: MLLM-Guided Boosting**
- Multimodal LLM extracts semantic descriptions from Stage 1 output
- Image-to-image diffusion refines geometry and perceptual coherence
- Preserves EEG-grounded structure while improving visual quality

## Implementation Pattern

```python
import torch
import torch.nn as nn
from diffusers import StableDiffusionPipeline, StableDiffusionImg2ImgPipeline

class EEG2Vision(nn.Module):
    """
    Two-stage EEG-to-image reconstruction framework.
    Stage 1: EEG-conditioned diffusion for initial reconstruction
    Stage 2: MLLM-guided boosting for geometry/perceptual refinement
    """
    
    def __init__(self, n_channels=64, eeg_sample_rate=250, 
                 eeg_window=2.0, latent_dim=768):
        super().__init__()
        self.n_channels = n_channels
        self.eeg_len = int(eeg_sample_rate * eeg_window)
        
        # EEG feature extractor
        self.eeg_encoder = nn.Sequential(
            nn.Conv1d(n_channels, 128, kernel_size=3, padding=1),
            nn.BatchNorm1d(128),
            nn.GELU(),
            nn.Conv1d(128, 256, kernel_size=3, padding=1),
            nn.AdaptiveAvgPool1d(1),
            nn.Flatten(),
            nn.Linear(256, latent_dim),
            nn.LayerNorm(latent_dim)
        )
        
        # EEG-to-CLIP feature mapper
        self.eeg_to_clip = nn.Sequential(
            nn.Linear(latent_dim, 1024),
            nn.LayerNorm(1024),
            nn.GELU(),
            nn.Linear(1024, 768)  # CLIP ViT-L/14 dimension
        )
    
    def stage1_reconstruct(self, eeg_signal, diffusion_pipeline):
        """
        Stage 1: EEG-conditioned diffusion reconstruction.
        
        Args:
            eeg_signal: [B, n_channels, eeg_len]
            diffusion_pipeline: StableDiffusionPipeline
        Returns:
            initial_image: PIL Image
        """
        eeg_features = self.eeg_encoder(eeg_signal)
        clip_embedding = self.eeg_to_clip(eeg_features)
        
        # Use CLIP embedding as conditioning for diffusion
        image_latents = diffusion_pipeline(
            prompt_embeds=clip_embedding.unsqueeze(0),
            guidance_scale=7.5,
            num_inference_steps=50
        ).images[0]
        
        return image_latents
    
    def stage2_boost(self, initial_image, mllm, img2img_pipeline,
                     strength=0.35):
        """
        Stage 2: MLLM-guided boosting for refinement.
        
        Args:
            initial_image: PIL Image from Stage 1
            mllm: Multimodal LLM for semantic extraction
            img2img_pipeline: StableDiffusionImg2ImgPipeline
            strength: How much to modify (lower = preserve more)
        Returns:
            boosted_image: Refined PIL Image
        """
        # Extract semantic description from MLLM
        prompt = mllm.describe_image(initial_image)
        
        # Refine via image-to-image diffusion
        boosted = img2img_pipeline(
            prompt=prompt,
            image=initial_image,
            strength=strength,  # Preserve EEG-grounded structure
            guidance_scale=7.5,
            num_inference_steps=30
        ).images[0]
        
        return boosted
    
    def forward(self, eeg_signal, diffusion_pipeline, 
                mllm, img2img_pipeline):
        """Full pipeline: EEG → initial image → boosted image."""
        initial = self.stage1_reconstruct(eeg_signal, diffusion_pipeline)
        boosted = self.stage2_boost(initial, mllm, img2img_pipeline)
        return initial, boosted


# Usage example
def reconstruct_from_eeg(eeg_data, n_channels=64):
    """End-to-end visual reconstruction from EEG."""
    model = EEG2Vision(n_channels=n_channels)
    
    # Load pretrained components
    text2img = StableDiffusionPipeline.from_pretrained(
        "runwayml/stable-diffusion-v1-5", torch_dtype=torch.float16
    ).to("cuda")
    
    img2img = StableDiffusionImg2ImgPipeline.from_pretrained(
        "runwayml/stable-diffusion-v1-5", torch_dtype=torch.float16
    ).to("cuda")
    
    mllm = load_mllm()  # e.g., LLaVA, Qwen-VL
    
    initial, boosted = model(eeg_data, text2img, mllm, img2img)
    return initial, boosted
```

## Channel Resolution Trade-offs

| Channels | Use Case | Quality |
|----------|----------|---------|
| 128 | Research-grade | Highest fidelity |
| 64 | Standard lab setup | Good quality |
| 32 | Portable/clinical | Acceptable |
| 24 | Consumer wearable | Boosting critical |

The MLLM-guided boosting stage is especially valuable for low-density configurations (32/24 channels) where Stage 1 reconstruction quality is limited.

## Activation Keywords

- eeg to image reconstruction
- visual reconstruction eeg
- diffusion model brain decoding
- eeg2vision
- multimodal brain-computer interface
- EEG视觉重建
- 脑电图图像重建
- 扩散模型脑解码
- cognitive neuroscience visual decoding
- low-density eeg reconstruction

## Applications

1. **BCI Visual Communication**: Enable locked-in patients to communicate visual thoughts
2. **Dream Visualization**: Reconstruct dream imagery from sleep EEG
3. **Neurofeedback**: Real-time visual feedback for cognitive training
4. **Cognitive Research**: Study visual processing through reconstruction

## References

- EEG2Vision: A Multimodal EEG-Based Framework for 2D Visual Reconstruction in Cognitive Neuroscience. arXiv:2604.08898, 2026-04-13.