---
name: qmt-qnn-training-stability
description: "Quantum Measurement Temperature (QMT) methodology for mitigating measurement-induced training instability in hybrid QNN classifiers. Introduces learnable scaling parameter to rescale quantum measurement outputs, improving gradient magnitude and preventing training collapse."
category: neuroscience
metadata:
  arxiv_id: "2606.22551"
  authors: "Milton Mondal, Sushovan Chanda, Mohamad Mahdi Alawieh"
  published: "2026-06-21"
  categories: "quant-ph, cs.LG"
---

# QMT: Quantum Measurement Temperature for Hybrid QNN Training Stability

## Context

Hybrid Quantum Neural Network (QNN) classifiers produce bounded logits [-1,1] from Pauli measurements, which causes measurement-induced logit contraction that suppresses gradients during training. This paper introduces Quantum Measurement Temperature (QMT) — a learnable scaling parameter that rescales quantum measurement outputs prior to loss computation, stabilizing training across multiple benchmarks.

## Core Methodology

### 1. The Problem: Measurement-Induced Logit Contraction

- QNN classifiers output logits via expectation values of Pauli observables: `z = ⟨ψ(θ)|O|ψ(θ)⟩`
- These are bounded: z ∈ [-1, 1], regardless of parameter values
- When targets are far from this range, or when the model needs to push predictions to extremes, gradients vanish
- This causes training instability, especially in deeper circuits or with limited qubits

### 2. QMT Solution

Introduce a learnable temperature parameter β:
```
z_rescaled = β · z = β · ⟨ψ(θ)|O|ψ(θ)⟩
```

The temperature β is trained jointly with the quantum circuit parameters θ via gradient descent:
```
L(θ, β) = CrossEntropy(σ(β · z), y)
∂L/∂β = ∂L/∂z_rescaled · z
∂L/∂θ = ∂L/∂z_rescaled · β · ∂z/∂θ
```

### 3. Architecture-Agnostic Design

- QMT works with any QNN architecture (IQP, hardware-efficient, data re-uploading)
- Does not modify the quantum circuit — only the classical post-processing
- Computationally negligible overhead (single scalar multiplication)
- Compatible with existing quantum ML frameworks (PennyLane, Qiskit)

### 4. Empirical Results

Tested on:
- **Fluorescence microscopy images**: Stable convergence where baseline QNN fails
- **Fashion MNIST**: Improved accuracy and training stability
- Gradient magnitude and variance both improved with QMT

## Implementation Steps

1. Build your hybrid QNN classifier as usual (data encoding → variational circuit → Pauli measurement)
2. Initialize β = 1.0 (or a small positive value)
3. Before computing loss, rescale: `logits = β * expectation_values`
4. Include β in your optimizer's parameter list alongside circuit parameters
5. Train end-to-end with standard loss functions (cross-entropy, MSE)
6. Monitor β during training — it should adapt to the optimal scaling for your task

## Pitfalls

- **β initialization**: Starting β too small can still cause vanishing gradients initially. β = 1.0 is a safe default.
- **β runaway**: Without regularization, β can grow unbounded. Consider adding a small penalty term: `λ · log(β)` or clipping β to [0.1, 100].
- **Multi-class extension**: For multi-class QNNs with multiple output qubits, apply a single shared β or per-class β_i — experiment to determine which works better for your task.
- **Not a substitute for expressibility**: QMT addresses gradient scaling but cannot fix fundamentally unexpressive ansätze.

## Verification

- Training loss should decrease monotonically (no plateaus or divergence)
- Gradient norms should remain above numerical noise floor throughout training
- β should converge to a task-specific value (typically 2-20 for binary classification)
- QNN with QMT should match or exceed classical baseline performance on same task

## Activation Keywords

QMT, quantum measurement temperature, QNN training, hybrid quantum neural network, gradient vanishing, logit contraction, Pauli measurement, variational quantum circuit, quantum classifier, training stability, learnable scaling, quantum machine learning, fluorescence microscopy, NISQ, parameterized quantum circuit, PennyLane, Qiskit
