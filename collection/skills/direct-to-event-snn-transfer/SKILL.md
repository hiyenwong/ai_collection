---
name: direct-to-event-snn-transfer
description: "Direct-to-Event (D2E) Spiking Neural Network Transfer methodology. Converts direct-coded SNNs trained with floating-point inputs into energy-efficient event-based representations using Self-Knowledge Distillation (SKD). Activation: SNN transfer, direct-to-event, D2E, event-based SNN, neuromorphic deployment, TTFS, self-knowledge distillation, SNN energy efficiency."
---

# Direct-to-Event Spiking Neural Network Transfer

**arXiv:** 2605.07207 [cs.NE] | IEEE Signal Processing Letters (2026)  
**Authors:** Nhan Trong Luu, Duong Trung Luu, Pham Ngoc Nam, Truong Cong Thang

## Problem Statement

Spiking Neural Networks (SNNs) trained with **direct coding** (floating-point inputs) achieve high accuracy but are substantially less energy-efficient than **event-based** counterparts (e.g., TTFS — time-to-first-spike) upon deployment on neuromorphic hardware. The **D2E transfer** problem: given a high-accuracy direct-coded SNN, convert it to an event-based representation while preserving performance.

## Core Methodology

### Self-Knowledge Distillation (SKD)

The key insight: use the **pretrained direct-coded SNN as its own teacher** to guide event-based finetuning. This bridges the distributional gap between input domains while preserving learned representations.

#### Theoretical Foundation — KL Divergence Bound (Theorem 1)

The cross-domain accuracy gap is bounded by:

$$|acc_X(f_X) - acc_S(f_S)| \leq \sqrt{\frac{1}{2}\mathbb{E}_{x \sim X}[D_{KL}(f_X(\cdot|x) \| f_S(\cdot|x))]} + 2 \cdot TV(X, S)$$

- Minimizing forward KL divergence between teacher (direct) and student (event) output distributions tightens the accuracy gap
- Pearson correlation r=0.925 between KL and accuracy gap during training empirically validates the bound
- The bound is always a strict upper envelope and decreases monotonically with training

#### SKD Training Objective

$$\min_w R(f_S, h_X) = \mathbb{E}_{x \sim X}\left[\alpha \cdot \mathcal{L}_{CE}(\mathbb{E}_T[f_S(e(x))], h_X(x)) + (1-\alpha) \cdot D_{KL}(f_X(y|x) \| f_S(y|x))\right]$$

- **α = 0.4**: balance between cross-entropy loss and KL distillation
- Teacher $f_X$: direct-coded SNN (frozen pretrained weights)
- Student $f_S$: same architecture, initialized from teacher, receives event-coded input $e(x)$
- **Key**: teacher and student share architecture and label space; only input coding differs

### Why Naive Transfer Fails — Three Effects

1. **Information Loss** (Theorem 2): TTFS encoding with T=8 caps mutual information at $d \log_2(T+1)$ bits vs. continuous representation — ~60% of input entropy is unrecoverable
2. **Spike Magnitude Collapse** (Proposition 1): LIF pre-activation mean shrinks by factor of T at each timestep; deeper architectures suffer exponentially more
3. **Gradient Mismatch** (Theorem 3): At the direct-code optimum, gradient under event input is non-zero proportional to $TV(X, S)$

### Comparison with Alternatives

| Method | Approach | Performance |
|--------|----------|-------------|
| TSF (Task-Specific Finetuning) | Direct finetuning with event input | Significant drop, no theoretical guarantee |
| SKD (Self-Knowledge Distillation) | KL-regularized self-distillation | Best across all architectures |
| Reverse KL distillation | Mode-seeking KL variant | +0.87pp accuracy but +19% KL divergence |
| MSE/ℓ₁ on softmax | Alternative distillation losses | Slightly below forward KL |

## Implementation Guide

### Setup

```python
import torch
from spikingjelly.clock_driven import neuron, functional, layer
import torch.nn as nn

# Hyperparameters
alpha = 0.4          # SKD loss balancing
T = 8                # Timesteps
batch_size = 256
lr = 0.1 * (batch_size / 256)
epochs = 200         # Single-shot finetuning
```

### Training Pipeline

```python
def skd_loss(student_logits, teacher_logits, labels, alpha=0.4):
    """Self-Knowledge Distillation loss for D2E transfer."""
    # Cross-entropy with true labels
    ce_loss = F.cross_entropy(student_logits, labels)
    
    # KL divergence with teacher's soft targets
    kl_loss = F.kl_div(
        F.log_softmax(student_logits / temperature, dim=-1),
        F.softmax(teacher_logits / temperature, dim=-1),
        reduction='batchmean'
    ) * (temperature ** 2)
    
    return alpha * ce_loss + (1 - alpha) * kl_loss

def train_skd(model, teacher_model, dataloader, optimizer, alpha=0.4):
    """Single epoch of SKD training."""
    model.train()
    teacher_model.eval()
    
    for direct_inputs, event_inputs, labels in dataloader:
        # Teacher: direct-coded forward pass (no grad)
        with torch.no_grad():
            teacher_logits = teacher_model(direct_inputs)
        
        # Student: event-coded forward pass
        student_logits = model(event_inputs)
        
        loss = skd_loss(student_logits, teacher_logits, labels, alpha)
        
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
```

### Optimization Settings

| Parameter | Value |
|-----------|-------|
| Optimizer | SGD with Nesterov momentum (0.9) |
| LR schedule | Cosine Annealing with warmup (lr/10 → lr) |
| Neuron type | LIF with hard-reset |
| Surrogate gradient | Arctangent |
| Timesteps | 8 |
| Seeds | Fixed for reproducibility |

### Encoding Function e(x)

For **TTFS (Time-to-First-Spike)** encoding:

```python
def ttfs_encode(x, T=8):
    """Convert continuous input to TTFS spike events."""
    # x: [B, C, H, W] in [0, 1]
    # Return: [B, T, C, H, W] binary spikes
    # Fire at timestep t if pixel intensity crosses threshold
    thresholds = torch.linspace(1.0, 1.0/T, T)
    spikes = torch.zeros(x.shape[0], T, *x.shape[1:], device=x.device)
    
    for t in range(T):
        mask = (x > thresholds[t]) & (spikes.sum(dim=1) == 0)
        spikes[:, t][mask] = 1
    
    return spikes
```

## Performance Benchmarks

### CIFAR-10 (Spiking-WRN20)
| Method | Accuracy | Gain over Baseline |
|--------|----------|--------------------|
| Direct-coded | 90.11% | — |
| TTFS baseline | 28.69% | — |
| TSF | 50.66% | +22.0pp |
| **SKD (Ours)** | **74.18%** | **+45.5pp** |

### CIFAR-100 (Spiking-WRN20)
| Method | Accuracy | Gain over Baseline |
|--------|----------|--------------------|
| Direct-coded | 62.52% | — |
| TTFS baseline | 6.60% | — |
| TSF | 17.23% | +10.6pp |
| **SKD (Ours)** | **43.83%** | **+37.2pp** |

### ImageNet (Spiking-WRN16)
| Method | Accuracy | Gain over Baseline |
|--------|----------|--------------------|
| Direct-coded | 62.65% | — |
| TTFS baseline | 6.21% | — |
| TSF | 10.69% | +4.5pp |
| **SKD (Ours)** | **35.04%** | **+28.8pp** |

**Pattern**: SKD consistently outperforms TSF across all 9 architectures on CIFAR-10, 8/9 on CIFAR-100, and 3/3 on ImageNet.

## Pitfalls

### Critical Pitfalls

1. **Information-theoretic ceiling**: Even optimal D2E transfer cannot recover ~60% of input entropy lost in TTFS encoding. Expect a non-trivial gap vs. direct-coded teacher (e.g., 90%→74%).
2. **Deep architecture sensitivity**: Deeper networks (Spiking-VGG16, SEW-RN50) suffer exponential spike rate collapse across layers. Consider increasing T or using richer encodings.
3. **Temperature scaling**: The KL distillation benefits from temperature scaling. Without it, forward KL may not effectively transfer "dark knowledge" in probability distribution tails.
4. **DVS vs TTFS**: When converting to simulated DVS sensors (not just TTFS), the encoding gap is even larger. SKD still works but absolute accuracy is lower.
5. **Single-shot vs multi-shot**: The benchmarks use single-shot finetuning. Multi-shot (50+ epochs) shows tighter convergence but may overfit.

## Applications

- **Neuromorphic deployment**: Convert existing direct-coded SNN research models for Loihi, Speck, TrueNorth hardware
- **Edge inference**: Deploy high-accuracy SNNs on energy-constrained devices with TTFS/Event-based coding
- **SNN research reuse**: Reuse pretrained SNN databases trained with direct coding for event-based applications
- **ANN-SNN pipeline complement**: Unlike ANN-to-SNN conversion, D2E addresses intra-SNN encoding shift when upstream training already committed to direct coding

## Related Approaches

- **Information Bottleneck (IB) methods**: SNIB, HOSIB, SIBoLS — complementary intra-domain regularizers that could be combined with SKD
- **ANN-to-SNN conversion**: Different problem (ANN→SNN vs. direct-SNN→event-SNN); calibration techniques don't directly apply to TTFS
- **Knowledge distillation variants**: Reverse KL offers +0.87pp but loses theoretical bound guarantee; symmetric KL may be future improvement direction

## Key References

- Luu et al. (2026). Direct-to-Event Spiking Neural Network Transfer. IEEE Signal Processing Letters.
- Kim et al. (2022). Rate coding or direct coding: which one is better? ICASSP.
- Fang et al. (2021). Deep residual learning in SNNs. NeurIPS.
- Hinton et al. (2015). Distilling the knowledge in a neural network.
