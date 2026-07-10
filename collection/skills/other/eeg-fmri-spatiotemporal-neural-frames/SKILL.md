---
title: EEG-conditioned fMRI Reconstruction for High-Resolution Brain Dynamics
name: eeg-fmri-spatiotemporal-neural-frames
category: ai_collection
description: EEG-conditioned framework for reconstructing dynamic fMRI as continuous neural sequences with high spatial fidelity and temporal coherence at cortical-vertex level. Incorporates null-space intermediate-frame reconstruction for handling sampling irregularities.
arXiv_id: 2603.24176
author: Wanying Qu, Jianxiong Gao, Wei Wang, Yanwei Fu
date: 2026
venue: CVPR 2026
---

# Modeling Spatiotemporal Neural Frames for High Resolution Brain Dynamics

## Overview

A CVPR 2026 paper presenting an EEG-conditioned framework for reconstructing dynamic fMRI as continuous neural sequences with high spatial fidelity and strong temporal coherence at the cortical-vertex level. Key innovation: null-space intermediate-frame reconstruction for handling real-world fMRI sampling irregularities.

## Core Contributions

1. **EEG-to-fMRI Reconstruction**: Leverages millisecond-level EEG temporal cues to reconstruct high-resolution fMRI
2. **Spatiotemporal Neural Frames**: Continuous neural sequences at cortical-vertex level
3. **Null-space Intermediate Reconstruction**: Handles sampling irregularities in real fMRI acquisitions
4. **Measurement-Consistent Completion**: Guarantees arbitrary intermediate frame completion

## Methodology

### Framework Architecture

```python
class SpatiotemporalNeuralFrames(nn.Module):
    """
    EEG-conditioned fMRI reconstruction with null-space completion
    """
    def __init__(self, 
                 eeg_channels=64,
                 fmri_vertices=59412,  # Cortical surface vertices
                 latent_dim=512,
                 num_frames=10):
        super().__init__()
        
        # EEG encoder (temporal features)
        self.eeg_encoder = EEGEncoder(
            in_channels=eeg_channels,
            temporal_dim=latent_dim // 2
        )
        
        # Spatial decoder (vertex-wise reconstruction)
        self.spatial_decoder = CorticalVertexDecoder(
            latent_dim=latent_dim,
            num_vertices=fmri_vertices
        )
        
        # Null-space completion module
        self.nullspace_completer = NullSpaceCompleter(
            latent_dim=latent_dim
        )
        
        # Temporal coherence module
        self.temporal_coherence = TemporalCoherence(
            latent_dim=latent_dim
        )
        
    def forward(self, eeg_sequence, known_fmri_indices, known_fmri_frames):
        """
        Args:
            eeg_sequence: [batch, channels, time] - EEG recording
            known_fmri_indices: [num_known] - Indices of known fMRI frames
            known_fmri_frames: [batch, vertices, num_known] - Available fMRI frames
        
        Returns:
            complete_sequence: [batch, vertices, num_frames] - Full fMRI sequence
        """
        # Encode EEG temporal dynamics
        eeg_features = self.eeg_encoder(eeg_sequence)
        
        # Generate initial frame estimates from EEG
        initial_frames = self.spatial_decoder(eeg_features)
        
        # Apply null-space completion for known frames
        completed_frames = self.nullspace_completer(
            initial_frames,
            known_fmri_indices,
            known_fmri_frames
        )
        
        # Enforce temporal coherence
        coherent_sequence = self.temporal_coherence(completed_frames)
        
        return coherent_sequence

class NullSpaceCompleter(nn.Module):
    """
    Null-space intermediate frame reconstruction
    
    Handles irregular sampling by decomposing into:
    - Measurement space: Matches known observations
    - Null space: Completes unknown frames while consistent with measurements
    """
    def __init__(self, latent_dim, num_iterations=5):
        super().__init__()
        self.latent_dim = latent_dim
        self.num_iterations = num_iterations
        
        # Learnable projection operators
        self.P_measured = nn.Linear(latent_dim, latent_dim)
        self.P_null = nn.Linear(latent_dim, latent_dim)
        
    def forward(self, initial_frames, known_indices, known_values):
        """
        Args:
            initial_frames: [batch, vertices, num_frames]
            known_indices: [num_known]
            known_values: [batch, vertices, num_known]
        
        Returns:
            completed_frames: [batch, vertices, num_frames]
        """
        # Initial estimate
        x = initial_frames.clone()
        
        # Iterative null-space projection
        for _ in range(self.num_iterations):
            # Project to measurement space (force known values)
            x_measured = x.clone()
            x_measured[..., known_indices] = known_values
            
            # Encode to latent
            z_measured = self.P_measured(x_measured.transpose(-2, -1))
            z_null = self.P_null(x.transpose(-2, -1))
            
            # Combine: measurement + null space exploration
            z_combined = z_measured + z_null
            
            # Decode back
            x = z_combined.transpose(-2, -1)
            
        return x

class TemporalCoherence(nn.Module):
    """
    Enforce temporal smoothness across frames using learned dynamics
    """
    def __init__(self, latent_dim):
        super().__init__()
        
        # Temporal dynamics model
        self.temporal_model = nn.LSTM(
            latent_dim, latent_dim,
            num_layers=2, bidirectional=True
        )
        
        # Smoothness constraint
        self.smoothness_weight = 0.1
        
    def forward(self, frames):
        """
        Args:
            frames: [batch, vertices, num_frames]
        
        Returns:
            smoothed: [batch, vertices, num_frames]
        """
        # Transpose for LSTM [batch, seq, features]
        x = frames.transpose(-2, -1)  # [batch, frames, vertices]
        
        # Temporal modeling
        smoothed, _ = self.temporal_model(x)
        
        # Combine forward and backward
        smoothed = smoothed[..., :frames.size(-2)] + smoothed[..., frames.size(-2):]
        
        # Temporal smoothness loss
        temporal_diff = smoothed[:, 1:] - smoothed[:, :-1]
        smoothness_loss = torch.mean(temporal_diff ** 2)
        
        return smoothed.transpose(-2, -1), smoothness_loss
```

### EEG Feature Extraction

```python
class EEGEncoder(nn.Module):
    """
    Extract temporal features from EEG signals
    """
    def __init__(self, in_channels=64, temporal_dim=256):
        super().__init__()
        
        # Multi-scale temporal convolution
        self.temporal_conv = nn.ModuleList([
            nn.Conv1d(in_channels, 64, kernel_size=k, padding=k//2)
            for k in [3, 7, 15, 31]  # Different temporal scales
        ])
        
        # Attention across scales
        self.scale_attention = nn.MultiheadAttention(64 * 4, num_heads=4)
        
        # Frequency analysis
        self.freq_bands = {
            'delta': (0.5, 4),
            'theta': (4, 8),
            'alpha': (8, 13),
            'beta': (13, 30),
            'gamma': (30, 100)
        }
        
        self.freq_encoder = nn.Sequential(
            nn.Linear(len(self.freq_bands) * 64, temporal_dim),
            nn.LayerNorm(temporal_dim),
            nn.GELU()
        )
        
    def extract_frequency_bands(self, eeg):
        """
        Extract power in canonical frequency bands
        eeg: [batch, channels, time]
        """
        from scipy import signal
        
        batch, channels, time = eeg.shape
        band_powers = []
        
        for band_name, (low, high) in self.freq_bands.items():
            # Bandpass filter
            sos = signal.butter(4, [low, high], btype='band', fs=128, output='sos')
            filtered = signal.sosfilt(sos, eeg.cpu().numpy(), axis=-1)
            
            # Compute power
            power = torch.from_numpy(filtered ** 2).to(eeg.device)
            band_powers.append(power.mean(dim=-1, keepdim=True))
            
        return torch.cat(band_powers, dim=-1)  # [batch, channels, num_bands]
        
    def forward(self, eeg):
        """
        Args:
            eeg: [batch, channels, time] - Raw EEG signal
        
        Returns:
            features: [batch, temporal_dim] - Temporal features
        """
        # Multi-scale temporal features
        temporal_features = []
        for conv in self.temporal_conv:
            feat = F.relu(conv(eeg))
            temporal_features.append(feat.mean(dim=-1))  # Global temporal pooling
            
        multi_scale = torch.cat(temporal_features, dim=-1)  # [batch, 256]
        
        # Frequency features
        freq_features = self.extract_frequency_bands(eeg)
        freq_features = freq_features.view(freq_features.size(0), -1)
        
        # Combine
        combined = torch.cat([multi_scale, freq_features], dim=-1)
        
        return self.freq_encoder(combined)
```

### Cortical Vertex Decoder

```python
class CorticalVertexDecoder(nn.Module):
    """
    Decode latent features to cortical vertex activations
    """
    def __init__(self, latent_dim=512, num_vertices=59412):
        super().__init__()
        
        # Surface-aware graph convolution
        self.surface_encoder = SurfaceGraphEncoder(latent_dim)
        
        # Vertex-wise MLP
        self.vertex_decoder = nn.Sequential(
            nn.Linear(latent_dim, 1024),
            nn.LayerNorm(1024),
            nn.GELU(),
            nn.Linear(1024, 512),
            nn.LayerNorm(512),
            nn.GELU(),
            nn.Linear(512, 1)  # Single activation per vertex
        )
        
        # Temporal expansion
        self.temporal_expansion = nn.Linear(1, num_frames)
        
    def forward(self, eeg_features, surface_mesh):
        """
        Args:
            eeg_features: [batch, latent_dim]
            surface_mesh: Graph structure of cortical surface
        
        Returns:
            vertex_activations: [batch, num_vertices, num_frames]
        """
        # Encode surface geometry
        surface_features = self.surface_encoder(eeg_features, surface_mesh)
        
        # Decode to vertices
        activations = self.vertex_decoder(surface_features)  # [batch, vertices, 1]
        
        # Expand temporally
        activations_temporal = self.temporal_expansion(activations)
        
        return activations_temporal

class SurfaceGraphEncoder(nn.Module):
    """
    Graph encoder incorporating cortical surface geometry
    """
    def __init__(self, latent_dim):
        super().__init__()
        from torch_geometric.nn import GCNConv
        
        self.conv1 = GCNConv(latent_dim, 256)
        self.conv2 = GCNConv(256, 256)
        self.conv3 = GCNConv(256, latent_dim)
        
    def forward(self, eeg_features, surface_mesh):
        """
        Args:
            eeg_features: [batch, latent_dim]
            surface_mesh: PyTorch Geometric Data object
        
        Returns:
            surface_features: [batch, num_vertices, latent_dim]
        """
        x, edge_index = surface_mesh.x, surface_mesh.edge_index
        
        # Broadcast EEG features to all vertices
        x = x + eeg_features.unsqueeze(1)  # [batch, vertices, latent_dim]
        
        # Graph convolution
        x = F.relu(self.conv1(x, edge_index))
        x = F.relu(self.conv2(x, edge_index))
        x = self.conv3(x, edge_index)
        
        return x
```

## Key Innovations

1. **Null-space Completion**: Decomposes reconstruction into measurement + null spaces
2. **Cortical-Vertex Level**: Operates at fine-grained surface vertices (59k+ vertices)
3. **Temporal Coherence**: Enforces smoothness across time using bidirectional LSTM
4. **Multi-scale EEG**: Uses multiple temporal scales and frequency bands

## Results

### Dataset: CineBrain

- Superior voxel-wise reconstruction quality
- Robust temporal consistency across whole brain
- Preserves functional information for downstream tasks
- Supports visual decoding from reconstructed fMRI

### Metrics

| Metric | Performance |
|--------|-------------|
| Voxel-wise Reconstruction | State-of-the-art |
| Temporal Consistency | Robust |
| Functional Preservation | Excellent |
| Visual Decoding | Supported |

## Applications

1. **High-resolution fMRI estimation from EEG**: Cost-effective alternative
2. **Missing data imputation**: Complete irregularly sampled fMRI
3. **Temporal super-resolution**: Increase temporal resolution of fMRI
4. **Visual decoding**: Reconstruct perceived stimuli from neural activity

## Implementation

```python
def train_model(model, train_loader, num_epochs=100):
    optimizer = torch.optim.AdamW(model.parameters(), lr=1e-4)
    
    for epoch in range(num_epochs):
        for batch in train_loader:
            eeg, fmri, sampling_mask = batch
            
            # Known frames from sampling mask
            known_indices = torch.where(sampling_mask)[0]
            known_frames = fmri[..., known_indices]
            
            # Forward
            reconstructed = model(eeg, known_indices, known_frames)
            
            # Losses
            recon_loss = F.mse_loss(reconstructed, fmri)
            smooth_loss = model.temporal_coherence.smoothness_weight
            
            loss = recon_loss + smooth_loss
            
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()
```

## References

- Paper: "Modeling Spatiotemporal Neural Frames for High Resolution Brain Dynamic" (arXiv:2603.24176)
- Authors: Wanying Qu, Jianxiong Gao, Wei Wang, Yanwei Fu
- Venue: CVPR 2026

## Trigger Words
- EEG fMRI reconstruction, spatiotemporal neural frames, null-space completion, cortical-vertex reconstruction, temporal coherence brain, multimodal neuroimaging, measurement-consistent completion