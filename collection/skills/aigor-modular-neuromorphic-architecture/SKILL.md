---
name: aigor-modular-neuromorphic-architecture
description: "AIGOR - modular, event-driven neuromorphic architecture for configurable SNN inference. Organizes neurons into timestep-synchronized processing cores with packet-switched communication, supporting multiple neuron models (LIF, HH, AH) and configurable precision."
tags: [spiking-neural-network, neuromorphic-computing, fpga, event-driven, hardware-accelerator, snn-inference]
activation_words: [AIGOR, neuromorphic architecture, event-driven SNN, FPGA accelerator, packet-switched, timestep-synchronized, configurable SNN]
---

# AIGOR: Modular Event-Driven Neuromorphic Architecture

## Overview

AIGOR is a modular, event-driven neuromorphic architecture for spiking neural network (SNN) inference that addresses the fragmented landscape of SNN hardware by providing a configurable, IP-block-based design approach.

## Core Innovation

**Problem**: Current SNN hardware is fragmented:
- Dedicated neuromorphic processors (fixed neuron models)
- Application-specific FPGA accelerators (single workload class)
- Large-scale neuroscience simulators (not optimized for inference)

**AIGOR Solution**: Modular architecture assembled from parameterized IP blocks:
- Neuron model, numeric precision, hardware folding, and core partitioning are **configured per instance**
- Single declarative specification generates cores, neuron kernels, and synaptic-memory images
- Supports multiple neuron models (LIF, HH, Axon-Hillock) on same hardware

## Architecture

### Core Components

1. **Processing Cores**: Timestep-synchronized neuron processing units
2. **Packet-Switched Communication**: Spikes exchanged as packets between cores
3. **IP Block Library**: Parameterized compute, memory, and communication blocks
4. **Declarative Specification**: Single config file generates entire hardware design

### Key Features

- **Multi-Model Support**: LIF, Hodgkin-Huxley (HH), Axon-Hillock (AH) neurons
- **Configurable Precision**: Numeric precision set per instance
- **Multi-Core Scaling**: Neurons folded onto hardware, partitioned across cores
- **Cross-Platform**: Validated on AMD Versal VPK180 FPGA

## Validation

### Workloads Tested

1. **Feedforward Image Classifier** (snnTorch-trained)
   - Reproduces reference accuracy
   - Mapped onto configurable cores

2. **Recurrent Balanced Random Network** (NEST-modeled)
   - Matches NEST reference at spike-level precision
   - Multi-core execution across two FPGAs

### Scaling Results

- **Simulation Validation**: Multi-node synchronization validated up to 1000 cores
- **Topology**: 3D torus interconnect
- **Bottleneck Analysis**: Throughput limited by synaptic-delivery datapath and global timestep barrier

## Implementation Pattern

### Declarative Specification

```yaml
# Example AIGOR configuration
network:
  type: "feedforward_classifier"
  neuron_model: "LIF"
  precision: "fixed_16bit"
  
hardware:
  num_cores: 4
  neurons_per_core: 1024
  folding_factor: 8
  
communication:
  topology: "packet_switched"
  timestep_sync: true
```

### Generation Flow

```bash
# 1. Write declarative specification
cat > network_config.yaml << 'EOF'
...
EOF

# 2. Generate hardware design
aigor-generate --config network_config.yaml --output hw_design/

# 3. Synthesize for target FPGA
aigor-synthesize --target amd_versal_vp180 --design hw_design/

# 4. Program and run
aigor-program --bitstream hw_design.bit --input data.bin
```

## Performance Metrics

### Hardware-Oriented Metrics

- **Silicon Area**: Reported post-implementation utilization
- **Power Consumption**: Measured during inference
- **Quantization Sensitivity**: Accuracy vs. precision tradeoffs
- **Throughput**: Spikes/second per core

### Benchmark Results

- **N-MNIST**: Classification accuracy matches software baseline
- **DVS Gesture**: Real-time inference on FPGA
- **Spiking Heidelberg Digits**: Multi-core scaling validated

## Design Space Exploration

### Configuration Parameters

1. **Neuron Model**: LIF (fast) vs. HH (biologically detailed) vs. AH (intermediate)
2. **Precision**: 8-bit, 16-bit, 32-bit fixed-point
3. **Folding**: How many neurons per physical core
4. **Partitioning**: How to distribute network across cores

### Tradeoffs

- **Accuracy vs. Energy**: Lower precision → less energy but potential accuracy loss
- **Throughput vs. Area**: More cores → higher throughput but larger area
- **Flexibility vs. Efficiency**: Configurable design vs. application-specific optimization

## Limitations

- **Synaptic Delivery Bottleneck**: Current prototype limited by synaptic datapath
- **Global Timestep Barrier**: Synchronization overhead at scale
- **Configuration Overhead**: Design generation time for new configurations

## Future Work

- Datapath refinements for synaptic delivery (in development)
- Event-driven (asynchronous) execution mode
- Support for learning on-chip (plasticity rules)

## Related Work

- **Loihi** (Intel): Fixed-architecture neuromorphic chip
- **SpiNNaker**: Large-scale SNN simulator
- **BrainScaleS**: Analog neuromorphic hardware
- **snntorch**: Software SNN training framework

## Activation

AIGOR, neuromorphic architecture, event-driven SNN, FPGA accelerator, packet-switched, timestep-synchronized, configurable SNN, modular neuromorphic, hardware-aware SNN

## arXiv Reference

- ID: 2607.03191
- Title: AIGOR: A Modular, Event-Driven Neuromorphic Architecture for Configurable SNN Inference
- Authors: Pierpaolo Perticaroli, Roberto Ammendola, Andrea Biagioni
- Categories: cs.AR, cs.ET
- Published: 2026-07-03
