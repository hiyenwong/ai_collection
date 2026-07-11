---
name: snn-sequence-timing-replay-speed
description: "Spiking Temporal Memory (sTM) model for learning sequence timing and flexible replay speed control - biologically plausible timing encoding via oscillatory modulation"
trigger_words:
  - spiking neural network
  - sequence timing
  - replay speed
  - spTM temporal memory
  - oscillatory control
  - sequential processing
  - spatiotemporal patterns
activation_keywords:
  - sequence timing learning
  - replay speed control
  - oscillatory background
  - spatiotemporal encoding
  - element-specific timing
  - sparse representation
version: 1.0.0
last_updated: 2026-06-19
paper_source: arXiv:2605.22523
authors: Melissa Lober, Younes Bouhadjar, Markus Diesmann, Tom Tetzlaff
submitted: 2026-05-21
---

# Learning Sequence Timing and Control of Replay Speed in Networks of Spiking Neurons

## Background

Processing sequential inputs is a **fundamental brain function**, underlying:
- Sensory perception
- Language processing
- Motor control

**Challenge**: Represent not only event **order**, but also their **precise timing**.

Existing models can learn sequential structure but lack:
- Biologically plausible mechanisms for element-specific timing
- Flexible control of replay speed

## Core Innovation: Spiking Temporal Memory (sTM) Model

### Previous sTM Capabilities

- Each sequence element represented by **small set of neurons firing synchronously**
- Element identity encoded in **set of active neurons** (sequential context)
- Could learn **order** but not **timing**

### New Contributions

1. **Duration Encoding**: Element-specific timing via sequential activation of neuronal populations
2. **Wide Timescale Coverage**: Encode sequences across diverse durations
3. **Replay Speed Control**: Oscillatory background inputs serve as clock signal
4. **Biological Plausibility**: Sparse spatiotemporal patterns encode elapsed time

## Methodology

### Timing Mechanism

**Key insight**: Duration of sequence elements represented by **sequential activation of element-specific neuronal populations**

```
Element A → Population A neurons fire in sequence
- Neuron 1 (time t0)
- Neuron 2 (time t0+δ)
- Neuron 3 (time t0+2δ)
...
Duration = N * δ (where N = number of neurons in population)
```

### Replay Speed Control

**Oscillatory background inputs** act as:
- Clock signal for sequence replay
- Flexible speed modulation mechanism
- Correlated with EEG/LFP characteristics

```
Fast oscillations → Fast replay
Slow oscillations → Slow replay
```

### Encoding Principles

- **Elapsed time** encoded by **unique sparse spatiotemporal patterns**
- Each moment has distinct neural signature
- No dedicated "time neurons" - timing emerges from population dynamics

## Key Findings

### 1. Timing Representation

- **Unique spatiotemporal patterns** for each time point
- **Sparse activation**: Only subset of neurons active per moment
- **Context-dependent**: Same element, different timing = different patterns

### 2. Replay Speed Correlation

Speed during **wakefulness and sleep** correlates with:
- Global oscillatory activity
- EEG/LFP characteristics

```
Waking: Faster oscillations → faster replay
Sleep: Slower oscillations → slower replay (memory consolidation)
```

### 3. Biological Basis

Framework provides biological explanation for:
- How temporal patterns are learned
- Why replay speed varies (oscillations)
- Sparse, distributed timing representations

## Neuroscience Implications

### Sequence Processing in Brain

1. **Order**: Learned through synaptic plasticity
2. **Timing**: Encoded in spatiotemporal population patterns
3. **Speed**: Controlled by global oscillations

### Behavioral Correlations

- EEG alpha/beta rhythms → replay speed indicators
- LFP oscillation frequency → temporal compression factor
- Sleep replay → consolidation mechanisms

## Implementation

### Model Architecture

```python
# sTM Model Structure
Element A represented by Population {N_A1, N_A2, ...}

# Timing Encoding
def encode_duration(element, duration):
    for neuron in element.population:
        neuron.fire_at(time_offset)
    
# Replay with oscillatory control
def replay(sequence, oscillation_freq):
    for element in sequence:
        timing = duration / oscillation_freq
        activate(element.population, timing)
```

### Training

- STDP-based learning for sequence structure
- Duration learning through population size modulation
- Speed control via oscillation parameter

## Applications

1. **Sequence Memory** - Temporal pattern storage
2. **Music/Rhythm** - Precise timing representation
3. **Motor Control** - Action sequence timing
4. **Language** - Syntactic sequence timing
5. **Memory Consolidation** - Sleep replay modeling

## Relation to Biology

### Hippocampal Replay

- Place cell sequences during sleep
- Temporal compression during replay
- Oscillatory modulation (theta rhythms)

### Cortical Processing

- Sensory sequence analysis
- Motor command sequences
- Working memory timing

## Key Technical Insights

### Sparse Spatiotemporal Encoding

- **Unique patterns**: Each time point distinct
- **Sparse**: Few neurons active at any moment
- **Efficient**: High information density

### Oscillatory Clock

- **Flexible**: Speed adjustable via oscillation frequency
- **Robust**: Consistent timing despite noise
- **Biological**: Matches observed oscillations

### Population-Based Duration

- **Scalable**: Different populations → different durations
- **Contextual**: Same element, different timing possible
- **Learnable**: Plasticity can adjust population sizes

## Validation

Model demonstrates:
- Correct sequence order learning
- Precise timing encoding
- Flexible replay speed
- Correlation with EEG/LFP data

## Future Directions

- Multi-modal sequence integration
- Attention-modulated timing
- Hierarchical temporal structure
- Neuromorphic hardware implementation
- Clinical applications (timing disorders)

## Critical Significance

This work provides:
- **First biologically plausible timing mechanism** in spiking networks
- **Flexible replay control** via oscillations
- **Connection to measured brain signals** (EEG/LFP)
- **Sparse encoding** matching neural observations

## Bridge to Neuromorphic Computing

- Efficient timing representation
- Oscillatory speed control implementable
- Population-based duration scalable
- Sparse activation energy-efficient