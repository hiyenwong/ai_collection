---
name: exploring-brain-networks-eeg-meg
description: "Skill for exploring brain networks using noninvasive electrophysiological measurements (EEG/MEG) based on arXiv:2607.17602v1. Covers forward/inverse problems, source reconstruction, connectivity measures, and analysis pipelines."
license: Complete terms in LICENSE.txt
metadata:
  arxiv_id: "2607.17602v1"
  published: "2026-07-20"
  authors: ["Unknown"]
tags: [eeg, meg, brain network, connectivity, source localization]
---

# Exploring Brain Networks Using Noninvasive Electrophysiological Measurements

Based on arXiv:2607.17602v1 - "Exploring Brain Networks Using Noninvasive Electrophysiological Measurements: Methods and Applications"

## Overview
This skill provides a practical guide for analyzing brain networks using EEG and MEG data. It covers the methodological foundations from forward/inverse modeling to connectivity analysis and practical workflows using open-source tools like Brainstorm.

## Key Concepts

### 1. Forward and Inverse Problems
- **Forward problem**: Predicting sensor signals from known neural sources
- **Inverse problem**: Estimating neural sources from sensor measurements (ill-posed)
- Requires accurate head modeling and source reconstruction techniques

### 2. Source Reconstruction Techniques
- Minimum norm estimates (MNE)
- Beamforming (LCMV)
- Multiple sparse priors (MSP)
- Dipole fitting

### 3. Mitigating Volume Conduction and Signal Leakage
- Orthogonalization approaches
- Signal space projection (SSP)
- Surface Laplacian
- Imaginary part of coherency
- Phase lag index

### 4. Functional and Effective Connectivity Measures
- **Functional** (symmetric, undirected):
  - Coherence
  - Phase synchronization (PLV, PLI)
  - Amplitude envelope correlation
- **Effective** (directed, causal):
  - Granger causality
  - Dynamic causal modeling (DCM)
  - Transfer entropy

### 5. Analysis Pipelines
- Preprocessing (filtering, artifact removal)
- Source localization
- Connectivity estimation
- Statistical validation
- Visualization (brain networks, graphs)

## Practical Workflow (Brainstorm-centric)

1. **Data Import**: Load raw EEG/MEG files (EDF, BDF, FIF, etc.)
2. **Preprocessing**:
   - Bandpass filtering (typically 1-40 Hz)
   - Artifact removal (ICA, SSP, regression)
   - Bad channel detection/interpolation
3. **Head Modeling**:
   - Create volume conduction model (single sphere, realistically shaped)
   - Align MRI with sensor positions
4. **Source Localization**:
   - Compute leadfield matrix
   - Apply inverse method (MNE, beamforming)
   - Extract source time series
5. **Connectivity Analysis**:
   - Choose appropriate measure based on hypothesis
   - Compute connectivity matrices (frequency-specific if needed)
   - Apply statistical thresholding (permutation testing, FDR)
6. **Network Analysis**:
   - Graph theoretical metrics (degree, betweenness, clustering, path length)
   - Community detection
   - Rich-club analysis
7. **Visualization**:
   - Source activations on cortical surface
   - Connectivity matrices (circular, matrix plots)
   - Brain networks (glass brain, force-directed layouts)

## Emerging Approaches
- **Time-varying connectivity**: Sliding windows, state-space models, hidden Markov models
- **Cross-frequency interactions**: Phase-amplitude coupling, cross-frequency coherence
- **Multivariate decoding**: MVPA on source space, decoding networks

## Tools and Resources
- **Brainstorm**: https://neuroimage.usc.edu/brainstorm/
- **EEGLAB**: https://sccn.ucsd.edu/eeglab/
- **MEG-Python (MNE-Python)**: https://mne.tools/
- **FieldTrip**: https://www.fieldtriptoolbox.org/
- **TVB**: The Virtual Brain (https://www.thevirtualbrain.org/)
- **Graph analysis**: Brain Connectivity Toolbox (https://sites.google.com/site/bctnet/)

## Validation and Best Practices
- Validate forward model with simulated dipoles
- Test inverse solutions with known source configurations
- Use surrogate data testing for connectivity measures
- Correct for multiple comparisons
- Report parameters and preprocessing steps for reproducibility

## Activation Keywords
eeg meg brain network connectivity source localization brainstorm mne python neuroscience electrophysiology

## References
1. arXiv:2607.17602v1 - Exploring Brain Networks Using Noninvasive Electrophysiological Measurements: Methods and Applications
2. Brainstorm tutorials and documentation
3. MNE-Python documentation
4. FieldTrip tutorials
