---
name: brain-inspired-capture-visual-decoding
description: Neuromimetic perceptual simulation paradigm for visual decoding from neurophysiological signals. Emulates Human Visual System (HVS) processing with dynamic transformations and MI-guided blur regulation for brain-to-image retrieval.
version: 1.0.0
author: Research Synthesis
license: MIT
metadata:
  hermes:
    tags: [brain-decoding, visual-decoding, BCI, neuromimetic, HVS, brain-to-image, zero-shot-retrieval]
    source_paper: "Brain-Inspired Capture: Evidence-Driven Neuromimetic Perceptual Simulation for Visual Decoding (arXiv:2604.17927)"
    authors: "Feixue Shao, Guangze Shi, Xueyu Liu et al."
    published: "2026-04-20"
---

# Brain-Inspired Capture (BI-Cap) for Visual Decoding

## Overview

BI-Cap addresses the systematic and stochastic gaps between neural and visual modalities by emulating Human Visual System (HVS) processing. It constructs a neuromimetic pipeline with biologically plausible transformations and introduces evidence-driven latent space representations to handle neural activity non-stationarity.

## Core Concepts

### Neuromimetic Pipeline

Four biologically plausible transformations that simulate HVS processing:

1. **Dynamic Transformation**: Time-varying neural signal processing
2. **Static Transformation**: Spatial feature extraction mimicking V1-V4 hierarchy
3. **Adaptive Processing**: MI-guided dynamic blur regulation
4. **Uncertainty Modeling**: Evidence-driven latent representation

### Mutual Information-Guided Dynamic Blur Regulation

```python
import numpy as np
from scipy.ndimage import gaussian_filter

def compute_mutual_information(x, y, n_bins=32):
    """Estimate mutual information using histogram-based method."""
    hist_xy, _, _ = np.histogram2d(x, y, bins=n_bins)
    prob_xy = hist_xy / np.sum(hist_xy)
    prob_x = np.sum(prob_xy, axis=1)
    prob_y = np.sum(prob_xy, axis=0)
    
    mi = 0
    for i in range(n_bins):
        for j in range(n_bins):
            if prob_xy[i, j] > 0:
                mi += prob_xy[i, j] * np.log(prob_xy[i, j] / (prob_x[i] * prob_y[j] + 1e-10) + 1e-10)
    return mi

def mi_guided_blur_regulation(neural_features, visual_features):
    """
    Regulate blur dynamically based on mutual information between
    neural and visual features, simulating adaptive visual processing.
    """
    mi = compute_mutual_information(neural_features.flatten(), visual_features.flatten())
    
    # Higher MI -> sharper (less blur), lower MI -> more blur
    blur_sigma = max(0.1, 5.0 - mi * 2.0)
    
    return gaussian_filter(visual_features, sigma=blur_sigma)
```

### Evidence-Driven Latent Space

```python
class EvidenceDrivenLatentSpace:
    """
    Models uncertainty in neural activity to ensure robust embeddings.
    """
    
    def __init__(self, latent_dim=256):
        self.latent_dim = latent_dim
        
    def encode(self, neural_data):
        """
        Encode neural data into latent space with uncertainty modeling.
        Uses evidence-based weighting for robustness.
        """
        # Compute evidence (reliability) from neural data
        evidence = self._compute_evidence(neural_data)
        
        # Weighted encoding
        weighted_data = neural_data * evidence
        
        # Project to latent space
        latent = self._project(weighted_data)
        
        return latent, evidence
    
    def _compute_evidence(self, data):
        """Compute evidence/reliability from signal-to-noise ratio."""
        signal_power = np.mean(data ** 2, axis=0)
        noise_power = np.var(data, axis=0)
        snr = signal_power / (noise_power + 1e-10)
        
        # Sigmoid mapping to [0, 1]
        evidence = 1.0 / (1.0 + np.exp(-snr))
        return evidence
    
    def _project(self, data):
        """Linear projection to latent space."""
        # PCA or learned projection
        from sklearn.decomposition import PCA
        pca = PCA(n_components=self.latent_dim)
        return pca.fit_transform(data)
```

## Key Results

- **Zero-shot brain-to-image retrieval** across two public benchmarks
- **Relative gains**: 9.2% and 8.0% over state-of-the-art methods
- **Code released**: https://github.com/flysnow1024/BI-Cap

## Applications

- Brain-computer interfaces for visual communication
- Neural prosthetics for visual restoration
- Cognitive neuroscience research
- Neurological disorder assessment

## References

- Brain-Inspired Capture: Evidence-Driven Neuromimetic Perceptual Simulation for Visual Decoding
- Authors: Feixue Shao, Guangze Shi, Xueyu Liu et al.
- arXiv: 2604.17927
- Published: 2026-04-20
- Categories: cs.CV, cs.AI

## Related Skills
- [[eeg2vision-multimodal-eeg-framework-2d-visual]]
- [[meta-learning-in-context-brain-decoding-v4]]
- [[brain-dit-fmri-foundation-model-v4]]
