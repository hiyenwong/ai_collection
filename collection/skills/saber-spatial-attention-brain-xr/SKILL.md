---
name: saber-spatial-attention-brain-xr
description: "SABER framework integrating spatial attention neuroscience with extended reality (XR) for brain-aware XR interface design. Uses EEG-based spatial attention monitoring to adapt XR environments in real-time. Activation: spatial attention, XR, extended reality, EEG attention, brain-computer interface, adaptive interface, attention-aware, neuroadaptive, VR, AR."
---

# SABER: Spatial Attention Brain-Extended Reality Framework

> Integrates EEG-measured spatial attention with extended reality (XR) systems to create brain-adaptive interfaces that respond to users' attentional state in real-time, improving XR usability and cognitive load management.

## Metadata
- **Source**: arXiv:2603.24830
- **Authors**: Research team (see paper for full author list)
- **Published**: 2026-03-25

## Core Methodology

### Key Innovation
SABER bridges **computational neuroscience of spatial attention** with **extended reality (XR) interface design** by creating a closed-loop system: EEG measures the user's spatial attention distribution, a decoder maps attention to 3D spatial regions in the XR environment, and the interface adapts content rendering and interaction parameters based on the decoded attentional state. This creates neuroadaptive XR that reduces cognitive load and improves task performance.

### Problem Addressed
- XR interfaces present overwhelming visual information, causing cognitive overload
- Current XR systems are attention-blind — they don't know where users are focusing
- Spatial attention in XR involves 3D depth, peripheral vision, and dynamic scene changes
- EEG-based attention decoding has been limited to 2D screens; 3D/XR extension is non-trivial
- No integrated framework connects neuroscience attention models with XR rendering pipelines

### Technical Framework
1. **EEG spatial attention decoder**: Train classifiers on EEG signals during spatial attention tasks in XR
2. **3D attention mapping**: Map decoded attention to 3D spatial coordinates in the XR scene
3. **Closed-loop adaptation**: Adjust XR rendering (LOD, highlight, de-clutter) based on attention
4. **Cognitive load estimation**: Derive workload metrics from attention dynamics over time
5. **Real-time pipeline**: Sub-100ms latency from EEG acquisition to XR adaptation

## Implementation Guide

### Prerequisites
- XR headset with integrated or compatible EEG (e.g., Meta Quest + OpenBCI)
- Python: `torch`, `mne`, `numpy`, `scipy`
- XR development SDK (Unity/Unreal with Python bridge or OpenXR)
- EEG spatial attention dataset (training data with labeled attention regions)

### Step-by-Step
1. **Calibrate EEG decoder**: Collect training data with known spatial attention targets in XR
2. **Train attention classifier**: Use CSP (Common Spatial Patterns) + SVM or deep learning on EEG bands (alpha, theta)
3. **Integrate with XR pipeline**: Connect EEG decoder output to XR rendering engine via network socket or shared memory
4. **Implement adaptation rules**: Define how XR content changes with attention state (e.g., highlight attended, dim unattended)
5. **Real-time validation**: Measure latency, accuracy, and user experience improvement

### Code Example
```python
import numpy as np
import torch
import torch.nn as nn
from scipy.signal import welch

class SpatialAttentionDecoder(nn.Module):
    """Decode spatial attention direction from EEG signals for XR."""
    
    def __init__(self, n_channels=32, n_freq_bands=5, n_spatial_regions=8):
        super().__init__()
        # Input: [batch, channels, frequency_bands, time_windows]
        self.conv = nn.Sequential(
            nn.Conv2d(n_channels, 64, kernel_size=(3, 3), padding=1),
            nn.BatchNorm2d(64),
            nn.ReLU(),
            nn.Dropout(0.3),
            nn.Conv2d(64, 32, kernel_size=(3, 3), padding=1),
            nn.BatchNorm2d(32),
            nn.ReLU(),
        )
        self.attention_head = nn.Sequential(
            nn.Linear(32 * n_freq_bands * 4, 128),  # adjust time_window dim
            nn.ReLU(),
            nn.Dropout(0.4),
            nn.Linear(128, n_spatial_regions),
            nn.Softmax(dim=-1)
        )
        self.load_head = nn.Sequential(
            nn.Linear(32 * n_freq_bands * 4, 64),
            nn.ReLU(),
            nn.Linear(64, 1),
            nn.Sigmoid()
        )
    
    def forward(self, x):
        features = self.conv(x)
        features = features.view(features.size(0), -1)
        attention_map = self.attention_head(features)  # spatial attention distribution
        cognitive_load = self.load_head(features)       # workload estimate
        return attention_map, cognitive_load

def extract_spatial_features(eeg_data, sfreq=256):
    """Extract frequency band power features for spatial attention decoding.
    
    Args:
        eeg_data: [n_trials, n_channels, n_samples]
        sfreq: sampling frequency
    Returns:
        features: [n_trials, n_channels, n_freq_bands]
    """
    bands = {
        'theta': (4, 8),
        'alpha': (8, 13),
        'beta': (13, 30),
        'gamma': (30, 45),
        'low_gamma': (30, 40)
    }
    
    n_trials, n_channels, n_samples = eeg_data.shape
    features = np.zeros((n_trials, n_channels, len(bands)))
    
    for i, (band_name, (low, high)) in enumerate(bands.items()):
        freqs, psd = welch(eeg_data, fs=sfreq, nperseg=min(256, n_samples))
        band_mask = (freqs >= low) & (freqs <= high)
        features[:, :, i] = psd[:, :, band_mask].mean(axis=-1)
    
    return features

class SABERAdapter:
    """XR adaptation engine based on decoded spatial attention."""
    
    def __init__(self, decoder, n_regions=8):
        self.decoder = decoder
        self.n_regions = n_regions
        self.attention_history = []
        self.adaptation_threshold = 0.6
    
    def adapt_xr_scene(self, eeg_window, scene_objects):
        """Adapt XR scene based on decoded attention.
        
        Args:
            eeg_window: recent EEG data [1, channels, freq_bands, time]
            scene_objects: list of {id, region, priority, current_lod}
        Returns:
            adapted_objects: list with updated rendering parameters
        """
        with torch.no_grad():
            attention_map, load = self.decoder(eeg_window)
        
        self.attention_history.append(attention_map.cpu().numpy())
        attended_region = attention_map.argmax(dim=-1).item()
        load_value = load.item()
        
        adapted = []
        for obj in scene_objects:
            adaptation = obj.copy()
            if obj['region'] == attended_region:
                # Attended region: high detail, full color
                adaptation['lod'] = 'high'
                adaptation['opacity'] = 1.0
                adaptation['highlight'] = True
            else:
                # Non-attended: reduce detail based on cognitive load
                adaptation['lod'] = 'medium' if load_value < 0.7 else 'low'
                adaptation['opacity'] = 0.7 if load_value < 0.7 else 0.4
                adaptation['highlight'] = False
            adapted.append(adaptation)
        
        return adapted, load_value
```

## Applications
- **Neuroadaptive XR**: VR/AR systems that respond to user attention in real-time
- **Training simulators**: Adaptive difficulty and content based on cognitive load
- **Accessibility**: Attention-aware interfaces for users with attention disorders
- **Neuroscience research**: Tool for studying spatial attention in immersive 3D environments
- **Surgical XR**: Reduce cognitive overload during image-guided surgery

## Pitfalls
- EEG-to-3D attention mapping accuracy is limited (~60-75% for multi-region)
- Real-time latency constraints are strict (<100ms for seamless adaptation)
- Individual calibration required — inter-subject generalization is poor
- Motion artifacts in VR headsets degrade EEG signal quality
- Over-adaptation can be disorienting — need smooth transitions

## Related Skills
- eeg-visual-attention-decoding
- bci-rehabilitation-protocols
- perception-neuroscience-framework-sensorless-gaze
- neuromimetic-perceptual-compression
