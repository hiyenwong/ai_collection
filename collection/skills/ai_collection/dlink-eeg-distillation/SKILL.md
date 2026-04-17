---
name: dlink-eeg-distillation
category: ai_collection
tags:
  - knowledge-distillation
  - diffusion-models
  - eeg-decoding
  - visual-reconstruction
  - layer-wise-knowledge
  - dominant-knowledge
  - brain-computer-interface
  - neuroscience
  - generative-models
description: >
  DLink: Distilling Layer-wise and Dominant Knowledge from Diffusion Models for Enhanced EEG Decoding — layer-wise and dominant knowledge extraction from diffusion models to enhance EEG-to-visual reconstruction.
paper:
  title: "DLink: Distilling Layer-wise and Dominant Knowledge from Diffusion Models for Enhanced EEG Decoding"
  arxiv: "2604.12572"
  date: 2026-04-15
---

# DLink: Distilling Layer-wise and Dominant Knowledge from Diffusion Models for Enhanced EEG Decoding

## Overview

This skill covers the **DLink** method — a knowledge distillation framework that transfers layer-wise and dominant knowledge from pre-trained diffusion models into EEG decoding networks to significantly enhance EEG-based visual reconstruction. By leveraging the rich visual priors encoded in diffusion models (e.g., Stable Diffusion), DLink bridges the massive gap between sparse, noisy neural signals and high-fidelity visual outputs.

## Why Distill Diffusion Knowledge into EEG Decoders?

| Challenge in EEG Decoding | How DLink Addresses It |
|---|---|
| Sparse, low-SNR EEG signals with limited information | Diffusion models provide rich visual priors to fill in missing details |
| Large modality gap between neural activity and visual space | Layer-wise distillation creates structured knowledge bridges at multiple abstraction levels |
| Overfitting due to small EEG datasets | Knowledge distillation acts as a powerful regularizer |
| Blurry, low-fidelity reconstructions | Dominant knowledge preserves the most salient visual features |
| No temporal consistency in frame-by-frame reconstruction | Diffusion model's learned dynamics provide coherent reconstruction priors |

## Core Methodology

### 1. Problem Formulation

Given:
- **Teacher**: Pre-trained diffusion model (e.g., Stable Diffusion UNet) with frozen weights
- **Student**: EEG-to-visual decoder trained on paired EEG-image data
- **Goal**: Transfer the visual generation knowledge from the diffusion model to the EEG decoder via knowledge distillation

```
EEG Signal → EEG Encoder → Latent → DLink Decoder → Reconstructed Image
                              ↓
                    Layer-wise Distillation Loss
                              ↓
              Diffusion UNet (Frozen Teacher) → Visual Priors
```

### 2. Architecture Design

#### 2a. Teacher Network: Diffusion Model

A pre-trained diffusion model serves as the knowledge source. The UNet architecture contains rich hierarchical representations:

```
┌─────────────────────────────────────────────────────────────────┐
│              DIFFUSION UNET (TEACHER — FROZEN)                   │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  Input x_t → [Encoder Block 1]  →  Feature Map F_1 (high-res)  │
│                   ↓                                              │
│              [Encoder Block 2]  →  Feature Map F_2              │
│                   ↓                                              │
│              [Encoder Block 3]  →  Feature Map F_3              │
│                   ↓                                              │
│              [Middle Block]     →  Feature Map F_mid (semantic)  │
│                   ↓                                              │
│              [Decoder Block 1]  →  Feature Map F_4              │
│                   ↓                                              │
│              [Decoder Block 2]  →  Feature Map F_5              │
│                   ↓                                              │
│              [Decoder Block 3]  →  Feature Map F_6 (fine detail) │
│                   ↓                                              │
│              Output → ε-prediction / x_0-prediction             │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

Each layer captures different levels of visual knowledge:
- **Early layers**: Low-level features (edges, textures, gradients)
- **Middle layers**: Mid-level features (shapes, parts, object fragments)
- **Late layers**: High-level features (semantic concepts, object identity, scene layout)
- **Decoder layers**: Fine details and spatial refinement

#### 2b. Student Network: EEG Decoder

```
┌─────────────────────────────────────────────────────────────────┐
│                  EEG DECODER (STUDENT)                           │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  Raw EEG  →  Preprocessing  →  EEG Encoder (Temporal Conv/Transformer) │
│                                      ↓                           │
│                              Latent Representation Z_eeg         │
│                                      ↓                           │
│                        ┌───────────────────────────┐             │
│                        │     DLink Decoder Blocks   │             │
│                        │                           │             │
│                        │  [DLink Block 1] → S_1 ───┼───┐        │
│                        │       ↓                   │   │        │
│                        │  [DLink Block 2] → S_2 ───┼───┤        │
│                        │       ↓                   │   │        │
│                        │  [DLink Block 3] → S_3 ───┼───┤        │
│                        │       ↓                   │   │        │
│                        │  [DLink Block 4] → S_4 ───┼───┤        │
│                        │       ↓                   │   │        │
│                        │  [DLink Block 5] → S_5 ───┼───┤        │
│                        │       ↓                   │   │        │
│                        │  [DLink Block 6] → S_6 ───┼───┘        │
│                        └───────────────────────────┘             │
│                                      ↓                           │
│                        Latent Space → VAE Decoder → Image       │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

Each student block `S_i` produces feature maps aligned with teacher features `F_i`.

### 3. Layer-Wise Knowledge Distillation

#### 3a. Multi-Level Feature Alignment

Knowledge is distilled at multiple layers simultaneously, capturing visual information at different abstraction levels:

```python
import torch
import torch.nn as nn
import torch.nn.functional as F

class LayerWiseDistillation(nn.Module):
    """Layer-wise knowledge distillation from diffusion model to EEG decoder."""
    
    def __init__(self, teacher_feature_dims, student_feature_dims, 
                 layer_weights=None, alignment='linear'):
        super().__init__()
        self.n_layers = len(teacher_feature_dims)
        self.layer_weights = layer_weights or [1.0] * self.n_layers
        self.alignment = alignment
        
        # Projection layers to align student and teacher feature spaces
        self.projections = nn.ModuleList([
            nn.Sequential(
                nn.Linear(student_dim, teacher_dim),
                nn.LayerNorm(teacher_dim),
                nn.ReLU(inplace=True),
                nn.Linear(teacher_dim, teacher_dim),
            )
            for student_dim, teacher_dim in zip(student_feature_dims, teacher_feature_dims)
        ])
        
    def forward(self, student_features, teacher_features, mask=None):
        """
        Compute layer-wise distillation loss.
        
        Args:
            student_features: List of student feature maps [S_1, ..., S_n]
            teacher_features: List of teacher feature maps [F_1, ..., F_n]
            mask: Optional attention mask for spatial weighting
        
        Returns:
            Total distillation loss
        """
        total_loss = 0.0
        layer_losses = []
        
        for i in range(self.n_layers):
            S_i = student_features[i]  # [B, C_s, H, W]
            F_i = teacher_features[i]  # [B, C_t, H', W']
            
            # Spatial alignment (adaptive pooling if spatial dims differ)
            if S_i.shape[-2:] != F_i.shape[-2:]:
                S_i = F.adaptive_avg_pool2d(S_i, F_i.shape[-2:])
            
            # Channel projection
            B, C_s, H, W = S_i.shape
            S_i_proj = self.projections[i](S_i.permute(0, 2, 3, 1).reshape(B, H*W, C_s))
            S_i_proj = S_i_proj.reshape(B, H, W, -1).permute(0, 3, 1, 2)
            
            # Compute distillation loss for this layer
            if self.alignment == 'linear':
                loss_i = F.mse_loss(S_i_proj, F_i.detach())
            elif self.alignment == 'cosine':
                S_i_flat = S_i_proj.flatten(2)
                F_i_flat = F_i.flatten(2).detach()
                loss_i = 1 - F.cosine_similarity(S_i_flat, F_i_flat, dim=1).mean()
            elif self.alignment == 'attn_mse':
                # Attention-weighted MSE
                attn = F.softmax(F_i.flatten(2).detach(), dim=-1)
                loss_i = (attn * (S_i_proj.flatten(2) - F_i.detach().flatten(2))**2).sum()
            
            total_loss += self.layer_weights[i] * loss_i
            layer_losses.append(loss_i.item())
            
        return total_loss, layer_losses
```

#### 3b. Hierarchical Feature Mapping

Map student layers to teacher layers based on semantic similarity:

```python
def map_student_to_teacher_layers(student_arch, teacher_arch):
    """
    Create a mapping between student and teacher layers based on abstraction level.
    
    Strategy: Early student layers → Early teacher layers (low-level features)
              Middle student layers → Middle teacher layers (mid-level features)
              Late student layers → Late teacher layers (high-level features)
    """
    mapping = {}
    
    # Student layers (EEG decoder progression)
    student_layers = [
        'eeg_temporal',      # Temporal EEG features
        'eeg_spatial',       # Spatial EEG features  
        'latent_projection', # Project to visual latent space
        'decoder_stage_1',   # Coarse structure
        'decoder_stage_2',   # Mid-level features
        'decoder_stage_3',   # Fine details
    ]
    
    # Teacher layers (Diffusion UNet progression)
    teacher_layers = [
        'encoder_block_1',   # Edges, textures
        'encoder_block_2',   # Local patterns
        'encoder_block_3',   # Shapes, parts
        'middle_block',      # Semantic concepts
        'decoder_block_1',   # Object refinement
        'decoder_block_2',   # Fine detail synthesis
        'decoder_block_3',   # Pixel-level features
    ]
    
    # Create optimal mapping
    for i, s_layer in enumerate(student_layers):
        # Map proportionally, but bias toward semantic alignment
        t_idx = min(i * len(teacher_layers) // len(student_layers), len(teacher_layers) - 1)
        mapping[s_layer] = teacher_layers[t_idx]
    
    return mapping
```

### 4. Dominant Knowledge Preservation

#### 4a. What is Dominant Knowledge?

Dominant knowledge refers to the most salient, high-impact features in the diffusion model's representation — features that are most critical for accurate visual reconstruction. This includes:

- **Object identity** features (what is in the image)
- **Scene layout** features (spatial arrangement)
- **Dominant color/texture** patterns
- **Semantic consistency** features

#### 4b. Dominant Knowledge Extraction

```python
class DominantKnowledgeExtractor(nn.Module):
    """Extract and preserve dominant knowledge from diffusion model features."""
    
    def __init__(self, feature_dim, top_k_ratio=0.3, aggregation='attention'):
        super().__init__()
        self.top_k_ratio = top_k_ratio
        self.aggregation = aggregation
        
        # Attention mechanism to identify dominant channels/features
        self.channel_attention = nn.Sequential(
            nn.AdaptiveAvgPool2d(1),
            nn.Conv2d(feature_dim, feature_dim // 4, 1),
            nn.ReLU(inplace=True),
            nn.Conv2d(feature_dim // 4, feature_dim, 1),
            nn.Sigmoid()
        )
        
        # Spatial attention for dominant regions
        self.spatial_attention = nn.Sequential(
            nn.Conv2d(feature_dim, 1, 3, padding=1),
            nn.Sigmoid()
        )
        
    def extract_dominant_features(self, features):
        """
        Extract dominant features using attention-guided selection.
        
        Args:
            features: [B, C, H, W] feature map from diffusion model
        
        Returns:
            dominant_features: Selected dominant features
            attention_mask: Spatial+channel attention weights
        """
        B, C, H, W = features.shape
        
        # Channel-wise importance
        channel_attn = self.channel_attention(features)  # [B, C, 1, 1]
        
        # Spatial importance
        spatial_attn = self.spatial_attention(features)  # [B, 1, H, W]
        
        # Combined attention
        combined_attn = channel_attn * spatial_attn  # [B, C, H, W]
        
        # Select top-k dominant features
        top_k = int(C * H * W * self.top_k_ratio)
        flat_attn = combined_attn.flatten(1)
        top_values, top_indices = torch.topk(flat_attn, top_k, dim=-1)
        
        # Create mask
        mask = torch.zeros_like(flat_attn)
        mask.scatter_(1, top_indices, 1.0)
        mask = mask.view_as(combined_attn)
        
        # Extract dominant features
        dominant_features = features * mask
        
        return dominant_features, combined_attn
    
    def forward(self, student_features, teacher_features):
        """
        Compute dominant knowledge distillation loss.
        Student is strongly penalized for missing dominant teacher features.
        """
        dominant_teacher, teacher_attn = self.extract_dominant_features(teacher_features.detach())
        dominant_student, student_attn = self.extract_dominant_features(student_features)
        
        # Dominant feature alignment loss (higher weight for dominant features)
        dominant_loss = F.mse_loss(dominant_student, dominant_teacher)
        
        # Attention consistency loss
        attn_loss = F.mse_loss(student_attn, teacher_attn)
        
        return dominant_loss, attn_loss, teacher_attn
```

#### 4c. Multi-Stage Dominant Distillation

```python
class MultiStageDominantDistillation(nn.Module):
    """Apply dominant knowledge distillation across multiple abstraction stages."""
    
    def __init__(self, stage_configs):
        """
        Args:
            stage_configs: List of dicts with:
                - name: Stage identifier
                - feature_dim: Teacher feature dimension
                - student_dim: Student feature dimension
                - top_k_ratio: Ratio of dominant features to preserve
                - weight: Distillation loss weight for this stage
        """
        super().__init__()
        self.stages = nn.ModuleDict()
        self.weights = {}
        
        for config in stage_configs:
            self.stages[config['name']] = DominantKnowledgeExtractor(
                feature_dim=config['feature_dim'],
                top_k_ratio=config['top_k_ratio'],
            )
            self.weights[config['name']] = config['weight']
            
    def forward(self, student_features_dict, teacher_features_dict):
        """
        Compute multi-stage dominant distillation loss.
        
        Args:
            student_features_dict: {stage_name: student_features}
            teacher_features_dict: {stage_name: teacher_features}
        
        Returns:
            Total weighted loss, per-stage losses
        """
        total_loss = 0.0
        stage_losses = {}
        attention_maps = {}
        
        for stage_name in self.stages:
            if stage_name in student_features_dict and stage_name in teacher_features_dict:
                S = student_features_dict[stage_name]
                T = teacher_features_dict[stage_name]
                
                d_loss, a_loss, attn = self.stages[stage_name](S, T)
                weighted_loss = self.weights[stage_name] * (d_loss + 0.5 * a_loss)
                
                total_loss += weighted_loss
                stage_losses[stage_name] = {
                    'dominant': d_loss.item(),
                    'attention': a_loss.item(),
                    'weighted': weighted_loss.item()
                }
                attention_maps[stage_name] = attn
                
        return total_loss, stage_losses, attention_maps
```

### 5. Combined Distillation Objective

The total training objective combines multiple distillation signals:

```
L_total = α · L_reconstruction + β · L_layer_wise + γ · L_dominant + δ · L_consistency
```

```python
class DLinkDistillationLoss(nn.Module):
    """Combined distillation loss for DLink training."""
    
    def __init__(self, config):
        super().__init__()
        self.alpha = config.get('alpha', 1.0)    # Reconstruction weight
        self.beta = config.get('beta', 0.5)       # Layer-wise distillation weight
        self.gamma = config.get('gamma', 0.3)     # Dominant knowledge weight
        self.delta = config.get('delta', 0.1)     # Consistency weight
        
        self.layer_distillation = LayerWiseDistillation(
            teacher_feature_dims=config['teacher_dims'],
            student_feature_dims=config['student_dims'],
            layer_weights=config.get('layer_weights'),
            alignment=config.get('alignment', 'linear')
        )
        
        self.dominant_distillation = MultiStageDominantDistillation(
            stage_configs=config['stage_configs']
        )
        
    def forward(self, student_output, student_features, teacher_features, 
                target_image, student_features_prev=None):
        """
        Compute full DLink distillation loss.
        
        Args:
            student_output: Reconstructed image from EEG decoder
            student_features: Dict of student feature maps per stage
            teacher_features: Dict of teacher (diffusion) feature maps
            target_image: Ground truth image
            student_features_prev: Previous step features (for consistency)
        
        Returns:
            Loss dict with individual components
        """
        losses = {}
        
        # 1. Reconstruction loss
        losses['reconstruction'] = F.mse_loss(student_output, target_image)
        
        # 2. Layer-wise distillation
        layer_loss, layer_details = self.layer_distillation(
            [student_features[k] for k in sorted(student_features.keys())],
            [teacher_features[k] for k in sorted(teacher_features.keys())]
        )
        losses['layer_wise'] = layer_loss
        
        # 3. Dominant knowledge distillation
        dom_loss, dom_details, attn_maps = self.dominant_distillation(
            student_features, teacher_features
        )
        losses['dominant'] = dom_loss
        
        # 4. Temporal consistency (for video/sequence EEG)
        if student_features_prev is not None:
            consistency_loss = 0.0
            for key in student_features:
                if key in student_features_prev:
                    consistency_loss += F.mse_loss(
                        student_features[key], 
                        student_features_prev[key].detach()
                    )
            losses['consistency'] = consistency_loss
        else:
            losses['consistency'] = torch.tensor(0.0, device=student_output.device)
        
        # Total weighted loss
        total_loss = (
            self.alpha * losses['reconstruction'] +
            self.beta * losses['layer_wise'] +
            self.gamma * losses['dominant'] +
            self.delta * losses['consistency']
        )
        
        losses['total'] = total_loss
        return losses
```

## Implementation Patterns

### Pattern 1: Feature Hook Registration

Extract intermediate features from the frozen diffusion model using PyTorch hooks:

```python
class FeatureHook:
    """Hook to capture intermediate layer features from the teacher model."""
    
    def __init__(self, model, layer_names):
        self.hooks = []
        self.features = {}
        
        # Register hooks on specified layers
        for name in layer_names:
            layer = self._get_layer_by_name(model, name)
            if layer is not None:
                hook = layer.register_forward_hook(
                    self._create_hook_fn(name)
                )
                self.hooks.append(hook)
    
    def _get_layer_by_name(self, model, name):
        """Navigate model structure to find layer by dotted name."""
        parts = name.split('.')
        module = model
        for part in parts:
            if hasattr(module, part):
                module = getattr(module, part)
            else:
                return None
        return module
    
    def _create_hook_fn(self, name):
        def hook_fn(module, input, output):
            self.features[name] = output
        return hook_fn
    
    def clear(self):
        self.features.clear()
    
    def remove(self):
        for hook in self.hooks:
            hook.remove()
        self.hooks.clear()


# Usage with Stable Diffusion UNet
def register_teacher_hooks(unet, target_layers=None):
    """Register hooks on key diffusion model layers for knowledge extraction."""
    if target_layers is None:
        target_layers = [
            'down_blocks.0.attentions.0',    # Early: edges/textures
            'down_blocks.1.attentions.0',    # Low-mid: local patterns
            'down_blocks.2.attentions.0',    # Mid: shapes/parts
            'mid_block.attentions.0',         # High: semantic concepts
            'up_blocks.1.attentions.0',      # Mid-high: object refinement
            'up_blocks.2.attentions.0',      # Late: fine details
        ]
    
    hook = FeatureHook(unet, target_layers)
    return hook
```

### Pattern 2: EEG Encoder with DLink Decoder

```python
class EEGEncoder(nn.Module):
    """Encodes multi-channel EEG into compact latent representations."""
    
    def __init__(self, n_channels=64, n_timepoints=512, latent_dim=768):
        super().__init__()
        
        # Temporal encoding
        self.temporal_conv = nn.Sequential(
            nn.Conv1d(n_channels, 256, kernel_size=3, padding=1),
            nn.BatchNorm1d(256),
            nn.GELU(),
            nn.Conv1d(256, 512, kernel_size=3, padding=1),
            nn.BatchNorm1d(512),
            nn.GELU(),
            nn.AdaptiveAvgPool1d(64),
        )
        
        # Spatial-temporal transformer
        encoder_layer = nn.TransformerEncoderLayer(
            d_model=512, nhead=8, dim_feedforward=2048,
            batch_first=True, norm_first=True
        )
        self.transformer = nn.TransformerEncoder(encoder_layer, num_layers=4)
        
        # Projection to visual latent space
        self.projection = nn.Sequential(
            nn.Linear(512, latent_dim),
            nn.LayerNorm(latent_dim),
            nn.GELU(),
        )
        
    def forward(self, eeg):
        """
        Args:
            eeg: [B, n_channels, n_timepoints]
        Returns:
            latent: [B, n_patches, latent_dim]
        """
        # Temporal features: [B, 512, 64]
        temporal = self.temporal_conv(eeg)
        temporal = temporal.permute(0, 2, 1)  # [B, 64, 512]
        
        # Transformer encoding
        encoded = self.transformer(temporal)  # [B, 64, 512]
        
        # Project to latent space
        latent = self.projection(encoded)  # [B, 64, 768]
        return latent


class DLinkDecoderBlock(nn.Module):
    """Single decoder block with distillation capability."""
    
    def __init__(self, in_dim, out_dim, spatial_res):
        super().__init__()
        self.spatial_res = spatial_res
        
        self.conv = nn.Sequential(
            nn.Conv2d(in_dim, out_dim, kernel_size=3, padding=1),
            nn.GroupNorm(32, out_dim),
            nn.SiLU(),
            nn.Conv2d(out_dim, out_dim, kernel_size=3, padding=1),
            nn.GroupNorm(32, out_dim),
            nn.SiLU(),
        )
        
        # Self-attention for long-range dependencies
        self.attn = nn.MultiheadAttention(
            embed_dim=out_dim, num_heads=8, batch_first=True
        )
        self.norm = nn.LayerNorm(out_dim)
        
    def forward(self, x):
        B, C, H, W = x.shape
        
        # Conv processing
        out = self.conv(x)
        
        # Self-attention (flatten spatial dims)
        out_flat = out.flatten(2).permute(0, 2, 1)
        attn_out, _ = self.attn(out_flat, out_flat, out_flat)
        attn_out = self.norm(attn_out)
        
        # Reshape back
        out = attn_out.permute(0, 2, 1).reshape(B, -1, H, W)
        return out


class DLinkDecoder(nn.Module):
    """Full EEG-to-image decoder with layer-wise distillation outputs."""
    
    def __init__(self, latent_dim=768, vae_latent_dim=4):
        super().__init__()
        
        # Initial projection from EEG latent to feature map
        self.initial = nn.Sequential(
            nn.Linear(latent_dim, 512 * 4 * 4),
            nn.Unflatten(1, (512, 4, 4)),
        )
        
        # Decoder stages with increasing resolution
        self.stage1 = DLinkDecoderBlock(512, 512, 4)
        self.up1 = nn.ConvTranspose2d(512, 256, 2, stride=2)  # 4→8
        
        self.stage2 = DLinkDecoderBlock(256, 256, 8)
        self.up2 = nn.ConvTranspose2d(256, 128, 2, stride=2)  # 8→16
        
        self.stage3 = DLinkDecoderBlock(128, 128, 16)
        self.up3 = nn.ConvTranspose2d(128, 64, 2, stride=2)   # 16→32
        
        self.stage4 = DLinkDecoderBlock(64, 64, 32)
        self.up4 = nn.ConvTranspose2d(64, vae_latent_dim, 2, stride=2)  # 32→64
        
        self.output_norm = nn.GroupNorm(32, vae_latent_dim)
        
    def forward(self, latent):
        """
        Returns both output and intermediate features for distillation.
        
        Args:
            latent: [B, n_patches, latent_dim] from EEG encoder
        
        Returns:
            output: [B, vae_latent_dim, 64, 64] VAE latent
            features: Dict of intermediate feature maps
        """
        # Average pool patches if multiple
        if latent.dim() == 3:
            latent = latent.mean(dim=1)  # [B, latent_dim]
        
        # Initial feature map
        x = self.initial(latent)
        features = {}
        
        # Stage 1
        x = self.stage1(x)
        features['stage1'] = x
        x = self.up1(x)
        
        # Stage 2
        x = self.stage2(x)
        features['stage2'] = x
        x = self.up2(x)
        
        # Stage 3
        x = self.stage3(x)
        features['stage3'] = x
        x = self.up3(x)
        
        # Stage 4
        x = self.stage4(x)
        features['stage4'] = x
        x = self.up4(x)
        
        output = self.output_norm(x)
        return output, features
```

### Pattern 3: Full Training Loop

```python
class DLinkTrainer:
    """End-to-end trainer for DLink EEG distillation."""
    
    def __init__(self, eeg_encoder, dlink_decoder, diffusion_unet,
                 vae_decoder, loss_config, optimizer_config):
        self.eeg_encoder = eeg_encoder
        self.dlink_decoder = dlink_decoder
        self.diffusion_unet = diffusion_unet  # Frozen teacher
        self.vae_decoder = vae_decoder        # Frozen VAE decoder
        
        # Freeze teacher models
        for param in self.diffusion_unet.parameters():
            param.requires_grad = False
        for param in self.vae_decoder.parameters():
            param.requires_grad = False
        
        self.criterion = DLinkDistillationLoss(loss_config)
        self.optimizer = torch.optim.AdamW(
            list(self.eeg_encoder.parameters()) + 
            list(self.dlink_decoder.parameters()),
            **optimizer_config
        )
        
        self.scheduler = torch.optim.lr_scheduler.CosineAnnealingLR(
            self.optimizer, T_max=optimizer_config.get('epochs', 100)
        )
        
    def extract_teacher_features(self, latent, timestep=500):
        """
        Run diffusion model at a fixed timestep to extract features.
        
        The timestep choice is critical — middle timesteps (400-600 for 
        1000-step diffusion) capture the most transferable knowledge.
        """
        B = latent.shape[0]
        # Add noise to latent for feature extraction
        noise = torch.randn_like(latent)
        noisy_latent = self.add_noise(latent, timestep, noise)
        
        # Run UNet forward pass (inference mode)
        with torch.no_grad():
            self.diffusion_unet(noisy_latent, timestep)
        
        # Features captured by hooks
        teacher_features = self.feature_hook.features.copy()
        self.feature_hook.clear()
        
        return teacher_features
    
    def add_noise(self, x, t, noise):
        """Add noise at timestep t using diffusion schedule."""
        # Use DDPM noise schedule
        betas = self.noise_schedule.betas
        alphas = 1.0 - betas
        alphas_cumprod = torch.cumprod(alphas, dim=0)
        
        sqrt_alpha_t = torch.sqrt(alphas_cumprod[t]).to(x.device)
        sqrt_one_minus_alpha_t = torch.sqrt(1 - alphas_cumprod[t]).to(x.device)
        
        return sqrt_alpha_t * x + sqrt_one_minus_alpha_t * noise
    
    def train_step(self, eeg_batch, image_batch):
        """Single training step."""
        self.eeg_encoder.train()
        self.dlink_decoder.train()
        
        # Forward pass: EEG → latent → VAE latent
        eeg_latent = self.eeg_encoder(eeg_batch)
        vae_latent, student_features = self.dlink_decoder(eeg_latent)
        
        # Extract teacher features from diffusion model
        teacher_features = self.extract_teacher_features(vae_latent.detach())
        
        # Decode VAE latent to image
        reconstructed = self.vae_decoder.decode(vae_latent)
        
        # Compute loss
        losses = self.criterion(
            student_output=reconstructed,
            student_features=student_features,
            teacher_features=teacher_features,
            target_image=image_batch,
        )
        
        # Backward pass
        self.optimizer.zero_grad()
        losses['total'].backward()
        torch.nn.utils.clip_grad_norm_(
            list(self.eeg_encoder.parameters()) + 
            list(self.dlink_decoder.parameters()),
            max_norm=1.0
        )
        self.optimizer.step()
        
        return {k: v.item() if hasattr(v, 'item') else v for k, v in losses.items()}
    
    def train_epoch(self, dataloader):
        """Train for one epoch."""
        epoch_losses = {
            'total': 0, 'reconstruction': 0, 
            'layer_wise': 0, 'dominant': 0, 'consistency': 0
        }
        
        for eeg_batch, image_batch in dataloader:
            eeg_batch = eeg_batch.to(self.device)
            image_batch = image_batch.to(self.device)
            
            step_losses = self.train_step(eeg_batch, image_batch)
            
            for key in epoch_losses:
                if key in step_losses:
                    epoch_losses[key] += step_losses[key]
        
        n_batches = len(dataloader)
        return {k: v / n_batches for k, v in epoch_losses.items()}
```

### Pattern 4: Progressive Distillation Strategy

```python
class ProgressiveDLinkTrainer:
    """
    Progressive training strategy:
    Phase 1: Train EEG encoder alone with basic reconstruction
    Phase 2: Add layer-wise distillation (all layers, low weight)
    Phase 3: Increase layer-wise distillation weight
    Phase 4: Add dominant knowledge distillation
    Phase 5: Full combined objective with all losses
    """
    
    def __init__(self, model, config):
        self.model = model
        self.phase = 0
        self.phase_epochs = config.get('phase_epochs', [10, 20, 30, 40, 100])
        
    def get_loss_weights(self, current_epoch):
        """Get loss weights based on current training phase."""
        if current_epoch < self.phase_epochs[0]:
            # Phase 1: Reconstruction only
            return {'alpha': 1.0, 'beta': 0.0, 'gamma': 0.0, 'delta': 0.0}
        elif current_epoch < self.phase_epochs[1]:
            # Phase 2: Reconstruction + light layer-wise
            return {'alpha': 1.0, 'beta': 0.1, 'gamma': 0.0, 'delta': 0.0}
        elif current_epoch < self.phase_epochs[2]:
            # Phase 3: Stronger layer-wise
            return {'alpha': 1.0, 'beta': 0.5, 'gamma': 0.0, 'delta': 0.05}
        elif current_epoch < self.phase_epochs[3]:
            # Phase 4: Add dominant knowledge
            return {'alpha': 1.0, 'beta': 0.5, 'gamma': 0.3, 'delta': 0.05}
        else:
            # Phase 5: Full objective
            return {'alpha': 1.0, 'beta': 0.5, 'gamma': 0.3, 'delta': 0.1}
```

## Key Implementation Details

### Timestep Selection for Feature Extraction

The choice of diffusion timestep for feature extraction significantly impacts distillation quality:

| Timestep Range | Knowledge Type | Distillation Benefit |
|---|---|---|
| 0–200 | Near-clean images, fine details | Good for high-frequency feature alignment |
| 200–400 | Structured content emerging | Moderate transfer value |
| 400–600 | **Optimal** — semantic structure + noise | Best balance of signal and transferable priors |
| 600–800 | Heavy noise, abstract structure | Good for robustness learning |
| 800–1000 | Pure noise | Not useful for distillation |

```python
def optimal_timestep_schedule(diffusion_steps=1000):
    """Generate timestep schedule for multi-step distillation."""
    # Primary: focus on 400-600 range
    primary = torch.linspace(400, 600, steps=8).long()
    
    # Secondary: include some variety
    secondary = torch.tensor([200, 300, 700, 800]).long()
    
    # Combined schedule (shuffle for training)
    schedule = torch.cat([primary, secondary])
    return schedule[torch.randperm(len(schedule))]
```

### Spatial Alignment Strategy

Teacher and student feature maps may have different spatial resolutions:

```python
def align_spatial_dimensions(student_feat, teacher_feat, method='pool'):
    """Align spatial dimensions between student and teacher features."""
    if student_feat.shape[-2:] == teacher_feat.shape[-2:]:
        return student_feat
    
    if method == 'pool':
        return F.adaptive_avg_pool2d(student_feat, teacher_feat.shape[-2:])
    elif method == 'interpolate':
        return F.interpolate(student_feat, size=teacher_feat.shape[-2:], 
                           mode='bilinear', align_corners=False)
    elif method == 'learned':
        # Learnable spatial adapter
        adapter = nn.Conv2d(student_feat.shape[1], student_feat.shape[1], 
                          kernel_size=3, padding=1)
        aligned = adapter(student_feat)
        return F.interpolate(aligned, size=teacher_feat.shape[-2:],
                           mode='bilinear', align_corners=False)
```

### Gradient Isolation for Teacher

```python
@torch.no_grad()
def get_teacher_features_safe(unet, latent, timestep, feature_hook):
    """
    Safely extract teacher features with gradient isolation.
    Ensures no gradients flow through the frozen teacher.
    """
    noise = torch.randn_like(latent)
    noisy = add_noise(latent, timestep, noise)
    
    # All teacher computation is gradient-free
    with torch.no_grad():
        unet(noisy, timestep)
    
    # Return detached copies
    features = {k: v.detach().clone() for k, v in feature_hook.features.items()}
    feature_hook.clear()
    return features
```

## Evaluation Metrics

### Quantitative Metrics for EEG Visual Reconstruction

```python
def compute_reconstruction_metrics(reconstructed, ground_truth):
    """Compute standard reconstruction quality metrics."""
    import numpy as np
    from skimage.metrics import structural_similarity as ssim
    from skimage.metrics import peak_signal_noise_ratio as psnr
    
    # Convert to numpy
    rec_np = reconstructed.detach().cpu().numpy()
    gt_np = ground_truth.detach().cpu().numpy()
    
    metrics = {}
    
    # Pixel-wise MSE
    metrics['mse'] = np.mean((rec_np - gt_np) ** 2)
    
    # PSNR
    metrics['psnr'] = psnr(gt_np, rec_np, data_range=gt_np.max() - gt_np.min())
    
    # SSIM (structural similarity)
    metrics['ssim'] = ssim(gt_np, rec_np, 
                          data_range=gt_np.max() - gt_np.min(),
                          channel_axis=0)
    
    return metrics


def compute_feature_similarity(student_features, teacher_features):
    """Compute CKA (Centered Kernel Alignment) between student and teacher features."""
    def cka(X, Y):
        """Linear CKA similarity."""
        # Center the matrices
        X = X - X.mean(axis=0, keepdims=True)
        Y = Y - Y.mean(axis=0, keepdims=True)
        
        # HSIC values
        hsic_xy = np.trace(X @ X.T @ Y @ Y.T)
        hsic_xx = np.trace(X @ X.T @ X @ X.T)
        hsic_yy = np.trace(Y @ Y.T @ Y @ Y.T)
        
        return hsic_xy / np.sqrt(hsic_xx * hsic_yy)
    
    # Compute per-layer CKA
    similarities = {}
    for key in student_features:
        if key in teacher_features:
            S = student_features[key].flatten(2).detach().cpu().numpy()
            T = teacher_features[key].flatten(2).detach().cpu().numpy()
            similarities[key] = cka(S.T, T.T)
    
    return similarities
```

## Full End-to-End Pipeline

```
┌─────────────────────────────────────────────────────────────────┐
│                       DLINK PIPELINE                              │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  Raw EEG Signal                                                  │
│       │                                                          │
│       ▼                                                          │
│  ┌─────────────────┐                                             │
│  │  EEG Encoder    │  Temporal Conv → Transformer → Projection   │
│  │  (Student)      │                                             │
│  └────────┬────────┘                                             │
│           │                                                      │
│           ▼                                                      │
│  ┌─────────────────┐                                             │
│  │  DLink Decoder  │  Progressive upsampling with distillation   │
│  │  (Student)      │  outputs at each stage                      │
│  └────────┬────────┘                                             │
│           │                                                      │
│           ├──► VAE Latent ──► VAE Decoder ──► Reconstructed Image │
│           │                                                        │
│           ▼                                                        │
│  ┌──────────────────────────────────────────┐                     │
│  │         Distillation Module               │                     │
│  │                                          │                     │
│  │  Layer-Wise Distillation:                │                     │
│  │  ──────────────────────────              │                     │
│  │  • Stage 1: Edges/Textures ←─────────┐   │                     │
│  │  • Stage 2: Local Patterns ←─────────┤   │                     │
│  │  • Stage 3: Shapes/Parts ←───────────┤   │                     │
│  │  • Stage 4: Semantic Concepts ←──────┤   │                     │
│  │  • Stage 5: Object Refinement ←──────┤   │                     │
│  │  • Stage 6: Fine Details ←───────────┤   │                     │
│  │                                       │   │                     │
│  │  Dominant Knowledge:                  │   │                     │
│  │  ──────────────────                   │   │                     │
│  │  • Object Identity ←─────────────────┤   │                     │
│  │  • Scene Layout ←────────────────────┤   │                     │
│  │  • Color/Texture Patterns ←──────────┤   │                     │
│  │  • Semantic Consistency ←────────────┘   │                     │
│  │                                          │                     │
│  │  Teacher: Diffusion UNet (Frozen) ───────┘                     │
│  └──────────────────────────────────────────┘                     │
│                                                                  │
│  L_total = α·L_recon + β·L_layer + γ·L_dominant + δ·L_consistency │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

## Practical Considerations

### Memory Efficiency

Diffusion models are large. Use these strategies for memory-efficient distillation:

```python
def memory_efficient_distillation(student, teacher, batch, chunk_size=4):
    """Process large batches in chunks for memory efficiency."""
    total_loss = 0.0
    
    for i in range(0, batch['eeg'].shape[0], chunk_size):
        eeg_chunk = batch['eeg'][i:i+chunk_size]
        image_chunk = batch['image'][i:i+chunk_size]
        
        # Forward pass
        with torch.no_grad():
            teacher_features = get_teacher_features(
                teacher, eeg_chunk, timestep=500
            )
        
        student_latent = student.encoder(eeg_chunk)
        student_output, student_features = student.decoder(student_latent)
        
        # Compute loss on chunk
        loss, _ = compute_distillation_loss(
            student_features, teacher_features, image_chunk
        )
        total_loss += loss * chunk_size  # Scale back up
    
    return total_loss / batch['eeg'].shape[0]
```

### Checkpointing and Resumption

```python
def save_checkpoint(epoch, encoder, decoder, optimizer, scheduler, path):
    """Save training checkpoint with full state."""
    torch.save({
        'epoch': epoch,
        'encoder_state_dict': encoder.state_dict(),
        'decoder_state_dict': decoder.state_dict(),
        'optimizer_state_dict': optimizer.state_dict(),
        'scheduler_state_dict': scheduler.state_dict(),
        'config': get_current_config(),
    }, path)


def load_checkpoint(path, encoder, decoder, optimizer, scheduler):
    """Load training checkpoint."""
    checkpoint = torch.load(path, map_location='cpu')
    encoder.load_state_dict(checkpoint['encoder_state_dict'])
    decoder.load_state_dict(checkpoint['decoder_state_dict'])
    optimizer.load_state_dict(checkpoint['optimizer_state_dict'])
    scheduler.load_state_dict(checkpoint['scheduler_state_dict'])
    return checkpoint['epoch']
```

### Hyperparameter Guidelines

| Parameter | Typical Range | Notes |
|---|---|---|
| Learning rate | 1e-4 to 5e-4 | Use cosine annealing with warmup |
| Batch size | 16–64 | Limited by GPU memory with teacher features |
| β (layer-wise weight) | 0.3–0.7 | Increase progressively during training |
| γ (dominant weight) | 0.2–0.5 | Higher for semantic-rich datasets |
| δ (consistency weight) | 0.05–0.2 | Important for temporal EEG data |
| Timestep for extraction | 400–600 | Optimal range for diffusion prior transfer |
| top_k_ratio (dominant) | 0.2–0.4 | Fraction of features to treat as dominant |
| Projection layers | 2–3 layers | Linear or MLP for feature alignment |

## Dependencies

```
pip install torch torchvision
pip install diffusers transformers  # for diffusion model access
pip install accelerate  # for mixed precision and distributed training
pip install mne  # for EEG data loading and preprocessing
pip install numpy scipy scikit-learn
pip install opencv-python  # for image processing
pip install einops  # for tensor rearrangement
pip install timm  # for pretrained model utilities
```

## References

1. DLink Paper: "DLink: Distilling Layer-wise and Dominant Knowledge from Diffusion Models for Enhanced EEG Decoding." arXiv:2604.12572, 2026-04-15.
2. Hinton, G., Vinyals, O., & Dean, J. (2015). "Distilling the Knowledge in a Neural Network." *NeurIPS Workshop*.
3. Rombach, R. et al. (2022). "High-Resolution Image Synthesis with Latent Diffusion Models." *CVPR*.
4. Raghu, M. et al. (2017). "SVCCA: Singular Vector Canonical Correlation Analysis for Deep Learning Dynamics." *NeurIPS*.
5. Kornblith, S. et al. (2019). "Similarity of Neural Network Representations Revisited." *ICML*.
