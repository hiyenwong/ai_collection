---
name: spiking-bandpass-wavelet-encoding
description: >
  Spiking Bandpass Wavelet encoding methodology for temporal signal representation.
  Recasts spike encoders as time-causal wavelet frames with quantitative bandwidths and resolution guarantees.
  Connects neuromorphic spike encoding with classical signal processing via bandpass wavelet decomposition.
  Use when: spike encoding, temporal signal encoding, wavelet-based spiking, neuromorphic encoding,
  event-based temporal representation, bandpass filtering with spikes, signal processing for SNNs,
  time-causal encoding, spike-based signal decomposition.
---

# Spiking Bandpass Wavelet Encoding

## Source
- **Paper**: Encoding and Decoding Temporal Signals with Spiking Bandpass Wavelets (2026)
- **arXiv**: 2605.09770v1
- **Authors**: Jens Egholm Pedersen, Tony Lindeberg, Peter Gerstoft
- **Categories**: cs.NE, eess.SP, q-bio.NC

## Core Concept

Spike-based temporal encoders, traditionally formulated probabilistically, are mathematically equivalent to
**time-causal bandpass wavelet frames**. This provides quantitative bandwidth analysis and resolution guarantees
for spiking temporal encoders, bridging neuromorphic computing with classical signal processing.

## Key Contributions

### 1. Wavelet Frame Interpretation
- A spike encoder with kernel ψ generates events when the filtered signal exceeds threshold
- Convolution of input signal with kernel → wavelet coefficient
- Threshold crossing → coefficient quantization to spike/no-spike
- Kernel properties determine time-frequency resolution

### 2. Bandpass Properties
- **Center frequency**: Determined by kernel scale parameter
- **Bandwidth**: Inversely proportional to kernel duration
- **Q-factor**: Tunable through kernel design
- **Time-frequency trade-off**: Governed by uncertainty principle

### 3. Time-Causal Guarantee
Unlike standard wavelets, encoding uses **time-causal** kernels — only past signal values
influence current encoding decisions, enabling real-time event generation without look-ahead.

### 4. Reconstruction Bounds
- Sampling density bounds from wavelet frame theory
- Error bounds based on kernel properties and threshold
- Multi-scale decomposition enables signal recovery

## Implementation

### Single-Band Spike Encoder
```python
import numpy as np

def bandpass_spike_encode(signal, kernel, threshold, dt=0.001, refractory_ms=5):
    filtered = np.convolve(signal, kernel, mode='same')
    spikes = np.zeros_like(signal)
    refractory = int(refractory_ms / dt)
    for i, val in enumerate(filtered):
        if refractory > 0:
            refractory -= 1
            continue
        if val > threshold:
            spikes[i] = 1.0
            refractory = int(refractory_ms / dt)
    return spikes
```

### Multi-Scale Spike Decomposition
```python
def multiscale_spike_encode(signal, kernels, thresholds):
    return [bandpass_spike_encode(signal, k, t)
            for k, t in zip(kernels, thresholds)]
```

## Applications
- **Event-based vision**: DVS temporal encoding with frequency guarantees
- **Audio processing**: Spike-based cochlear models with defined frequency channels
- **Control systems**: Event-triggered control with bandwidth analysis
- **Neuromorphic sensing**: Sensor design with quantified temporal resolution

## Connections to Existing Skills
- `spiking-neural-network-analysis`: SNN input encoding
- `snn-performance-analysis`: Event-based processing
- `neural-dynamics-universal-translator`: Signal representation

## Pitfalls
- **Threshold sensitivity**: Reconstruction quality degrades near critical threshold
- **Aliasing**: Time-causal constraint limits frequency resolution
- **Multi-band interference**: Overlapping wavelet bands cause spike correlations
- **Non-stationary signals**: Wavelet assumptions break for rapidly changing statistics
