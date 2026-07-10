---
name: spiker-ll-snn-accelerator
description: >
  SPIKER-LL methodology for FPGA-accelerated adaptive local learning in Spiking Neural Networks.
  Extends Spiker+ inference architecture with STSF (Spike-Timing-Specific-Feedback) local learning
  rule support on FPGA. DSP-free, sub-millisecond latency, <0.1 mJ per inference.
  Enables on-device SNN training at the edge.
  Use when: designing FPGA SNN accelerators, implementing local learning rules in hardware,
  building edge AI systems with on-device learning, optimizing SNN inference/training latency,
  comparing neuromorphic hardware architectures, or evaluating STSF/STDP learning in hardware.
  Activation: spiker-ll, FPGA SNN accelerator, adaptive local learning SNN, STSF learning rule,
  edge FPGA SNN, spiker-plus, on-device SNN training, neuromorphic FPGA, spike-timing learning hardware,
  DSP-free SNN accelerator.
---

# SPIKER-LL: FPGA-Accelerated Adaptive Local Learning in SNNs

> On-device SNN training on FPGA: extending inference-only architectures with efficient local learning, achieving DSP-free implementation with sub-millisecond latency.

## Metadata

- **Source**: arXiv:2605.18003
- **Authors**: Alessio Caviglia, Filippo Marostica, Alessandro Savino, Stefano Di Carlo
- **Published**: 2026-05-18
- **Categories**: cs.NE; cs.AI

## Core Methodology

### Key Innovation

SPIKER-LL extends the open-source **Spiker+** inference architecture with hardware support for
the **STSF local learning rule** (Spike-Timing-Specific-Feedback), enabling both inference and
online learning on a single FPGA with minimal overhead.

### Architecture

1. **Base**: Spiker+ open-source SNN inference framework
2. **Extension**: Microarchitectural additions for STSF weight updates
3. **Key property**: **DSP-free** — uses LUT/FF/BRAM only, no DSP slices
4. **Scalable**: Configurable for different SNN sizes on edge FPGAs

### Performance

| Metric | Value |
|--------|-------|
| Accuracy | Up to 93% (MNIST, F-MNIST, DIGITS) |
| Latency | Sub-millisecond |
| Energy | <0.1 mJ per inference |
| DSP Usage | 0 (DSP-free) |
| Learning | Online (STSF local rule) |

### STSF Local Learning Rule

Spike-Timing-Specific-Feedback is a local learning rule that:

- Uses only **local information** available at each synapse (pre/post spike timing)
- Compatible with **three-factor learning** (local + global modulatory signal)
- Enables **online adaptation** without backpropagation
- Hardware-efficient: weight updates computed in-place

### Hardware Design Principles

1. **Minimal overhead**: Learning logic adds negligible area over inference-only Spiker+
2. **Memory bandwidth optimization**: Weight updates co-located with inference datapath
3. **Parallel processing**: Layer-level parallelism for inference + weight updates
4. **Edge-optimized**: Targets resource-constrained FPGAs (no DSP requirement)

## Comparison with Related Work

| Approach | On-device Learning | DSP Required | Latency | Edge-Ready |
|----------|-------------------|--------------|---------|------------|
| SPIKER-LL | ✅ STSF local | ❌ No | <1ms | ✅ |
| Spiker+ | ❌ Inference only | ❌ No | <1ms | ✅ |
| GPU training | ✅ Backprop | N/A | High | ❌ |
| Loihi 2 | ✅ Local rules | Custom ASIC | Low | ❌ (ASIC) |
| BrainChip Akida | ✅ Local rules | Custom ASIC | Low | ❌ (ASIC) |

## Use Cases

1. **Edge SNN deployment** — Deploy adaptive SNNs on resource-constrained FPGAs
2. **Online adaptation** — Enable SNNs to learn/adjust in real-time without cloud connectivity
3. **Hardware-algorithm co-design** — Optimize learning rules for specific FPGA architectures
4. **Energy-constrained AI** — Ultra-low-power adaptive inference for IoT/embedded systems

## Pitfalls

- STSF is a **local** rule — may not match backprop accuracy on complex tasks
- FPGA resource limits constrain network size (LUT/BRAM bound, not compute)
- No GPU fallback in the original design — purely FPGA-targeted
- Benchmarks on MNIST/F-MNIST/DIGITS — larger datasets need validation

## Activation Keywords

- spiker-ll
- FPGA SNN accelerator
- adaptive local learning SNN
- STSF learning rule
- edge FPGA SNN
- spiker-plus
- on-device SNN training
- DSP-free SNN
