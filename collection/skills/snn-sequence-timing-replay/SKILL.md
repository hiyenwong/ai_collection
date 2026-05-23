---
name: snn-sequence-timing-replay
description: "Biologically plausible spiking neural network model for learning sequence timing and controlling replay speed. Extends the spiking Temporal Memory (sTM) model to encode element-specific duration via sequential activation of neuronal populations, and uses oscillatory background inputs as a clock signal for speed modulation. Activation: sequence timing, spiking temporal memory, sTM, replay speed, sequence learning, spiking neural network, oscillatory clock, timing control, neural replay, sparse spatiotemporal patterns, EEG oscillations, LFP oscillations."
---

# Learning Sequence Timing and Control of Replay Speed in Networks of Spiking Neurons

> A biologically plausible spiking neural network model that learns not only the order but also the precise timing of sequence elements, with oscillatory inputs providing flexible speed control during replay.

## Metadata
- **Source**: arXiv:2605.22523
- **Authors**: Melissa Lober, Younes Bouhadjar, Markus Diesmann, Tom Tetzlaff
- **Published**: 2026-05-21
- **Subjects**: Neurons and Cognition (q-bio.NC)

## Core Methodology

### Key Innovation

Extends the spiking Temporal Memory (sTM) model to:
1. Encode element-specific **duration** (not just order) by sequential activation of dedicated neuronal populations
2. Use **oscillatory background inputs** as a biologically plausible clock signal for flexible speed control
3. Provide a mechanism where **elapsed time is encoded by unique sparse spatiotemporal activity patterns**

### Technical Framework

#### 1. Spiking Temporal Memory (sTM) Model Baseline
- Each sequence element is represented by a small set of synchronously firing neurons
- The set of active neurons encodes both the element's identity and its sequential context
- Original sTM learns order but not duration/timing

#### 2. Duration Encoding via Sequential Populations
- **Mechanism**: Each sequence element maps to a dedicated sub-population that activates sequentially
- Duration is encoded by the firing pattern within each population — longer durations activate more neurons in sequence
- Enables encoding sequences across a wide range of timescales (milliseconds to seconds)
- Biologically plausible: hippocampal time cells and cortical sequence cells show similar sequential activity

#### 3. Replay Speed Control via Oscillatory Clock
- **Oscillatory background inputs** serve as a global clock signal
- The frequency of the oscillation determines the speed of replay
- Higher oscillation frequency → faster replay (compressed in time)
- Lower oscillation frequency → slower replay (dilated in time)
- This provides a robust, flexible mechanism without requiring explicit timing parameters

#### 4. Speed-Rhythm Correlation
- Replay speed during wakefulness vs. sleep correlates with global oscillatory activity
- Faster replay during active wake (gamma/beta oscillations)
- Slower replay during sleep (theta/delta oscillations)
- Matches experimental EEG/LFP observations

### Key Findings

1. Elapsed time is encoded by **unique and sparse spatiotemporal patterns** of neural activity — not by a single clock or integrator
2. **Oscillatory inputs** provide a robust mechanism for flexibly controlling replay speed without disrupting sequence structure
3. The model reproduces experimental phenomena where replay during sleep is temporally compressed or dilated relative to the original experience

## Implementation Guide

### Prerequisites
- NEST Simulator or Brian2 (for spiking neural network simulation)
- Python with numpy, scipy

### Core Model Components

```
1. sTM network: recurrent SNN with sparse excitatory connections
2. Sequence encoding: each element → dedicated neuronal population
3. Duration mechanism: staggered activation within each population
4. Clock input: oscillatory current injection to all neurons
```

### Key Parameters
- `N_seq`: number of sequence elements
- `T_duration`: learned duration per element (ms)
- `f_clock`: oscillatory input frequency (Hz)
- `A_clock`: oscillatory input amplitude
- `N_pop`: neurons per element population

### Minimal Simulation Setup

```python
import nest
import numpy as np

# Create sTM network
neuron_params = {
    'C_m': 250.0,       # pF
    'tau_m': 20.0,       # ms
    'V_th': -55.0,       # mV
    'V_reset': -70.0,    # mV
    'E_L': -70.0         # mV
}

# Create oscillatory clock generator
clock = nest.Create('ac_generator', params={
    'amplitude': A_clock,
    'frequency': f_clock
})

# Create neuron populations for each sequence element
populations = []
for i in range(N_seq):
    pop = nest.Create('iaf_psc_alpha', N_pop, params=neuron_params)
    populations.append(pop)

# Connect clock to all populations
for pop in populations:
    nest.Connect(clock, pop, 'all_to_all',
                 syn_spec={'weight': 10.0, 'delay': 1.0})

# Connect populations in sequence order
for i in range(N_seq - 1):
    nest.Connect(populations[i], populations[i+1],
                 {'rule': 'pairwise_bernoulli', 'p': 0.1},
                 syn_spec={'weight': 50.0, 'delay': 2.0})
```

## Applications

1. **Computational neuroscience**: Model of hippocampal replay and sequence learning
2. **Neuromorphic computing**: Implementing timing-dependent computations in SNN hardware
3. **Sleep research**: Modeling memory consolidation through replay speed modulation
4. **Motor control**: Learning precise temporal sequences for movement
5. **Sensory processing**: Encoding spatiotemporal patterns in auditory and visual cortex

## Predictions
1. Sequence element duration is encoded by unique sparse spatiotemporal activity patterns
2. Manipulating oscillatory activity should change replay speed proportionally
3. Replay speed during different brain states correlates with dominant oscillation frequency

## Related Skills
- learning-sequence-timing-spiking-neurons
- working-memory-heterogeneous-delays
- snn-working-memory-heterogeneous-delays-v3
- attractor-models-language-reasoning
