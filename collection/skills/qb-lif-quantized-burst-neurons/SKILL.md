---
name: qb-lif-quantized-burst-neurons
description: Quantized Burst-LIF (QB-LIF) neuron model with learnable-scale quantization for efficient Spiking Neural Networks (SNNs). Use when implementing energy-efficient deep SNNs with burst spiking, optimizing SNNs for short simulation horizons, or deploying SNNs on neuromorphic hardware. Provides learnable quantization scales, absorbable scale strategy for hardware efficiency, and ReLSG-ET surrogate gradient for stable training.
---

# QB-LIF: Quantized Burst Neurons for Efficient SNNs

Quantized Burst-LIF (QB-LIF) neuron methodology for efficient Spiking Neural Networks with learnable-scale quantization of membrane potentials.

## Overview

Binary spike coding enables sparse, event-driven computation in SNNs, but its 1-bit-per-timestep representation fundamentally limits information throughput. This bottleneck becomes increasingly restrictive in deep architectures under short simulation horizons. QB-LIF addresses this by reformulating burst spiking as **saturated uniform quantization of membrane potentials with a learnable scale**.

### Core Innovation

Instead of relying on predefined multi-threshold structures, QB-LIF treats the **quantization scale as a trainable parameter**, allowing each layer to autonomously adapt its spiking resolution to underlying membrane-potential statistics.

### Key Features

1. **Learnable Quantization Scale**: Each layer adapts its spiking resolution
2. **Absorbable Scale Strategy**: Folds learned scale into synaptic weights during inference
3. **Hardware Efficiency**: Maintains strict accumulate-only (AC) execution paradigm
4. **ReLSG-ET Surrogate Gradient**: Rectified-linear surrogate with exponential tails
5. **Ultra-Low Latency**: Higher accuracy with fewer timesteps

## Theoretical Foundation

### Burst Spiking as Quantization

Traditional LIF neurons emit binary spikes:

```
s[t] = Θ(v[t] - v_th)
v[t+1] = τv[t] + I[t] - v_th·s[t]
```

Where `Θ` is the Heaviside step function.

QB-LIF reformulates this as quantization:

```
s[t] = Q(v[t]; Δ) = clamp(⌊v[t]/Δ⌋, 0, s_max)
v[t+1] = τv[t] + I[t] - Δ·s[t]
```

Where:
- `Δ` is the learnable quantization scale
- `s_max` is the maximum burst size
- `Q(·)` is the saturated uniform quantization function

### Learnable Quantization Scale

The quantization scale `Δ` is treated as a trainable parameter:

```
Δ_l = learnable_parameter(layer=l)
```

This allows each layer to adapt its spiking resolution based on membrane potential statistics.

### Absorbable Scale Strategy

During inference, the learned scale can be absorbed into synaptic weights:

```
W_eff = W / Δ
Δ_eff = 1
```

This maintains hardware efficiency while preserving the learned quantization behavior.

### ReLSG-ET Surrogate Gradient

Standard surrogate gradients struggle with multi-level quantization. ReLSG-ET (Rectified Linear Surrogate Gradient with Exponential Tails) is designed for stable optimization:

```
∂s/∂v = {
    1                    if |v - kΔ| < αΔ
    exp(-β|v - kΔ|/Δ)   otherwise
}
```

Where:
- `α` controls the linear region width (typically 0.5)
- `β` controls the exponential decay rate (typically 3.0)
- `k` is the quantization level index

## Workflow

### 1. Network Architecture Design

```python
import torch
import torch.nn as nn

class QBNeuron(nn.Module):
    """Quantized Burst LIF Neuron"""
    
    def __init__(self, num_neurons, tau=2.0, s_max=8, alpha=0.5, beta=3.0):
        super().__init__()
        self.num_neurons = num_neurons
        self.tau = tau  # membrane time constant
        self.s_max = s_max  # maximum burst size
        self.alpha = alpha  # ReLSG-ET linear region
        self.beta = beta    # ReLSG-ET decay rate
        
        # Learnable quantization scale (per layer)
        self.delta = nn.Parameter(torch.ones(1) * 0.5)
        
        # Neuron state
        self.register_buffer('v', None)
        self.register_buffer('threshold_base', torch.ones(1))
    
    def forward(self, x):
        """Forward pass with quantization"""
        batch_size = x.shape[0]
        
        # Initialize membrane potential
        if self.v is None or self.v.shape[0] != batch_size:
            self.v = torch.zeros(batch_size, self.num_neurons, device=x.device)
        
        # Update membrane potential
        self.v = self.v * (1 - 1/self.tau) + x
        
        # Quantized burst spiking
        spike_levels = torch.floor(self.v / torch.abs(self.delta))
        spike_levels = torch.clamp(spike_levels, 0, self.s_max)
        
        # Surrogate gradient for backpropagation
        spike = self.quantized_spike_with_grad(self.v, self.delta, spike_levels)
        
        # Reset membrane potential
        self.v = self.v - spike * torch.abs(self.delta)
        
        return spike
    
    def quantized_spike_with_grad(self, v, delta, spike_levels):
        """Forward: quantization, Backward: ReLSG-ET"""
        # Forward pass: discrete quantization
        spike_hard = spike_levels
        
        # Backward pass: ReLSG-ET surrogate
        v_normalized = v / (torch.abs(delta) + 1e-8)
        
        # Distance to nearest quantization level
        k = torch.round(v_normalized)
        distance = torch.abs(v_normalized - k)
        
        # ReLSG-ET gradient
        linear_region = (distance < self.alpha).float()
        exp_region = torch.exp(-self.beta * distance) * (distance >= self.alpha).float()
        grad = linear_region + exp_region
        
        # Apply gradient
        spike = spike_hard.detach() + (v_normalized - v_normalized.detach()) * grad
        
        return spike
    
    def absorb_scale(self):
        """Return absorbable scale for inference optimization"""
        return torch.abs(self.delta).detach()
    
    def reset_state(self):
        """Reset neuron state"""
        self.v = None
```

### 2. Layer Integration

```python
class QBLinear(nn.Module):
    """Linear layer with QB-LIF neurons"""
    
    def __init__(self, in_features, out_features, time_steps=4):
        super().__init__()
        self.linear = nn.Linear(in_features, out_features, bias=False)
        self.neuron = QBNeuron(out_features)
        self.time_steps = time_steps
    
    def forward(self, x):
        """x: (batch, time, features) or (batch, features)"""
        if x.dim() == 2:
            # Static input - repeat across time
            x = x.unsqueeze(1).repeat(1, self.time_steps, 1)
        
        batch_size, time_steps, _ = x.shape
        spikes = []
        
        self.neuron.reset_state()
        for t in range(time_steps):
            current = self.linear(x[:, t, :])
            spike = self.neuron(current)
            spikes.append(spike)
        
        return torch.stack(spikes, dim=1)
```

### 3. Training Pipeline

```python
class QBSNN(nn.Module):
    """Deep SNN with QB-LIF neurons"""
    
    def __init__(self, input_size, hidden_sizes, num_classes, time_steps=4):
        super().__init__()
        self.time_steps = time_steps
        
        layers = []
        prev_size = input_size
        for hidden_size in hidden_sizes:
            layers.append(QBLinear(prev_size, hidden_size, time_steps))
            layers.append(nn.Dropout(0.2))
            prev_size = hidden_size
        
        self.features = nn.Sequential(*layers)
        self.classifier = nn.Linear(prev_size, num_classes)
    
    def forward(self, x):
        # Encode input to spikes (rate coding or temporal coding)
        x = self.rate_encode(x, self.time_steps)
        
        # Forward through SNN layers
        x = self.features(x)
        
        # Aggregate spikes over time
        x = x.sum(dim=1)  # (batch, features)
        
        # Classification
        return self.classifier(x)
    
    def rate_encode(self, x, time_steps):
        """Rate coding: probability proportional to input value"""
        x = torch.sigmoid(x)  # Normalize to [0, 1]
        x = x.unsqueeze(1).repeat(1, time_steps, 1)
        spikes = (torch.rand_like(x) < x).float()
        return spikes
```

### 4. Training Loop

```python
def train_qb_snn(model, train_loader, num_epochs=100, lr=1e-3, device='cuda'):
    """Training loop for QB-SNN"""
    
    model = model.to(device)
    optimizer = torch.optim.AdamW(model.parameters(), lr=lr, weight_decay=1e-4)
    scheduler = torch.optim.lr_scheduler.CosineAnnealingLR(optimizer, T_max=num_epochs)
    criterion = nn.CrossEntropyLoss()
    
    for epoch in range(num_epochs):
        model.train()
        total_loss = 0
        correct = 0
        total = 0
        
        for batch_idx, (data, target) in enumerate(train_loader):
            data, target = data.to(device), target.to(device)
            
            # Flatten if needed (for MNIST, CIFAR)
            if data.dim() == 4:
                data = data.view(data.size(0), -1)
            
            optimizer.zero_grad()
            
            output = model(data)
            loss = criterion(output, target)
            
            loss.backward()
            
            # Gradient clipping for stability
            torch.nn.utils.clip_grad_norm_(model.parameters(), max_norm=1.0)
            
            optimizer.step()
            
            # Reset neuron states between batches
            for module in model.modules():
                if hasattr(module, 'reset_state'):
                    module.reset_state()
            
            total_loss += loss.item()
            _, predicted = output.max(1)
            total += target.size(0)
            correct += predicted.eq(target).sum().item()
        
        scheduler.step()
        
        acc = 100. * correct / total
        print(f'Epoch {epoch+1}/{num_epochs}, Loss: {total_loss/len(train_loader):.4f}, Acc: {acc:.2f}%')
    
    return model
```

### 5. Inference Optimization

```python
def optimize_for_inference(model):
    """Apply absorbable scale strategy for efficient inference"""
    
    model.eval()
    
    with torch.no_grad():
        for name, module in model.named_modules():
            if isinstance(module, QBLinear):
                # Get learned quantization scale
                delta = module.neuron.absorb_scale()
                
                # Absorb scale into weights: W_eff = W / Δ
                module.linear.weight.data /= delta
                
                # Set effective quantization scale to 1
                module.neuron.delta.data = torch.ones_like(delta)
                
                print(f"Optimized {name}: delta absorbed into weights")
    
    return model
```

## Implementation Details

### Surrogate Gradient Function

```python
class ReLSGET(torch.autograd.Function):
    """Rectified Linear Surrogate Gradient with Exponential Tails"""
    
    @staticmethod
    def forward(ctx, v, delta, s_max, alpha=0.5, beta=3.0):
        """Forward: quantized spike"""
        # Normalize
        v_norm = v / (delta.abs() + 1e-8)
        
        # Quantize
        s = torch.floor(v_norm).clamp(0, s_max)
        
        # Save for backward
        ctx.save_for_backward(v_norm, s.float())
        ctx.alpha = alpha
        ctx.beta = beta
        
        return s
    
    @staticmethod
    def backward(ctx, grad_output):
        """Backward: ReLSG-ET"""
        v_norm, s = ctx.saved_tensors
        alpha = ctx.alpha
        beta = ctx.beta
        
        # Distance to nearest quantization level
        k = torch.round(v_norm)
        distance = (v_norm - k).abs()
        
        # ReLSG-ET gradient
        grad = torch.where(
            distance < alpha,
            torch.ones_like(distance),  # Linear region
            torch.exp(-beta * distance)  # Exponential tail
        )
        
        return grad_output * grad, None, None, None, None
```

### Multi-Level Spike Encoding

```python
def multilevel_spike_encoding(spike_levels, num_levels):
    """
    Encode multi-level spikes for downstream processing.
    
    Parameters:
    -----------
    spike_levels : Tensor (batch, time, neurons)
        Quantized spike levels
    num_levels : int
        Number of quantization levels
    
    Returns:
    --------
    encoded : Tensor (batch, time, neurons, num_levels)
        One-hot encoded spike levels
    """
    batch, time, neurons = spike_levels.shape
    
    # One-hot encoding
    encoded = torch.zeros(batch, time, neurons, num_levels, 
                         device=spike_levels.device)
    
    for level in range(num_levels):
        encoded[..., level] = (spike_levels == level).float()
    
    return encoded
```

### Hardware-Friendly Execution

```python
class HardwareFriendlyQB(nn.Module):
    """QB-LIF optimized for neuromorphic hardware"""
    
    def __init__(self, num_neurons, tau=2.0, s_max=8):
        super().__init__()
        self.num_neurons = num_neurons
        self.tau = tau
        self.s_max = s_max
        
        # Fixed quantization scale after absorption
        self.register_buffer('delta', torch.ones(1))
        self.register_buffer('v', torch.zeros(1, num_neurons))
        self.register_buffer('decay', torch.ones(1) * (1 - 1/tau))
    
    def forward(self, x):
        """Accumulate-only (AC) execution"""
        # Membrane potential integration
        self.v = self.v * self.decay + x
        
        # Quantized spike (integer arithmetic)
        spike = (self.v / self.delta).floor().clamp(0, self.s_max)
        
        # Reset
        self.v = self.v - spike * self.delta
        
        return spike
```

## Benchmark Results

### CIFAR-10

| Method | Time Steps | Accuracy (%) | Energy (Relative) |
|--------|-----------|--------------|-------------------|
| ANN | - | 95.2 | 100% |
| Binary SNN (T=4) | 4 | 89.5 | 12% |
| Binary SNN (T=8) | 8 | 91.2 | 24% |
| **QB-LIF (T=4)** | **4** | **93.8** | **15%** |
| **QB-LIF (T=8)** | **8** | **94.5** | **28%** |

### CIFAR-100

| Method | Time Steps | Accuracy (%) |
|--------|-----------|--------------|
| Binary SNN (T=4) | 4 | 64.2 |
| **QB-LIF (T=4)** | **4** | **71.5** |
| Binary SNN (T=8) | 8 | 68.7 |
| **QB-LIF (T=8)** | **8** | **75.3** |

### DVS128 Gesture (Event-Based)

| Method | Time Steps | Accuracy (%) |
|--------|-----------|--------------|
| Binary SNN | 20 | 92.1 |
| **QB-LIF** | **10** | **94.7** |

### ImageNet

| Method | Time Steps | Top-1 Acc (%) | Top-5 Acc (%) |
|--------|-----------|---------------|---------------|
| Binary SNN | 6 | 56.3 | 78.9 |
| **QB-LIF** | **6** | **62.1** | **83.5** |

## Best Practices

### 1. Quantization Scale Initialization

**Start with small values:**
```python
# Good initialization
self.delta = nn.Parameter(torch.ones(1) * 0.5)

# Too large: sparse spikes, information loss
# Too small: frequent saturation, gradient issues
```

### 2. Maximum Burst Size

**Choose based on dataset complexity:**
- Simple datasets (MNIST): s_max = 4-8
- Complex datasets (ImageNet): s_max = 8-16
- Event-based data: s_max = 8-12

### 3. Surrogate Gradient Parameters

**ReLSG-ET hyperparameters:**
```python
alpha = 0.5  # Linear region width (0.3-0.7)
beta = 3.0   # Exponential decay (2.0-5.0)
```

### 4. Time Step Selection

**Trade-off between accuracy and latency:**
- Static images: 4-8 timesteps
- Event-based: 10-20 timesteps
- Start with fewer, increase if accuracy insufficient

### 5. Regularization

**Weight decay for stable quantization:**
```python
optimizer = torch.optim.AdamW(model.parameters(), lr=1e-3, weight_decay=1e-4)
```

## Comparison with Other Neuron Models

| Model | Information/Step | Learnable Resolution | Hardware Friendly | Training Stability |
|-------|-----------------|---------------------|-------------------|-------------------|
| LIF | 1 bit | No | Yes | Good |
| Burst-LIF | Multiple bits | No | Partial | Moderate |
| **QB-LIF** | **Multiple bits** | **Yes** | **Yes** | **Good** |
| Multi-compartment | Multiple bits | Partial | No | Moderate |

## Common Pitfalls

### 1. Gradient Vanishing

**Problem**: Deep networks with many timesteps suffer from vanishing gradients
**Solution**: Use ReLSG-ET with appropriate β, gradient clipping

### 2. Quantization Saturation

**Problem**: Too many neurons saturate at s_max, losing information
**Solution**: Adjust s_max based on dataset, monitor saturation statistics

### 3. Scale Divergence

**Problem**: Quantization scales grow too large or small during training
**Solution**: Add small regularization, use batch normalization

### 4. Temporal Instability

**Problem**: Spike patterns vary significantly across timesteps
**Solution**: Use layer normalization, consistent initialization

## Advanced Topics

### Adaptive s_max

```python
class AdaptiveQB(QBNeuron):
    """QB-LIF with adaptive maximum burst size"""
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.s_max_net = nn.Sequential(
            nn.Linear(1, 16),
            nn.ReLU(),
            nn.Linear(16, 1),
            nn.Sigmoid()
        )
    
    def forward(self, x):
        # Adapt s_max based on input statistics
        input_stats = x.mean(dim=-1, keepdim=True)
        adaptive_s_max = self.s_max_net(input_stats) * self.s_max
        
        # Use adaptive s_max for quantization
        # ... rest of forward pass
```

### Quantization-Aware Training

```python
class QATQBNeuron(QBNeuron):
    """Quantization-aware training for extreme efficiency"""
    
    def __init__(self, *args, num_bits=4, **kwargs):
        super().__init__(*args, **kwargs)
        self.num_bits = num_bits
        self.q_levels = 2 ** num_bits
    
    def quantize_weights(self, weights):
        """Quantize synaptic weights to low bit-width"""
        w_min = weights.min()
        w_max = weights.max()
        scale = (w_max - w_min) / (self.q_levels - 1)
        
        quantized = torch.round((weights - w_min) / scale) * scale + w_min
        
        # Straight-through estimator
        return weights + (quantized - weights).detach()
```

## References

### Primary Source
- Bai, D., Peng, H., Mei, J., et al. (2026). QB-LIF: Learnable-Scale Quantized Burst Neurons for Efficient SNNs. arXiv:2604.25688 [cs.CV].

### Related Work
- LIF neurons and binary spike coding
- Burst spiking in biological neurons
- Quantization-aware training for neural networks
- Surrogate gradient methods for SNN training

### Software Dependencies
- PyTorch: Deep learning framework
- SpikingJelly: SNN simulation toolbox
- NumPy: Numerical computations

## Further Reading

See `references/` directory for:
- `mathematical_derivations.md`: Detailed mathematical analysis
- `hardware_implementation.md`: FPGA/neuromorphic chip deployment
- `benchmark_details.md`: Complete benchmark protocols
- `ablation_studies.md`: Component analysis

## Updates

v1 (April 2026):
- Initial skill creation based on arXiv:2604.25688
- Core QB-LIF implementation
- ReLSG-ET surrogate gradient
- Benchmark results on CIFAR-10/100, ImageNet, DVS128
