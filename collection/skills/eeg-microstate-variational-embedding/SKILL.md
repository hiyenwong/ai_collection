---
name: eeg-microstate-variational-embedding
description: "EEG Microstate Discovery via Variational Deep Embedding — unsupervised discovery of EEG microstates using variational autoencoder-based deep embedding. Use when: discovering EEG microstates, unsupervised EEG analysis, variational deep embedding for brain signals, temporal segmentation of EEG, microstate-based biomarker discovery. Based on arXiv:2605.10947 (2026). Trigger: EEG microstate discovery, variational EEG embedding, microstate analysis, EEG temporal segmentation, deep embedding EEG"
---

# EEG Microstate Discovery via Variational Deep Embedding

## Overview

Unsupervised discovery of EEG microstates using variational deep embedding methods. Replaces traditional k-means clustering with deep representation learning for more robust microstate identification.

Based on: arXiv:2605.10947 (2026) "EEG Microstate Discovery via Variational Deep Embedding"

## Background

### EEG Microstates

- Brief (~60-120ms) quasi-stable topographical patterns in EEG
- Typically 4-6 canonical microstate classes (A, B, C, D, E, F)
- Represent fundamental building blocks of spontaneous brain activity
- Traditional discovery: k-means on GFP-peaked scalp maps

### Limitations of Traditional Methods

- K-means assumes spherical clusters — EEG microstates are nonlinearly distributed
- Sensitive to noise and preprocessing choices
- Requires fixed number of clusters a priori

## Methodology

### Variational Deep Embedding

1. **Encoder**: Maps scalp topographies to latent distribution q(z|x)
2. **Latent space**: Continuous representation where microstates form distinct clusters
3. **Decoder**: Reconstructs scalp maps from latent codes
4. **Clustering**: Apply clustering (GMM, spectral) in learned latent space

### Architecture

```python
class MicrostateVAE(nn.Module):
    def __init__(self, n_channels=64, latent_dim=8):
        super().__init__()
        self.encoder = nn.Sequential(
            nn.Linear(n_channels, 128),
            nn.ReLU(),
            nn.Linear(128, 64),
            nn.ReLU()
        )
        self.fc_mu = nn.Linear(64, latent_dim)
        self.fc_logvar = nn.Linear(64, latent_dim)
        self.decoder = nn.Sequential(
            nn.Linear(latent_dim, 64),
            nn.ReLU(),
            nn.Linear(64, n_channels)
        )
    
    def forward(self, x):
        h = self.encoder(x)
        mu, logvar = self.fc_mu(h), self.fc_logvar(h)
        z = self.reparameterize(mu, logvar)
        return self.decoder(z), mu, logvar
```

### Temporal Dynamics

- VAE trained on GFP-peaked scalp maps
- Temporal smoothing via HMM on latent codes
- Microstate sequences analyzed for clinical biomarkers

## Advantages

1. **Nonlinear clustering**: Captures complex microstate structure
2. **Probabilistic**: Soft assignment to microstate classes
3. **Robust**: Less sensitive to noise and outliers
4. **Scalable**: Works with high-density EEG (128-256 channels)

## When to Use

- Microstate analysis for neurological conditions
- Unsupervised EEG biomarker discovery
- Cross-subject microstate comparison
- Clinical applications: schizophrenia, depression, epilepsy

## Resources

- Original paper: arXiv:2605.10947
- Related: eeg-brain-connectivity-bci for EEG analysis methods
