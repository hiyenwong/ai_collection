---
name: hqnn-blood-cell-classification
description: "Hybrid Quantum-Classical Neural Network (HQNN) methodology for medical image classification, specifically blood cell classification. Combines pre-trained classical backbone (ResNet-50) with variational quantum circuit for enhanced feature representation. Use when: (1) medical image classification with limited data, (2) hybrid quantum-classical ML pipeline design, (3) comparing quantum vs classical feature transformations, (4) NISQ-era quantum advantage in medical imaging. Activation: HQNN, hybrid quantum neural network, blood cell classification, quantum medical imaging, variational quantum circuit, ResNet quantum, quantum feature transformation"
license: MIT
metadata:
  arxiv_id: "2605.23324"
  published: "2026-05-22"
  authors: "Guilherme Cruz, Nouhaila Innan, Alberto Marchisio, Gabriel Falcao, Muhammad Shafique"
  tags: [quantum, medical, HQNN, classification, blood-cells, variational-circuit]
---

# HQNN Blood Cell Classification

## Core Architecture

Modular HQNN architecture combining:
1. **Classical backbone**: Pre-trained ResNet-50 for feature extraction
2. **Latent bottleneck**: Low-dimensional classical projection (reduces to match qubit count)
3. **Variational quantum circuit**: Parameterized quantum gates for feature transformation
4. **Classical output layer**: Final classification

## Key Design Patterns

### Three-Model Comparison Protocol

To isolate quantum contribution, always evaluate three architectures:
1. **HQNN**: Classical backbone → bottleneck → VQC → classifier
2. **Classical Matched**: Classical backbone → bottleneck → *classical nonlinear layer* (same capacity as VQC) → classifier
3. **Baseline**: Classical backbone → classifier (no intermediate transformation)

This controls for model capacity and ensures quantum improvements are genuine.

### Quantum Circuit Design

- Use **angle encoding** for classical-to-quantum data mapping
- **Strongly entangling layers** (e.g., RealAmplitudes or EfficientSU2)
- Keep circuit depth shallow for NISQ compatibility (2-4 layers)
- Measure all qubits in computational basis

### Training Strategy

- Freeze backbone during initial VQC training
- End-to-end fine-tuning after VQC converges
- Use parameter-shift rule for quantum gradients
- Shot noise: 1024+ shots per circuit evaluation

## Hardware Evaluation

- Test on both simulator (noiseless) and real quantum hardware
- Expect modest degradation on real hardware (~1-3% F1 drop)
- Report both to demonstrate noise robustness

## Pitfalls

- **Barren plateaus**: VQCs with too many qubits/layers suffer from vanishing gradients. Keep qubit count ≤ 10 for medical classification tasks.
- **Bottleneck dimension mismatch**: Latent space dimension must exactly match qubit count. Use linear projection with appropriate activation.
- **Simulation vs hardware gap**: Simulators are orders of magnitude faster. Train on simulator, evaluate on hardware for final validation.
- **Dataset saturation**: On near-saturated benchmarks (e.g., 98%+ accuracy), even small F1 improvements (0.1-0.5%) are statistically meaningful.
