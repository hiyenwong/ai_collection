---
name: vision-smolmamba-token-pruning
description: "Vision SmolMamba: Spike-Guided Token Pruning for energy-efficient spiking state-space vision models. Combines SNN event-driven sparsity with Mamba selective recurrence via SST-TP (Spike-Guided Spatio-Temporal Token Pruner). Activation: Vision SmolMamba, spike-guided token pruning, state-space SNN, Mamba vision, SST-TP"
---

# Vision SmolMamba: Spike-Guided Token Pruning for SNN State-Space Vision

> Energy-efficient spiking state-space vision architecture combining spike-driven dynamics with linear-time Mamba recurrence, achieving 1.5x+ energy reduction over spiking Transformers through SST-TP token pruning.

## Metadata

- **Source**: arXiv:2604.25570v1
- **Title**: Vision SmolMamba: Spike-Guided Token Pruning for Energy-Efficient Spiking State-Space Vision Models
- **Published**: 2026-04-28
- **Category**: cs.CV, cs.LG, cs.AR

## Core Methodology

### Key Innovation

**Problem**: Spiking Transformers suffer from quadratic token interactions that fundamentally conflict with the sparse, event-driven nature of spiking neural computation. Self-attention in SNNs creates dense temporal dependencies even when most neurons are silent.

**Solution**: Vision SmolMamba integrates spike-driven dynamics with **linear-time selective recurrence** (Mamba state-space models) through a novel **Spike-Guided Spatio-Temporal Token Pruner (SST-TP)**.

### Spike-Guided Spatio-Temporal Token Pruner (SST-TP)

#### Token Importance Estimation

Two complementary signals from SNN spike activity:

1. **Spike Activation Strength**:
   ```
   A(t) = Σ_i s_i(t)  # Count of active neurons at time t
   ```

2. **First-Spike Latency**:
   ```
   L(p) = argmin_t {s_p(t) > 0}  # First spike time for patch p
   ```
   Lower latency = higher importance (earlier activation in temporal processing)

#### Token Importance Score

```
I(p,t) = α * A(p,t) + β * (T_max - L(p)) / T_max
```

Where:
- `A(p,t)`: Normalized activation strength for patch p
- `L(p)`: First-spike latency for patch p
- `T_max`: Maximum simulation timesteps
- `α, β`: Learnable weighting coefficients

#### Progressive Token Removal

```python
def sst_tp_prune(tokens, spike_history, keep_ratio):
    """Progressive token pruning based on spike statistics"""
    # Compute importance scores
    importance = compute_spike_importance(spike_history)
    
    # Sort and select top-k
    k = int(len(tokens) * keep_ratio)
    top_k_indices = torch.topk(importance, k, dim=-1).indices
    
    return tokens[top_k_indices], top_k_indices
```

**Key property**: Importance evolves dynamically with spike patterns—redundant regions naturally receive fewer spikes and are pruned.

### SmolMamba Block Architecture

```
Input Tokens → Spike Encoding → SST-TP Pruning → Bidirectional SSM → Spike Decoding → Output
                  ↓                    ↓                 ↓
            Spike events          Token subset      Linear recurrence
```

#### Components

1. **Spike Event Encoder**: Convert spatial patches to spike sequences
2. **SST-TP Layer**: Dynamically prune tokens based on spike statistics
3. **Bidirectional State-Space Module**:
   ```
   h_t = A · h_{t-1} + B · x_t      # Forward selective recurrence
   h'_t = A' · h'_{t+1} + B' · x_t  # Backward selective recurrence
   y_t = C · (h_t + h'_t)           # Combined output
   ```
4. **Spike Decoder**: Convert state-space features back to spike representations

#### Selective State-Space with Spikes

The core Mamba selective mechanism adapted for SNNs:

```python
class SmolMambaBlock(nn.Module):
    def __init__(self, dim):
        # Standard SSM parameters
        self.A = nn.Parameter(torch.randn(dim))
        self.B = nn.Linear(dim, dim)
        self.C = nn.Linear(dim, dim)
        
        # Spike-aware selection
        self.spike_gate = SpikeGate(dim)
        
    def forward(self, x, spikes):
        # Prune based on spike importance
        x_pruned, keep_indices = sst_tp_prune(x, spikes, keep_ratio=0.5)
        
        # Bidirectional selective SSM
        h_forward = selective_ssm(x_pruned, self.A, self.B(x_pruned), direction='forward')
        h_backward = selective_ssm(x_pruned, self.A, self.B(x_pruned), direction='backward')
        
        # Combine and expand back
        h_combined = h_forward + h_backward
        return expand_tokens(h_combined, keep_indices, original_size=len(x))
```

## Implementation Guide

### Prerequisites

- PyTorch >= 2.0
- SNN toolkit (SpikingJelly or snntorch)
- CUDA-capable GPU (recommended)

### Step-by-Step Implementation

#### 1. SST-TP Token Pruning

```python
import torch
import torch.nn as nn

class SSTTP(nn.Module):
    """Spike-Guided Spatio-Temporal Token Pruner"""
    
    def __init__(self, dim, keep_ratio=0.5):
        super().__init__()
        self.keep_ratio = keep_ratio
        self.alpha = nn.Parameter(torch.tensor(0.5))
        self.beta = nn.Parameter(torch.tensor(0.5))
        
    def compute_importance(self, spike_history):
        """
        spike_history: [B, T, N] - spike events over T timesteps for N tokens
        Returns: importance scores [B, N]
        """
        # Activation strength: total spikes per token
        activation = spike_history.sum(dim=1)  # [B, N]
        activation_norm = activation / (activation.max(dim=-1, keepdim=True)[0] + 1e-8)
        
        # First-spike latency
        first_spike = torch.argmax(spike_history > 0, dim=1).float()  # [B, N]
        T_max = spike_history.size(1)
        latency_score = 1.0 - (first_spike / T_max)  # Earlier = more important
        
        # Combined importance
        importance = self.alpha * activation_norm + self.beta * latency_score
        return importance
    
    def forward(self, tokens, spike_history):
        """
        tokens: [B, N, C] - N tokens of dimension C
        spike_history: [B, T, N] - spike events
        Returns: pruned tokens [B, N_keep, C], keep_indices
        """
        B, N, C = tokens.shape
        importance = self.compute_importance(spike_history)
        
        k = int(N * self.keep_ratio)
        keep_indices = torch.topk(importance, k, dim=-1, largest=True).indices
        
        # Gather pruned tokens
        pruned_tokens = torch.gather(tokens, 1, 
                                     keep_indices.unsqueeze(-1).expand(-1, -1, C))
        return pruned_tokens, keep_indices
```

#### 2. Spike-Guided State-Space Block

```python
class SpikeGuidedSSM(nn.Module):
    """Bidirectional state-space model with spike-aware selection"""
    
    def __init__(self, dim, state_dim=16):
        super().__init__()
        self.dim = dim
        self.state_dim = state_dim
        
        # SSM parameters
        self.A = nn.Parameter(torch.randn(dim, state_dim))
        self.B = nn.Linear(dim, state_dim)
        self.C = nn.Linear(state_dim, dim)
        
        # Spike gating
        self.spike_proj = nn.Linear(dim, state_dim)
        
    def selective_ssm(self, x, direction='forward'):
        """State-space recurrence with selective gating"""
        B, N, C = x.shape
        h = torch.zeros(B, self.state_dim).to(x.device)
        
        outputs = []
        steps = range(N) if direction == 'forward' else reversed(range(N))
        
        for t in steps:
            h = self.A * h + self.B(x[:, t]) * torch.sigmoid(self.spike_proj(x[:, t]))
            y = self.C(h)
            outputs.append(y)
            
        return torch.stack(outputs, dim=1)
    
    def forward(self, x, spike_history):
        # Forward pass
        forward_out = self.selective_ssm(x, 'forward')
        
        # Backward pass
        backward_out = self.selective_ssm(x, 'backward')
        
        # Combine
        return forward_out + backward_out
```

#### 3. Vision SmolMamba Model

```python
class VisionSmolMamba(nn.Module):
    """Complete Vision SmolMamba architecture"""
    
    def __init__(self, img_size=224, patch_size=16, dim=384, 
                 num_classes=1000, depth=12, keep_ratios=[0.8, 0.6, 0.5, 0.4]):
        super().__init__()
        
        # Patch embedding with spike encoding
        self.patch_embed = SpikingPatchEmbed(img_size, patch_size, dim)
        
        # SmolMamba blocks with progressive pruning
        self.blocks = nn.ModuleList([
            SmolMambaBlock(dim, keep_ratio=keep_ratios[i % len(keep_ratios)])
            for i in range(depth)
        ])
        
        # Classification head
        self.head = nn.Sequential(
            nn.LayerNorm(dim),
            nn.Linear(dim, num_classes)
        )
        
    def forward(self, x):
        B = x.size(0)
        
        # Patch + spike encoding
        tokens, spike_history = self.patch_embed(x)
        
        # SmolMamba blocks with token pruning
        for block in self.blocks:
            tokens, spike_history = block(tokens, spike_history)
        
        # Global average pooling
        x = tokens.mean(dim=1)
        
        return self.head(x)
```

### Training Configuration

```python
config = {
    # Model
    'dim': 384,
    'depth': 12,
    'num_heads': 6,
    'keep_ratios': [0.8, 0.6, 0.5, 0.4],  # Progressive pruning
    
    # SNN-specific
    'timesteps': 4,
    'spike_fn': 'surrogate_gradient',
    'v_threshold': 1.0,
    
    # Training
    'batch_size': 128,
    'lr': 1e-3,
    'epochs': 300,
    'weight_decay': 0.05,
    'warmup_epochs': 20,
    
    # Data augmentation
    'mixup_alpha': 0.8,
    'cutmix_alpha': 1.0,
    'auto_augment': 'rand-m9-mstd0.5-inc1'
}
```

## Applications

- **Event-based Vision**: DVS camera processing with temporal sparsity
- **Static Image Recognition**: ImageNet-level accuracy with spiking efficiency
- **Real-time Video Processing**: Low-latency video understanding
- **Edge AI Devices**: Battery-powered vision systems
- **Neuromorphic Sensors**: Integration with silicon retinas

## Benchmark Results

### Static Image Datasets

| Dataset | Model | Accuracy | Energy Cost | Note |
|---------|-------|----------|-------------|------|
| ImageNet-1K | Spiking Transformer | 74.2% | 2.5x | Baseline |
| ImageNet-1K | **Vision SmolMamba** | **74.5%** | **1.6x** | +0.3%, 1.56x more efficient |
| CIFAR-10 | Spiking Transformer | 95.8% | 2.0x | Baseline |
| CIFAR-10 | **Vision SmolMamba** | **96.1%** | **1.3x** | +0.3%, 1.54x more efficient |
| CIFAR-100 | Spiking Transformer | 78.4% | 2.2x | Baseline |
| CIFAR-100 | **Vision SmolMamba** | **78.9%** | **1.4x** | +0.5%, 1.57x more efficient |

### Event-based Datasets

| Dataset | Model | Accuracy | Energy Cost |
|---------|-------|----------|-------------|
| CIFAR10-DVS | Spiking Transformer | 81.2% | 2.8x |
| CIFAR10-DVS | **Vision SmolMamba** | **82.1%** | **1.7x** |
| DVS128 Gesture | Spiking Transformer | 97.5% | 3.1x |
| DVS128 Gesture | **Vision SmolMamba** | **97.8%** | **1.9x** |

### Energy Efficiency Analysis

| Component | Spiking Transformer | Vision SmolMamba | Savings |
|-----------|--------------------|--------------------|---------|
| Token Processing | 100% | 45% (pruned) | **55%** |
| Attention/SSM | O(n²) | O(n) | **Linear complexity** |
| Overall Energy | 2.5x-3.0x | 1.5x-2.0x | **1.5x+** |

## Pitfalls

1. **First-Spike Latency Sensitivity**: Tokens that spike late in the temporal window may be incorrectly pruned if latency is over-weighted
2. **Keep Ratio Tuning**: Too aggressive pruning (>60% removal) can hurt performance; optimal varies by dataset
3. **Temporal Alignment**: SST-TP assumes temporal processing; may need adaptation for non-temporal vision tasks
4. **Surrogate Gradient Stability**: Combining SSM with surrogate gradients requires careful gradient flow management
5. **Hardware Realization**: State-space operations may not be as hardware-friendly as sparse convolutions on some neuromorphic chips

## Related Skills

- `gemst-multidimensional-grouping-snn`: Multi-dimensional grouping for energy-efficient S-ViTs
- `spike-mllm-multimodal-spiking`: Multimodal LLMs with spiking components
- `stdp-spiking-transformer-attention`: STDP-based spiking transformers
- `adaptive-spiking-neuron-asn`: Adaptive spiking neurons for vision

## References

- arXiv:2604.25570v1: Vision SmolMamba paper
- Mamba: arXiv:2312.00752 (state-space models)
- SpikingJelly: https://github.com/fangwei123456/spikingjelly
- Spiking Transformer: arXiv:2109.02869
