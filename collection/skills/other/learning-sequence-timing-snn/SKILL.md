---
id: learning-sequence-timing-snn
title: Learning Sequence Timing and Control of Replay Speed in Spiking Neural Networks
description: Learning sequence timing and control of replay speed in networks of spiking neurons. The spiking Temporal Memory (sTM) model encodes element-specific timing via sequential neuronal population activation, with oscillatory inputs serving as clock signals for flexible replay speed control.
tags:
  - spiking-neural-networks
  - sequence-learning
  - temporal-memory
  - sequence-timing
  - replay-speed
  - oscillatory-dynamics
  - biological-plausibility
  - hippocampus
  - working-memory
  - EEG-LFP
arxiv: "2605.22523"
authors: "Melissa Lober, Younes Bouhadjar, Markus Diesmann, Tom Tetzlaff"
published: "2025-05-28"
---

# Learning Sequence Timing and Control of Replay Speed in Spiking Neural Networks

## Overview

This work extends the **spiking Temporal Memory (sTM) model** to encode not just sequence order but also **element-specific timing**, while introducing a mechanism for **flexible replay speed control** via oscillatory background inputs.

**Core Problem**: How does the brain encode both *what* happens and *when* in sequences? How can replay speed be flexibly modulated (e.g., fast replay during sleep vs. real-time replay)?

**Key Contributions**:
1. Mechanism for encoding element duration via sequential sub-population activation
2. Oscillatory inputs as clock signals for flexible replay speed modulation
3. Biological connection: elapsed time ≡ unique spatiotemporal spike patterns

**arXiv**: 2605.22523 | Published: 2025-05-28

## Core Architecture: spiking Temporal Memory (sTM)

### Sequence Encoding Principle
```
Each sequence element E_i → small set of neurons firing synchronously
Active neuron set encodes element identity + sequential context
```

The sTM model uses **sparse, context-dependent representations**:
- Each element has a different active population depending on what came before
- This provides unique identification even for repeated elements in a sequence

### Element Timing Encoding (New Mechanism)
```
Duration(E_i) → sequential activation of element-specific sub-populations

E_i duration = T_i time steps
→ T_i sub-populations activate one by one
→ Each sub-population active for 1 time step
→ Elapsed time encoded by which sub-population is active
```

**Key insight**: Time is represented by *which neurons are active*, not by persistent activity or decay — purely spatial encoding of temporal information.

```python
# Conceptual implementation
def encode_sequence_with_timing(sequence, durations):
    # For each element with its duration
    for element_i, duration_i in zip(sequence, durations):
        # Activate sub-populations sequentially
        for t in range(duration_i):
            sub_pop = get_subpopulation(element_i, t)
            activate_neurons(sub_pop)
            # Each unique (element, t) → unique sparse pattern
```

### Replay Speed Control via Oscillations
```
Global oscillatory input → clock signal → controls replay speed

High oscillation frequency → fast replay
Low oscillation frequency → slow replay
```

The biological correspondence:
- **Wakefulness**: θ-band oscillations (4-8 Hz) → real-time replay
- **Sleep (SWS)**: sharp-wave ripples → fast replay/consolidation
- **EEG/LFP oscillation characteristics** → directly predict replay speed

## Key Mechanisms

### 1. Temporal Sub-Population Structure
```python
class TemporalMemoryNetwork:
    def __init__(self, n_elements, max_duration, neurons_per_subpop):
        # Sub-populations: (element, time_within_element) → neuron set
        self.sub_populations = {
            (elem, t): create_neuron_set(neurons_per_subpop)
            for elem in range(n_elements) 
            for t in range(max_duration)
        }
        # Learned synaptic connections via STDP
        self.weights = initialize_connections()
    
    def present_sequence(self, sequence, durations):
        for elem, dur in zip(sequence, durations):
            for t in range(dur):
                self.activate(self.sub_populations[(elem, t)])
```

### 2. Oscillatory Clock Mechanism
```python
def oscillatory_input(t, frequency, amplitude=1.0):
    """Global oscillatory background input"""
    return amplitude * np.sin(2 * np.pi * frequency * t)

def replay_with_oscillation(network, frequency):
    """Replay speed controlled by oscillation frequency"""
    for step in range(total_replay_steps):
        osc_drive = oscillatory_input(step, frequency)
        # Higher oscillation → stronger drive → faster progression
        network.step(background_input=osc_drive)
```

### 3. Sparse Spatiotemporal Encoding
```
Elapsed time since element onset → unique sparse pattern
Identity of element × time within element → unique neuron subset active
```

This allows:
- **Unambiguous time reading**: Any snapshot of activity → knows what + when
- **Scalable timing**: Add more sub-populations for finer time resolution
- **Biological plausibility**: Matches hippocampal sequence cell observations

## Experimental Results

### Sequence Timing Encoding
- Successfully encodes sequences with varied element durations
- Timing preserved across a wide range of timescales
- Sparse activity patterns uniquely identify (element, time) pairs

### Replay Speed Control
- Oscillation frequency linearly controls replay speed
- Works across biologically observed frequency ranges (δ, θ, γ)
- Robust to noise in oscillatory input

### Connection to EEG/LFP
- Replay speed during wakefulness ∝ θ-band power
- Fast replay during sleep correlates with high-frequency ripple activity
- Provides testable predictions for electrophysiology experiments

## Biological Relevance

### Hippocampal Connection
| Model Feature | Biological Counterpart |
|---|---|
| Sub-population activation | Place/time cells in hippocampus |
| Sequential propagation | Theta sequences |
| Oscillatory clock | Hippocampal theta oscillations |
| Fast replay | Sleep ripples |
| Sparse coding | Sparse hippocampal activity |

### Motor and Language Sequences
- Motor cortex: millisecond-precise timing for skilled movements
- Language: phoneme/syllable timing in speech production
- Working memory: ordered recall with temporal context

## Applications

### 1. Biologically Plausible Sequence Models
```python
# Train sTM model on sequences with precise timing
model = SpikingTemporalMemory(
    n_elements=26,          # e.g., alphabet
    max_element_duration=10, # max 10 timesteps per element
    subpop_size=20           # neurons per sub-population
)
model.learn_sequence(sequence="HELLO", 
                     durations=[3, 2, 4, 3, 2])
model.replay(speed_osc_freq=8.0)  # 8 Hz theta → real-time
model.replay(speed_osc_freq=80.0)  # 80 Hz ripple → fast replay
```

### 2. Sleep/Memory Consolidation Modeling
```python
# Model sleep replay for memory consolidation
awake_replay = model.replay(osc_frequency=theta_freq)
sleep_replay = model.replay(osc_frequency=ripple_freq)
# Fast sleep replay allows more consolidation cycles
```

### 3. Neural Data Analysis
```python
# Predict replay speed from LFP recordings
lfp_freq = estimate_dominant_frequency(lfp_signal)
predicted_replay_speed = model.freq_to_speed(lfp_freq)
```

## When to Use This Skill

- Building SNN models of sequence learning with precise timing
- Studying temporal coding in hippocampus/cortex
- Modeling sleep replay and memory consolidation
- Understanding oscillatory control of sequential behavior
- Analyzing EEG/LFP recordings in context of sequence replay
- Creating biologically plausible working memory models

**Trigger keywords**: sequence timing, spiking temporal memory, replay speed, oscillatory clock, hippocampal sequences, theta sequences, sleep replay, temporal coding SNN

## Implementation Tips

1. **Sub-population size**: 10-30 neurons is typically sufficient for unique identification
2. **Learning rule**: STDP naturally captures sequence order; pair with explicit timing labels for duration
3. **Oscillation integration**: Use additive background current, not multiplicative gating
4. **Timescales**: Model works from milliseconds (motor) to seconds (language/navigation)
5. **Initialization**: Random sparse connectivity → STDP → structured sequence weights

## Connections to Related Work

- **Temporal Memory** (Hawkins & Ahmad): Hierarchical temporal memory framework
- **Place cells/time cells** (Pastalkova et al.): Hippocampal sequential representations  
- **Theta sequences** (Dragoi & Buzsáki): Compressed sequence representations during theta
- **Sleep replay** (Wilson & McNaughton): Fast replay during SWS for consolidation
- **FORCE learning**: Alternative SNN sequence learning via supervised feedback
