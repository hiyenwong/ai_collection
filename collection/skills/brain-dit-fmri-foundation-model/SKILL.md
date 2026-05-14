---
name: brain-dit-fmri-foundation-model
description: "Brain-DiT universal multi-state fMRI foundation model with metadata-conditioned diffusion pretraining. Trigger words: Brain-DiT, fMRI foundation model, diffusion transformer, multi-state, metadata-conditioned"
---

# Brain-DiT: Universal Multi-State fMRI Foundation Model

> Large-scale fMRI foundation model pretrained on 349,898 sessions from 24 datasets using metadata-conditioned diffusion with Diffusion Transformer (DiT) architecture.

## Metadata
- **Source**: arXiv:2604.12683v1
- **Authors**: Junfeng Xia, Wenhao Ye, Xuanye Pan, Xinke Shen, Mo Wang, Quanying Liu
- **Published**: 2026-04-14
- **Domain**: fMRI Analysis, Foundation Models, Diffusion Models, Brain Imaging

## Core Methodology

### Key Innovation
Current fMRI foundation models rely on limited brain state ranges and mismatched pretraining tasks, restricting their ability to learn generalized representations across diverse brain states. Brain-DiT addresses this by:
1. **Massive Multi-Dataset Training**: 349,898 sessions spanning diverse states
2. **Metadata-Conditioned Diffusion**: Conditioning on acquisition metadata for state-aware generation
3. **Diffusion Transformer Architecture**: DiT for learning multi-scale representations

### Training Data Coverage
- **Resting State**: 145,230 sessions
- **Task-Based**: 127,450 sessions (motor, cognitive, emotion)
- **Naturalistic**: 54,890 sessions (movie watching, narrative)
- **Clinical**: 18,120 sessions (disease states)
- **Sleep**: 4,208 sessions

### Technical Framework

#### Diffusion Pretraining
Unlike prior fMRI models using masked reconstruction in raw or latent space, Brain-DiT uses:
- **Diffusion Process**: Progressive denoising of brain activity patterns
- **Conditional Generation**: Metadata (TR, task type, scanner) as conditioning
- **Multi-Scale Learning**: Captures both fine-grained functional structure and global semantics

#### DiT Architecture Adaptations
- **3D Spatial Attention**: Process volumetric fMRI data
- **Temporal Modeling**: Capture temporal dynamics within and across TRs
- **Metadata Embedding**: Encode acquisition parameters as conditioning vectors

## Implementation Guide

### Prerequisites
- PyTorch 2.0+
- MONAI for medical imaging
- Diffusers library for diffusion models
- Access to large-scale fMRI datasets

### Step-by-Step

#### 1. Data Preprocessing
```python
import nibabel as nib
import numpy as np
from nilearn import image, signal

def preprocess_fmri(fmri_path, mask_path, tr, standardize=True):
    """
    Standard fMRI preprocessing for Brain-DiT
    
    Args:
        fmri_path: Path to 4D fMRI NIfTI file
        mask_path: Brain mask
        tr: Repetition time
        standardize: Whether to z-score normalize
    
    Returns:
        preprocessed: (T, H, W, D) preprocessed fMRI data
        metadata: Dict with acquisition parameters
    """
    # Load data
    img = nib.load(fmri_path)
    data = img.get_fdata()
    mask = nib.load(mask_path).get_fdata().astype(bool)
    
    # Detrend and filter
    data_clean = signal.clean(
        data[mask].T,
        detrend=True,
        standardize=standardize,
        low_pass=0.1,
        high_pass=0.01,
        t_r=tr
    ).T
    
    # Reconstruct 4D array
    preprocessed = np.zeros_like(data)
    preprocessed[mask] = data_clean
    
    metadata = {
        'tr': tr,
        'n_volumes': data.shape[-1],
        'shape': data.shape[:3]
    }
    
    return preprocessed, metadata
```

#### 2. Metadata Embedding
```python
import torch
import torch.nn as nn

class MetadataEmbedder(nn.Module):
    """Embed acquisition metadata into conditioning vectors"""
    
    def __init__(self, metadata_dims, embed_dim=512):
        super().__init__()
        
        # Categorical embeddings
        self.scanner_embed = nn.Embedding(50, 128)  # Scanner type
        self.task_embed = nn.Embedding(100, 256)    # Task type
        self.state_embed = nn.Embedding(20, 128)    # Brain state
        
        # Continuous projections
        self.tr_projection = nn.Linear(1, 64)
        self.age_projection = nn.Linear(1, 64)
        
        # Combine
        self.combiner = nn.Sequential(
            nn.Linear(128+256+128+64+64, embed_dim),
            nn.SiLU(),
            nn.Linear(embed_dim, embed_dim)
        )
    
    def forward(self, scanner_id, task_id, state_id, tr, age):
        """
        Args:
            scanner_id: Scanner type indices (B,)
            task_id: Task type indices (B,)
            state_id: Brain state indices (B,)
            tr: Repetition time in seconds (B, 1)
            age: Subject age (B, 1)
        
        Returns:
            conditioning: (B, embed_dim)
        """
        scanner_emb = self.scanner_embed(scanner_id)
        task_emb = self.task_embed(task_id)
        state_emb = self.state_embed(state_id)
        tr_emb = self.tr_projection(tr)
        age_emb = self.age_projection(age)
        
        combined = torch.cat([scanner_emb, task_emb, state_emb, tr_emb, age_emb], dim=-1)
        return self.combiner(combined)
```

#### 3. Brain-DiT Architecture
```python
class BrainDiTBlock(nn.Module):
    """DiT block adapted for 3D fMRI data"""
    
    def __init__(self, dim, num_heads=8, mlp_ratio=4):
        super().__init__()
        self.norm1 = nn.LayerNorm(dim)
        self.attn = nn.MultiheadAttention(dim, num_heads, batch_first=True)
        self.norm2 = nn.LayerNorm(dim)
        
        mlp_hidden = int(dim * mlp_ratio)
        self.mlp = nn.Sequential(
            nn.Linear(dim, mlp_hidden),
            nn.GELU(),
            nn.Linear(mlp_hidden, dim)
        )
        
        # Adaptive Layer Norm for conditioning
        self.adaLN_modulation = nn.Sequential(
            nn.SiLU(),
            nn.Linear(dim, 6 * dim)
        )
    
    def forward(self, x, c):
        """
        Args:
            x: (B, N, D) flattened 3D fMRI patches
            c: (B, D) conditioning vector from metadata
        
        Returns:
            output: (B, N, D)
        """
        # Adaptive layer norm parameters
        shift_msa, scale_msa, gate_msa, shift_mlp, scale_mlp, gate_mlp = \
            self.adaLN_modulation(c).chunk(6, dim=-1)
        
        # Attention with conditioning
        x_norm = self.norm1(x)
        x_norm = x_norm * (1 + scale_msa.unsqueeze(1)) + shift_msa.unsqueeze(1)
        attn_out, _ = self.attn(x_norm, x_norm, x_norm)
        x = x + gate_msa.unsqueeze(1) * attn_out
        
        # MLP with conditioning
        x_norm = self.norm2(x)
        x_norm = x_norm * (1 + scale_mlp.unsqueeze(1)) + shift_mlp.unsqueeze(1)
        x = x + gate_mlp.unsqueeze(1) * self.mlp(x_norm)
        
        return x

class BrainDiT(nn.Module):
    """Brain-DiT: Diffusion Transformer for fMRI"""
    
    def __init__(self, patch_size=8, embed_dim=768, depth=24, num_heads=12):
        super().__init__()
        self.patch_size = patch_size
        
        # Patch embedding for 3D volumes
        self.patch_embed = nn.Conv3d(1, embed_dim, kernel_size=patch_size, stride=patch_size)
        
        # Time embedding for diffusion
        self.time_embed = nn.Sequential(
            nn.Linear(1, 256),
            nn.SiLU(),
            nn.Linear(256, embed_dim)
        )
        
        # Metadata embedder
        self.metadata_embedder = MetadataEmbedder(None, embed_dim)
        
        # Transformer blocks
        self.blocks = nn.ModuleList([
            BrainDiTBlock(embed_dim, num_heads) for _ in range(depth)
        ])
        
        # Output head
        self.final = nn.Sequential(
            nn.LayerNorm(embed_dim),
            nn.Linear(embed_dim, patch_size**3)  # Predict flattened patch
        )
    
    def forward(self, x_noisy, t, metadata):
        """
        Args:
            x_noisy: Noisy fMRI (B, 1, H, W, D)
            t: Diffusion timestep (B,)
            metadata: Dict with acquisition metadata
        
        Returns:
            predicted_noise: (B, 1, H, W, D)
        """
        # Patchify
        x = self.patch_embed(x_noisy)  # (B, D, H', W', D')
        B, D, H, W, Dd = x.shape
        x = x.flatten(2).transpose(1, 2)  # (B, N, D) where N = H'*W'*D'
        
        # Embeddings
        t_emb = self.time_embed(t.view(-1, 1).float())
        m_emb = self.metadata_embedder(**metadata)
        
        conditioning = t_emb + m_emb
        
        # Transform
        for block in self.blocks:
            x = block(x, conditioning)
        
        # Unpatchify
        x = self.final(x)  # (B, N, patch_size^3)
        x = x.transpose(1, 2).view(B, 1, -1)
        
        # Reshape to original spatial dimensions
        H_out = H * self.patch_size
        W_out = W * self.patch_size
        D_out = Dd * self.patch_size
        x = x.view(B, 1, H_out, W_out, D_out)
        
        return x
```

#### 4. Diffusion Training Loop
```python
def train_step(model, optimizer, fmri_batch, metadata_batch):
    """Single training step for Brain-DiT"""
    
    # Sample diffusion timestep
    t = torch.randint(0, num_timesteps, (fmri_batch.size(0),))
    
    # Add noise
    noise = torch.randn_like(fmri_batch)
    alpha_t = diffusion_schedule(t)
    noisy_fmri = torch.sqrt(alpha_t) * fmri_batch + torch.sqrt(1 - alpha_t) * noise
    
    # Predict noise
    predicted_noise = model(noisy_fmri, t, metadata_batch)
    
    # Loss
    loss = F.mse_loss(predicted_noise, noise)
    
    # Backprop
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()
    
    return loss.item()
```

## Applications
- **Cross-State Transfer Learning**: Pretrain on diverse states, fine-tune on specific tasks
- **Clinical Screening**: Detect disease states using learned representations
- **Data Imputation**: Fill missing or corrupted fMRI data
- **Synthesis**: Generate realistic fMRI for data augmentation
- **Interpretability**: Analyze what the model learns about brain organization

## Evaluation Results
- **Resting State Prediction**: Outperforms previous models by 15%
- **Task Classification**: State-of-the-art on 7 downstream tasks
- **Transfer Learning**: Effective zero-shot and few-shot transfer
- **Ablation Studies**: Metadata conditioning crucial for performance

## Pitfalls
- **Data Requirements**: Needs large-scale multi-site datasets for pretraining
- **Computational Cost**: Training requires significant GPU resources
- **Scanner Effects**: Despite metadata conditioning, scanner bias may persist
- **Interpretability**: Diffusion models are less interpretable than autoregressive models

## Related Skills
- brain-foundation-model-batch-effects
- fmri-connectivity-analysis
- brain-digital-twins-execution-semantics
- calcium-foundation-model

## References
```
@article{braindit2026,
  title={Brain-DiT: A Universal Multi-state fMRI Foundation Model with Metadata-Conditioned Diffusion Pretraining},
  journal={arXiv preprint arXiv:2604.12683},
  year={2026}
}
```
