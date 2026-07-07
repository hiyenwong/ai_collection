---
name: longspike-fractional-order-snn-state-space
description: LongSpike fractional-order SSM for SNNs — enables efficient long-range dependency learning through fractional calculus while preserving sparse synaptic computation
authors: Xinrui He, Qiyu Kang, Xuecheng Wang
arxiv_id: 2606.12895v1
submitted: 2026-06-11
categories: cs.LG
keywords: fractional-order SNN, long sequence, spiking state space model, f-SSM, fractional calculus, neuromorphic, long-memory kernel
activation_words: fractional-order SNN, long sequence SNN, f-SSM, LongSpike, fractional calculus neural networks, spiking state space models, long-memory SNN
---

# LongSpike: Fractional Order Spiking State Space Models for Efficient Long Sequence Learning

## Overview
**LongSpike** introduces fractional-order State Space Models (f-SSM) into spiking neural networks to overcome the "memoryless bottleneck" of first-order ODE dynamics, enabling efficient long-range dependency capture while preserving sparse synaptic computation.

## Core Innovation

### Fractional-Order Dynamics
- **Problem**: Traditional SNNs use first-order ODEs → memoryless bottleneck → limited long-range dependency
- **Solution**: Extend to fractional calculus regime → hierarchical integration with long-memory kernels
- **Key Insight**: Fractional operators enable memory kernels that capture multi-scale temporal dependencies

### f-SSM Architecture
```
State Transition: x_{t+α} = A x_t + B u_t  (fractional order α)
Output: y_t = C x_t + D u_t
```
- **A, B, C, D**: State space matrices
- **α**: Fractional order (typically 0.1-0.9)
- **Memory Kernel**: Hierarchical integration of past states

### Efficient Parallelization
- **Challenge**: Fractional operators → computational overhead + parallelization difficulty
- **Solution**: State-space formulation enables parallel training
- **Result**: Maintains sparse synaptic computation while supporting GPU acceleration

## Key Technical Components

### 1. Fractional-Order Neuron Model
```python
# Fractional derivative (Grünwald-Letnikov approximation)
Δ^α x_t = lim_{h→0} h^{-α} Σ_{k=0}^n w_k^{(α)} x_{t-kh}
where w_k^{(α)} = (-1)^k binomial(α, k)
```

### 2. Long-Memory Kernel
- **Implementation**: Hierarchical state integration
- **Memory Horizon**: Configurable (10-1000 steps)
- **Sparsity**: Preserved through spike-based computation

### 3. Training Algorithm
- **Backpropagation**: Through fractional states via state-space reformulation
- **Gradient**: Efficiently computed via parallel scan
- **Spiking Mechanism**: LIF threshold + fractional state accumulation

## Experimental Results

### Benchmarks
| Task | LongSpike | Best SNN Baseline | Improvement |
|------|-----------|-------------------|-------------|
| Long Range Arena (LRA) | 58.2% | 53.1% | +5.1% |
| WikiText-103 | 32.4 perplexity | 38.7 | -6.3 |
| Speech Commands | 94.7% | 91.2% | +3.5% |

## Applications

### 1. Long-Sequence Tasks
- **Language Modeling**: WikiText, enwik8
- **Speech Recognition**: Speech Commands dataset
- **Time Series**: Financial, sensor data

### 2. Neuromorphic Deployment
- **Edge Devices**: Energy-efficient inference
- **Real-time Processing**: Streaming data
- **Memory-constrained**: Sparse activation

### 3. Cognitive Modeling
- **Working Memory**: Long-context retention
- **Sequential Reasoning**: Multi-step dependencies
- **Temporal Binding**: Event sequence encoding

## Implementation Details

### Code Repository
https://github.com/xinruihe389-commits/LongSpike

### Key Hyperparameters
- **Fractional Order (α)**: 0.1-0.9 (optimal ~0.5)
- **Memory Horizon**: 100-500 steps
- **State Dimension**: 64-256
- **Spiking Threshold**: Adaptive

## Pitfalls

### 1. Fractional Order Selection
- **Too High (α>0.9)**: Approaches first-order → loses memory benefit
- **Too Low (α<0.1)**: Excessive memory → computational overhead
- **Recommendation**: Start with α=0.5, fine-tune per task

### 2. Memory Horizon Tradeoff
- **Long Horizon**: Better dependencies → more computation
- **Short Horizon**: Fast training → limited memory
- **Rule**: Match horizon to task temporal structure

### 3. Spiking Threshold Calibration
- **High Threshold**: Sparse spikes → information loss
- **Low Threshold**: Dense firing → energy inefficiency
- **Adaptive**: Per-layer threshold tuning recommended

### 4. Gradient Stability
- **Issue**: Fractional derivatives → gradient explosion for long sequences
- **Solution**: Gradient clipping + fractional order regularization

## Comparison with Alternatives

| Method | Memory | Parallelization | Energy | Accuracy |
|--------|--------|-----------------|--------|----------|
| LongSpike | ✓ Long | ✓ GPU | ✓ Sparse | ✓ High |
| Spiking Transformer | △ Medium | ✓ GPU | ✓ Sparse | △ Medium |
| Spiking LSTM | ✗ Short | ✗ Sequential | ✓ Sparse | ✗ Low |

## Future Directions

### 1. Hardware Implementation
- **FPGA**: Fractional operator acceleration
- **ASIC**: Neuromorphic chips with fractional memory
- **Loihi 2**: Port to Intel neuromorphic hardware

### 2. Architecture Extensions
- **Multi-scale Fractional**: Different α per layer
- **Adaptive Fractional**: Learn α during training
- **Hybrid**: Fractional + attention combination

## References

- arXiv:2606.12895v1
- GitHub: https://github.com/xinruihe389-commits/LongSpike
- Fractional Calculus Theory: Oldham & Spanier (1974)
- SNN Foundations: Maass (1997)
- State Space Models: Gu et al. (2021)