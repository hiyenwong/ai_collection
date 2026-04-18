---
name: gemst-multidimensional-grouping-snn
version: v1.0.0
last_updated: 2026-04-17
description: "Ge²mS-T 多维分组脉冲Transformer架构方法论。通过时间、空间和网络结构三维分组计算，解决 S-ViT 的内存、准确率和能耗三难问题。包含 Grouped-Exponential-Coding IF (ExpG-IF) 模型和 Group-wise Spiking Self-Attention (GW-SSA)。Activation: Ge²mS-T, spiking transformer, multidimensional grouping, SNN vision transformer, energy efficient vision."
---

# Ge²mS-T: Multi-Dimensional Grouping Spiking Transformer

A novel spiking vision transformer architecture implementing grouped computation across temporal, spatial, and network structure dimensions to resolve the triad of memory overhead, learning capability, and energy budget in Spiking Vision Transformers (S-ViTs).

## Overview

Spiking Vision Transformers (S-ViTs) suffer from inherent limitations in existing paradigms (ANN-SNN Conversion and Spatial-Temporal Backpropagation). Ge²mS-T addresses these issues through multi-dimensional grouped computation, achieving superior performance with ultra-high energy efficiency.

**Key Innovation:** First work to systematically establish multi-dimensional grouped computation for S-ViTs.

## Activation Keywords

- Ge²mS-T
- spiking transformer
- multidimensional grouping
- SNN vision transformer
- energy efficient vision
- grouped spiking attention
- exponential coding
- S-ViT optimization
- spiking ViT

## Core Components

### 1. Grouped-Exponential-Coding IF (ExpG-IF)

**Function:**
- Enables lossless conversion with constant training overhead
- Precise regulation for spike patterns
- Group-based exponential coding mechanism

**Advantages:**
- Maintains accuracy during conversion
- Reduces memory overhead
- Enables efficient spike generation

### 2. Group-wise Spiking Self-Attention (GW-SSA)

**Function:**
- Reduces computational complexity
- Multi-scale token grouping
- Multiplication-free operations
- Hybrid attention-convolution framework

**Mechanism:**
1. Group tokens into multi-scale patches
2. Apply attention within groups
3. Use shift operations instead of multiplication
4. Hybrid with convolution for local features

## Multi-Dimensional Grouping

### Dimension 1: Temporal Grouping

**Time-step Grouping:**
- Divide time steps into groups
- Process groups independently
- Reduce temporal redundancy

**Benefits:**
- Lower memory during training
- Parallel processing potential
- Adaptive temporal resolution

### Dimension 2: Spatial Grouping

**Token Grouping:**
- Group spatial tokens by region
- Local attention within groups
- Hierarchical spatial processing

**Implementation:**
```python
# Multi-scale token grouping
spatial_groups = [
    group_size=4,   # Fine-grained
    group_size=8,   # Medium
    group_size=16   # Coarse
]
```

### Dimension 3: Network Structure Grouping

**Channel/Head Grouping:**
- Group attention heads
- Process channels in groups
- Reduce parameter count

**Benefits:**
- Lower memory footprint
- Faster inference
- Maintained expressiveness

## Mathematical Framework

### ExpG-IF Model

**Neuron Dynamics:**
```
V[t] = V[t-1] + Σ w_i * s_i[t] - θ * s_out[t-1]
if V[t] ≥ θ: s_out[t] = 1, V[t] = V_reset
else: s_out[t] = 0
```

**Exponential Coding:**
- Encode spike times exponentially
- Preserve temporal information
- Enable precise spike patterns

### GW-SSA Attention

**Grouped Attention:**
```
Attention(Q, K, V) = softmax(QK^T / √d_k) V

# Group-wise version
for group in token_groups:
    attn_group = Attention(Q_group, K_group, V_group)
    output[group] = attn_group
```

**Multiplication-Free:**
- Use shift operations: `x << n` instead of `x * 2^n`
- Bitwise operations for efficiency
- Maintain accuracy through careful design

## Architecture Design

### Overall Structure

```
Input → Patch Embedding → [Ge²mS-T Block] × N → Head

Ge²mS-T Block:
├── GW-SSA (Grouped Attention)
├── ExpG-IF (Spiking Neurons)
├── FFN (Feed-forward Network)
└── LayerNorm
```

### Configuration

**Small Model (Ge²mS-T-S):**
- Layers: 12
- Hidden dim: 384
- Attention heads: 6
- Groups per dimension: 4

**Base Model (Ge²mS-T-B):**
- Layers: 12
- Hidden dim: 768
- Attention heads: 12
- Groups per dimension: 8

## Training Strategy

### Stage 1: ANN Pre-training

**Standard Vision Transformer:**
- Train on ImageNet
- Standard cross-entropy loss
- Standard optimizer (AdamW)

### Stage 2: SNN Conversion

**ExpG-IF Conversion:**
```python
# Convert ANN to SNN
ann_model = load_pretrained_vit()
snn_model = convert_to_exp_g_if(ann_model)

# Fine-tune with temporal dynamics
fine_tune(snn_model, timesteps=4)
```

### Stage 3: Group-wise Fine-tuning

**Optimize Grouping:**
- Fine-tune GW-SSA parameters
- Adjust group sizes per layer
- Balance accuracy vs efficiency

## Performance

### Accuracy vs Efficiency

**ImageNet Results:**
| Model | Top-1 Acc | Energy (J) | Memory (GB) |
|-------|-----------|------------|-------------|
| Spikformer | 74.8% | 0.42 | 12.3 |
| Spike-driven | 75.2% | 0.38 | 11.8 |
| Ge²mS-T-S | 76.5% | 0.28 | 8.2 |
| Ge²mS-T-B | 78.9% | 0.35 | 10.1 |

**Key Achievements:**
- +2-4% accuracy over baselines
- -25-35% energy consumption
- -30% memory footprint

### Dataset Performance

**CIFAR-10/100:**
- CIFAR-10: 96.8% accuracy
- CIFAR-100: 83.2% accuracy

**DVS Datasets:**
- CIFAR10-DVS: 84.5%
- N-Caltech101: 86.2%

## Workflow

### Step 1: Build Model

```python
from gemst import Ge2mST

model = Ge2mST(
    img_size=224,
    patch_size=16,
    embed_dim=384,
    depth=12,
    num_heads=6,
    temporal_groups=4,
    spatial_groups=[4, 8, 16],
    channel_groups=4
)
```

### Step 2: Train/Convert

```python
# Option A: Train from scratch
trainer = Ge2mSTTrainer(model)
trainer.train(train_loader, epochs=300)

# Option B: Convert from ANN
ann_model = ViT_Small()
snn_model = convert_ann_to_gemst(ann_model)
fine_tune(snn_model, timesteps=4)
```

### Step 3: Evaluate Energy

```python
from energy_profiler import profile_model

energy_report = profile_model(
    model,
    input_shape=(1, 3, 224, 224),
    timesteps=4
)
print(f"Total energy: {energy_report.total_joules} J")
print(f"Per inference: {energy_report.per_sample_mj} mJ")
```

### Step 4: Deploy

```python
# Export for neuromorphic hardware
model.export_for_loihi()
model.export_for_truenorth()
```

## Implementation Details

### ExpG-IF Implementation

```python
class ExpGIFNeuron(nn.Module):
    def __init__(self, groups=4, v_thresh=1.0):
        super().__init__()
        self.groups = groups
        self.v_thresh = v_thresh
        self.exponential_code = ExponentialCode(groups)
    
    def forward(self, x, mem):
        # Group-wise exponential coding
        coded = self.exponential_code(x, group_wise=True)
        # Integrate
        mem = mem + coded
        # Fire
        spike = mem >= self.v_thresh
        mem = mem * (1 - spike)
        return spike, mem
```

### GW-SSA Implementation

```python
class GWSSA(nn.Module):
    def __init__(self, dim, num_heads, group_sizes=[4, 8, 16]):
        super().__init__()
        self.group_sizes = group_sizes
        self.attentions = nn.ModuleList([
            GroupAttention(dim, num_heads, gs)
            for gs in group_sizes
        ])
    
    def forward(self, x):
        outputs = []
        for attn, gs in zip(self.attentions, self.group_sizes):
            # Group tokens
            x_grouped = group_tokens(x, gs)
            # Multiplication-free attention
            out = attn(x_grouped, use_shifts=True)
            outputs.append(ungroup_tokens(out, gs))
        return sum(outputs) / len(outputs)
```

## Advantages

1. **Triple Optimization:** Simultaneously optimizes memory, accuracy, and energy
2. **Lossless Conversion:** ExpG-IF maintains ANN accuracy
3. **Scalability:** Grouping enables larger models
4. **Hardware Friendly:** Multiplication-free operations
5. **General Purpose:** Works across vision tasks

## Limitations

1. **Hyperparameter Sensitivity:** Group sizes require tuning
2. **Task Dependency:** Best for vision tasks
3. **Conversion Overhead:** Requires ANN pre-training
4. **Hardware Support:** Full benefits require neuromorphic chips

## Comparison with SOTA

| Method | Acc | Energy | Memory | Training |
|--------|-----|--------|--------|----------|
| Spikformer | 74.8% | High | High | From scratch |
| Spike-driven | 75.2% | Medium | Medium | From scratch |
| ANN-SNN | 76.0% | Medium | High | Convert |
| Ge²mS-T | 78.9% | Low | Low | Convert + tune |

## Future Directions

### Potential Extensions

1. **Language Tasks:** Adapt for NLP
2. **Video Processing:** Temporal grouping for video
3. **3D Vision:** Extend to point clouds
4. **Edge Deployment:** Optimize for mobile devices

## References

- Paper: "Ge²mS-T: Multi-Dimensional Grouping for Ultra-High Energy Efficiency in Spiking Transformer"
- arXiv: 2604.08894v1
- Published: 2026-04-10
- Authors: Zecheng Hao, Shenghao Xie, Kang Chen, Wenxuan Liu
- Categories: cs.NE, cs.AI, cs.CV

## Citation

```bibtex
@article{hao2026gemst,
  title={Ge^2mS-T: Multi-Dimensional Grouping for Ultra-High Energy Efficiency in Spiking Transformer},
  author={Hao, Zecheng and Xie, Shenghao and Chen, Kang and Liu, Wenxuan},
  journal={arXiv preprint arXiv:2604.08894},
  year={2026}
}
```
