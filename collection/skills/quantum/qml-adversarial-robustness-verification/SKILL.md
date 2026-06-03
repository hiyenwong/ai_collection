---
name: qml-adversarial-robustness-verification
description: "Adversarial robustness verification framework for Quantum Machine Learning (QML) models. Covers fidelity-based robustness bounds, SDP optimal bounds, VeriQR tool, and physical validation on NISQ hardware. Activation: QML robustness, quantum adversarial, QML verification, VeriQR, quantum machine learning robustness, quantum adversarial robustness"
---

# QML Adversarial Robustness Verification

Framework for verifying adversarial robustness in Quantum Machine Learning (QML) models, based on arXiv:2605.29877 (Guan & Ying, 2026).

## Source Paper

- **Title**: Verifying Adversarial Robustness in Quantum Machine Learning: from theory to physical validation via a software tool
- **Authors**: Ji Guan, Mingsheng Ying
- **arXiv**: [2605.29877](https://arxiv.org/abs/2605.29877)
- **Published**: 2026-05-28
- **Categories**: quant-ph
- **Journal**: Quantum Robustness in Artificial Intelligence, Quantum Science and Technology, Springer Nature Switzerland, 2026

## Core Concepts

### 1. Fidelity-Based Robustness Lower Bound

QML models are vulnerable to small input perturbations (adversarial attacks) similar to classical neural networks. The fidelity-based robustness lower bound is computed directly from the measurement outcome distribution:

$$R_{fidelity} = 1 - \sqrt{1 - F(\rho_{clean}, \rho_{perturbed})^2}$$

Where $F$ is the quantum state fidelity between clean and perturbed inputs.

**Key insight**: The bound is estimable on real NISQ hardware without full tomography — only measurement outcome distributions needed.

### 2. SDP Optimal Bound

When full knowledge of the QML model is available, the optimal robustness bound can be computed via Semidefinite Programming (SDP):

- Formulate robustness verification as an SDP feasibility problem
- Solve for the worst-case perturbation within a given noise budget
- The optimal bound is tighter but requires full model knowledge

### 3. VeriQR Tool

VeriQR is the first dedicated QML robustness verification software tool. It implements:

1. **Formal verification framework** — mathematically certified bounds
2. **Empirical estimation** — on real quantum devices
3. **Scalable evaluation** — works on 20+ qubit superconducting processors

### 4. Physical Validation

First experimental benchmark of quantum adversarial robustness on a **20-qubit superconducting processor**. Bridges the gap between theoretical robustness bounds and actual hardware performance.

## Application Patterns

### Pattern 1: Quick Fidelity-Based Check

```python
# When you need a fast robustness estimate on hardware:
# 1. Run QML model on clean input → get measurement distribution P_clean
# 2. Run QML model on perturbed input → get P_perturbed
# 3. Compute fidelity F(P_clean, P_perturbed)
# 4. Robustness lower bound = function of fidelity
# No full tomography needed — only measurement statistics
```

### Pattern 2: SDP-Based Optimal Verification

```python
# When full model knowledge is available:
# 1. Formulate QML circuit as quantum channel Φ
# 2. Define perturbation set ε (e.g., bounded input noise)
# 3. Solve SDP: max_{δ ∈ ε} ||Φ(ρ) - Φ(ρ+δ)||_1
# 4. Optimal robustness bound from dual solution
# Tighter but requires full circuit specification
```

### Pattern 3: NISQ Hardware Validation

```python
# For physical validation on real devices:
# 1. Prepare adversarial inputs using VeriQR
# 2. Execute on target quantum processor (20+ qubits)
# 3. Compare measured robustness with theoretical bounds
# 4. Account for hardware noise in the analysis
```

## When to Use

- Evaluating QML model security before deployment
- Comparing robustness of different quantum architectures
- Setting noise tolerance thresholds for quantum AI systems
- Benchmarking QML models on NISQ hardware
- Designing robust quantum classifiers

## Key Relationships to Other Skills

- **quantum-ml-robustness**: Broader QML robustness analysis — this skill provides the verification framework
- **qml-mutation-testing**: Complementary testing approach for QML models
- **noise-aware-quantum-testing**: Hardware noise considerations
- **quantum-adversarial-defense**: Defense mechanisms against adversarial attacks
- **qml-model-testing**: General QML testing methodology

## Pitfalls

- **NISQ noise vs adversarial noise**: Hardware noise can mask or amplify adversarial effects — must account for baseline error rates
- **Fidelity estimation**: Requires sufficient measurement shots for statistical significance; low shot counts produce unreliable bounds
- **SDP scalability**: Optimal SDP bounds become intractable for large circuits — use fidelity-based bounds as fallback
- **Perturbation model**: The choice of perturbation set ε critically affects the robustness bound; ensure it matches realistic threat models
