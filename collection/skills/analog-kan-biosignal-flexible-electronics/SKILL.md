---
name: analog-kan-biosignal-flexible-electronics
description: "Analog Kolmogorov-Arnold Networks (AKANs) for low-power function approximation in flexible electronics. Hardware-software co-optimization with circuit-level error modeling during training and dual-level pruning. Targets wearable biosignal processing (EEG, ECG, EMG) with 55% area and 50% power savings. Use when: neuromorphic computing for biosignals, analog neural network hardware, flexible electronics, low-power function approximation, wearable neural inference, sensor calibration, logarithmic compression."
date_added: 2026-06-30
arxiv_id: "2606.27892"
authors:
  - Paula Carolina Lozano Duarte
  - Georgios Zervakis
  - Mehdi Tahoori
  - Sani Nassif
categories:
  - cs.AR
  - cs.ET
  - cs.NE
venue: IEEE JETCAS (2026)
doi: "10.1109/JETCAS.2026.3707339"
---

# Analog Kolmogorov-Arnold Networks for Low-Power Biosignal Processing

## Paper Metadata
- **arXiv ID**: 2606.27892
- **Published**: 2026-06-26
- **Categories**: cs.AR (Hardware Architecture), cs.ET (Emerging Technologies), cs.NE (Neural and Evolutionary Computing)
- **Venue**: IEEE Journal on Emerging and Selected Topics in Circuits and Systems (JETCAS)
- **Authors**: Paula Carolina Lozano Duarte, Georgios Zervakis, Mehdi Tahoori, Sani Nassif

## Core Problem
Wearable devices and IoT sensors require on-sensor processing of biosignals (EEG, ECG, etc.) including:
- Nonlinear activation functions for neural network inference
- Sensor calibration curves (raw → physical units)
- Signal preprocessing (logarithmic compression, power operations)

These operations are computationally demanding in digital implementations, especially on Flexible Electronics (FE) platforms with strict area/power constraints.

## Key Innovation: Analog KAN (AKAN)

### Architecture
- **Kolmogorov-Arnold Network** variant designed for analog hardware
- Functions learned on learnable spline-based activation functions (KAN paradigm)
- Implemented in analog domain → eliminates ADC overhead
- Hardware-software co-optimization with circuit-level error modeling during training

### Hardware-Software Co-Optimization Pipeline
```
1. Software Training → Circuit-level error injection during forward pass
2. Pruning at Software Level → Remove redundant spline parameters
3. Hardware Mapping → Physical circuit implementation with pruning
4. Hardware-level Pruning → Further area/power reduction
5. Accuracy Recovery → Pruning regularizes spline parameters (can IMPROVE accuracy)
```

### Key Insight: Pruning as Regularization
Counterintuitively, pruning not only reduces hardware cost but **improves approximation accuracy** by regularizing spline parameters — preventing overfitting to hardware non-idealities.

## Results
- **Area savings**: up to 55%, average ~30%
- **Power savings**: up to 50%, average ~30%
- Validated across multiple biosignal processing benchmarks
- Generalizable to various function approximation tasks

## Neuroscience Relevance

### Direct Applications
1. **EEG signal preprocessing**: On-sensor artifact removal, feature extraction
2. **ECG monitoring**: Real-time arrhythmia detection at the sensor
3. **EMG processing**: Prosthetic control with ultra-low power
4. **Neural implant interfaces**: Low-power spike sorting at the electrode

### Broader Implications
- Enables always-on neural signal processing without cloud connectivity
- Supports edge intelligence for brain-computer interfaces
- Reduces data transmission bandwidth (compute at sensor vs. transmit raw data)
- Critical for implantable neurodevices with strict power budgets

## Technical Details

### Flexible Electronics Constraints
- Limited transistor count → aggressive pruning essential
- Process variations → circuit-level error modeling needed during training
- Power budget → analog computation eliminates ADC/digital overhead
- Mechanical flexibility → limits circuit complexity

### KAN vs MLP Paradigm
| Aspect | KAN (Analog) | Traditional MLP (Digital) |
|--------|-------------|--------------------------|
| Activation | Learnable splines on edges | Fixed nonlinearities on nodes |
| Hardware | Analog current/voltage | Digital gates |
| Power | ~50% lower | Baseline |
| Area | ~30% smaller | Baseline |
| Biosignal fit | Natural for continuous signals | Requires quantization |

## Methodology for Reproduction
1. Define target function (calibration curve, preprocessing operation)
2. Train KAN with injected circuit non-idealities
3. Apply structured pruning to spline coefficients
4. Map pruned network to analog FE circuit
5. Apply hardware-level pruning based on physical layout
6. Validate on real biosignal datasets

## Connections
- [[analog-neuromorphic-plasticity]] - Related neuromorphic computing approaches
- [[snn-mcu-fullfeature-edge]] - Edge SNN processing (complementary approach)
- [[edgespike-edge-iot-snn]] - SNN for IoT edge processing
- [[sniff-near-sensor-noise-filter-dvs]] - Near-sensor neural processing
- [[rescom-reconfigurable-snn-stochastic-computing]] - Stochastic computing for SNNs
- [[physical-neural-computing-review]] - Survey of physical neural substrates

## Activation Keywords
- Analog KAN, AKAN
- Flexible electronics biosignal
- Low-power neural hardware
- Wearable neural inference
- Sensor-level processing
- Hardware-software co-optimization
- Analog function approximation
- Edge biosignal computing
- Kolmogorov-Arnold network hardware
- Pruning regularization
- Circuit-level error modeling
- On-sensor neural computation
