---
name: intrinsically-stable-snn-bn-free
description: "Intrinsically Stable SNN (IS-SNN) architecture for deep spiking neural networks without batch normalization. Removes activation-normalization layers via topology-aware weight standardization and offline reparameterization, restoring accumulation-only inference datapath. Achieves 68.05% ImageNet accuracy with 96.4% FPGA LUT reduction. Use when designing hardware-friendly deep SNNs, eliminating runtime normalization overhead, or analyzing firing-rate stability. Activation: IS-SNN, normalization-free SNN, batch normalization free, weight standardization, firing-rate decay, neuromorphic hardware, offline reparameterization"
license: Complete terms in LICENSE.txt
metadata:
  arxiv_id: "2606.31695"
  paper_title: "Intrinsically Stable Spiking Neural Networks: Overcoming the Performance Barrier in the Absence of Batch Normalization"
  authors: "Ruichen Ma, Xiaoyang Zhang, Jian Bai, Guanchao Qiao, Liwei Meng, Ning Ning, Yang Liu, Shaogang Hu"
  published: "2026-06-30"
  venue: "ECCV 2026 Accepted"
  github: "https://github.com/Ruichen0424/IS-SNN"
  tags: [spiking neural networks, batch normalization, weight standardization, neuromorphic hardware, firing-rate stability, offline reparameterization, synaptic scaling, homeostatic plasticity]
---

# Intrinsically Stable SNN (IS-SNN): Normalization-Free Deep Spiking Networks

## Problem: BN Paradox in SNNs

State-of-the-art deep SNNs rely on **non-fusible dynamic BN variants** (tdBN, BNTT, TEBN, TAB) that compute normalization statistics dynamically at runtime. These introduce **runtime multiplications** that defeat the core hardware-efficiency motivation of SNNs (accumulation-only datapath).

Without BN, deep SNNs suffer **catastrophic firing-rate decay**: the ratio `c = μ_{L+1}/μ_L` between adjacent minimum repetition units (MRUs) deviates from 1, causing firing rates to vanish (`c < 1`) or saturate (`c > 1`) exponentially with depth.

## Core Solution: IS-SNN Architecture

IS-SNN enforces **signal homeostasis** (inspired by biological synaptic scaling) through two mechanisms:

### 1. Topology-Aware Weight Standardization (WS-Conv)

Each convolutional layer standardizes its weights during training:

```
Ŵ_{i,j} = γ_ℓ · (W_{i,j} - μ_i) / √(N·σ_i² + ε)
```

- `N` = fan-in
- `γ_ℓ` = layer-specific scaling factor = `1/σ_ℓ` (topology-aware)
- `σ_ℓ` = theoretically estimated input std for layer ℓ
- Targets pre-activation scale `x_pa ~ N(0, 1)`

**Pre-activation statistics** (key derivation):
```
μ_pa = N · μ_in · μ_Wi
σ²_pa = N · σ²_in · (σ²_Wi + μ²_Wi)
```

To achieve `x_pa ~ N(0,1)`: enforce `μ_Wi = 0` and `σ²_Wi = 1/(N·σ²_in)`.

### 2. Topology-Dependent Variance Propagation

The scaling factor `γ_ℓ` depends on network topology:

| Architecture | Input variance per layer | γ_ℓ |
|---|---|---|
| **Plain (VGG)** | `σ²_{in,ℓ+1} = σ²_{out,ℓ} = σ²_g` (constant) | `1/σ_g` |
| **Residual (ResNet)** | Compounds through additions → grows | `1/√(1 + α²·(blocks-1))` with residual scaling α |
| **First encoding layer** | Direct from input data | `γ_1 = 1` |

### 3. Modified Residual Connection

```
x_{ℓ+1} = α · SN(f(x_ℓ)) + x_ℓ
```

where `α = 0.5` (power of 2 → bit-shift implementable, no multiplication). Controls variance growth rate across residual blocks.

### 4. Empirical Estimation of σ²_g (Neuron Output Variance)

Unlike ReLU (transparent linear input-output variance), spiking neurons are highly non-linear and timestep-dependent. **σ²_g is measured empirically** by stimulating neurons with `N(0,1)` inputs:

| Neuron Model | Decay | Input Decay | σ²_g (T=4) | σ²_g (T=8) | σ²_g (T=16) |
|---|---|---|---|---|---|
| LIF (τ=2) | × | | 0.1234 | 0.1195 | 0.1174 |
| LIF (τ=2) | √ | | 0.0290 | 0.0298 | 0.0302 |

## Offline Reparameterization (Key Innovation)

During **training**: WS operates on live weights (statistics update each step).

During **inference**: WS is folded into static weights offline:
```
W_fused = γ_ℓ · W / √(N·σ²_W + ε)    [pre-computed]
```

Result: **zero runtime normalization overhead** — pure accumulation + thresholding datapath.

## Performance Results

### Accuracy (competitive with/superior to dynamic BN)

| Dataset | Model | Method | Timesteps | Accuracy |
|---|---|---|---|---|
| CIFAR-10 | ResNet-19 | TEBN (SOTA BN) | 6 | 94.51% |
| CIFAR-10 | ResNet-19 | **IS-SNN** | 6 | **94.51%** |
| CIFAR-100 | ResNet-19 | TEBN (SOTA BN) | 6 | 76.41% |
| CIFAR-100 | ResNet-19 | **IS-SNN** | 6 | **76.47%** |
| CIFAR-100 | ResNet-152 | w/o BN | 4 | 17.10% (FAIL) |
| CIFAR-100 | ResNet-152 | **IS-SNN** | 4 | **76.98%** |
| ImageNet | ResNet-34 | w/o BN | 4 | 32.58% |
| ImageNet | ResNet-34 | TET | 4 | 68.00% |
| ImageNet | ResNet-34 | **IS-SNN** (400ep) | 4 | **68.05%** |

### Hardware Efficiency

| Metric | Dynamic BN Neuron | IS-SNN Neuron | Improvement |
|---|---|---|---|
| FPGA LUTs (32-bit) | ~512 (multiplier O(N²)) | ~32 (adder O(N)) | **96.4% reduction** |
| Training throughput | 401 img/s/GPU | 461 img/s/GPU | **+15%** |
| Training memory | baseline | -17% | **17% reduction** |

## Implementation Workflow

### Step 1: Estimate σ²_g for Your Neuron Model

```python
import torch

def estimate_sigma_g2(neuron_fn, T=4, num_samples=100000, fan_in=128):
    """Empirically estimate output variance of spiking neuron under N(0,1) input."""
    x = torch.randn(num_samples, fan_in)
    spikes = []
    mem = torch.zeros(num_samples)
    for t in range(T):
        mem = neuron_fn(mem, x)  # your neuron dynamics
        s = (mem >= 1.0).float()
        mem = mem * (1 - s)  # reset
        spikes.append(s)
    output = torch.stack(spikes).mean(dim=0)  # time-averaged firing rate per sample
    return output.var().item()
```

### Step 2: Apply IS-SNN to Plain Networks (VGG)

```python
import torch.nn as nn

class WSConv2d(nn.Conv2d):
    """Weight Standardized Convolution with topology-aware scaling."""
    def __init__(self, in_channels, out_channels, kernel_size, gamma_l, **kwargs):
        super().__init__(in_channels, out_channels, kernel_size, **kwargs)
        self.gamma_l = gamma_l  # = 1/sigma_g for plain networks

    def forward(self, x):
        weight = self.weight
        # Compute weight statistics across fan-in dimensions
        fan_in = weight[0].numel()
        mu = weight.mean(dim=[1,2,3], keepdim=True)
        var = weight.var(dim=[1,2,3], unbiased=False, keepdim=True)
        weight_hat = self.gamma_l * (weight - mu) / torch.sqrt(fan_in * var + 1e-4)
        return nn.functional.conv2d(x, weight_hat, self.bias, self.stride, self.padding, self.dilation, self.groups)
```

### Step 3: Apply IS-SNN to Residual Networks

```python
class ISResBlock(nn.Module):
    def __init__(self, in_ch, out_ch, sigma_g, alpha=0.5):
        super().__init__()
        gamma = 1.0 / sigma_g  # constant for all blocks in residual networks
        self.conv1 = WSConv2d(in_ch, out_ch, 3, gamma, padding=1)
        self.conv2 = WSConv2d(out_ch, out_ch, 3, gamma, padding=1)
        self.sn = LIFNeuron()  # spiking neuron
        self.alpha = alpha  # residual scaling (0.5 = bit-shift)

    def forward(self, x):
        out = self.sn(self.conv2(self.sn(self.conv1(x))))
        return self.alpha * out + x  # modified residual connection
```

### Step 4: Offline Reparameterization for Deployment

```python
def fold_ws_for_inference(ws_conv):
    """Fold weight standardization into static weights for hardware deployment."""
    with torch.no_grad():
        weight = ws_conv.weight
        fan_in = weight[0].numel()
        mu = weight.mean(dim=[1,2,3], keepdim=True)
        var = weight.var(dim=[1,2,3], unbiased=False, keepdim=True)
        gamma = ws_conv.gamma_l
        # Fused weight: W_fused = gamma * (W - mu) / sqrt(N*var + eps)
        fused_weight = gamma * (weight - mu) / torch.sqrt(fan_in * var + 1e-4)
        ws_conv.weight.data = fused_weight
        ws_conv.fused = True
    return ws_conv
```

## Key Design Decisions

1. **α = 0.5 for residual scaling**: Power of 2 → bit-shift (no multiplier). Broad solution plateau (α=0.5 vs α=1.0 gap < 0.2%). Unified across architectures without per-network sweeps.

2. **Strided convolution > max-pooling**: Max-pooling with binary spikes has non-monotonic variance relationship (peaks at μ_in=0.5). Use strided convolutions for downsampling.

3. **First layer γ₁ = 1**: Encoding layer handles non-spike input; simplification for generalizability.

4. **Hard reset with detached gradient**: Improves optimization stability during surrogate gradient training.

## Training Configuration

| Dataset | Optimizer | LR | Weight Decay | Batch Size | Epochs |
|---|---|---|---|---|---|
| CIFAR-10/100 | SGD (mom=0.9) | 0.02 | 5e-4 | 128 | 256 |
| ImageNet | SGD (mom=0.9) | 0.1 | 2e-5 | 256 | 128/400 |
| DVS-Gesture | SGD (mom=0.9) | 0.01 | 5e-4 | 16 | 196 |
| Spikformer | AdamW | standard | standard | standard | standard |

- Firing threshold: V_th = 1.0, V_reset = 0.0
- Surrogate gradient: arctan-based, `g(x) = (1/π)arctan(παx/2) + 0.5`
- Cosine annealing LR schedule
- Framework: SpikingJelly

## Pitfalls and Limitations

1. **Fixed weights assumption**: Offline reparameterization assumes weights are fixed after training. Not suitable for online learning without additional hardware for statistics tracking.

2. **Max-pooling complexity**: Non-monotonic variance relationship with binary spikes. Prefer strided convolutions.

3. **Neuron-specific σ²_g**: Must re-estimate for non-standard neuron models (PLIF, adapting neurons, etc.).

4. **Transition blocks**: Additional transition blocks in ResNets can exacerbate firing-rate decay if variance propagation is not properly tracked.

5. **Full-system energy**: Reported FPGA savings focus on arithmetic datapath only. Memory access, routing, and system-level scheduling add overhead not captured.

## When to Use

- **Deploying deep SNNs on neuromorphic hardware** (Loihi, SpiNNaker, TrueNorth) where runtime multiplications are costly
- **Edge deployment** with power/latency constraints (autonomous robotics, wearable sensors)
- **Scaling SNN depth** beyond what BN-free architectures previously achieved (ResNet-152, deep Transformers)
- **Designing biologically plausible architectures** where synaptic scaling / homeostatic regulation is desired

## Related Concepts

- **Synaptic scaling**: Biological homeostatic process adjusting synaptic strengths to stabilize neuronal activity — the neuroscience inspiration for IS-SNN
- **Weight Standardization (WS)** in ANNs (Brock et al., 2021) — IS-SNN derives topology-aware scaling specific to SNN dynamics
- **SEW ResNet** (Fang et al., 2021) — residual structure adopted for IS-SNN residual architectures
- **tdBN/BNTT/TEBN/TAB** — the non-fusible dynamic BN variants IS-SNN replaces

## References

1. Ma, R., Zhang, X., Bai, J., Qiao, G., Meng, L., Ning, N., Liu, Y., & Hu, S. (2026). Intrinsically Stable Spiking Neural Networks: Overcoming the Performance Barrier in the Absence of Batch Normalization. *ECCV 2026*. arXiv:2606.31695.
2. Code: https://github.com/Ruichen0424/IS-SNN
3. Brock, A., De, S., & Smith, S.L. (2021). Characterizing signal propagation to close the performance gap in unnormalized ResNets. *ICLR*.
4. Fang, W., et al. (2021). Deep residual learning in spiking neural networks. *NeurIPS*.
