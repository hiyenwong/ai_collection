---
name: gsu-dbnet-snn-speech-enhancement
description: "GSU-DBNet: Dual-Branch Spiking Neural Network for neuromorphic speech enhancement with Gated Spiking Units (GSU). Achieves PESQ 3.04 with only 394K params (4.5-10.6% of ANN models). (arXiv: 2606.23761)"
tags: [SNN, speech-enhancement, neuromorphic, gated-spiking-unit, dual-branch, energy-efficient, Interspeech2026]
---

# GSU-DBNet: Dual-Branch SNN for Speech Enhancement

## Paper Reference
- **Title**: Neuromorphic Speech Enhancement with Dual-Branch Spiking Neural Networks
- **arXiv**: 2606.23761
- **Authors**: Taiyu Meng, Wenbin Jiang, Haoyi Zhang, Yuhan Zhou, Haibing Yin
- **Submitted**: June 22, 2026
- **Venue**: Submitted to Interspeech 2026
- **Categories**: cs.SD, cs.AI, eess.AS

## Core Methodology

### Architecture: GSU-DBNet
Novel dual-branch spiking neural network with Gated Spiking Units (GSU) for speech enhancement.

### Key Components
1. **Gated Spiking Unit (GSU)**: Novel neuron model with gating mechanism addressing binary activation limitations
2. **Dual-Branch Architecture**: Simultaneously models:
   - Speech magnitude spectrum → magnitude spectral mask
   - Complex spectrum → complex spectral mask
3. **Dual-Path GSU Module**: Exploits both temporal and frequency dimensions for enhanced spatiotemporal feature representation
4. **Spike-Driven Processing**: Entire pipeline uses event-driven computation

### Innovation Points
- First dual-branch SNN for speech enhancement
- GSU gating mechanism overcomes binary activation limitations of traditional SNNs
- Simultaneous magnitude and complex spectrum processing (bio-inspired: mimics cochlear dual processing)
- Extreme parameter efficiency: 394K params

### Results
- **PESQ Score**: 3.04 (state-of-the-art among SNN-based methods)
- **Parameter Count**: Only 394K parameters
  - 4.5%--10.6% of representative ANN-based models
- **Energy Efficiency**: Inherent spike-driven computation enables ultra-low power deployment

## Neuroscience Connection
- Dual-branch processing mirrors auditory system's parallel magnitude/phase processing
- GSU gating resembles cortical inhibitory gating mechanisms
- Temporal-frequency dual-path mimics auditory cortex feature hierarchy
- Demonstrates neuromorphic computing's viability for real-world audio tasks

## Practical Applications
- Hearing aids and cochlear implants
- Voice assistants on edge devices
- Real-time noise cancellation
- Telecommunications
- IoT audio processing

## Activation Keywords
- GSU-DBNet
- gated spiking unit
- dual-branch SNN
- neuromorphic speech enhancement
- SNN speech processing
- Interspeech 2026 SNN
- energy-efficient speech

## Related Skills
- [[spiketimer-snn-copyright-protection]] - SNN temporal coding
- [[emrformer-neuromorphic-amr]] - Neuromorphic signal processing
- [[edgespike-edge-iot-snn]] - Edge SNN deployment
- [[neuromorphic-supremacy]] - Neuromorphic computing framework
