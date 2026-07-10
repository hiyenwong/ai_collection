---
name: jet-eeg-flow-matching
description: "Just EEG Transformer (JET) — generative EEG framework using conditional flow matching to model neural signals as continuous trajectories, preserving spectral structure, temporal stationarity, and signal statistics. ICML 2026. Reduces TS-FID by >40% on large-scale benchmarks. arXiv:2605.21280"
tags: [eeg, flow-matching, generative-model, transformer, continuous-dynamics, neural-signals, icml-2026, eeg-generation]
arxiv_id: "2605.21280"
date: "2026-05-20"
---

# JET: Just EEG Transformer — Continuous Flow Matching for EEG Generation

## Paper Reference

**Title:** Let EEG Models Learn EEG
**Authors:** Yifan Wang, Yijia Ma, Wen Li, Chenyu You
**arXiv:** 2605.21280 (May 20, 2026)
**Category:** cs.CV (Computer Vision and Pattern Recognition) — **Accepted ICML 2026**
**Project page:** https://jet-eeg.github.io (placeholder)

## Abstract Summary

High-fidelity EEG generation is critical for alleviating data scarcity and privacy constraints. Existing approaches use discrete denoising objectives that inadequately reflect the continuous temporal dynamics and spectral structure of neural activity. JET (Just EEG Transformer) is a generative framework based on **conditional flow matching** that models EEG as raw sequences evolving along **continuous trajectories**, learning a smooth vector field that transports noise to EEG data distribution.

## Core Innovations

### 1. Continuous Flow Matching for EEG

Instead of discrete denoising (diffusion), JET uses conditional flow matching:

```
Discrete (diffusion):  x₀ → x₁ → x₂ → ... → x_T (discrete steps)
Continuous (JET):      x(t) where t ∈ [0,1] (smooth trajectory)
```

- Learns a **smooth vector field** v(x,t) that transports noise to EEG
- Captures **temporal continuity** without discretized denoising schemes
- No domain-specific representations needed (works on raw sequences)

### 2. Principled Constraints for EEG Structure

JET introduces three key constraints:

| Constraint | Purpose | Implementation |
|-----------|---------|---------------|
| **Spectral structure** | Preserve frequency content | Loss on spectrogram/PSD |
| **Temporal stationarity** | Maintain statistical consistency over time | Stationarity regularization |
| **Signal-level statistics** | Match amplitude distributions | Moment matching loss |

### 3. Just EEG Transformer Architecture

```
┌──────────────────────────────────────┐
│         Noise z ~ N(0,1)             │
│              │                        │
│              ▼                        │
│   ┌────────────────────┐             │
│   │  Transformer Enc.  │             │
│   │  (Flow Matching)   │             │
│   └────────┬───────────┘             │
│            │                          │
│            ▼                          │
│   Continuous Trajectory x(t)         │
│   t ∈ [0,1]                           │
│            │                          │
│            ▼                          │
│      Generated EEG                    │
└──────────────────────────────────────┘
```

## Key Results

### Performance (3 Large-Scale Benchmarks)

| Metric | JET | Previous SOTA | Improvement |
|--------|:---:|:------------:|:-----------:|
| **TS-FID** | — | — | **>40% reduction** |
| Spectral preservation | ✓ | ✗ | Captures frequency structure |
| Temporal dynamics | ✓ | ✗ | Continuous trajectory modeling |
| Signal statistics | ✓ | ✗ | Matches real EEG distribution |

### Advantages Over Diffusion-Based Methods

1. **Continuous trajectories**: Better captures neural dynamics
2. **No discrete steps**: Avoids step-induced artifacts
3. **Spectral fidelity**: Preserves frequency content
4. **Temporal consistency**: Maintains stationarity
5. **Raw sequence modeling**: No domain-specific preprocessing

## Methodology Details

### Conditional Flow Matching Objective

```
ℒ_CFM = E_{t, x(0), x(1)} [ || v(x(t), t) - u(x(t)|x(1)) ||² ]
```

Where:
- x(0) ~ noise distribution (e.g., Gaussian)
- x(1) ~ EEG data distribution  
- u(x(t)|x(1)): conditional vector field toward data
- v(x(t), t): learned vector field (parameterized by Transformer)

### Spectral Regularization

```
ℒ_spectral = || S(x_generated) - S(x_real) ||²
```

Where S(·) computes the power spectral density.

### Stationarity Regularization

Enforces consistent statistics across temporal segments:
```
ℒ_stationarity = Σ || μ_seg_i - μ_global ||² + || σ²_seg_i - σ²_global ||²
```

## Applications

1. **EEG data augmentation**: Generate synthetic EEG for training
2. **Privacy-preserving sharing**: Share generated (not real) EEG
3. **Transfer learning**: Pre-train on generated EEG, fine-tune on real
4. **Brain-computer interfaces**: Augment limited BCI datasets
5. **Clinical EEG**: Generate pathological EEG patterns for rare conditions

## Pitfalls & Considerations

- Requires large training datasets (3 benchmarks used)
- Flow matching inference is slower than GANs (multiple ODE steps)
- Spectral constraints may limit diversity of generated signals
- Raw sequence modeling is computationally intensive
- Clinical validation of generated EEG fidelity still needed

## Activation Keywords

- JET EEG transformer
- conditional flow matching EEG
- continuous EEG generation
- EEG flow matching
- EEG data augmentation generative
- ICML 2026 EEG
- spectral structure EEG generation
- raw EEG sequence modeling
- arXiv:2605.21280

## Related Skills

- reve-eeg-foundation
- eeg-foundation-lrp-interpretability
- laya-eeg-foundation
- eeg-structure-guided-diffusion
- eeg-foundation-sae-interpretability

## References

- arXiv:2605.21280 — "Let EEG Models Learn EEG" (Wang et al., ICML 2026)
- Conditional Flow Matching (Lipman et al., 2022)
- Diffusion Models for EEG (prior work)
- Just EEG Transformer (JET) — project page: https://jet-eeg.github.io
