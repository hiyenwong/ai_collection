---
name: bandroutenet-eeg-artifact-removal
description: "Adaptive frequency-aware neural network for EEG artifact removal using band-specific processing and routing mechanisms. Activation triggers: EEG denoising, artifact removal, BandRouteNet, EOG removal, EMG removal."
---

# BandRouteNet: Adaptive Band Routing Neural Network for EEG Artifact Removal

> BandRouteNet introduces a novel adaptive frequency-aware neural network architecture that jointly exploits band-specific processing and full-band contextual modeling for effective EEG denoising.

## Metadata
- **Source**: arXiv:2604.24428v1
- **Authors**: Phat Lam
- **Published**: 2026-04-27
- **Category**: Neuroscience, Signal Processing, Deep Learning

## Core Methodology

### Problem Statement
EEG signals are highly susceptible to contamination from:
- **Electrooculographic (EOG)** artifacts (eye movements, blinks)
- **Electromyographic (EMG)** artifacts (muscle activity)
- Mixed artifact conditions with diverse, temporally varying distributions
- Distinct spectral characteristics across frequency bands

Traditional denoising methods struggle because artifact patterns are frequency-dependent and time-varying.

### Key Innovation
BandRouteNet combines:
1. **Band-wise denoising** - explicitly captures frequency-dependent artifact patterns
2. **Adaptive routing mechanism** - determines where and to what extent denoising should be applied across temporal locations within each frequency band
3. **Full-band conditioner** - extracts global temporal context from original noisy EEG

### Architecture

```
Noisy EEG Input
     ↓
┌─────────────────────────────────────┐
│      Full-Band Conditioner          │
│  - Extracts global temporal context │
│  - Produces conditional parameters  │
│  - Provides coarse signal refinement│
└──────────────────┬──────────────────┘
                   ↓
     ┌─────────────┼─────────────┐
     ↓             ↓             ↓
[Delta Band]  [Theta Band]  [Alpha Band]  ... (Band-wise Pathways)
     ↓             ↓             ↓
[Band-specific Denoising + Adaptive Routing]
     ↓             ↓             ↓
     └─────────────┴─────────────┘
                   ↓
          [Signal Reconstruction]
                   ↓
          Clean EEG Output
```

### Technical Components

**1. Band-wise Processing Pathway**
- Decomposes EEG into multiple frequency bands (delta, theta, alpha, beta, gamma)
- Each band processed independently to capture band-specific artifact patterns
- Adaptive routing determines temporal locations requiring denoising

**2. Adaptive Routing Mechanism**
- Learns to identify artifact-contaminated time segments
- Dynamically controls denoising intensity per band and time point
- Reduces over-denoising of clean signal regions

**3. Full-Band Conditioner**
- Processes original multi-band EEG signal
- Extracts global temporal dependencies
- Generates conditioning parameters for band-wise pathways
- Provides coarse-grained signal-level refinement

**4. Multi-scale Fusion**
- Combines band-specific outputs with global context
- Preserves frequency-specific features while maintaining temporal coherence

## Implementation Guide

### Prerequisites
```python
# Core dependencies
torch >= 2.0
numpy
scipy
mne  # For EEG preprocessing
```

### Architecture Implementation

```python
import torch
import torch.nn as nn
import torch.nn.functional as F

class AdaptiveBandRouter(nn.Module):
    """
    Adaptive routing mechanism for band-specific denoising.
    Determines where and how much to denoise within each frequency band.
    """
    def __init__(self, channels, temporal_dim):
        super().__init__()
        self.routing_net = nn.Sequential(
            nn.Conv1d(channels, channels//2, kernel_size=3, padding=1),
            nn.ReLU(),
            nn.Conv1d(channels//2, channels//4, kernel_size=3, padding=1),
            nn.ReLU(),
            nn.Conv1d(channels//4, 1, kernel_size=1),
            nn.Sigmoid()  # Routing weights [0, 1]
        )
    
    def forward(self, x):
        # x: [batch, channels, time]
        routing_weights = self.routing_net(x)  # [batch, 1, time]
        return routing_weights


class BandWiseDenoiser(nn.Module):
    """
    Band-specific denoising module with adaptive routing.
    """
    def __init__(self, in_channels, hidden_channels):
        super().__init__()
        self.feature_extractor = nn.Sequential(
            nn.Conv1d(in_channels, hidden_channels, kernel_size=5, padding=2),
            nn.BatchNorm1d(hidden_channels),
            nn.ReLU(),
            nn.Conv1d(hidden_channels, hidden_channels, kernel_size=3, padding=1),
            nn.BatchNorm1d(hidden_channels),
            nn.ReLU()
        )
        self.router = AdaptiveBandRouter(hidden_channels, temporal_dim=None)
        self.denoising_head = nn.Conv1d(hidden_channels, in_channels, kernel_size=3, padding=1)
    
    def forward(self, x):
        features = self.feature_extractor(x)
        routing_weights = self.router(features)
        denoised = self.denoising_head(features)
        # Apply adaptive routing: weighted combination of denoised and original
        output = routing_weights * denoised + (1 - routing_weights) * x
        return output


class FullBandConditioner(nn.Module):
    """
    Extracts global temporal context from full-band EEG.
    Generates conditioning parameters for band-wise pathways.
    """
    def __init__(self, in_channels, cond_dim):
        super().__init__()
        self.encoder = nn.Sequential(
            nn.Conv1d(in_channels, 64, kernel_size=7, padding=3),
            nn.ReLU(),
            nn.MaxPool1d(2),
            nn.Conv1d(64, 128, kernel_size=5, padding=2),
            nn.ReLU(),
            nn.MaxPool1d(2),
            nn.Conv1d(128, cond_dim, kernel_size=3, padding=1),
            nn.AdaptiveAvgPool1d(1)
        )
        
    def forward(self, x):
        # Returns global conditioning vector
        return self.encoder(x).squeeze(-1)  # [batch, cond_dim]


class BandRouteNet(nn.Module):
    """
    Complete BandRouteNet architecture for EEG artifact removal.
    """
    def __init__(self, n_bands=5, channels_per_band=4, cond_dim=256):
        super().__init__()
        self.n_bands = n_bands
        
        # Band-wise denoisers
        self.band_denoisers = nn.ModuleList([
            BandWiseDenoiser(channels_per_band, hidden_channels=32)
            for _ in range(n_bands)
        ])
        
        # Full-band conditioner
        self.conditioner = FullBandConditioner(
            in_channels=n_bands * channels_per_band,
            cond_dim=cond_dim
        )
        
        # Conditioning projection for each band
        self.cond_projectors = nn.ModuleList([
            nn.Linear(cond_dim, 32) for _ in range(n_bands)
        ])
        
        # Final reconstruction
        self.reconstruction = nn.Sequential(
            nn.Conv1d(n_bands * channels_per_band, 64, kernel_size=3, padding=1),
            nn.ReLU(),
            nn.Conv1d(64, n_bands * channels_per_band, kernel_size=1)
        )
    
    def forward(self, x_bands):
        """
        Args:
            x_bands: List of tensors, each [batch, channels_per_band, time]
        Returns:
            denoised_bands: List of denoised band signals
        """
        # Concatenate for conditioner
        x_full = torch.cat(x_bands, dim=1)  # [batch, n_bands*channels, time]
        
        # Get global conditioning
        cond = self.conditioner(x_full)  # [batch, cond_dim]
        
        # Process each band with conditioning
        denoised_bands = []
        for i, (denoiser, proj) in enumerate(zip(self.band_denoisers, self.cond_projectors)):
            # Apply conditioning to band features
            band_cond = proj(cond)  # [batch, 32]
            
            # Denoise with band-specific processing
            denoised = denoiser(x_bands[i])
            denoised_bands.append(denoised)
        
        # Reconstruct with global refinement
        combined = torch.cat(denoised_bands, dim=1)
        refined = self.reconstruction(combined)
        
        # Residual connection
        output = refined + x_full
        
        # Split back into bands
        output_bands = torch.chunk(output, self.n_bands, dim=1)
        return output_bands
```

### Preprocessing Pipeline

```python
import numpy as np
from scipy import signal

def decompose_eeg_bands(eeg_signal, fs=256):
    """
    Decompose EEG into frequency bands.
    
    Args:
        eeg_signal: [channels, time] EEG data
        fs: Sampling frequency
    
    Returns:
        bands: Dict of band_name -> band_signal
    """
    bands = {}
    
    # Define frequency bands (Hz)
    band_ranges = {
        'delta': (0.5, 4),
        'theta': (4, 8),
        'alpha': (8, 13),
        'beta': (13, 30),
        'gamma': (30, 100)
    }
    
    for band_name, (low, high) in band_ranges.items():
        # Design bandpass filter
        nyquist = fs / 2
        low_norm = low / nyquist
        high_norm = high / nyquist
        b, a = signal.butter(4, [low_norm, high_norm], btype='band')
        
        # Apply filter
        filtered = signal.filtfilt(b, a, eeg_signal, axis=-1)
        bands[band_name] = filtered
    
    return bands
```

### Training

```python
def train_bandroutenet(model, train_loader, epochs=100, lr=1e-3):
    optimizer = torch.optim.Adam(model.parameters(), lr=lr)
    criterion = nn.MSELoss()
    
    for epoch in range(epochs):
        model.train()
        total_loss = 0
        
        for noisy_bands, clean_bands in train_loader:
            optimizer.zero_grad()
            
            # Forward pass
            denoised_bands = model(noisy_bands)
            
            # Compute loss across all bands
            loss = sum(criterion(d, c) for d, c in zip(denoised_bands, clean_bands))
            
            # Backward pass
            loss.backward()
            optimizer.step()
            
            total_loss += loss.item()
        
        print(f"Epoch {epoch+1}/{epochs}, Loss: {total_loss/len(train_loader):.4f}")
```

## Applications

1. **Neurological Diagnosis** - Clean EEG for epilepsy detection, sleep staging
2. **Brain-Computer Interfaces** - Artifact-free signals for BCI control
3. **Cognitive Neuroscience** - High-quality data for ERP studies
4. **Clinical Monitoring** - Continuous EEG in ICU settings
5. **Mobile EEG** - Real-time denoising for wearable devices

## Key Metrics

- **Model Size**: Only 0.2M trainable parameters (highly parameter-efficient)
- **Performance**: Outperforms existing methods on EEGDenoiseNet benchmark
- **Artifacts**: Handles EOG, EMG, and mixed artifacts
- **Metrics**: Optimized for RRMSE and SNR improvement

## Pitfalls

1. **Band Selection** - Frequency bands may need adjustment for specific applications
2. **Training Data** - Requires paired clean/noisy EEG data for supervision
3. **Computational Cost** - Multiple band pathways increase inference time
4. **Artifact Types** - May not generalize to uncommon artifact types not in training
5. **Channel Count** - Architecture assumes fixed number of input channels

## Related Skills

- eeg-structure-guided-diffusion - EEG-based visual reconstruction
- eeg-tinnitus-biomarker-robustness - EEG biomarker analysis
- eeg-foundation-model-adapters - EEG foundation models

## References

```bibtex
@article{lam2026bandroutenet,
  title={BandRouteNet: An Adaptive Band Routing Neural Network for EEG Artifact Removal},
  author={Lam, Phat},
  journal={arXiv preprint arXiv:2604.24428},
  year={2026}
}
```
