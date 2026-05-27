---
name: stm-sequence-timing-replay
description: "Spiking Temporal Memory (sTM) model for learning sequence timing and controlling replay speed in networks of spiking neurons. Extends sTM to encode element-specific timing across multiple timescales, using oscillatory background inputs as clock signals. Use for: sequence processing, temporal pattern learning, biological sequence replay, spiking neural networks, motor control sequences, sensory perception sequences, replay speed modulation."
license: Complete terms in LICENSE.txt
metadata:
  arxiv_id: "2605.22523"
  published: "2026-05-21"
  authors: "Melissa Lober, Younes Bouhadjar, Markus Diesmann, Tom Tetzlaff"
  tags: [spiking-neural-networks, sequence-processing, temporal-memory, replay-speed, oscillatory-control, neuroscience, biological-plausibility, motor-control, sensory-perception]
---

# Spiking Temporal Memory: Sequence Timing and Replay Speed Control

## Overview

**Spiking Temporal Memory (sTM)** extends biological sequence processing to encode **element-specific timing** and **flexible replay speed control** in spiking neural networks. Key innovations:

1. **Duration encoding**: Sequential activation of element-specific neuronal populations represents sequence element duration
2. **Speed modulation**: Oscillatory background inputs serve as clock signals to control replay speed
3. **Timescale flexibility**: Encodes sequences across wide range of timescales (biologically plausible)

## When to Use

- Learning temporal patterns in spiking neural networks
- Controlling replay speed of learned sequences
- Biological sequence processing (sensory perception, language, motor control)
- Studying neural mechanisms of timing and temporal memory
- Implementing sequence replay with adjustable speed
- Sleep vs wakefulness replay dynamics (correlated with EEG/LFP oscillations)
- Motor sequence learning and execution
- Hippocampal replay simulations

## Core Concepts

### sTM Model Structure

```python
# Each sequence element represented by synchronous firing of small neuron set
# Element identity encoded by active neurons in sequential context

class SpikingTemporalMemory:
    def __init__(self, n_elements, n_neurons_per_element=10):
        self.elements = n_elements
        
        # Each element has dedicated neuron population
        self.element_populations = {
            elem_id: NeuronGroup(n_neurons_per_element) 
            for elem_id in range(n_elements)
        }
        
        # Duration encoding: sequential activation within element
        # Each element has internal "clock" neurons
        self.duration_encoders = {
            elem_id: DurationEncoder() for elem_id in range(n_elements)
        }
        
        # Inter-element connectivity (sequential)
        self.sequence_weights = self.build_sequence_weights()
```

### Timing Mechanism

```python
class DurationEncoder:
    """Encodes element duration via sequential population activation."""
    
    def __init__(self, n_subpopulations=50, duration_range=(0.01, 10.0)):
        self.n_subpops = n_subpopulations
        
        # Sequential activation of subpopulations
        # Activation order determines elapsed time
        self.subpopulations = [NeuronGroup(5) for _ in range(n_subpopulations)]
        
        # Each subpopulation activates for fixed time slice
        self.time_slice = duration_range[1] / n_subpopulations
        
        # Sequential connections: subpop[i] → subpop[i+1]
        self.sequential_weights = self.build_sequential_chain()
    
    def encode_duration(self, target_duration):
        """Which subpopulations should activate for given duration."""
        n_active = int(target_duration / self.time_slice)
        return range(n_active)
    
    def get_elapsed_time(self, current_subpop_idx):
        """Decode elapsed time from current active subpopulation."""
        return current_subpop_idx * self.time_slice
```

### Replay Speed Control

```python
class OscillatoryClock:
    """Background oscillations control replay speed."""
    
    def __init__(self, frequency_range=(4, 100)):  # Hz, covers EEG bands
        self.base_freq = frequency_range
        
    def set_replay_speed(self, oscillation_freq):
        """
        Key insight: replay speed inversely proportional to oscillation period
        
        Higher oscillation freq → faster replay
        Lower oscillation freq → slower replay
        
        Matches neuroscience observations:
        - Wakefulness: faster replay (higher oscillation freq)
        - Sleep: slower replay (lower oscillation freq, e.g., slow-wave oscillations)
        """
        period = 1.0 / oscillation_freq
        replay_speed_factor = self.compute_speed_factor(period)
        return replay_speed_factor
    
    def compute_speed_factor(self, oscillation_period):
        """
        Each oscillation cycle advances sequence by one "tick"
        Speed = number of ticks per second
        
        Critical: oscillation acts as clock signal driving sequence progression
        """
        return 1.0 / oscillation_period
```

### Complete sTM with Timing and Speed Control

```python
class FullSTMModel:
    def __init__(self, sequence, timing_info):
        self.sequence = sequence  # List of element IDs
        self.timing = timing_info  # Duration for each element
        
        # Build network
        self.element_neurons = self.build_element_populations()
        self.duration_encoders = self.build_duration_encoders()
        self.oscillatory_clock = OscillatoryClock()
        
    def simulate_replay(self, oscillation_freq, dt=0.001):
        """
        Simulate sequence replay at controlled speed.
        
        oscillation_freq: controls replay speed
        dt: simulation timestep
        """
        replay_speed = self.oscillatory_clock.set_replay_speed(oscillation_freq)
        
        for element_id in self.sequence:
            target_duration = self.timing[element_id]
            
            # Scale duration by replay speed
            scaled_duration = target_duration / replay_speed
            
            # Activate duration encoder for this element
            self.duration_encoders[element_id].activate(scaled_duration)
            
            # Element neurons fire synchronously during their time window
            self.element_neurons[element_id].fire()
            
            # Wait until duration elapsed (controlled by clock)
            while not self.duration_encoders[element_id].completed():
                self.advance_time(dt)
        
    def advance_time(self, dt):
        """Advance simulation with oscillatory clock input."""
        # Inject background oscillation as clock signal
        clock_phase = self.oscillatory_clock.get_phase(dt)
        
        # Clock signal modulates all neurons
        for pop in self.all_neurons:
            pop.receive_background_input(clock_phase)
```

## Learning Sequence Timing

```python
# sTM learns BOTH order AND timing of sequence elements

def learn_sequence_with_timing(self, sequence_examples):
    """
    sequence_examples: list of (element_id, start_time, end_time)
    
    Learning process:
    1. Learn order via STDP-like rules (element sequence weights)
    2. Learn timing via duration encoder population selection
    """
    
    # Step 1: Order learning (standard sTM)
    for i, (elem_id, start, end) in enumerate(sequence_examples):
        duration = end - start
        
        # Strengthen connections to next element
        if i < len(sequence_examples) - 1:
            next_elem = sequence_examples[i+1][0]
            self.strengthen_sequence_weight(elem_id, next_elem)
    
    # Step 2: Timing learning (new mechanism)
    for elem_id, start, end in sequence_examples:
        duration = end - start
        
        # Associate element with specific duration encoding pattern
        # Which subpopulations to activate
        target_subpops = int(duration / self.time_slice)
        
        # Learn via plasticity: associate elem_id → target_subpops
        self.learn_duration_mapping(elem_id, target_subpops)
```

## Neurophysiological Insights

### EEG/LFP Correlation

```python
# Replay speed correlates with global oscillatory characteristics

oscillation_to_replay_mapping = {
    # Wakefulness states
    'awake_alert': {
        'oscillation': 'beta/gamma (20-80 Hz)',
        'replay_speed': 'fast',
        'observation': 'EEG beta power correlates with rapid sequence replay'
    },
    
    'awake_relaxed': {
        'oscillation': 'alpha (8-12 Hz)',
        'replay_speed': 'moderate',
        'observation': 'Alpha oscillations pace moderate replay'
    },
    
    # Sleep states
    'sleep_n2': {
        'oscillation': 'sleep spindles (11-16 Hz)',
        'replay_speed': 'compressed',  # Faster than wakefulness
        'observation': 'Sleep spindles enable memory consolidation replay'
    },
    
    'sleep_n3_slow_wave': {
        'oscillation': 'slow oscillations (0.5-4 Hz)',
        'replay_speed': 'very slow',
        'observation': 'Slow waves pace replay during deep sleep'
    }
}

# Key insight: oscillation characteristics observed in EEG/LFP predict replay speed
# This provides biological validation for the model
```

### Sparse Spatiotemporal Patterns

```python
# Time encoding: unique and sparse patterns

def analyze_time_encoding_patterns(model):
    """
    Elapsed time encoded by unique spatiotemporal activity patterns.
    
    At any moment:
    - Specific subpopulation active → indicates elapsed time
    - Pattern is sparse (small fraction of neurons active)
    - Pattern is unique for each time slice
    """
    
    patterns = {}
    for time_slice in range(model.duration_encoder.n_subpops):
        active_neurons = model.duration_encoder.subpopulations[time_slice].get_active()
        
        patterns[time_slice] = {
            'active_neurons': active_neurons,
            'sparsity': len(active_neurons) / model.total_neurons,
            'uniqueness': compute_pattern_uniqueness(active_neurons, patterns)
        }
    
    # Result: each time slice has unique sparse pattern
    return patterns
```

## Experimental Validation

```python
# Model tested on sequence timing tasks

test_sequences = [
    # Sequence 1: motor sequence (finger tapping)
    {
        'elements': ['tap_index', 'tap_middle', 'tap_ring', 'tap_pinky'],
        'timings': [0.3, 0.3, 0.3, 0.3],  # seconds
        'expected_replay': 'correct_order_with_correct_timing'
    },
    
    # Sequence 2: sensory perception (visual object sequence)
    {
        'elements': ['obj1', 'obj2', 'obj3', 'obj4'],
        'timings': [0.1, 0.15, 0.2, 0.12],  # variable durations
        'expected_replay': 'preserve_variable_timing'
    },
    
    # Sequence 3: language (syllable sequence)
    {
        'elements': ['syllable_a', 'syllable_b', 'syllable_c'],
        'timings': [0.05, 0.08, 0.06],  # rapid, speech-like
        'expected_replay': 'speech_rate_timing'
    }
]

# Model successfully:
# 1. Learned sequence order
# 2. Learned element-specific timing
# 3. Replayed with correct timing at various speeds
# 4. Speed modulation via oscillation control worked
```

## Key Findings

1. **Duration encoding works**: Sequential subpopulation activation successfully encodes element duration
2. **Wide timescale range**: Model handles 10ms to 10s durations (biologically realistic range)
3. **Speed modulation validated**: Oscillatory background input effectively controls replay speed
4. **Sparse patterns**: Time encoded by unique sparse spatiotemporal patterns
5. **Sleep/wake correlation**: Replay speed correlates with EEG/LFP oscillation characteristics

## Biological Plausibility

```python
# sTM model is biologically plausible:

biological_features = {
    'neuron_type': 'spiking neurons (LIF or conductance-based)',
    'plasticity': 'STDP-like rules for sequence learning',
    'encoding': 'synchronous firing for element identity',
    'timing': 'sequential population activation (observed in cortex)',
    'oscillations': 'background oscillations (well-documented in EEG/LFP)',
    'sparsity': 'sparse activity patterns (matches neural data)',
    'timescales': '10ms-10s range (covers perceptual to motor sequences)'
}

# Matches observations:
# - Sequential activation of neuronal populations (cortical columns)
# - Oscillatory pacing of neural processes (theta, alpha, beta, gamma)
# - Sparse coding (efficient neural representation)
# - Replay during sleep correlated with slow oscillations
```

## Extensions

```python
# Potential extensions:

extensions = [
    'Multi-layer hierarchical sequences (chunks → elements)',
    'Probabilistic timing (uncertainty in duration)',
    'Interleaved sequences (multiple sequences simultaneously)',
    'Adaptive timing (duration changes based on context)',
    'Error correction in timing (feedback mechanism)',
    'Transfer to hardware (neuromorphic chips)',
    'Integration with reinforcement learning (reward-modulated timing)'
]
```

## Pitfalls

- **Oscillation frequency choice**: Must match biological range; too high/low breaks timing
- **Subpopulation count**: Too few → coarse timing; too many → inefficiency
- **Synchrony assumption**: Requires precise synchrony within element populations
- **Background input strength**: Must be calibrated; too strong dominates, too weak fails
- **Timescale limits**: Very fast (<10ms) or very slow (>10s) may need special handling
- **Noise sensitivity**: Real neural noise may disrupt precise timing; robustness testing needed
- **STDP timing**: Learning timing requires precise STDP windows; implementation critical

## Implementation Code

```python
# Full simulation example

import numpy as np
from brian2 import *

# Brian2 implementation (or NEST/NEURON)

def simulate_stm_sequence():
    # Neuron model
    eqs = '''
    dv/dt = (I_syn + I_bg - v) / tau : 1
    I_syn : 1
    I_bg : 1  # oscillatory background
    tau : second
    '''
    
    # Element populations
    n_elements = 4
    n_per_element = 10
    
    element_groups = [NeuronGroup(n_per_element, eqs, threshold='v>1', reset='v=0')
                     for _ in range(n_elements)]
    
    # Duration encoders (subpopulations)
    n_subpops = 50
    duration_groups = [NeuronGroup(5, eqs) for _ in range(n_subpops)]
    
    # Oscillatory background
    freq = 20  # Hz (beta oscillation)
    I_bg = 'sin(2*pi*freq*t)'
    
    # Monitor spikes
    monitors = [SpikeMonitor(g) for g in element_groups]
    
    # Run simulation
    run(1000*ms)
    
    return monitors

# Analyze timing patterns
def analyze_timing(monitors):
    for i, mon in enumerate(monitors):
        spike_times = mon.t[:]
        print(f"Element {i}: spikes at {spike_times}")
```

## Key References

- **Primary**: Lober et al. (2026). "Learning sequence timing and control of replay speed in networks of spiking neurons." arXiv:2605.22523
- Original sTM: Tetzlaff et al. (prior work)
- Sequence replay in hippocampus: Foster & Wilson (2006), Csicsvari et al.
- Oscillations and replay: Buzsáki (2015)
- Spiking networks: Diesmann et al. (1999), Brunel (2000)
- Timing in motor sequences: Hinton et al., Tanji et al.

## Activation Keywords

spiking temporal memory, sequence timing, replay speed control, oscillatory clock, duration encoding, biological sequence processing, motor sequence learning, sensory sequence replay, sTM model, spiking neural network timing, EEG oscillation replay, LFP replay speed, sparse spatiotemporal patterns, sequence replay modulation, wakefulness sleep replay