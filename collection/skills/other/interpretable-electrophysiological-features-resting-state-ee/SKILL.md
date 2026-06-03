---
name: interpretable-electrophysiological-features-resting-state-ee
description: "Parkinsons disease (PD) alters cortical neural dynamics, yet reliable non-invasive electrophysiological biomarkers remain elusive. This study examined whether interpretable EEG fea... Activation: network, neural, dynamics, EEG"
---

# Interpretable Electrophysiological Features of Resting-State EEG Capture Cortical Network Dynamics in Parkinsons Disease

## Overview
Parkinsons disease (PD) alters cortical neural dynamics, yet reliable non-invasive electrophysiological biomarkers remain elusive. This study examined whether interpretable EEG features capturing complementary aspects of neural dynamics can discriminate Parkinsonian neural states. A comprehensive set of interpretable features was extracted and grouped into Standard descriptors (spectral power, phase synchronization, time-domain statistics) and Dynamical descriptors (aperiodic activity, cross-frequency coupling, scale-free dynamics, neuronal avalanche statistics, and instantaneous frequency measures). A multi-head attention transformer classifier was trained using strict LOSO validation. Group-level comparisons were performed to identify electrophysiological differences associated with disease and medication state. Standard feature sets achieved strongest performance in discriminating medication states (PDoff vs PDon), whereas Dynamical performed competitively in contrasts between PD patients and healthy controls. Random feature ablation analyses indicated that Dynamical descriptors provide complementary information distributed across features while correlation analysis revealed low redundancy within both feature sets. Group-level comparisons revealed medication-sensitive reductions in delta power and voltage variance, modulation of neuronal avalanche statistics, persistent increases in theta phase synchronization in PD patients, and disease-related alterations in cross-frequency interactions. Traditional spectral and synchronization features primarily reflect medication-related neural modulation, whereas dynamical descriptors reveal broader alterations in cortical network organization associated with disease but also with medication. These findings support multivariate EEG representations as a promising framework for developing non-invasive biomarkers of PD.

## Source Paper
- **Title:** Interpretable Electrophysiological Features of Resting-State EEG Capture Cortical Network Dynamics in Parkinsons Disease
- **Authors:** Antonios G. Dougalis
- **arXiv:** 2604.01475v1
- **Published:** 2026-04-01
- **Categories:** q-bio.NC, q-bio.QM
- **PDF:** https://arxiv.org/pdf/2604.01475v1

## Core Concepts

### Key Contributions
- Parkinsons disease (PD) alters cortical neural dynamics, yet reliable non-invasive electrophysiological biomarkers remain elusive
- This study examined whether interpretable EEG features capturing complementary aspects of neural dynamics can discriminate Parkinsonian neural states

### Applications
- Neuroscience research
- Brain network analysis
- Neural signal processing

## Implementation Notes
- Python-based neuroimaging analysis
- Standard preprocessing pipelines

## References
- Antonios G. Dougalis et al. (2026). "Interpretable Electrophysiological Features of Resting-State EEG Capture Cortical Network Dynamics in Parkinsons Disease." arXiv:2604.01475v1.

## Activation Keywords
- network
- neural
- dynamics
- EEG
- neuroscience
- brain research
