---
name: sparse-mamba-decoder-qec
description: "Sparse Mamba Decoder (SMD) for quantum error correction — a defect-centric neural decoder using Mamba state-space model that processes only active detection events (k ≪ d²R) achieving O(k) complexity on surface codes. 95-467x faster than Tesseract near-MLD decoder."
version: 1.0.0
author: Hermes Agent (Cron Job)
license: MIT
---

# Sparse Mamba Decoder (SMD) for Quantum Error Correction

**arXiv: 2605.17156 (May 2026)**
**Authors: Samira Sayedsalehi, Nader Bagherzadeh, Maxim Shcherbakov, Jean-Luc Gaudiot**

## Overview

The Sparse Mamba Decoder (SMD) is a defect-centric neural decoder for surface-code quantum error correction. Unlike existing neural decoders that process the full dense syndrome array (O(d²R) complexity), SMD processes only the k active detection events using a Mamba state-space backbone, achieving O(k) complexity.

### Key Innovation

At physically relevant error rates (p ~ 0.1%), fewer than 5% of syndrome entries contain active detection events. SMD exploits this sparsity by encoding each defect with a 13-dimensional feature representation and processing them through a Mamba (structured state-space) model, enabling nearly constant latency across code distances.

## Core Methodology

### 1. Defect-Centric Processing

- Instead of processing the full d²R syndrome volume, SMD identifies only active detection events
- Each active event is encoded as a 13-dimensional feature vector (spatial position, round, neighbors, etc.)
- Number of active events k ≪ d²R at low error rates

### 2. Mamba State-Space Backbone

- Uses the Mamba architecture (SSM-based, linear complexity in sequence length)
- Processes the variable-length sequence of defect features
- Outputs correction predictions

### 3. SMD Ensemble

- Multiple SMD decoders can be combined in an ensemble for improved accuracy
- On Sycamore experimental data, matches or slightly surpasses dense Mamba decoder accuracy

## Key Results

| Metric | Performance |
|--------|-------------|
| **Complexity** | O(k), where k = active detection events |
| **Accuracy** | Up to 49% MWPM logical error rate reduction at d ≤ 5 (SI1000) |
| **Speed vs Tesseract** | 95-467× faster |
| **Speed vs Belief Matching** | 232-463× faster |
| **Latency** | 24-57 μs nearly constant across d = 3-9 (circuit-level noise) |
| **Parameters** | 7.5M-16M parameters |
| **Hardware** | Commodity NVIDIA GPUs, no specialized accelerators |

### Benchmarks

- **Depolarizing noise**
- **Uniform circuit-level noise**
- **SI1000** (Sycamore-inspired noise model)
- **Google Sycamore experimental dataset**

## When to Use

- You need real-time or near-real-time QEC decoding at scale
- You want a neural decoder that scales to large code distances
- You need low-latency decoding for feedback in QEC cycles
- You're working with surface codes and want to leverage syndrome sparsity
- You want to explore Mamba/SSM architectures for physics tasks

## Implementation Considerations

- Requires NVIDIA GPU for inference
- Implemented in PyTorch with 7.5M-16M parameters
- Mamba backbone can use the official Mamba implementation or custom SSM
- Defect encoding is critical: 13D feature vector encodes spatial + temporal + neighborhood info
- Ensemble decoding improves accuracy but increases compute proportionally

## Comparison with Other Decoders

| Decoder | Type | Complexity | Latency |
|---------|------|-----------|---------|
| **SMD (this work)** | Neural (Mamba) | O(k) | 24-57 μs |
| MWPM | Classical | O(n³) | High |
| Tesseract | Near-MLD | High | 95-467× slower |
| Belief Matching | Classical BP | O(n²) | 232-463× slower |
| Dense Neural | Neural (CNN/Transformer) | O(d²R) | Moderate |

## Activation

**Keywords**: Sparse Mamba Decoder, SMD, quantum error correction, surface code, defect-centric decoding, state-space model, Mamba, QEC neural decoder, syndrome sparsity, real-time QEC, fault-tolerant quantum computing

## References

- arXiv:2605.17156 — SMD original paper
- arXiv:2406.11082 — Mamba: Linear-Time Sequence Modeling with Selective State Spaces
- arXiv:2403.07888 — Dense Mamba decoder for QEC (Varbanov et al.)
- arXiv:2303.07205 — Surface code MWPM decoding
- arXiv:2207.06454 — Tensor network decoders
- arXiv:2406.03460 — Tesseract near-MLD decoder
