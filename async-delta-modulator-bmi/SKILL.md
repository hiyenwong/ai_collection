---
name: async-delta-modulator-bmi
description: "Asynchronous Delta Modulation (ADM) for spike encoding in event-driven Brain-Machine Interfaces. Converts analog biopotentials into discrete ON/OFF spikes for SNN-compatible neural recording in 65nm CMOS. Activation: async delta modulator, spike encoding BMI, event-driven neural recording, neuromorphic front-end, asynchronous ADC"
---

# Asynchronous Delta Modulator for Spike Encoding in Event-Driven Brain-Machine Interfaces

## Overview

This methodology presents an **Asynchronous Delta Modulator (ADM)** as a spike encoder for event-driven neural recording, implemented in 65nm CMOS. The ADM converts continuous analog biopotential signals (EEG, ECoG, neural spikes) into discrete, asynchronous ON and OFF spike trains that are natively compatible with Spiking Neural Networks (SNNs) for real-time decoding in closed-loop BMI systems.

## Source Paper

- **Title:** An Asynchronous Delta Modulator for Spike Encoding in Event-Driven Brain-Machine Interface
- **Authors:** Kaushik Lakshmiramanan, Vineeta Nair, Ching-Yi Lin et al.
- **arXiv:** 2604.08758v2
- **Published:** 2026-04-09
- **Categories:** eess.SY, cs.NE

## Core Concepts

### Asynchronous Delta Modulation (ADM)

Unlike conventional ADCs that sample at fixed rates, ADM operates **asynchronously** -- it generates events (spikes) only when the input signal crosses a threshold relative to its previous value:

- **ON spike**: Input exceeds reference + threshold (signal rising)
- **OFF spike**: Input drops below reference - threshold (signal falling)
- **No output**: Signal stays within deadband (power saving)

### Key Advantages

1. **Data compression**: Continuous biopotentials -> sparse spike trains (10-100x reduction)
2. **Event-driven processing**: Computation only when events occur (ultra-low power)
3. **SNN-native output**: Spike trains directly feed into neuromorphic decoders
4. **Closed-loop compatible**: Low latency enables real-time BMI control

## Implementation

```python
import numpy as np

class AsynchronousDeltaModulator:
    """Software model of Asynchronous Delta Modulator for spike encoding."""
    
    def __init__(self, threshold=0.01, initial_value=0.0):
        self.threshold = threshold
        self.reference = initial_value
        self.spike_times = []
        self.spike_types = []  # +1 for ON, -1 for OFF
        
    def encode(self, signal, timestamps):
        """Encode continuous signal into asynchronous spike train."""
        self.spike_times = []
        self.spike_types = []
        self.reference = signal[0]
        
        for t, val in zip(timestamps, signal):
            diff = val - self.reference
            
            if diff > self.threshold:
                self.spike_times.append(t)
                self.spike_types.append(+1)
                self.reference += self.threshold
            elif diff < -self.threshold:
                self.spike_times.append(t)
                self.spike_types.append(-1)
                self.reference -= self.threshold
        
        return np.array(self.spike_times), np.array(self.spike_types)
    
    def decode(self, spike_times, spike_types):
        """Reconstruct signal from spike train (for validation)."""
        reconstructed = []
        current_value = 0.0
        
        for st, sp in zip(spike_times, spike_types):
            if sp == +1:
                current_value += self.threshold
            else:
                current_value -= self.threshold
            reconstructed.append((st, current_value))
        
        return reconstructed


def encode_eeg_to_spikes(eeg_signal, sampling_rate=1000, threshold=50e-6):
    """Convert EEG signal to spike train using ADM."""
    timestamps = np.arange(len(eeg_signal)) / sampling_rate
    adm = AsynchronousDeltaModulator(threshold=threshold)
    spike_times, spike_types = adm.encode(eeg_signal, timestamps)
    
    events = []
    for i, (t, tp) in enumerate(zip(spike_times, spike_types)):
        events.append((t, 0, tp))
    
    return events
```

## Practical Applications

- Real-time neural decoding for prosthetic control
- Adaptive DBS (Deep Brain Stimulation) triggering
- Implantable neural recording systems
- Wearable EEG/BCI headsets

## Limitations

- Threshold selection trades off between compression and fidelity
- Reconstruction quality depends on signal dynamics
- 65nm CMOS implementation has area/power trade-offs

## References

- Lakshmiramanan, K., Nair, V., Lin, C.-Y. et al. (2026). "An Asynchronous Delta Modulator for Spike Encoding in Event-Driven Brain-Machine Interface." arXiv:2604.08758v2.

## Activation Keywords

- async delta modulator
- spike encoding BMI
- event-driven neural recording
- neuromorphic front-end
- asynchronous ADC
- 异步增量调制
- 脑机接口脉冲编码
- 事件驱动神经记录
