---
name: lapis-spiking-attention
description: "Lapis: multiplication-free spiking attention."
metadata:
  arxiv_id: "2608.11865"
  published: "2026-08-12"
  authors: "Kaiwen Tang, Jiaqi Zheng, Zixuan Zhu, Yiqun Wang, Zhanglu Yan, Weng-Fai Wong"
  tags: [spiking-neural-network, attention-mechanism, energy-efficiency, neuromorphic-computing]
license: Complete terms in LICENSE.txt
---

# Lapis: Laplacian Spiking Attention

## Overview

Lapis is a novel spiking attention mechanism specifically designed for spiking neural networks (SNNs) that leverages the native properties of spike timing and membrane leakage. Unlike traditional dot-product attention mechanisms inherited from dense networks, Lapis scores token pairs using the L1 distance between query and key first-spike latency vectors under time-to-first-spike coding, then maps this distance to an affinity through a Laplacian kernel.

The key innovation is that the Laplacian kernel's exponential decay naturally matches the impulse response of a leaky integrate-and-fire (LIF) membrane, making the computation biologically plausible and hardware-efficient.

## Key Features

### Computational Efficiency
- **Multiplication-free**: Only requires subtraction, absolute value, and accumulation operations
- **Removes all multiplication** between query and key channels
- **Row normalization reduces to bit shift** under power-of-two rounding
- **14.5x reduction** in arithmetic energy compared to dense dot-product attention

### Performance Metrics
- **CIFAR-10**: 96.56% top-1 accuracy (within 0.53 points of dot-product scoring)
- **ImageNet-1K**: 83.25% top-1 accuracy for 6-bit model
- **Energy efficiency**: 3.28mJ per image on ImageNet-1K

### Biological Plausibility
- Leverages **first-spike timing** as the native variable of spiking networks
- **Membrane leakage** naturally implements the Laplacian kernel decay
- **Time-to-first-spike coding** aligns with neural coding principles

## Implementation Guidelines

### Architecture Integration
1. **Replace standard dot-product attention** in spiking vision transformers with Lapis mechanism
2. **Use time-to-first-spike coding** for input representation
3. **Implement L1 distance calculation** between query and key latency vectors
4. **Apply Laplacian kernel** with exponential decay matching LIF membrane dynamics
5. **Use power-of-two rounding** for efficient row normalization via bit shifts

### Hardware Considerations
- **Quantization**: The 6-bit implementation achieves optimal accuracy-energy tradeoff
- **Memory access patterns**: Optimize for sequential memory access in latency vector processing
- **Accumulator design**: Design accumulators to handle the membrane trace accumulation efficiently

### Training Protocol
- **Match backbone architecture** to baseline spiking transformer
- **Use identical training schedule** as dot-product attention baseline for fair comparison
- **Power-of-two quantization** should be applied during training for hardware deployment

## Use Cases

### When to Use Lapis
- **Energy-constrained edge AI** applications requiring ultra-low power consumption
- **Neuromorphic hardware** implementations where biological plausibility is desired
- **Spiking vision transformers** where computational efficiency is critical
- **Real-time inference** scenarios requiring minimal arithmetic operations

### When Not to Use Lapis
- **Non-spiking architectures** (use standard attention mechanisms)
- **Applications requiring maximum accuracy** without energy constraints (dot-product may perform slightly better)
- **Complex attention variants** requiring advanced features not supported by Lapis

## Pitfalls and Solutions

### Common Issues
1. **Timing precision**: Ensure sufficient temporal resolution for first-spike latency vectors
   - **Solution**: Use appropriate time binning and ensure consistent spike timing across layers

2. **Quantization effects**: Aggressive quantization may degrade performance
   - **Solution**: Follow the validated 6-bit quantization scheme from the paper

3. **Training stability**: May require adjustment of learning rates compared to dot-product attention
   - **Solution**: Start with same hyperparameters as baseline and fine-tune if needed

### Validation Checklist
- [ ] Verify L1 distance calculation correctness
- [ ] Confirm Laplacian kernel matches membrane dynamics
- [ ] Test power-of-two rounding for normalization
- [ ] Benchmark against dot-product baseline on target dataset
- [ ] Measure actual energy consumption on target hardware

## References

- **Original Paper**: [Lapis: Laplacian Spiking Attention via First-Spike Timing and Membrane Leakage](https://arxiv.org/abs/2608.11865)
- **Code Repository**: Check author GitHub repositories for official implementation
- **Related Work**: 
  - Spiking Transformer architectures
  - Time-to-first-spike coding schemes
  - Leaky integrate-and-fire neuron models
  - Energy-efficient neuromorphic computing

## Activation Keywords

- `lapis`
- `spiking attention`
- `first-spike timing`
- `membrane leakage`
- `energy-efficient SNN`
- `Laplacian kernel attention`
- `multiplication-free attention`