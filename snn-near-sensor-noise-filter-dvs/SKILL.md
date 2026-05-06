---
name: snn-near-sensor-noise-filter-dvs
description: "SNN-based near-sensor noise filter (SNNF) for Dynamic Vision Sensors (DVS) using Event-Based Binary Image (EBBI) representation. Eliminates Background Activity noise with spike-based computation. Use when: event camera noise filtering, neuromorphic vision, DVS preprocessing, IoVT edge applications, SNN hardware deployment, or near-sensor filtering."
---

# SNN Near-Sensor Noise Filter for DVS

> Hardware-efficient SNN-based Background Activity noise filter for Dynamic Vision Sensors using EBBI representation and spike-based computation.

## Metadata
- **Source**: arXiv:2605.01937
- **Authors**: Yahan Yang, Pradeep Kumar Gopalakrishnan, Chang Chip Hong, Arindam Basu
- **Published**: 2026-05-03

## Core Problem

Dynamic Vision Sensors (DVS) offer exceptional dynamic range and low power for edge/IoVT applications, but output is heavily degraded by spurious **Background Activity (BA) noise**, causing significant computational overhead downstream.

## SNNF Architecture

### Three Components

1. **Event-Based Binary Image (EBBI) Representation**
   - Binary-array format that **eliminates timestamp dependency**
   - Drastically reduces memory footprint vs. traditional event representations
   - Converts asynchronous events into spatial binary patches

2. **Parallel Memory Architecture**
   - Stores EBBI patches for temporal context
   - Enables efficient lookup for noise pattern matching

3. **Single-Layer SNN Classifier**
   - Spike-based computation replaces power-hungry multipliers
   - Uses simple accumulation logic
   - Minimizes inter-neuron data width

### Key Innovation

The EBBI representation removes timestamp dependency, converting the filtering problem from temporal sequence processing to spatial pattern recognition. The SNN classifier then operates on these binary patterns using only accumulate operations — no multiplications needed.

## Implementation Guide

### EBBI Construction

```python
import numpy as np

def build_ebbi(events, sensor_width=346, sensor_height=260, patch_size=5):
    """
    Build Event-Based Binary Image from DVS events.
    
    Parameters:
    - events: list of (x, y, t, polarity) tuples
    - sensor_width/height: DVS sensor dimensions
    - patch_size: spatial window size
    
    Returns:
    - ebbi: binary array of shape (H//patch_size, W//patch_size)
    """
    # Aggregate events into spatial bins
    h_bins = sensor_height // patch_size
    w_bins = sensor_width // patch_size
    ebbi = np.zeros((h_bins, w_bins), dtype=np.uint8)
    
    for x, y, t, pol in events:
        bin_x = x // patch_size
        bin_y = y // patch_size
        if 0 <= bin_x < w_bins and 0 <= bin_y < h_bins:
            ebbi[bin_y, bin_x] = 1
    
    return ebbi
```

### SNN Classification

```python
class SNNNoiseFilter:
    """Single-layer SNN for BA noise classification."""
    
    def __init__(self, input_dim, n_neurons=64):
        self.weights = np.random.randn(n_neurons, input_dim) * 0.1
        self.threshold = 1.0
        self.spike_window = 10  # time steps
        
    def classify(self, ebbi_flat):
        """
        Classify EBBI patch as signal or noise.
        Uses accumulation-only computation (no multiplication).
        """
        # Spike-based: count weighted contributions
        membrane_potentials = np.zeros(self.weights.shape[0])
        
        for i, val in enumerate(ebbi_flat):
            if val > 0:  # Only process active pixels
                membrane_potentials += self.weights[:, i]
        
        # Threshold to get spikes
        spikes = (membrane_potentials > self.threshold).astype(np.float32)
        
        # Majority vote
        return spikes.mean() > 0.5  # True = signal, False = noise
```

## Hardware Performance Benchmarks

| Metric | SNNF Result |
|:---|:---|
| **Filtering Accuracy** | AUC = 0.89 |
| **FPGA Memory** | ~11% of SOTA |
| **FPGA Logic** | ~40% of SOTA |
| **FPGA Throughput** | 29 Meps |
| **65nm CMOS ASIC Area** | ~13% of ANN designs |
| **65nm CMOS ASIC Power** | <5% of ANN designs |
| **65nm CMOS ASIC Throughput** | 44.4 Meps |

## Applications

- Event camera preprocessing pipelines
- Neuromorphic vision systems
- IoVT (Internet of Video Things) edge devices
- Autonomous robotics with DVS
- Low-power surveillance systems

## Pitfalls

- **EBBI loses temporal resolution**: Timestamp information is discarded; fine-grained temporal patterns may be lost
- **Patch size trade-off**: Larger patches lose spatial detail; smaller patches increase memory
- **Training data dependency**: Must be trained on representative DVS datasets matching target deployment conditions
- **Not a replacement for temporal filters**: Works best combined with simple temporal filtering for BA noise

## Related Skills

- edgespike-edge-iot-snn
- realtime-snn-object-detection-edge
- snn-microcontroller-simulation
- snn-fpga-hardware-software-codesign
