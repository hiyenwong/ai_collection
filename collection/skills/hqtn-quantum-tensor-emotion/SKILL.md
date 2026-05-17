---
name: hqtn-quantum-tensor-emotion
description: >
  Design and implement hybrid quantum-classical neural architectures for emotion
  recognition and affective computing tasks. Combines quantum circuit Born machines
  (QCBM), tensor networks, and classical neural networks for compact nonlinear
  correlation modeling in scenarios with subtle, speaker-dependent, or confounded
  emotional signals. Use when: speech emotion recognition (SER), affective computing,
  quantum machine learning for neuroscience/brain-related tasks, hybrid quantum-
  classical architectures, tensor network quantum circuits, emotion-aware AI, or
  compact quantum neural modules are needed.
---

## Overview

Hybrid Quantum Tensor Networks (HQTN) combine classical feature extraction with
quantum circuit modules to model complex nonlinear correlations in emotional/neural
signals where classical models struggle with limited data and subtle patterns.

## Core Architecture Pattern

```
Classical Feature Extractor → Quantum Circuit Module → Classical Head
```

### 1. Feature Extraction
- Use classical networks (LSTM, CNN, Transformer) for initial feature extraction
- Extract multi-scale temporal patterns from sequential data
- For audio/speech: MFCC, spectral features, prosodic features

### 2. Quantum Circuit Born Machine (QCBM) Module
- Replace or augment classical hidden layers with parameterized quantum circuits
- Use QCBM for compact nonlinear correlation modeling
- Circuit structure matters: test RY+CX, RZ+CY, and hardware-efficient ansatzes
- Parameter count independent of input dimension → compact modules
- Key advantage: introduces nonlinearity and correlation with fewer parameters

### 3. Measurement and Readout
- Measure qubit expectation values as output features
- Use shot-based estimation for probabilistic outputs
- For emotion classification: map to probability distribution over emotion classes

## Implementation Guidelines

### Circuit Design Principles
- **Depth**: 2-4 layers for NISQ-era devices; deeper circuits increase expressivity but degrade under noise
- **Entanglement**: Use controlled gates to model cross-feature correlations
- **Ansatz**: Hardware-efficient ansatzes preferred for real devices
- **Parameter sharing**: Share parameters across circuit blocks to reduce optimization difficulty

### Noise Robustness
- Test under backend-calibrated noise models (e.g., ibm-torino)
- Verify numerical stability across shot ranges
- QCBM shows resilience: compact structure means fewer error channels
- For real deployment: use noisy simulators before hardware

### Training Strategy
1. Pre-train classical feature extractor on large dataset
2. Initialize quantum circuit with random or problem-informed parameters
3. Train end-to-end with hybrid classical-quantum gradient flow
4. Use parameter-shift rule for quantum gradients
5. Monitor: classical baseline vs hybrid with matched parameter budget

## Performance Considerations

- **Parameter efficiency**: QCBM modules achieve comparable results with 50-80% fewer parameters
- **Small data regimes**: HQTN excels when training data is limited (e.g., rare emotion categories)
- **Real-world robustness**: Better generalization across recording conditions
- **Circuit structure impact**: Different ansatzes yield significantly different performance — always ablate

## Evaluation Protocol

1. Establish classical baseline (matched parameter count)
2. Test hybrid architecture with various circuit structures
3. Evaluate under noise: noisy simulator with backend-calibrated parameters
4. Sweep quantum-channel budget to find optimal classical-quantum partition
5. Report: accuracy, F1, confusion matrix, and parameter count comparison

## Related Architectures

- **Photonic QNN**: For energy-efficient deep quantum networks, use Hilbert space
  expansion via input replication instead of ancillary qubits (arXiv: 2605.06397)
- **QTCNN**: Quantum temporal convolutional networks for time-series prediction
  (arXiv: 2512.xxxx) — combines temporal encoder with quantum convolution
- **QPINN**: Quantum physics-informed neural networks for PDE-constrained tasks

## Activation
- speech emotion recognition, SER, emotion classification, affective computing
- quantum neural network, QNN, quantum circuit Born machine, QCBM
- tensor network, hybrid quantum-classical, quantum machine learning
- compact quantum modules, parameter-efficient quantum, NISQ deployment
- quantum neuroscience, brain-computer interface, neural signal analysis
