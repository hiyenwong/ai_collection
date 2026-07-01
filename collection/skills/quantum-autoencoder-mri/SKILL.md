---
name: quantum-autoencoder-mri
description: "Compression-driven anomaly detection in brain MRI using Quantum Autoencoders (QAE). Uses angle encoding + variational encoder-decoder with trash qubits. Achieves slice-level ROC-AUC ~0.95, produces spatially localized anomaly heatmaps. Key insight: structured encoder compression (not decoder expressivity) drives detection. Use when: quantum anomaly detection in medical imaging, interpretable quantum ML, MRI tumor detection, compression-based outlier detection."
---

## Core Methodology

### Quantum Autoencoder Architecture

The QAE maps classical image patches to quantum states via angle encoding, then compresses through a variational encoder-decoder circuit:

```
Image Patches → Angle Encoding → Variational Encoder → [Kept Qubits | Trash Qubits] → Variational Decoder → Reconstruction
```

**Trash Qubits**: The encoder is trained to discard information into auxiliary "trash" qubits. Normal data compresses well (low trash information); anomalies resist compression (high trash information).

### Anomaly Detection Principle

**Compression-Driven Detection**: Anomaly scores reflect the degree to which inputs resist compression relative to the learned normal data manifold. Higher compression resistance = higher anomaly score.

**Key Finding**: Effective anomaly detection arises from **structured information compression within the encoder** rather than increased parameter magnitude or decoder expressivity. This creates a controlled compression-reconstruction trade-off with a clear operating regime for principled threshold selection.

### Encoding Strategy

**Angle Encoding**: Maps pixel intensity values to rotation angles of qubits. For an n-pixel patch, each pixel maps to an angle θ_i = π * pixel_value / max_value, applied as RY(θ_i) rotation.

### Performance Results

| Metric | QAE | Classical AE | PCA |
|--------|-----|-------------|-----|
| Slice-level ROC-AUC | ~0.95 | ~0.89 | ~0.82 |
| Patch-level ROC-AUC | ~0.813 | ~0.75 | ~0.71 |

### Key Advantages

1. **Interpretability**: QAE produces spatially localized anomaly heatmaps aligned with tumorous regions
2. **Controllability**: Clear compression-reconstruction trade-off enables principled threshold selection
3. **Encoder-Decoder Asymmetry**: Analysis reveals the encoder's structured compression is the key driver, not decoder expressivity

### Implementation Pattern

```
1. Preprocess: Extract overlapping patches from MRI slices
2. Encode: Map each patch to quantum state via angle encoding
3. Train: Variational encoder-decoder minimizing reconstruction loss
   - Loss = ⟨trash_qubits⟩ (fidelity of discarded information)
   - Normal data → low trash; Anomalous data → high trash
4. Score: Anomaly score = 1 - reconstruction_fidelity
5. Threshold: Use ROC analysis for principled threshold selection
6. Visualize: Map anomaly scores back to spatial heatmaps
```

### When to Use

- Quantum anomaly detection in medical imaging workflows
- Interpretable ML where spatial localization matters
- Scenarios requiring controlled false-positive rates
- Compression-based outlier detection with principled thresholds

### References

- Ganguly, Liang, Makris (2026): "Compression-Driven Anomaly Detection in Brain MRI Using an Interpretable Quantum Autoencoder" (arXiv:2606.27411)
