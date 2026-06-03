---
name: spiking-bandpass-wavelet-encoding
description: "Spiking Bandpass Wavelet encoding methodology for temporal signal encoding and decoding. Recasts spike encoders as time-causal wavelet frames with quantitative bandwidths and reconstruction error bounds. Maps directly to neuromorphic hardware. Applicable to spike-based encoding, temporal signal processing, neuromorphic computing, event-based sensing. Triggers: spike encoding, wavelet encoding, temporal signal processing, neuromorphic encoding, event-based signal reconstruction."
---

# Spiking Bandpass Wavelet Encoding

## Overview

Methodology from arXiv:2605.09770 (Pedersen, Lindeberg, Gerstoft, 2026-05-10) bridging spike-based encoding with classical signal processing theory.

## Core Problem

Spike-based encodings are sparse and energy-efficient, but have been formulated **probabilistically**, disconnected from most signal processing literature. This limits theoretical understanding and practical deployment.

## Key Innovation

**Reformulates spike encoders as time-causal wavelet frames** with:
- Quantitative bandwidths
- Reconstruction error bounds
- Preservation of sparsity and locality
- Direct mapping to neuromorphic hardware

## Methodology

### 1. Wavelet Frame Construction

- Construct time-causal wavelets from spike encoding principles
- Each wavelet corresponds to a bandpass filter
- Wavelets are inherently causal (no future information needed)

### 2. Reconstruction Theory

```
Signal -> Spike Encoder -> Spike Train -> Wavelet Decoder -> Reconstructed Signal
```

- Reconstruction up to spike quantization and time discretization errors
- Quantitative bounds on reconstruction error
- Normalized RMSE comparable to continuous wavelet transforms

### 3. Properties

- **Sparsity**: Maintains sparse representation of spikes
- **Locality**: Local in both time and frequency
- **Causality**: Real-time compatible, no look-ahead needed
- **Hardware Mapping**: Directly implementable on neuromorphic chips

## Applications

- ECG signal reconstruction
- Audio signal processing
- Event-based camera data
- Neuromorphic sensor processing
- Real-time temporal signal encoding

## Connection to Spiking Neural Networks

Wavelet-encoded inputs provide theoretically-grounded representations for SNNs:
- Better input encoding than heuristic methods
- Preserves temporal structure with error bounds
- Compatible with neuromorphic hardware deployment

## arXiv Reference

- **Paper**: Encoding and Decoding Temporal Signals with Spiking Bandpass Wavelets
- **ID**: 2605.09770
- **URL**: https://arxiv.org/abs/2605.09770
- **PDF**: https://arxiv.org/pdf/2605.09770v1
