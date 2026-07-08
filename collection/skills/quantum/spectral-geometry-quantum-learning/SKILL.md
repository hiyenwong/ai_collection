---
name: spectral-geometry-quantum-learning
description: "Spectral geometry framework for diagnosing quantum learning systems using bosonic-Bloch probes. Links learned spectral partitions to two-boson interference signatures, Bloch-space drift for anomaly detection, and quantum Fisher information geometry. Activation: spectral geometry quantum learning, bosonic interference probe, Bloch-space drift, quantum autoencoder diagnostics, quantum Fisher information geometry, 谱几何量子学习"
metadata:
  arxiv_id: "2607.00063"
  published: "2026-06-30"
  authors: "Spectral Geometry quantum learning authors"
  tags: [quantum, machine-learning, spectral-geometry, bosonic, bloch-probe, anomaly-detection]
---

# Spectral Geometry in Quantum Learning

## Core Methodology

**Problem**: How to diagnose and understand what quantum learning models actually learn — beyond accuracy metrics.

**Solution**: Unified spectral-geometric framework using physically grounded probes:

### 1. Spectral Dimension Shift
- Graph-regularized quantum networks reorganize output similarity graph during training
- Effective spectral dimension increases (ΔS = +0.23)
- Laplacian spectrum reshapes — learning creates geometric structure

### 2. Bosonic Interference Probes
- Edge-resolved two-boson interference probes spectral restructuring
- Bosonic enhancement ΔP_uv correlates with Fiedler edge split |Δv₂| (r = -0.50)
- Links learned spectral partitions to measurable interference signatures

### 3. Bloch-Space Drift
- Geometric diagnostic of hybrid quantum autoencoder latent representations
- Absolute Bloch drift discriminates anomalies (ROC-AUC ≥ 0.9)
- Consecutive drift is near random (ROC-AUC ≈ 0.5) — detection from persistent displacement
- With unsupervised benign threshold: ROC-AUC ≈ 0.99, negligible false negatives

### 4. Phase Diagram
- Nonmonotonic dependence on coupling strength γ and noise δ
- Graph regularization improves fidelity only in restricted regime
- Hardware experiments confirm predicted interference within shot-noise

## Usage Patterns

### Pattern 1: Spectral Diagnosis of QML Models
When analyzing what a quantum neural network learns:
1. Compute output similarity graph from trained model
2. Measure effective spectral dimension ΔS
3. Track Laplacian spectrum evolution during training
4. Compare pre/post training spectral structure

### Pattern 2. Bosonic Interference Validation
When validating learned structure on quantum hardware:
1. Run edge-resolved two-boson interference experiments
2. Measure bosonic enhancement ΔP_uv per edge
3. Correlate with Fiedler vector components from spectral analysis
4. Confirm within shot-noise uncertainty

### Pattern 3. Bloch-Space Anomaly Detection
When using quantum autoencoders for anomaly detection:
1. Track Bloch vector drift in latent space
2. Use absolute Bloch drift as anomaly score (not consecutive drift)
3. Set unsupervised threshold on benign data distribution
4. Achieves ROC-AUC ≈ 0.99 with negligible false negatives

## Activation Keywords
- spectral geometry quantum learning
- bosonic interference probe
- Bloch-space drift
- quantum autoencoder anomaly detection
- quantum Fisher information geometry
- graph-regularized quantum networks
- quantum learning diagnostics
- 谱几何量子学习
- 量子学习诊断

## Related Skills
- `spectral-anatomy-quantum-kernels` — spectral analysis of quantum kernels
- `effective-rank-qnn-expressivity` — QNN expressivity measurement
- `qml-expressivity-trainability` — QML expressivity-trainability analysis
- `quantum-autoencoder-anomaly-detection` — QAE anomaly detection
- `coherence-law-noisy-equivariant-qnn` — QML trainability under noise
