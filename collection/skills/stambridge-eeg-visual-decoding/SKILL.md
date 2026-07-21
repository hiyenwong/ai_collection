---
name: stambridge-eeg-visual-decoding
description: "STAMBRIDGE: Spectral-Temporal Amplitude-aware Mid-Feature Bridge for EEG Visual Decoding. Two-stage framework combining Spectral-Temporal Amplitude-aware Modulation (STAM) and Mid-Feature Semantic Bridge (MFSB) for zero-shot EEG-to-image retrieval and reconstruction. Achieves 34.50% Top-1 on THINGS-EEG. Activation: EEG visual decoding, EEG-to-image, zero-shot EEG retrieval, spectral-temporal modulation, brain-computer interface"
---

# STAMBRIDGE: Spectral-Temporal Amplitude-aware Mid-Feature Bridge for EEG Visual Decoding

**arXiv**: [2605.23137](https://arxiv.org/abs/2605.23137) | **Date**: 2026-05-22 | **Category**: eess.IV, cs.CV

**Authors**: Jiahe Meng, Weiming Zeng, Yueyang Li, Bo Chai, Hongjie Yan, Zhiguo Zhang, Wai Ting Siok, Nizhuan Wang

**Code**: [github.com/thabeatmjh/STAMBRIDGE](https://github.com/thabeatmjh/STAMBRIDGE)

## Overview

STAMBRIDGE is a versatile **two-stage framework** for EEG visual decoding that sequentially tackles feature conditioning and cross-modal alignment. It addresses two fundamental challenges: (1) extracting robust EEG representations that preserve frequency-aware transients without introducing filtering artifacts, and (2) stabilizing cross-modal alignment between low-SNR neural signals and high-level vision-language spaces.

**Key Insight**: Hard frequency masking in existing EEG spectral modulation introduces ringing artifacts that distort short-lived neural transients. STAM replaces hard masking with amplitude-derived soft channel weighting to preserve temporal integrity.

## Core Methodology

### Stage 1: Spectral-Temporal Amplitude-aware Modulation (STAM)

Replaces hard frequency masking (used in prior work like Neural-MCRL) with:
- **Amplitude-derived soft channel weighting**: Uses spectral amplitude as soft weights for frequency bands, avoiding abrupt spectral truncation
- **Multi-scale temporal convolutions**: Captures frequency-aware transients across different timescales
- **Explicit preservation of time-domain integrity**: Reduces ringing artifacts that obscure stimulus-locked transient responses

### Stage 2: Mid-Feature Semantic Bridge (MFSB)

A model-agnostic alignment module that:
- Constructs a **regularized intermediate semantic space** through directed cross-modal interactions
- Enables **staged distillation** (not one-step alignment), alleviating optimization instability
- Decouples signal denoising, semantic abstraction, and cross-modal geometric alignment into separate stages

### EEG Encoding Pipeline
1. **Subject-Specific Linear Layer**: Learns per-subject mappings
2. **iTransformer Backbone**: Captures long-range temporal dependencies
3. **STAM Module**: Spectral-temporal feature conditioning

## Results (THINGS-EEG Benchmark)

| Metric | Performance |
|--------|-------------|
| 200-way Top-1 accuracy | 34.50% |
| 200-way Top-5 accuracy | 65.95% |
| Semantic coherence | Validated via diffusion model reconstruction |

### Key Findings
- **Zero-shot retrieval**: Competitive performance on the challenging THINGS-EEG RSVP benchmark
- **Semantic alignment**: Embeddings produce semantically coherent image reconstructions with a diffusion model
- **Staged alignment > one-step**: Decoupling representation learning from cross-modal alignment improves stability
- **Soft spectral modulation > hard masking**: Preserves temporal transients critical for RSVP paradigms

## Advantages Over Prior Work

| Method | Artifact Handling | Alignment | Stage Decoupling |
|--------|------------------|-----------|-----------------|
| Neural-MCRL | Hard masking (ringing artifacts) | One-step | No |
| ATM | Hard masking | One-step | No |
| NeuroBridge | Hard masking | Shared projector | Partial |
| **STAMBRIDGE** | **Soft amplitude weighting** | **Staged MFSB** | **Yes** |

## When to Use

This skill is relevant when:
- **Decoding visual content from EEG** (zero-shot retrieval)
- **Building EEG-to-image reconstruction** systems
- **Designing EEG representation learning** with spectral priors
- **Working with RSVP paradigms** where transient preservation is critical
- **Addressing cross-modal alignment** challenges in BCI
- **Using THINGS-EEG benchmark** for evaluation

## Dependencies
- PyTorch, CLIP vision-language model
- iTransformer backbone for temporal encoding
- Latent diffusion model for reconstruction validation
- THINGS-EEG dataset (RSVP paradigm)

## Activation Keywords
EEG visual decoding, EEG-to-image reconstruction, zero-shot EEG retrieval, spectral-temporal modulation, STAM, Mid-Feature Semantic Bridge, THINGS-EEG, RSVP paradigm, brain-computer interface, cross-modal alignment, contrastive learning EEG, EEG embedding, soft spectral weighting, staged distillation, EEG-to-vision, multimodal neural decoding
