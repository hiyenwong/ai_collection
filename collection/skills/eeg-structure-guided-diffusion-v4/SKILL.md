---
name: eeg-structure-guided-diffusion-v4
description: "Structure-Guided Diffusion Model (SGDM v4) for EEG-Based Visual Cognition Reconstruction. Diffusion-based framework for reconstructing visual stimuli from EEG with structural guidance for improved accuracy. Activation: SGDM, EEG reconstruction, visual cognition, structure-guided diffusion."
---

# Structure-Guided Diffusion Model (SGDM v4) for EEG-Based Visual Cognition Reconstruction

> Diffusion-based generative framework that reconstructs visual stimuli from EEG signals using structural guidance from semantic features and neural responses for accurate visual cognition decoding.

## Metadata
- **Source**: arXiv:2604.22649v1
- **Authors**: Yansen Wang, Yijun Zhang, Junjie Bu, Yining Wang, Ning Qiang, Jinfeng Li, Xiaorong Gao
- **Published**: 2026-04-24
- **Categories**: cs.CV, cs.AI, eess.SP

## Core Methodology

### Problem Statement
Decoding visual information from electroencephalography (EEG) is crucial for neuroscience and brain-computer interfaces. Existing methods are limited by:
- **Low Spatial Resolution**: EEG has poor spatial resolution compared to fMRI
- **High Noise**: EEG signals are noisy and artifact-prone
- **Limited Reconstruction Quality**: Existing methods produce blurry or semantically incorrect images
- **Cross-Subject Variability**: EEG patterns vary significantly across individuals

### Key Innovation
Structure-Guided Diffusion Model (SGDM) integrates:
1. **Semantic Structure Guidance**: Use pre-trained vision-language models for semantic constraints
2. **Neural Structure Guidance**: EEG-derived features guide the diffusion process
3. **Hierarchical Conditioning**: Multi-scale conditioning for coarse-to-fine reconstruction
4. **Cross-Modal Alignment**: Align EEG latent space with image latent space

### Technical Framework

#### Architecture Overview

```
┌─────────────────────────────────────────────────────────┐
│         Structure-Guided Diffusion Model (SGDM)          │
├─────────────────────────────────────────────────────────┤
│                                                          │
│  EEG Encoder                                             │
│  ├── Temporal Convolutions (capture temporal dynamics)   │
│  ├── Spatial Attention (focus on informative channels)   │
│  └── Projection to Latent Space (z_eeg)                  │
│                     ↓                                    │
│  Structure Extraction                                    │
│  ├── Semantic Features (CLIP embeddings)                 │
│  ├── Category Information (classifier guidance)          │
│  └── Neural Correlates (brain region activation)         │
│                     ↓                                    │
│  Conditional Diffusion Process                           │
│  ├── Forward: Add noise to image q(x_t | x_{t-1})        │
│  └── Reverse: Denoise with EEG guidance p(x_{t-1}|x_t,z) │
│                     ↓                                    │
│  Multi-Scale Reconstruction                              │
│  ├── Coarse structure (low resolution)                   │
│  ├── Mid-level features (medium resolution)              │
│  └── Fine details (high resolution)                      │
│                     ↓                                    │
│  Reconstructed Image                                     │
│                                                          │
└─────────────────────────────────────────────────────────┘
```

#### 1. EEG Encoding

Extract rich features from EEG:

```python
class EEGEncoder(nn.Module):
    """
    Encode EEG signals into latent representations
    """
    def __init__(self, n_channels=64, n_samples=512, latent_dim=512):
        super().__init__()
        
        # Temporal convolutions
        self.temporal_conv = nn.Sequential(
            nn.Conv1d(n_channels, 128, kernel_size=7, padding=3),
            nn.BatchNorm1d(128),
            nn.ReLU(),
            nn.Conv1d(128, 256, kernel_size=5, padding=2),
            nn.BatchNorm1d(256),
            nn.ReLU(),
            nn.AdaptiveAvgPool1d(128)
        )
        
        # Spatial attention
        self.spatial_attn = nn.MultiheadAttention(256, num_heads=8)
        
        # Projection to latent
        self.fc = nn.Sequential(
            nn.Linear(256 * 128, 1024),
            nn.ReLU(),
            nn.Dropout(0.3),
            nn.Linear(1024, latent_dim)
        )
        
    def forward(self, eeg):
        """
        Args:
            eeg: [batch, n_channels, n_samples]
        Returns:
            z_eeg: [batch, latent_dim]
        """
        # Temporal features
        x = self.temporal_conv(eeg)  # [batch, 256, 128]
        
        # Spatial attention across channels
        x = x.permute(2, 0, 1)  # [seq, batch, feat]
        x, _ = self.spatial_attn(x, x, x)
        x = x.permute(1, 0, 2)  # [batch, seq, feat]
        
        # Flatten and project
        x = x.reshape(x.size(0), -1)
        z_eeg = self.fc(x)
        
        return z_eeg
```

#### 2. Structure-Guided Diffusion

The diffusion process with dual guidance:

**Forward Process**:
```
q(x_t | x_{t-1}) = N(x_t; √(1-β_t) x_{t-1}, β_t I)

Where x_0 is the target image and x_T ~ N(0, I)
```

**Reverse Process with Structure Guidance**:
```
p(x_{t-1} | x_t, z_eeg, z_sem) = N(x_{t-1}; μ_θ(x_t, t, z_eeg, z_sem), Σ_θ(t))

μ_θ = (1/√α_t) (x_t - (β_t/√(1-ᾱ_t)) ε_θ(x_t, t, z_eeg, z_sem))
```

Where:
- `z_eeg`: EEG latent features
- `z_sem`: Semantic structure from CLIP
- `ε_θ`: Noise prediction network

#### 3. Multi-Scale Conditioning

Hierarchical guidance at different resolutions:

```python
class MultiScaleConditioning(nn.Module):
    """
    Apply EEG and semantic guidance at multiple scales
    """
    def __init__(self, latent_dim=512, n_scales=3):
        super().__init__()
        self.n_scales = n_scales
        
        # Scale-specific projections
        self.eeg_projections = nn.ModuleList([
            nn.Linear(latent_dim, 128 * (2**i))
            for i in range(n_scales)
        ])
        
        self.sem_projections = nn.ModuleList([
            nn.Linear(512, 128 * (2**i))  # CLIP dim = 512
            for i in range(n_scales)
        ])
        
    def forward(self, z_eeg, z_sem, scale):
        """
        Get conditioning vectors for specific scale
        """
        eeg_cond = self.eeg_projections[scale](z_eeg)
        sem_cond = self.sem_projections[scale](z_sem)
        
        return eeg_cond, sem_cond
```

## Implementation Guide

### Prerequisites
- PyTorch >= 2.0
- diffusers library for diffusion models
- CLIP for semantic features
- MNE-Python for EEG preprocessing
- CUDA-capable GPU (16GB+ VRAM recommended)

### Step-by-Step Implementation

#### 1. EEG Preprocessing

```python
import mne
import numpy as np
from scipy import signal

def preprocess_eeg(eeg_raw, sfreq=1000, l_freq=1, h_freq=50):
    """
    Preprocess raw EEG for reconstruction
    
    Args:
        eeg_raw: Raw EEG data [n_channels, n_times]
        sfreq: Sampling frequency
        l_freq, h_freq: Bandpass filter frequencies
    
    Returns:
        eeg_clean: Preprocessed EEG
    """
    # Create MNE Raw object
    info = mne.create_info(
        ch_names=[f'EEG{i}' for i in range(eeg_raw.shape[0])],
        sfreq=sfreq,
        ch_types='eeg'
    )
    raw = mne.io.RawArray(eeg_raw, info)
    
    # Filter
    raw.filter(l_freq=l_freq, h_freq=h_freq)
    
    # Artifact removal (ICA or SSP)
    ica = mne.preprocessing.ICA(n_components=15, random_state=42)
    ica.fit(raw)
    raw = ica.apply(raw)
    
    # Epoch around stimulus onset
    events = mne.make_fixed_length_events(raw, duration=0.5)
    epochs = mne.Epochs(raw, events, tmin=0, tmax=0.5, baseline=None)
    
    return epochs.get_data()  # [n_epochs, n_channels, n_times]
```

#### 2. Semantic Structure Extraction

```python
import clip
import torch

class SemanticExtractor:
    """
    Extract semantic structure using CLIP
    """
    def __init__(self, device='cuda'):
        self.device = device
        self.model, self.preprocess = clip.load("ViT-B/32", device=device)
        
    def extract_image_features(self, image):
        """
        Extract CLIP features from image
        
        Args:
            image: PIL Image or tensor
        Returns:
            features: [512] CLIP embedding
        """
        image_input = self.preprocess(image).unsqueeze(0).to(self.device)
        
        with torch.no_grad():
            image_features = self.model.encode_image(image_input)
            image_features = image_features / image_features.norm(dim=-1, keepdim=True)
        
        return image_features.cpu()
    
    def extract_text_features(self, text):
        """
        Extract CLIP features from text description
        """
        text_tokens = clip.tokenize([text]).to(self.device)
        
        with torch.no_grad():
            text_features = self.model.encode_text(text_tokens)
            text_features = text_features / text_features.norm(dim=-1, keepdim=True)
        
        return text_features.cpu()
    
    def semantic_similarity(self, features1, features2):
        """Compute cosine similarity between features"""
        return (features1 @ features2.T).item()
```

#### 3. Structure-Guided Diffusion Model

```python
import torch
import torch.nn as nn
from diffusers import UNet2DConditionModel, DDPMScheduler

class StructureGuidedDiffusion(nn.Module):
    """
    Complete SGDM for EEG-to-Image reconstruction
    """
    def __init__(self, eeg_latent_dim=512, image_size=256):
        super().__init__()
        
        # EEG encoder
        self.eeg_encoder = EEGEncoder(latent_dim=eeg_latent_dim)
        
        # Semantic encoder (frozen CLIP)
        self.semantic_extractor = SemanticExtractor()
        
        # UNet with conditioning
        self.unet = UNet2DConditionModel(
            sample_size=image_size // 8,  # Latent size
            in_channels=4,
            out_channels=4,
            layers_per_block=2,
            block_out_channels=(320, 640, 1280, 1280),
            cross_attention_dim=eeg_latent_dim + 512,  # EEG + Semantic
        )
        
        # VAE for latent space
        from diffusers import AutoencoderKL
        self.vae = AutoencoderKL.from_pretrained("stabilityai/sd-vae-ft-mse")
        
        # Scheduler
        self.scheduler = DDPMScheduler(num_train_timesteps=1000)
        
    def encode_image(self, image):
        """Encode image to latent space"""
        with torch.no_grad():
            latent = self.vae.encode(image).latent_dist.sample()
            latent = latent * 0.18215  # Scaling factor
        return latent
    
    def decode_latent(self, latent):
        """Decode latent to image"""
        latent = latent / 0.18215
        with torch.no_grad():
            image = self.vae.decode(latent).sample
        return image
    
    def forward(self, eeg, image, semantic_features=None):
        """
        Training forward pass
        
        Args:
            eeg: [batch, n_channels, n_samples]
            image: [batch, 3, H, W]
            semantic_features: [batch, 512] (optional, from CLIP)
        
        Returns:
            loss: Diffusion loss
        """
        batch_size = eeg.shape[0]
        
        # Encode EEG
        z_eeg = self.eeg_encoder(eeg)  # [batch, eeg_latent_dim]
        
        # Get semantic features if not provided
        if semantic_features is None:
            semantic_features = self.semantic_extractor.extract_image_features(image)
        
        # Combine conditions
        condition = torch.cat([z_eeg, semantic_features], dim=-1)  # [batch, eeg_latent_dim + 512]
        
        # Encode image to latent
        latent = self.encode_image(image)  # [batch, 4, H/8, W/8]
        
        # Sample timestep
        timesteps = torch.randint(
            0, self.scheduler.config.num_train_timesteps,
            (batch_size,), device=eeg.device
        ).long()
        
        # Add noise
        noise = torch.randn_like(latent)
        noisy_latent = self.scheduler.add_noise(latent, noise, timesteps)
        
        # Predict noise with conditioning
        noise_pred = self.unet(
            noisy_latent,
            timesteps,
            encoder_hidden_states=condition.unsqueeze(1)  # [batch, 1, cond_dim]
        ).sample
        
        # Loss
        loss = nn.functional.mse_loss(noise_pred, noise)
        
        return loss
    
    @torch.no_grad()
    def reconstruct(self, eeg, num_inference_steps=50, guidance_scale=7.5):
        """
        Reconstruct image from EEG
        
        Args:
            eeg: [batch, n_channels, n_samples]
            num_inference_steps: Number of denoising steps
            guidance_scale: Classifier-free guidance scale
        
        Returns:
            images: [batch, 3, H, W] reconstructed images
        """
        batch_size = eeg.shape[0]
        device = eeg.device
        
        # Encode EEG
        z_eeg = self.eeg_encoder(eeg)
        
        # Start from random noise
        latent = torch.randn(
            (batch_size, 4, 64, 64),
            device=device
        )
        
        # Semantic guidance (if available, otherwise use EEG only)
        # In practice, you might use a classifier to get semantic info
        semantic_dummy = torch.randn(batch_size, 512, device=device)
        condition = torch.cat([z_eeg, semantic_dummy], dim=-1)
        
        # Denoising loop
        self.scheduler.set_timesteps(num_inference_steps)
        
        for t in self.scheduler.timesteps:
            # Predict noise
            noise_pred = self.unet(
                latent,
                t,
                encoder_hidden_states=condition.unsqueeze(1)
            ).sample
            
            # Compute previous sample
            latent = self.scheduler.step(noise_pred, t, latent).prev_sample
        
        # Decode to image
        images = self.decode_latent(latent)
        
        return images
```

#### 4. Training Pipeline

```python
class SGDMTrainer:
    """
    Training pipeline for SGDM
    """
    def __init__(self, model, lr=1e-4, device='cuda'):
        self.model = model.to(device)
        self.optimizer = torch.optim.AdamW(model.parameters(), lr=lr)
        self.device = device
        
    def train_epoch(self, dataloader):
        """
        Train for one epoch
        
        Args:
            dataloader: Yields (eeg, image, label) tuples
        """
        self.model.train()
        total_loss = 0
        
        for batch_idx, (eeg, image, _) in enumerate(dataloader):
            eeg = eeg.to(self.device)
            image = image.to(self.device)
            
            # Extract semantic features
            sem_features = []
            for img in image:
                img_pil = to_pil_image(img.cpu())
                feat = self.model.semantic_extractor.extract_image_features(img_pil)
                sem_features.append(feat)
            sem_features = torch.cat(sem_features, dim=0).to(self.device)
            
            # Forward
            loss = self.model(eeg, image, sem_features)
            
            # Backward
            self.optimizer.zero_grad()
            loss.backward()
            torch.nn.utils.clip_grad_norm_(self.model.parameters(), 1.0)
            self.optimizer.step()
            
            total_loss += loss.item()
            
            if batch_idx % 100 == 0:
                print(f"Batch {batch_idx}, Loss: {loss.item():.4f}")
        
        return total_loss / len(dataloader)
    
    def evaluate(self, dataloader):
        """Evaluate reconstruction quality"""
        self.model.eval()
        
        metrics = {'mse': 0, 'ssim': 0, 'lpips': 0}
        
        with torch.no_grad():
            for eeg, image, _ in dataloader:
                eeg = eeg.to(self.device)
                image = image.to(self.device)
                
                # Reconstruct
                recon = self.model.reconstruct(eeg)
                
                # Compute metrics
                metrics['mse'] += nn.functional.mse_loss(recon, image).item()
                # Add SSIM, LPIPS computation here
        
        for k in metrics:
            metrics[k] /= len(dataloader)
        
        return metrics
```

## Applications

1. **Visual BCI**: Thought-to-image brain-computer interfaces
2. **Dream Visualization**: Reconstruct perceived imagery from EEG
3. **Neuroscience Research**: Understanding visual representation in brain
4. **Memory Reconstruction**: Visualize remembered visual content
5. **Communication Aid**: Help locked-in patients communicate visual thoughts

## Key Results

- Superior reconstruction quality compared to GAN/VAE baselines
- Semantic consistency with original stimuli
- Handles low-density EEG montages
- Cross-subject generalization capabilities

## Pitfalls

1. **Training Data**: Requires paired EEG-image datasets (e.g., THINGS-EEG2)
2. **Computational Cost**: Diffusion models are slow for real-time use
3. **Subject Variability**: Cross-subject performance degrades
4. **Semantic Ambiguity**: Multiple images can produce similar EEG patterns
5. **Overfitting Risk**: Models may memorize training stimuli

## Related Skills
- eeg2vision-multimodal-eeg-framework-2d-visual
- eeg-visual-attention-decoding
- eeg-hopfield-emotion-energy

## References
```
Wang, Y., et al. (2026). Structure-Guided Diffusion Model for EEG-Based 
Visual Cognition Reconstruction. 
arXiv preprint arXiv:2604.22649v1.
```
