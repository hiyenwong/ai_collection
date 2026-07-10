---
name: hybrid-qml-pipeline-design
description: >
  Design and evaluate hybrid quantum-classical machine learning pipelines.
  Covers NISQ-era variational quantum algorithms (VQAs), noise-aware pipeline design,
  correlation-guided quantum circuit construction, and classical-quantum benchmarking frameworks.
  Use when: designing QML systems, evaluating quantum vs classical ML tradeoffs,
  building noise-robust quantum pipelines, optimizing variational quantum circuits,
  implementing quantum feature maps, or comparing hybrid vs pure classical approaches.
  Keywords: quantum machine learning, VQA, hybrid quantum-classical, NISQ, quantum neural network,
  quantum circuit design, noise robustness, quantum feature map, QAOA, QCNN, variational quantum classifier.
---

# Hybrid Quantum-Classical ML Pipeline Design

## Core Patterns

### 1. Noise-Aware Pipeline Architecture

Hybrid QML pipelines must account for noise at two levels simultaneously:

- **Classical input noise**: speckle noise, impulse noise, quantization noise, feature dropout
- **Quantum circuit noise**: depolarizing, amplitude damping, phase damping, Pauli errors, readout errors

Design rule: Evaluate classical and quantum noise together — classical noise amplifies quantum decoherence effects.

### 2. Variational Quantum Algorithm (VQA) Template

```
Classical Data → [Feature Map] → Parameterized Quantum Circuit → Measurement → Classical Optimizer → Update Parameters
```

Key components:
- **Feature Map**: ZZ feature map, amplitude encoding, angle encoding
- **Ansatz Design**: Hardware-efficient, problem-inspired, or trainable
- **Classical Optimizer**: Gradient-based (SPSA, parameter-shift) or gradient-free (COBYLA, Nelder-Mead)
- **Cost Function**: Problem-specific objective with barren plateau mitigation

### 3. Correlation-Guided Circuit Design

Incorporate domain-specific feature correlations into quantum circuit structure:
1. Compute pairwise correlations in classical features
2. Map correlated features to entangled qubit pairs
3. Reduce trainable parameters by leveraging known structure
4. Achieve competitive accuracy with fewer parameters than classical baselines

### 4. Compact Model Advantage

Compact quantum models (e.g., 4-qubit QCNN) often outperform larger models due to:
- Better trainability (fewer barren plateau risks)
- Encoding efficiency matters more than model scaling
- Lower variance and faster convergence

## Pipeline Design Steps

### Step 1: Classical Preprocessing
- Clean and normalize classical data
- Apply noise augmentation for robustness testing
- Feature selection guided by domain correlations

### Step 2: Quantum Encoding Selection
| Encoding | Best For | Qubit Cost |
|----------|----------|------------|
| ZZ Feature Map | Structured data with correlations | O(n) |
| Amplitude Encoding | High-dimensional dense vectors | O(log n) |
| Angle Encoding | Normalized features | O(n) |

### Step 3: Ansatz Design
- Start with hardware-efficient ansatz for NISQ devices
- Use correlation-guided entanglement for structured problems
- Consider problem-inspired ansatz for domain-specific tasks

### Step 4: Noise Simulation
Use Qiskit Aer or TensorCircuit-NG to simulate:
- Depolarizing noise with realistic error rates
- Amplitude/phase damping matching target hardware
- Combined classical + quantum noise for realistic evaluation

### Step 5: Benchmarking
Compare against:
- Classical baseline (same parameter count)
- Quantum-only model
- Hybrid architectures (quantum-classical layers)
- Measure: accuracy, training stability, parameter efficiency, convergence speed

## Key Frameworks

- **TensorCircuit-NG**: Unified tensor-native platform for quantum circuits + tensor networks + neural networks (JAX/TF/PyTorch backends)
- **Qiskit Aer**: Hardware-inspired noise simulation
- **openQSE**: Reference architecture for quantum-HPC software stacks

## Pitfalls

- **Barren Plateaus**: Gradients vanish exponentially with qubit count. Mitigate with: layered ansatz, local cost functions, pre-training
- **Classical-Quantum Noise Synergy**: Classical input noise significantly amplifies quantum decoherence. Test both simultaneously.
- **Over-Scaling**: Larger quantum models don't always perform better. Compact models often win on trainability.
- **Encoding Sensitivity**: Performance heavily depends on encoding choice. Test multiple encodings before committing.
- **NISQ Limitations**: Current hardware limits qubit count and circuit depth. Design for 4-20 qubits with shallow circuits.

## Verification

1. Run noise-free simulation as upper bound
2. Add classical noise alone, measure degradation
3. Add quantum noise alone, measure degradation
4. Combine both noise types, verify non-linear amplification
5. Compare compact vs scaled model on same problem
6. Validate against classical baseline with matched parameter count
