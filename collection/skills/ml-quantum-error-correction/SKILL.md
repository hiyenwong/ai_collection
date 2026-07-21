---
name: ml-quantum-error-correction
description: >
  Machine Learning approaches for Quantum Error Correction (QEC). Use when researching,
  designing, or implementing ML-assisted QEC systems including: (1) diffusion models for
  error decoding (DiffQEC pattern), (2) reinforcement learning for QEC control and
  calibration, (3) neural network decoders for surface codes and LDPC codes, (4) loss-biased
  fault-tolerant architectures, (5) quantum error correction for quantum machine learning (QML).
  Activation keywords: ML QEC, diffusion model quantum error, RL quantum control, neural decoder,
  quantum error correction machine learning, QEC decoder, fault-tolerant quantum computing ML,
  QML model validation, quantum mutation testing, quantum certified training, QNN robustness.
---

# ML-Assisted Quantum Error Correction

## Core Patterns

### Pattern 1: Diffusion Models for QEC Decoding (DiffQEC)

Use diffusion models to learn the noise-to-error mapping for quantum error correction.

**Workflow:**
1. Generate training data from quantum circuit simulations with realistic noise models
2. Train a diffusion model to map syndrome measurements to error configurations
3. Use the trained model as a fast decoder during QEC cycles
4. Validate logical error rate against baseline minimum-weight perfect matching (MWPM)

**Key design choices:**
- Condition diffusion on syndrome patterns (binary vectors from stabilizer measurements)
- Use classifier-free guidance to balance decoding speed vs accuracy
- Target sub-microsecond decoding for real-time QEC cycles

### Pattern 2: Reinforcement Learning for QEC Control

Use RL to adaptively control QEC parameters under environmental drift.

**Workflow:**
1. Define state as syndrome history + calibration parameters
2. Define actions as parameter adjustments (gate durations, pulse shapes, bias ratios)
3. Reward = negative logical error rate (or proxy via syndrome entropy)
4. Train with PPO or SAC on simulated quantum hardware

**Advantage over recalibration:**
- Continuous adaptation without halting computation
- Learns drift patterns specific to hardware instance
- Reduces calibration overhead by 10-100x

### Pattern 3: Loss-Biased Fault Tolerance

Exploit physical error bias (loss errors dominant over other errors) for simplified QEC.

**Workflow:**
1. Characterize error channel: identify dominant error type (e.g., atom loss in neutral atoms)
2. Design code that corrects dominant error with fewer resources
3. Use fast detection mechanism (e.g., autoionization for loss detection < 1ms)
4. Combine with standard QEC for residual errors

**Platforms where this applies:**
- Neutral atom qubits (Rydberg platforms)
- Photonic qubits (loss-dominant channel)
- Superconducting qubits with engineered dissipation

### Pattern 4: Neural Decoders for Topological Codes

Replace classical decoders (MWPM, union-find) with trained neural networks.

**Architecture patterns:**
- CNN on 2D syndrome lattice for surface codes
- Graph neural network for irregular code geometries
- Transformer for temporal syndrome sequences

**Training data:**
- Simulate Pauli noise at various physical error rates
- Generate syndrome-error pairs for supervised learning
- Augment with realistic noise models (crosstalk, leakage, SPAM errors)

## QEC for Quantum Machine Learning

When applying QEC to QML workloads:

1. **Error detection vs correction**: QML may tolerate higher error rates than universal QC
2. **Mid-circuit measurement**: QEC must not destroy quantum state used for ML inference
3. **Code choice**: CSS codes preferred for compatibility with variational circuits
4. **Overhead estimation**: Factor QEC overhead into quantum advantage calculations

**Note:** For QML model quality assurance (mutation testing, robustness analysis, certified training via IBP, hardware readiness), see [references/qml-model-validation.md](references/qml-model-validation.md). This covers validation of trained QML models, which is distinct from hardware-level error correction.

## Evaluation Metrics

| Metric | Target | Notes |
|--------|--------|-------|
| Logical error rate | < 10^-6 | Below threshold for fault tolerance |
| Decoding latency | < 1 μs | Must be faster than QEC cycle time |
| Training data size | 10^6-10^8 samples | Depends on code distance and noise model |
| Generalization | Works at unseen p_phys | Must extrapolate beyond training error rates |

## References

- DiffQEC (2604.24640): Diffusion models for versatile QEC
- Loss-biased QEC (2604.21876): Fast autoionization for sub-ms QEC cycles
- RL control of QEC (2511.08493): Adaptive calibration under drift
- QEC for QML (2601.07223): Error correction at the quantum-classical ML intersection
- Linear-time QEC codes (2603.04543): Breakthroughs in quantum LDPC decoding
