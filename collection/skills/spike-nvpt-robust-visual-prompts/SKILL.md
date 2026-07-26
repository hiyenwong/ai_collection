---
name: spike-nvpt-robust-visual-prompts
description: "Spike-NVPT: Noise-robust visual prompt tuning using bio-inspired temporal filtering and spike-based discretization. Parameter-efficient adaptation for pre-trained vision models with enhanced robustness to input perturbations. Keywords: Spike-NVPT, visual prompt tuning, bio-inspired, temporal filtering, noise robustness, spiking neural networks, computer vision."
---

# Spike-NVPT: Robust Visual Prompts via Bio-Inspired Temporal Filtering

> Learning robust visual prompts through bio-inspired temporal filtering and spike-based discretization for parameter-efficient vision model adaptation.

## Metadata
- **Source**: arXiv:2604.18284v1
- **Authors**: Qiugang Zhan, Anning Jiang, Ran Tao, Ao Ma
- **Published**: 2026-04-20
- **Categories**: cs.CV

## Core Methodology

### Problem Statement

Prompt tuning-based methods for vision models face a critical trade-off:
- **Overfitting to noise**: Continuous, dense prompts have high capacity but overfit to task-irrelevant details
- **Sensitivity to perturbations**: Standard visual prompts are vulnerable to input noise
- **Parameter efficiency vs. robustness**: Difficult to achieve both simultaneously

### Key Innovation

Spike-NVPT introduces bio-inspired mechanisms from spiking neural networks:

1. **Temporal Filtering**
   - Bio-inspired temporal accumulation
   - Leaky integrate-and-fire dynamics
   - Noise suppression through temporal integration

2. **Spike-Based Discretization**
   - Binary/ternary spike representation
   - Event-driven computation
   - Reduced sensitivity to perturbations

3. **Robust Prompt Learning**
   - Parameter-efficient adaptation
   - Maintains pre-trained model frozen
   - Enhanced generalization to noisy inputs

### Technical Framework

```
Spike-NVPT Architecture
├── Frozen Pre-trained Vision Model (e.g., CLIP, ViT)
├── Visual Prompt Encoder
│   ├── Continuous Prompt Initialization
│   ├── Temporal Filtering Module
│   │   ├── Leaky integration
│   │   └── Temporal windowing
│   └── Spike Discretization
│       ├── Threshold-based spiking
│       └── Sparse activation
└── Task-Specific Head (learnable)
```

## Implementation Guide

### Prerequisites

```python
# Required libraries
pip install torch torchvision timm
pip install spikingjelly  # For SNN components
```

### Step-by-Step Implementation

#### 1. Temporal Filtering Module

```python
import torch
import torch.nn as nn
import torch.nn.functional as F

class TemporalFilteringModule(nn.Module):
    """
    Bio-inspired temporal filtering using leaky integration.
    
    Simulates the temporal dynamics of biological neurons where
    information is accumulated over time with decay, providing
    natural noise filtering.
    """
    def __init__(self, 
                 channels: int,
                 temporal_window: int = 5,
                 leak_factor: float = 0.9):
        super().__init__()
        self.channels = channels
        self.temporal_window = temporal_window
        self.leak_factor = leak_factor
        
        # Temporal integration weights (learnable)
        self.temporal_weights = nn.Parameter(
            torch.ones(temporal_window) / temporal_window
        )
        
        # Leaky integration state
        self.register_buffer('membrane_potential', None)
        
    def forward(self, x: torch.Tensor) -> torch.Tensor:
        """
        Apply temporal filtering to input features.
        
        Args:
            x: Input tensor of shape (B, C, H, W) or (B, T, C, H, W)
            
        Returns:
            Temporally filtered features
        """
        if x.dim() == 4:
            # Add temporal dimension if not present
            x = x.unsqueeze(1)  # (B, 1, C, H, W)
            
        B, T, C, H, W = x.shape
        
        # Apply weighted temporal integration
        weights = F.softmax(self.temporal_weights[:T], dim=0)
        
        # Leaky integration over time
        integrated = torch.zeros(B, C, H, W, device=x.device)
        for t in range(T):
            leak = integrated * self.leak_factor
            integrated = leak + x[:, t] * weights[t]
            
        return integrated
        
    def reset_state(self):
        """Reset membrane potential for new sequence."""
        self.membrane_potential = None
```

#### 2. Spike Discretization Layer

```python
class SpikeDiscretization(nn.Module):
    """
    Convert continuous activations to discrete spikes.
    
    Uses a threshold-based mechanism inspired by biological
    neurons, creating sparse binary/ternary representations
    that are naturally robust to noise.
    """
    def __init__(self,
                 threshold: float = 0.5,
                 spike_mode: str = 'binary',  # 'binary', 'ternary'
                 surrogate_gradient: str = 'straight-through'):
        super().__init__()
        self.threshold = threshold
        self.spike_mode = spike_mode
        
        # Learnable threshold adaptation
        self.adaptive_threshold = nn.Parameter(torch.tensor(threshold))
        
    def forward(self, x: torch.Tensor) -> torch.Tensor:
        """
        Convert continuous input to discrete spikes.
        
        Args:
            x: Continuous input tensor
            
        Returns:
            Discretized spike tensor
        """
        # Apply adaptive threshold
        threshold = torch.sigmoid(self.adaptive_threshold)
        
        if self.spike_mode == 'binary':
            # Binary spikes: 0 or 1
            spikes = (x >= threshold).float()
            
        elif self.spike_mode == 'ternary':
            # Ternary spikes: -1, 0, or 1
            spikes = torch.where(
                x >= threshold,
                torch.ones_like(x),
                torch.where(
                    x <= -threshold,
                    -torch.ones_like(x),
                    torch.zeros_like(x)
                )
            )
        else:
            raise ValueError(f"Unknown spike mode: {self.spike_mode}")
            
        # Straight-through estimator for gradient flow
        if self.training:
            spikes = x + (spikes - x).detach()
            
        return spikes
        
    def get_sparsity(self, x: torch.Tensor) -> float:
        """Calculate sparsity of spike representation."""
        return (x == 0).float().mean().item()
```

#### 3. Spike-NVPT Visual Prompt

```python
class SpikeNVPTPrompt(nn.Module):
    """
    Visual prompt with temporal filtering and spike discretization.
    
    Inspired by the robustness of spiking neural networks to noise,
    this prompt design uses bio-inspired temporal dynamics to create
    noise-robust visual prompts.
    """
    def __init__(self,
                 prompt_size: int = 30,
                 embed_dim: int = 768,
                 num_prompts: int = 10,
                 temporal_window: int = 3,
                 spike_threshold: float = 0.3):
        super().__init__()
        self.prompt_size = prompt_size
        self.embed_dim = embed_dim
        self.num_prompts = num_prompts
        
        # Continuous prompt embeddings (learnable)
        self.prompt_embeddings = nn.Parameter(
            torch.randn(num_prompts, embed_dim) * 0.02
        )
        
        # Temporal filtering for prompts
        self.temporal_filter = TemporalFilteringModule(
            channels=embed_dim,
            temporal_window=temporal_window
        )
        
        # Spike discretization
        self.spike_layer = SpikeDiscretization(
            threshold=spike_threshold,
            spike_mode='ternary'
        )
        
        # Spatial projection for patch-based models
        self.spatial_proj = nn.Linear(embed_dim, prompt_size * prompt_size * 3)
        
    def forward(self, batch_size: int, device: torch.device) -> torch.Tensor:
        """
        Generate visual prompts for a batch.
        
        Args:
            batch_size: Number of samples in batch
            device: Target device
            
        Returns:
            Visual prompts tensor
        """
        # Get base prompt embeddings
        prompts = self.prompt_embeddings.unsqueeze(0)  # (1, N, D)
        prompts = prompts.expand(batch_size, -1, -1)   # (B, N, D)
        
        # Apply temporal filtering
        prompts = self.temporal_filter(prompts)
        
        # Discretize to spikes
        prompts = self.spike_layer(prompts)
        
        # Project to spatial domain
        prompts = self.spatial_proj(prompts)  # (B, N, H*W*3)
        prompts = prompts.view(
            batch_size, self.num_prompts, 3, self.prompt_size, self.prompt_size
        )
        
        return prompts
        
    def get_sparsity_stats(self) -> dict:
        """Get statistics about prompt sparsity."""
        with torch.no_grad():
            prompts = self.prompt_embeddings
            spikes = self.spike_layer(prompts)
            return {
                'sparsity': self.spike_layer.get_sparsity(spikes),
                'positive_ratio': (spikes > 0).float().mean().item(),
                'negative_ratio': (spikes < 0).float().mean().item()
            }
```

#### 4. Complete Spike-NVPT Adapter

```python
import timm
from typing import Optional

class SpikeNVPTAdapter(nn.Module):
    """
    Complete adapter for parameter-efficient fine-tuning with Spike-NVPT.
    
    Combines visual prompting with a frozen pre-trained vision model
    and a learnable task head, achieving robust adaptation with
    minimal parameters.
    """
    def __init__(self,
                 model_name: str = 'vit_base_patch16_224',
                 num_classes: int = 10,
                 prompt_size: int = 30,
                 num_prompts: int = 10,
                 temporal_window: int = 3):
        super().__init__()
        
        # Load pre-trained vision model (frozen)
        self.backbone = timm.create_model(
            model_name, 
            pretrained=True,
            num_classes=0  # Remove classification head
        )
        for param in self.backbone.parameters():
            param.requires_grad = False
        self.backbone.eval()
        
        # Get embedding dimension
        self.embed_dim = self.backbone.num_features
        
        # Spike-NVPT visual prompts
        self.visual_prompt = SpikeNVPTPrompt(
            prompt_size=prompt_size,
            embed_dim=self.embed_dim,
            num_prompts=num_prompts,
            temporal_window=temporal_window
        )
        
        # Task-specific head (learnable)
        self.task_head = nn.Sequential(
            nn.LayerNorm(self.embed_dim),
            nn.Linear(self.embed_dim, self.embed_dim // 2),
            nn.GELU(),
            nn.Dropout(0.1),
            nn.Linear(self.embed_dim // 2, num_classes)
        )
        
    def forward(self, images: torch.Tensor) -> torch.Tensor:
        """
        Forward pass with visual prompting.
        
        Args:
            images: Input images (B, 3, H, W)
            
        Returns:
            Class logits
        """
        batch_size = images.shape[0]
        
        # Generate visual prompts
        prompts = self.visual_prompt(batch_size, images.device)
        
        # Add prompts to images (prepend as patches or add as noise)
        # Method 1: Prepend as additional patches
        prompted_images = self._prepend_prompt_patches(images, prompts)
        
        # Extract features through frozen backbone
        with torch.no_grad():
            features = self.backbone.forward_features(prompted_images)
        
        # Global average pooling
        if features.dim() == 3:  # (B, N, D) for transformers
            features = features.mean(dim=1)
        
        # Task prediction
        logits = self.task_head(features)
        
        return logits
        
    def _prepend_prompt_patches(self, 
                                images: torch.Tensor,
                                prompts: torch.Tensor) -> torch.Tensor:
        """
        Prepend visual prompts as additional input patches.
        
        Args:
            images: Input images
            prompts: Visual prompts (B, N, 3, H, W)
            
        Returns:
            Prompted images
        """
        # For ViT-style models, we can inject prompts at the patch level
        # Here we simply add the prompts as a residual
        B, N, C, H, W = prompts.shape
        
        # Resize prompts to match image size
        prompt_combined = prompts.view(B, N * C, H, W)
        prompt_resized = F.interpolate(
            prompt_combined,
            size=images.shape[2:],
            mode='bilinear',
            align_corners=False
        )
        
        # Add as residual with learnable scale
        return images + 0.1 * prompt_resized.view(B, C, *images.shape[2:])
        
    def get_trainable_params(self) -> int:
        """Count trainable parameters."""
        return sum(p.numel() for p in self.parameters() if p.requires_grad)
        
    def get_sparsity_stats(self) -> dict:
        """Get sparsity statistics."""
        return self.visual_prompt.get_sparsity_stats()
```

#### 5. Training with Noise Augmentation

```python
class RobustPromptTrainer:
    """
    Trainer for Spike-NVPT with noise augmentation.
    """
    def __init__(self, model: SpikeNVPTAdapter, noise_levels: list = [0.1, 0.2, 0.3]):
        self.model = model
        self.noise_levels = noise_levels
        
    def train_step(self, 
                   images: torch.Tensor,
                   labels: torch.Tensor,
                   optimizer: torch.optim.Optimizer) -> dict:
        """
        Single training step with noise augmentation.
        
        Args:
            images: Clean input images
            labels: Ground truth labels
            optimizer: Optimizer instance
            
        Returns:
            Dictionary of metrics
        """
        self.model.train()
        optimizer.zero_grad()
        
        # Forward with clean images
        logits_clean = self.model(images)
        loss_clean = F.cross_entropy(logits_clean, labels)
        
        # Forward with noisy images (robustness training)
        loss_noisy = 0
        for noise_level in self.noise_levels:
            noise = torch.randn_like(images) * noise_level
            noisy_images = torch.clamp(images + noise, 0, 1)
            logits_noisy = self.model(noisy_images)
            loss_noisy += F.cross_entropy(logits_noisy, labels)
        
        loss_noisy = loss_noisy / len(self.noise_levels)
        
        # Combined loss
        total_loss = loss_clean + 0.5 * loss_noisy
        
        total_loss.backward()
        optimizer.step()
        
        # Get sparsity stats
        sparsity_stats = self.model.get_sparsity_stats()
        
        return {
            'loss': total_loss.item(),
            'loss_clean': loss_clean.item(),
            'loss_noisy': loss_noisy.item(),
            'sparsity': sparsity_stats['sparsity'],
            'accuracy': (logits_clean.argmax(dim=1) == labels).float().mean().item()
        }
```

## Applications

- **Robust few-shot image classification**
- **Noise-resistant visual transfer learning**
- **Domain adaptation under distribution shift**
- **Edge deployment with limited compute**
- **Adversarial robustness enhancement**

## Pitfalls

- Spike discretization may lose fine-grained information
- Temporal filtering introduces latency
- Requires careful tuning of spike thresholds
- May underperform on noise-free clean data

## Related Skills

- spike-mllm-multimodal-spiking: Multimodal spiking LLMs
- bsvit-burst-spiking-vision-transformer: Burst spiking vision transformers
- vision-smolmamba-token-pruning: Vision token pruning
- adaptive-spiking-neuron-asn: Adaptive spiking neurons

## References

Zhan, Q., Jiang, A., Tao, R., & Ma, A. (2026). Spike-NVPT: Learning Robust Visual Prompts via Bio-Inspired Temporal Filtering and Discretization. arXiv:2604.18284v1.
