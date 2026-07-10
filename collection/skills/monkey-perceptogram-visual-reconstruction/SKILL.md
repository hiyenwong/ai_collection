---
name: monkey-perceptogram-visual-reconstruction
description: "Perceptogram: visual reconstruction framework from monkey neural activity — decoding perceived images from primate visual cortex recordings using deep generative models. Activation: monkey visual reconstruction, perceptogram, primate neuroscience, visual decoding, neural-to-image, brain-to-image, visual cortex, perceptual reconstruction."
---

# Perceptogram: Visual Reconstruction from Monkey Neural Activity

> Framework for reconstructing perceived visual stimuli from monkey visual cortex neural recordings, advancing cross-species brain-to-image decoding using deep generative models.

## Metadata
- **Source**: arXiv:2510.07576
- **Authors**: Teng Fei, Wenrui Zhao, Yiyuan Yang, Mingmin Zhao, Xiaoliang Li, Yujie Luo, Lu Zhang, Rufeng Li
- **Published**: 2025-10-09
- **Categories**: q-bio.NC

## Core Methodology

### Key Innovation
Develops "Perceptogram" — a framework specifically designed for reconstructing visual percepts from monkey visual cortex activity. Unlike human fMRI-based visual reconstruction, this method works with primate electrophysiology (single-unit/multi-unit recordings) which has different spatial resolution and noise characteristics.

### Technical Framework
1. **Neural Recording**: Multi-electrode array recordings from monkey visual cortex (V1, V4, IT) during visual stimulus presentation
2. **Neural Feature Extraction**: Convert spike trains to time-binned firing rates, apply population-level dimensionality reduction (PCA/FA)
3. **Perceptogram Decoder**: Deep convolutional decoder mapping neural features → reconstructed images
4. **Training**: Paired neural-visual data with perceptual loss (LPIPS) + pixel loss + adversarial loss
5. **Cross-Session Alignment**: Handle session-to-session variability via shared latent alignment

### Implementation Guide

#### Prerequisites
- Primate electrophysiology data analysis
- Deep generative models (VAE, GAN, diffusion)
- Visual cortex neuroscience (V1→V4→IT hierarchy)
- Spike train processing

#### Step-by-Step
1. **Data Collection**: Record multi-unit activity from visual cortex during stimulus presentation
2. **Spike Processing**: Bin spikes (e.g., 50ms windows), z-score firing rates per unit
3. **Feature Engineering**: Apply PCA to population vectors, retain top-k components
4. **Train Perceptogram**: Neural features → CNN decoder → reconstructed image
5. **Evaluation**: Low-level (MSE, SSIM) + high-level (category accuracy, LPIPS) metrics

### Code Example
```python
import torch
import torch.nn as nn

class PerceptogramDecoder(nn.Module):
    """Decode perceived images from monkey visual cortex neural features."""
    def __init__(self, neural_dim=256, img_size=64, latent_dim=512):
        super().__init__()
        # Neural features → latent image representation
        self.neural_encoder = nn.Sequential(
            nn.Linear(neural_dim, 1024),
            nn.ReLU(),
            nn.Linear(1024, latent_dim),
            nn.ReLU()
        )
        # Reshape to spatial feature map and upsample
        self.decoder = nn.Sequential(
            nn.ConvTranspose2d(latent_dim // 64, 256, 4, 1, 0),  # 4x4
            nn.BatchNorm2d(256), nn.ReLU(),
            nn.ConvTranspose2d(256, 128, 4, 2, 1),  # 8x8
            nn.BatchNorm2d(128), nn.ReLU(),
            nn.ConvTranspose2d(128, 64, 4, 2, 1),  # 16x16
            nn.BatchNorm2d(64), nn.ReLU(),
            nn.ConvTranspose2d(64, 32, 4, 2, 1),  # 32x32
            nn.BatchNorm2d(32), nn.ReLU(),
            nn.ConvTranspose2d(32, 3, 4, 2, 1),  # 64x64
            nn.Sigmoid()
        )
    
    def forward(self, neural_features):
        latent = self.neural_encoder(neural_features)
        spatial = latent.view(-1, latent.size(-1) // 64, 8, 8)
        return self.decoder(spatial)

# Training with multi-loss
def perceptogram_loss(recon, target, discriminator=None, alpha=0.5):
    pixel_loss = nn.functional.mse_loss(recon, target)
    perceptual_loss = compute_lpips(recon, target)  # LPIPS metric
    total = alpha * pixel_loss + (1 - alpha) * perceptual_loss
    if discriminator is not None:
        adv_loss = -discriminator(recon).mean()
        total += 0.1 * adv_loss
    return total
```

## Applications
- **Primate Visual Neuroscience**: Reconstruct what monkeys perceive from cortical recordings
- **Cross-Species Visual Decoding**: Bridge human fMRI and primate electrophysiology decoding
- **Brain-Machine Interface**: Visual prosthetic development using electrophysiological signals
- **Comparative Neuroscience**: Compare visual representations across species via reconstruction quality

## Pitfalls
- Monkey electrophysiology has limited spatial coverage (few hundred electrodes vs whole-brain fMRI)
- Electrode arrays sample unevenly across visual areas
- Stimulus sets for monkeys are simpler than human visual decoding studies
- Cross-session alignment challenging due to electrode drift and neural plasticity

## Related Skills
- brain-inspired-capture-visual-decoding
- eeg2vision-multimodal-eeg-framework-2d-visual
- visual-imagery-decoding-fmri
- primate-ventral-visual-stream-dynamic
