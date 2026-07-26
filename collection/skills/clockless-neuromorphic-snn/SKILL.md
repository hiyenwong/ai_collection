---
name: clockless-neuromorphic-snn
description: >
  Clockless (asynchronous) digital Boolean spiking neural networks for neuromorphic computing.
  Based on arXiv:2605.16114 (May 2026). Use when: designing clockless/async neuromorphic
  hardware, implementing Boolean spiking neurons on FPGA, liquid state machines with
  spike-based encoding, energy-efficient neuromorphic processors, bridging digital and
  analog neuromorphic systems, Boolean spiking neural network design, autonomous digital
  circuits for neural dynamics. Activation: clockless neuromorphic, boolean spiking neuron,
  async spiking network, liquid state machine FPGA, energy-efficient SNN hardware,
  autonomous Boolean circuit, neuromorphic FPGA, clockless digital chip, B-SNN.
---

# Clockless Neuromorphic Boolean Spiking Neural Networks

arXiv:2605.16114 | Eric Oliveira Gomes & Damien Rontani | May 2026

## Core Architecture

### Boolean Spiking Neuron (B-SN)

Autonomous digital circuit emulating integrate-and-fire dynamics:

1. **Boolean Soma** — Counter accumulates presynaptic inputs (analogous to membrane
   potential). Fires when count exceeds threshold, then resets.
2. **Boolean Dendritic Module** — Combines excitatory (+) and inhibitory (−) inputs
   via configurable synaptic weights and propagation delays.
3. **Axon Output** — Spike output feeds into downstream neurons' dendritic modules.

### Clockless (Asynchronous) Operation

Key distinction from clocked digital SNNs:

- No global clock governs neuron state transitions
- Dynamics emerge from autonomous time-continuous evolution of Boolean logic gates
- Spike duration: ~2.07 ns (vs. 20 ns clock period on same FPGA)
- Massively parallel: all neurons evolve simultaneously at transistor-level timescales
- Quasi-analog behavior arises from intrinsic chip response (wire delays, gate timing)

### Network as Liquid State Machine (LSM)

- B-SNN serves as reservoir: history-dependent nonlinear transformation
- Projects low-dimensional spike sequences → high-dimensional state space
- Readout layer (trained separately) maps reservoir states to classification outputs
- Excitatory/inhibitory balance prevents saturation, maintains rich dynamics
- Propagation delays add temporal depth to reservoir dynamics

## Implementation Details

### FPGA Hardware

- **Platform**: Altera DE2-115 (Cyclone IV EP4CE115F29C7, 114,480 LEs)
- **Spike duration**: 2.07 ns (orders of magnitude faster than clocked implementations)
- **Power**: 2 orders of magnitude lower than digital FPGA SNN implementations
- **Input layer**: Synchronous spike generator (100 MHz PLL) interfaces to async reservoir
- **Output sampling**: 10 ns time steps

### Audio Classification (SHD Dataset)

- **Test accuracy**: 84.50 ± 0.67%
- **Gap to analog state-of-the-art**: small, competitive
- **Comparison**: outperforms clocked digital implementations on energy efficiency

## Key Advantages

1. **No specialized hardware** — Uses commercially available FPGAs
2. **Energy efficient** — 2 orders of magnitude improvement over digital SNN on FPGA
3. **Fast timescale** — Nanosecond spike dynamics vs. microsecond clocked systems
4. **Reconfigurable** — Same chip can implement different network topologies
5. **Bridges digital-analog gap** — Quasi-analog dynamics from purely digital logic

## Limitations

- Synaptic weights and delays fixed at synthesis time (no runtime plasticity)
- Discretization of delays and weights limits resolution
- No charge decay mechanism without inhibitory inputs
- Spike miscounting possible when inputs overlap closely
- Readout layer not yet implemented on hardware

## Design Principles for B-SNN

```
Boolean Neuron:
  Dendritic Module (inputs: excitation, inhibition)
    → Spike Counter (membrane accumulation)
      → Threshold Comparator (excitability)
        → Pulse Generator (spike output)
          → Feedback loop (refractory period)
```

### Synaptic Weight Configuration

- Excitatory synapses: increment counter by configurable amount
- Inhibitory synapses: decrement counter, prevent firing
- Balance E/I ratio to maintain critical dynamics (avoid saturation or silence)

### Propagation Delays

- Implemented via configurable delay lines in FPGA routing
- Different delay values create temporal diversity in reservoir
- Critical for temporal pattern recognition tasks

## Related Work

- Intel Loihi, IBM TrueNorth (digital SNN, clocked)
- Neurogrid, BrainScaleS-2 (mixed-signal, analog)
- Photonic neuromorphic systems (optical reservoir computing)
- Memristive crossbars (analog in-memory computing)

## Application Areas

- Edge AI inference with ultra-low power
- Real-time audio/signal processing
- Temporal pattern recognition
- Event-driven sensing systems
- Robotics control with neuromorphic efficiency
