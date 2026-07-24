---
name: a-32ch-event-based-bio-signal-frontend-neuromorphic
description: Skill for understanding and applying the 32-channel event-based bio-signal acquisition front-end for adaptive neuromorphic processing (arXiv:2607.12901v1). This skill outlines the dual-mode encoding (PFM and aADM) approach for low-power neural signal acquisition and its compatibility with spiking neural network processors.
tags: [neuroscience, brain-network, neural-dynamics, spiking-neural-network, computational-neuroscience, hardware, bio-signal-acquisition]
related_skills: []
---

# 32-Channel Event-Based Bio-Signal Acquisition Front-End for Adaptive Neuromorphic Processing

## Overview
This skill is based on the arXiv paper: "32-channel event-based bio-signal acquisition front-end for adaptive neuromorphic processing" (arXiv:2607.12901v1) by Narayanan Shyam, Saptarshi Ghosh, and Giacomo Indiveri.

The paper presents a 32-channel application-specific integrated circuit (ASIC) designed for acquiring bio-signals (e.g., neural signals) and encoding them in an event-based format suitable for neuromorphic processing. The key innovation is the dual-mode encoding per channel:
1. **Pulse Frequency Modulation (PFM)**: Converts signal amplitude to pulse frequency.
2. **Adaptive Asynchronous Delta Modulator (aADM)**: An auto-scaling delta modulator that adjusts the encoding data-rate based on the input signal envelope, enabling high data compression for low-power transmission.

The system is fabricated in a 180 nm CMOS process and provides a configurable interface for integration with state-of-the-art Spiking Neural Network (SNN) neuromorphic processors.

## Core Concepts

### Event-Based Sensing
Event-based sensors only transmit information when a change occurs, reducing data redundancy and power consumption compared to traditional sampled systems.

### Dual-Mode Encoding
- **PFM**: Simple, linear frequency encoding suitable for moderate signal dynamics.
- **aADM**: Adaptive delta modulation that tracks the signal envelope, providing high compression for slowly varying signals and higher fidelity for rapid changes.

### Adaptive Data Rate
The aADM dynamically adjusts its sampling rate based on the signal's amplitude variations, optimizing the trade-off between fidelity and bandwidth.

### Neuromorphic Compatibility
The output format (asynchronous spike-like events) is directly compatible with Spiking Neural Network (SNN) processors, enabling end-to-end low-power neural signal processing pipelines.

## Application Scenarios
- **Brain-Computer Interfaces (BCIs)**: Wireless acquisition and processing of neural signals for assistive technology.
- **Implantable Medical Devices**: Long-term monitoring of neural or other bio-signals with minimal power consumption.
- **Wireless Sensor Networks**: Event-based transmission reduces bandwidth requirements in distributed sensing systems.

## Implementation Steps
1. **Understand the Dual-Mode Architecture**:
   - Study the PFM and aADM circuit designs (refer to the paper's schematic diagrams).
   - Note the configurability of each channel via bias currents and reference voltages.

2. **Simulate the System**:
   - Use transistor-level simulators (e.g., Spectre, HSPICE) to verify the PFM and aADM responses to various input signals (sine waves, spikes, noise).
   - Validate the adaptive behavior of the aADM under varying signal envelopes.

3. **Integrate with SNN Processor**:
   - Map the event output (pulses or spikes) to the input spikes of an SNN.
   - Ensure voltage levels and timing compatibility between the ASIC and the neuromorphic chip (e.g., Loihi, SpiNNaker, or custom ASNN).

4. **Power Optimization**:
   - Tune the bias currents to minimize static power while maintaining sufficient signal-to-noise ratio.
   - Leverage the event-driven nature to achieve ultra-low average power consumption.

5. **System Validation**:
   - Test with real bio-signals (e.g., EEG, EMG, or neural spikes) to evaluate fidelity and compression ratios.
   - Compare performance against traditional ADC-based acquisition systems.

## Key Parameters
- **Number of Channels**: 32
- **Encoding Modes**: PFM and aADM (selectable per channel)
- **Process**: 180 nm CMOS
- **Interface**: Configurable bias currents for power/performance trade-off
- **Output**: Asynchronous event streams (voltage pulses)

## References
- Shyam, N., Ghosh, S., & Indiveri, G. (2026). 32-channel event-based bio-signal acquisition front-end for adaptive neuromorphic processing. arXiv preprint arXiv:2607.12901.
- Indiveri, G., et al. (2011). Neuromorphic silicon neuron circuits. Frontiers in Neuroscience, 5, 73.
- Essaifi, A., et al. (2020). Asynchronous delta modulation for neural signal compression. IEEE Transactions on Biomedical Circuits and Systems.

## Activation
Trigger this skill when working on:
- Designing low-power bio-signal acquisition systems
- Developing brain-computer interfaces
- Exploring event-based sensing for neuromorphic computing
- Integrating analog front-ends with spiking neural networks

## Notes
- The chip is specifically designed for compatibility with SNN processors, making it a valuable component for neuromorphic engineering pipelines.
- The dual-mode approach allows flexibility: PFM for deterministic latency requirements, aADM for maximum compression.