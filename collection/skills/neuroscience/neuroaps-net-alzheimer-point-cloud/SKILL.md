---
name: neuroaps-net-alzheimer-point-cloud
description: "Neuro-Anatomically Aware Point Cloud Representation (NeuroAPS-Net) for efficient Alzheimer's disease classification from MRI. Converts T1-weighted MRI into anatomically-informed 2D point clouds with region-aware feature encoding. Activation triggers: Alzheimer's classification, neuroanatomical point cloud, MRI analysis, geometric deep learning."
---

# NeuroAPS-Net: Neuro-Anatomically Aware Point Cloud Representation for Alzheimer's Disease Classification

> A lightweight geometric deep learning model that converts T1-weighted MRI into anatomically-informed 2D point clouds for efficient and interpretable Alzheimer's disease classification.

## Metadata
- **Source**: arXiv:2604.22883v1
- **Authors**: Towhidul Islam, Mufti Mahmud
- **Published**: 2026-04-24
- **Category**: Neuroimaging, Geometric Deep Learning, Alzheimer's Disease

## Core Methodology

### Problem Statement
Alzheimer's disease (AD) classification from structural MRI faces challenges:
- **Computational cost** - 3D CNNs are resource-intensive
- **Limited deployment** - Difficult to deploy in resource-constrained settings
- **Memory requirements** - 3D convolutions consume significant GPU memory
- **Interpretability** - Voxel-based methods lack anatomical interpretability

### Key Innovations

**1. Anatomical Priority Sampling (APS)**
Converts T1-weighted MRI into neuroanatomically-labeled 2D point clouds:
- Prioritizes sampling from AD-relevant brain regions
- Preserves anatomical structure in point cloud representation
- Creates ADNI-2DPC: first neuroanatomically labeled MRI-derived point cloud dataset

**2. NeuroAPS-Net Architecture**
Lightweight geometric deep learning model with:
- Region-aware feature encoding
- ROI token aggregation
- Anatomical prior integration

### System Pipeline

```
T1-weighted MRI
      ↓
[Preprocessing: Skull Stripping, Registration]
      ↓
[Anatomical Segmentation: AAL or Destrieux Atlas]
      ↓
[Anatomical Priority Sampling (APS)]
      ↓
Neuroanatomical Point Cloud (ADNI-2DPC)
      ↓
[NeuroAPS-Net: Geometric Deep Learning]
      ↓
AD Classification (CN/MCI/AD)
```

### Anatomical Priority Sampling (APS)

**AD-Relevant Brain Regions:**
- Hippocampus (medial temporal lobe)
- Amygdala
- Entorhinal cortex
- Posterior cingulate cortex
- Precuneus
- Lateral temporal cortex
- Parietal association cortex

**Sampling Strategy:**
```
Traditional Uniform Sampling:
┌──────────────────────────────┐
│  •    •    •    •    •       │  ← Equal density everywhere
│  •    •    •    •    •       │
│  •    •    •    •    •       │
└──────────────────────────────┘

Anatomical Priority Sampling:
┌──────────────────────────────┐
│     •••  (hippocampus)       │  ← Higher density in AD regions
│  •    •••••    •             │
│     •  (precuneus)  •        │
│  •    •    •    •    •       │  ← Lower density elsewhere
└──────────────────────────────┘
```

### NeuroAPS-Net Architecture

```
Input Point Cloud [N_points, 3(xyz) + C_features + R_roi_id]
                ↓
    ┌───────────────────────┐
    │  Point Feature Encoder│
    │  - MLP for local feat │
    └───────────┬───────────┘
                ↓
    ┌───────────────────────┐
    │  Region-Aware Encoding│
    │  - ROI-specific layers│
    │  - Anatomical priors  │
    └───────────┬───────────┘
                ↓
    ┌───────────────────────┐
    │  ROI Token Aggregation│
    │  - Pool by anatomical │
    │    region             │
    └───────────┬───────────┘
                ↓
    ┌───────────────────────┐
    │  Classification Head  │
    │  - MLP + Softmax      │
    └───────────┬───────────┘
                ↓
         AD / MCI / CN
```

## Implementation Guide

### Prerequisites
```python
# Core dependencies
numpy
scipy
torch
torch-geometric  # For point cloud processing
nibabel          # For MRI I/O
scikit-learn

# Neuroimaging
ants             # Advanced Normalization Tools
freesurfer       # For anatomical segmentation (optional)
```

### Anatomical Priority Sampling

```python
import numpy as np
import nibabel as nib
from scipy.spatial import cKDTree

class AnatomicalPrioritySampler:
    """
    Convert T1-weighted MRI to anatomically-informed point cloud.
    """
    def __init__(self, ad_relevant_regions=None, base_samples=2048,
                 priority_ratio=0.6):
        """
        Args:
            ad_relevant_regions: List of ROI IDs for AD-relevant regions
            base_samples: Total number of points to sample
            priority_ratio: Fraction of samples allocated to priority regions
        """
        # Default AD-relevant regions (AAL atlas IDs)
        self.ad_regions = ad_relevant_regions or [
            37, 38,  # Hippocampus (L/R)
            39, 40,  # Amygdala (L/R)
            89, 90,  # Parahippocampal gyrus (L/R)
            85, 86,  # Posterior cingulate (L/R)
            67, 68,  # Precuneus (L/R)
        ]
        self.base_samples = base_samples
        self.priority_ratio = priority_ratio
    
    def load_mri_and_atlas(self, mri_path, atlas_path):
        """Load T1 MRI and anatomical atlas."""
        mri_img = nib.load(mri_path)
        atlas_img = nib.load(atlas_path)
        
        mri_data = mri_img.get_fdata()
        atlas_data = atlas_img.get_fdata()
        
        # Get voxel coordinates
        coords = np.argwhere(mri_data > 0)  # Non-zero voxels
        
        return mri_data, atlas_data, coords
    
    def sample_priority_regions(self, mri_data, atlas_data, coords):
        """
        Sample more densely from AD-relevant regions.
        
        Returns:
            priority_points: [N_priority, 4] - (x, y, z, intensity)
            priority_labels: [N_priority] - ROI labels
        """
        priority_points = []
        priority_labels = []
        
        n_priority_samples = int(self.base_samples * self.priority_ratio)
        
        for roi_id in self.ad_regions:
            roi_mask = atlas_data == roi_id
            roi_coords = np.argwhere(roi_mask)
            
            if len(roi_coords) == 0:
                continue
            
            # Sample from this region
            n_samples_per_roi = n_priority_samples // len(self.ad_regions)
            
            if len(roi_coords) > n_samples_per_roi:
                idx = np.random.choice(len(roi_coords), n_samples_per_roi, replace=False)
                sampled = roi_coords[idx]
            else:
                sampled = roi_coords
            
            # Get intensity values
            intensities = mri_data[sampled[:, 0], sampled[:, 1], sampled[:, 2]]
            
            for i, coord in enumerate(sampled):
                priority_points.append([coord[0], coord[1], coord[2], intensities[i]])
                priority_labels.append(roi_id)
        
        return np.array(priority_points), np.array(priority_labels)
    
    def sample_background(self, mri_data, atlas_data, n_samples):
        """Sample from non-priority brain regions."""
        background_mask = ~np.isin(atlas_data, self.ad_regions) & (mri_data > 0)
        background_coords = np.argwhere(background_mask)
        
        if len(background_coords) > n_samples:
            idx = np.random.choice(len(background_coords), n_samples, replace=False)
            sampled = background_coords[idx]
        else:
            sampled = background_coords
        
        intensities = mri_data[sampled[:, 0], sampled[:, 1], sampled[:, 2]]
        
        points = []
        labels = []
        for i, coord in enumerate(sampled):
            points.append([coord[0], coord[1], coord[2], intensities[i]])
            labels.append(0)  # Background label
        
        return np.array(points), np.array(labels)
    
    def convert_to_2d(self, points_3d, projection_plane='axial'):
        """
        Project 3D points to 2D while preserving anatomical information.
        
        Args:
            points_3d: [N, 4] array of (x, y, z, intensity)
            projection_plane: 'axial', 'sagittal', or 'coronal'
        
        Returns:
            points_2d: [N, 3] array of (u, v, intensity)
        """
        if projection_plane == 'axial':
            # Project to x-y plane, use z as feature
            points_2d = np.column_stack([
                points_3d[:, 0],  # x
                points_3d[:, 1],  # y
                points_3d[:, 3]   # intensity
            ])
        elif projection_plane == 'sagittal':
            points_2d = np.column_stack([
                points_3d[:, 1],  # y
                points_3d[:, 2],  # z
                points_3d[:, 3]   # intensity
            ])
        else:  # coronal
            points_2d = np.column_stack([
                points_3d[:, 0],  # x
                points_3d[:, 2],  # z
                points_3d[:, 3]   # intensity
            ])
        
        return points_2d
    
    def sample(self, mri_path, atlas_path, projection='axial'):
        """
        Complete sampling pipeline.
        
        Returns:
            point_cloud: [N, 3] 2D point cloud (x, y, intensity)
            roi_labels: [N] ROI labels for each point
        """
        mri_data, atlas_data, _ = self.load_mri_and_atlas(mri_path, atlas_path)
        
        # Sample priority regions
        priority_points, priority_labels = self.sample_priority_regions(
            mri_data, atlas_data, None
        )
        
        # Sample background
        n_background = self.base_samples - len(priority_points)
        background_points, background_labels = self.sample_background(
            mri_data, atlas_data, n_background
        )
        
        # Combine
        all_points = np.vstack([priority_points, background_points])
        all_labels = np.concatenate([priority_labels, background_labels])
        
        # Convert to 2D
        point_cloud_2d = self.convert_to_2d(all_points, projection)
        
        return point_cloud_2d, all_labels
```

### NeuroAPS-Net Model

```python
import torch
import torch.nn as nn
import torch.nn.functional as F
from torch_geometric.nn import MessagePassing, global_mean_pool

class PointFeatureEncoder(nn.Module):
    """
    Encode local point features using MLP.
    """
    def __init__(self, in_channels=3, hidden_dim=64):
        super().__init__()
        self.mlp = nn.Sequential(
            nn.Linear(in_channels, hidden_dim),
            nn.ReLU(),
            nn.BatchNorm1d(hidden_dim),
            nn.Linear(hidden_dim, hidden_dim),
            nn.ReLU(),
            nn.BatchNorm1d(hidden_dim)
        )
    
    def forward(self, x):
        return self.mlp(x)


class RegionAwareEncoding(nn.Module):
    """
    Region-aware feature encoding with anatomical priors.
    """
    def __init__(self, num_rois=116, feature_dim=64, embed_dim=32):
        super().__init__()
        self.num_rois = num_rois
        
        # ROI embedding (learnable anatomical priors)
        self.roi_embedding = nn.Embedding(num_rois + 1, embed_dim)  # +1 for background
        
        # Feature transformation
        self.feature_transform = nn.Sequential(
            nn.Linear(feature_dim + embed_dim, feature_dim),
            nn.ReLU(),
            nn.Linear(feature_dim, feature_dim)
        )
    
    def forward(self, features, roi_labels):
        """
        Args:
            features: [N, feature_dim]
            roi_labels: [N] ROI labels (0 = background)
        """
        # Get ROI embeddings
        roi_embeds = self.roi_embedding(roi_labels.long())
        
        # Concatenate features with ROI embeddings
        combined = torch.cat([features, roi_embeds], dim=-1)
        
        # Transform
        output = self.feature_transform(combined)
        
        return output


class ROITokenAggregation(nn.Module):
    """
    Aggregate features by anatomical region (ROI tokens).
    """
    def __init__(self, feature_dim=64, num_rois=116):
        super().__init__()
        self.feature_dim = feature_dim
        self.num_rois = num_rois
    
    def forward(self, features, roi_labels):
        """
        Args:
            features: [N, feature_dim]
            roi_labels: [N] ROI labels
        
        Returns:
            roi_tokens: [num_rois, feature_dim] aggregated by ROI
        """
        roi_tokens = []
        
        for roi_id in range(1, self.num_rois + 1):  # Skip background (0)
            mask = roi_labels == roi_id
            if mask.sum() > 0:
                # Mean pooling for this ROI
                roi_feat = features[mask].mean(dim=0)
            else:
                # Empty ROI - use zero vector
                roi_feat = torch.zeros(self.feature_dim, device=features.device)
            roi_tokens.append(roi_feat)
        
        return torch.stack(roi_tokens)


class NeuroAPSNet(nn.Module):
    """
    Complete NeuroAPS-Net for AD classification.
    """
    def __init__(self, in_channels=3, hidden_dim=64, num_rois=116, num_classes=3):
        super().__init__()
        
        # Point feature encoder
        self.point_encoder = PointFeatureEncoder(in_channels, hidden_dim)
        
        # Region-aware encoding
        self.region_encoder = RegionAwareEncoding(num_rois, hidden_dim)
        
        # ROI token aggregation
        self.roi_aggregator = ROITokenAggregation(hidden_dim, num_rois)
        
        # Classification head
        self.classifier = nn.Sequential(
            nn.Linear(hidden_dim * num_rois, 512),
            nn.ReLU(),
            nn.Dropout(0.3),
            nn.Linear(512, 128),
            nn.ReLU(),
            nn.Dropout(0.3),
            nn.Linear(128, num_classes)
        )
    
    def forward(self, point_cloud, roi_labels):
        """
        Args:
            point_cloud: [N, 3] (x, y, intensity)
            roi_labels: [N] ROI labels
        
        Returns:
            logits: [batch_size, num_classes]
        """
        # Encode point features
        features = self.point_encoder(point_cloud)
        
        # Apply region-aware encoding
        features = self.region_encoder(features, roi_labels)
        
        # Aggregate into ROI tokens
        roi_tokens = self.roi_aggregator(features, roi_labels)
        
        # Flatten and classify
        roi_tokens_flat = roi_tokens.view(1, -1)
        logits = self.classifier(roi_tokens_flat)
        
        return logits
```

### Training Pipeline

```python
def train_neuroaps_net(model, train_loader, val_loader, epochs=100, lr=1e-3):
    optimizer = torch.optim.Adam(model.parameters(), lr=lr)
    criterion = nn.CrossEntropyLoss()
    scheduler = torch.optim.lr_scheduler.ReduceLROnPlateau(optimizer, patience=10)
    
    best_val_acc = 0
    
    for epoch in range(epochs):
        # Training
        model.train()
        train_loss = 0
        for point_cloud, roi_labels, labels in train_loader:
            optimizer.zero_grad()
            
            logits = model(point_cloud, roi_labels)
            loss = criterion(logits, labels)
            
            loss.backward()
            optimizer.step()
            
            train_loss += loss.item()
        
        # Validation
        model.eval()
        val_correct = 0
        val_total = 0
        with torch.no_grad():
            for point_cloud, roi_labels, labels in val_loader:
                logits = model(point_cloud, roi_labels)
                _, predicted = torch.max(logits, 1)
                val_correct += (predicted == labels).sum().item()
                val_total += labels.size(0)
        
        val_acc = val_correct / val_total
        scheduler.step(val_acc)
        
        if val_acc > best_val_acc:
            best_val_acc = val_acc
            torch.save(model.state_dict(), 'best_neuroaps_net.pth')
        
        print(f"Epoch {epoch+1}: Train Loss={train_loss/len(train_loader):.4f}, "
              f"Val Acc={val_acc:.4f}")
```

## Applications

1. **Early AD Detection** - Screen for mild cognitive impairment
2. **Clinical Decision Support** - Assist radiologists in diagnosis
3. **Longitudinal Tracking** - Monitor disease progression
4. **Research Studies** - Large-scale AD analysis
5. **Resource-Constrained Settings** - Deploy in clinics with limited GPU resources

## Key Metrics

- **Accuracy**: Competitive with state-of-the-art 3D CNNs
- **Efficiency**: Significantly reduced inference latency
- **Memory**: Lower GPU memory requirements
- **Interpretability**: ROI-level predictions explain which brain regions contribute

## Pitfalls

1. **Atlas Dependency** - Requires accurate anatomical segmentation
2. **Sampling Variability** - Random sampling may affect reproducibility
3. **2D Projection** - Some 3D spatial information is lost
4. **ROI Selection** - AD-relevant regions are dataset-dependent
5. **Point Cloud Size** - Trade-off between detail and computational cost

## Related Skills

- alzheimer-pet-suvr-network-models - Spatio-temporal AD models
- multimodal-brain-connectivity-gnn - Multi-modal brain analysis
- brain-graph-neural - Graph-based brain network analysis

## References

```bibtex
@article{islam2026neuroaps,
  title={NeuroAPS-Net: Neuro-Anatomically Aware Point Cloud Representation for Efficient Alzheimer's Disease Classification},
  author={Islam, Towhidul and Mahmud, Mufti},
  journal={arXiv preprint arXiv:2604.22883},
  year={2026}
}
```
