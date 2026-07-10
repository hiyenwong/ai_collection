---
name: brain-to-language-source-attribution
title: "What Are We Actually Decoding? Source Attribution for Non-Invasive Brain-to-Language Retrieval"
description: Source attribution framework for MEG-to-audio brain decoding that separates decoding performance into structural shortcuts, stimulus-evoked evidence, and contextual aggregation
tags:
  - brain-decoding
  - source-attribution
  - meg
  - language-decoding
  - gcb
  - group-context-bias
  - neuroscience
  - computational-neuroscience
created: 2026-05-26
---

# What Are We Actually Decoding? Source Attribution for Non-Invasive Brain-to-Language Retrieval

**arXiv**: [2605.24524](https://arxiv.org/abs/2605.24524)
**Authors**: Xinyu Zhang, Sichao Liu, Runhao Lu, Alexandra Woolgar, Lihui Wang
**Subjects**: Machine Learning (cs.LG); Computation and Language (cs.CL); Neurons and Cognition (q-bio.NC)

## Summary

This paper addresses a critical methodological challenge in non-invasive neural language decoding: how to properly attribute decoding performance to neural sources versus confounding factors. The authors recast stimulus-locked MEG-to-audio retrieval as an auditing framework that separates apparent performance into three sources:

1. **Structural shortcuts** — non-neural nuisances like signal duration that can inflate results
2. **Window-level stimulus-locked evidence** — genuine neural evidence at the individual time-window level
3. **Cross-window contextual aggregation** — integration of evidence across multiple windows

## Key Contributions

1. **Structured Auditing Framework**: Separates brain-to-language decoding performance into three distinct sources with diagnostic tests for each

2. **Structural Leakage Isolation**: Signal-blind Gaussian noise reaches 66.3% Rank@1 under variable-length decoding but collapses to near chance once fixed-duration windows and stimulus-identity splits are enforced — demonstrating that variable-length decoding creates a structural shortcut

3. **Group Context Bias (GCB)**: An inference-time additive logit bias that pools sentence-consistent evidence across windows, making the contextual source measurable:
   - R@1 shifts from 44% to 52% on Gwilliams dataset
   - R@1 shifts from 22% to 29% on MOUS dataset
   - Effect collapses under random-grouping perturbations
   - Vanishes when local evidence is attenuated in MEG or near chance in EEG

4. **Oracle Diagnostic**: 95.7% of Top-1 errors select the wrong sentence, localising the residual bottleneck to sentence-level competition

## Methodology

- **Framework**: Stimulus-locked MEG-to-audio retrieval with controlled source attribution
- **Controls**: Fixed-duration windows, stimulus-identity splits, signal-blind baselines
- **Intervention**: Group Context Bias (GCB) — an auditable score-space intervention
- **Validation**: Two datasets (Gwilliams, MOUS) with MEG and EEG modalities

## Implications

- Brain-to-language decoding performance should be source-attributed, not merely reported
- Variable-length decoding without proper controls overestimates neural evidence
- GCB provides a principled way to measure contextual aggregation effects
- Framework applicable to other neural decoding tasks beyond language

## Activation Keywords

brain-to-language-source-attribution, meg-audio-retrieval, structural-shortcut-detection, group-context-bias, neural-decoding-evaluation, source-attribution-framework, brain-decoding-methodology
