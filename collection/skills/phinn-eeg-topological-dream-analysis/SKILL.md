---
name: phinn-eeg-topological-dream-analysis
category: neuroscience
description: Topological time-series analysis methodology for dream-state EEG using Dynamic Betti curves, persistent homology, and topology-conditioned neural signal synthesis. arXiv:2607.09662
created: 2026-07-13
source: arXiv:2607.09662v1 (Takahashi, Yusuf, Bhaduri, 2026-07-10)
---

# PHINN-EEG: Topological Dream-State EEG Analysis

## Overview

PHINN-EEG (Persistent Homology Inspired Neural Network for EEG) is the first topological time-series framework for dream mentation analysis. It shifts dream detection from spectral energy (PSD) to phase-space geometry using persistent homology.

## Core Methodology

### 1. Dynamic Betti Curves
- **Sliding-window Takens delay embeddings** on multichannel pre-awakening EEG epochs
- **Vietoris-Rips filtrations** extract topological invariants (Betti numbers β₀, β₁, β₂...)
- **Dynamic Betti Curves** characterize the geometric architecture of neural activity, not just energy
- Targets AUC = 0.82-0.90 vs. ~0.70 SOTA (PSD + catch22 benchmarks)

### 2. Topology-Conditioned Flow Matching
- **Topology-conditioned rectified flow model** for dream-state EEG synthesis
- Spectral-conditioned flow model used as ablation baseline to isolate topological conditioning value
- Candidate Betti transition archetypes link topology to phenomenological dream report categories

### 3. Dataset
- DREAM database: 1,462-awakening open-access subset (from 3,191 total awakenings, 263 participants, 20 labs)

## Key Innovation

**Paradigm shift**: From spectral energy analysis to phase-space geometry for neural rare-event detection. The Betti curves capture topological features (connected components, loops, voids) in the reconstructed state space of EEG signals.

## Implementation Steps

1. **Preprocessing**: Extract pre-awakening EEG epochs from polysomnography data
2. **Takens Embedding**: Apply delay embedding to reconstruct phase space (choose embedding dimension d and delay τ)
3. **Vietoris-Rips Filtration**: Compute persistent homology across filtration parameter ε
4. **Betti Curve Extraction**: Track β₀(t), β₁(t), β₂(t) over sliding windows
5. **Classification**: Feed Dynamic Betti Curves (or topology-conditioned features) to a downstream classifier; use topology-conditioned rectified flow for synthesis/ablation

## Activation / Triggers

phinn-eeg, betti curves, persistent homology, topological eeg, dream detection, takens embedding, vietoris-rips, topology-conditioned flow

## Verification

- Outperforms PSD and catch22 baselines on the DREAM open-access subset (target AUC 0.82-0.90)
- Spectral-conditioned ablation confirms added value of topological conditioning
- Betti transition archetypes reproducible across the 20 independent laboratories subset
