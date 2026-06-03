---
name: wearbci-dataset-wearable-bci
description: "WearBCI Dataset: Understanding and benchmarking real-world wearable brain-computer interface signals. Large-scale wearable BCI benchmark dataset for evaluating signal processing and decoding under real-world conditions. Activation triggers: wearable BCI, BCI dataset, benchmark, real-world EEG, mobile BCI, dry electrode EEG."
---

# WearBCI Dataset: Understanding and Benchmarking Real-World Wearable BCI Signals

> Large-scale benchmark dataset and evaluation framework for wearable brain-computer interfaces under real-world conditions.

## Metadata
- **Source**: arXiv:2604.09649
- **Authors**: Haoxian Liu, Hengle Jiang, Lanxuan Hong, Xiaomin Ouyang
- **Published**: 2026-03-29
- **Category**: cs.HC

## Core Methodology

### Key Innovation
WearBCI provides a comprehensive dataset specifically designed for wearable BCI research, capturing real-world signal variability including motion artifacts, environmental noise, and diverse user conditions that traditional lab-based datasets miss.

### Technical Framework
1. **Data Collection**: Wearable non-invasive EEG devices in real-world settings
2. **Signal Characterization**: Analysis of signal quality degradation factors in mobile scenarios
3. **Benchmark Tasks**: Standardized evaluation protocols for wearable BCI performance
4. **Baseline Methods**: Reference implementations for common BCI paradigms on wearable data

## Implementation Guide

### Prerequisites
- Wearable EEG device (dry/wet electrode systems)
- Python with MNE, scipy, numpy
- Access to WearBCI dataset

### Step-by-Step
1. Load WearBCI dataset with real-world recording conditions
2. Characterize signal quality metrics (SNR, impedance, artifact rates)
3. Apply wearable-specific preprocessing (motion artifact removal, channel interpolation)
4. Benchmark decoding algorithms against provided baselines
5. Evaluate robustness across mobility conditions

### Code Example
```python
import numpy as np
from scipy.signal import welch

def evaluate_wearable_snr(eeg_signal, artifact_mask):
    clean = eeg_signal[~artifact_mask]
    noisy = eeg_signal[artifact_mask]
    snr = 10 * np.log10(np.var(clean) / np.var(noisy))
    return snr
```

## Applications
- Benchmarking wearable BCI algorithms
- Developing robust motion-artifact rejection methods
- Evaluating dry electrode performance
- Mobile neurorehabilitation systems
- Real-world BCI deployment studies

## Pitfalls
- Wearable EEG has significantly lower SNR than lab-grade systems
- Motion artifacts are task-dependent and hard to generalize
- Ground truth labels may be noisier in real-world settings
- Cross-device generalization remains challenging

## Related Skills
- neuropath-motor-imagery-eeg
- bci-rehabilitation-protocols
- eeg-foundation-model-adapters
- eeg-ieeg-bridge-bci
