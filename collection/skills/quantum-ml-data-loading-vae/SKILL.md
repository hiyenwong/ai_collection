---
name: quantum-ml-data-loading-vae
description: VAE-based quantum data loading for QML. Compresses classical data into compact quantum representations. Use for quantum embedding design, autoencoder QML, dimensionality reduction for quantum circuits.
---

# Quantum ML Data Loading via VAE Framework

From arXiv:2606.26312

## Core Idea

Learn task-specific quantum embeddings using variational quantum autoencoder:
1. Classical encoder learns latent representation
2. Quantum encoder maps latent to n-qubit state
3. Circuit-centric classifier operates on compressed state
4. Quantum decoder reconstructs from polynomial measurements

## Key Results

- ImageNet -> 13-qubit representation (reconstructable)
- MNIST 3v5: 98.5% accuracy (classical NN: 99.7%, amplitude embedding: <68%)
- Validated on IBM hardware with real noise

## Training Protocol

1. Train classical autoencoder first
2. Quantize latent to match quantum circuit dimension
3. Train quantum encoder VQC
4. Train quantum decoder VQC
5. Joint fine-tuning

## Advantages vs Traditional Embeddings

- Amplitude: needs full tomography (exponential)
- Angle: needs circuit inversion (restrictive)
- VAE: polynomial measurements via learned decoder

## Implementation

- Affine feature maps + variational circuits
- Trigonometric structure -> Fourier approximation
- O(n^-1/2) L2 convergence rate proven
- Stable on real quantum hardware noise