---
name: untrained-cnns-match-backpropagation-v1-rsa
description: "Systematic RSA comparison showing untrained CNNs match backpropagation-trained CNNs at V1 visual cortex. Untrained random-weights CNN (rho=0.076) exceeds backprop (rho=0.034) at V1/V2 (p<0.001). STDP achieves highest V1 alignment among trained rules (rho=0.064). Four learning rules (BP, FA, PC, STDP) compared against human fMRI from THINGS-fMRI dataset (720 stimuli, 3 subjects)."
tags: [RSA, backpropagation, feedback-alignment, predictive-coding, STDP, visual-cortex, fMRI, THINGS-fMRI, untrained-baseline, V1-alignment, architecture-driven]
arxiv_id: "2604.16875"
date: "2026-04-18"
---

# Untrained CNNs Match Backpropagation at V1: Systematic RSA Study

> Large-scale fMRI study (THINGS-fMRI, 720 stimuli, 3 subjects) reveals untrained CNNs achieve higher RSA alignment to V1 (rho=0.076) than backpropagation-trained CNNs (rho=0.034), demonstrating that **early visual alignment is architecture-driven, not learning-rule-driven**.

## Paper Reference

**Title:** Untrained CNNs Match Backpropagation at V1: A Systematic RSA Comparison of Four Learning Rules Against Human fMRI
**Author:** Nils Leutenegger
**arXiv:** 2604.16875 (April 18, 2026)
**Category:** cs.LG (Machine Learning), q-bio.NC (Neurons and Cognition)

## Full Abstract

A central question in computational neuroscience is whether the learning rule used to train a neural network determines how well its internal representations align with those of the human visual cortex. We present a systematic comparison of four learning rules (backpropagation (BP), feedback alignment (FA), predictive coding (PC), and spike-timing-dependent plasticity (STDP)) applied to identical convolutional architectures and evaluated against human fMRI data from the THINGS-fMRI dataset (720 stimuli, 3 subjects) using Representational Similarity Analysis (RSA). All models process stimuli at 224x224 resolution; results are averaged across 5 random seeds. Crucially, we include an untrained random-weights baseline that reveals the dominant role of architecture. At V1/V2, the untrained baseline exceeds backpropagation (rho = 0.076 vs. rho = 0.034; Delta-rho = +0.044, p < 0.001), and STDP achieves the highest V1 alignment among trained rules (rho = 0.064). At LOC, only BP reliably exceeds the random baseline (rho = 0.012 vs. -0.005, p < 0.001). At IT, all five conditions converge (rho = 0.008-0.014) with no significant pairwise differences among trained rules (p > 0.05, FDR-corrected). FA consistently produces the lowest alignment at V1, V2, and LOC (rho = 0.012 at V1, below all other conditions). Partial RSA confirms all effects survive pixel-similarity control. Seed variability is small relative to between-rule differences at V1/V2.

## Core Methodology

1. **Dataset**: THINGS-fMRI (720 stimuli, 3 subjects)
2. **Models**: Identical CNN architectures with 4 learning rules
3. **Evaluation**: RSA with Representational Dissimilarity Matrices
4. **Critical Baseline**: Untrained random-weights network
5. **All models**: 224×224 resolution, 5 random seeds averaged
6. **Control**: Partial RSA for pixel-similarity confound

## Key Findings

| Brain Area | Key Result | p-value |
|------------|------------|---------|
| **V1/V2** | Untrained rho=0.076 > BP rho=0.034 | Δρ=+0.044, p<0.001 |
| **V1 (STDP)** | STDP rho=0.064 (highest trained) | — |
| **V1 (FA)** | FA rho=0.012 (lowest) | — |
| **LOC** | Only BP exceeds random (rho=0.012 vs -0.005) | p<0.001 |
| **IT** | All converge (rho=0.008-0.014) | n.s. |

## Implications

1. **Architecture dominates**: CNN structure encodes priors matching V1, independent of weights
2. **Learning rules matter only at intermediate, not early or late, stages**
3. **Re-evaluation needed**: Many studies attribute alignment to learning, not architecture
4. **Seed variability small** relative to between-rule differences at V1/V2
5. **STDP's strong V1 showing**: Local rules may better capture early visual representations

## Applications
- Evaluate CNN architectures for neuroscience research
- Study how architectural constraints shape brain-like representations
- Always include untrained baseline in brain-model comparisons
- Isolate contribution of training from architecture

## Pitfalls
- **Beyond V1**: Results may not generalize without control
- **Task specificity**: Untrained networks lack task-relevant features
- **Correlation vs causation**: RSA similarity ≠ identical computation
- **Always include untrained baseline**: Critical control

## Activation Keywords
- untrained CNN V1 alignment, RSA brain comparison
- backpropagation vs STDP V1, architecture-driven brain alignment
- THINGS-fMRI RSA, random weights V1 match
- learning rule comparison fMRI, predictive coding brain alignment
- feedback alignment RSA, representational similarity visual cortex
- arXiv:2604.16875
