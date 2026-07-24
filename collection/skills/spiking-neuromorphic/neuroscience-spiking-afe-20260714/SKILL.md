---
name: neuroscience-spiking-afe-20260714
category: neuroscience
description: Skill summarizing the 32-channel event-based bio-signal analog front-end with adaptive delta and pulse frequency encoding for neuromorphic signal processing.
---

# A 32-channel event-based bio-signal analog front-end with adaptive delta and pulse frequency encoding

## Overview
This skill summarizes the arXiv paper: *"A 32-channel event-based bio-signal analog front-end with adaptive delta and pulse frequency encoding"* (arXiv:2607.12901v1, submitted 2026-07-14). The work presents an Application-Specific Integrated Circuit (ASIC) designed for biomedical signal acquisition and encoding, featuring 32 independently programmable input channels with dual-mode encoding: Pulse Frequency Modulation (PFM) and adaptive Asynchronous Delta Modulator (aADM). The aADM provides an auto-scaling mechanism that adapts the encoding data-rate based on the input signal envelope in real-time, enabling high data compression for low-power information transmission. The chip is fabricated in a 180 nm CMOS process and is compatible with state-of-the-art Spiking Neural Network (SNN) neuromorphic processors.

## Methodology
The AFE architecture consists of:
- **32 independent channels**: Each channel contains a programmable gain amplifier (PGA), a dual-mode encoder (PFM/aADM), and output drivers.
- **Adaptive Asynchronous Delta Modulator (aADM)**: Dynamically adjusts the delta step size based on the instantaneous amplitude of the input signal, achieving efficient encoding by allocating more bits to high-amplitude segments and fewer bits to low-amplitude segments.
- **Pulse Frequency Modulation (PFM)**: Encodes signal amplitude into the frequency of output pulses, providing a simple, robust alternative.
- **Configurable biasing and calibration**: Each channel can be individually programmed via a serial interface to optimize gain, bandwidth, and encoder thresholds for specific bio-signals (e.g., EEG, ECG, EMG).
- **Event-driven output**: Only transmits when a significant change occurs, reducing idle power consumption and enabling asynchronous communication with SNN processors.

## Key Contributions
1. Dual-mode encoding (PFM + aADM) per channel allows trade-off between precision and power.
2. Real-time adaptive data-rate reduction via aADM achieves compression ratios suitable for wireless transmission.
3. Fabrication in standard 180 nm CMOS ensures accessibility and compatibility with existing neuromorphic hardware.
4. Demonstrated compatibility with SNN processors for end-to-end brain-computer interface (BCI) applications.

## Usage
To leverage this work in your neuromorphic engineering projects:
1. **Reference the design**: Use the architecture as a reference when designing your own analog front-end for bio-signal acquisition.
2. **Simulate the aADM**: Implement the adaptive delta modulation algorithm in software or hardware to test its compression properties on your target bio-signals.
3. **Integrate with SNN**: Connect the event-driven output spikes to spiking neuron models (e.g., Leaky Integrate-and-Fire) for event-driven processing.
4. **Customize per channel**: Utilize the programmable gain and threshold settings to tailor each channel to the specific amplitude and bandwidth of signals like EEG (µV range) versus EMG (mV range).

## References
- arXiv:2607.12901v1 – [A 32-channel event-based bio-signal analog front-end with adaptive delta and pulse frequency encoding](https://arxiv.org/abs/2607.12901v1)
- Submitted to NeuroPHY 2026 workshop, at the EWSN 2026 conference.

## Notes
This skill was automatically generated from the arXiv abstract and metadata. For implementation details, refer to the full paper.