---
name: convolution-delay-recurrent-snn
description: Combining convolutional recurrent connections with delay learning (DelRec extension) in spiking neural networks. Achieves 99% recurrent parameter savings, 52x faster inference while retaining accuracy. Evaluated on audio classification tasks.
version: 1.1
authors:
  - Lúcio Folly Sanches Zebendo
  - et al.
paper: arXiv:2604.15997
date: 2026-04-17
tags:
  - spiking-neural-network
  - convolution
  - delay-learning
  - DelRec
  - recurrent-connections
  - audio-classification
  - parameter-efficiency
  - neuromorphic
category: ai_collection
---

# Combining Convolution and Delay Learning in Recurrent Spiking Neural Networks

## Summary

This work extends the **DelRec (Delay Learning in Recurrent Connections)** framework by introducing **convolutional recurrent connections with learnable delays**. Instead of storing full recurrent weight matrices (O(N²)), the method uses local convolutional kernels with delay channels, reducing recurrent parameters by **99%** and enabling **52x faster inference** while maintaining accuracy on audio classification tasks.

**Key Innovation**: Replacing dense recurrent connections with convolution-delay approximations — each neuron's recurrent input comes from a small convolutional kernel applied to delayed versions of the population activity.

## Key Contributions

1. **Convolution-Delay Recurrent Connections**: Replace W_rec ∈ R^{N×N} with small convolutional kernels K ∈ R^{C×K×D} where C is channels, K is kernel size, D is number of delays.

2. **Massive Parameter Reduction**: 99% fewer recurrent parameters compared to standard recurrent SNNs.

3. **52x Inference Speedup**: Convolution operations are highly optimized on GPU, and the reduced parameter count eliminates memory bottleneck.

4. **Delay Learning**: Each synaptic connection learns its optimal delay, enabling temporal processing without explicit time steps.

5. **Audio Classification Validation**: Demonstrated on speech command recognition and environmental sound classification tasks.

## Technical Approach

### Problem: Dense Recurrent Weights

Standard recurrent SNN:
$$I_{rec,i}(t) = \sum_{j=1}^{N} W_{ij} \cdot S_j(t-1)$$

For N neurons: **N² recurrent parameters**. For N=1000, that's 1M parameters just for recurrence.

### Solution: Convolution + Delay Approximation

The key insight: recurrent connections in biological neural circuits are **local** and **delay-structured**. Most neurons connect to nearby neurons with varying conduction delays.

#### Convolutional Recurrent Connection

$$I_{rec}(t) = \sum_{d=1}^{D} \text{Conv1D}(S(t-d), K_d)$$

Where:
- S(t-d): spike trains at delay d
- K_d ∈ R^{C×K}: convolutional kernel for delay channel d
- C: number of convolution channels
- K: kernel size (typically 3-7)
- D: number of delay channels

#### Parameter Comparison

| Connection Type | Parameters | For N=512 |
|----------------|------------|-----------|
| Dense recurrent W_rec | N² | 262,144 |
| Conv-delay recurrent | C × K × D | 4 × 5 × 8 = 160 |
| **Savings** | **99.94%** | **1,638x fewer** |

### Delay Learning via DelRec Extension

Each delay channel d has a learnable delay value δ_d:

$$I_{rec}(t) = \sum_{d=1}^{D} \text{Conv1D}(S(t - \delta_d), K_d)$$

The delay values δ_d are learned via backpropagation through a differentiable delay operator:

$$S(t - \delta) \approx S(t - \lfloor\delta\rfloor) \cdot (\lceil\delta\rceil - \delta) + S(t - \lceil\delta\rceil) \cdot (\delta - \lfloor\delta\rfloor)$$

### Network Architecture

```
Input → [Conv Frontend] → [Conv-Delay Recurrent SNN] → [Readout]
         Feature extraction    Temporal processing        Classification
```

#### Conv Frontend
- 2-3 convolutional layers for feature extraction
- Converts raw audio/spectrogram into spike trains
- Standard SNN convolution with LIF neurons

#### Conv-Delay Recurrent Layer
```python
class ConvDelayRecurrent(nn.Module):
    def __init__(self, channels, kernel_size=5, num_delays=8):
        super().__init__()
        self.num_delays = num_delays
        self.kernel_size = kernel_size
        self.channels = channels
        
        # Learnable convolutional kernels per delay
        self.kernels = nn.ParameterList([
            nn.Parameter(torch.randn(channels, 1, kernel_size) * 0.01)
            for _ in range(num_delays)
        ])
        
        # Learnable delays (initialized with uniform spacing)
        self.delays = nn.Parameter(
            torch.linspace(1, num_delays * 2, num_delays).float()
        )
        
        # LIF neuron state
        self.register_buffer('V', torch.zeros(1, channels))
    
    def forward(self, spikes_seq):
        """
        spikes_seq: [T, B, C] — spike trains over time
        Returns: [T, B, C] — processed spike trains
        """
        T, B, C = spikes_seq.shape
        output = []
        
        for t in range(T):
            # Accumulate recurrent input from all delay channels
            I_rec = torch.zeros(B, C, device=spikes_seq.device)
            
            for d in range(self.num_delays):
                delay = self.delays[d]
                d_low = int(torch.floor(delay))
                d_high = int(torch.ceil(delay))
                frac = delay - d_low
                
                # Get delayed spike trains with interpolation
                if t - d_high >= 0:
                    s_low = spikes_seq[t - d_low] if t - d_low >= 0 else 0
                    s_high = spikes_seq[t - d_high]
                    s_delayed = s_low * (1 - frac) + s_high * frac
                elif t - d_low >= 0:
                    s_delayed = spikes_seq[t - d_low]
                else:
                    continue
                
                # Apply convolutional kernel
                I_rec += F.conv1d(
                    s_delayed.unsqueeze(0), 
                    self.kernels[d], 
                    padding=self.kernel_size // 2
                ).squeeze(0)
            
            # LIF update
            self.V = self.V + (-self.V + I_rec) / 20.0  # τ_m = 20
            new_spikes = (self.V >= 1.0).float()
            self.V = self.V * (1 - new_spikes)
            output.append(new_spikes)
        
        return torch.stack(output)
```

## Experimental Results

### Audio Classification Benchmarks

| Dataset | Method | Accuracy | Recurrent Params | Inference Time |
|---------|--------|----------|-----------------|----------------|
| Speech Commands | Dense R-SNN | 95.2% | 262,144 | 1.0× (baseline) |
| Speech Commands | DelRec | 94.8% | 2,560 | 0.08× |
| Speech Commands | **Conv-Delay** | **95.0%** | **160** | **0.019× (52x faster)** |
| ESC-50 | Dense R-SNN | 88.4% | 262,144 | 1.0× |
| ESC-50 | DelRec | 87.9% | 2,560 | 0.09× |
| ESC-50 | **Conv-Delay** | **88.1%** | **160** | **0.021×** |

### Ablation Studies

| Kernel Size | Num Delays | Accuracy | Params |
|-------------|-----------|----------|--------|
| 3 | 4 | 94.1% | 48 |
| 5 | 4 | 94.5% | 80 |
| 3 | 8 | 94.7% | 96 |
| **5** | **8** | **95.0%** | **160** |
| 7 | 8 | 94.9% | 224 |
| 5 | 16 | 95.1% | 320 |

**Optimal**: K=5, D=8 — good balance of accuracy and efficiency.

### Energy Efficiency

| Method | MACs (inference) | Estimated Power |
|--------|-------------------|----------------|
| Dense R-SNN | 262K | 1.0 mW |
| DelRec | 2.5K | 0.01 mW |
| **Conv-Delay** | **1.6K** | **0.006 mW** |

## Comparison with Related Methods

| Method | Param Savings | Speedup | Learnable Delays? | Convolution? |
|--------|--------------|---------|-------------------|-------------|
| Dense R-SNN | 0% | 1× | ✗ | ✗ |
| Sparse R-SNN | ~80% | 5× | ✗ | ✗ |
| DelRec | ~99% | 12× | ✓ | ✗ |
| **Conv-Delay (this work)** | **~99.9%** | **52×** | **✓** | **✓** |

## Implementation Considerations

### Hardware Deployment
- **GPU**: Conv1d is highly optimized (cuDNN), enabling 52x speedup
- **Neuromorphic chips**: Convolution maps to crossbar arrays efficiently
- **Microcontrollers**: 160 parameters fit in SRAM; no external memory needed

### Training Tips
1. **Initialize delays uniformly**: δ_d = linspace(1, 2D, D)
2. **Clamp delays**: 1 ≤ δ_d ≤ max_delay during training
3. **Gradual delay learning**: Fix delays for first 50 epochs, then unfreeze
4. **Regularization**: L1 on kernel weights to encourage sparsity

### Memory Budget
```
Full recurrent SNN (N=512): 262K × 4 bytes = 1 MB
Conv-delay SNN (C=4, K=5, D=8): 160 × 4 bytes = 640 bytes
→ Fits in L1 cache of most processors
```

## Key Equations Summary

### Convolutional Recurrent Input
$$I_{rec,i}(t) = \sum_{d=1}^{D} \sum_{c=1}^{C} \sum_{k=-K/2}^{K/2} K_{d,c,k} \cdot S_{i+k}(t - \delta_d)$$

### Learnable Delay with Interpolation
$$S(t - \delta) = (1 - \alpha) \cdot S(t - \lfloor\delta\rfloor) + \alpha \cdot S(t - \lceil\delta\rceil)$$
$$\alpha = \delta - \lfloor\delta\rfloor$$

### LIF Neuron Update
$$\tau_m \frac{dV_i}{dt} = -V_i + I_{rec,i}(t) + I_{ext,i}(t)$$

## Relevance

This work enables **practical deployment of recurrent SNNs** on resource-constrained hardware by:
- Reducing memory footprint by 1000x
- Speeding up inference by 52x
- Maintaining task accuracy
- Preserving temporal processing capability through learned delays

Applications:
- **Always-on audio sensing**: Wake word detection, environmental monitoring
- **Wearable devices**: Ultra-low-power speech recognition
- **IoT edge devices**: Sound classification with sub-mW power budgets
- **Neuromorphic processors**: Efficient recurrent layer implementation

## Triggers (激活词)

convolution delay, DelRec, recurrent SNN, parameter efficient, delay learning, audio classification, spiking neural network, inference speedup, hardware deployment, convolutional recurrent, learnable delays, temporal processing, neuromorphic computing, edge AI
