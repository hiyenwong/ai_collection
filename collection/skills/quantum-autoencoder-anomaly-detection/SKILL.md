---
name: quantum-autoencoder-anomaly-detection
description: Quantum autoencoder (QAE) for compression-driven anomaly detection in medical imaging using trash qubits and encoder-decoder asymmetry (arXiv:2606.27411)
category: quantum-medical
---

# Quantum Autoencoder for Compression-Driven Anomaly Detection

Methodology from arXiv:2606.27411 (June 2026). Quantum autoencoder for anomaly detection in brain MRI data.

## Core Pattern

QAE leverages **angle encoding** to map image patches into quantum states, followed by a **variational encoder-decoder architecture** trained to discard information via **auxiliary trash qubits**. Anomaly scores reflect the degree to which inputs resist compression relative to normal data — higher scores = deviations from the learned normal manifold.

## Key Findings

- **Slice-level ROC-AUC ~0.95**, patch-level ROC-AUC ~0.813 — outperforms classical autoencoder and PCA baselines
- **Encoder-decoder asymmetry**: effective anomaly detection arises from structured information compression within the encoder, not increased parameter magnitude or decoder expressivity
- Produces **spatially localized anomaly heatmaps** aligned with tumorous regions
- Controlled **compression-reconstruction trade-off** with clear operating regime for principled threshold selection

## Implementation Steps

1. Encode image patches into quantum states via angle encoding
2. Train variational encoder-decoder with trash qubits to discard redundant information
3. Compute anomaly scores as compression resistance relative to normal data manifold
4. Apply threshold from compression-reconstruction trade-off curve
5. Generate spatially localized anomaly heatmaps from reconstruction residuals

## When to Use

- Anomaly detection in medical imaging (MRI, CT, etc.)
- Scenarios needing interpretable anomaly localization
- Cases where quantum advantage may arise from structured compression
- Quality control and outlier detection in imaging pipelines

## References

- arXiv: 2606.27411v1
- Authors: Santanu Ganguly, Xing Liang, Dimitrios Makris
