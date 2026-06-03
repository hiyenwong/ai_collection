---
name: swpc-directed-functional-connectivity
description: >
  Sliding-window prediction correlation (SWpC) for time-varying directed functional connectivity.
  Embeds directional LTI models within sliding windows to estimate time-resolved information
  flow in brain networks, going beyond undirected correlation.
---

# SWpC: Sliding-Window Prediction Correlation for Directed Functional Connectivity

**Paper:** arXiv:2602.16004
**Authors:** Nan Xu, Xiaodi Zhang, Wen-Ju Pan, et al.
**Categories:** q-bio.NC, cs.LG
**Year:** 2026

## Overview

SWpC estimates time-varying directed functional connectivity in brain networks. Unlike traditional sliding-window correlation (SWC) which captures undirected associations, SWpC resolves directional interactions by embedding a directional LTI model within each sliding window.

## Key Concepts

### Limitations of SWC
- Captures time-varying undirected associations only
- Cannot resolve directionality of information flow

### SWpC Method
- Embeds directional LTI model within each sliding window
- Two complementary measures:
  1. Strength: Prediction correlation
  2. Duration: Window-wise duration of information transfer

## Methodology

### Algorithm
1. Sliding window for time series segmentation
2. LTI model fitting within each window between all region pairs
3. Duration estimation across windows
4. Output: Time-varying directed connectivity matrices

### Validation
- Multimodal: Concurrent LFP and fMRI BOLD
- Task fMRI: HCP motor task data
- Clinical: Post-concussion vestibular dysfunction

## Applications
- Task-based fMRI analysis
- Clinical neuroscience: brain-state shifts detection
- Brain-computer interfaces
- Network neuroscience

## Key Insights
1. Direction matters in brain connectivity
2. Two complementary measures: strength and duration
3. Multimodal consistency across LFP and BOLD
4. Clinical utility: improved healthy vs patient discrimination

## References
- Xu, N., Zhang, X., Pan, W.-J., et al. (2026). SWpC. arXiv:2602.16004.
