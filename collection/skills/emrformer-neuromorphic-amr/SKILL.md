---
name: emrformer-neuromorphic-amr
description: "EMRFormer: End-to-End Radar and Communication Modulation Recognition with Neuromorphic Computing using spike-driven transformers on KA200 neuromorphic chip. Achieves SOTA accuracy with 90%+ energy reduction. (arXiv: 2606.24075)"
tags: [neuromorphic, SNN, spike-driven-transformer, modulation-recognition, edge-AI, KA200, LIF-neurons]
---

# EMRFormer: Neuromorphic Modulation Recognition

## Paper Reference
- **Title**: End-to-End Radar and Communication Modulation Recognition with Neuromorphic Computing
- **arXiv**: 2606.24075
- **Authors**: Xiaohu Li, Chongxiao Qu, Caiyong Lin, Chenxiao Dou, Wei Hua
- **Submitted**: June 23, 2026
- **Categories**: cs.CV, cs.AI

## Core Methodology

### Architecture: EMRFormer
End-to-end spiking neural network applying spike-driven transformer to automatic modulation recognition (AMR) under neuromorphic hardware constraints.

### Key Components
1. **Adaptive Spike Encoder**: Converts raw IQ waveforms into spike representations while preserving temporal information
2. **Integer Leaky Integrate-and-Fire (I-LIF) Neurons**: Mitigates effective information degradation in spike encoding
3. **Spike-Separable CNN (SSCNN)**: Multi-scale temporal feature extraction from raw IQ data
4. **SpikeFormer Integration**: Spike-driven transformer backbone combining SSCNN with temporal attention

### Innovation Points
- First application of spike-driven transformers to AMR tasks
- Integer LIF neurons enable hardware-friendly computation
- End-to-end pipeline from raw IQ waveforms to modulation classification
- Deployed and validated on KA200 neuromorphic chip

### Results
- **Accuracy**: SOTA across multiple modulation datasets, outperforming all baselines
- **Low SNR Robustness**: Maintains strong performance in challenging signal conditions
- **Energy Efficiency**: 90%+ theoretical energy reduction vs ANN counterparts
- **Hardware Deployment**: 5x power reduction on KA200 vs 3090 GPU or Orin NX

## Practical Applications
- Resource-constrained edge devices for radar/communication
- Military/defense signal intelligence
- IoT modulation classification
- Real-time spectrum monitoring

## Activation Keywords
- EMRFormer
- spike-driven transformer
- neuromorphic modulation recognition
- KA200 chip
- SNN automatic modulation recognition
- edge AI radar
- IQ waveform classification

## Related Skills
- [[spiketimer-snn-copyright-protection]] - SNN temporal coding
- [[neuromorphic-lidar-bev-snn]] - SNN for sensor processing
- [[edgespike-edge-iot-snn]] - Edge SNN deployment
- [[frequency-matching-snn-mmwave]] - SNN for mmWave signals
