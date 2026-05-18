---
name: clockless-asynchronous-neuromorphic-computing
description: "Clockless asynchronous neuromorphic computing methodology using FPGA-based spiking neural networks. Core approach: implement networks of interacting Boolean spiking neurons with configurable excitatory/inhibitory synaptic weights on clockless digital circuits. Enables energy-efficient neuromorphic processing without specialized analog hardware. Use when: designing neuromorphic systems, FPGA spiking implementations, clockless/asynchronous digital circuits for ML, energy-efficient spike-based processing, bridging digital-analog neuromorphic gap."
---

# Clockless Asynchronous Neuromorphic Computing

## Core Methodology

Implement scalable neuromorphic architectures using spiking dynamics emerging from autonomous time-continuous evolution of clockless (asynchronous) digital circuits on FPGAs.

## Key Innovation

- **Clockless Digital Hardware**: Networks of Boolean spiking neurons evolve continuously without clock synchronization
- **Configurable Synaptic Weights**: Excitatory and inhibitory connections configurable per synapse
- **Complete Spike Pipeline**: Encoding → Processing → Decoding for ML tasks
- **Energy Efficiency**: Significantly lower power than traditional digital implementations
- **No Specialized Hardware**: Runs on commercial FPGAs, bridges gap to analog neuromorphic systems

## Architecture Components

### 1. Boolean Spiking Neurons

```
Each neuron: Boolean state with configurable threshold dynamics
- No clock: autonomous time-continuous evolution
- Interconnected via excitatory (+) and inhibitory (-) synapses
- Spike events trigger state transitions in connected neurons
```

### 2. Processing Pipeline

```
Input → Spike Encoding → Clockless SNN Processing → Spike Decoding → Output
```

- **Spike Encoding**: Convert input data (e.g., audio) to spike trains
- **Clockless SNN**: Boolean spiking network performs computation
- **Spike Decoding**: Convert output spikes to predictions/classifications

### 3. FPGA Implementation

- Implemented on commercial FPGAs (no custom silicon needed)
- Reconfigurable architecture allows rapid prototyping
- Power-efficient: approaches analog neuromorphic performance

## Application Domains

- Audio classification with spike-based encoding
- Real-time sensory processing
- Edge AI with power constraints
- Any task requiring low-latency, energy-efficient inference

## Activation Keywords

- clockless neuromorphic, asynchronous spiking, FPGA neuromorphic, Boolean spiking neurons, energy-efficient SNN, clockless digital circuits for ML

## Reference

- arXiv:2605.16114 - "Scalable neuromorphic computing from autonomous spiking dynamics in a clockless reconfigurable chip"
- Authors: Eric Oliveira Gomes, Damien Rontani
