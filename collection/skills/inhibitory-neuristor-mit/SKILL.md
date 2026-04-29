---
name: inhibitory-neuristor-mit
version: 1.0.0
description: "Inhibitory neuristor circuit based on metal-to-insulator transition (MIT) in VO2. Implements both excitatory and inhibitory neuronal behaviors in a single compact device using volatile resistance switching. Advances neuromorphic hardware by mimicking biological excitation-inhibition balance. arXiv:2604.19951."
date: 2026-04-23
arxiv_id: "2604.19951"
authors: "Victor Palin, Akash Agnihotri, Nareg Ghazikhanian, Matthew Frame et al."
categories: "cond-mat.mtrl-sci, cond-mat.str-el"
activation:
  - neuristor
  - VO2
  - metal-insulator transition
  - inhibitory neuron
  - neuromorphic hardware
  - spiking oscillator
  - excitation-inhibition balance
  - memristive neuron
---

# Inhibitory Neuristor Based on Metal-to-Insulator Transition

## Overview
Demonstrates an **inhibitory neuristor circuit** leveraging the insulator-to-metal transition (IMT) in VO₂ (vanadium dioxide). Unlike prior excitatory-only neuristors, this device implements **both excitatory and inhibitory neuronal behaviors** in a single compact circuit, advancing neuromorphic hardware toward biological realism.

## Key Methodology

### Metal-Insulator Transition (MIT) in VO₂
- VO₂ exhibits volatile high-to-low resistance switching at ~68°C
- IMT produces abrupt current increase → neuronal excitation analog
- Reverse transition (metal→insulator) provides recovery phase
- Drives self-oscillating spiking behavior under DC bias

### Inhibitory Neuristor Design
1. **Excitatory mode**: Standard IMT-based spiking — input voltage triggers resistance drop, current spike
2. **Inhibitory mode**: Circuit configuration where input *suppresses* ongoing oscillation
3. **Mode switching**: Controlled by bias conditions and circuit topology
4. **Single device**: No separate excitatory/inhibitory elements needed

### Circuit Architecture
- VO₂ device in series with load resistor
- Parallel capacitive element for membrane potential analog
- Bias voltage controls operating regime (excitatory vs. inhibitory)
- Input modulation mimics synaptic current injection

### Biological Analogy
- Excitation: depolarization → action potential firing
- Inhibition: hyperpolarization → suppression of firing
- Excitation-inhibition balance critical for neural computation
- Single device replicates both functions like biological neurons

## Implementation Guidance
- Fabricate VO₂ thin film on sapphire or Si substrate
- Pattern electrodes for electrical contact
- Characterize IMT transition temperature and hysteresis
- Design circuit with appropriate load resistance for desired regime
- Measure spiking frequency, threshold, and inhibition response

## Key Parameters
- **Transition temperature**: ~68°C (intrinsic to VO₂)
- **Hysteresis width**: affects spiking dynamics
- **Load resistance**: determines excitatory vs. inhibitory regime
- **Bias voltage**: controls oscillation frequency

## Advantages
- True hardware-level excitation-inhibition in single device
- Compact footprint compared to CMOS neuron circuits
- Low energy per spike (nanojoule range)
- Volatile switching — no power needed to maintain state
- Directly compatible with crossbar array architectures

## Pitfalls
- Temperature sensitivity requires thermal management
- Device-to-device variability in transition parameters
- Limited programmability compared to digital neurons
- Hysteresis may cause timing-dependent behavior
- Scaling to large arrays requires uniform VO₂ film quality

## References
- arXiv: [2604.19951](https://arxiv.org/abs/2604.19951)
- Key terms: neuristor, VO₂, metal-insulator transition, inhibitory neuron, neuromorphic hardware, spiking circuit, excitation-inhibition balance
