---
name: sequence-timing-snn-replay
category: neuroscience
description: Spiking neural network methodology for learning sequence timing and controlling replay speed through STDP-based temporal encoding.
source: arxiv:2605.22523
created: 2026-05-25
activation: sequence timing, replay speed, spiking neurons, STDP, temporal encoding, sequence learning, temporal abstraction, brain function
---

# Sequence Timing & Replay Speed Control in Spiking Neural Networks

## Overview

Methodology for encoding and reproducing temporal sequences in spiking neural networks through **sequential activation of element-specific neuronal populations**. Enables sequence learning across a wide range of timescales with controllable replay speed.

**Source**: arXiv:2605.22523 - "Learning Sequence Timing and Control of Replay Speed in Networks of Spiking Neurons" (Lober, Bouhadjar, Diesmann, Tetzlaff, 2026)

## Core Mechanism

1. **Element-Specific Population Encoding**: Each sequence element is represented by a dedicated neuronal population
2. **Sequential Activation**: Duration of sequence elements is encoded by the order and timing of population activations
3. **STDP Learning**: Spike-timing-dependent plasticity learns the temporal relationships between populations
4. **Replay Speed Control**: The network can reproduce learned sequences at different speeds by modulating the activation dynamics

## Key Principles

### Temporal Abstraction
- Sequential inputs → dedicated populations → temporal patterns
- Wide timescale encoding (milliseconds to seconds)
- Speed-invariant sequence representation

### STDP-Based Learning
- Causal spike timing strengthens forward connections
- Anti-causal timing weakens or prevents backward connections
- Temporal windows determine which connections are learned

### Replay Mechanism
- Partial cue triggers full sequence replay
- Replay speed is controlled by network dynamics parameters
- Temporal structure is preserved even at different speeds

## Implementation Pattern

```python
# Pseudocode for sequence timing SNN
class SequenceTimingSNN:
    def __init__(self, n_elements, n_neurons_per_element):
        # Element-specific populations
        self.populations = [NeuronPool(n_neurons_per_element) for _ in range(n_elements)]
        self.stdp = STDP(learning_rate=0.01, window=20ms)
        
    def encode_sequence(self, sequence, durations):
        """Encode temporal sequence with element-specific timing"""
        for element, duration in zip(sequence, durations):
            pop = self.populations[element]
            pop.activate(duration=duration)  # Duration encodes timing
            self.stdp.update(pre=pop, post=next_population)
    
    def replay(self, speed_factor=1.0):
        """Replay sequence at controlled speed"""
        cue = self.populations[0]
        cue.activate(duration=base_duration / speed_factor)
        # Sequential activation propagates through learned connections
```

## Use Cases

- **BCI temporal decoding**: Understanding how the brain encodes movement sequences
- **Temporal pattern recognition**: Learning and reproducing time-series patterns
- **Working memory models**: Sequence storage and retrieval with timing
- **Motor control**: Learning and executing movement sequences at variable speeds
- **Speech processing**: Temporal encoding of phoneme sequences

## Related Skills

- `spiking-neural-network-analysis` - SNN analysis methodology
- `stochastic-synaptic-plasticity` - STDP mathematical modeling
- `brain-inspired-snn-pattern-analysis` - Brain-inspired SNN patterns
- `snn-sequence-timing-replay` - Related sequence timing work

## Activation Keywords

sequence timing, replay speed, spiking neurons, STDP, temporal encoding, sequence learning, temporal abstraction, brain function, element-specific population, spike-timing-dependent plasticity, temporal patterns
