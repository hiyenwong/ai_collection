---
name: qml-equilibrium-propagation-medical
description: "Quantum Machine Learning with Equilibrium Propagation for medical image analysis. Energy-based training without backpropagation using Variational Quantum Circuits (VQCs) for resource-constrained quantum hardware. Use when: analyzing blood cells, leukemia detection, medical imaging with QML, energy-based quantum training, backprop-free quantum networks, or evaluating QML feasibility on NISQ devices."
metadata:
  arxiv_ids: "1808"
  published: "2026-01-26"
  tags: [quantum, machine-learning, medical, equilibrium-propagation, blood-cells, vqc, nisoq]
---

# QML with Equilibrium Propagation for Medical Imaging

## Description

Feasibility study applying Quantum Machine Learning (QML) with Equilibrium Propagation (EP) — an energy-based, backpropagation-free training method — and Variational Quantum Circuits (VQCs) for acute myeloid leukemia (AML) detection from blood cell images. Demonstrates competitive performance under severe quantum hardware constraints (limited qubits, noise).

**Key insight**: EP avoids backpropagation by computing gradients through energy differences, making it compatible with quantum circuits where backprop is not natively supported.

## Core Methodology

### Equilibrium Propagation (EP)

EP computes gradients via energy differences rather than backpropagation:

1. **Forward pass**: Run input through network to equilibrium state
2. **Nudging**: Slightly perturb output toward target (±ε)
3. **Gradient estimation**: ∂E/∂θ ≈ (E_nudged - E_free) / ε
4. **Update**: Apply gradient to quantum circuit parameters

### Variational Quantum Circuits (VQCs)

- Parameterized quantum gates (rotation angles = trainable params)
- Classical-quantum hybrid: classical optimizer updates quantum params
- Measurement outcomes feed into loss function
- Hardware-efficient ansatz for NISQ compatibility

### Medical Application Pipeline

1. **Input**: Blood cell microscopy images
2. **Preprocessing**: Resize, normalize, encode into quantum states
3. **Feature extraction**: VQC layer(s) with EP training
4. **Classification**: Binary (AML vs normal) or multi-class
5. **Output**: Prediction with confidence

## When to Use

- Medical image classification with quantum circuits
- Backpropagation-free quantum training needed
- NISQ hardware constraints (few qubits, high noise)
- Blood cell analysis, leukemia detection
- Evaluating QML feasibility before scaling

## Implementation Steps

1. **Data preparation**: Encode medical images into quantum states (amplitude/angle encoding)
2. **VQC design**: Choose hardware-efficient ansatz matching device topology
3. **EP training**: Implement energy-based gradient computation
4. **Classical optimizer**: Use gradient-free (COBYLA, SPSA) or EP-computed gradients
5. **Validation**: Compare against classical baselines on same task

## Error Handling

### Limited Qubit Count
- Use amplitude encoding to maximize information per qubit
- Consider circuit cutting for larger problems
- Feature selection to reduce input dimensionality

### Hardware Noise
- Error mitigation: zero-noise extrapolation, readout error correction
- Noise-aware training: include noise model in simulation
- Shallow circuits to reduce decoherence impact

### EP Convergence Issues
- Careful ε selection (too small → noisy gradients, too large → biased)
- Multiple nudging directions for variance reduction
- Warm-start from classically pretrained weights

## Resources

- Paper: Entity ID 1808 in kg.db
- Related: VQC architecture patterns from quantum-neural-architecture skill
- Related: Medical imaging patterns from quantum-medical-diagnosis skill
