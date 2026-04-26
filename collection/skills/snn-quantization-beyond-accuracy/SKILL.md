---
name: snn-quantization-beyond-accuracy
description: "Quantization of Spiking Neural Networks beyond accuracy metrics. Earth Mover's Distance framework for evaluating firing distribution preservation during quantization. Activation: snn quantization, firing distribution, EMD, behavior preservation, earth mover's distance, deployment metrics."
---

# SNN Quantization Beyond Accuracy

> Comprehensive evaluation framework for SNN quantization using Earth Mover's Distance to assess firing distribution preservation, addressing the gap between accuracy metrics and deployment-relevant behavior.

## Metadata
- **Source**: arXiv:2604.14487v1
- **Authors**: Evan Gibson Smith, Jacob Whitehill, Fatemeh Ganji
- **Published**: 2026-04-15
- **Institution**: Worcester Polytechnic Institute

## Core Methodology

### Key Innovation
Demonstration that quantization methods can produce substantially different firing distributions at equivalent accuracy, and introduction of Earth Mover's Distance (EMD) as a diagnostic metric for firing distribution divergence, enabling behavior-aware quantization evaluation.

### Problem Statement
Standard SNN quantization evaluation focuses exclusively on accuracy, overlooking:
- Effective sparsity (governed by firing activity)
- State storage requirements
- Event-processing load
- Hardware deployment characteristics

### Technical Framework

#### Quantization Dimensions Evaluated
| Dimension | Description |
|-----------|-------------|
| Weight Quantization | Reduces memory bandwidth |
| Membrane Quantization | Reduces state storage |
| Clipping Range | Affects dynamic range |
| Bit-width | Precision vs. efficiency trade-off |

#### Proposed Metric: Earth Mover's Distance (EMD)
- **Purpose**: Measure firing distribution divergence
- **Advantage**: Captures distributional differences invisible to accuracy
- **Application**: Compare quantized vs. full-precision firing behavior

#### Key Findings
1. **Uniform Quantization**: Induces distributional drift even at preserved accuracy
2. **Learned Quantization (LQ-Net style)**: Maintains firing behavior close to baseline
3. **Accuracy-Behavior Gap**: Accuracy alone insufficient for quantization evaluation

## Implementation Guide

### Evaluation Workflow
```python
# SNN Quantization Evaluation Framework

1. Train Full-Precision SNN
   ↓
2. Apply Quantization (weight/membrane)
   - Uniform quantization
   - Learned quantization (LQ-Net)
   - Various bit-widths
   ↓
3. Measure Both Metrics:
   a. Accuracy (standard)
   b. EMD (firing distribution)
   ↓
4. Compare Quantization Methods
   - High accuracy + low EMD = ideal
   - High accuracy + high EMD = caution
```

### EMD Calculation
```python
# Earth Mover's Distance for Firing Distributions
from scipy.stats import wasserstein_distance

emd_score = wasserstein_distance(
    fp_firing_distribution,  # Full-precision
    quant_firing_distribution  # Quantized
)
```

### Tested Architectures
- SEW-ResNet variants
- CIFAR-10 and CIFAR-100 datasets

## Applications
- **Hardware-Aware Quantization**: Optimize for target deployment platform
- **Energy Estimation**: Accurate power consumption prediction
- **Deployment Validation**: Ensure behavior consistency
- **Quantization Method Selection**: Choose methods preserving behavior

## Pitfalls
- **EMD Interpretation**: Requires baseline comparison
- **Dataset Dependency**: Results may vary across datasets
- **Architecture Sensitivity**: Different networks respond differently
- **Computational Cost**: EMD adds evaluation overhead

## Recommendations
1. Always evaluate both accuracy and EMD
2. Prefer learned quantization for behavior-critical applications
3. Consider target hardware characteristics in quantization choice
4. Validate on deployment-relevant metrics

## Related Skills
- `integer-state-dynamics`: Quantized SNN dynamics
- `snn-quantized-dynamics-integer`: Integer-state SNN implementation
- `quantized-snn-hardware-optimization`: Hardware-aware quantization
- `sharpness-aware-surrogate-training`: Related training methodology

## References
- Smith, E.G. et al. "Quantization of Spiking Neural Networks Beyond Accuracy." arXiv:2604.14487 (2026).
