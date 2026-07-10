---
name: tensor-network-quantum-federated
description: >
  Privacy-aware federated learning combining tensor-network compression with
  quantum-enhanced processing for medical diagnosis. Use when building multi-institutional
  medical AI systems that need: (1) MPC-secured aggregation, (2) small-qubit quantum
  processing on compressed features, (3) tensor-network frontends (MPS/TTN/MERA).
  Addresses the dual challenge of communication overhead and qubit limitations.
---

# Tensor-Network Quantum Federated Learning

## Architecture Overview

```
[Client A] ── MPS/TTN/MERA ──┐
[Client B] ── MPS/TTN/MERA ──┤ → MPC Aggregation → QEP → Diagnosis
[Client C] ── MPS/TTN/MERA ──┘
```

## Three-Layer Design

### Layer 1: Tensor-Network Frontend (Client-Side)
Compresses high-dimensional medical images into compact latent representations.

| Frontend | Compression | Best For |
|----------|-------------|----------|
| MPS | Linear scaling | 1D sequences, time-series |
| TTN | Logarithmic scaling | 2D images (recommended) |
| MERA | Multi-scale | Hierarchical features |

**Key insight**: TTN+QEP combination shows the most balanced overall profile.

### Layer 2: MPC-Secured Aggregation (Server-Side)
- Multi-party computation protects aggregated latents
- Communication cost ∝ latent dimension (not original image size)
- Tensor-network compression directly reduces MPC overhead

### Layer 3: Quantum-Enhanced Processor (Post-Aggregation)
- Quantum-state embedding of aggregated latents
- Observable-based readout for classification
- Stable when qubit count ≈ latent dimension
- Degrades under noise vs. noiseless simulation

## Design Principles

### Co-Design Requirement
Representation compression, quantum refinement, and privacy deployment must be optimized **jointly**, not independently.

### Qubit-Latent Matching
QEP stability requires qubit count sufficiently matched to latent dimension:
- Too few qubits → information bottleneck
- Too many qubits → noise amplification on NISQ devices

### Dual Role of Compression
Tensor-network compression serves two purposes:
1. Enables small-qubit quantum processing
2. Reduces MPC communication overhead

## Implementation Checklist

1. Choose tensor-network frontend based on data modality
2. Set latent dimension to match available qubit count
3. Configure MPC protocol for chosen latent dimension
4. Train QEP with noise models matching target hardware
5. Validate end-to-end on PneumoniaMNIST or similar benchmark

## Performance Notes

- QEP effect is **frontend-dependent**, not uniform across architectures
- Noisy conditions degrade QEP performance relative to noiseless
- TTN frontend recommended as starting point for medical imaging
- Communication cost governed by latent dimension, not original data size

## Related Papers in Knowledge Graph

- ID 250: Quantum-Enhanced Processing with Tensor-Network Frontends
- ID 260: Adaptive Hybrid Quantum-Classical Feature Fusion
- ID 261: QML for Medical Image Classification Review
