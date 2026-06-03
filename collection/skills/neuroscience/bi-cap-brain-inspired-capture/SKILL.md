---
name: bi-cap-brain-inspired-capture
description: "Brain-Inspired Capture (BI-Cap) — neuromimetic perceptual simulation for visual decoding from neural signals. Emulates Human Visual System processing with dynamic/static transformations and MI-guided blur regulation. Evidence-driven latent space handles neural non-stationarity. Activation: bi-cap, brain inspired capture, visual decoding, neural visual reconstruction, neuromimetic simulation, brain-to-image"
tags: ["brain-decoding", "visual-reconstruction", "neuromimetic", "BCI", "fMRI", "EEG"]
related_skills: ["eeg-structure-guided-diffusion-v4", "brain-dit-fmri-foundation-model", "sgdm-eeg-visual-cognition"]
---

# Brain-Inspired Capture (BI-Cap): Neuromimetic Visual Decoding

Based on arXiv:2604.17927 (April 20, 2026) — "Brain-Inspired Capture: Evidence-Driven Neuromimetic Perceptual Simulation for Visual Decoding"

## Overview

BI-Cap addresses the systematic and stochastic gaps between neural and visual modalities by emulating the **Human Visual System (HVS)** processing pipeline. It constructs a neuromimetic pipeline with biologically plausible transformations and an evidence-driven latent space that explicitly models uncertainty.

## Key Innovations

### 1. Neuromimetic Pipeline
Four biologically plausible transformations emulating HVS:
1. **Retinal Preprocessing** — photoreceptor response simulation
2. **LGN Filtering** — center-surround receptive field modeling
3. **V1 Feature Extraction** — oriented edge detection (Gabor-like)
4. **Higher-Visual Processing** — invariant representation formation

### 2. MI-Guided Dynamic Blur Regulation
- Uses **Mutual Information (MI)** between neural and visual features to adaptively regulate blur
- Simulates adaptive visual processing (foveal vs. peripheral acuity)
- Dynamically adjusts receptive field sizes based on neural evidence strength

### 3. Evidence-Driven Latent Space
- Explicitly models **uncertainty** in neural activity
- Non-stationarity-aware embeddings
- Robust neural-to-visual alignment under noise

## Results

| Benchmark | Previous SOTA | BI-Cap | Relative Gain |
|-----------|--------------|--------|---------------|
| Zero-shot brain-to-image retrieval (Benchmark 1) | Baseline | +9.2% | **9.2% improvement** |
| Zero-shot brain-to-image retrieval (Benchmark 2) | Baseline | +8.0% | **8.0% improvement** |

## Architecture

```
Neural Signal → [Evidence Encoder] → Uncertainty-aware Embedding
                                              ↓
Visual Image → [HVS Neuromimetic Pipeline] → Processed Visual Features
                                              ↓
                    [MI-Guided Alignment Module]
                                              ↓
                        [Shared Latent Space]
```

### Neuromimetic Transformations

```python
import torch
import torch.nn as nn
import torch.nn.functional as F
from scipy.ndimage import gaussian_filter


class RetinalPreprocessing(nn.Module):
    """Simulates photoreceptor response and retinal processing."""
    def __init__(self, n_channels=3):
        super().__init__()
        # Nonlinear photoreceptor response (Naka-Rushton)
        self.naka_rushton_n = 2.0
        self.naka_rushton_sigma = 0.5

    def forward(self, x):
        """
        Naka-Rushton response: R = R_max * I^n / (I^n + sigma^n)
        """
        x_norm = x.clamp(0, 1)
        response = x_norm ** self.naka_rushton_n / \
                   (x_norm ** self.naka_rushton_n + self.naka_rushton_sigma ** self.naka_rushton_n)
        return response


class LGNFiltering(nn.Module):
    """Center-surround receptive field modeling (DoG filter)."""
    def __init__(self, center_sigma=1.0, surround_sigma=3.0, center_weight=1.0, surround_weight=0.6):
        super().__init__()
        self.center_sigma = center_sigma
        self.surround_sigma = surround_sigma
        self.center_weight = center_weight
        self.surround_weight = surround_weight

    def forward(self, x):
        """
        Difference-of-Gaussians: DoG = center - surround
        """
        center = gaussian_filter(x.cpu().numpy(), sigma=self.center_sigma)
        surround = gaussian_filter(x.cpu().numpy(), sigma=self.surround_sigma)
        dog = self.center_weight * center - self.surround_weight * surround
        return torch.tensor(dog, device=x.device, dtype=x.dtype)


class GaborFeatureExtractor(nn.Module):
    """V1-like oriented edge detection using Gabor filters."""
    def __init__(self, n_orientations=8, kernel_size=15):
        super().__init__()
        self.n_orientations = n_orientations
        self.gabor_filters = self._create_gabor_bank(kernel_size, n_orientations)

    def _create_gabor_bank(self, size, n_orientations):
        """Create bank of Gabor filters at different orientations."""
        filters = []
        for theta in np.linspace(0, np.pi, n_orientations, endpoint=False):
            kernel = self._gabor_kernel(size, theta=theta)
            filters.append(kernel)
        return torch.tensor(np.stack(filters), dtype=torch.float32)

    def _gabor_kernel(self, size, theta=0, sigma=3.0, lambd=10.0, gamma=0.5):
        """Create a single Gabor kernel."""
        # Standard Gabor filter
        ...  # implementation omitted for brevity

    def forward(self, x):
        """Apply Gabor filter bank."""
        # Convolve with each orientation
        features = []
        for f in self.gabor_filters:
            response = F.conv2d(x, f.unsqueeze(0).unsqueeze(0), padding='same')
            features.append(response)
        return torch.cat(features, dim=1)


class MIBlurRegulator(nn.Module):
    """Mutual Information-guided dynamic blur regulation."""
    def __init__(self, min_blur=0.5, max_blur=5.0):
        super().__init__()
        self.min_blur = min_blur
        self.max_blur = max_blur

    def estimate_mi(self, neural_feat, visual_feat):
        """Estimate mutual information between neural and visual features."""
        # KL-divergence based MI estimation
        # MI = KL(p(neural, visual) || p(neural)p(visual))
        joint = torch.cat([neural_feat, visual_feat], dim=-1)
        # Use MINE or other MI estimator
        ...

    def forward(self, visual_feat, neural_feat):
        """
        Adaptively blur visual features based on neural evidence.
        Low MI → more blur (uncertain neural signal)
        High MI → less blur (strong neural evidence)
        """
        mi = self.estimate_mi(neural_feat, visual_feat)
        # Normalize MI to [0, 1]
        mi_norm = (mi - mi.min()) / (mi.max() - mi.min() + 1e-8)
        # Map to blur level (inverse relationship)
        blur_level = self.max_blur - mi_norm * (self.max_blur - self.min_blur)
        # Apply adaptive blur
        ...
        return regulated_features
```

### Evidence-Driven Latent Space

```python
class EvidenceDrivenEncoder(nn.Module):
    """
    Encodes neural signals with explicit uncertainty modeling.
    Handles non-stationarity of neural activity.
    """
    def __init__(self, input_dim, latent_dim):
        super().__init__()
        self.encoder = nn.Sequential(
            nn.Linear(input_dim, 512),
            nn.ReLU(),
            nn.Linear(512, latent_dim * 2)  # mean + log_var
        )

    def forward(self, neural_signal):
        """
        Returns:
            z_mean: [batch, latent_dim] - point estimate
            z_log_var: [batch, latent_dim] - uncertainty (log variance)
        """
        stats = self.encoder(neural_signal)
        z_mean = stats[:, :latent_dim]
        z_log_var = stats[:, latent_dim:]

        # Reparameterization trick
        std = torch.exp(0.5 * z_log_var)
        eps = torch.randn_like(std)
        z = z_mean + eps * std

        return z, z_mean, z_log_var
```

## Training Pipeline

```python
def train_bi_cap(neural_encoder, visual_processor, aligner,
                 neural_data, visual_data, epochs=100):
    """
    Train BI-Cap with MI-guided alignment.
    """
    optimizer = torch.optim.Adam([
        {'params': neural_encoder.parameters()},
        {'params': visual_processor.parameters()},
        {'params': aligner.parameters()},
    ], lr=1e-4)

    for epoch in range(epochs):
        # Forward pass
        z, z_mean, z_log_var = neural_encoder(neural_data)
        v_processed = visual_processor(visual_data)

        # MI-guided alignment
        mi_loss = aligner.compute_mi_loss(z, v_processed)

        # VAE-style reconstruction loss
        kl_loss = -0.5 * torch.sum(1 + z_log_var - z_mean.pow(2) - z_log_var.exp())

        # Total loss
        loss = mi_loss + 0.1 * kl_loss

        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
```

## Applications

1. **Brain-to-Image Retrieval** — given neural activity, retrieve most similar image from database
2. **BCI Visual Decoding** — reconstruct perceived images from fMRI/EEG
3. **Neurofeedback** — real-time visual feedback based on brain state
4. **Cognitive State Monitoring** — decode attention, engagement from neural signals

## Pitfalls

1. **HVS Approximation**: The neuromimetic pipeline is an approximation. Individual differences in visual processing may reduce alignment quality.
2. **MI Estimation**: Mutual information estimation is notoriously difficult in high dimensions. Use MINE (Mutual Information Neural Estimation) or contrastive methods.
3. **Non-Stationarity**: Neural signals drift over time. The evidence-driven latent space helps but may need periodic recalibration.
4. **Benchmark Dependency**: Results may vary across datasets. The paper reports gains on two benchmarks — verify on your data.
5. **Computational Cost**: The neuromimetic pipeline adds computation overhead compared to direct neural-to-visual mapping.

## Verification Steps

1. Verify MI between neural and visual features increases during training
2. Check that uncertainty estimates (z_log_var) correlate with signal quality
3. Compare against direct mapping baseline (without HVS emulation)
4. Validate on held-out subjects (cross-subject generalization)
5. Measure zero-shot retrieval accuracy against SOTA

## References

- Shao, F., Shi, G., Liu, X., Wu, Y., Wei, M., Zhang, J., Lu, J., Yan, G., & Yang, W. (2026). *Brain-Inspired Capture: Evidence-Driven Neuromimetic Perceptual Simulation for Visual Decoding.* arXiv:2604.17927 [cs.CV].
- Code: https://github.com/flysnow1024/BI-Cap