---
name: quantum-autoencoder-mri-anomaly
description: "Quantum autoencoder (QAE) for compression-driven anomaly detection in brain MRI. Uses angle encoding, variational encoder-decoder with trash qubits, and incompressibility-based anomaly scoring. Achieves ROC-AUC ~0.95 slice-level and ~0.813 patch-level with spatially localized anomaly heatmaps. Use when: quantum anomaly detection, brain MRI analysis, quantum autoencoder design, compression-based medical diagnostics, trash qubit encoding, variational quantum encoders."
metadata:
  arxiv_id: "2606.27411"
  published: "2026-06-25"
  authors: "Santanu Ganguly, Xing Liang, Dimitrios Makris"
  tags: [quantum-autoencoder, brain-MRI, anomaly-detection, medical-imaging, compression, trash-qubits]
---

# Quantum Autoencoder for Brain MRI Anomaly Detection

## Core Concept

Anomaly detection in brain MRI using a quantum autoencoder trained to compress normal data. Anomalies (tumors, lesions) are identified by their resistance to compression relative to the learned normal manifold — higher compression resistance = higher anomaly score.

## Architecture

### Encoding
- **Angle encoding**: Maps image patches into quantum states via rotational angles
- **Patch-based processing**: Operates on image patches rather than full volumes

### Variational Encoder-Decoder
- **Encoder**: Variational circuit compressing input into latent quantum state
- **Trash qubits**: Auxiliary qubits explicitly trained to discard information
- **Decoder**: Reconstructs from compressed latent representation

### Anomaly Scoring
- Anomaly score = degree of input resistance to compression
- Normal data: High compression, low reconstruction error
- Anomalous data: Low compression (resists learned manifold), high reconstruction error

## Key Findings

| Metric | Value |
|--------|-------|
| Slice-level ROC-AUC | ~0.95 |
| Patch-level ROC-AUC | ~0.813 |
| Baselines outperformed | Classical autoencoder, PCA |

### Encoder-Decoder Asymmetry
- Effective anomaly detection arises from **structured information compression within the encoder**
- NOT from increased parameter magnitude or decoder expressivity
- Results in controlled compression-reconstruction trade-off with clear operating regime for principled threshold selection

### Spatial Localization
- QAE produces **spatially localized anomaly heatmaps** aligned with tumorous regions
- Enables interpretable anomaly detection beyond binary classification

## Implementation Pattern

```python
# Conceptual architecture
class QuantumAnomalyDetector:
    def __init__(self, n_qubits, n_trash):
        self.encoder = VariationalQuantumCircuit(n_qubits)
        self.decoder = VariationalQuantumCircuit(n_qubits - n_trash)
        self.n_trash = n_trash  # auxiliary qubits for discarding info
    
    def anomaly_score(self, patch):
        """Higher score = more anomalous"""
        encoded = self.encode_angle(patch)
        compressed = self.encoder(encoded)
        trash_state = compressed[:self.n_trash]  # discarded information
        reconstructed = self.decoder(compressed[self.n_trash:])
        return reconstruction_error(patch, reconstructed)
    
    def encode_angle(self, patch):
        # Map pixel values to rotation angles
        angles = normalize(patch) * pi
        return prepare_rotated_state(angles)
```

## Compression-Reconstruction Trade-off

The QAE operates in a distinct regime where:
- **Compression**: Encoder actively discards information to trash qubits
- **Reconstruction**: Decoder must work with compressed representation
- **Anomaly detection**: Inputs outside the learned normal manifold resist compression, yielding higher reconstruction errors

This provides a **principled threshold selection** mechanism based on the operating regime boundary.

## Applications

- Brain tumor detection and localization
- Anomaly detection in medical imaging workflows
- Decision support for radiologists
- Studying compression dynamics in quantum machine learning

## Pitfalls

- **Patch-level vs slice-level performance**: Patch-level ROC-AUC (~0.813) lower than slice-level (~0.95) — patch granularity introduces more false positives
- **DICOM dataset specificity**: Evaluated on publicly available brain MRI DICOM datasets — generalization to other modalities requires retraining
- **Quantum hardware constraints**: Current results from simulation; actual quantum hardware may show different performance due to noise
- **Threshold calibration**: Anomaly score thresholds must be calibrated per dataset — no universal threshold

## Activation Keywords

- quantum autoencoder, brain MRI anomaly detection, compression-driven diagnosis, trash qubit encoding, variational quantum encoder-decoder, quantum medical imaging, anomaly heatmap, incompressibility-based detection, angle encoding quantum, DICOM quantum analysis
