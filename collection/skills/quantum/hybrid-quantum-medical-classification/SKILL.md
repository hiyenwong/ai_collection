---
name: hybrid-quantum-medical-classification
description: >
  Hybrid quantum-classical architectures for medical image classification.
  Use when building diagnostic models that combine quantum circuits (variational,
  parameterized) with classical backbones (ResNet, CNN) for tasks like breast cancer
  detection, pneumonia classification, or cardiac disease prediction. Covers feature
  fusion strategies (Static/Dynamic/Temperature-Scaled), tensor-network compression
  (MPS/TTN/MERA), and privacy-aware federated quantum refinement.
---

# Hybrid Quantum Medical Classification

## Core Architecture Pattern

```
Classical Backbone → Feature Extractor → Quantum Circuit → Measurement → Classifier
```

### Key Components

1. **Classical Branch**: ResNet/CNN for initial feature extraction
2. **Quantum Branch**: 4-qubit variational circuit with strongly entangling layers
3. **Feature Fusion**: Three progressive strategies (see below)
4. **Readout**: Observable-based measurement → classical classification head

## Feature Fusion Strategies

### 1. Static Hybrid Fusion (SHF)
- Offline extraction: classical features frozen, quantum features computed separately
- Simple concatenation before final classifier
- Best for: quick prototyping, limited compute

### 2. Dynamic Hybrid Fusion (DHF)
- End-to-end co-adaptation: both branches trained jointly
- Gradient flows through both classical and quantum paths
- Best for: maximum performance when compute allows

### 3. Temperature-Scaled Hybrid Fusion (TSHF) ⭐ Recommended
- Learnable scalar balances hybrid gradient dynamics
- Resolves optimization bottlenecks from quantum-classical asymmetry
- Achieved: 87.82% accuracy, 91.77% F1, 89.08% AUC-ROC on BreastMNIST
- Best for: clinical deployment, stable training

## Quantum Circuit Design

```python
# 4-qubit variational circuit pattern
# - Amplitude encoding for compressed features
# - Strongly entangling layers (CZ + RX/RY/RZ)
# - Observable-based readout (Pauli-Z expectations)
```

### Encoding Guidelines
- Use amplitude encoding when feature dim ≤ 2^n (n = qubit count)
- For higher dimensions, apply tensor-network compression first (TTN recommended)
- Angle encoding for tabular clinical data

## Privacy-Aware Federated Pattern

For multi-institutional medical AI:

1. **Client-side**: Tensor-network frontend (MPS/TTN/MERA) compresses local data
2. **Server**: MPC-secured aggregation of compressed latents
3. **Post-aggregation**: Quantum-Enhanced Processor refines aggregated features
4. **Result**: TTN+QEP combination shows most balanced performance

## Datasets & Benchmarks

| Dataset | Task | Best Approach | Key Metric |
|---------|------|---------------|------------|
| BreastMNIST | Cancer classification | ResNet + TSHF + trainable QC | 87.82% acc |
| PneumoniaMNIST | Pneumonia detection | TTN + QEP | Balanced profile |
| CHD datasets | Heart disease | Ensemble QML classifiers | Higher F1 than classical |
| MedMNIST v2 | Multi-task | HQCNN (5-layer CNN + 4-qubit VQC) | Competitive |

## Error Handling

### Optimization Instability
- **Symptom**: Quantum gradients oscillate, classical converges
- **Fix**: Apply TSHF with learnable temperature scalar
- **Fallback**: Switch to SHF (static fusion) for stable baseline

### Qubit-Latent Mismatch
- **Symptom**: QEP performance degrades under noise
- **Fix**: Ensure qubit count matches latent dimension
- **Fallback**: Use classical-only when noise > threshold

### Communication Overhead (Federated)
- **Symptom**: MPC aggregation too slow
- **Fix**: Tensor-network compression reduces latent dimension
- **Fallback**: Switch to non-MPC aggregation with differential privacy

## Performance Expectations

- Current quantum advantage is demonstrated via **classical simulation**
- NISQ-era devices: expect noise to degrade vs. noiseless simulation
- Hybrid approaches consistently outperform pure classical baselines in accuracy
- Parameter efficiency: quantum circuits reduce trainable parameters by 10-100x

## Related Papers in Knowledge Graph

- ID 260: Adaptive Hybrid Quantum-Classical Feature Fusion (TSHF strategy)
- ID 261: QML for Medical Image Classification (comprehensive review)
- ID 262: Hybrid QML for Coronary Heart Disease detection
- ID 250: Quantum-Enhanced Privacy-Aware Federated Medical Diagnosis
- ID 251: Hybrid QNN for Breast Cancer Thermographic Classification
