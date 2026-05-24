---
name: stream-randomness-extraction-quantum
description: >
  Stream-processing randomness extraction methodology for quantum random number generators (QRNGs)
  with security against quantum side information. Converts block-wise extractors to on-the-fly
  stream implementations using offline pre-computed pseudo-random masks and bitwise XOR, preserving
  all security guarantees while eliminating latency and buffering overheads. Supports Toeplitz,
  circulant, and modified Toeplitz matrix constructions. Use when: implementing real-time QRNGs,
  designing low-latency quantum key distribution systems, optimizing randomness extraction for
  high-throughput quantum cryptographic systems, or building post-quantum secure random sources.
  Activation: quantum randomness extraction, QRNG stream processing, Toeplitz hashing, quantum
  side information, real-time random number generation, universal hashing, quantum cryptography,
  post-quantum randomness.
---

# Stream Randomness Extraction against Quantum Side Information

Methodology from arXiv:2605.09556 — "Stream randomness extraction against quantum side information" (Luan et al., 2026).

## Core Innovation

Convert block-wise randomness extractors to **stream implementations** that process data on-the-fly
using a simple bitwise XOR with an offline pre-computed mask:

```
stream_output[i] = raw_data[i] XOR precomputed_mask[i]
```

This eliminates the latency and buffering overhead of block-wise post-processing while
**strictly preserving** the security guarantees against quantum side information.

## Transformation Process

### Step 1: Offline Pre-processing
- Generate pseudo-random mask from the extractor's random hash function
- This is the computationally intensive stage — done once, offline

### Step 2: Online Stream Processing
- Raw quantum measurement data arrives continuously
- Each bit processed immediately via XOR with mask
- No buffering, no accumulation, no waiting

### Step 3: Security Preservation
- The stream implementation is mathematically proven to preserve all security guarantees
- Security against quantum side information holds identically to block-wise version

## Supported Constructions

### 1. Standard Toeplitz Matrix
- Toeplitz matrix H: H[i,j] = t[i-j] (constant along diagonals)
- Pre-compute mask = H × seed
- Stream: output = raw XOR mask

### 2. Circulant Matrix
- Circulant matrix: each row is cyclic shift of previous
- Exploits FFT structure for efficient mask generation
- Stream: same XOR pattern

### 3. Modified Toeplitz Matrix
- Optimized variant with better finite-size performance
- Mask pre-computation accounts for structural modifications
- Stream: identical XOR interface

## Performance Benefits

- **Latency**: O(1) per bit vs O(n log n) or O(n²) for block-wise
- **Buffering**: Zero buffer needed vs full block accumulation
- **Throughput**: Limited only by XOR speed — can keep up with any QRNG
- **Memory**: Mask can be generated incrementally if storage is constrained

## When to Apply

- Real-time quantum key distribution (QKD) systems
- High-throughput QRNGs where buffering is impractical
- Embedded quantum cryptography with limited memory
- Low-latency quantum random number generation pipelines
- Any system requiring continuous randomness output

## Security Considerations

- Security proof assumes universal₂ or almost-dual-universal₂ hash family
- Quantum side information model: adversary holds quantum state correlated with raw data
- Smooth min-entropy bounds apply identically to stream and block versions
- Finite-size effects must be accounted for in security parameter selection