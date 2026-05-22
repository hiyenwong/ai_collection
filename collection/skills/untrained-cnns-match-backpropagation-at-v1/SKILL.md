---
name: untrained-cnns-match-backpropagation-at-v1
description: "Systematic RSA comparison showing untrained CNNs match backpropagation at V1 alignment with human fMRI. Evaluates BP, FA, PC, and STDP learning rules against THINGS-fMRI dataset using 720 stimuli across 3 subjects. Use when studying brain-model alignment, comparing learning rules, or analyzing visual cortex representations via Representational Similarity Analysis."
version: 1.0.0
metadata:
  hermes:
    tags: ["representational-similarity-analysis", "learning-rules", "brain-alignment", "fMRI", "visual-cortex", "STDP"]
    source_paper: "Untrained CNNs Match Backpropagation at V1: A Systematic RSA Comparison of Four Learning Rules Against Human fMRI (arXiv:2604.16875)"
---

# Untrained CNNs Match Backpropagation at V1: A Systematic RSA Comparison of Four Learning Rules Against Human fMRI

## Source

- **arXiv:** [2604.16875](https://arxiv.org/abs/2604.16875)
- **Authors:** Nils Leutenegger
- **Published:** 2026-04-18 (revised 2026-04-29)
- **Categories:** cs.LG, q-bio.NC

## Abstract

A central question in computational neuroscience is whether the learning rule used to train a neural network determines how well its internal representations align with those of the human visual cortex. We present a systematic comparison of four learning rules — backpropagation (BP), feedback alignment (FA), predictive coding (PC), and spike-timing-dependent plasticity (STDP) — applied to identical convolutional architectures and evaluated against human fMRI data from the THINGS-fMRI dataset (720 stimuli, 3 subjects) using Representational Similarity Analysis (RSA). All models process stimuli at 224×224 resolution; results are averaged across 5 random seeds. Crucially, we include an untrained random-weights baseline.

## Key Findings

### 1. Architecture Dominates at Early Visual Areas (V1/V2)
- Untrained random-weights baseline **exceeds** backpropagation at V1/V2 alignment
  - Untrained: ρ = 0.076 vs. BP: ρ = 0.034 (Δρ = +0.044, p < 0.001)
  - Architecture alone explains most early visual alignment
  - Learning rules contribute minimally at early stages

### 2. STDP Achieves Best Alignment Among Trained Rules at V1
- STDP: ρ = 0.064 at V1 — highest among all trained learning rules
- Suggests biologically plausible plasticity rules better capture early visual processing

### 3. Learning Rules Only Differentiate at Intermediate Areas (LOC)
- At LOC, only BP reliably exceeds the random baseline (ρ = 0.012 vs. -0.005, p < 0.001)
- FA consistently produces the lowest alignment at V1, V2, and LOC (ρ = 0.012 at V1)

### 4. All Rules Converge at High-Level Areas (IT)
- At IT, all five conditions converge (ρ = 0.008–0.014)
- No significant pairwise differences among trained rules (p > 0.05, FDR-corrected)
- Suggests task-independent architectural constraints dominate at highest levels

### 5. Robustness Checks
- Partial RSA confirms all effects survive pixel-similarity control
- Seed variability is small relative to between-rule differences at V1/V2

## Methodology

- **Dataset:** THINGS-fMRI (720 naturalistic stimuli, 3 human subjects)
- **Architecture:** Identical CNN across all learning rules
- **Learning Rules Compared:** BP, FA, PC, STDP, plus untrained baseline
- **Evaluation Metric:** Representational Similarity Analysis (RSA)
- **Visual Areas:** V1, V2, LOC, IT
- **Statistical Rigor:** FDR correction, 5 random seeds, pixel-similarity controls

## Implications

- Early visual alignment is **architecture-driven**, not learning-rule-driven
- Biologically plausible rules (STDP) outperform BP at early visual areas
- Different learning rules cannot be distinguished by brain alignment at highest levels
- Suggests rethinking of brain-DNN comparison benchmarks: control for architectural effects
- Untrained baselines are essential for proper attribution of brain alignment

## Activation Keywords

- representational-similarity-analysis, learning-rules, brain-alignment, fMRI, visual-cortex, STDP, backpropagation comparison, V1 alignment, computational neuroscience
