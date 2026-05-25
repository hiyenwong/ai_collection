---
name: learning-sequence-timing-snn
description: "Learning sequence timing and control of replay speed in networks of spiking neurons — extending the spiking Temporal Memory (sTM) model to encode element-specific timing via sequential neuronal population activation, with oscillatory background inputs serving as a clock for flexibly controlling replay speed."
tags: [spiking-neural-network, sequence-learning, replay, temporal-memory, computational-neuroscience, snn]
---

# Learning Sequence Timing and Control of Replay Speed in Networks of Spiking Neurons

**arXiv:2605.22523** | Submitted: 21 May 2026

**Authors:** Melissa Lober, Younes Bouhadjar, Markus Diesmann, Tom Tetzlaff

## Summary

Processing sequential inputs is a fundamental brain function, underlying tasks such as sensory perception, language, and motor control. A challenge in sequence processing is to represent not only the order of events, but also their **precise timing**. While existing computational models can learn sequential structure, many lack biologically plausible mechanisms to encode element-specific timing and to flexibly control the speed of sequence replay.

The **spiking Temporal Memory (sTM) model**, a biologically inspired network model, provides a framework for key aspects of sequence processing. In the sTM model, each sequence element is represented by a small set of neurons firing synchronously, where the set of active neurons encodes the element's identity in its sequential context. In its original version, however, the sTM model learns the order but not the timing of sequence elements.

## Key Contributions

1. **Timing Encoding via Sequential Population Activation**: The duration of sequence elements is represented by a sequential activation of element-specific neuronal populations, enabling the model to encode sequences across a wide range of timescales.

2. **Oscillatory Clock for Replay Speed Control**: Oscillatory background inputs serve as a clock signal and provide a robust and flexible mechanism for controlling the speed of sequence replay.

3. **Sparse Spatiotemporal Encoding**: Elapsed time is encoded by unique and sparse spatiotemporal patterns of neural activity.

4. **Biologically Plausible Replay Modulation**: The speed of sequence replay during wakefulness and sleep is correlated to the characteristics of global oscillatory activity observed in EEG or LFP recordings.

## Methodological Framework

- **sTM Model**: Each sequence element → small set of synchronously firing neurons
  - Identity encoded by which neurons are active
  - Context encoded by the activation pattern
- **Timing Extension**: Element duration → sequential activation within population-specific groups
  - Timescale encoding via population dynamics
  - Supports learning and replaying complex temporal patterns
- **Replay Speed Control**: Oscillatory background injection
  - Frequency of oscillation → replay speed
  - Links to EEG/LFP rhythms (theta, sharp-wave ripples)

## Relation to Experimental Neuroscience

- Provides a circuit-level mechanism for how elapsed time is represented in neural activity
- Explains the correlation between oscillatory brain rhythms and the speed of memory replay during different brain states (wakefulness vs. sleep)
- Offers testable predictions for how replay speed is modulated by global brain state

## Potential Applications

- Neuromorphic sequence learning and timing
- Spike-based temporal pattern generation
- Understanding hippocampal replay and memory consolidation
- Flexible speed control in neural sequence generators

## Activation Keywords

- spiking-temporal-memory, sTM, sequence-timing, replay-speed, oscillatory-clock, spatiotemporal-encoding, spike-timing

## References

- arXiv:2605.22523 [q-bio.NC]
- Original sTM model papers (cited within)
