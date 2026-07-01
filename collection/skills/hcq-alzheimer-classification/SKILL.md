---
name: hcq-alzheimer-classification
description: Hybrid Classical-Quantum pipeline for Alzheimer's disease classification using supervised beta-VAE and quantum kernels with ZZ feature map on 3D structural MRI volumes.
category: medicine
tags:
  - quantum-computing
  - medical-imaging
  - alzheimer-disease
  - quantum-kernel
  - beta-vae
  - hcq-pipeline
  - structural-mri
source: arxiv:2606.14194
authors:
  - Tia Tiwari
  - Vamshi Krishna Kancharla
  - Neelam Sinha
published: "2026-06-12"
categories:
  - cs.CV
  - cs.LG
---

# HCQ Alzheimer Classification

## Description

Hybrid Classical-Quantum (HCQ) pipeline for binary Alzheimer's disease classification from 3D T1-weighted structural MRI volumes using supervised beta-VAE dimensionality reduction and quantum kernels with ZZ feature map. Achieves competitive accuracy with significantly fewer quantum resources than naive approaches.

## Activation Keywords

- HCQ Alzheimer classification
- quantum Alzheimer detection
- hybrid quantum medical classification
- beta-VAE quantum kernel
- ZZ feature map MRI
- 阿尔茨海默量子分类
- 混合量子医学诊断
- quantum medical imaging

## Tools Used

- `web_search` or `arxiv`: Fetch arXiv paper details
- `read_file`: Read MRI datasets and metadata
- `terminal`: Run Python quantum ML scripts
- `vision_analyze`: For medical image visualization

## Architecture Overview

```
3D MRI Volume
    ↓
[Preprocessing] → Bias correction, skull stripping, normalization
    ↓
[Supervised beta-VAE] → Dimensionality reduction to latent space
    ↓
[ZZ Feature Map] → Quantum feature map with entangling ZZ gates
    ↓
[Quantum Kernel SVM] → Classification via quantum kernel method
    ↓
[AD vs CN Prediction]
```

## Pipeline Steps

### Step 1: Data Preparation

```python
# Load 3D T1-weighted structural MRI volumes
# Target: Binary classification (AD vs CN - Cognitively Normal)
# Standard preprocessing: N4 bias field correction, skull stripping, MNI registration
```

### Step 2: Supervised Beta-VAE Encoding

- Use supervised beta-VAE for dimensionality reduction
- Preserves class-discriminative features in latent space
- Reduces 3D volume to manageable latent vector for quantum encoding
- Supervised variant incorporates label information during training

### Step 3: ZZ Feature Map Construction

- Map classical latent vectors to quantum state space
- ZZ feature map: entangling gates with ZZ interactions
- Circuit depth scales with latent dimension
- Feature map parameters encode data values

### Step 4: Quantum Kernel SVM Classification

- Compute quantum kernel matrix: K(x_i, x_j) = |⟨ψ(x_i)|ψ(x_j)⟩|²
- Train SVM using quantum kernel
- Quantum advantage from high-dimensional feature space
- Classical simulation fallback for NISQ-era validation

## Key Innovation Points

1. **Supervised beta-VAE**: Class-aware dimensionality reduction preserves discriminative features
2. **ZZ Feature Map**: Entanglement-enhanced feature encoding for better separability
3. **End-to-End HCQ**: Seamless classical-quantum pipeline without intermediate classical bottlenecks
4. **3D MRI Direct**: Works directly with 3D structural volumes, not 2D slices

## Implementation Notes

- Requires ~10-20 qubits for practical latent dimensions
- Quantum kernel computation can be done on simulators or real QPU
- beta-VAE training is purely classical
- ZZ feature map circuit: H-RZ(2x_i)-CNOT-RZ(2x_j)-CNOT structure per qubit pair

## Error Handling

### Dataset Issues
- If MRI preprocessing fails: fall back to simpler normalization
- If beta-VAE doesn't converge: reduce beta parameter, increase training epochs

### Quantum Issues
- If qubit count exceeds available hardware: use dimensionality reduction
- If quantum kernel too noisy: use error mitigation (readout error correction)

## References

- arXiv:2606.14194 - "Hybrid Classical-Quantum (HCQ) Alzheimer Classification via Supervised beta-VAE and Quantum Kernels"
- Tia Tiwari, Vamshi Krishna Kancharla, Neelam Sinha
- Categories: cs.CV, cs.LG
