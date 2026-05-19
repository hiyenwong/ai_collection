---
name: spiker-ll-fpga-snn-accelerator
description: >
  Spiker-LL: FPGA-based Spiking Neural Network accelerator enabling adaptive
  on-device local learning. Extends open-source Spiker architecture with STSF
  (Spiking Time Sparse Feedback) local learning rule for supervised training
  without BPTT. Use when designing edge neuromorphic hardware, FPGA SNN
  accelerators, on-device learning systems, local learning rules, or
  hardware-algorithm co-design for spiking networks. Trigger words: Spiker-LL,
  SNN accelerator, FPGA neuromorphic, STSF learning rule, on-device training,
  local learning, Spiker architecture, DSP-free SNN, edge intelligence,
  Spiking Time Sparse Feedback.
---

# Spiker-LL: FPGA SNN Accelerator with On-Device Learning

## Core Thesis

Deploying adaptive intelligence at the edge requires hardware-algorithm co-design. Spiker-LL extends the open-source Spiker+ inference architecture with efficient STSF local learning, enabling **inference + training** on low-cost edge FPGAs with <0.1 mJ per inference.

*Source: arXiv:2605.18003 (Caviglia et al. 2026)*

## Architecture Overview

### Spiker-LL Microarchitecture

1. **Local Learning Module**: Implements STSF rule — computes weight updates using only local spike timing and pre/post activity
2. **Arbiter**: Manages access to synaptic state between inference and learning phases
3. **Control Units**: Coordinate learning/inference switching with minimal overhead

### Design Principles

- **DSP-free**: Uses multiplier-free LIF neurons — no DSP slices needed
- **Streaming**: Maintains Spiker's pipelined execution during both inference and learning
- **Minimal overhead**: Training support added only at synaptic-state access points
- **Reusable**: Existing datapaths, memory banks, and control logic shared between modes

## STSF Learning Rule

**Spiking Time Sparse Feedback** provides supervised learning via:
- Direct Feedback Alignment (DFA): fixed random top-down error signals
- Spike-triggered local plasticity: updates only when spikes occur
- No eligibility traces needed (unlike e-Prop, DECOLLE)
- Negligible state overhead compared to trace-based methods

**Tradeoff**: Limited temporal credit assignment vs. extreme hardware efficiency. Best for feedforward, low-latency spiking workloads.

## Performance Results

| Benchmark | Accuracy | Latency | Energy |
|-----------|----------|---------|--------|
| MNIST | ~93% | <1ms | <0.1 mJ |
| F-MNIST | ~92% | <1ms | <0.1 mJ |
| DIGITS | ~92% | <1ms | <0.1 mJ |

- Scales from <5k LUTs (ultra-compact) to larger networks
- Maintains real-time operation across configurations
- Competitive with prior FPGA/ASIC SNN accelerators

## Comparison to Other Local Learning Rules

| Method | State Overhead | Temporal Credit | Hardware Cost |
|--------|---------------|-----------------|---------------|
| STSF (Spiker-LL) | Minimal | Limited | Lowest |
| e-Prop | High (eligibility traces) | Strong | Higher |
| DECOLLE | Medium (local losses) | Medium | Medium |
| BPTT | O(NT) memory | Strongest | Prohibitive |

## Design Guidelines for Edge SNN Hardware

1. **Reuse existing infrastructure**: Add learning at synaptic access points, don't rebuild datapaths
2. **Prefer DSP-free designs**: Multiplier-free neurons scale better on FPGA
3. **Event-driven updates**: Only compute when spikes occur — exploit temporal sparsity
4. **Fixed random feedback**: DFA avoids backpropagation complexity
5. **Minimal state**: Avoid per-synapse eligibility traces when possible

## Application to AI Systems

- Edge deployment of adaptive SNNs on resource-constrained devices
- Hardware design for neuromorphic sensors + on-device learning
- Co-designing algorithms and hardware for streaming spiking workloads
- Open-source alternative to proprietary neuromorphic chips (Loihi, etc.)

## Limitations

- STSF limited in tasks with long-range temporal dependencies
- Tested on standard benchmarks (MNIST, F-MNIST, DIGITS) — complex real-world tasks need evaluation
- FPGA-specific; ASIC deployment would require different optimization

## Activation Keywords

- Spiker-LL, SNN FPGA accelerator, on-device learning
- STSF learning rule, local learning, Spiking Time Sparse Feedback
- DSP-free neuromorphic hardware, edge intelligence
- Spiker architecture, hardware-algorithm co-design
- multiplier-free LIF neurons, Direct Feedback Alignment
