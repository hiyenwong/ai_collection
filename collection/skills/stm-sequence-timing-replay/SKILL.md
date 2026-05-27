---
name: stm-sequence-timing-replay
description: "Spiking Temporal Memory (sTM) model for learning sequence timing and controlling replay speed. Uses element-specific neuronal populations to encode timing, and oscillatory background inputs as clock signals for replay speed modulation. Apply when: sequence processing, temporal coding, spiking neural networks, replay dynamics, sequence timing, motor control, language processing. Keywords: spiking temporal memory, sequence timing, replay speed, oscillatory clock, sTM model, sequence processing, temporal coding."
---

# Learning Sequence Timing and Control of Replay Speed

Spiking Temporal Memory (sTM) model extending sequence processing to learn both element order AND timing, with flexible replay speed control.

## Overview

The sTM model addresses a fundamental challenge in sequence processing: representing not only the order of events, but also their precise timing. Key innovations:

1. **Element-Specific Timing Encoding**: Sequential activation of neuronal populations encodes duration
2. **Oscillatory Clock Signals**: Background oscillations control replay speed
3. **Spatiotemporal Patterns**: Unique sparse patterns encode elapsed time

## Core Methodology

### Sequence Element Representation
- Each sequence element = small set of neurons firing synchronously
- Active neurons encode element identity in sequential context
- Provides biologically plausible basis for complex temporal patterns

### Timing Mechanism
- **Duration Encoding**: Sequential activation of element-specific populations
- **Wide Timescale Coverage**: Enables encoding across multiple timescales
- **Biological Plausibility**: Matches neural activity patterns

### Replay Speed Control
- **Oscillatory Background**: Global oscillations serve as clock signals
- **Speed Modulation**: Correlated to EEG/LFP oscillation characteristics
- **Wakefulness vs Sleep**: Different oscillation properties determine replay speed

## Key Insights

1. **Elapsed Time Encoding**: Unique sparse spatiotemporal patterns of neural activity
2. **Flexible Control**: Speed adjustable via oscillatory input characteristics
3. **Biological Correlation**: Replay speed linked to observed EEG/LFP patterns

## Applications

- Motor sequence learning and control
- Language temporal structure processing
- Sensory perception timing
- Memory replay during sleep/wake
- Temporal pattern generation

## Implementation Considerations

### Network Architecture
- Small synchronous firing neuron sets per element
- Sequential population activation for timing
- Oscillatory input integration

### Training
- Sequence order learning (original sTM)
- Duration encoding via sequential population activation
- Oscillation parameter tuning for speed control

## Biological Validity

- Matches EEG/LFP oscillation observations
- Sparse spatiotemporal activity patterns
- Sequence replay speed correlations (wake vs sleep)
- Motor control timing relevance

## Reference

**Paper**: "Learning sequence timing and control of replay speed in networks of spiking neurons"
**arXiv ID**: 2605.22523
**Authors**: Melissa Lober, Younes Bouhadjar, Markus Diesmann, Tom Tetzlaff
**Published**: 2026-05-21
**Category**: q-bio.NC (Neurons and Cognition)

## Activation Keywords

`spiking temporal memory`, `sequence timing`, `replay speed`, `oscillatory clock`, `sTM model`, `sequence processing`, `temporal coding`, `motor sequence`, `language timing`, `replay dynamics`, `sequence duration`, `temporal patterns`
