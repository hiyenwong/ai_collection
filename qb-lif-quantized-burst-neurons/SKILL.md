---
name: qb-lif-quantized-burst-neurons
description: "QB-LIF: Learnable-Scale Quantized Burst Neurons for Efficient Spiking Neural Networks. Novel neuron model that learns optimal quantization scales during training, achieving higher information throughput than binary spikes while maintaining energy efficiency. Keywords: QB-LIF, quantized burst neurons, SNN quantization, learnable scale, spiking neural networks, neuromorphic hardware, burst coding."
---

# QB-LIF: Learnable-Scale Quantized Burst Neurons for Efficient SNNs

## Overview

QB-LIF (Quantized Burst Leaky Integrate-and-Fire) addresses the fundamental limitation of binary spike coding in Spiking Neural Networks (SNNs). While binary spikes enable sparse event-driven computation, the 1-bit-per-timestep representation limits information throughput, becoming increasingly restrictive in deep architectures and complex tasks.

## Core Innovation

**Learnable-Scale Quantization**: Instead of fixed quantization scales, QB-LIF learns optimal quantization levels during training through:
- Learnable quantization scales (burst sizes)
- Straight-through estimator for gradient flow
- Balance between information capacity and energy efficiency

## Technical Framework

### 1. Quantized Burst Neuron Model

Traditional LIF neuron:
```
V[t] = αV[t-1] + I[t]
S[t] = 1 if V[t] ≥ θ else 0
V[t] = V[t] - θ if S[t] = 1
```

QB-LIF neuron with learnable burst scale:
```
V[t] = αV[t-1] + I[t]
B[t] = clamp(round(V[t]/θ_scale), 0, B_max)  # Burst count
S[t] = B[t]  # Multi-bit spike output
V[t] = V[t] - B[t] × θ_scale if B[t] > 0

where θ_scale is learnable per neuron/channel
```

### 2. Learnable Quantization Scale

```python
class LearnableQuantizationScale(nn.Module):
    """
    Learnable quantization scale for burst neurons.
    """
    def __init__(self, channels, num_bits=3, init_scale=1.0):
        super().__init__()
        self.num_bits = num_bits
        self.max_val = 2 ** num_bits - 1
        
        # Learnable scale parameter (per channel)
        self.log_scale = nn.Parameter(
            torch.ones(channels) * torch.log(torch.tensor(init_scale))
        )
        
    def forward(self, membrane_potential):
        """
        Quantize membrane potential to burst count.
        
        Args:
            membrane_potential: [B, C, H, W] or [B, C, T]
        
        Returns:
            burst_count: [B, C, H, W] quantized burst spikes
        """
        scale = torch.exp(self.log_scale).view(1, -1, 1, 1)
        
        # Quantize to burst count
        normalized = membrane_potential / scale
        
        # Straight-through estimator
        burst_hard = torch.clamp(
            torch.round(normalized),
            0,
            self.max_val
        )
        
        # Soft for gradients during training
        if self.training:
            burst_soft = normalized
            burst = burst_soft + (burst_hard - burst_soft).detach()
        else:
            burst = burst_hard
        
        return burst
```

### 3. QB-LIF Neuron Implementation

```python
class QBLIFNeuron(nn.Module):
    """
    Quantized Burst Leaky Integrate-and-Fire Neuron.
    
    Args:
        channels: Number of input/output channels
        num_bits: Number of bits for burst coding (default: 3)
        tau_mem: Membrane time constant
        tau_syn: Synaptic time constant
        spike_grad: Surrogate gradient function
    """
    def __init__(
        self,
        channels,
        num_bits=3,
        tau_mem=20.0,
        tau_syn=5.0,
        spike_grad='fast_sigmoid'
    ):
        super().__init__()
        self.channels = channels
        self.num_bits = num_bits
        self.max_burst = 2 ** num_bits - 1
        
        # Learnable quantization scale
        self.quantizer = LearnableQuantizationScale(channels, num_bits)
        
        # Membrane and synaptic decay
        self.alpha = nn.Parameter(torch.exp(-1.0 / tau_mem))
        self.beta = nn.Parameter(torch.exp(-1.0 / tau_syn))
        
        # Threshold for spike generation
        self.threshold = nn.Parameter(torch.ones(channels) * 0.5)
        
        self.register_buffer('mem', None)
        self.register_buffer('syn', None)
        
    def reset_states(self, batch_size, spatial_shape):
        """Reset membrane and synaptic states."""
        H, W = spatial_shape
        self.mem = torch.zeros(batch_size, self.channels, H, W)
        self.syn = torch.zeros(batch_size, self.channels, H, W)
        
    def forward(self, input_current, return_states=False):
        """
        Forward pass with quantized burst output.
        
        Args:
            input_current: [B, C, H, W] input current at time t
            return_states: Whether to return internal states
            
        Returns:
            burst_spikes: [B, C, H, W] quantized burst output
        """
        if self.mem is None:
            self.reset_states(input_current.size(0), input_current.shape[2:])
        
        # Update synaptic current
        self.syn = self.beta * self.syn + input_current
        
        # Update membrane potential
        self.mem = self.alpha * self.mem + self.syn
        
        # Quantize to burst spikes
        burst = self.quantizer(self.mem)
        
        # Subtract emitted spikes from membrane
        scale = torch.exp(self.quantizer.log_scale).view(1, -1, 1, 1)
        self.mem = self.mem - burst * scale
        
        if return_states:
            return burst, (self.mem, self.syn)
        return burst
```

### 4. Multi-Bit Spike Representation

```python
class MultiBitSpikeConv(nn.Module):
    """
    Convolutional layer optimized for multi-bit spike inputs.
    More efficient than binary spike accumulation.
    """
    def __init__(self, in_channels, out_channels, kernel_size, num_bits=3):
        super().__init__()
        self.num_bits = num_bits
        self.weight = nn.Parameter(
            torch.randn(out_channels, in_channels, kernel_size, kernel_size)
        )
        self.bias = nn.Parameter(torch.zeros(out_channels))
        
        # Decompose weights for bit-wise computation
        self.register_buffer('weight_bit_masks', None)
        
    def forward(self, multi_bit_spikes):
        """
        Compute convolution with multi-bit spikes efficiently.
        
        Args:
            multi_bit_spikes: [B, C, H, W] with values in [0, 2^num_bits-1]
            
        Returns:
            output: [B, out_C, H', W']
        """
        B, C, H, W = multi_bit_spikes.shape
        
        # Decompose into bit planes
        output = torch.zeros(
            B, self.out_channels,
            H - self.kernel_size + 1,
            W - self.kernel_size + 1
        )
        
        for bit in range(self.num_bits):
            # Extract bit plane
            bit_mask = ((multi_bit_spikes >> bit) & 1).float()
            
            # Convolve with weight scaled by 2^bit
            bit_weight = self.weight * (2 ** bit)
            output += F.conv2d(bit_mask, bit_weight, self.bias)
        
        return output
```

## Training Strategy

### Surrogate Gradient for Burst

```python
class BurstSurrogateGradient(torch.autograd.Function):
    """
    Surrogate gradient for burst quantization.
    Combines quantization-aware training with SNN-specific gradients.
    """
    @staticmethod
    def forward(ctx, input, scale, max_val):
        # Forward: hard quantization
        normalized = input / scale
        burst = torch.clamp(torch.round(normalized), 0, max_val)
        ctx.save_for_backward(input, scale, normalized, burst)
        ctx.max_val = max_val
        return burst
    
    @staticmethod
    def backward(ctx, grad_output):
        input, scale, normalized, burst = ctx.saved_tensors
        
        # Surrogate: derivative of fast sigmoid
        # near quantization boundaries
        alpha = 0.3
        sigmoid_deriv = alpha / (1 + alpha * torch.abs(normalized))
        
        # Gradient w.r.t input
        grad_input = grad_output * sigmoid_deriv / scale
        
        # Gradient w.r.t scale (learnable parameter)
        grad_scale = -grad_output * normalized * sigmoid_deriv / scale
        
        return grad_input, grad_scale.sum(), None
```

### QB-LIF Training Loop

```python
def train_qb_lif(model, train_loader, optimizer, num_epochs, device='cuda'):
    """
    Train SNN with QB-LIF neurons.
    
    Args:
        model: SNN model with QB-LIF layers
        train_loader: DataLoader for training data
        optimizer: PyTorch optimizer
        num_epochs: Number of training epochs
        device: Device to train on
    """
    model.train()
    
    for epoch in range(num_epochs):
        total_loss = 0
        total_spikes = 0
        total_bits = 0
        
        for batch_idx, (data, target) in enumerate(train_loader):
            data, target = data.to(device), target.to(device)
            optimizer.zero_grad()
            
            # Reset neuron states
            for module in model.modules():
                if isinstance(module, QBLIFNeuron):
                    module.reset_states(data.size(0), data.shape[2:])
            
            # Time-stepped forward pass
            T = 10  # Time steps
            outputs = []
            spike_counts = []
            
            for t in range(T):
                output = model(data)
                outputs.append(output)
                
                # Count spikes (weighted by burst magnitude)
                for module in model.modules():
                    if isinstance(module, QBLIFNeuron):
                        if hasattr(module, 'last_spike'):
                            total_spikes += module.last_spike.sum().item()
                            total_bits += (module.last_spike > 0).sum().item() * module.num_bits
            
            # Loss: classification + regularization
            avg_output = torch.stack(outputs).mean(dim=0)
            ce_loss = F.cross_entropy(avg_output, target)
            
            # Sparsity regularization (encourage efficient coding)
            sparsity_loss = total_spikes / (T * data.size(0) * 1000)  # Normalize
            
            loss = ce_loss + 0.01 * sparsity_loss
            loss.backward()
            optimizer.step()
            
            total_loss += loss.item()
        
        print(f"Epoch {epoch}: Loss={total_loss/len(train_loader):.4f}, "
              f"Efficiency={total_bits/max(total_spikes, 1):.2f} bits/spike")
```

## Performance Results

### ImageNet Classification (T=10 timesteps)

| Model | Neuron | Bits | Top-1 Acc | Energy (mJ) | Info Throughput |
|-------|--------|------|-----------|-------------|-----------------|
| ResNet-18 | LIF | 1 | 71.2% | 45.3 | 1.0x |
| ResNet-18 | Burst-LIF | 2 | 72.8% | 52.1 | 1.8x |
| ResNet-18 | **QB-LIF** | 3 | **74.5%** | **48.7** | **2.7x** |
| VGG-16 | LIF | 1 | 73.5% | 62.4 | 1.0x |
| VGG-16 | **QB-LIF** | 3 | **76.2%** | **65.1** | **2.5x** |

### Neuromorphic Dataset (N-MNIST, DVS-Gesture)

| Dataset | Method | Accuracy | Event Reduction | Latency |
|---------|--------|----------|-----------------|---------|
| N-MNIST | Binary SNN | 98.7% | 1.0x | 300ms |
| N-MNIST | **QB-LIF** | **99.1%** | **0.6x** | **150ms** |
| DVS-Gesture | Binary SNN | 94.3% | 1.0x | 500ms |
| DVS-Gesture | **QB-LIF** | **96.8%** | **0.5x** | **250ms** |

## Hardware Implementation

### Bit-Parallel Processing

```verilog
// Verilog-style pseudocode for multi-bit spike processing
module MultiBitSpikeAccumulator (
    input [2:0] burst_in,      // 3-bit burst spike
    input [7:0] weight,
    output [15:0] partial_sum
);
    // Parallel computation for each bit
    wire [7:0] bit0 = burst_in[0] ? weight : 8'b0;
    wire [8:0] bit1 = burst_in[1] ? (weight << 1) : 9'b0;
    wire [9:0] bit2 = burst_in[2] ? (weight << 2) : 10'b0;
    
    // Sum all bit contributions
    assign partial_sum = bit0 + bit1 + bit2;
endmodule
```

### Energy Comparison

| Operation | Binary SNN | QB-LIF (3-bit) | Speedup |
|-----------|------------|----------------|---------|
| MAC / spike | 1 | 1.2 | 0.83x |
| Information / spike | 1 bit | 2.7 bits | 2.7x |
| Energy / bit | 1.0 | 0.44 | **2.25x** |

## Advantages Over Binary SNNs

1. **Higher Information Throughput**: 2-3x more information per spike
2. **Reduced Latency**: 50% fewer timesteps for equivalent accuracy
3. **Learnable Efficiency**: Automatic balance between precision and sparsity
4. **Hardware Friendly**: Simple bit-parallel processing
5. **Backward Compatible**: Can degrade to binary mode when needed

## Comparison with Prior Work

| Method | Coding | Learnable | Hardware Cost | Efficiency |
|--------|--------|-----------|---------------|------------|
| Binary SNN | 1-bit | N/A | Low | Baseline |
| Rate Coding | Multi-spike | No | High | 0.5x |
| Burst Coding | Multi-bit | No | Medium | 1.5x |
| **QB-LIF** | **Multi-bit** | **Yes** | **Medium** | **2.7x** |

## Applications

- **Edge AI**: Resource-constrained devices needing high throughput
- **Neuromorphic Vision**: Event camera processing with reduced latency
- **Audio Processing**: Time-series tasks requiring fine temporal precision
- **Deep SNNs**: Multi-layer architectures where information loss compounds

## Limitations

1. **Hardware Support**: Requires neuromorphic hardware with multi-bit accumulator support
2. **Training Stability**: Learnable scales need careful initialization
3. **Quantization Bounds**: Fixed bit-width may limit dynamic range
4. **Memory Overhead**: Storing multi-bit spike trains requires more memory

## Implementation Tips

1. **Initialization**: Start with small quantization scales (~0.1) and let them grow
2. **Bit-width Selection**: 3-4 bits typically optimal; more bits show diminishing returns
3. **Gradient Clipping**: Important for stable training with learnable scales
4. **Regularization**: Add spike count penalty to prevent saturation at max burst

## Related Skills
- adaptive-spiking-neuron-asn
- snn-quantization-beyond-accuracy
- multiplication-free-spike-time-fpga
- stdp-spiking-transformer-attention

## References

```bibtex
@article{bai2026qblif,
  title={QB-LIF: Learnable-Scale Quantized Burst Neurons for Efficient Spiking Neural Networks},
  author={Bai, Dewei and Peng, Hongxiang and Mei, Jiajun and others},
  journal={arXiv preprint arXiv:2604.25688},
  year={2026}
}
```

## Activation Keywords

- qb-lif
- quantized burst neurons
- learnable scale
- spiking neural network quantization
- multi-bit spike coding
- burst coding SNN
- neuromorphic efficiency
- SNN information throughput
