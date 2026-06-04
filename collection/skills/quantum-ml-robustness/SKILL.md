---
name: quantum-ml-robustness
description: >
  Analyze and test Quantum Machine Learning (QML) model accuracy and robustness.
  Covers quantum neural network (QNN) robustness evaluation, mutation testing for
  quantum circuits, variational quantum circuit analysis, and scalability assessment
  for near-term quantum hardware. Use when evaluating QML model reliability, designing
  fault injection tests for quantum circuits, assessing QNN generalization, or preparing
  quantum algorithms for NISQ-era hardware deployment.
  Triggers: quantum ML robustness, QNN testing, quantum mutation testing,
  variational quantum circuit analysis, quantum model accuracy, 量子机器学习鲁棒性,
  quantum neural network robustness.
---

# Quantum ML Robustness Testing

Analyze robustness, accuracy, and fault tolerance of Quantum Machine Learning models.

## Core Methodology

### 1. QNN Architecture Analysis

Quantum Neural Networks consist of:
- **Variational Quantum Circuits (VQC)**: Parameterized quantum gates forming layers
- **Encoding/Ansatz**: Data embedding into quantum states via rotation gates, amplitude encoding
- **Measurement**: Extracting classical outputs via expectation values

Key robustness factors:
- Circuit depth vs. hardware noise (decoherence time)
- Parameter count vs. expressibility (barren plateaus risk)
- Entanglement structure vs. task complexity

### 2. Mutation Testing for Quantum Circuits

Inject controlled faults into quantum circuits to evaluate model resilience:

```
Mutation Operations:
├── Gate-level: Replace H with I, swap CX targets, remove gates
├── Parameter-level: Perturb rotation angles (±ε), random phase shifts
├── Structural: Add/remove entangling gates, change qubit connectivity
└── Noise-level: Insert depolarizing channels, amplitude damping
```

Metrics:
- **Mutation Score**: % of mutants detected by test suite
- **Accuracy Degradation**: Δaccuracy between original and mutated models
- **Robustness Index**: 1 - (mean accuracy drop / max possible drop)

### 3. Accuracy-Robustness Tradeoff

QNNs exhibit unique tradeoffs:
- More parameters → better accuracy but wider attack surface
- Deeper circuits → more expressivity but more noise sensitivity
- More qubits → higher capacity but more crosstalk errors

Evaluation protocol:
1. Train QNN on target task (classification, regression, optimization)
2. Apply mutation operators at increasing severity levels
3. Measure accuracy degradation curves
4. Compute robustness metrics and identify failure modes

### 4. NISQ Hardware Readiness

Assess if QNN is deployable on near-term hardware:
- **Circuit depth** < coherence time / gate time
- **Qubit count** ≤ available physical qubits with connectivity
- **Noise budget**: estimated error rate < algorithmic threshold
- **Error mitigation**: zero-noise extrapolation, measurement mitigation

## Workflow

### Step 1: Model Characterization
Identify QNN architecture: encoding strategy, ansatz type, measurement scheme, number of parameters and qubits.

### Step 2: Baseline Evaluation
Run QNN on clean data to establish baseline accuracy, loss, and convergence behavior.

### Step 3: Mutation Testing
Apply mutation operators systematically. Use references/qnn-mutations.md for specific gate-level mutations.

### Step 4: Robustness Analysis
Plot accuracy vs. mutation severity. Identify critical thresholds where model fails.

### Step 5: Hardware Assessment
Map circuit to target quantum backend. Estimate noise impact using references/hardware-mapping.md.

## Key Papers & Patterns

From recent research (2026-05-05):
- "A Comprehensive Analysis of Accuracy and Robustness in Quantum Neural Networks" — layered VQC robustness evaluation
- "Efficient Mutation Testing of Quantum Machine Learning Models" — fault injection in quantum circuits
- "Getting large-scale quantum neural networks ready for quantum hardware" — NISQ deployment preparation

## Pitfalls

- **Barren Plateaus**: Deep QNNs may have vanishing gradients. Use shallow circuits or layer-wise training.
- **Data Encoding Bias**: Different encoding strategies (angle, amplitude, basis) affect robustness differently.
- **Simulation vs. Reality**: Noise-free simulators overestimate robustness. Always test with noise models.
- **Mutant Equivalence**: Some mutations produce functionally identical circuits. Verify mutation diversity.
