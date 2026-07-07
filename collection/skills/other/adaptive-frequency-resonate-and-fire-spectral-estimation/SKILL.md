---
name: adaptive-frequency-resonate-and-fire-spectral-estimation
description: Adaptive-Frequency Resonate-and-Fire (ARF) neurons for spectral estimation of streaming signals. Neuromorphic-inspired method that dynamically adjusts internal frequency to match dominant frequency components, enabling real-time range/velocity estimation in FMCW radar and neural signal processing.
trigger_words:
  - resonate-and-fire
  - spectral estimation
  - adaptive frequency
  - neuromorphic signal processing
  - FMCW radar
  - streaming signals
  - resonate neuron
  - frequency tracking
  - real-time processing
  - edge computing
---

# Adaptive-Frequency Resonate-and-Fire Neurons for Spectral Estimation

## Core Innovation

**Adaptive-Frequency Resonate-and-Fire (ARF) neurons** represent a breakthrough in neuromorphic signal processing, enabling **real-time spectral estimation** without storing large data buffers. This addresses a fundamental limitation of traditional FFT-based methods: the requirement to store and process entire signal blocks.

**Key breakthrough**: Sample-by-sample frequency estimation with **memory scaling proportional to number of targets**, not signal length.

## Theoretical Framework

### Resonate-and-Fire Neuron Dynamics

ARF neurons extend classical resonate-and-fire models with **adaptive frequency tuning**:

```mathematical
# Discrete-time ARF dynamics
θ_{n+1} = θ_n + ω_n Δt  (phase evolution)
ω_{n+1} = ω_n + η · (∂L/∂ω)  (frequency adaptation)
spike when: θ_n ≈ 2πk (resonance condition)
```

Where:
- $θ$ = internal phase state
- $ω$ = adaptive frequency parameter
- $η$ = learning rate for frequency adjustment
- $L$ = objective function matching signal frequency

### Frequency Adaptation Mechanism

Each neuron **dynamically adjusts its internal frequency** to match dominant frequency components:

```mathematical
∂L/∂ω = correlation(signal, cos(ωt)) · feedback_weight
```

This enables:
- Automatic frequency locking to input signal
- Multi-target tracking via multiple neurons
- Continuous frequency estimation without FFT

### Feedback Mechanism

For multi-target scenarios, introduces **feedback inhibition**:
- Neurons that lock to a frequency inhibit others
- Prevents multiple neurons tracking same frequency
- Enables distribution across frequency spectrum

## Implementation Architecture

### Core ARF Neuron Model

```python
class ARFNeuron:
    def __init__(self, initial_freq, learning_rate):
        self.phase = 0.0
        self.frequency = initial_freq
        self.learning_rate = learning_rate
        self.spiked = False
        
    def update(self, signal_sample, dt):
        # Phase evolution
        self.phase += self.frequency * dt
        self.phase = self.phase % (2 * np.pi)
        
        # Frequency adaptation
        correlation = signal_sample * np.cos(self.phase)
        self.frequency += self.learning_rate * correlation
        
        # Spike generation
        if self.phase < 0.1:  # Near resonance
            self.spiked = True
            return self.frequency  # Estimated frequency
        else:
            self.spiked = False
            return None
```

### Multi-Neuron Network

```python
class ARFNetwork:
    def __init__(self, num_neurons, freq_range, learning_rate):
        # Initialize neurons across frequency range
        frequencies = np.linspace(freq_range[0], freq_range[1], num_neurons)
        self.neurons = [ARFNeuron(f, learning_rate) for f in frequencies]
        self.feedback_weights = np.ones(num_neurons)
        
    def process(self, signal_stream):
        estimated_freqs = []
        
        for sample in signal_stream:
            # Update all neurons
            freq_estimates = []
            for neuron in self.neurons:
                freq = neuron.update(sample, dt=1.0)
                if freq:
                    freq_estimates.append(freq)
            
            # Feedback inhibition
            for i, neuron in enumerate(self.neurons):
                if neuron.spiked:
                    # Inhibit other neurons
                    for j, other in enumerate(self.neurons):
                        if j != i:
                            other.frequency -= feedback_factor
            
            estimated_freqs.extend(freq_estimates)
        
        return estimated_freqs
```

## FMCW Radar Application

### Range and Velocity Estimation

In FMCW radar, frequency components encode **target range and velocity**:

```mathematical
beat_frequency = (2 · v · f_c) / c  (velocity)
range_frequency = (2 · R · B) / (c · T)  (range)
```

ARF neurons directly estimate these beat frequencies:
- Each neuron locks to a beat frequency component
- Real-time range/velocity extraction
- No FFT computation required

### Advantages Over FFT

| Metric | FFT-based | ARF neurons |
|--------|-----------|-------------|
| Memory | O(N) signal buffer | O(K) neurons |
| Latency | Block processing delay | Sample-by-sample |
| Edge deployment | Memory-intensive | Resource-efficient |
| Multi-target | Post-processing | Inherent distribution |

## Neuromorphic Implementation

### Hardware Realization

ARF neurons suitable for neuromorphic hardware:
- **Memristive circuits**: Phase accumulation
- **Analog oscillators**: Frequency adaptation
- **Digital FPGA**: Discrete-time implementation

### Edge Computing Benefits

```python
# Edge deployment characteristics
memory_per_target = sizeof(ARFNeuron)  # ~O(1) parameters
total_memory = num_targets * memory_per_target  # Independent of signal length
processing_per_sample = num_targets * neuron_updates  # Constant time per sample
```

### Power Efficiency

- No FFT computation (significant savings)
- Sample-by-sample processing (no buffering overhead)
- Adaptive computation (neurons only active when detecting)

## Experimental Validation

### Simulated Data Results
Successfully tracks multiple targets across:
- Single target scenarios
- Multi-target with distinct frequencies
- Overlapping frequency ranges

### Real Radar Data Performance
- **Range estimation accuracy**: Comparable to FFT
- **Velocity estimation**: Real-time tracking demonstrated
- **Multi-target separation**: Feedback mechanism validated

### Performance Metrics
- Frequency estimation error vs FFT
- Memory usage comparison
- Processing latency measurement
- Target tracking fidelity

## Neuroscience Applications

### EEG Frequency Tracking

ARF neurons can track EEG frequency bands:
- Alpha (8-12 Hz), Beta (13-30 Hz), Gamma (30-100 Hz)
- Real-time band power estimation
- Event-related desynchronization detection

### Neural Signal Processing

```python
# EEG frequency tracking example
eeg_arf = ARFNetwork(
    num_neurons=10,
    freq_range=(1, 100),  # EEG frequency range
    learning_rate=0.001
)

# Track dominant frequencies in real-time
dominant_freqs = eeg_arf.process(eeg_stream)
```

### Spike Train Analysis

For neural spike trains:
- Estimate oscillatory components
- Track bursting frequencies
- Detect rhythmic patterns

## Key Algorithmic Innovations

### 1. Sample-by-Sample Processing
```mathematical
ω_estimated = lim_{n→∞} ω_n (convergence to true frequency)
```

### 2. Feedback Inhibition
```mathematical
∂ω_i/∂t = -γ · Σ_{j≠i} spike_j · (ω_i - ω_j)
```
Prevents frequency collapse to single component.

### 3. Frequency Range Initialization
Distribute initial frequencies across expected range:
- Uniform spacing for unknown targets
- Prior distribution for known frequency bands
- Dynamic adjustment during tracking

## Pitfalls and Considerations

### Frequency Lock Time
- Neurons require convergence time
- Trade-off between learning rate and stability
- Fast adaptation may cause overshoot

### Multi-Target Interference
- Close frequencies may compete
- Feedback strength tuning critical
- Spatial distribution helps separation

### Noise Sensitivity
- High noise levels challenge frequency locking
- Signal-to-noise threshold considerations
- Robustness enhancement techniques needed

### Learning Rate Selection
- Too high: Instability, oscillations
- Too low: Slow convergence, missed targets
- Adaptive rates may improve performance

## Related Methodologies

### Comparison with FFT
- FFT: Block processing, full spectrum, high memory
- ARF: Streaming, targeted frequencies, low memory

### Comparison with IIR Filters
- IIR: Fixed bandpass, manual tuning
- ARF: Adaptive frequency, automatic tuning

### Comparison with Wavelet Transform
- Wavelet: Multi-scale, time-frequency
- ARF: Real-time, frequency-focused

## Implementation Guidelines

### Step-by-Step Setup

1. **Define Frequency Range**:
   - Expected target frequencies
   - Radar band or EEG bands
   - Neuron distribution across range

2. **Configure Neurons**:
   ```python
   network = ARFNetwork(
       num_neurons=expected_targets * 2,  # Oversample
       freq_range=(min_freq, max_freq),
       learning_rate=0.01  # Tune empirically
   )
   ```

3. **Set Feedback Parameters**:
   - Inhibition strength
   - Competition dynamics
   - Frequency separation threshold

4. **Process Streaming Data**:
   - Feed samples one-by-one
   - Collect frequency estimates
   - Track neuron state evolution

### Hyperparameter Tuning
- `learning_rate`: Speed vs stability
- `feedback_strength`: Multi-target separation
- `num_neurons`: Frequency resolution
- `phase_threshold`: Spike generation sensitivity

## Research Directions

### Open Questions
- Optimal neuron number vs frequency resolution
- Adaptive learning rate strategies
- Non-stationary frequency tracking

### Extensions
- Combined with other neuromorphic neurons
- Hierarchical frequency decomposition
- Multi-dimensional frequency tracking

## Citation

```bibtex
@article{chiavazza2026adaptive,
  title={Adaptive-Frequency Resonate-and-Fire Neurons for Spectral Estimation of Streaming Radar Signals},
  author={Chiavazza, Stefano and Yuan, Sen and Geilen, Marc and Fioranelli, Francesco and Corradi, Federico},
  journal={arXiv preprint arXiv:2606.13516},
  year={2026}
}
```

## Activation

Keywords: resonate-and-fire, spectral estimation, adaptive frequency, neuromorphic signal processing, FMCW radar, streaming signals, resonate neuron, frequency tracking, real-time processing, edge computing, sample-by-sample, target tracking, feedback inhibition, range velocity, memory efficiency, EEG frequency, neural signal, oscillator dynamics, phase evolution, frequency locking