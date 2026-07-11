---
name: mast-aigv-detection-snn
description: "MAST (Multi-channel pseudo-event SNN with Adaptive Spiking Temporal integrators) — first SNN-based detector for AI-generated videos. Converts inter-frame residuals into pseudo-events processed by spike-driven temporal branch with learnable per-channel time constants, fused with frozen X-CLIP semantic trajectory encoder. Achieves 93.14% cross-generator accuracy on GenVideo. Activation: AI-generated video detection, SNN video detection, temporal artifact detection, pseudo-event conversion, cross-generator generalization, MAST, spike-driven temporal integration, AIGV detection, boundary-localized firing, SDT-V3."
---

# MAST: Multi-channel pseudo-event SNN with Adaptive Spiking Temporal integrators for AIGV Detection

> First SNN-based detector for AI-generated video detection, leveraging the natural alignment between SNN event-driven sparse dynamics and the sparse, boundary-localized temporal artifacts in AI-generated videos.

## Metadata
- **Source**: arXiv:2605.05895
- **Authors**: Minsuk Jang, Yujin Yang, Heeseon Kim, Minseok Son, Younghun Kim, Changick Kim
- **Published**: 2026-05-07
- **Category**: cs.CV, cs.AI
- **Institution**: KAIST

## Core Problem

Modern AI-generated videos are photorealistic at the single-frame level. Detection must rely on **temporal structure** — whether motion, change, and semantic evolution remain natural over time. Prior detectors degrade sharply under **cross-generator evaluation**, where artifact type and timescale vary across generators.

## Key Insight

AI-generated videos exhibit two complementary temporal signatures:

1. **Pixel level**: Smoother frame-to-frame temporal residuals with late-accumulating residual dynamics
   - Spectral centroid f_c is 3× to 13× lower for generators than real videos
   - Gap widens in later frames due to error accumulation under conditional generation

2. **Semantic level**: More compact trajectories in feature space
   - X-CLIP trajectory convex-hull volume is 2× to 6× smaller for generators
   - Angular curvature θ significantly reduced

3. **Boundary-localized SNN firing**: When raw video is fed to SNNs, fake clips elicit firing predominantly at object and motion boundaries (unlike real clips), suggesting SNN responds to temporal artifacts localized at edges
   - Boundary Fire (BF) rate is 1.3×+ higher for fakes across all generators
   - Interior Fire (IF) stays close to real — additional firing concentrates on boundary ring

This makes **SNNs a natural choice** for AIGV detection: their event-driven, sparsely-activated dynamics align with the structure of the residual signal in a way that dense ANN backbones do not.

## MAST Architecture

### Overview

MAST combines two complementary pathways:

1. **Spike-Driven Temporal Branch (SDTB)** — processes multi-channel temporal residuals as pseudo-events with learnable per-channel time constants
2. **Frozen Semantic Encoder** — X-CLIP trajectory encoder for semantic-level temporal coherence

### 1. Pseudo-Event Front-End

Converts inter-frame residuals into spike-like events:

```
ΔHF_t = |Lap(Y_t) - Lap(Y_{t-1})|          # High-frequency Laplacian residual
ΔSobel_t = |Sobel(Y_t) - Sobel(Y_{t-1})|    # Sobel edge residual
ΔAbsDiff_t = |Y_t - Y_{t-1}|                 # Absolute difference
ΔDiff2_t = |Y_t - 2Y_{t-1} + Y_{t-2}|       # Second-order difference
```

Each channel is converted to pseudo-events via soft thresholding:

```
E_{t,c} = σ((|ΔF_{t,c}| - c_th) / β)
```

where c_th = 0.10 (contrast threshold) and β = 0.025 (temperature), matching physical event camera semantics.

**Note**: Chroma channel was tested but excluded — provided no additional signal for detection.

### 2. Spike-Driven Temporal Branch (SDTB)

Architecture:
- **PerChannelLIF** — per-channel LIF with learnable τ_c and V_{th,c}
- **SDT-V3 Gate** — Spiking Transformer with spike separable convolutions
- **MultiSpike (L=4)** — output values in {0, 1, 2, 3, 4} for richer spike communication
- **Spike Anomaly Gate** — adaptive spike integration with learnable timescales
- **Linear attention** (O(N D²)) instead of full attention (O(N² D)) for efficiency

PerChannelLIF dynamics:
```
v_t^{(c)} = (1 - 1/τ_c) * v_{t-1}^{(c)} + x_t^{(c)}
s_t^{(c)} = Spike(v_t^{(c)}, V_{th,c})
v_t^{(c)} ← v_t^{(c)} - s_t^{(c)} * V_{th,c}  # soft reset
```

Parameters:
- τ_c ∈ [0.5, 20.0] — learnable time constant per channel
- V_{th,c} ∈ [0.05, 10.0] — learnable firing threshold per channel
- Both stored in log space and recovered via exp() to keep strictly positive
- Initialized at base values (τ_0 = 2.0, V_{th,0} = 1.0)

### 3. Semantic Trajectory Encoder

- **X-CLIP-B/16** (frozen) — text-aligned video encoder
- Extracts per-frame embeddings from video encoder
- Computes trajectory curvature as auxiliary cue
- Cross-frame attention provides temporal coherence at semantic level

**Why X-CLIP?** Its cross-frame attention mechanism computes each embedding in temporal context of the entire clip, encoding short-range temporal coherence at semantic level — complementary to pixel-level residual dynamics of SDTB.

### 4. Fusion & Classification

```
final_logit = σ(W_t * z_t + W_s * z_s + b)
```

where z_t is SDTB output and z_s is semantic trajectory output.

## Training Details

| Parameter | Value |
|-----------|-------|
| Optimizer | AdamW (weight decay 0.01) |
| Epochs | 10 |
| Batch size | 16 per GPU × 4 GPUs = 64 effective |
| X-CLIP LR | 1×10⁻⁵ (frozen) |
| SDTB LR | 3×10⁻⁴ |
| Label smoothing | 0.1 |
| Gradient clipping | L2 norm 1.0 |
| Surrogate | ATan (α = 2.0) |

### Auxiliary Objectives

| Loss | Weight | Purpose |
|------|--------|---------|
| SupCon | λ = 0.3 (τ_c = 0.07) | Contrastive learning for feature separation |
| SNN-only BCE | λ = 0.2 | Keeps SDTB gradient alive |
| Anomaly BCE | λ = 0.2 (margin 0.5) | Anomaly score supervision |
| Spike-rate penalty | λ = 0.01 (r* = 0.15) | Prevents SDTB silence/deadlock |

### Critical Training Pitfall

Under "Main BCE only" (without auxiliary losses), the SDTB goes **silent** in the first epoch:
- Gate bias keeps sigmoid output below 0.15
- L=4 Multispike requires v/V_th > 0.5 to fire
- Xavier-initialized convolutions don't produce this
- Leaky integrator accumulates membrane potentials → NaN logits → training collapse
- Under DDP with find_unused_parameters=true → extra ALLREDUCE on NaN tensor → NCCL watchdog deadlock

**Solution**: The spike-rate regularizer (L_rate) forces non-zero firing rate from the first epoch, keeping SDTB gradient alive.

## Results

### GenVideo Cross-Generator (Pika-trained)

| Metric | Value |
|--------|-------|
| mACC | **93.14%** (10 unseen generators) |
| mAUC | **94.95%** |

This matches or surpasses the strongest ANN-based detectors.

### Energy Efficiency

| Component | Ops | Energy |
|-----------|-----|--------|
| SDT-V3 (SNN gate) | 1.38 SOPs | **1.24 mJ** |
| CNN-Transformer (ANN gate) | 18.61 MACs | **85.61 mJ** |
| X-CLIP backbone (frozen) | 281.2 FLOPs | 1293.61 mJ |

SNN gate adds only **+0.10%** on top of backbone; matched ANN gate adds **+6.62%**.
**69× energy savings** for the gate at parameter parity.

### GenVidBench Main Task

| Generator | Accuracy |
|-----------|----------|
| CogVideo | 97.80% |
| Mora | 91.18% |
| HD-VG | 97.53% |
| MuseV | 55.55% |
| SVD | 41.99% |

Underperforms on flow-based generators (MuseV, SVD) — pseudo-event residuals align better with diffusion-style temporal artifacts.

### SEINE Configuration

MAST achieves 77.41% mACC under SEINE training — significantly below Pika-trained (93.14%) due to:
1. SEINE is frame-interpolation generator → spike gate adapts to low spike density
2. Training/test clips sit at opposite ends of temporal-smoothness axis
3. Temporal subsampling shortcut doesn't transfer to 24 fps test generators

## Implementation Guide

### Prerequisites
- PyTorch
- Pre-trained X-CLIP-B/16 (frozen)
- GenVidBench or GenVideo dataset
- 4× NVIDIA RTX 3090 GPUs (recommended)

### Pseudo-Event Conversion

```python
def compute_pseudo_events(frames):
    """Convert video frames to pseudo-event tensor.
    
    frames: [B, T, C, H, W] normalized to [0, 1]
    returns: [B, T, C_events, H', W'] pseudo-event tensor
    """
    T = frames.shape[1]
    events = []
    
    for t in range(1, T):
        # High-frequency Laplacian residual
        lap_t = laplacian(frames[:, t])
        lap_tm1 = laplacian(frames[:, t-1])
        hf = torch.abs(lap_t - lap_tm1)
        
        # Sobel edge residual
        sobel_t = sobel(frames[:, t])
        sobel_tm1 = sobel(frames[:, t-1])
        sobel_res = torch.abs(sobel_t - sobel_tm1)
        
        # Absolute difference
        abs_diff = torch.abs(frames[:, t] - frames[:, t-1])
        
        # Second-order difference
        if t >= 2:
            diff2 = torch.abs(frames[:, t] - 2*frames[:, t-1] + frames[:, t-2])
        else:
            diff2 = abs_diff  # fallback
        
        # Stack channels
        event_t = torch.stack([hf, sobel_res, abs_diff, diff2], dim=1)
        
        # Soft threshold to pseudo-events
        c_th = 0.10
        beta = 0.025
        event_t = torch.sigmoid((event_t - c_th) / beta)
        
        events.append(event_t)
    
    return torch.stack(events, dim=1)
```

### PerChannelLIF

```python
class PerChannelLIF(nn.Module):
    def __init__(self, n_channels, tau_base=2.0, vth_base=1.0):
        super().__init__()
        # Stored in log space for positivity
        self.log_tau = nn.Parameter(torch.zeros(n_channels))
        self.log_vth = nn.Parameter(torch.zeros(n_channels))
        
        # Initialize at base values
        nn.init.constant_(self.log_tau, math.log(tau_base))
        nn.init.constant_(self.log_vth, math.log(vth_base))
    
    def forward(self, x):
        """x: [B, C, T] input tensor"""
        tau = torch.exp(self.log_tau).clamp(0.5, 20.0)
        vth = torch.exp(self.log_vth).clamp(0.05, 10.0)
        
        B, C, T = x.shape
        v = torch.zeros(B, C, device=x.device)
        spikes = []
        
        for t in range(T):
            # LIF dynamics per channel
            v = (1 - 1/tau.unsqueeze(0)) * v + x[:, :, t]
            # MultiSpike (L=4)
            s = torch.clamp(v / vth.unsqueeze(0), 0, 4.5).round()
            spikes.append(s)
            v = v - s * vth.unsqueeze(0)  # soft reset
        
        return torch.stack(spikes, dim=2)
```

### ATan Surrogate Gradient

```python
class MultiSpikeATan(torch.autograd.Function):
    @staticmethod
    def forward(ctx, v, vth, L=4, alpha=2.0):
        ctx.save_for_backward(v, torch.tensor(vth), torch.tensor(L), torch.tensor(alpha))
        return torch.clamp(v / vth, 0, L + 0.5).round()
    
    @staticmethod
    def backward(ctx, grad_output):
        v, vth, L, alpha = ctx.saved_tensors
        L = int(L)
        
        # Sum ATan kernels at each integer threshold
        grad = torch.zeros_like(grad_output)
        for k in range(L):
            threshold = k + 0.5
            grad += alpha / (2 * (1 + ((v - threshold) * alpha / 2) ** 2))
        
        # Clip: zero gradient outside saturating range
        mask = (v > 0) & (v < L)
        grad = grad_output * grad * mask.float()
        
        return grad, None, None, None
```

## Applications

- **AI-generated video detection**: Cross-generator generalization across 10+ unseen generators
- **Deepfake detection**: Temporal artifact detection in synthetic media
- **Content authentication**: Verifying video provenance and authenticity
- **Neuromorphic deployment**: Energy-efficient detection on edge devices
- **Temporal anomaly detection**: Generalizable to any domain with temporal artifacts

## Advantages Over ANN-Based Detectors

| Aspect | ANN Detectors | MAST (SNN) |
|--------|---------------|------------|
| Cross-generator mACC | ~85-92% | **93.14%** |
| Gate energy | 85.61 mJ/clip | **1.24 mJ/clip** (69× less) |
| Pipeline overhead | +6.62% | **+0.10%** |
| Temporal modeling | Dense backbone | Event-driven, sparse |
| Parameter efficiency | Requires large backbones | Lightweight SDTB (9.3M params) |

## Pitfalls

1. **Training silence/deadlock**: Without spike-rate regularization, SDTB goes silent in epoch 1, leading to NaN and NCCL deadlock. **Always include L_rate penalty.**
2. **SEINE training configuration**: Underperforms (77.41% vs 93.14%) due to temporal-smoothness distribution mismatch. **Train on generators with diverse temporal artifacts.**
3. **Flow-based generators**: Underperforms on MuseV/SVD where ReStraV is stronger. Pseudo-event residuals align better with diffusion-style artifacts.
4. **Chroma channel**: Tested but excluded — provides no additional detection signal. **Don't waste compute on color residuals.**
5. **X-CLIP choice**: Other text-aligned encoders (ViCLIP, InternVideo2) and generic video backbones (VideoMamba) underperform. X-CLIP's cross-frame attention is key.
6. **Firing rate target**: r* = 0.15 is critical — too high wastes energy, too low causes silence.
7. **Soft vs hard reset**: Soft reset is default; hard reset available as option but not used in experiments.

## Related Skills

- spiking-neural-network-analysis
- snn-learning-survey
- spiking-oscillation-mapping
- edgespike-edge-iot-snn
- snn-performance-analysis
- spike-sparsity-deployment-cost
- quantization-spiking-neural-networks-beyond-accuracy
- sd-tv3-spike-driven-transformer
