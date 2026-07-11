---
name: qml-framework-agnostic-design
description: Design framework-agnostic quantum machine learning (QML) systems using the Model-Agnostic Learning System (MALS) paradigm. Extracts QML models from any framework (PennyLane, Qiskit, TensorFlow Quantum, etc.) into portable representations with auto-validation and cross-framework compatibility testing.
---

Design and implement framework-agnostic Quantum Machine Learning (QML) systems using the Model-Agnostic Learning System (MALS) paradigm.

## When to Use
- Building QML pipelines that must run across multiple quantum frameworks (PennyLane, Qiskit, Qulacs, TensorFlow Quantum)
- Migrating existing QML code from one framework to another without rewriting
- Creating reusable QML model libraries independent of underlying hardware/software stack
- Validating that a QML model produces identical results across different framework implementations
- Evaluating QML performance across noisy simulators vs real quantum hardware

## Architecture: MALS Pattern

The MALS (Model-Agnostic Learning System) pattern decouples QML model definition from framework-specific execution:

```
┌─────────────────────────────────────────────┐
│            MALS Architecture                 │
├─────────────────────────────────────────────┤
│  ┌──────────┐    ┌────────────┐             │
│  │ Model    │───▶│ Framework  │──▶ Output   │
│  │ Extract  │    │ Adapter    │             │
│  │          │◀───│ (PennyLane,│             │
│  └──────────┘    │  Qiskit,   │             │
│                  │  TQ, etc)  │             │
│  ┌──────────┐    └────────────┘             │
│  │ Cross-   │    ┌────────────┐             │
│  │ Framework│◀───│ Validation │             │
│  │ Verifier │    │ Engine     │             │
│  └──────────┘    └────────────┘             │
└─────────────────────────────────────────────┘
```

## Core Steps

### 1. Model Extraction
Extract QML model components into framework-agnostic representation:
- **Ansatz/Architecture**: Gate sequence, parameterized rotations, entanglement topology
- **Observables**: Measurement operators, expectation value targets
- **Cost Function**: Loss landscape definition (independent of autodiff backend)
- **Data Encoding**: Feature map specification (angle, amplitude, basis encoding)

### 2. Framework Adapter Selection
Map extracted model to target framework:
- **PennyLane**: Use `qml.qnode` with appropriate device backend
- **Qiskit**: Use `Estimator` primitive with `QuantumCircuit`
- **Qulacs**: Use `Observable` + `GeneralQuantumSimulator`
- **TensorFlow Quantum**: Use `tfq.layers.Expectation`

### 3. Cross-Framework Validation
Verify implementation correctness:
- Run identical inputs through all target frameworks
- Compare expectation values within numerical tolerance (1e-6)
- Validate gradient consistency across frameworks
- Test noise robustness under equivalent noise models

### 4. Performance Benchmarking
- Measure circuit execution time per framework
- Profile memory usage for different qubit counts
- Compare convergence rates on identical optimization tasks
- Evaluate hardware-specific compilation overhead

## Pitfalls
- **Framework-specific defaults**: Different frameworks use different default gradient methods, shot counts, and optimizer settings — always explicitly specify these
- **Gate decomposition differences**: Same logical gate may decompose differently (e.g., CNOT vs CX naming, rotation conventions)
- **Noise model incompatibility**: PennyLane's noise channels ≠ Qiskit's noise models — need explicit mapping
- **Parameter shift rule variations**: Some frameworks support analytic gradients only for specific gate types
- **Shot noise**: Frameworks handle finite-shot statistics differently; ensure identical shot counts for fair comparison

## Verification
- [ ] Model produces identical outputs (within 1e-6) across ≥2 frameworks
- [ ] Gradients match within tolerance for all parameters
- [ ] No framework-specific API calls remain in the core model definition
- [ ] Adapter layer is the only framework-dependent code
- [ ] Benchmark suite runs successfully on all target frameworks
