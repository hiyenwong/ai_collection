---
name: eeg-structure-guided-diffusion-v4
description: "Structure-Guided Diffusion Model (SGDM) for EEG-based visual cognition reconstruction. Two-stage generative mechanism combining structurally-supervised VAE with spatiotemporal EEG encoder. Keywords: EEG reconstruction, visual cognition, diffusion model, brain-computer interface"
---

# EEG Structure-Guided Diffusion Model (SGDM) v4

> Two-stage generative framework for decoding visual information from EEG signals by incorporating explicit structural information into the diffusion process.

## Metadata
- **Source**: arXiv:2604.22649v1
- **Authors**: Yongxiang Lian, Yueyang Cang, Pingge Hu, Yuchen He, Li Shi
- **Published**: 2026-04-24

## Core Methodology

### Key Innovation
Traditional EEG-based visual reconstruction methods are restricted to natural images and categorical representations with limited structural feature capture. SGDM introduces explicit structural information into the generative process, enabling differentiation between objective perception and subjective cognition.

### Technical Framework

**Architecture Components:**
1. **Structurally-Supervised Variational Autoencoder (ssVAE)**
   - Encodes structural information into latent space
   - Supervised by geometric/semantic structure labels
   - Provides structural guidance to the diffusion process

2. **Spatiotemporal EEG Encoder**
   - Captures temporal dynamics from EEG signals
   - Aligns neural activity to visual embedding space
   - Handles multi-channel spatiotemporal correlations

3. **Conditional Diffusion Model**
   - Uses structural guidance from ssVAE
   - Conditioned on EEG encoder outputs
   - Two-stage generative mechanism

**Two-Stage Generation:**
- Stage 1: Structure prediction from EEG
- Stage 2: Detail synthesis via diffusion with structural conditioning

## Implementation Guide

### Prerequisites
```bash
pip install torch torchvision diffusers transformers
pip install mne  # For EEG processing
pip install scikit-learn matplotlib
```

### Step-by-Step Implementation

**Step 1: EEG Preprocessing**
```python
import mne
import numpy as np
from scipy import signal

def preprocess_eeg(raw_eeg, sfreq=1000, low_freq=1, high_freq=40):
    """
    Preprocess EEG data for SGDM input.
    
    Args:
        raw_eeg: Raw EEG data (channels x timepoints)
        sfreq: Sampling frequency
        low_freq, high_freq: Bandpass filter range
    
    Returns:
        Preprocessed EEG features (channels x time x freq_bands)
    """
    # Bandpass filter
    filtered = mne.filter.filter_data(
        raw_eeg, sfreq=sfreq, 
        l_freq=low_freq, h_freq=high_freq
    )
    
    # Time-frequency decomposition (e.g., wavelet or STFT)
    # Extract relevant frequency bands
    freq_bands = {
        'delta': (0.5, 4),
        'theta': (4, 8), 
        'alpha': (8, 13),
        'beta': (13, 30),
        'gamma': (30, 40)
    }
    
    features = []
    for band, (low, high) in freq_bands.items():
        band_power = bandpower(filtered, sfreq, low, high)
        features.append(band_power)
    
    return np.stack(features, axis=-1)

def bandpower(data, sfreq, low, high):
    """Compute band power using Welch's method."""
    freqs, psd = signal.welch(data, sfreq, nperseg=256)
    idx = np.logical_and(freqs >= low, freqs <= high)
    return np.mean(psd[:, idx], axis=-1)
```

**Step 2: Spatiotemporal EEG Encoder**
```python
import torch
import torch.nn as nn

class SpatiotemporalEEGEncoder(nn.Module):
    """
    Encodes EEG signals into visual embedding space.
    Captures both spatial (channel) and temporal dynamics.
    """
    def __init__(self, n_channels=64, n_timepoints=1000, 
                 n_freq_bands=5, embed_dim=512):
        super().__init__()
        
        # Spatial attention (channel correlations)
        self.spatial_attn = nn.MultiheadAttention(
            embed_dim=n_freq_bands, num_heads=1, 
            batch_first=True
        )
        
        # Temporal convolution
        self.temporal_conv = nn.Sequential(
            nn.Conv1d(n_channels, 128, kernel_size=3, padding=1),
            nn.ReLU(),
            nn.Conv1d(128, 256, kernel_size=3, padding=1),
            nn.ReLU(),
            nn.AdaptiveAvgPool1d(64)
        )
        
        # Final embedding projection
        self.projection = nn.Sequential(
            nn.Linear(256 * 64, 1024),
            nn.ReLU(),
            nn.Linear(1024, embed_dim)
        )
    
    def forward(self, eeg_input):
        # eeg_input: (batch, channels, time, freq_bands)
        b, c, t, f = eeg_input.shape
        
        # Spatial attention across channels
        eeg_flat = eeg_input.permute(0, 2, 1, 3).reshape(b*t, c, f)
        spatial_out, _ = self.spatial_attn(eeg_flat, eeg_flat, eeg_flat)
        spatial_out = spatial_out.reshape(b, t, c, f).permute(0, 2, 1, 3)
        
        # Average over frequency bands
        temporal_input = spatial_out.mean(dim=-1)  # (b, c, t)
        
        # Temporal convolution
        temporal_out = self.temporal_conv(temporal_input)
        temporal_out = temporal_out.flatten(1)
        
        # Project to visual embedding
        embedding = self.projection(temporal_out)
        return embedding
```

**Step 3: Structurally-Supervised VAE**
```python
class StructurallySupervisedVAE(nn.Module):
    """
    VAE with structural supervision for shape/semantic guidance.
    """
    def __init__(self, input_dim=512, latent_dim=256, 
                 structure_dim=128):
        super().__init__()
        
        # Encoder
        self.encoder = nn.Sequential(
            nn.Linear(input_dim, 512),
            nn.ReLU(),
            nn.Linear(512, 256)
        )
        self.fc_mu = nn.Linear(256, latent_dim)
        self.fc_var = nn.Linear(256, latent_dim)
        
        # Structure prediction head
        self.structure_head = nn.Sequential(
            nn.Linear(latent_dim, 256),
            nn.ReLU(),
            nn.Linear(256, structure_dim)
        )
        
        # Decoder
        self.decoder = nn.Sequential(
            nn.Linear(latent_dim, 256),
            nn.ReLU(),
            nn.Linear(256, 512),
            nn.ReLU(),
            nn.Linear(512, input_dim)
        )
    
    def encode(self, x):
        h = self.encoder(x)
        mu = self.fc_mu(h)
        log_var = self.fc_var(h)
        return mu, log_var
    
    def reparameterize(self, mu, log_var):
        std = torch.exp(0.5 * log_var)
        eps = torch.randn_like(std)
        return mu + eps * std
    
    def decode(self, z):
        return self.decoder(z)
    
    def predict_structure(self, z):
        return self.structure_head(z)
    
    def forward(self, x, structure_labels=None):
        mu, log_var = self.encode(x)
        z = self.reparameterize(mu, log_var)
        reconstruction = self.decode(z)
        structure_pred = self.predict_structure(z)
        
        # Compute losses
        recon_loss = nn.MSELoss()(reconstruction, x)
        kl_loss = -0.5 * torch.sum(1 + log_var - mu.pow(2) - log_var.exp())
        
        if structure_labels is not None:
            structure_loss = nn.MSELoss()(structure_pred, structure_labels)
        else:
            structure_loss = 0
        
        return reconstruction, mu, log_var, structure_loss, recon_loss + kl_loss
```

**Step 4: Structure-Guided Diffusion**
```python
from diffusers import DDPMScheduler, UNet2DConditionModel

class StructureGuidedDiffusion:
    """
    Diffusion model conditioned on EEG embeddings and structure guidance.
    """
    def __init__(self, embed_dim=512, structure_dim=128):
        self.scheduler = DDPMScheduler(num_train_timesteps=1000)
        
        # Conditional UNet
        self.unet = UNet2DConditionModel(
            sample_size=64,
            in_channels=3,
            out_channels=3,
            layers_per_block=2,
            block_out_channels=(128, 256, 512, 512),
            cross_attention_dim=embed_dim + structure_dim,
        )
    
    def forward_diffusion(self, x0, t, noise=None):
        """Add noise to image at timestep t."""
        if noise is None:
            noise = torch.randn_like(x0)
        
        # Get noise schedule
        alpha_t = self.scheduler.alphas_cumprod[t]
        noisy_x = torch.sqrt(alpha_t) * x0 + torch.sqrt(1 - alpha_t) * noise
        return noisy_x, noise
    
    def train_step(self, images, eeg_embeddings, structure_labels):
        """
        Training step for structure-guided diffusion.
        
        Args:
            images: Target images (B, 3, H, W)
            eeg_embeddings: EEG encoder outputs (B, embed_dim)
            structure_labels: Structure guidance (B, structure_dim)
        """
        batch_size = images.shape[0]
        
        # Random timesteps
        timesteps = torch.randint(0, 1000, (batch_size,))
        
        # Add noise
        noisy_images, noise = self.forward_diffusion(images, timesteps)
        
        # Conditioning: concatenate EEG embedding with structure
        conditioning = torch.cat([eeg_embeddings, structure_labels], dim=-1)
        conditioning = conditioning.unsqueeze(1)  # Add sequence dim
        
        # Predict noise
        noise_pred = self.unet(
            noisy_images, 
            timesteps, 
            encoder_hidden_states=conditioning
        ).sample
        
        # MSE loss
        loss = nn.MSELoss()(noise_pred, noise)
        return loss
    
    @torch.no_grad()
    def generate(self, eeg_embedding, structure_label, num_inference_steps=50):
        """
        Generate image from EEG embedding and structure guidance.
        """
        self.scheduler.set_timesteps(num_inference_steps)
        
        # Start from random noise
        image = torch.randn(1, 3, 64, 64)
        
        conditioning = torch.cat([eeg_embedding, structure_label], dim=-1)
        conditioning = conditioning.unsqueeze(1)
        
        for t in self.scheduler.timesteps:
            # Predict noise
            noise_pred = self.unet(image, t, encoder_hidden_states=conditioning).sample
            
            # Denoise step
            image = self.scheduler.step(noise_pred, t, image).prev_sample
        
        return image
```

**Step 5: Full Pipeline**
```python
def train_sgdm(eeg_data, images, structure_labels, epochs=100):
    """
    Train the complete SGDM pipeline.
    """
    # Initialize models
    eeg_encoder = SpatiotemporalEEGEncoder()
    ss_vae = StructurallySupervisedVAE()
    diffusion = StructureGuidedDiffusion()
    
    # Optimizers
    optimizer = torch.optim.Adam(
        list(eeg_encoder.parameters()) + 
        list(ss_vae.parameters()) +
        list(diffusion.unet.parameters()),
        lr=1e-4
    )
    
    for epoch in range(epochs):
        # Stage 1: Train EEG encoder and VAE
        eeg_embeddings = eeg_encoder(eeg_data)
        recon, mu, log_var, struct_loss, vae_loss = ss_vae(
            eeg_embeddings, structure_labels
        )
        
        # Stage 2: Train diffusion with EEG conditioning
        structure_pred = ss_vae.predict_structure(mu)
        diff_loss = diffusion.train_step(images, eeg_embeddings, structure_pred)
        
        # Combined loss
        total_loss = vae_loss + diff_loss + struct_loss
        
        optimizer.zero_grad()
        total_loss.backward()
        optimizer.step()
        
        if epoch % 10 == 0:
            print(f"Epoch {epoch}: Loss = {total_loss.item():.4f}")
    
    return eeg_encoder, ss_vae, diffusion
```

## Applications

### 1. Visual Reconstruction from EEG
```python
# Reconstruct seen/imagined images from EEG
eeg_signal = load_eeg_recording(subject_id, trial_id)
eeg_features = preprocess_eeg(eeg_signal)
eeg_embedding = eeg_encoder(eeg_features)
structure = ss_vae.predict_structure(eeg_embedding)
reconstructed = diffusion.generate(eeg_embedding, structure)
```

### 2. Objective vs Subjective Cognition Differentiation
- **Objective Perception**: Reconstruction from stimulus-locked EEG
- **Subjective Cognition**: Reconstruction from post-stimulus/reminiscence EEG
- Compare structural fidelity between conditions

### 3. Brain-Computer Interface
- Real-time visual reconstruction for communication
- Mental imagery visualization
- Dream/imagery decoding

## Datasets

- **Kilogram**: Abstract visual object dataset with EEG recordings
- **THINGS**: Natural image dataset with EEG

## Pitfalls

1. **Temporal Misalignment**: EEG has poor temporal resolution (~100ms); ensure proper stimulus-locking
2. **Individual Variability**: EEG patterns vary significantly across subjects; consider subject-specific fine-tuning
3. **Structure Label Quality**: Requires accurate structure annotations for supervision
4. **Computational Cost**: Diffusion models are computationally expensive for real-time BCI

## Related Skills

- eeg-structure-guided-diffusion
- eeg-structure-guided-diffusion-v2  
- eeg-structure-guided-diffusion-v3
- eeg2vision-multimodal-eeg-framework-2d-visual
- eeg-hopfield-emotion-energy

## References

```bibtex
@article{lian2026sgdm,
  title={Structure-Guided Diffusion Model for EEG-Based Visual Cognition Reconstruction},
  author={Lian, Yongxiang and Cang, Yueyang and Hu, Pingge and He, Yuchen and Shi, Li},
  journal={arXiv preprint arXiv:2604.22649},
  year={2026}
}
```
