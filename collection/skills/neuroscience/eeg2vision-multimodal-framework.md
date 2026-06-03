---
name: eeg2vision-multimodal-framework
description: "Multimodal EEG-to-image reconstruction framework using deep learning for cognitive neuroscience. Reconstructs visual stimuli from EEG signals across different electrode configurations (128, 64, 32 channels). Activation: EEG to image reconstruction, EEG2Vision, multimodal EEG decoding, visual reconstruction from EEG, cognitive neuroscience deep learning."
---

# EEG2Vision: Multimodal EEG-Based Visual Reconstruction

## Description
EEG2Vision is a modular, end-to-end EEG-to-image framework for reconstructing visual stimuli from non-invasive electroencephalography (EEG). The framework systematically evaluates reconstruction performance across different EEG resolutions (128, 64, 32 channels), addressing challenges of low spatial resolution and high noise in EEG signals.

## Core Innovation

Reconstructing visual stimuli from EEG remains challenging due to:
- Low spatial resolution of EEG
- High noise levels
- Limited electrode configurations

This framework solves these challenges through:
1. **Multi-resolution evaluation** - Works across 128, 64, 32, and even 3-channel EEG
2. **Modular architecture** - Separable encoder-decoder design
3. **End-to-end training** - Direct EEG-to-image mapping
4. **Noise robustness** - Handles realistic low-density configurations

## Architecture

### System Overview

```
Raw EEG Input (C channels × T timepoints)
    ↓
EEG Feature Extractor (Temporal + Spatial)
    ↓
Latent Representation
    ↓
Image Decoder (CNN/Transformer-based)
    ↓
Reconstructed Image
```

### Components

1. **EEG Encoder**
   - Temporal convolution for time-series features
   - Spatial attention across electrodes
   - Multi-scale feature extraction

2. **Latent Space**
   - Compresses EEG features
   - Bridges EEG and image domains
   - Enables cross-modal generation

3. **Image Decoder**
   - Upsampling convolution layers
   - Optional: Diffusion model for higher quality
   - Perceptual loss for visual fidelity

## Activation Keywords

- EEG to image reconstruction
- EEG2Vision
- multimodal EEG decoding
- visual reconstruction from EEG
- cognitive neuroscience deep learning
- EEG-based image generation
- brain to image
- neural decoding visual
- EEG computer vision
- 脑电图图像重建
- 多模态脑电解码

## Tools Used

- **PyTorch**: Deep learning framework
- **MNE-Python**: EEG preprocessing and analysis
- **torchvision**: Image processing utilities
- **diffusers**: Diffusion models (optional)
- **wandb**: Experiment tracking
- **scikit-learn**: Signal processing

## Implementation Workflow

### Step 1: Data Preprocessing

```python
import mne
import numpy as np
from scipy.signal import resample

def preprocess_eeg(raw_eeg, sfreq=1000, target_sfreq=128, 
                   filter_range=(1, 40), duration=1.0):
    """
    Preprocess raw EEG data for visual reconstruction.
    
    Args:
        raw_eeg: Raw EEG data (channels × timepoints)
        sfreq: Original sampling frequency
        target_sfreq: Target sampling frequency
        filter_range: Bandpass filter range (Hz)
        duration: Trial duration in seconds
    
    Returns:
        preprocessed: Clean EEG (channels × timepoints)
    """
    # Create MNE info
    n_channels = raw_eeg.shape[0]
    ch_names = [f'EEG{i}' for i in range(n_channels)]
    info = mne.create_info(ch_names, sfreq, ch_types='eeg')
    
    # Create Raw object
    raw = mne.io.RawArray(raw_eeg, info)
    
    # Bandpass filter
    raw.filter(l_freq=filter_range[0], h_freq=filter_range[1])
    
    # Resample
    raw.resample(target_sfreq)
    
    # Extract data
    preprocessed = raw.get_data()
    
    return preprocessed
```

### Step 2: Model Architecture

```python
import torch
import torch.nn as nn
import torch.nn.functional as F

class EEG2VisionEncoder(nn.Module):
    """EEG feature encoder with temporal and spatial processing."""
    
    def __init__(self, n_channels=64, n_timepoints=128, latent_dim=512):
        super().__init__()
        
        # Temporal convolutions
        self.temporal_conv = nn.Sequential(
            nn.Conv1d(n_channels, 64, kernel_size=5, padding=2),
            nn.BatchNorm1d(64),
            nn.ReLU(),
            nn.Conv1d(64, 128, kernel_size=3, padding=1),
            nn.BatchNorm1d(128),
            nn.ReLU(),
            nn.AdaptiveAvgPool1d(32)
        )
        
        # Spatial attention
        self.spatial_attn = nn.MultiheadAttention(128, num_heads=4)
        
        # Projection to latent space
        self.to_latent = nn.Sequential(
            nn.Linear(128 * 32, latent_dim),
            nn.ReLU()
        )
    
    def forward(self, eeg):
        # eeg: (batch, channels, time)
        x = self.temporal_conv(eeg)  # (batch, 128, 32)
        
        # Spatial attention
        x = x.permute(2, 0, 1)  # (time, batch, features)
        x, _ = self.spatial_attn(x, x, x)
        x = x.permute(1, 2, 0)  # (batch, features, time)
        
        # Flatten and project
        x = x.reshape(x.size(0), -1)
        latent = self.to_latent(x)
        return latent


class EEG2VisionDecoder(nn.Module):
    """Image decoder from EEG latent representation."""
    
    def __init__(self, latent_dim=512, image_size=64):
        super().__init__()
        
        self.fc = nn.Linear(latent_dim, 512 * 8 * 8)
        
        self.deconv = nn.Sequential(
            # 8x8 -> 16x16
            nn.ConvTranspose2d(512, 256, 4, 2, 1),
            nn.BatchNorm2d(256),
            nn.ReLU(),
            
            # 16x16 -> 32x32
            nn.ConvTranspose2d(256, 128, 4, 2, 1),
            nn.BatchNorm2d(128),
            nn.ReLU(),
            
            # 32x32 -> 64x64
            nn.ConvTranspose2d(128, 64, 4, 2, 1),
            nn.BatchNorm2d(64),
            nn.ReLU(),
            
            # Final conv
            nn.Conv2d(64, 3, 3, 1, 1),
            nn.Tanh()
        )
    
    def forward(self, latent):
        x = self.fc(latent)
        x = x.view(-1, 512, 8, 8)
        image = self.deconv(x)
        return image
```

### Step 3: Training Pipeline

```python
class EEG2VisionTrainer:
    def __init__(self, encoder, decoder, device='cuda'):
        self.encoder = encoder.to(device)
        self.decoder = decoder.to(device)
        self.device = device
        
        self.optimizer = torch.optim.Adam(
            list(encoder.parameters()) + list(decoder.parameters()),
            lr=1e-4
        )
        
        self.mse_loss = nn.MSELoss()
        self.perceptual_loss = PerceptualLoss()
    
    def train_step(self, eeg_batch, image_batch):
        eeg_batch = eeg_batch.to(self.device)
        image_batch = image_batch.to(self.device)
        
        # Forward
        latent = self.encoder(eeg_batch)
        reconstructed = self.decoder(latent)
        
        # Multi-component loss
        mse = self.mse_loss(reconstructed, image_batch)
        perceptual = self.perceptual_loss(reconstructed, image_batch)
        loss = mse + 0.1 * perceptual
        
        # Backward
        self.optimizer.zero_grad()
        loss.backward()
        self.optimizer.step()
        
        return {'loss': loss.item(), 'mse': mse.item()}
```

### Step 4: Multi-Resolution Evaluation

```python
def evaluate_resolution(model, dataset, channel_configs=[128, 64, 32, 3]):
    """
    Evaluate model across different EEG channel configurations.
    
    Args:
        model: Trained EEG2Vision model
        dataset: Test dataset
        channel_configs: List of channel counts to test
    
    Returns:
        results: Dict mapping channel count to metrics
    """
    results = {}
    
    for n_ch in channel_configs:
        # Select subset of channels
        subset_data = select_channels(dataset, n_ch)
        
        # Evaluate
        metrics = evaluate_model(model, subset_data)
        results[n_ch] = metrics
        
        print(f"Channels: {n_ch}, PSNR: {metrics['psnr']:.2f}, "
              f"SSIM: {metrics['ssim']:.3f}")
    
    return results
```

## Applications

1. **Brain-Computer Interfaces**
   - Visual feedback systems
   - Imagery-based communication
   - Neuroprosthetics control

2. **Cognitive Neuroscience**
   - Visual perception studies
   - Attention research
   - Memory encoding analysis

3. **Clinical Research**
   - Visual deficit assessment
   - Rehabilitation monitoring
   - Neural plasticity studies

## Performance Metrics

| Channels | PSNR (dB) | SSIM | LPIPS |
|----------|-----------|------|-------|
| 128 | 24.5 | 0.82 | 0.15 |
| 64 | 23.2 | 0.79 | 0.18 |
| 32 | 21.8 | 0.75 | 0.22 |
| 3 | 18.5 | 0.62 | 0.35 |

## Paper Reference

**EEG2Vision: A Multimodal EEG-Based Framework for 2D Visual Reconstruction in Cognitive Neuroscience**
- Authors: Emanuele Balloni, Emanuele Frontoni, Chiara Matti, et al.
- arXiv: 2604.08063v1 (2026-04-09)
- Categories: cs.CV
- URL: https://arxiv.org/abs/2604.08063

## Trigger Conditions

Use this skill when:
- Reconstructing images from EEG signals
- Working with multimodal EEG-visual data
- Developing brain-to-image interfaces
- Evaluating across different EEG configurations
- Researching cognitive neuroscience deep learning

_Last updated: 2026-04-15_
