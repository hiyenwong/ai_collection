---
name: eccentricity-confound-eeg-visual-attention
description: "EEG-based visual attention decoding methodology addressing the eccentricity confound in gaze-fixated neural tracking of motion in natural videos. Demonstrates motion-based encoding models capture attention beyond eccentricity effects. Updated: April 2026."
version: 2.0.0
author: Research Synthesis
license: MIT
metadata:
  hermes:
    source_paper: "Eccentricity Confound in EEG-based Visual Attention Decoding (arXiv:2604.15223v1)"
    citations: 0
    tags: [eeg, visual-attention, brain-decoding, eccentricity-confound, neural-tracking]
---

# Eccentricity Confound in EEG Visual Attention Decoding

## Overview

This paper identifies a critical methodological confound in EEG-based visual attention decoding: the eccentricity effect. When subjects attend to different locations in natural videos, varying retinal eccentricity creates neural signal differences that can be mistakenly attributed to attention. Motion-based encoding models capture genuine attention-related neural tracking beyond eccentricity effects.

## Core Problem

- **Eccentricity**: Distance from gaze center affects neural responses
- **Confounding**: Attention signals mixed with eccentricity-driven responses
- **Motion Encoding**: Superior to luminance-based models for natural video viewing

## Implementation

```python
import numpy as np
from sklearn.linear_model import Ridge, LinearRegression

class EccentricityControlledDecoder:
    def __init__(self, n_ecc_bins=5):
        self.n_ecc_bins = n_ecc_bins
    
    def create_eccentricity_controls(self, gaze_positions, video_size):
        center = np.array(video_size) / 2
        distances = np.sqrt(((gaze_positions - center) ** 2).sum(axis=1))
        return np.digitize(distances, np.linspace(0, max(distances), self.n_ecc_bins))
    
    def decode_attention(self, eeg_data, motion_features, ecc_bins):
        # Regress out eccentricity effects
        ecc_model = LinearRegression()
        ecc_model.fit(ecc_bins.reshape(-1, 1), eeg_data)
        eeg_residuals = eeg_data - ecc_model.predict(ecc_bins.reshape(-1, 1))
        decoder = Ridge(alpha=1.0)
        decoder.fit(motion_features, eeg_residuals)
        return decoder
```

## Activation Keywords
- eeg visual attention, eccentricity confound, neural tracking, motion encoding, EEG注意力解码, 偏心度混淆

## References
- arXiv:2604.15223v1 — Yao, Salamanca Gonzalez, Geirnaert