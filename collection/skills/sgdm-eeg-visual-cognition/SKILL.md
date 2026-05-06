---
name: sgdm-eeg-visual-cognition
description: "Structure-Guided Diffusion Model (SGDM) for EEG-based visual cognition reconstruction. Leverages brain structural information to guide diffusion process for improved visual stimulus reconstruction from EEG. Keywords: EEG, diffusion model, visual reconstruction, brain structure, BCI."
---

# Structure-Guided Diffusion Model for EEG-Based Visual Cognition

> Structure-Guided Diffusion Model (SGDM) incorporating brain anatomical information to guide the reconstruction of visual stimuli from EEG signals, improving upon standard diffusion approaches for brain-computer interface applications.

## Metadata
- **Source**: arXiv:2604.22649
- **Authors**: Yongxiang Lian, Yueyang Cang, Pingge Hu
- **Published**: 2026-04-24

## Core Methodology

### Key Innovation
Decoding visual information from EEG is challenging due to:
- Low spatial resolution of scalp recordings
- Volume conduction blurring neural sources
- Individual anatomical variations affecting signal propagation

SGDM addresses this by leveraging brain structure to:
1. Guide the diffusion generation process with anatomical constraints
2. Incorporate individual cortical geometry via forward models
3. Condition image generation on structural priors
4. Improve reconstruction quality over standard latent diffusion

### Technical Framework
1. **Structural Encoder**: Brain anatomy to latent conditioning vectors
2. **EEG Feature Extractor**: Temporal-spatial feature extraction
3. **Guided Diffusion Process**: Structural conditioning at each denoising step
4. **Cross-Modal Fusion**: Integration of neural and anatomical information

## Implementation Guide

### Prerequisites
- Diffusers library (HuggingFace)
- PyTorch for deep learning
- MNE-Python for EEG processing
- Forward modeling (e.g., OpenMEEG, FieldTrip)

### Step-by-Step
1. Compute individual forward model: Anatomy to sensor projection
2. Train structural encoder: Cortical regions to conditioning space
3. Extract EEG features: Spatiotemporal patterns encoding visual information
4. Fine-tune diffusion model: With structural guidance mechanism
5. Generate reconstructions: Conditioned on both EEG and structure

### Code Example
```python
import torch
import torch.nn as nn
from diffusers import DDPMScheduler, UNet2DConditionModel

class StructureGuidedDiffusion(nn.Module):
    """Diffusion model guided by brain structure for EEG visual reconstruction"""
    def __init__(self, eeg_channels, n_cortical_regions, image_size=256):
        super().__init__()
        # EEG feature extractor
        self.eeg_encoder = nn.Sequential(
            nn.Conv1d(eeg_channels, 64, kernel_size=3, padding=1),
            nn.ReLU(),
            nn.AdaptiveAvgPool1d(64),
            nn.Flatten(),
            nn.Linear(64*64, 512)
        )
        
        # Structural encoder
        self.structural_encoder = nn.Sequential(
            nn.Linear(n_cortical_regions, 256),
            nn.ReLU(),
            nn.Linear(256, 512)
        )
        
        # Cross-modal fusion
        self.fusion = nn.MultiheadAttention(embed_dim=512, num_heads=8)
        
        # Conditional diffusion UNet
        self.unet = UNet2DConditionModel(
            sample_size=image_size,
            in_channels=3,
            out_channels=3,
            cross_attention_dim=512
        )
        
    def forward(self, noisy_image, timestep, eeg, structural_prior):
        # Encode EEG and structural information
        eeg_features = self.eeg_encoder(eeg)
        struct_features = self.structural_encoder(structural_prior)
        
        # Cross-modal fusion
        combined = torch.stack([eeg_features, struct_features], dim=0)
        fused, _ = self.fusion(combined, combined, combined)
        conditioning = fused.mean(dim=0)
        
        # Structure-guided denoising
        noise_pred = self.unet(noisy_image, timestep, conditioning)
        return noise_pred

def generate_reconstruction(model, eeg_data, structural_prior, num_steps=50):
    """Generate visual reconstruction from EEG with structural guidance"""
    scheduler = DDPMScheduler(num_train_timesteps=1000)
    scheduler.set_timesteps(num_steps)
    
    # Start from random noise
    image = torch.randn(1, 3, 256, 256)
    
    for t in scheduler.timesteps:
        noise_pred = model(image, t, eeg_data, structural_prior)
        image = scheduler.step(noise_pred, t, image).prev_sample
    
    return image
```

## Applications
- Visual BCI: Thought-to-image interfaces
- Dream reconstruction: Decoding visual imagery from EEG
- Perceptual decoding: Understanding visual processing
- Clinical assessment: Quantifying visual perception deficits

## Pitfalls
- Requires individual MRI for optimal structural guidance
- High computational cost for diffusion sampling
- Limited by EEG spatial resolution even with structural priors

## Related Skills
- eeg-structure-guided-diffusion
- eeg-3d-visual-decoding
- brain-inspired-capture-evidence-driven
