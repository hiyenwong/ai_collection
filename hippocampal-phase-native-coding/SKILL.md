---
name: hippocampal-phase-native-coding
description: "Unified phase-native computational principle governing hippocampal spike timing and neural coding. Explains how phase precession, sequence coding, and spatial representation emerge from a common mechanism. Activation: hippocampal coding, phase precession, theta oscillation, sequence coding, spatial representation, temporal coding."
---

# Hippocampal Phase-Native Computational Principle

A unified phase-native computational principle that governs both spike timing and neural coding in the hippocampus. This framework reveals how phase precession, sequence coding, and spatial representation emerge from a common underlying mechanism.

## Background

Hippocampal neurons encode information through precise spike timing relative to ongoing theta oscillations (~8 Hz). Key phenomena include:

- **Phase precession**: Spikes occur at progressively earlier phases as animal traverses place field
- **Sequence coding**: Sequential activation of neurons representing spatial paths
- **Spatial representation**: Place cells fire at specific locations

## Core Principle

The **Phase-Native Computational Principle** states that hippocampal neurons encode information through:

1. **Oscillatory phase** as a temporal reference frame
2. **Spike timing** relative to this reference carries information
3. **Phase precession** emerges naturally from this coding scheme

## Mathematical Framework

### Theta Phase Reference

```python
import numpy as np

class ThetaOscillator:
    """
    Theta oscillation as reference frame.
    
    Frequency: 6-10 Hz (typically 8 Hz)
    """
    
    def __init__(self, frequency=8.0, phase_offset=0.0):
        self.frequency = frequency  # Hz
        self.phase_offset = phase_offset
        self.omega = 2 * np.pi * frequency  # rad/s
    
    def phase(self, t):
        """Theta phase at time t (in radians, 0 to 2π)."""
        return (self.omega * t + self.phase_offset) % (2 * np.pi)
    
    def amplitude(self, t):
        """Theta amplitude (can be modulated)."""
        return 1.0  # Constant amplitude for simplicity
    
    def oscillation(self, t):
        """Full oscillation value."""
        return self.amplitude(t) * np.cos(self.phase(t))


# Example usage
theta = ThetaOscillator(frequency=8.0)
times = np.linspace(0, 1, 1000)  # 1 second
phases = [theta.phase(t) for t in times]
```

### Phase-Native Spike Coding

```python
class PhaseNativeCoding:
    """
    Spike timing relative to theta phase encodes information.
    """
    
    def __init__(self, theta_oscillator, preferred_phase=np.pi):
        """
        Args:
            theta_oscillator: Reference oscillation
            preferred_phase: Preferred spike phase (default: π = 180°)
        """
        self.theta = theta_oscillator
        self.preferred_phase = preferred_phase
    
    def spike_probability(self, t, stimulus_intensity, phase_precession_rate=0):
        """
        Probability of spiking at time t.
        
        Args:
            t: Time
            stimulus_intensity: Strength of stimulus (0 to 1)
            phase_precession_rate: Rate of phase precession (rad/s)
        """
        current_phase = self.theta.phase(t)
        
        # Adjust preferred phase for precession
        adjusted_preferred = (
            self.preferred_phase + phase_precession_rate * t
        ) % (2 * np.pi)
        
        # Von Mises distribution (circular Gaussian)
        kappa = 10  # Concentration parameter
        phase_diff = current_phase - adjusted_preferred
        phase_likelihood = np.exp(kappa * np.cos(phase_diff))
        
        # Overall spike probability
        p_spike = stimulus_intensity * phase_likelihood / np.exp(kappa)
        
        return min(p_spike, 1.0)
    
    def generate_spikes(self, times, stimulus_trajectory, phase_precession=True):
        """
        Generate spike train for stimulus trajectory.
        
        Args:
            times: Array of time points
            stimulus_trajectory: Stimulus intensity over time
            phase_precession: Enable phase precession
        """
        spikes = []
        
        if phase_precession:
            # Phase precession: earlier phases as stimulus progresses
            precession_rate = 2 * np.pi * 0.5  # Half cycle precession
        else:
            precession_rate = 0
        
        for i, t in enumerate(times):
            p = self.spike_probability(
                t, 
                stimulus_trajectory[i],
                precession_rate * (i / len(times))  # Progressive precession
            )
            
            if np.random.random() < p:
                spikes.append(t)
        
        return np.array(spikes)
```

## Phase Precession Mechanism

### 1. Progressive Phase Shift

```python
class PhasePrecession:
    """
    Phase precession: spikes occur at progressively earlier phases.
    
    As animal moves through place field, spikes advance in phase.
    """
    
    def __init__(self, place_field_center, place_field_width):
        self.center = place_field_center
        self.width = place_field_width
    
    def spike_phase(self, position):
        """
        Determine spike phase based on position in place field.
        
        Returns phase from 2π (entry) to 0 (exit) - precession.
        """
        # Distance through place field (0 to 1)
        relative_pos = (position - (self.center - self.width/2)) / self.width
        relative_pos = np.clip(relative_pos, 0, 1)
        
        # Phase precession: 2π → 0 as position goes 0 → 1
        phase = 2 * np.pi * (1 - relative_pos)
        
        return phase
    
    def plot_precession(self, positions, spike_times, theta):
        """
        Visualize phase precession.
        
        X-axis: Position
        Y-axis: Theta phase at spike time
        """
        spike_phases = []
        for spike_t in spike_times:
            spike_phases.append(theta.phase(spike_t))
        
        # Plot should show diagonal from top-left to bottom-right
        return positions, spike_phases
```

### 2. Sequence Coding

```python
class SequenceCoding:
    """
    Sequential activation of neurons represents spatial paths.
    
    Phase coding enables compression of temporal sequences.
    """
    
    def __init__(self, n_neurons, sequence_length):
        self.n_neurons = n_neurons
        self.sequence_length = sequence_length
        
        # Each neuron codes for position in sequence
        self.place_fields = np.linspace(0, sequence_length, n_neurons)
    
    def encode_trajectory(self, trajectory, theta):
        """
        Encode spatial trajectory as phase-coded spike sequence.
        
        Theta cycle compression: entire trajectory fits in one cycle.
        """
        spikes = {i: [] for i in range(self.n_neurons)}
        
        for t, position in enumerate(trajectory):
            # Find active neuron
            active_neuron = np.argmin(np.abs(self.place_fields - position))
            
            # Determine spike phase based on position in field
            phase_coding = PhasePrecession(
                self.place_fields[active_neuron],
                sequence_length / self.n_neurons
            )
            
            spike_phase = phase_coding.spike_phase(position)
            
            # Convert phase to time within theta cycle
            theta_period = 1 / theta.frequency
            spike_time_within_cycle = spike_phase / (2 * np.pi) * theta_period
            
            spikes[active_neuron].append(
                t * theta_period + spike_time_within_cycle
            )
        
        return spikes
    
    def decode_sequence(self, spikes, theta):
        """
        Decode spike sequence back to trajectory.
        
        Use phase information to reconstruct spatial order.
        """
        trajectory = []
        
        # Collect all spikes with phases
        all_spikes = []
        for neuron_id, spike_times in spikes.items():
            for t in spike_times:
                phase = theta.phase(t)
                all_spikes.append((t, phase, neuron_id))
        
        # Sort by phase (earlier phase = later in trajectory)
        all_spikes.sort(key=lambda x: -x[1])  # Reverse phase order
        
        # Reconstruct trajectory
        for t, phase, neuron_id in all_spikes:
            position = self.place_fields[neuron_id]
            trajectory.append(position)
        
        return np.array(trajectory)
```

## Unified Computational Principle

### Phase as Information Carrier

```python
class UnifiedPhasePrinciple:
    """
    Unified framework: phase carries all information.
    
    1. Spatial information → preferred phase
    2. Temporal information → spike timing within phase
    3. Sequence information → phase relationships
    """
    
    def __init__(self, theta_frequency=8.0):
        self.theta = ThetaOscillator(theta_frequency)
    
    def encode(self, stimulus_features):
        """
        Encode features using phase-native coding.
        
        Multiple features multiplexed in phase space:
        - Spatial position: preferred phase
        - Velocity: phase modulation rate
        - Context: phase offset
        """
        encoding = {}
        
        # Spatial feature → preferred phase
        position = stimulus_features.get('position', 0)
        encoding['preferred_phase'] = self.position_to_phase(position)
        
        # Velocity → phase precession rate
        velocity = stimulus_features.get('velocity', 0)
        encoding['precession_rate'] = velocity * 0.1
        
        # Context → theta frequency modulation
        context = stimulus_features.get('context', 'default')
        encoding['theta_freq'] = self.context_to_frequency(context)
        
        return encoding
    
    def decode(self, spike_train):
        """
        Decode spike train to stimulus features.
        """
        features = {}
        
        # Extract phases from spike times
        phases = [self.theta.phase(t) for t in spike_train]
        
        # Mean phase → position
        mean_phase = np.mean(phases)
        features['position'] = self.phase_to_position(mean_phase)
        
        # Phase variance → velocity (precession strength)
        phase_variance = np.var(phases)
        features['velocity'] = phase_variance * 10
        
        # Theta frequency → context
        features['context'] = self.frequency_to_context(self.theta.frequency)
        
        return features
    
    def position_to_phase(self, position):
        """Map position to preferred phase."""
        return (position * 2 * np.pi / 100) % (2 * np.pi)
    
    def phase_to_position(self, phase):
        """Map phase back to position."""
        return (phase * 100 / (2 * np.pi)) % 100
    
    def context_to_frequency(self, context):
        """Context modulates theta frequency."""
        base_freq = 8.0
        context_mod = {'default': 0, 'familiar': 0.5, 'novel': -0.5}
        return base_freq + context_mod.get(context, 0)
    
    def frequency_to_context(self, freq):
        """Infer context from theta frequency."""
        if freq > 8.2:
            return 'familiar'
        elif freq < 7.8:
            return 'novel'
        return 'default'
```

## Biological Implementation

### Single Neuron Model

```python
class PhaseCodingNeuron:
    """
    Biophysically plausible phase-coding neuron.
    """
    
    def __init__(self, preferred_phase, theta_oscillator):
        self.preferred_phase = preferred_phase
        self.theta = theta_oscillator
        
        # Membrane properties
        self.v_rest = -70
        self.v_thresh = -50
        self.tau_m = 20  # ms
        
        # Phase selectivity
        self.phase_selectivity = 10  # kappa in von Mises
    
    def theta_modulated_input(self, t, base_input):
        """
        Theta oscillation modulates input.
        
        Creates windows of excitability at preferred phase.
        """
        current_phase = self.theta.phase(t)
        
        # Phase preference (von Mises)
        phase_factor = np.exp(
            self.phase_selectivity * 
            np.cos(current_phase - self.preferred_phase)
        )
        
        # Modulated input
        return base_input * phase_factor / np.exp(self.phase_selectivity)
    
    def step(self, dt, t, external_input):
        """Single timestep with phase-modulated dynamics."""
        # Theta-modulated input
        I_theta = self.theta_modulated_input(t, external_input)
        
        # Integrate and fire
        dv = (-self.v + self.v_rest + I_theta) / self.tau_m * dt
        self.v += dv
        
        # Check spike
        spike = self.v >= self.v_thresh
        if spike:
            self.v = self.v_rest
        
        return spike
```

## Applications

### 1. Memory Compression

```python
def compress_memory(trajectory, theta):
    """
    Compress temporal sequence into single theta cycle.
    
    Phase coding allows N positions to be represented 
    within one theta cycle (~125 ms).
    """
    sequence_coder = SequenceCoding(n_neurons=50, sequence_length=len(trajectory))
    
    # Encode
    spikes = sequence_coder.encode_trajectory(trajectory, theta)
    
    # Entire trajectory compressed into ~125 ms
    return spikes
```

### 2. Path Planning

```python
class PathPlanning:
    """
    Use phase-coded sequences for path planning.
    """
    
    def __init__(self, place_cells):
        self.place_cells = place_cells
    
    def plan_path(self, start, goal, obstacles):
        """
        Generate sequence of place cell activations for path.
        """
        # Compute optimal path
        path = self.compute_path(start, goal, obstacles)
        
        # Convert to phase-coded sequence
        theta = ThetaOscillator(8.0)
        sequence = []
        
        for position in path:
            # Find place cell for this position
            cell_idx = self.find_place_cell(position)
            
            # Phase based on progress
            phase = 2 * np.pi * (1 - position / len(path))
            
            sequence.append({
                'cell': cell_idx,
                'phase': phase,
                'time': phase / (2 * np.pi * theta.frequency),
            })
        
        return sequence
```

## Predictions and Experiments

### Testable Predictions

1. **Phase coding extends beyond place cells**: Other hippocampal neurons should show phase coding
2. **Context modulates theta frequency**: Different environments → different theta frequencies
3. **Phase precession is general**: Should occur in non-spatial memory tasks

### Experimental Design

```python
def design_phase_coding_experiment():
    """
    Design experiment to test phase-native principle.
    """
    experiment = {
        'recording': {
            'target': 'CA1 pyramidal neurons',
            'duration': '30 min',
            'sampling_rate': 30000,  # Hz for spikes
        },
        'task': {
            'type': 'spatial_navigation',
            'environment': 'linear_track',
            'length': '2 meters',
        },
        'analysis': {
            'phase_precession': {
                'method': 'circular_linear_regression',
                'expected': 'negative_slope',
            },
            'sequence_coding': {
                'method': 'bayesian_decoding',
                'expected': 'position_correlation > 0.8',
            },
            'theta_modulation': {
                'method': 'rayleigh_test',
                'expected': 'p < 0.001',
            },
        },
    }
    return experiment
```

## References

- Unified Phase-Native Computational Principle Governs Hippocampal Spike Timing and Neural Coding. arXiv:2603.19690
- O'Keefe & Recce (1993). Phase relationship between hippocampal place units and the EEG theta rhythm
- Skaggs et al. (1996). Theta phase precession in hippocampal neuronal populations

## Activation Keywords

- hippocampal phase coding
- phase precession
- theta oscillation
- sequence coding
- spatial representation
- temporal coding
- place cells
- neural oscillations
