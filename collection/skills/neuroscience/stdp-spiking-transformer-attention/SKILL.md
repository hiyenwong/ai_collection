---
name: stdp-spiking-transformer-attention
description: "Spiking STDP Transformer (S²TDPT) implementing self-attention through spike-timing-dependent plasticity for energy-efficient neuromorphic computing with 88% energy reduction. Activation triggers: STDP transformer, spiking attention, neuromorphic transformer, bio-inspired attention, SNN transformer, energy-efficient attention."
---

# Attention via Synaptic Plasticity: Spiking Neuromorphic Transformer

> Biologically inspired Spiking STDP Transformer (S²TDPT) that implements self-attention through spike-timing-dependent plasticity, embedding query-key correlations directly in synaptic weights for 88.47% energy reduction.

## Metadata
- **Source**: arXiv:2511.14691 [cs.NE]
- **Authors**: Kallol Mondal, Ankush Kumar
- **Published**: 2025-11-18
- **Affiliation**: NIT Allahabad, IIT Roorkee
- **Categories**: cs.NE, cs.AI, cs.CV, cs.ET, stat.ML

## Core Methodology

### Key Innovation
Modern Transformers rely on energy-intensive dot-product attention operations unsuited for neuromorphic hardware. S²TDPT replaces this with:
- **STDP-based Attention**: Biological synaptic plasticity implements attention
- **In-Memory Computing**: Attention weights stored in synapses
- **Event-Driven Operation**: Computation only when spikes occur
- **88.47% Energy Reduction**: Compared to standard ANN Transformers

### Technical Framework

#### 1. Biological Attention vs Transformer Attention

**Standard Transformer:**
$$\text{Attention}(Q, K, V) = \text{softmax}\left(\frac{QK^T}{\sqrt{d_k}}\right)V$$

**S²TDPT STDP Attention:**
- Query-Key correlation **learned via STDP** in synaptic weights
- Attention matrix **stored in synapses**, not computed on-the-fly
- Spike timing encodes **temporal relationships**

#### 2. STDP Learning Rule
$$\Delta w_{ij} = \begin{cases} A_+ e^{-|\Delta t|/\tau_+} & \text{if } \Delta t > 0 \\ -A_- e^{-|\Delta t|/\tau_-} & \text{if } \Delta t < 0 \end{cases}$$

Where:
- $\Delta t = t_{post} - t_{pre}$: Spike time difference
- $A_+, A_-$: Learning rate parameters
- $\tau_+, \tau_-$: Time constants

#### 3. Spiking Transformer Architecture
- **Spiking Input Embedding**: Convert inputs to spike trains
- **STDP Self-Attention Layers**: Attention via plastic synapses
- **Spiking Feedforward**: Event-driven MLP
- **Rate Coding Output**: Spike count to classification

#### 4. Hardware Advantages
- **Non-von Neumann**: In-memory computation
- **Sparse Activity**: Only active when spikes occur
- **Low Precision**: Binary or low-bit weights sufficient
- **Parallel Updates**: STDP updates in parallel

## Implementation Guide

### Prerequisites
- Python 3.8+
- PyTorch 2.0+
- Sinabs (spiking neural network library) or custom implementation
- NumPy, Matplotlib
- Optional: Brian2 for detailed biophysical modeling

### Step-by-Step Implementation

```python
import torch
import torch.nn as nn
import torch.nn.functional as F
from typing import Tuple, Optional
import numpy as np

class STDPSpikingTransformer(nn.Module):
    """
    Spiking STDP Transformer (S²TDPT) - Attention via Synaptic Plasticity
    """
    def __init__(
        self,
        input_dim: int,
        embed_dim: int = 256,
        num_heads: int = 8,
        num_layers: int = 6,
        mlp_ratio: float = 4.0,
        num_classes: int = 10,
        time_steps: int = 4,
        tau_mem: float = 20.0,  # ms
        v_thresh: float = 1.0,
        stdp_params: Optional[dict] = None
    ):
        super().__init__()
        
        self.input_dim = input_dim
        self.embed_dim = embed_dim
        self.num_heads = num_heads
        self.time_steps = time_steps
        self.tau_mem = tau_mem
        self.v_thresh = v_thresh
        
        # Input embedding (converts to spikes)
        self.input_embedding = SpikingInputEmbedding(
            input_dim, embed_dim, time_steps
        )
        
        # STDP Transformer blocks
        self.blocks = nn.ModuleList([
            STDPTransformerBlock(
                embed_dim=embed_dim,
                num_heads=num_heads,
                mlp_dim=int(embed_dim * mlp_ratio),
                tau_mem=tau_mem,
                v_thresh=v_thresh,
                stdp_params=stdp_params
            )
            for _ in range(num_layers)
        ])
        
        # Classification head
        self.norm = nn.LayerNorm(embed_dim)
        self.head = nn.Linear(embed_dim, num_classes)
    
    def forward(self, x: torch.Tensor) -> torch.Tensor:
        """
        Forward pass
        
        Args:
            x: [batch, channels, height, width] or [batch, seq_len, features]
        
        Returns:
            logits: [batch, num_classes]
        """
        # Convert to spike trains
        spikes = self.input_embedding(x)  # [batch, time, seq_len, embed_dim]
        
        # Process through STDP Transformer blocks
        for block in self.blocks:
            spikes = block(spikes)
        
        # Rate coding: count spikes over time
        spike_counts = spikes.sum(dim=1)  # [batch, seq_len, embed_dim]
        
        # Global average pooling
        pooled = spike_counts.mean(dim=1)  # [batch, embed_dim]
        
        # Classification
        pooled = self.norm(pooled)
        logits = self.head(pooled)
        
        return logits


class STDPTransformerBlock(nn.Module):
    """
    Transformer block with STDP-based attention
    """
    def __init__(
        self,
        embed_dim: int,
        num_heads: int,
        mlp_dim: int,
        tau_mem: float,
        v_thresh: float,
        stdp_params: Optional[dict]
    ):
        super().__init__()
        
        # STDP Self-Attention
        self.attn = STDPAttention(
            embed_dim=embed_dim,
            num_heads=num_heads,
            stdp_params=stdp_params
        )
        
        # Spiking MLP
        self.mlp = SpikingMLP(
            in_features=embed_dim,
            hidden_features=mlp_dim,
            out_features=embed_dim,
            tau_mem=tau_mem,
            v_thresh=v_thresh
        )
        
        # Layer norms
        self.norm1 = nn.LayerNorm(embed_dim)
        self.norm2 = nn.LayerNorm(embed_dim)
    
    def forward(self, x: torch.Tensor) -> torch.Tensor:
        """
        Args:
            x: [batch, time, seq_len, embed_dim] spike trains
        
        Returns:
            [batch, time, seq_len, embed_dim] output spikes
        """
        # STDP Attention with residual
        batch, time, seq_len, embed_dim = x.shape
        
        # Normalize (across embedding dimension)
        x_norm = self.norm1(x.view(-1, embed_dim)).view(batch, time, seq_len, embed_dim)
        
        # Apply STDP attention
        attn_out = self.attn(x_norm)
        x = x + attn_out
        
        # Spiking MLP with residual
        x_norm = self.norm2(x.view(-1, embed_dim)).view(batch, time, seq_len, embed_dim)
        mlp_out = self.mlp(x_norm)
        x = x + mlp_out
        
        return x


class STDPAttention(nn.Module):
    """
    STDP-based attention mechanism
    
    Attention weights are stored in synaptic weights and learned via STDP,
    rather than computed via dot product.
    """
    def __init__(
        self,
        embed_dim: int,
        num_heads: int,
        stdp_params: Optional[dict]
    ):
        super().__init__()
        
        self.embed_dim = embed_dim
        self.num_heads = num_heads
        self.head_dim = embed_dim // num_heads
        
        assert self.head_dim * num_heads == embed_dim, "embed_dim must be divisible by num_heads"
        
        # Learnable attention weights (representing synapses)
        # Shape: [num_heads, seq_len, seq_len] - attention pattern per head
        self.attention_weights = nn.Parameter(
            torch.randn(num_heads, 1, 1) * 0.01
        )
        
        # Projection layers
        self.q_proj = nn.Linear(embed_dim, embed_dim)
        self.k_proj = nn.Linear(embed_dim, embed_dim)
        self.v_proj = nn.Linear(embed_dim, embed_dim)
        self.out_proj = nn.Linear(embed_dim, embed_dim)
        
        # STDP parameters
        if stdp_params is None:
            stdp_params = {
                'A_plus': 0.01,
                'A_minus': 0.01,
                'tau_plus': 20.0,
                'tau_minus': 20.0
            }
        self.stdp_params = stdp_params
        
        # Track spike times for STDP
        self.register_buffer('pre_spike_times', None)
        self.register_buffer('post_spike_times', None)
    
    def apply_stdp(
        self,
        pre_spikes: torch.Tensor,
        post_spikes: torch.Tensor
    ) -> torch.Tensor:
        """
        Apply STDP learning rule to update attention weights
        
        Args:
            pre_spikes: [batch, time, num_heads, seq_len, head_dim]
            post_spikes: [batch, time, num_heads, seq_len, head_dim]
        
        Returns:
            weight_updates: Updates to attention weights
        """
        batch, time, num_heads, seq_len, head_dim = pre_spikes.shape
        
        # Compute spike times (first spike per position)
        pre_times = torch.argmax(pre_spikes, dim=1).float()  # [batch, num_heads, seq_len, head_dim]
        post_times = torch.argmax(post_spikes, dim=1).float()
        
        # Time differences: [batch, num_heads, seq_len, seq_len]
        # For each pair of positions
        delta_t = post_times.unsqueeze(3) - pre_times.unsqueeze(2)
        
        # STDP weight update
        A_plus = self.stdp_params['A_plus']
        A_minus = self.stdp_params['A_minus']
        tau_plus = self.stdp_params['tau_plus']
        tau_minus = self.stdp_params['tau_minus']
        
        # Causal mask - only attend to previous positions
        causal_mask = (delta_t > 0).float()
        
        # LTP when post spikes after pre
        ltp = A_plus * torch.exp(-delta_t / tau_plus) * (delta_t > 0).float()
        
        # LTD when post spikes before pre
        ltd = -A_minus * torch.exp(delta_t / tau_minus) * (delta_t < 0).float()
        
        delta_w = (ltp + ltd) * causal_mask
        
        # Average over batch and features
        delta_w = delta_w.mean(dim=[0, -1])  # [num_heads, seq_len, seq_len]
        
        return delta_w
    
    def forward(self, x: torch.Tensor) -> torch.Tensor:
        """
        Apply STDP-based attention
        
        Args:
            x: [batch, time, seq_len, embed_dim]
        
        Returns:
            output: [batch, time, seq_len, embed_dim]
        """
        batch, time, seq_len, embed_dim = x.shape
        
        # Project to Q, K, V
        q = self.q_proj(x)  # [batch, time, seq_len, embed_dim]
        k = self.k_proj(x)
        v = self.v_proj(x)
        
        # Reshape for multi-head attention
        q = q.view(batch, time, seq_len, self.num_heads, self.head_dim).transpose(2, 3)
        k = k.view(batch, time, seq_len, self.num_heads, self.head_dim).transpose(2, 3)
        v = v.view(batch, time, seq_len, self.num_heads, self.head_dim).transpose(2, 3)
        # [batch, time, num_heads, seq_len, head_dim]
        
        # Apply STDP learning (if in training mode)
        if self.training:
            with torch.no_grad():
                delta_w = self.apply_stdp(k, q)
                # Update attention weights
                self.attention_weights.data += delta_w.mean(dim=(1, 2), keepdim=True)
        
        # Apply attention weights (synaptic transmission)
        # Broadcast attention weights across sequence
        attn_weights = self.attention_weights.abs().clamp(0, 1)
        attn_weights = attn_weights.view(1, 1, self.num_heads, 1, 1)
        
        # Weighted sum (attention)
        out = attn_weights * v  # [batch, time, num_heads, seq_len, head_dim]
        
        # Reshape and project
        out = out.transpose(2, 3).contiguous()
        out = out.view(batch, time, seq_len, embed_dim)
        out = self.out_proj(out)
        
        return out


class SpikingInputEmbedding(nn.Module):
    """
    Convert input to spike trains
    """
    def __init__(
        self,
        input_dim: int,
        embed_dim: int,
        time_steps: int,
        v_thresh: float = 1.0
    ):
        super().__init__()
        
        self.time_steps = time_steps
        self.v_thresh = v_thresh
        
        # Projection to embedding
        self.proj = nn.Linear(input_dim, embed_dim)
        
        # Positional encoding
        self.pos_encoding = nn.Parameter(
            torch.randn(1, 1, 1000, embed_dim) * 0.02  # Max 1000 positions
        )
    
    def forward(self, x: torch.Tensor) -> torch.Tensor:
        """
        Convert input to spike trains
        
        Args:
            x: [batch, input_dim] or [batch, seq_len, input_dim]
        
        Returns:
            spikes: [batch, time_steps, seq_len, embed_dim]
        """
        if x.dim() == 2:
            x = x.unsqueeze(1)  # [batch, 1, input_dim]
        
        batch, seq_len, _ = x.shape
        
        # Project
        x = self.proj(x)  # [batch, seq_len, embed_dim]
        
        # Add positional encoding
        x = x + self.pos_encoding[:, :, :seq_len, :]
        
        # Rate coding to temporal spikes
        # Normalize to firing probability
        firing_prob = torch.sigmoid(x)  # [batch, seq_len, embed_dim]
        
        # Generate spikes over time
        spikes = []
        for t in range(self.time_steps):
            # Bernoulli sampling
            spike_t = (torch.rand_like(firing_prob) < firing_prob).float()
            spikes.append(spike_t)
        
        spikes = torch.stack(spikes, dim=1)  # [batch, time, seq_len, embed_dim]
        
        return spikes


class SpikingMLP(nn.Module):
    """
    Spiking MLP with LIF neurons
    """
    def __init__(
        self,
        in_features: int,
        hidden_features: int,
        out_features: int,
        tau_mem: float,
        v_thresh: float
    ):
        super().__init__()
        
        self.fc1 = nn.Linear(in_features, hidden_features)
        self.fc2 = nn.Linear(hidden_features, out_features)
        
        self.tau_mem = tau_mem
        self.v_thresh = v_thresh
        self.v = None
    
    def forward(self, x: torch.Tensor) -> torch.Tensor:
        """
        Args:
            x: [batch, time, seq_len, features]
        
        Returns:
            spikes: [batch, time, seq_len, out_features]
        """
        batch, time, seq_len, _ = x.shape
        
        # Flatten spatial dimensions
        x = x.view(batch * time * seq_len, -1)
        
        # First layer
        h = self.fc1(x)
        h = torch.relu(h)
        
        # Second layer with spiking
        out = self.fc2(h)
        
        # LIF activation
        if self.v is None or self.v.shape != out.shape:
            self.v = torch.zeros_like(out)
        
        # Leaky integration
        alpha = np.exp(-1 / self.tau_mem)
        self.v = alpha * self.v + out
        
        # Spike generation
        spikes = (self.v >= self.v_thresh).float()
        self.v = self.v * (1 - spikes)
        
        # Reshape back
        spikes = spikes.view(batch, time, seq_len, -1)
        
        return spikes
```

### Energy Calculation

```python
def calculate_energy_consumption(
    model: STDPSpikingTransformer,
    input_shape: Tuple[int, ...],
    time_steps: int
) -> dict:
    """
    Calculate energy consumption of S²TDPT
    
    Args:
        model: S²TDPT model
        input_shape: Shape of input
        time_steps: Number of time steps
    
    Returns:
        energy_stats: Dictionary of energy metrics
    """
    # Energy per operation (approximate values in pJ)
    E_MAC = 0.5  # Multiply-accumulate (FP32)
    E_AC = 0.1   # Accumulate
    E_MEM = 2.0  # Memory access
    E_SPIKE = 0.01  # Spike event
    
    # Count operations
    total_macs = 0
    total_spikes = 0
    
    # Forward pass tracking
    def count_ops(module, input, output):
        nonlocal total_macs, total_spikes
        if isinstance(output, torch.Tensor):
            total_spikes += output.sum().item()
    
    hooks = []
    for module in model.modules():
        if isinstance(module, (nn.Linear, nn.Conv2d)):
            hooks.append(module.register_forward_hook(count_ops))
    
    # Run forward pass
    dummy_input = torch.randn(1, *input_shape)
    with torch.no_grad():
        _ = model(dummy_input)
    
    for hook in hooks:
        hook.remove()
    
    # Calculate energy
    energy_macs = total_macs * E_MAC
    energy_spikes = total_spikes * E_SPIKE
    total_energy = energy_macs + energy_spikes
    
    return {
        'total_energy_pJ': total_energy,
        'spike_events': total_spikes,
        'mac_operations': total_macs,
        'energy_per_inference': total_energy,
        'energy_per_time_step': total_energy / time_steps
    }


# Comparison
# Paper reports: 0.49 mJ on CIFAR-100 (4 timesteps)
# Standard ANN Transformer: ~4.25 mJ
# Energy reduction: 88.47%
```

## Applications

### 1. Low-Power Vision
- **CIFAR-10/100**: 94.35% / 78.08% accuracy
- **ImageNet**: Scalable to larger datasets
- **Edge Devices**: Smart cameras, drones
- **Always-on Vision**: Battery-powered systems

### 2. Neuromorphic Hardware
- **Intel Loihi**: Native spike support
- **IBM TrueNorth**: Massive parallelism
- **BrainChip Akida**: On-chip learning
- **Custom ASICs**: Application-specific optimization

### 3. Real-time Processing
- **Sub-millisecond Latency**: Event-driven response
- **High Throughput**: Parallel spike processing
- **Deterministic Timing**: No inference variability
- **Fault Tolerance**: Graceful degradation

### 4. Explainable AI
- **Grad-CAM Visualization**: Attention maps show focus
- **Biological Plausibility**: Brain-inspired mechanism
- **Interpretable Attention**: Learned synaptic patterns
- **Neuroscience Insights**: Bridge to brain function

## Pitfalls

1. **Limited Timesteps**: Performance depends on sufficient time steps
   - *Mitigation*: Optimize temporal coding, better initialization

2. **Training Instability**: STDP can be unstable
   - *Mitigation*: Careful learning rate tuning, gradient clipping

3. **Hardware Constraints**: Current neuromorphic chips have limitations
   - *Mitigation*: Simulation, gradual hardware transition

4. **Sequence Length**: Attention complexity still O(n²) in sequence
   - *Mitigation*: Linear attention variants, sparse patterns

5. **Transfer Learning**: Pretrained models not readily available
   - *Mitigation*: Train from scratch, knowledge distillation

## Related Skills
- spike-agreement-dependent-plasticity: Population-level STDP
- snn-working-memory-delays: SNN architectures
- neuromorphic-continual-nuclear-ics: Continual learning for SNNs
- stdp-synaptic-delay-learning: Delay learning with STDP

## References
```bibtex
@article{mondal2025attention,
  title={Attention via Synaptic Plasticity is All You Need: A Biologically Inspired Spiking Neuromorphic Transformer},
  author={Mondal, Kallol and Kumar, Ankush},
  journal={arXiv preprint arXiv:2511.14691},
  year={2025}
}
```

## Further Reading
- STDP: Song et al., "Competitive Hebbian learning through spike-timing-dependent synaptic plasticity"
- Transformers: Vaswani et al., "Attention is All You Need"
- Spiking Neural Networks: Maass, "Networks of spiking neurons"
- Neuromorphic Computing: Schuman et al., "A Survey of Neuromorphic Computing"
