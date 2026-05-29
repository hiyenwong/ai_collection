---
name: stm-sequence-timing-replay
description: Spiking Temporal Memory (sTM) model for learning sequence timing and controlling replay speed via oscillatory background inputs. Provides biologically plausible mechanisms for encoding element-specific timing and flexible speed control.
version: 1.0.0
author: Melissa Lober, Younes Bouhadjar, Markus Diesmann, Tom Tetzlaff
arxiv_id: 2605.22523
created: 2026-05-30
category: neuroscience
tags: [spiking neural network, sequence timing, replay, temporal memory, oscillation, neuroscience]
activation_keywords: [sequence timing, replay speed, sTM, spiking temporal memory, oscillatory control, temporal encoding]
---

# Spiking Temporal Memory (sTM): Sequence Timing and Replay Speed Control

## Overview

A biologically inspired network model that extends the spiking Temporal Memory (sTM) framework to learn not only the order of sequence elements but also their precise timing, with flexible control of replay speed via oscillatory background inputs.

**Source**: arXiv:2605.22523 (Submitted 21 May 2026)
**Authors**: Melissa Lober, Younes Bouhadjar, Markus Diesmann, Tom Tetzlaff
**Category**: Quantitative Biology - Neurons and Cognition (q-bio.NC)

## Key Concepts

### 1. Sequence Processing Challenge
- Traditional models learn **order** but not **timing** of sequence elements
- Need biologically plausible mechanisms for:
  - Encoding element-specific timing
  - Flexibly controlling replay speed

### 2. sTM Model Foundation
- Each sequence element represented by **small set of synchronously firing neurons**
- Active neuron set encodes element identity in its **sequential context**
- Original version: learns order but **not timing**

### 3. Duration Encoding Mechanism
```
Element Duration → Sequential Activation of Element-Specific Populations
                  → Enables encoding across wide range of timescales
```

- Duration of each sequence element encoded by:
  - Sequential activation of **element-specific neuronal populations**
  - Unique and **sparse spatiotemporal patterns** for elapsed time

### 4. Oscillatory Background as Clock Signal
- **Oscillatory background inputs** serve as clock signal
- Provides **robust and flexible mechanism** for:
  - Controlling sequence replay speed
  - Modulating speed during wakefulness and sleep

### 5. Speed-Replay Correlation
- Replay speed correlates with:
  - Characteristics of **global oscillatory activity**
  - Observed in EEG or LFP recordings
  - Different during wakefulness vs. sleep

## Implementation Approach

### Network Architecture
1. **Element representation**: Synchronous firing of small neuron groups
2. **Timing encoding**: Sequential population activation for each element
3. **Speed control**: Oscillatory background input modulation
4. **Context encoding**: Sequence-specific neural activation patterns

### Learning Mechanism
- Biologically plausible learning rules
- No need for external clock signals
- Self-organizing timing representation

### Key Parameters
- Oscillation frequency (clock speed)
- Population size per element
- Timing precision requirements
- Replay speed modulation factor

## Applications

### Use Cases
- **Sensory perception**: Processing sequential sensory inputs
- **Language processing**: Sequential word/syllable timing
- **Motor control**: Timed action sequences
- **Memory replay**: Hippocampal replay during sleep
- **BCI systems**: Sequence timing interpretation

### When to Use
- Modeling temporal sequences with precise timing requirements
- Investigating replay speed modulation mechanisms
- Understanding oscillation-cognition relationships
- Designing biologically plausible sequence learning systems

## Biological Implications

### 1. Time Encoding Hypothesis
- **Elapsed time** encoded by unique sparse spatiotemporal patterns
- Different from traditional "clock neurons" hypothesis
- Distributed representation across network

### 2. Oscillation-Replay Connection
- Global oscillatory activity determines replay speed
- Explains different replay speeds:
  - During **wakefulness**: Faster oscillations → faster replay
  - During **sleep**: Slower oscillations → slower replay
- Links EEG/LFP characteristics to sequence processing

### 3. Sequence Learning Mechanism
- Biologically plausible: no external timekeeper needed
- Self-organizing: timing emerges from network dynamics
- Flexible: speed controlled by oscillatory modulation

## Technical Details

### Spiking Implementation
```python
# Conceptual sTM model structure
class SpikingTemporalMemory:
    def __init__(self):
        self.element_populations = {}  # Per-element neuron groups
        self.timing_encoder = {}       # Duration encoding
        self.oscillation_input = None  # Clock signal
        
    def encode_sequence(self, sequence, timings):
        for element, duration in zip(sequence, timings):
            # Activate element-specific population sequentially
            self._activate_population(element, duration)
            
    def set_replay_speed(self, oscillation_freq):
        # Modulate replay via oscillatory input
        self.oscillation_input = oscillation_freq
```

### Oscillatory Control Mechanism
- Input: Background oscillation signal (e.g., theta, alpha)
- Effect: Determines rate of population transitions
- Higher frequency → faster replay
- Lower frequency → slower replay

## Comparison with Related Models

| Model | Order | Timing | Speed Control | Biological |
|-------|-------|--------|---------------|------------|
| Traditional RNN | Yes | Implicit | No | Limited |
| LSTM | Yes | Explicit | No | Limited |
| sTM (original) | Yes | No | No | Yes |
| sTM (extended) | Yes | Yes | Yes | Yes |

## Research Questions

1. How does oscillatory frequency precisely map to replay speed?
2. What determines the optimal population size per element?
3. How are timing patterns consolidated during sleep?
4. What role do different oscillation bands play?

## Key Equations

### Timing Encoding
- Duration D → Number of population activations N
- N = D × f(oscillation) where f is oscillation frequency

### Replay Speed
- Speed S = f(oscillation) × k (modulation constant)
- Correlates with EEG/LFP power in specific bands

## Experimental Validation

### Predictions
1. EEG oscillation changes → replay speed changes
2. Sequence timing affects spatiotemporal patterns
3. Sleep vs. wakefulness replay speed differences
4. Population-specific activation timing

### Testable Hypotheses
- Oscillatory entrainment affects sequence learning
- Timing patterns are sparse and element-specific
- Speed modulation is oscillation-frequency dependent

## Limitations

1. Requires specific oscillatory input patterns
2. Timing precision limited by oscillation frequency
3. Population size constraints for wide timescales
4. Complex sequences may require hierarchical structure

## Future Directions

- Integration with hierarchical sequence models
- Multi-timescale timing encoding
- Sleep replay optimization mechanisms
- Clinical applications for timing disorders

## References

- Original sTM model: Diesmann et al.
- Free Energy Principle connections
- Oscillation-cognition literature
- Hippocampal replay research

---

## Quick Reference

**Activation Keywords**: sequence timing, replay speed, sTM, spiking temporal memory, oscillatory control, temporal encoding

**Use When**: 
- Modeling temporal sequences with timing requirements
- Investigating oscillation-speed relationships
- Designing biologically plausible sequence systems
- Understanding replay mechanisms

**Core Insight**: Oscillatory background inputs act as flexible clock signals, enabling precise timing encoding and replay speed control without dedicated timekeeper neurons.