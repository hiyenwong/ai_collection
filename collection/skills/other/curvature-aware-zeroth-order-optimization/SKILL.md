---
name: curvature-aware-zeroth-order-optimization
description: "CAZO for memory-efficient test-time adaptation."
metadata:
  arxiv_id: "2608.12279"
  published: "2026-08-12"
  authors: "Junming Zhang, Shuyu Yin, Peilin Liu, Rendong Ying, Fei Wen"
  tags: [zeroth-order, test-time-adaptation, memory-efficiency, curvature]
license: Complete terms in LICENSE.txt
---

# Curvature-Aware Zeroth-Order Optimization (CAZO)

## Overview

Curvature-Aware Zeroth-Order (CAZO) optimization is a memory-efficient test-time adaptation method that addresses the high variance problem of traditional zeroth-order methods by leveraging loss landscape curvature information. CAZO uses a sliding-average estimation of the diagonal Hessian to construct anisotropic perturbation sampling, significantly improving performance while maintaining BP-free forward-only computation.

## Key Innovations

1. **Low-Rank Hessian Structure Observation**: Persistent low-rank structure in loss Hessian during adaptation
2. **Diagonal Hessian Estimation**: Sliding-average estimation of diagonal Hessian elements
3. **Anisotropic Perturbation Sampling**: Covariance matrix construction based on curvature information
4. **Memory-Efficient Architecture**: Freezes pretrained weights, optimizes minimal adapter parameters
5. **Forward-Only Computation**: Eliminates backpropagation overhead for on-device deployment

## Algorithm Details

### Core Components
- **Hessian Diagonal Estimation**: 
  - Maintain sliding window of recent gradient estimates
  - Compute diagonal Hessian approximation from gradient differences
  - Update with exponential moving average for stability
  
- **Anisotropic Sampling**:
  - Construct covariance matrix Σ = diag(h₁⁻¹, h₂⁻¹, ..., hₙ⁻¹)
  - Sample perturbations u ~ N(0, Σ) instead of isotropic N(0, I)
  - Scale learning rate by Hessian-aware factors

- **Adapter-Based Optimization**:
  - Freeze all pretrained model weights
  - Introduce minimal trainable adapter parameters
  - Optimize adapters using curvature-aware ZO gradients

### Memory and Computational Benefits
- **Memory Reduction**: Eliminates need for storing intermediate activations for backprop
- **Forward-Only**: Only requires forward passes through the network
- **On-Device Friendly**: Suitable for memory-constrained edge deployment
- **Scalable**: Performance independent of model size due to adapter focus

## Implementation Guidelines

### When to Use CAZO
- Test-time adaptation scenarios with unlabeled target data
- Memory-constrained on-device deployment
- Cross-domain generalization requirements
- Backpropagation unavailable or impractical

### Practical Implementation Steps
1. **Model Preparation**:
   - Load pretrained model
   - Insert minimal adapter modules at strategic locations
   - Freeze all original weights

2. **Hessian Estimation Setup**:
   - Initialize diagonal Hessian estimates with small positive values
   - Set sliding window size (typically 5-10 recent updates)
   - Configure exponential moving average decay rate

3. **Optimization Loop**:
   - For each test batch:
     - Sample anisotropic perturbations using current Hessian estimate
     - Compute function evaluations with perturbed adapters
     - Estimate ZO gradient using curvature-aware formula
     - Update adapter parameters
     - Update diagonal Hessian estimates
   - Apply adapted model to subsequent batches

## Performance Characteristics

### Accuracy vs Efficiency Trade-offs
- **Accuracy**: State-of-the-art TTA performance across multiple benchmarks
- **Memory**: Significantly reduced compared to BP-based methods
- **Computation**: Forward-only passes reduce computational overhead
- **Convergence**: Faster convergence due to reduced gradient variance

### Benchmark Results
- Outperforms existing ZO-TTA methods by significant margins
- Competitive with or superior to BP-based TTA methods
- Maintains performance across diverse domain shifts
- Robust to varying levels of distribution shift

## Pitfalls and Considerations

- **Hessian Estimation Stability**: Requires careful initialization and smoothing
- **Adapter Design**: Performance sensitive to adapter architecture choices
- **Hyperparameter Tuning**: Learning rates and Hessian update rates need tuning
- **Domain Shift Magnitude**: May struggle with extreme distribution shifts
- **Computational Overhead**: Additional Hessian estimation adds some overhead

## Extensions and Variants

### Potential Improvements
- **Full Hessian Approximation**: Extend beyond diagonal approximation
- **Adaptive Window Size**: Dynamically adjust Hessian estimation window
- **Multi-Scale Adapters**: Combine adapters at different network depths
- **Hybrid Approaches**: Combine with limited backpropagation when available

### Related Methods
- **Traditional ZO Methods**: Isotropic sampling without curvature awareness
- **BP-Based TTA**: Standard backpropagation-based adaptation methods
- **Other Memory-Efficient TTA**: Methods focusing on parameter efficiency

## References

- Original Paper: [Curvature-Aware Zeroth-Order Optimization](https://arxiv.org/abs/2608.12279v1)
- Code Repository: https://github.com/Hollyming/CAZO
- Related Work: Zeroth-order optimization, test-time adaptation, memory-efficient learning

## Activation Keywords

- curvature-aware zeroth-order
- CAZO
- test-time adaptation
- memory-efficient adaptation
- Hessian-aware optimization
- anisotropic perturbation
- forward-only adaptation
- on-device TTA