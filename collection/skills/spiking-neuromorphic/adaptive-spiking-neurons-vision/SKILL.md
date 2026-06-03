---
name: adaptive-spiking-neurons-vision
description: "Adaptive Spiking Neuron (ASN) methodology for vision and language modeling. Implements adaptive spiking neurons capable of handling large-scale applications with temporal dynamics and multi-timescale processing. Activation: adaptive spiking neuron, ASN, vision SNN, language SNN, large-scale spiking neural network, temporal dynamics."
---

# Adaptive Spiking Neurons for Vision and Language Modeling

## Description

Implementation of Adaptive Spiking Neurons (ASNs) for large-scale vision and language modeling tasks. This methodology extends traditional spiking neural networks with adaptive mechanisms that enable handling complex temporal dynamics at scale, making SNNs suitable for applications previously dominated by artificial neural networks.

Based on research from arXiv:2604.12365v1 - "Adaptive Spiking Neurons for Vision and Language Modeling" by Chenlin Zhou et al.

## Activation Keywords

- adaptive spiking neuron
- ASN
- vision SNN
- language SNN
- large-scale spiking neural network
- temporal dynamics
- multi-timescale processing
- adaptive SNN
- spiking transformer
- 自适应脉冲神经元
- 脉冲神经网络视觉

## Tools Used

- `write`: Create ASN model implementations
- `exec`: Run training and inference
- `read`: Load model configurations
- `patch`: Modify neuron parameters

## Core Concepts

### 1. Adaptive Spiking Neuron Model

Adaptive spiking neurons extend standard LIF neurons with:
- **Adaptive threshold**: Threshold potential increases after each spike
- **Multiple timescales**: Different time constants for different dynamics
- **Activity-dependent adaptation**: Modulation based on firing history

Mathematical formulation:
```
τ_m * dv/dt = -(v - v_rest) + R * I(t)
τ_ada * dθ/dt = -(θ - θ_0) + Δθ * S(t)

where:
- v: membrane potential
- θ: adaptive threshold
- S(t): spike train (1 at spike times, 0 otherwise)
- τ_m, τ_ada: membrane and adaptation time constants
```

### 2. Multi-Timescale Processing

Handle different temporal scales:
- **Fast dynamics**: Millisecond-scale spike timing
- **Slow dynamics**: Second-scale adaptation
- **Ultra-slow**: Minute-scale plasticity

### 3. Scalability Features

For large-scale applications:
- Efficient spike propagation
- Batched computation
- Sparse activation patterns
- Hardware-friendly operations

## Implementation

### Step 1: ASN Neuron Model

```python
import torch
import torch.nn as nn

class AdaptiveSpikingNeuron(nn.Module):
    """
    Adaptive Spiking Neuron with multi-timescale dynamics.
    
    Args:
        tau_m: Membrane time constant (ms)
        tau_adp: Adaptation time constant (ms)
        v_rest: Resting potential (mV)
        v_thresh: Base threshold (mV)
        delta_theta: Threshold adaptation increment (mV)
    """
    
    def __init__(self, tau_m=20.0, tau_adp=2000.0, 
                 v_rest=-70.0, v_thresh=-55.0, delta_theta=2.0):
        super().__init__()
        self.tau_m = tau_m
        self.tau_adp = tau_adp
        self.v_rest = v_rest
        self.v_thresh_base = v_thresh
        self.delta_theta = delta_theta
        
        # State variables
        self.v = None  # Membrane potential
        self.theta = None  # Adaptive threshold
        self.spike = None  # Spike output
        
    def forward(self, input_current, dt=1.0):
        """
        Forward pass with adaptive spiking dynamics.
        
        Args:
            input_current: Input current (batch_size, num_neurons)
            dt: Time step (ms)
        
        Returns:
            spike: Binary spike output
            v: Updated membrane potential
        """
        if self.v is None:
            self.reset(input_current.shape)
        
        # Membrane potential update (exponential Euler)
        alpha = torch.exp(-dt / self.tau_m)
        self.v = alpha * self.v + (1 - alpha) * self.v_rest + input_current
        
        # Adaptive threshold decay
        beta = torch.exp(-dt / self.tau_adp)
        self.theta = beta * self.theta + (1 - beta) * self.v_thresh_base
        
        # Spike generation
        self.spike = (self.v >= self.theta).float()
        
        # Reset and threshold adaptation
        self.v = self.v * (1 - self.spike) + self.v_rest * self.spike
        self.theta = self.theta + self.delta_theta * self.spike
        
        return self.spike, self.v
    
    def reset(self, shape):
        """Reset neuron states."""
        device = next(self.parameters()).device
        self.v = torch.full(shape, self.v_rest, device=device)
        self.theta = torch.full(shape, self.v_thresh_base, device=device)
        self.spike = torch.zeros(shape, device=device)
```

### Step 2: ASN Layer with Surrogate Gradient

```python
class ASNLayer(nn.Module):
    """
    Adaptive Spiking Neuron layer with surrogate gradient training.
    """
    
    def __init__(self, input_size, hidden_size, num_steps=10):
        super().__init__()
        self.input_size = input_size
        self.hidden_size = hidden_size
        self.num_steps = num_steps
        
        # Linear transformation
        self.linear = nn.Linear(input_size, hidden_size)
        
        # Adaptive spiking neurons
        self.neurons = AdaptiveSpikingNeuron()
        
    def forward(self, x):
        """
        Forward pass through time.
        
        Args:
            x: Input tensor (batch_size, seq_len, input_size)
        
        Returns:
            spike_record: Spike trains (batch_size, seq_len, hidden_size)
            v_record: Membrane potentials (batch_size, seq_len, hidden_size)
        """
        batch_size, seq_len, _ = x.shape
        
        # Initialize recording
        spike_record = []
        v_record = []
        
        # Reset neuron states
        self.neurons.reset((batch_size, self.hidden_size))
        
        # Temporal processing
        for t in range(seq_len):
            # Linear transformation
            current = self.linear(x[:, t, :])
            
            # Neuron dynamics with surrogate gradient
            spike, v = self.surrogate_forward(current)
            
            spike_record.append(spike)
            v_record.append(v)
        
        # Stack over time
        spike_record = torch.stack(spike_record, dim=1)
        v_record = torch.stack(v_record, dim=1)
        
        return spike_record, v_record
    
    def surrogate_forward(self, current):
        """Forward with surrogate gradient for backpropagation."""
        # Store pre-activation for gradient computation
        v_pre = self.neurons.v.clone() if self.neurons.v is not None else None
        
        # Forward pass
        spike, v = self.neurons(current)
        
        # Apply surrogate gradient during backward
        if self.training:
            spike = SpikeFunction.apply(v_pre, self.neurons.theta, spike)
        
        return spike, v


class SpikeFunction(torch.autograd.Function):
    """
    Surrogate gradient function for backpropagation through spikes.
    Uses fast sigmoid surrogate.
    """
    
    @staticmethod
    def forward(ctx, v_pre, threshold, spike):
        ctx.save_for_backward(v_pre, threshold)
        ctx.spike = spike
        return spike
    
    @staticmethod
    def backward(ctx, grad_output):
        v_pre, threshold = ctx.saved_tensors
        spike = ctx.spike
        
        # Fast sigmoid surrogate gradient
        alpha = 2.0
        surrogate = alpha / (1.0 + (alpha * (v_pre - threshold)).abs()) ** 2
        
        return grad_output * surrogate, None, None
```

### Step 3: Vision ASN Network

```python
class VisionASN(nn.Module):
    """
    Adaptive Spiking Neural Network for vision tasks.
    """
    
    def __init__(self, num_classes=10, T=10):
        super().__init__()
        self.T = T  # Number of time steps
        
        # Encoding layer (rate coding or learnable encoding)
        self.encoder = nn.Sequential(
            nn.Conv2d(3, 64, kernel_size=3, padding=1),
            nn.BatchNorm2d(64)
        )
        
        # ASN layers
        self.asn1 = ASNConvLayer(64, 128, kernel_size=3, num_steps=T)
        self.asn2 = ASNConvLayer(128, 256, kernel_size=3, num_steps=T)
        self.asn3 = ASNConvLayer(256, 512, kernel_size=3, num_steps=T)
        
        # Classification head
        self.classifier = nn.Linear(512, num_classes)
        
    def forward(self, x):
        """
        Args:
            x: Input images (batch_size, 3, H, W)
        
        Returns:
            output: Class logits (batch_size, num_classes)
        """
        batch_size = x.shape[0]
        
        # Encode to spike trains
        encoded = self.encode(x)
        
        # ASN processing
        x1, _ = self.asn1(encoded)
        x2, _ = self.asn2(x1)
        x3, _ = self.asn3(x2)
        
        # Temporal pooling
        x_pooled = x3.mean(dim=2).mean(dim=2)  # Spatial average pooling
        x_temporal = x_pooled.mean(dim=1)  # Temporal average
        
        # Classification
        output = self.classifier(x_temporal)
        
        return output
    
    def encode(self, x):
        """Convert images to spike trains."""
        # Poisson rate coding
        features = self.encoder(x)
        
        # Generate spike trains over time
        batch_size, C, H, W = features.shape
        spike_trains = []
        
        for t in range(self.T):
            # Poisson spike generation
            rates = torch.sigmoid(features)
            spikes = torch.poisson(rates).clamp(max=1.0)
            spike_trains.append(spikes)
        
        return torch.stack(spike_trains, dim=1)  # (batch, T, C, H, W)


class ASNConvLayer(nn.Module):
    """Convolutional ASN layer."""
    
    def __init__(self, in_channels, out_channels, kernel_size, num_steps=10):
        super().__init__()
        self.conv = nn.Conv2d(in_channels, out_channels, kernel_size, padding=kernel_size//2)
        self.bn = nn.BatchNorm2d(out_channels)
        self.neurons = AdaptiveSpikingNeuron()
        self.num_steps = num_steps
    
    def forward(self, x):
        """
        Args:
            x: (batch, T, C, H, W)
        """
        batch_size, T, C, H, W = x.shape
        spike_record = []
        
        self.neurons.reset((batch_size, self.conv.out_channels, H, W))
        
        for t in range(T):
            conv_out = self.conv(x[:, t])
            conv_out = self.bn(conv_out)
            
            spike, v = self.neurons(conv_out)
            spike_record.append(spike)
        
        return torch.stack(spike_record, dim=1), None
```

### Step 4: Language ASN Network

```python
class LanguageASN(nn.Module):
    """
    Adaptive Spiking Neural Network for language modeling.
    """
    
    def __init__(self, vocab_size, embed_dim=512, hidden_dim=1024, num_layers=6, T=20):
        super().__init__()
        self.T = T
        
        # Embedding
        self.embedding = nn.Embedding(vocab_size, embed_dim)
        
        # ASN transformer layers
        self.layers = nn.ModuleList([
            ASNTransformerLayer(embed_dim, hidden_dim, T)
            for _ in range(num_layers)
        ])
        
        # Output head
        self.lm_head = nn.Linear(embed_dim, vocab_size)
        
    def forward(self, input_ids):
        """
        Args:
            input_ids: Token ids (batch_size, seq_len)
        
        Returns:
            logits: Language modeling logits (batch_size, seq_len, vocab_size)
        """
        # Embed tokens
        embeddings = self.embedding(input_ids)
        
        # Encode to spike trains
        spike_input = self.temporal_encode(embeddings)
        
        # ASN processing
        x = spike_input
        for layer in self.layers:
            x = layer(x)
        
        # Decode from spike trains
        output = self.temporal_decode(x)
        
        # Language modeling head
        logits = self.lm_head(output)
        
        return logits
    
    def temporal_encode(self, embeddings):
        """Convert embeddings to temporal spike patterns."""
        # Time-based coding: different times represent different features
        batch_size, seq_len, embed_dim = embeddings.shape
        
        spike_trains = []
        for t in range(self.T):
            # Feature-wise time encoding
            time_mask = (torch.arange(embed_dim) % self.T == t).float()
            time_mask = time_mask.unsqueeze(0).unsqueeze(0).to(embeddings.device)
            
            spikes = (embeddings * time_mask).clamp(max=1.0)
            spike_trains.append(spikes)
        
        return torch.stack(spike_trains, dim=1)  # (batch, T, seq, embed)
    
    def temporal_decode(self, spike_trains):
        """Aggregate spike trains over time."""
        # Sum spikes across time dimension
        return spike_trains.sum(dim=1)


class ASNTransformerLayer(nn.Module):
    """ASN-based transformer layer with attention."""
    
    def __init__(self, embed_dim, hidden_dim, num_steps):
        super().__init__()
        self.attention = ASNMultiHeadAttention(embed_dim, num_steps)
        self.feedforward = ASNFeedForward(embed_dim, hidden_dim, num_steps)
        self.norm1 = nn.LayerNorm(embed_dim)
        self.norm2 = nn.LayerNorm(embed_dim)
    
    def forward(self, x):
        # Attention block
        attn_out = self.attention(self.norm1(x))
        x = x + attn_out
        
        # Feedforward block
        ff_out = self.feedforward(self.norm2(x))
        x = x + ff_out
        
        return x


class ASNMultiHeadAttention(nn.Module):
    """Multi-head attention with ASN dynamics."""
    
    def __init__(self, embed_dim, num_steps, num_heads=8):
        super().__init__()
        self.num_heads = num_heads
        self.head_dim = embed_dim // num_heads
        self.num_steps = num_steps
        
        self.q_proj = nn.Linear(embed_dim, embed_dim)
        self.k_proj = nn.Linear(embed_dim, embed_dim)
        self.v_proj = nn.Linear(embed_dim, embed_dim)
        self.out_proj = nn.Linear(embed_dim, embed_dim)
        
        self.neurons = AdaptiveSpikingNeuron()
    
    def forward(self, x):
        """
        Args:
            x: (batch, T, seq, embed)
        """
        batch_size, T, seq_len, embed_dim = x.shape
        
        # Project queries, keys, values
        Q = self.q_proj(x)  # (batch, T, seq, embed)
        K = self.k_proj(x)
        V = self.v_proj(x)
        
        # Multi-head reshape
        Q = Q.view(batch_size, T, seq_len, self.num_heads, self.head_dim)
        K = K.view(batch_size, T, seq_len, self.num_heads, self.head_dim)
        V = V.view(batch_size, T, seq_len, self.num_heads, self.head_dim)
        
        # Attention computation with ASN dynamics
        outputs = []
        self.neurons.reset((batch_size, seq_len, self.num_heads, self.head_dim))
        
        for t in range(T):
            # Attention scores
            scores = torch.einsum('bqhd,bkhd->bhqk', Q[:, t], K[:, t])
            scores = scores / (self.head_dim ** 0.5)
            attn_weights = torch.softmax(scores, dim=-1)
            
            # Attention output
            attn_out = torch.einsum('bhqk,bkhd->bqhd', attn_weights, V[:, t])
            
            # ASN processing
            attn_flat = attn_out.reshape(batch_size, seq_len, -1)
            spike, v = self.neurons(attn_flat)
            
            outputs.append(spike)
        
        output = torch.stack(outputs, dim=1)
        output = self.out_proj(output.view(batch_size, T, seq_len, embed_dim))
        
        return output
```

## Training

```python
def train_asn_model(model, train_loader, epochs=100, lr=1e-4):
    """Train ASN model with surrogate gradients."""
    optimizer = torch.optim.AdamW(model.parameters(), lr=lr)
    scheduler = torch.optim.lr_scheduler.CosineAnnealingLR(optimizer, epochs)
    criterion = nn.CrossEntropyLoss()
    
    for epoch in range(epochs):
        model.train()
        total_loss = 0
        
        for batch_idx, (data, target) in enumerate(train_loader):
            data, target = data.to(device), target.to(device)
            
            optimizer.zero_grad()
            output = model(data)
            loss = criterion(output, target)
            
            loss.backward()
            optimizer.step()
            
            total_loss += loss.item()
        
        scheduler.step()
        
        if epoch % 10 == 0:
            print(f"Epoch {epoch}, Loss: {total_loss / len(train_loader):.4f}")
```

## Error Handling

### Gradient Vanishing

If gradients vanish during training:
1. Increase surrogate gradient slope (alpha)
2. Use layer normalization
3. Implement residual connections
4. Check learning rate (may be too high)

### Spike Rate Too Low

If neurons rarely spike:
1. Reduce adaptive threshold increment (delta_theta)
2. Increase input current strength
3. Check encoding (ensure adequate input spike rates)
4. Adjust membrane time constant

### Memory Issues

For large-scale models:
1. Use gradient checkpointing
2. Reduce batch size
3. Use sparse attention patterns
4. Consider mixed precision training

## References

- Zhou, C., Guo, S., Wang, J., et al. (2026). Adaptive Spiking Neurons for Vision and Language Modeling. arXiv:2604.12365v1.
- Neftci, E. O., Mostafa, H., & Zenke, F. (2019). Surrogate gradient learning in spiking neural networks. IEEE Signal Processing Magazine.
- Zenke, F., & Vogels, T. P. (2021). The remarkable robustness of surrogate gradient learning for instilling complex function in spiking neural networks. Neural Computation.

## Related Skills

- `wta-spiking-transformer-language`: Winner-Take-All Spiking Transformer
- `spiking-neural-network-analysis`: General SNN analysis
- `brain-digital-twins-execution-semantics`: Execution semantics framework
