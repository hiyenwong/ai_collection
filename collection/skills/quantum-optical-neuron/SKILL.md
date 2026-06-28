---
name: quantum-optical-neuron
description: "Quantum optical neuron methodology — camera-free image classification via Hong-Ou-Mandel interference of spatially programmable single photons. Two-photon coincidences directly report overlap between input image mode and learned template. Use when building neuromorphic quantum photonic processors, photon-starved imaging systems, or quantum-classical hybrid inference pipelines."
metadata:
  arxiv_id: "2603.28879"
  published: "2026-03-30"
  authors: "Unknown"
  tags: [quantum, neuromorphic, photonics, imaging, neuroscience]
---

# Quantum Optical Neuron

## Core Concept

Camera-free quantum-optical image classifier using Hong-Ou-Mandel (HOM) interference. Input images are encoded as spatial modes of single photons; two-photon coincidences directly measure the overlap between input and a learned template, replacing pixel-resolved acquisition with a single global measurement.

## Mathematical Framework

**HOM Interference as Inner Product:**
- Input state: |ψ_in⟩ = spatial mode encoding image
- Template state: |ψ_template⟩ = learned reference mode  
- Two-photon coincidence rate: P_coincidence ∝ |⟨ψ_in|ψ_template⟩|²
- Direct measurement of image-template similarity without pixel-by-pixel scanning

**Single-Perceptron Quantum Optical Neuron:**
- Single tunable beam splitter with spatial light modulator
- Threshold on coincidence rate → binary classification

**Shallow Quantum Neural Network:**
- Two-neuron architecture with programmable weights
- Cascaded HOM interferometers for multi-class classification

## Key Properties

1. **Resolution Independence**: Performance insensitive to input resolution under fixed measurement budget — fundamentally different from classical pixel-scaling
2. **Photon Efficiency**: Operates in photon-starved regimes where classical cameras fail
3. **Noise Robustness**: Strong robustness to experimental noise from quantum interference properties
4. **Hardware Simplicity**: Minimal optical components vs. full quantum optical processors

## Usage Patterns

### Pattern 1: Photon-Starved Imaging Classification
When classical imaging SNR is insufficient (remote sensing, biological microscopy):
1. Encode image as spatial photon mode via SLM
2. Prepare template states for each class
3. Measure HOM coincidence rates against each template
4. Classify by maximum coincidence rate

### Pattern 2: Neuromorphic Quantum Photonic Processor
For building scalable quantum-neuromorphic systems:
1. Implement single-perceptron quantum optical neurons
2. Connect via tunable beam splitters (synaptic weights)
3. Cascade for shallow network inference
4. Train template states via classical optimization loop

### Pattern 3: Energy-Efficient Inference
For low-power edge inference with photon-level data:
1. Use HOM interference as physical-layer inner product computation
2. Avoid ADC + digital processing pipeline entirely
3. Achieve classification at measurement layer directly

## Implementation Notes

- **Platform**: Linear optical quantum computing with SPDC sources or quantum dots
- **Encoding**: Spatial light modulator for mode preparation
- **Detection**: Single-photon avalanche diodes (SPADs) for coincidence counting
- **Measurement Budget**: Fixed number of coincidence measurements; optimize allocation across classes

## Cross-References

- [[quantum-memristor-vacuum-one-photon]] (2503.02466) — Quantum memristors for memory-dependent quantum neurons
- [[quantum-snn-fusion]] — Quantum-SNN hybrid architectures
- [[neuromorphic-quantum-computing]] — Broader neuromorphic quantum computing patterns

## Activation Keywords

- quantum optical neuron
- HOM interference classification
- camera-free quantum imaging
- 量子光学神经元
- photon-starved image classification
- neuromorphic quantum photonic
- quantum perceptron optical
- Hong-Ou-Mandel neural network
