---
name: spiking-bandpass-wavelet-encoding
description: Spiking Bandpass Wavelet encoding methodology for temporal signal processing using spike-based representations. Recasts spike encoders as time-causal wavelet frames with quantitative bandwidths and reconstruction error bounds. Preserves sparsity and locality of spiking representations, with direct mapping to neuromorphic hardware. Use when: spike-based signal encoding, neuromorphic signal processing, spiking wavelet transforms, temporal signal encoding/decoding, energy-efficient spike encoding, ECG/audio spike representation, time-causal wavelet frames. arXiv: 2605.09770 (Pedersen, Lindeberg, Gerstoft, 2026).
---

# Spiking Bandpass Wavelet Encoding

Methodology from "Encoding and Decoding Temporal Signals with Spiking Bandpass Wavelets" (arXiv:2605.09770).

## Core Problem

Spike-based encodings are sparse and energy-efficient, but historically formulated probabilistically, disconnected from signal processing literature. This methodology bridges the gap by recasting spike encoders as time-causal wavelet frames.

## Key Concepts

### Spike Encoder as Wavelet Frame

1. **Spike generation**: Input signal s(t) → threshold-crossing events at times {t_i}
2. **Wavelet basis**: Each spike defines a bandpass wavelet ψ_i(t) centered at t_i
3. **Time-causal**: Wavelets depend only on past data, suitable for real-time streaming
4. **Quantitative bandwidths**: Each wavelet has measurable frequency support
5. **Reconstruction bounds**: Error bounded by spike quantization + time discretization

### Mathematical Formulation

```
s(t) ≈ Σ_i w_i · ψ_i(t - t_i)
```

where:
- {t_i} are spike times (threshold crossings)
- w_i are spike weights (amplitudes)
- ψ_i are bandpass wavelet kernels

### Advantages over Traditional Approaches

| Aspect | Probabilistic SNN | Spiking Wavelets |
|--------|------------------|------------------|
| Theory | Point processes | Wavelet frames |
| Bandwidth | Qualitative | Quantitative bounds |
| Reconstruction | Approximate | Bounded error |
| Signal proc. | Disconnected | Direct mapping |
| Hardware | Neuromorphic | Neuromorphic |

## Implementation Guide

### Step 1: Define Wavelet Kernels

```python
import numpy as np

def bandpass_wavelet(t, center, bandwidth, q_factor=5):
    """Time-causal bandpass wavelet kernel."""
    tau = t - center
    # Use causal window (only past)
    causal_mask = tau <= 0
    # Bandpass envelope
    freq = 2 * np.pi * bandwidth
    wavelet = np.exp(tau * bandwidth / q_factor) * np.cos(freq * tau) * causal_mask
    return wavelet
```

### Step 2: Spike Encoding

```python
def spike_encode(signal, dt, threshold=0.1, bandwidth=50):
    """Encode signal as spike times with wavelet parameters."""
    spikes = []
    for i, val in enumerate(signal):
        if abs(val) > threshold:
            t = i * dt
            spikes.append({
                'time': t,
                'weight': val,
                'bandwidth': bandwidth
            })
    return spikes
```

### Step 3: Signal Reconstruction

```python
def spike_decode(spikes, t_axis, q_factor=5):
    """Reconstruct signal from spike train using wavelets."""
    reconstructed = np.zeros_like(t_axis)
    for spike in spikes:
        wavelet = bandpass_wavelet(t_axis, spike['time'],
                                   spike['bandwidth'], q_factor)
        reconstructed += spike['weight'] * wavelet
    return reconstructed
```

### Step 4: Evaluate Reconstruction Quality

```python
def normalized_rmse(original, reconstructed):
    """Compute normalized RMSE for reconstruction quality."""
    error = np.sqrt(np.mean((original - reconstructed)**2))
    norm = np.sqrt(np.mean(original**2))
    return error / norm
```

## Applications

### Biomedical Signals
- ECG/EEG spike encoding for low-power monitoring
- Compressed representation of physiological time series

### Audio Processing
- Event-based audio encoding for neuromorphic chips
- Sparse audio feature extraction

### Edge Computing
- Low-bandwidth sensor data transmission
- Energy-efficient temporal feature extraction

## Key Parameters

| Parameter | Description | Typical Range |
|-----------|-------------|---------------|
| threshold | Spike trigger threshold | 0.05-0.5 (normalized) |
| bandwidth | Wavelet frequency band | 10-500 Hz |
| q_factor | Quality factor (bandwidth sharpness) | 3-10 |
| dt | Time discretization | 0.001-0.01 s |

## Performance Notes

- Reconstruction RMSE comparable to continuous wavelet transforms
- Spike count scales inversely with threshold
- Direct mapping to neuromorphic hardware (Loihi, SpiNNaker)
- Time-causal: suitable for real-time streaming applications

## References

- Pedersen, J.E., Lindeberg, T., Gerstoft, P. (2026). "Encoding and Decoding Temporal Signals with Spiking Bandpass Wavelets." arXiv:2605.09770
- Lindeberg, T. Time-causal scale-space representations
- Gerstoft, P. Array processing and signal reconstruction
