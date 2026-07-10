---
name: nm-pruning-spiking-neural-networks
description: "Probability-based N:M semi-structured pruning for Spiking Neural Networks from scratch. Uses basis-logit parameterization and eligibility-inspired distillation (EID) for hardware-amenable sparsity patterns. Activation: N:M pruning SNN, SpikeNM, semi-structured spiking pruning, probability pruning SNN."
---

# SpikeNM: Probability-Based N:M Pruning for Spiking Neural Networks

> First SNN-oriented semi-structured N:M pruning framework that learns sparse SNNs from scratch with linearized per-block complexity and eligibility-inspired distillation for stable high-sparsity training.

## Metadata
- **Source**: arXiv:2511.12097
- **Authors**: Shuhan Ye, Yi Yu, Qixin Zhang, Chenqi Kong, Qiangqiang Wu, Xudong Jiang, Dacheng Tao
- **Published**: 2025-11-15
- **Category**: cs.CV

## Core Methodology

### Key Innovation
Introduces semi-structured N:M pruning for SNNs — enforcing at most N non-zeros per M-weight block — with linearized complexity via basis-logit parameterization and neuroscience-inspired eligibility distillation.

### Technical Framework

1. **N:M Semi-Structured Sparsity**
   - Constraint: At most N non-zero weights per block of M consecutive weights
   - Hardware-amenable: Enables sparse tensor core acceleration (e.g., NVIDIA 2:4 sparsity)
   - Combines benefits of unstructured (high sparsity) and structured (hardware efficiency) pruning

2. **Basis-Logit Parameterization**
   - Problem: Combinatorial space grows as Σ(k=1 to N) C(M,k) — exponential in M
   - Solution: M-way basis-logit parameterization linearizes per-block complexity to O(M)
   - Each weight block parameterized as logits over M basis patterns
   - Differentiable top-k sampler enables gradient-based optimization

3. **Eligibility-Inspired Distillation (EID)**
   - Converts temporally accumulated eligibility credits into block-wise soft targets
   - Aligns mask probabilities with spiking dynamics
   - Reduces sampling variance during mask search
   - Stabilizes training under high sparsity regimes

4. **Training Pipeline**
   - Initialize with dense SNN weights
   - Jointly optimize weights and sparsity masks via basis-logit + top-k sampling
   - Apply EID to guide mask probability updates using temporal spike credits
   - Progressive sparsity schedule from low to target sparsity

### Code Example
```python
# Pseudocode for SpikeNM N:M pruning
import torch

class SpikeNMBlock(nn.Module):
    """N:M prunable weight block with basis-logit parameterization."""
    
    def __init__(self, in_features, out_features, N=2, M=4):
        super().__init__()
        self.N, self.M = N, M
        self.weight = nn.Parameter(torch.randn(out_features, in_features))
        # Basis-logit: M logits per weight block
        num_blocks = in_features * out_features // M
        self.mask_logits = nn.Parameter(torch.randn(num_blocks, M))
        self.temperature = nn.Parameter(torch.tensor(1.0))
    
    def sample_mask(self):
        """Differentiable top-k sampling over basis logits."""
        # Gumbel-softmax relaxation for differentiable sampling
        hard_mask = gumbel_topk(self.mask_logits, self.N, self.temperature)
        # Reshape to weight shape
        return hard_mask.view(self.weight.shape)
    
    def forward(self, x, timesteps):
        mask = self.sample_mask()
        masked_weight = self.weight * mask
        # SNN forward pass with masked weights
        return spiking_forward(x, masked_weight, timesteps)

def eligibility_distillation(student_mask_logits, teacher_spikes, alpha=0.5):
    """EID: Align mask probabilities with spiking temporal credits."""
    # Accumulate eligibility traces from teacher spikes
    eligibility = accumulate_spike_credits(teacher_spikes)
    # Convert to soft targets for mask probability alignment
    soft_target = normalize(eligibility)
    loss = kl_divergence(softmax(student_mask_logits), soft_target)
    return alpha * loss
```

## Applications
- **SNN edge deployment**: Hardware-amenable sparsity patterns for neuromorphic chips
- **Model compression**: Reduce SNN parameters while maintaining accuracy
- **Combined sparsity**: Complement intrinsic spike sparsity with weight sparsity
- **Neuromorphic accelerator design**: Provide structured sparsity for efficient hardware

## Pitfalls
- **Block size tradeoff**: Larger M increases hardware efficiency but may reduce accuracy
- **Sampling variance**: High sparsity can cause unstable gradient estimates — EID helps mitigate
- **Temperature tuning**: Gumbel-softmax temperature schedule needs careful tuning
- **Not all SNNs benefit**: Very small networks may lose too much capacity

## Related Skills
- quantization-spiking-neural-networks-beyond-accuracy
- snn-performance-analysis
- spike-sparsity-deployment-cost