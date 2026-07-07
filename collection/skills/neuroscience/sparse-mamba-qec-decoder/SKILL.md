---
name: sparse-mamba-qec-decoder
description: "Sparse Mamba Decoder (SMD) for quantum error correction — defect-centric neural decoder using state-space (Mamba) backbone. Processes only k active detection events (O(k) complexity) instead of full O(d²R) syndrome array. Reduces MWPM logical error rate by up to 49%, runs 95-467x faster than Tesseract near-MLD, achieves 24-57μs latency across d=3-9. Activation: sparse mamba decoder, SMD, QEC neural decoder, surface code Mamba, defect-centric decoding, sparse syndrome processing, quantum error correction state space model."
category: quantum
---

# Sparse Mamba Decoder for Quantum Error Correction

Defect-centric neural decoder for surface code syndromes using a Mamba (state-space model) backbone. Based on arXiv:2605.17156.

## Problem Statement

Quantum error correction (QEC) requires decoders that are simultaneously **accurate**, **fast**, and **scalable**.

**Existing limitation:** State-of-the-art neural decoders process the full dense syndrome array of size O(d²R) regardless of actual error rate. At physically relevant error rates (p ~ 0.1%), fewer than 5% of syndrome entries contain active detection events — yet all existing decoders process the entire syndrome volume.

## Core Innovation: Defect-Centric Sparse Processing

The Sparse Mamba Decoder (SMD) processes **only the k active detection events** using:

1. **13-dimensional feature representation per defect** — compact encoding of each detection event's spatiotemporal properties
2. **Mamba state-space backbone** — linear-complexity sequence modeling of the defect stream
3. **O(k) total complexity** — decouples from code distance d and number of measurement rounds R

### Feature Representation (13 dimensions per defect)

Each active detection event is encoded as a 13-dimensional vector capturing:
- Spatial coordinates (x, y position on the lattice)
- Temporal coordinate (measurement round)
- Syndrome type (X/Z basis indicators)
- Neighborhood context features
- Relative timing features

### Architecture

```
Input: Raw syndrome array (d × d × R)
  ↓
Detection Event Extraction (sparse)
  ↓  k active detection events
13-dim Feature Embedding (per defect)
  ↓
Mamba State-Space Backbone (linear complexity)
  ↓
Output: Correction prediction
```

## Results

| Metric | Performance |
|--------|-------------|
| Logical error rate vs MWPM (d ≤ 5, SI1000) | Up to 49% reduction |
| Speed vs Tesseract near-MLD | 95-467× faster |
| Speed vs Belief Matching | 232-463× faster |
| Latency (d = 3-9, uniform circuit-level noise) | Nearly constant 24-57 μs |
| Parameters | 7.5-16M (commodity NVIDIA GPU) |
| Sycamore experimental dataset | Ensemble matches/surpasses dense Mamba decoder |

## When to Use

- Real-time surface code decoding on quantum hardware
- Low-latency QEC for fault-tolerant quantum computing
- Scalable neural decoders with sparse syndrome input
- Paring QEC decoding complexity with physical error rates
- FPGA/ASIC implementation of neural decoders

## Design Principles

### 1. Exploit Sparsity at Source

At physically relevant error rates (p ~ 0.1%), <5% of syndrome entries are active. Processing only k active events yields O(k) complexity — a fundamental improvement over O(d²R). The sparsity is exponential at low error rates.

### 2. State-Space Models Over Transformers

Mamba's linear-complexity sequence modeling is ideal for the variable-length defect stream (k varies with error rate), avoiding the quadratic cost of self-attention.

### 3. Defect-Centric Over Dense

Unlike dense neural decoders that "see" the entire lattice, defect-centric processing focuses computation where errors actually occurred, dramatically reducing FLOPs.

### 4. Ensemble for Robustness

SMD ensemble matches or surpasses dense baselines, demonstrating that defect-centric processing does not sacrifice accuracy.

## Implementation Considerations

### Input Representation
- Extract detection events from syndrome using threshold-based or graph-based triggers
- 13-dim embedding: position (2), time (1), basis (1), neighborhood stats (4), relative timings (3), confidence (2)

### Backbone
- Mamba block: selective scan with state dimension 16-64
- 4-8 Mamba layers stacked with residual connections
- Optional: cross-attention between defects for long-range interactions

### Training
- Supervised on simulated noise data (depolarizing, circuit-level, Google Sycamore benchmarks)
- Loss: cross-entropy on correction prediction (or reinforcement learning for end-to-end)
- Data augmentation: rotate/translate lattice, vary error rate

### Hardware Targets
- Commodity NVIDIA GPU for training
- Real-time inference on FPGA/ASIC for quantum hardware integration (sub-μs latency target)

## Limitations

- Performance depends on accurate detection event extraction
- Very high error rates (p > 1%) reduce sparsity benefit
- Currently evaluated on surface codes only — generalization to other QEC codes is future work
- Training requires large simulated dataset at various noise rates

## Related Work

- **Tensor Network Decoders**: Achieve high accuracy but scale poorly
- **Transformer Decoders**: High accuracy, O(L²) attention cost
- **Dense Mamba Decoder** (Varbanov et al.): First Mamba application to QEC but processes full syndrome
- **Belief Matching**: Fastest existing decoder at time of publication
- **Tesseract near-MLD**: High accuracy but very slow

## Activation

sparse mamba decoder, SMD, QEC neural decoder, surface code Mamba, defect-centric decoding, sparse syndrome processing, quantum error correction state space model, Mamba QEC, neural QEC decoder, surface code decoder
