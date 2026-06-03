---
name: neurostorm-fmri-foundation
description: "NeuroSTORM - Neuroimaging Foundation Model with Spatial-Temporal Optimized Representation for fMRI analysis. Trained on 28.65M frames from 50,000 subjects using shifted scanning Mamba backbone. Activation triggers: fMRI foundation model, neuroimaging, NeuroSTORM, brain analysis, Mamba fMRI, spatial-temporal modeling."
---

# NeuroSTORM: fMRI Foundation Model

> A general-purpose foundation model for fMRI analysis with spatial-temporal optimized representation modeling, achieving efficient knowledge transfer across diverse downstream applications.

## Metadata
- **Source**: arXiv:2506.11167
- **Authors**: Cheng Wang, Yu Jiang, Zhihao Peng, Chenxin Li, Changbae Bang, Lin Zhao, Jinglei Lv, Jorge Sepulcre, Carl Yang, Lifang He, Tianming Liu, Daniel Barron, Quanzheng Li, Randy Hirschtick, Byung-Hoon Kim, Xiang Li, Yixuan Yuan
- **Published**: 2025-06
- **Code**: TBD (check paper for updates)

## Core Methodology

### Key Innovation

NeuroSTORM addresses three critical challenges in fMRI analysis:
1. **Reproducibility**: Standardized preprocessing and model architecture
2. **Transferability**: Generalizable representations across datasets and tasks
3. **Scalability**: Direct 4D volume processing without patch-wise fragmentation

### Technical Framework

#### 1. Shifted Scanning Mamba Backbone

```
Traditional Mamba: Sequential scan → Limited spatial context
NeuroSTORM Shifted Scanning:
┌─────────────────────────────────────────┐
│  Scan 1: Horizontal (→→→→→→)         │
│  Scan 2: Vertical   (↓↓↓↓↓↓)          │
│  Scan 3: Diagonal   (↘↘↘↘↘↘)         │
│  Scan 4: Anti-diagonal (↙↙↙↙↙)       │
└─────────────────────────────────────────┘
```

**Key Features**:
- Multi-directional scanning captures complex spatial dependencies
- Linear computational complexity O(N) vs O(N²) for transformers
- Efficient processing of high-resolution 4D fMRI volumes

#### 2. Spatial-Temporal Optimized Pre-training

| Component | Description | Benefit |
|-----------|-------------|---------|
| **Spatial Encoder** | Shifted scanning Mamba | Capture anatomical structure |
| **Temporal Encoder** | Temporal convolution | Model temporal dynamics |
| **Fusion Module** | Cross-attention | Integrate spatial-temporal features |
| **Prompt Tuning** | Task-specific adapters | Efficient downstream adaptation |

#### 3. Training Scale

- **Data**: 28.65 million fMRI frames (≈9,000 hours)
- **Subjects**: 50,000+ subjects
- **Age Range**: 5 to 100 years
- **Sites**: Multiple centers worldwide
- **Modalities**: rsfMRI, tfMRI, clinical data

### Model Architecture

```python
"""
NeuroSTORM Architecture Overview

Input: 4D fMRI (T, H, W, D) → (time, height, width, depth)
│
├─► Spatial-Temporal Embedding
│   ├─ 3D Patch Embedding: (H, W, D) → tokens
│   └─ Temporal Position Encoding
│
├─► Shifted Scanning Mamba Blocks (×L)
│   ├─ Multi-directional scanning
│   ├─ Selective state space modeling
│   └─ Residual connections
│
├─► Temporal Modeling
│   └─ 1D Convolution + Mamba
│
├─► Prompt Tuning Adapter
│   └─ Task-specific soft prompts
│
└─► Output: Task predictions
"""
```

### Prompt Tuning for Downstream Tasks

```python
class PromptTuningAdapter(nn.Module):
    """Task-specific prompt tuning for NeuroSTORM"""
    
    def __init__(self, embed_dim, n_tasks):
        super().__init__()
        # Learnable prompt tokens for each task
        self.task_prompts = nn.Parameter(
            torch.randn(n_tasks, num_prompt_tokens, embed_dim)
        )
        self.task_embeddings = nn.Embedding(n_tasks, embed_dim)
    
    def forward(self, x, task_id):
        # Get task-specific prompt
        prompt = self.task_prompts[task_id]
        
        # Concatenate prompt with features
        x = torch.cat([prompt, x], dim=1)
        
        # Process through frozen backbone
        return self.backbone(x)
```

## Implementation Guide

### Prerequisites

```python
# Required packages
pip install torch torchvision torchaudio
pip install nibabel nilearn  # fMRI I/O and visualization
pip install einops           # Tensor operations
pip install mamba-ssm        # State space models (if available)

# Or use pure PyTorch implementation
```

### Step-by-Step

#### Step 1: Data Preprocessing

```python
import nibabel as nib
import numpy as np
from nilearn import datasets, image

def preprocess_fmri(fmri_path, mask_path=None):
    """
    Standardize fMRI preprocessing for NeuroSTORM
    
    Args:
        fmri_path: Path to 4D fMRI nifti file
        mask_path: Optional brain mask
    
    Returns:
        preprocessed: (T, H, W, D) numpy array
    """
    # Load fMRI data
    fmri_img = nib.load(fmri_path)
    fmri_data = fmri_img.get_fdata()
    
    # Standard preprocessing steps
    # 1. Motion correction (if not done)
    # 2. Slice timing correction
    # 3. Spatial normalization to MNI space
    
    # 4. Temporal filtering (0.01-0.1 Hz for rsfMRI)
    from scipy.signal import butter, filtfilt
    
    def bandpass_filter(data, low_freq=0.01, high_freq=0.1, tr=2.0):
        """Bandpass filter fMRI time series"""
        nyquist = 1 / (2 * tr)
        low = low_freq / nyquist
        high = high_freq / nyquist
        b, a = butter(3, [low, high], btype='band')
        return filtfilt(b, a, data, axis=0)
    
    # Apply temporal filtering
    T, H, W, D = fmri_data.shape
    reshaped = fmri_data.reshape(T, -1)
    filtered = bandpass_filter(reshaped)
    fmri_filtered = filtered.reshape(T, H, W, D)
    
    # 5. Spatial smoothing (optional, FWHM=6mm)
    from scipy.ndimage import gaussian_filter
    fmri_smoothed = np.zeros_like(fmri_filtered)
    for t in range(T):
        fmri_smoothed[t] = gaussian_filter(fmri_filtered[t], sigma=1.5)
    
    # 6. Z-score normalization per voxel
    mean = fmri_smoothed.mean(axis=0, keepdims=True)
    std = fmri_smoothed.std(axis=0, keepdims=True)
    fmri_normalized = (fmri_smoothed - mean) / (std + 1e-8)
    
    return fmri_normalized


# Load standard brain template
def get_mni_template(resolution='2mm'):
    """Get MNI template for spatial normalization"""
    template = datasets.load_mni152_template(resolution=resolution)
    return template
```

#### Step 2: Shifted Scanning Mamba Implementation

```python
import torch
import torch.nn as nn
import torch.nn.functional as F
from einops import rearrange

class ShiftedScanMamba(nn.Module):
    """
    Shifted Scanning Mamba Block for 3D fMRI volumes
    """
    
    def __init__(self, dim, d_state=16, d_conv=4, expand=2):
        super().__init__()
        self.dim = dim
        self.d_inner = int(expand * dim)
        
        # Input projection
        self.in_proj = nn.Linear(dim, self.d_inner * 2, bias=False)
        
        # Convolution for local feature extraction
        self.conv = nn.Conv1d(
            in_channels=self.d_inner,
            out_channels=self.d_inner,
            kernel_size=d_conv,
            padding=d_conv // 2,
            groups=self.d_inner,
            bias=True
        )
        
        # State space parameters
        self.x_proj = nn.Linear(self.d_inner, d_state * 2 + self.d_inner, bias=False)
        self.dt_proj = nn.Linear(d_state, self.d_inner, bias=True)
        
        # Output projection
        self.out_proj = nn.Linear(self.d_inner, dim, bias=False)
        
    def forward(self, x, scan_mode='horizontal'):
        """
        Args:
            x: (B, L, D) - batch, sequence length, features
            scan_mode: 'horizontal', 'vertical', 'diagonal', 'anti_diagonal'
        """
        B, L, D = x.shape
        
        # Apply scanning based on mode
        if scan_mode == 'horizontal':
            x_scan = x
        elif scan_mode == 'vertical':
            x_scan = rearrange(x, 'b (h w) d -> b (w h) d', h=int(L**0.5))
        elif scan_mode == 'diagonal':
            # Diagonal scanning
            x_scan = self._diagonal_scan(x)
        elif scan_mode == 'anti_diagonal':
            # Anti-diagonal scanning
            x_scan = self._anti_diagonal_scan(x)
        
        # Input projection and split
        x_and_gate = self.in_proj(x_scan)
        x_in, gate = x_and_gate.chunk(2, dim=-1)
        
        # Convolution
        x_conv = self.conv(rearrange(x_in, 'b l d -> b d l'))
        x_conv = rearrange(x_conv, 'b d l -> b l d')
        
        # SSM computation (simplified)
        x_ssm = self._ssm_step(x_conv)
        
        # Gating
        output = x_ssm * F.silu(gate)
        
        # Output projection
        output = self.out_proj(output)
        
        # Reverse scan transformation
        if scan_mode == 'vertical':
            output = rearrange(output, 'b (w h) d -> b (h w) d', h=int(L**0.5))
        elif scan_mode in ['diagonal', 'anti_diagonal']:
            output = self._reverse_diagonal_scan(output, scan_mode)
        
        return output + x  # Residual connection
    
    def _ssm_step(self, x):
        """Simplified SSM forward pass"""
        # In practice, use mamba-ssm or implement full discretization
        # This is a placeholder for the actual SSM computation
        return x


class MultiScanMambaBlock(nn.Module):
    """Multi-directional scanning with feature fusion"""
    
    def __init__(self, dim, n_scans=4):
        super().__init__()
        self.scans = ['horizontal', 'vertical', 'diagonal', 'anti_diagonal']
        self.mamba_layers = nn.ModuleList([
            ShiftedScanMamba(dim) for _ in range(n_scans)
        ])
        self.fusion = nn.Linear(dim * n_scans, dim)
    
    def forward(self, x):
        """Aggregate multi-directional features"""
        outputs = []
        for mamba, scan in zip(self.mamba_layers, self.scans):
            outputs.append(mamba(x, scan_mode=scan))
        
        # Concatenate and fuse
        multi_scan = torch.cat(outputs, dim=-1)
        return self.fusion(multi_scan) + x
```

#### Step 3: NeuroSTORM Model

```python
class NeuroSTORM(nn.Module):
    """
    NeuroSTORM: Neuroimaging Foundation Model
    for Spatial-Temporal Optimized Representation Modeling
    """
    
    def __init__(
        self,
        img_size=(64, 64, 64),  # Standardized fMRI size
        patch_size=8,
        in_chans=1,
        embed_dim=768,
        depth=12,
        num_heads=12,
        num_prompts=50,
        num_tasks=10
    ):
        super().__init__()
        
        self.patch_size = patch_size
        self.num_patches = (img_size[0] // patch_size) * \
                          (img_size[1] // patch_size) * \
                          (img_size[2] // patch_size)
        
        # 3D Patch embedding
        self.patch_embed = nn.Conv3d(
            in_chans, embed_dim,
            kernel_size=patch_size,
            stride=patch_size
        )
        
        # Positional encoding
        self.pos_embed = nn.Parameter(
            torch.randn(1, self.num_patches, embed_dim) * 0.02
        )
        
        # Temporal encoding
        self.temporal_embed = nn.Parameter(
            torch.randn(1, 1000, embed_dim) * 0.02  # Max 1000 timepoints
        )
        
        # Multi-scan Mamba blocks
        self.blocks = nn.ModuleList([
            MultiScanMambaBlock(embed_dim) for _ in range(depth)
        ])
        
        # Task-specific prompts
        self.task_prompts = nn.Parameter(
            torch.randn(num_tasks, num_prompts, embed_dim)
        )
        
        # Temporal modeling
        self.temporal_conv = nn.Conv1d(
            embed_dim, embed_dim,
            kernel_size=3, padding=1
        )
        
        # Classification head
        self.norm = nn.LayerNorm(embed_dim)
        self.head = nn.Linear(embed_dim, num_classes)
    
    def forward(self, x, task_id=0, return_features=False):
        """
        Args:
            x: (B, T, H, W, D) - batch, time, spatial dims
            task_id: Task identifier for prompt tuning
            return_features: Return intermediate features
        
        Returns:
            logits or features
        """
        B, T, H, W, D = x.shape
        
        # Process each timepoint
        temporal_features = []
        for t in range(T):
            # Extract spatial features
            xt = x[:, t:t+1]  # (B, 1, H, W, D)
            
            # Patch embedding
            patches = self.patch_embed(xt)  # (B, E, h, w, d)
            patches = rearrange(patches, 'b e h w d -> b (h w d) e')
            
            # Add positional encoding
            patches = patches + self.pos_embed
            
            # Apply multi-scan blocks
            h = patches
            for block in self.blocks:
                h = block(h)
            
            temporal_features.append(h)
        
        # Stack temporal features
        temporal_stack = torch.stack(temporal_features, dim=1)  # (B, T, N, E)
        
        # Add temporal encoding
        temporal_stack = temporal_stack + self.temporal_embed[:, :T, None, :]
        
        # Temporal modeling per patch
        temporal_flat = rearrange(temporal_stack, 'b t n e -> (b n) e t')
        temporal_conv = self.temporal_conv(temporal_flat)
        temporal_feat = rearrange(temporal_conv, '(b n) e t -> b t n e', b=B)
        
        # Add task-specific prompts
        prompts = self.task_prompts[task_id:task_id+1]  # (1, P, E)
        prompts = prompts.expand(B, -1, -1)
        
        # Concatenate prompts with features
        features_with_prompts = torch.cat([prompts, temporal_feat[:, -1]], dim=1)
        
        # Normalize and pool
        features = self.norm(features_with_prompts)
        pooled = features.mean(dim=1)  # Global average pooling
        
        if return_features:
            return pooled
        
        # Classification
        logits = self.head(pooled)
        return logits
```

#### Step 4: Training and Fine-tuning

```python
import torch.optim as optim
from torch.utils.data import DataLoader

def pretrain_neurostorm(model, train_loader, epochs=100, lr=1e-4):
    """
    Pre-training with masked reconstruction objective
    """
    optimizer = optim.AdamW(model.parameters(), lr=lr, weight_decay=0.05)
    scheduler = optim.lr_scheduler.CosineAnnealingLR(optimizer, epochs)
    
    for epoch in range(epochs):
        model.train()
        total_loss = 0
        
        for batch in train_loader:
            fmri = batch['fmri']  # (B, T, H, W, D)
            
            # Apply spatial-temporal masking
            masked_fmri, mask = apply_spatiotemporal_mask(fmri, mask_ratio=0.4)
            
            # Forward pass
            reconstructed = model(masked_fmri, return_features=False)
            
            # Reconstruction loss
            loss = F.mse_loss(reconstructed, fmri[mask])
            
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()
            
            total_loss += loss.item()
        
        scheduler.step()
        print(f"Epoch {epoch}: Loss = {total_loss / len(train_loader):.4f}")
    
    return model


def finetune_task(model, task_loader, task_id, epochs=20, lr=1e-5):
    """
    Task-specific fine-tuning with prompt tuning
    """
    # Freeze backbone, only train prompts and head
    for param in model.parameters():
        param.requires_grad = False
    
    model.task_prompts.requires_grad = True
    model.head.requires_grad = True
    
    optimizer = optim.Adam([
        {'params': model.task_prompts, 'lr': lr * 10},
        {'params': model.head.parameters(), 'lr': lr}
    ])
    
    criterion = nn.CrossEntropyLoss()
    
    for epoch in range(epochs):
        model.train()
        for batch in task_loader:
            fmri = batch['fmri']
            labels = batch['label']
            
            logits = model(fmri, task_id=task_id)
            loss = criterion(logits, labels)
            
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()
        
        # Evaluate
        acc = evaluate(model, task_loader, task_id)
        print(f"Task {task_id}, Epoch {epoch}: Acc = {acc:.4f}")
    
    return model


def evaluate(model, loader, task_id):
    """Evaluate model on task"""
    model.eval()
    correct = 0
    total = 0
    
    with torch.no_grad():
        for batch in loader:
            fmri = batch['fmri']
            labels = batch['label']
            
            logits = model(fmri, task_id=task_id)
            preds = logits.argmax(dim=-1)
            
            correct += (preds == labels).sum().item()
            total += labels.size(0)
    
    return correct / total
```

## Applications

### 1. Age and Gender Prediction

```python
def predict_demographics(model, fmri_scan):
    """Predict age and gender from rsfMRI"""
    # Task 0: Age prediction (regression)
    age_pred = model(fmri_scan, task_id=0)
    
    # Task 1: Gender classification
    gender_logits = model(fmri_scan, task_id=1)
    gender_pred = gender_logits.argmax(dim=-1)
    
    return age_pred, gender_pred
```

### 2. Disease Diagnosis

```python
def diagnose_condition(model, fmri_scan, condition_type='alzheimer'):
    """Diagnose neurological conditions"""
    task_mapping = {
        'alzheimer': 2,
        'parkinson': 3,
        'depression': 4,
        'autism': 5
    }
    
    task_id = task_mapping.get(condition_type, 2)
    logits = model(fmri_scan, task_id=task_id)
    probabilities = F.softmax(logits, dim=-1)
    
    return probabilities
```

### 3. fMRI-to-Image Retrieval

```python
def fmri_image_retrieval(model, fmri_scan, image_database):
    """
    Retrieve matching images from fMRI activity patterns
    Cross-modal retrieval task
    """
    # Extract fMRI features
    fmri_features = model(fmri_scan, task_id=6, return_features=True)
    
    # Compare with image database
    similarities = cosine_similarity(fmri_features, image_database.features)
    
    # Return top-k matches
    top_k = similarities.topk(k=5)
    return image_database[top_k.indices]
```

## Benchmarks

| Task | Metric | NeuroSTORM | Previous SOTA |
|------|--------|------------|---------------|
| Age Prediction | MAE (years) | 3.2 | 4.5 |
| Gender Classification | Accuracy | 94.8% | 91.2% |
| Disease Diagnosis (17 types) | AUC | 0.89 | 0.82 |
| fMRI-to-Image Retrieval | R@10 | 78.5% | 71.3% |
| Task fMRI State Classification | Accuracy | 87.2% | 82.1% |

## Clinical Validation

NeuroSTORM evaluated on clinical datasets from:
- United States: Mass General Brigham
- South Korea: Yonsei University
- Australia: University of Sydney

**17 Different Diagnoses Covered**:
- Alzheimer's Disease
- Parkinson's Disease
- Major Depressive Disorder
- Autism Spectrum Disorder
- Schizophrenia
- ADHD
- Epilepsy
- And 10 others

## Pitfalls

- **Data Preprocessing**: Requires careful standardization across scanners and protocols
- **Computational Requirements**: Large-scale pre-training needs significant GPU resources
- **Temporal Resolution**: Assumes consistent TR (repetition time) across datasets
- **Age Range**: Performance may vary at extremes of age range (<5 or >100 years)
- **Site Effects**: Despite efforts to standardize, multi-site data may retain residual scanner effects
- **Prompt Tuning Limitations**: May not capture highly specialized tasks without full fine-tuning

## Related Skills

- brain-dit-fmri-foundation-model
- neural-dynamics-universal-translator-foundation
- reve-eeg-foundation
- brain-foundation-model-batch-effects
- meta-learning-in-context-brain-decoding

## References

```bibtex
@article{wang2025neurostorm,
  title={Towards a general-purpose foundation model for fMRI analysis},
  author={Wang, Cheng and Jiang, Yu and Peng, Zhihao and Li, Chenxin and Bang, Changbae and Zhao, Lin and Lv, Jinglei and Sepulcre, Jorge and Yang, Carl and He, Lifang and Liu, Tianming and Barron, Daniel and Li, Quanzheng and Hirschtick, Randy and Kim, Byung-Hoon and Li, Xiang and Yuan, Yixuan},
  journal={arXiv preprint arXiv:2506.11167},
  year={2025}
}
```
