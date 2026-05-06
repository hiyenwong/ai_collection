---
name: braincast-spatiotemporal-fmri-forecasting
description: "BrainCast methodology for spatio-temporal forecasting of whole-brain fMRI time series. Uses dual-branch architecture with ST-CausalConv for spatial decoding and ST-Mixer for temporal prediction. Activation: fMRI forecasting, brain time series prediction, spatio-temporal brain modeling."
---

# BrainCast: Spatio-Temporal Forecasting for Whole-Brain fMRI

> BrainCast is a novel spatio-temporal forecasting framework specifically designed for whole-brain fMRI time series prediction, addressing the challenge of short clinical scan durations.

## Metadata
- **Source**: arXiv:2603.13361v1
- **Authors**: Yunlong Gao, Jinbo Yang, Li Xiao, et al.
- **Published**: 2026-03-09
- **Category**: Computational Neuroscience, fMRI Analysis, Time Series Forecasting

## Core Methodology

### Problem Addressed
Clinical fMRI scans often have short durations due to human factors (patient comfort) and non-human factors (scanner availability), leading to:
- Reduced data quality
- Limited statistical power
- Incomplete brain state characterization

### Key Innovation
BrainCast introduces a **dual-branch architecture** that decouples spatial and temporal processing:

1. **ST-CausalConv Branch**: Captures spatial dependencies through causal convolutions
2. **ST-Mixer Branch**: Models temporal dynamics using MLP-based mixing

### Architecture Components

```
Input: Short fMRI time series (T timesteps × N voxels)
    ↓
┌─────────────────────────────────────────┐
│  Spatial Branch (ST-CausalConv)         │
│  - Causal convolution for spatial       │
│    dependency modeling                  │
│  - Preserves temporal causality         │
└─────────────────────────────────────────┘
                    ↓
┌─────────────────────────────────────────┐
│  Temporal Branch (ST-Mixer)             │
│  - MLP-based mixing across time         │
│  - Captures long-range temporal         │
│    dependencies                         │
└─────────────────────────────────────────┘
                    ↓
         Fusion & Prediction
                    ↓
Output: Extended fMRI time series
```

## Implementation Guide

### Prerequisites
- Python 3.8+
- PyTorch or TensorFlow
- Nilearn or Nibabel for fMRI data handling
- NumPy, SciPy for numerical operations

### Step-by-Step Implementation

#### Step 1: Data Preprocessing
```python
import nibabel as nib
import numpy as np
from nilearn import image

# Load fMRI data
fmri_img = nib.load('brain_fmri.nii.gz')
fmri_data = fmri_img.get_fdata()  # Shape: (X, Y, Z, T)

# Reshape to (voxels, time)
n_voxels = np.prod(fmri_data.shape[:3])
fmri_2d = fmri_data.reshape(n_voxels, -1)  # Shape: (N_voxels, T_timesteps)

# Normalize
fmri_normalized = (fmri_2d - fmri_2d.mean(axis=1, keepdims=True)) / (
    fmri_2d.std(axis=1, keepdims=True) + 1e-8
)
```

#### Step 2: ST-CausalConv (Spatial Branch)
```python
import torch
import torch.nn as nn

class STCausalConv(nn.Module):
    """Spatial branch with causal convolution"""
    def __init__(self, n_voxels, hidden_dim=256, kernel_size=3):
        super().__init__()
        self.causal_conv = nn.Conv1d(
            in_channels=n_voxels,
            out_channels=hidden_dim,
            kernel_size=kernel_size,
            padding=kernel_size - 1,  # Causal padding
            dilation=1
        )
        self.activation = nn.ReLU()
        
    def forward(self, x):
        # x: (batch, n_voxels, time)
        out = self.causal_conv(x)
        # Remove future information (causal)
        out = out[:, :, :-self.causal_conv.padding[0]]
        return self.activation(out)
```

#### Step 3: ST-Mixer (Temporal Branch)
```python
class STMixer(nn.Module):
    """Temporal branch with MLP mixing"""
    def __init__(self, time_steps, hidden_dim=256):
        super().__init__()
        self.temporal_mlp = nn.Sequential(
            nn.Linear(time_steps, hidden_dim),
            nn.ReLU(),
            nn.Linear(hidden_dim, hidden_dim),
            nn.ReLU()
        )
        
    def forward(self, x):
        # x: (batch, n_voxels, time)
        # Transpose for temporal mixing: (batch, n_voxels, time)
        out = self.temporal_mlp(x)
        return out
```

#### Step 4: Full BrainCast Model
```python
class BrainCast(nn.Module):
    """Complete BrainCast model"""
    def __init__(self, n_voxels, input_time, output_time, hidden_dim=256):
        super().__init__()
        self.spatial_branch = STCausalConv(n_voxels, hidden_dim)
        self.temporal_branch = STMixer(input_time, hidden_dim)
        
        # Fusion and prediction
        self.fusion = nn.Sequential(
            nn.Linear(hidden_dim * 2, hidden_dim),
            nn.ReLU(),
            nn.Linear(hidden_dim, output_time)
        )
        
    def forward(self, x):
        # x: (batch, n_voxels, input_time)
        spatial_feat = self.spatial_branch(x)
        temporal_feat = self.temporal_branch(x)
        
        # Global average pooling
        spatial_feat = spatial_feat.mean(dim=1)  # (batch, hidden_dim)
        temporal_feat = temporal_feat.mean(dim=1)  # (batch, hidden_dim)
        
        # Fusion
        combined = torch.cat([spatial_feat, temporal_feat], dim=1)
        prediction = self.fusion(combined)
        
        return prediction  # (batch, output_time)
```

#### Step 5: Training
```python
def train_braincast(model, train_loader, epochs=100, lr=1e-3):
    optimizer = torch.optim.Adam(model.parameters(), lr=lr)
    criterion = nn.MSELoss()
    
    for epoch in range(epochs):
        model.train()
        total_loss = 0
        
        for batch_input, batch_target in train_loader:
            # batch_input: (batch, n_voxels, input_time)
            # batch_target: (batch, n_voxels, output_time)
            
            optimizer.zero_grad()
            
            # Predict for each voxel
            predictions = []
            for v in range(batch_input.shape[1]):
                voxel_input = batch_input[:, v:v+1, :]  # (batch, 1, input_time)
                pred = model(voxel_input)  # (batch, output_time)
                predictions.append(pred)
            
            pred_tensor = torch.stack(predictions, dim=1)  # (batch, n_voxels, output_time)
            loss = criterion(pred_tensor, batch_target)
            
            loss.backward()
            optimizer.step()
            total_loss += loss.item()
        
        if epoch % 10 == 0:
            print(f"Epoch {epoch}: Loss = {total_loss / len(train_loader):.4f}")
```

## Applications

1. **Clinical fMRI Enhancement**: Extend short scan durations for better statistical power
2. **Resting-State Analysis**: Predict long-range temporal dependencies in resting-state data
3. **Task fMRI Completion**: Forecast task-related activation beyond scan duration
4. **Brain-Computer Interfaces**: Generate extended brain state representations

## Pitfalls

- **Spatial Complexity**: Whole-brain fMRI has high dimensionality (~100K voxels); consider ROI-based analysis or dimensionality reduction
- **Temporal Dependencies**: Causal structure must be preserved; avoid data leakage from future timesteps
- **Normalization**: fMRI data requires careful normalization due to scanner and subject variability
- **Computational Cost**: Training on whole-brain data is memory-intensive; use gradient accumulation or patch-based training

## Related Skills
- brain-dit-fmri-foundation-model
- eeg-fmri-spatiotemporal-neural-frames
- brain-digital-twins-execution-semantics

## Citation
```bibtex
@article{gao2026braincast,
  title={BrainCast: A Spatio-Temporal Forecasting Model for Whole-Brain fMRI Time Series Prediction},
  author={Gao, Yunlong and Yang, Jinbo and Xiao, Li and others},
  journal={arXiv preprint arXiv:2603.13361},
  year={2026}
}
```
