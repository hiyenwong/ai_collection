---
name: snn-fpga-hardware-software-codesign
description: "FPGA accelerator design for Spiking Neural Networks using Spiking Recurrent Cell (SRC) neurons, with mathematical simplifications to remove costly unary operators and avoid floating-point arithmetic. Covers piecewise approximations, LUT-register weight storage, and accuracy/energy trade-off analysis. Use when deploying SNNs on FPGA hardware, designing neuromorphic accelerators, or optimizing SNN inference energy efficiency. Trigger: SNN FPGA, spiking recurrent cell, SRC neuron, neuromorphic hardware, SNN energy efficiency, piecewise LIF approximation."
---

# SNN FPGA Hardware-Software Co-Design with Spiking Recurrent Cells

**Paper:** arXiv:2605.10679 (May 2026)
**Authors:** Pascal Harmeling, Florent De Geeter, Guillaume Drion

## Problem

Biologically faithful SNN models are too costly for FPGA. Simple models (LIF/IR) sacrifice neuronal dynamics. Need a middle ground.

## Solution: Spiking Recurrent Cell (SRC) on FPGA

### Key Simplifications

1. **Remove unary operators**: Replace `tanh`, `exp` with piecewise linear approximations
2. **Fixed-point arithmetic**: Scale weights/activations to avoid floating-point
3. **Direct LUT storage**: Weight matrices stored in LUT-registers without adaptation
4. **VHDL implementation**: Complete network in hardware description language

### Architecture

```
Off-line training → Weight matrix computation → LUT-register storage → FPGA inference
                                                                    ↓
                                                      Spiking trace processing (VHDL)
```

### Performance (Artix-7 XC7A200T @ 100MHz)

| Configuration | Accuracy | Energy/Image | Trace Length |
|--------------|----------|-------------|--------------|
| Reference (220 images, full precision) | 96.31% | ~1.74ms/digit | 220 |
| 55 images, 5-bit weights | 93.32% | 0.55 mJ | 55 |
| 44 images, 4-bit weights | 92.89% | 0.45 mJ | 44 |

### Design Principles

- **Piecewise approximation**: Replace nonlinear functions with linear segments
- **Weight quantization**: 4-5 bit weights maintain >92% accuracy
- **Trace reduction**: Shorter spiking traces reduce processing time proportionally
- **Robust weight mapping**: Pre-computed weights work directly in hardware

## Activation Keywords

- SNN FPGA implementation
- spiking recurrent cell SRC
- neuromorphic FPGA accelerator
- SNN hardware deployment
- SNN energy efficiency optimization
- piecewise neuron approximation
- 2605.10679

## Related Skills

- spikingjelly-framework
- snn-learning-survey
- snn-performance-analysis
