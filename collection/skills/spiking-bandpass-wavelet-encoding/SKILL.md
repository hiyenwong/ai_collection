---
name: spiking-bandpass-wavelet-encoding
description: "Recasting spike encoders as time-causal wavelet frames with quantitative bandwidths and reconstruction error bounds. Bridges spiking neural representations with classical signal processing. Demonstrates reconstruction on ECG/audio datasets with normalized RMSE comparable to continuous wavelet transforms. Maps directly to neuromorphic hardware. Activation: spiking wavelet, bandpass wavelet, temporal signal encoding, spike-based signal processing, neuromorphic encoding, wavelet frame reconstruction."
---

# Spiking Bandpass Wavelet Encoding

> Recasts spike encoders as time-causal wavelet frames with quantitative bandwidths and reconstruction error bounds, bridging spiking neural representations with classical signal processing theory.

## Metadata
- **Source**: arXiv:2605.09770
- **Authors**: Jens Egholm Pedersen, Tony Lindeberg, Peter Gerstoft
- **Published**: 2026-05-10
- **Subjects**: Neural and Evolutionary Computing (cs.NE); Signal Processing (eess.SP); Neurons and Cognition (q-bio.NC)

## Core Methodology

### Key Innovation
Spike-based encodings are sparse and energy-efficient but have historically been formulated probabilistically, disconnected from mainstream signal processing literature. This paper **recasts spike encoders as time-causal wavelet frames** with quantitative bandwidths and reconstruction error bounds. The proposed spiking wavelets preserve the sparsity and locality of spiking representations, with reconstruction up to spike quantization and time discretization.

### Technical Framework

1. **Wavelet Frame Formulation**: Spike encoders are mapped to time-causal wavelet frames, providing rigorous signal processing foundations for spike-based representations
2. **Bandwidth Quantification**: Quantitative bandwidth analysis of spiking wavelet representations
3. **Reconstruction Error Bounds**: Theoretical bounds on reconstruction error, accounting for spike quantization and time discretization
4. **Signal Processing Bridge**: Connects probabilistic spiking encodings with classical wavelet transform theory

### Validation
- **ECG dataset**: Reconstruction with normalized RMSE comparable to continuous wavelet transforms
- **Audio dataset**: Similar performance, demonstrating generality across signal types
- **Hardware Mapping**: The spiking wavelets map directly to neuromorphic hardware implementations

## Implementation Guide

### Prerequisites
- Spiking Neural Network framework (e.g., SpikingJelly, Norse)
- Signal processing library (e.g., PyWavelets)
- Time-series datasets (ECG, audio)

### Step-by-Step
1. Define spike encoder as a time-causal wavelet frame with specific bandwidth properties
2. Map input signal through the wavelet frame to generate spike trains
3. Reconstruct signal from spike trains using wavelet frame inversion
4. Validate reconstruction quality via normalized RMSE against ground truth
5. Compare with continuous wavelet transform baseline
6. Map to neuromorphic hardware ( Loihi, SpiNNaker, custom FPGA)

### Code Example
```python
import numpy as np

# Simplified spiking bandpass wavelet encoder
def spiking_wavelet_encode(signal, dt=1e-3, threshold=0.5):
    """Encode signal as spikes using time-causal wavelet frame."""
    # Define wavelet frame filters (bandpass characteristics)
    scales = np.logspace(0, 2, 8)  # Multiple frequency bands
    spike_trains = []
    
    for scale in scales:
        # Create bandpass wavelet kernel
        t = np.arange(len(signal)) * dt
        wavelet = np.exp(-t/scale) * np.sin(2*np.pi*t/(2*scale))
        wavelet = wavelet[:len(signal)]
        
        # Convolve with signal
        response = np.convolve(signal, wavelet, mode='same')
        
        # Generate spikes at threshold crossings
        spikes = np.zeros_like(signal)
        membrane = np.zeros(len(signal))
        for i in range(1, len(signal)):
            membrane[i] = membrane[i-1] * 0.9 + response[i]
            if membrane[i] > threshold:
                spikes[i] = 1
                membrane[i] = 0  # reset
        
        spike_trains.append(spikes)
    
    return np.array(spike_trains)

def spiking_wavelet_decode(spike_trains, dt=1e-3):
    """Reconstruct signal from spike trains via wavelet frame inversion."""
    scales = np.logspace(0, 2, len(spike_trains))
    reconstructed = np.zeros(len(spike_trains[0]))
    
    for i, (spikes, scale) in enumerate(zip(spike_trains, scales)):
        t = np.arange(len(spikes)) * dt
        wavelet = np.exp(-t/scale) * np.sin(2*np.pi*t/(2*scale))
        wavelet = wavelet[:len(spikes)]
        # Reconstruct from spikes
        reconstructed += np.convolve(spikes, wavelet, mode='same')
    
    return reconstructed

# Example usage
signal = np.sin(2*np.pi*10*np.arange(1000)*1e-3)  # 10 Hz sine
spikes = spiking_wavelet_encode(signal)
reconstructed = spiking_wavelet_decode(spikes)
rmse = np.sqrt(np.mean((signal - reconstructed)**2))
print(f"Normalized RMSE: {rmse:.4f}")
```

## Applications
- **Neuromorphic signal processing**: ECG, EEG, audio encoding for edge devices
- **Spike-based communication**: Time-causal encoding for event-based sensors
- **Energy-efficient edge AI**: Sparse spike representations with guaranteed reconstruction bounds
- **Brain-machine interfaces**: Interpretable spike encodings with signal processing guarantees

## Pitfalls
- **Time-causal constraint**: Wavelets must be causal (no future information), limiting reconstruction quality vs. non-causal transforms
- **Spike quantization error**: Binary spikes lose amplitude information; reconstruction is approximate
- **Hardware mapping**: Direct neuromorphic hardware mapping requires careful consideration of neuron model compatibility
- **Not a replacement for SNN training**: This is an encoding method, not a training methodology

## Related Skills
- vs-wno-variable-spiking-wavelet (wavelet neural operators + deployment cost)
- spiking-quantum-encoding (SPATE temporal encoding for QML)
- direct-to-event-snn-transfer
- event2vec-neuromorphic-representation
- snn-near-sensor-noise-filter-dvs
