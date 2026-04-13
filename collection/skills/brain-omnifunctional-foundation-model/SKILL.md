---
name: brain-omnifunctional-foundation-model
description: "Brain-OF: Omnifunctional foundation model for fMRI, EEG and MEG. First model jointly pretrained on multiple neuroimaging modalities with Any-Resolution Neural Signal Sampler and DINT attention with Sparse Mixture of Experts. Activation: brain foundation model, Brain-OF, multimodal brain model, fMRI EEG MEG foundation, 脑基础模型, 全功能脑模型."
---

# Brain-OF: An Omnifunctional Foundation Model for fMRI, EEG and MEG

## Description
Brain-OF is the first omnifunctional brain foundation model jointly pretrained on fMRI, EEG and MEG, capable of handling both unimodal and multimodal inputs within a unified framework. To reconcile heterogeneous spatiotemporal resolutions, it introduces the Any-Resolution Neural Signal Sampler, which projects diverse brain signals into a shared semantic space. The backbone integrates DINT attention with a Sparse Mixture of Experts, where shared experts capture modality-invariant representations and routed experts specialize in modality-specific semantics.

## Paper Reference
- **Title**: Brain-OF: An Omnifunctional Foundation Model for fMRI, EEG and MEG
- **Authors**: Hanning Guo, Farah Abdellatif, Hanwen Bi, Andrei Galbenus, Jon. N. Shah, Abigail Morrison, Jürgen Dammers
- **arXiv ID**: 2602.23410
- **Published**: 2026-02-26
- **PDF**: https://arxiv.org/pdf/2602.23410

## Key Contributions
1. **First Omnifunctional Model**: First brain foundation model jointly pretrained on fMRI, EEG and MEG
2. **Unified Framework**: Handles both unimodal and multimodal inputs
3. **Any-Resolution Neural Signal Sampler**: Projects diverse brain signals into shared semantic space
4. **DINT Attention**: Novel attention mechanism for brain signals
5. **Sparse Mixture of Experts**: Shared experts for modality-invariant representations, routed experts for modality-specific semantics
6. **Masked Temporal-Frequency Modeling**: Dual-domain pretraining objective
7. **Large-Scale Pretraining**: Pretrained on ~40 datasets

## Core Concepts

### Multimodal Brain Imaging
Different modalities capture complementary aspects:
```
fMRI: High spatial resolution, low temporal resolution (seconds)
EEG: High temporal resolution (ms), low spatial resolution
MEG: High temporal resolution (ms), moderate spatial resolution
```

### Challenge: Heterogeneous Resolutions
```
Spatial: Voxel (fMRI) vs. Channel (EEG/MEG)
Temporal: TR=2s (fMRI) vs. sampling rate=500Hz (EEG/MEG)
Signal Type: BOLD (fMRI) vs. electrical/magnetic (EEG/MEG)
```

### Solution: Any-Resolution Neural Signal Sampler
Projects diverse signals into shared semantic space regardless of original resolution.

## Activation Keywords
- brain foundation model
- Brain-OF
- multimodal brain model
- fMRI EEG MEG foundation
- 脑基础模型
- 全功能脑模型
- omnifunctional brain model
- any-resolution neural sampler
- DINT attention
- sparse mixture of experts brain
- temporal-frequency modeling

## Tools Used
- **python**: Implementation of Brain-OF
- **torch**: PyTorch for deep learning
- **numpy**: Numerical computations
- **nibabel**: Neuroimaging data I/O
- **nilearn**: Brain data processing
- **mne**: EEG/MEG processing

## Implementation

### Any-Resolution Neural Signal Sampler
```python
import torch
import torch.nn as nn
import numpy as np
from typing import Dict, Union, Literal

class AnyResolutionSampler(nn.Module):
    """
    Projects brain signals of any resolution into shared semantic space
    Handles fMRI (voxels), EEG (channels), MEG (channels)
    """
    def __init__(self, 
                 output_dim=768,
                 num_latent_tokens=64,
                 num_resolution_levels=4):
        super().__init__()
        self.output_dim = output_dim
        self.num_latent_tokens = num_latent_tokens
        
        # Learnable latent tokens (perceiver-style)
        self.latent_tokens = nn.Parameter(
            torch.randn(1, num_latent_tokens, output_dim)
        )
        
        # Cross-attention for different input types
        self.cross_attn = nn.ModuleDict({
            'fmri': PerceiverCrossAttention(output_dim, num_heads=12),
            'eeg': PerceiverCrossAttention(output_dim, num_heads=12),
            'meg': PerceiverCrossAttention(output_dim, num_heads=12),
        })
        
        # Positional encoding for spatial locations
        self.spatial_pos_enc = SpatialPositionalEncoding(output_dim)
        
        # Temporal encoding
        self.temporal_pos_enc = TemporalPositionalEncoding(output_dim)
        
    def forward(self, 
                signal: torch.Tensor,
                spatial_coords: torch.Tensor,
                modality: Literal['fmri', 'eeg', 'meg'],
                temporal_info: torch.Tensor = None) -> torch.Tensor:
        """
        Args:
            signal: Input brain signal
                - fMRI: [B, T, V] (batch, time, voxels)
                - EEG: [B, T, C] (batch, time, channels)
                - MEG: [B, T, C] (batch, time, channels)
            spatial_coords: [V, 3] or [C, 3] - 3D coordinates
            modality: 'fmri', 'eeg', or 'meg'
            temporal_info: Temporal indices
            
        Returns:
            sampled: [B, num_latent_tokens, output_dim]
        """
        B, T, N = signal.shape
        
        # Add spatial positional encoding
        signal_with_pos = signal + self.spatial_pos_enc(spatial_coords).unsqueeze(0).unsqueeze(0)
        
        # Add temporal positional encoding
        if temporal_info is not None:
            signal_with_pos = signal_with_pos + self.temporal_pos_enc(temporal_info).unsqueeze(2)
        
        # Flatten spatial/temporal dimensions
        signal_flat = signal_with_pos.reshape(B, T * N, -1)
        
        # Project to output dimension
        signal_proj = nn.Linear(signal_flat.shape[-1], self.output_dim)(signal_flat)
        
        # Cross-attention with latent tokens
        latent = self.latent_tokens.expand(B, -1, -1)
        sampled = self.cross_attn[modality](latent, signal_proj)
        
        return sampled

class PerceiverCrossAttention(nn.Module):
    """Perceiver-style cross attention"""
    def __init__(self, dim, num_heads=8):
        super().__init__()
        self.num_heads = num_heads
        self.scale = (dim // num_heads) ** -0.5
        
        self.q_proj = nn.Linear(dim, dim)
        self.k_proj = nn.Linear(dim, dim)
        self.v_proj = nn.Linear(dim, dim)
        self.out_proj = nn.Linear(dim, dim)
        
    def forward(self, queries, kv):
        B, N, C = queries.shape
        
        q = self.q_proj(queries).reshape(B, N, self.num_heads, C // self.num_heads)
        k = self.k_proj(kv).reshape(B, -1, self.num_heads, C // self.num_heads)
        v = self.v_proj(kv).reshape(B, -1, self.num_heads, C // self.num_heads)
        
        q = q.transpose(1, 2)  # [B, H, N, D]
        k = k.transpose(1, 2)  # [B, H, M, D]
        v = v.transpose(1, 2)  # [B, H, M, D]
        
        attn = (q @ k.transpose(-2, -1)) * self.scale
        attn = attn.softmax(dim=-1)
        
        out = (attn @ v).transpose(1, 2).reshape(B, N, C)
        out = self.out_proj(out)
        
        return out
```

### DINT Attention
```python
class DINTAttention(nn.Module):
    """
    Dynamic Inter-Modal Neural Token (DINT) Attention
    Handles cross-modal interactions
    """
    def __init__(self, dim, num_heads=12, num_modalities=3):
        super().__init__()
        self.dim = dim
        self.num_heads = num_heads
        self.num_modalities = num_modalities
        
        # Modality-specific projections
        self.modality_projs = nn.ModuleList([
            nn.Linear(dim, dim) for _ in range(num_modalities)
        ])
        
        # Inter-modal attention
        self.cross_modal_attn = nn.MultiheadAttention(
            dim, num_heads, batch_first=True
        )
        
        # Dynamic routing
        self.router = nn.Sequential(
            nn.Linear(dim, dim // 4),
            nn.ReLU(),
            nn.Linear(dim // 4, num_modalities),
            nn.Softmax(dim=-1)
        )
        
    def forward(self, 
                tokens: torch.Tensor,
                modality_ids: torch.Tensor) -> torch.Tensor:
        """
        Args:
            tokens: [B, N, D] - input tokens
            modality_ids: [B, N] - modality identifier for each token
        Returns:
            attended: [B, N, D]
        """
        B, N, D = tokens.shape
        
        # Apply modality-specific projections
        projected = torch.zeros_like(tokens)
        for mod_id in range(self.num_modalities):
            mask = modality_ids == mod_id
            if mask.any():
                projected[mask] = self.modality_projs[mod_id](tokens[mask])
        
        # Cross-modal attention
        attended, _ = self.cross_modal_attn(
            projected, projected, projected
        )
        
        # Dynamic routing weights
        routing_weights = self.router(attended.mean(dim=1))  # [B, num_modalities]
        
        return attended, routing_weights
```

### Sparse Mixture of Experts
```python
class BrainMoE(nn.Module):
    """
    Sparse Mixture of Experts for Brain-OF
    Shared experts: modality-invariant
    Routed experts: modality-specific
    """
    def __init__(self, 
                 dim=768,
                 num_shared_experts=4,
                 num_routed_experts_per_modality=4,
                 top_k=2):
        super().__init__()
        self.dim = dim
        self.top_k = top_k
        
        # Shared experts (modality-invariant)
        self.shared_experts = nn.ModuleList([
            FeedForwardExpert(dim) for _ in range(num_shared_experts)
        ])
        
        # Routed experts (modality-specific)
        self.routed_experts = nn.ModuleDict({
            'fmri': nn.ModuleList([FeedForwardExpert(dim) for _ in range(num_routed_experts_per_modality)]),
            'eeg': nn.ModuleList([FeedForwardExpert(dim) for _ in range(num_routed_experts_per_modality)]),
            'meg': nn.ModuleList([FeedForwardExpert(dim) for _ in range(num_routed_experts_per_modality)]),
        })
        
        # Router network
        self.router = nn.Linear(dim, num_routed_experts_per_modality)
        
    def forward(self, x: torch.Tensor, modality: str) -> torch.Tensor:
        """
        Args:
            x: [B, N, D]
            modality: 'fmri', 'eeg', or 'meg'
        Returns:
            output: [B, N, D]
        """
        # Always use shared experts
        shared_output = sum(expert(x) for expert in self.shared_experts) / len(self.shared_experts)
        
        # Route to modality-specific experts
        router_logits = self.router(x.mean(dim=1))  # [B, num_experts]
        weights, indices = torch.topk(torch.softmax(router_logits, dim=-1), self.top_k, dim=-1)
        weights = weights / weights.sum(dim=-1, keepdim=True)
        
        # Compute routed expert outputs
        routed_output = torch.zeros_like(x)
        for i in range(self.top_k):
            expert_idx = indices[:, i]
            expert_weight = weights[:, i].unsqueeze(1).unsqueeze(2)
            for b in range(x.shape[0]):
                expert = self.routed_experts[modality][expert_idx[b]]
                routed_output[b] += expert_weight[b] * expert(x[b:b+1])
        
        # Combine shared and routed
        output = shared_output + routed_output
        
        return output

class FeedForwardExpert(nn.Module):
    """Individual expert network"""
    def __init__(self, dim, hidden_dim=None):
        super().__init__()
        hidden_dim = hidden_dim or 4 * dim
        self.net = nn.Sequential(
            nn.Linear(dim, hidden_dim),
            nn.GELU(),
            nn.Linear(hidden_dim, dim)
        )
        
    def forward(self, x):
        return self.net(x)
```

### Masked Temporal-Frequency Modeling
```python
class MaskedTemporalFrequencyModeling(nn.Module):
    """
    Dual-domain pretraining objective
    Reconstructs brain signals in both time and frequency domains
    """
    def __init__(self, dim=768):
        super().__init__()
        self.dim = dim
        
        # Time domain decoder
        self.time_decoder = nn.Sequential(
            nn.Linear(dim, dim * 2),
            nn.GELU(),
            nn.Linear(dim * 2, dim)
        )
        
        # Frequency domain decoder
        self.freq_decoder = nn.Sequential(
            nn.Linear(dim, dim * 2),
            nn.GELU(),
            nn.Linear(dim * 2, dim)
        )
        
    def forward(self, 
                latent: torch.Tensor,
                mask_ratio=0.5,
                domain='both') -> Dict[str, torch.Tensor]:
        """
        Args:
            latent: [B, N, D] - latent representations
            mask_ratio: Ratio of tokens to mask
            domain: 'time', 'freq', or 'both'
        Returns:
            predictions and targets
        """
        B, N, D = latent.shape
        
        # Create mask
        num_masked = int(N * mask_ratio)
        shuffle = torch.rand(B, N).argsort(dim=1)
        mask_indices = shuffle[:, :num_masked]
        
        # Mask latent
        masked_latent = latent.clone()
        masked_latent[torch.arange(B).unsqueeze(1), mask_indices] = 0
        
        results = {}
        
        if domain in ['time', 'both']:
            # Time domain reconstruction
            time_pred = self.time_decoder(masked_latent)
            results['time_prediction'] = time_pred
            results['time_target'] = latent
            
        if domain in ['freq', 'both']:
            # Frequency domain reconstruction
            # Apply FFT
            latent_freq = torch.fft.rfft(latent, dim=1).real
            freq_pred = self.freq_decoder(masked_latent)
            results['freq_prediction'] = freq_pred
            results['freq_target'] = latent_freq
        
        results['mask_indices'] = mask_indices
        
        return results
```

## Workflow

### Step 1: Data Preparation
```python
# Load multimodal brain data
fmri_data = load_fmri(subject_id)
eeg_data = load_eeg(subject_id)
meg_data = load_meg(subject_id)
```

### Step 2: Initialize Model
```python
# Initialize Brain-OF
model = BrainOF(
    dim=768,
    num_shared_experts=4,
    num_routed_experts=4
)
```

### Step 3: Pretraining
```python
# Masked temporal-frequency modeling
for batch in dataloader:
    # Sample brain signals
    signals, modality = batch
    
    # Any-resolution sampling
    sampled = sampler(signals, modality)
    
    # DINT attention
    attended, routing_weights = dint_attention(sampled, modality)
    
    # MoE processing
    output = moe(attended, modality)
    
    # Temporal-frequency reconstruction
    recon = masked_tf_modeling(output)
    
    # Compute loss
    loss = compute_mtf_loss(recon)
    loss.backward()
```

### Step 4: Fine-tuning
```python
# Downstream tasks
tasks = ['classification', 'regression', 'generation', 'decoding']
for task in tasks:
    finetune(model, task_data[task])
```

## Applications

### Brain Decoding
- Visual stimulus reconstruction
- Cognitive state prediction
- Brain-computer interfaces

### Clinical Applications
- Disease diagnosis
- Treatment response prediction
- Biomarker discovery

### Neuroscience Research
- Understanding neural representations
- Cross-modal integration studies
- Individual difference analysis

## Advantages

1. **Unified Framework**: Single model for multiple modalities
2. **Scalable**: Handles any resolution input
3. **Efficient**: Sparse MoE reduces computation
4. **Interpretable**: Shared vs. routed expert separation
5. **Comprehensive**: Joint temporal-frequency modeling

## Limitations

- Requires large-scale pretraining data
- Computational cost for MoE
- Memory requirements for multimodal processing
- Limited to functional neuroimaging (not structural)

## Related Skills

- **multimodal-brain-connectivity-gnn**: Multimodal brain connectivity GNN
- **brain-graph-neural**: Graph neural networks for brain analysis
- **neuroscience**: Neuroscience research tools
- **in-context-brain-decoding**: Training-free brain decoding

## References

1. Guo, H., et al. (2026). Brain-OF: An Omnifunctional Foundation Model for fMRI, EEG and MEG. arXiv:2602.23410.
2. Jaegle, A., et al. (2021). Perceiver: General Perception with Iterative Attention.
3. Fedus, W., et al. (2022). Switch Transformers: Scaling to Trillion Parameter Models.

## Version
- **Created**: 2026-04-12
- **Skill Version**: 1.0.0
- **Paper Version**: arXiv:2602.23410v2


## Instructions for Agents

1. **理解需求**：分析用户请求的具体场景
2. **选择方法**：根据上下文选择合适的技术方案
3. **执行操作**：按照技能描述实施具体步骤
4. **验证结果**：检查结果是否符合预期


## Examples

### Example 1: Basic Usage

**User:** 请帮我应用此技能

**Agent:** 我将按照标准流程执行...

### Example 2: Advanced Usage

**User:** 有更复杂的场景需要处理

**Agent:** 针对复杂场景，我将采用以下策略...
