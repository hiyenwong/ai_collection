---
name: spiking-oscillation-mapping
description: Spiking-phase adaptive temporal encoding (SPATE) for quantum machine learning - mapping oscillatory/spiking dynamics to quantum state preparation. Combines spiking neural dynamics with quantum feature encoding for time-series QML. Activation: spiking quantum machine learning, oscillation encoding, temporal quantum encoding, spike-phase mapping, quantum neural dynamics
---

# Spiking-Phase Adaptive Temporal Encoding for Quantum ML

## Overview
Based on paper: [SPATE: Spiking-Phase Adaptive Temporal Encoding for Quantum Machine Learning](https://arxiv.org/abs/2604.11022) (arXiv:2604.11022).

Most quantum machine learning (QML) pipelines rely on static encodings such as angle and amplitude maps. SPATE (Spiking-Phase Adaptive Temporal Encoding) maps oscillatory dynamics of spiking neural signals to quantum feature encoding, utilizing temporal dynamics properties to adaptively prepare quantum states through spike-phase information.

## Core Concepts

### Limitations of Static QML Encodings
- **Angle encoding**: maps values to rotation angles, ignores temporal information
- **Amplitude encoding**: requires normalization, loses absolute scale
- **Problem**: static encodings cannot capture oscillations, frequency, and phase relationships in time series

### Spiking-Phase Encoding
1. **Phase mapping**: map oscillatory phase from time series to quantum gate rotations
2. **Adaptive timing**: adjust encoding time windows based on signal frequency
3. **Spike-driven**: use spike events as triggers for quantum state preparation
4. **Information retention**: simultaneously preserves amplitude, frequency, and phase

### SPATE Architecture
```
Input Time Series -> Oscillation Detection -> Phase Extraction ->
Quantum Gate Mapping -> State Preparation -> QML Circuit
```

## Implementation

```python
import numpy as np
from scipy.signal import hilbert, find_peaks

class SpikingPhaseEncoder:
    def __init__(self, n_qubits=4, encoding_window=1.0):
        self.n_qubits = n_qubits

    def extract_phase(self, signal):
        analytic = hilbert(signal)
        return np.angle(analytic), np.abs(analytic)

    def detect_spikes(self, signal, threshold=2.0):
        peaks, _ = find_peaks(signal, height=threshold)
        return peaks

    def encode_to_quantum_angles(self, signal, fs=1000):
        phase, amplitude = self.extract_phase(signal)
        spikes = self.detect_spikes(signal)
        window_size = len(signal) // self.n_qubits
        angles = []
        for i in range(self.n_qubits):
            s, e = i * window_size, (i+1) * window_size
            angles.append(np.mean(phase[s:e]))           # RX
            angles.append(np.mean(amplitude[s:e]) / (np.max(amplitude)+1e-10) * np.pi)  # RY
            n_spikes = np.sum((spikes >= s) & (spikes < e))
            angles.append(n_spikes * np.pi / (window_size/fs + 1))  # RZ
        return np.array(angles).reshape(self.n_qubits, 3)
```

## Applications
1. **Quantum Time-Series Classification**: QML-enhanced classification of EEG/MEG neural signals
2. **Financial Time Series**: quantum-enhanced market prediction
3. **Sensor Data Processing**: quantum feature extraction for oscillatory signals
4. **Hybrid Quantum-Classical Neuromorphic Systems**: direct encoding of SNN output to quantum states

## Advantages
| Method | Temporal Info | Phase Info | Adaptive | Spike Compatible |
|--------|--------------|------------|----------|-----------------|
| Angle  | No | No | No | No |
| Amplitude | No | No | No | No |
| SPATE  | Yes | Yes | Yes | Yes |

## References
- arXiv:2604.11022 - SPATE: Spiking-Phase Adaptive Temporal Encoding for Quantum Machine Learning

## Activation Keywords
- spiking quantum ML, phase encoding, temporal quantum encoding, SPATE, oscillation mapping, quantum feature engineering
