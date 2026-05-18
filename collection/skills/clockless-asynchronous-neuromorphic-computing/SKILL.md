---
name: clockless-asynchronous-neuromorphic-computing
description: "Scalable neuromorphic computing via autonomous spiking dynamics in clockless (asynchronous) digital circuits implemented on FPGAs. Boolean spiking neurons with configurable excitatory/inhibitory weights, spike-encoded data processing pipeline. Bridges gap to analog neuromorphic systems without specialized hardware. Based on Oliveira Gomes & Rontani (arXiv: 2605.16114). Use when designing energy-efficient neuromorphic systems on FPGAs, exploring clockless asynchronous digital circuits for neural computation, or implementing spike-based machine learning pipelines without analog hardware. Activation: clockless neuromorphic, asynchronous digital circuits, FPGA spiking, Boolean spiking neurons, reconfigurable neuromorphic chip, energy-efficient neuromorphic computing."
---

# Clockless Asynchronous Neuromorphic Computing

> Scalable neuromorphic architecture based on autonomous time-continuous evolution of clockless (asynchronous) digital circuits on FPGAs, implementing Boolean spiking neurons with configurable synaptic weights for energy-efficient quasi-analog neuromorphic processing.

## Metadata
- **Source**: arXiv:2605.16114
- **Authors**: Eric Oliveira Gomes, Damien Rontani
- **Published**: 2026-05-15

## Core Methodology

### Key Innovation
Demonstrates that **clockless (asynchronous) digital circuits** can serve as a viable neuromorphic computing platform, achieving energy efficiency comparable to analog neuromorphic systems without requiring specialized hardware design. The approach bridges the gap between traditional digital implementations and dedicated analog neuromorphic chips.

### Technical Framework

1. **Clockless Digital Architecture**: Spiking dynamics emerge from autonomous time-continuous evolution of asynchronous digital circuits — no global clock synchronization needed
2. **Boolean Spiking Neurons**: Networks of interacting Boolean neurons with configurable excitatory and inhibitory synaptic weights
3. **FPGA Implementation**: Runs on commercially available FPGAs — no custom ASIC required
4. **Spike-Encoded Data Pipeline**: Complete processing pipeline for efficient handling of spike-encoded data in machine learning tasks
5. **Energy Efficiency**: Significantly lower power consumption than traditional digital implementations; approaches analog neuromorphic efficiency

## Implementation Guide

### Prerequisites
- Commercially available FPGA hardware
- Hardware Description Language (HDL) knowledge for asynchronous circuit design
- Spike-based encoding for input data

### Design Principles
1. Replace clocked sequential logic with **asynchronous event-driven transitions**
2. Implement Boolean neuron dynamics with configurable excitatory/inhibitory connections
3. Use spike-timing as the computational substrate (not just spike rate)
4. Design complete pipeline: encoding → spiking network → readout

### Key Advantages
- **No specialized hardware**: Runs on off-the-shelf FPGAs
- **Scalable**: Easily expand network size on reconfigurable fabric
- **Energy-efficient**: Lower power than traditional digital; approaches analog efficiency
- **Reconfigurable**: Same chip can be reprogrammed for different tasks

## Applications
- Energy-efficient neural network inference on edge devices
- Real-time spike-based audio/sensory classification
- Neuromorphic prototyping without custom analog chip design
- Bridging digital-analog neuromorphic gap for research

## Pitfalls
- Requires expertise in asynchronous circuit design (different from standard synchronous FPGA workflows)
- Boolean neuron model is simplified compared to detailed biophysical models (e.g., Hodgkin-Huxley)
- Performance benchmarked on audio classification; generalization to other ML tasks needs validation
- Timing analysis for asynchronous circuits is more complex than clocked designs

## Related Skills
- neuromorphic-oscillator-reservoir-computing
- neuromorphic-spiking-ring-attractor-v2
- ember-autonomous-cognitive-behaviour-learned-spiking
- spiking-neural-network-analysis
