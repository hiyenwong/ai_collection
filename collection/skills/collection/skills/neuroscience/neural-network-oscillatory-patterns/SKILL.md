---
name: neural-network-oscillatory-patterns
description: "Analysis of emergent oscillatory patterns in recurrent neural networks and their relationship to brain rhythms. Studies how network architecture and connectivity give rise to specific frequency bands (theta, alpha, beta, gamma) and phase synchronization. Based on arXiv:2604.14091 (2026). Triggers: oscillatory patterns, brain rhythms, neural oscillations, frequency bands, phase synchronization, recurrent network dynamics, 振荡模式, 脑节律."
version: 1.0.0
metadata:
  hermes:
    source_paper: "Emergent Oscillatory Patterns in Recurrent Networks (arXiv:2604.14091)"
    tags:
      - neuroscience
      - oscillations
      - recurrent-networks
      - brain-rhythms
      - phase-synchronization
---

# Neural Network Oscillatory Patterns

## Overview

Studies how recurrent neural network architecture and connectivity patterns give rise to emergent oscillatory dynamics that mirror brain rhythms across frequency bands (theta, alpha, beta, gamma).

## Key Insights

- **Network topology** determines oscillation frequency: sparse connectivity favors higher frequencies
- **Excitation-inhibition balance** controls oscillation amplitude and stability
- **Phase synchronization** emerges naturally in networks with modular structure
- **Cross-frequency coupling** (phase-amplitude, phase-phase) arises from hierarchical network organization

## Core Methodology

### Oscillation Detection and Analysis

```python
import numpy as np
from scipy.signal import welch, hilbert, butter, filtfilt

def compute_power_spectrum(signal, fs, band=(8, 12)):
    """Compute power in a specific frequency band."""
    f, Pxx = welch(signal, fs=fs, nperseg=256)
    mask = (f >= band[0]) & (f <= band[1])
    return np.trapz(Pxx[mask], f[mask])

def extract_phase(signal, band):
    """Extract instantaneous phase using Hilbert transform."""
    b, a = butter(4, band, btype='bandpass', fs=256)
    filtered = filtfilt(b, a, signal)
    analytic = hilbert(filtered)
    return np.angle(analytic)

def phase_locking_value(phase1, phase2):
    """Compute phase synchronization between two signals."""
    plv = np.abs(np.mean(np.exp(1j * (phase1 - phase2))))
    return plv

def cross_frequency_coupling(phase_signal, amplitude_signal, phase_band, amp_band):
    """Compute phase-amplitude coupling (PAC)."""
    phase = extract_phase(phase_signal, phase_band)
    amp = np.abs(hilbert(extract_phase(amplitude_signal, amp_band)))
    # Modulation index
    mi = compute_modulation_index(phase, amp)
    return mi
```

### Network-Oscillation Mapping

```python
def predict_oscillation_from_connectivity(W, E, I):
    """
    Predict dominant oscillation frequency from network properties.
    
    Args:
        W: connectivity matrix
        E: excitation strength
        I: inhibition strength
    
    Returns:
        predicted_frequency: dominant oscillation frequency (Hz)
    """
    sparsity = np.count_nonzero(W) / W.size
    ei_ratio = E / I
    
    # Empirical mapping from network properties to frequency
    if sparsity < 0.1:
        return 30 + 10 * ei_ratio  # Gamma
    elif sparsity < 0.3:
        return 12 + 8 * ei_ratio   # Beta
    else:
        return 4 + 4 * ei_ratio    # Theta/Alpha
```

## Applications

- Brain-computer interface decoding using oscillatory features
- Neural mass model calibration
- Understanding pathological oscillations (Parkinson's tremor, epilepsy)
- Designing neuromorphic oscillatory computing systems

## Activation Keywords

- oscillatory patterns, brain rhythms, neural oscillations
- phase synchronization, cross-frequency coupling, E-I balance
- 振荡模式, 脑节律, 相位同步

## References

- arXiv:2604.14091 (2026)
- Related skills: kuramoto-brain-network, spiking-oscillation-mapping