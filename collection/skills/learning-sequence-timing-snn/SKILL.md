---
name: learning-sequence-timing-snn
version: 1.0.0
description: Learning sequence timing and control of replay speed in networks of spiking neurons — biologically plausible mechanism for encoding element-specific timing and flexibly controlling replay speed via oscillatory background inputs.
triggers:
  - sequence timing
  - replay speed
  - spiking temporal memory
  - sTM model
  - sequence learning SNN
  - temporal pattern spiking
  - oscillatory replay
  - elapsed time encoding
tags:
  - spiking-neural-network
  - sequence-learning
  - temporal-coding
  - replay-mechanism
  - computational-neuroscience
  - biologically-plausible
---

# Learning Sequence Timing and Control of Replay Speed in Spiking Neural Networks

**Source**: arXiv:2605.22523 (May 2026)  
**Authors**: Melissa Lober, Younes Bouhadjar, Markus Diesmann, Tom Tetzlaff  
**Categories**: q-bio.NC

## Summary

Proposes a biologically plausible mechanism for encoding element-specific timing in spiking neural networks and flexibly controlling the speed of sequence replay via oscillatory background inputs. Extends the spiking Temporal Memory (sTM) model to learn not just sequence order but precise timing.

## Key Contributions

1. **Timing Encoding Mechanism**: Each sequence element duration is represented by sequential activation of element-specific neuronal populations, enabling encoding across a wide range of timescales
2. **Oscillatory Replay Control**: Oscillatory background inputs serve as clock signals providing robust and flexible mechanism for controlling replay speed
3. **Sparse Spatiotemporal Patterns**: Elapsed time is encoded by unique and sparse spatiotemporal patterns of neural activity
4. **EEG/LFP Correlation**: Replay speed during wakefulness and sleep correlates with global oscillatory activity characteristics in EEG/LFP recordings

## Core Methodology

### Spiking Temporal Memory (sTM) Model
- Each sequence element represented by small set of synchronously firing neurons
- Active neuron set encodes element identity in sequential context
- Original sTM learns order but NOT timing → extended to learn timing

### Timing Mechanism
- Duration of sequence elements → sequential activation of element-specific populations
- Enables encoding sequences across wide range of timescales
- Biologically plausible basis for learning/replaying complex temporal patterns

### Replay Speed Control
- Oscillatory background inputs act as clock signal
- Provides flexible speed modulation mechanism
- Speed correlates with characteristics of global oscillatory activity

## Technical Details

- **Neuron Model**: Spiking neurons with biologically realistic dynamics
- **Sequence Representation**: Sparse synchronous neuron groups
- **Timing Encoding**: Sequential population activation for duration
- **Speed Control**: Oscillatory input frequency modulation

## Applications

- Sequence learning and temporal pattern recognition
- Memory replay during sleep (hippocampal replay)
- Motor sequence timing (speech, movement)
- Sensory perception temporal processing
- Brain-computer interfaces for temporal decoding

## Implementation Guidance

```python
# Pseudocode for sTM with timing
class SpikingTemporalMemoryWithTiming:
    def __init__(self, n_elements, n_neurons_per_element):
        self.elements = n_elements
        self.neurons_per_element = n_neurons_per_element
        # Element-specific timing populations
        self.timing_populations = {}
        # Oscillatory background
        self.bg_frequency = 10.0  # Hz, modulates replay speed
    
    def encode_sequence(self, sequence, timings):
        for i, (element, duration) in enumerate(zip(sequence, timings)):
            # Activate element-specific neurons synchronously
            self.activate_element(i, element)
            # Sequential activation of timing population for duration
            self.encode_duration(i, duration)
    
    def replay(self, speed_factor=1.0):
        # Oscillatory background controls speed
        effective_freq = self.bg_frequency * speed_factor
        for element in self.sequence:
            self.replay_element(element, effective_freq)
```

## Connections to Other Research

- **Hippocampal Replay**: Directly models speed control of sharp-wave ripple replay
- **Theta Sequences**: Oscillatory framework connects to theta-paced sequence compression
- **Motor Timing**: Element-specific timing populations relate to basal ganglia timing circuits
- **Working Memory**: Sparse spatiotemporal patterns for temporal order maintenance

## Experimental Predictions

1. Sequence replay speed should correlate with background oscillation frequency
2. Element-specific neuronal populations should show duration-tuned sequential activation
3. EEG/LFP oscillation characteristics should predict replay speed during sleep
4. Lesioning oscillatory inputs should impair speed control but not sequence order
