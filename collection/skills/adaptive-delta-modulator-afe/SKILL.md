---
name: adaptive-delta-modulator-afe
description: "Skill for understanding and applying a 32-channel event-based bio-signal analog front-end with adaptive delta and pulse frequency encoding for neuromorphic systems."
activation: adaptive-delta-modulator-afe, afe snn interface
category: neuroscience
---

# Adaptive Delta Modulator Analog Front-End for Spiking Neural Networks

## Overview
This skill encapsulates the knowledge from arXiv:2607.12901v1 "A 32-channel event-based bio-signal analog front-end with adaptive delta and pulse frequency encoding". The paper presents an ASIC that features 32 independently programmable input channels with dual-mode encoding (Pulse Frequency Modulation and adaptive Asynchronous Delta Modulator) optimized for biomedical signal acquisition and brain-computer interfaces.

## Core Concepts

### Dual-Mode Encoding
- **Pulse Frequency Modulation (PFM)**: Implemented via Adaptive Exponential Integrate-and-Fire (AdExp-IF) neuron.
- **Adaptive Asynchronous Delta Modulator (aADM)**: Dynamically adjusts the delta-modulation threshold based on the input signal envelope, enabling automatic data compression and noise rejection.

### Adaptive Threshold Mechanism
The aADM circuit includes an adaptive delta threshold generation block that:
1. Extracts signal envelope via subthreshold Source Follower.
2. Uses Differential Pair Integrator (DPI) circuits as current-mode low-pass filters.
3. Employs a Winner-Take-All (WTA) circuit to detect rapid changes and adapt thresholds.
4. The threshold follows the signal envelope, allowing trade-off between reconstruction accuracy and compression ratio.

### System Integration
- Fabricated in 180nm CMOS process.
- Outputs Address-Event Representation (AER) events compatible with state-of-the-art Spiking Neural Network (SNN) neuromorphic processors.
- Configurable via Serial Peripheral Interface (SPI) for bias currents, filter parameters, and aADM controls.

## Application Workflow
1. **Signal Conditioning**: Biomedical signals pass through Low-Noise Amplifier (LNA), Band-Pass Filter (BPF), and Programmable Gain Amplifier (PGA).
2. **Dual-Mode Encoding**: Conditioned signals are encoded via PFM and aADM in parallel.
3. **Event Arbitration**: Asynchronous events from both encoders are merged via an arbiter tree.
4. **AER Communication**: Events are transmitted off-chip using the Address-Event Representation protocol for SNN processing.

## Key Parameters
- **Channels**: 32 independently programmable
- **Process**: 180nm CMOS
- **Interface**: SPI configuration, AER output
- **Encoding Modes**: PFM (fixed threshold), aADM (adaptive threshold)
- **Compatibility**: Designed for integration with SNN neuromorphic processors

## Usage Notes
- The adaptive threshold allows the system to maintain low power consumption while adapting to varying signal conditions.
- This AFE enables scalable multi-channel bio-signal processing for long-term BCI applications.
- The design addresses the trade-off between signal fidelity and data rate in wireless neural interfaces.

## References
- Shyam, N., Ghosh, S., & Indiveri, G. (2026). A 32-channel event-based bio-signal analog front-end with adaptive delta and pulse frequency encoding. arXiv:2607.12901v1 [cs.AR].

## Activation Keywords
adaptive delta modulator, afe, snn interface, neuromorphic analog front end, bci, spiking neural network, pulse frequency modulation