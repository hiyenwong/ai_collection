---
name: neuroscience-eeg-meg-brain-networks
description: Skill for exploring brain networks using noninvasive electrophysiological measurements (EEG/MEG) based on arXiv:2607.17602v1.
tags: []
related_skills: []
---

# Neuroscience: EEG/MEG Brain Network Analysis

## Overview
This skill encapsulates the methodology from the arXiv preprint "Exploring Brain Networks Using Noninvasive Electrophysiological Measurements: Methods and Applications" (arXiv:2607.17602v1). It provides a structured approach to analyzing functional and effective connectivity in large-scale brain networks using EEG and MEG data.

## Activation
Trigger when you need to:
- Analyze EEG/MEG data for brain network connectivity.
- Apply functional connectivity metrics (coherence, phase synchronization, amplitude envelope correlation, Granger causality, dynamic causal modeling, transfer entropy).
- Implement effective connectivity analysis with source reconstruction.
- Follow end-to-end analysis pipelines using Brainstorm or open-source tools.
- Explore emerging approaches like time-varying connectivity, cross-frequency interactions, and network-based analyses.

## Steps

### 1. Data Acquisition and Preprocessing
- Ensure EEG/MEG recordings are acquired with appropriate hardware and sampling rate.
- Apply standard preprocessing: filtering, artifact removal (eye blinks, muscle noise), bad channel detection, and re-referencing.
- Use tools like EEGLAB, MNE-Python, or Brainstorm for preprocessing.

### 2. Forward and Inverse Modeling
- Construct a realistic head model (e.g., using individual MRI or standard templates).
- Compute the lead field matrix for source localization.
- Apply inverse solutions (e.g., minimum norm estimate, beamforming) to reconstruct source time series.
- Validate source localization accuracy with simulations or phantom data.

### 3. Source-Space Connectivity Analysis
- Extract time series from regions of interest (ROIs) or whole-brain source space.
- Compute functional connectivity measures:
  - **Coherence**: frequency-domain correlation.
  - **Phase Synchronization**: Phase Locking Value (PLV) or Phase Lag Index (PLI).
  - **Amplitude Envelope Correlation**: correlation of band-limited amplitude envelopes.
  - **Granger Causality**: predictability improvement in time domain.
  - **Transfer Entropy**: information-theoretic, model-free directed measure.
  - **Dynamic Causal Modeling (DCM)**: model-based effective connectivity.
- Correct for volume conduction and signal leakage using techniques like orthogonalization, imaginary part of coherency, or source leakage correction.

### 4. Statistical Analysis and Validation
- Use statistical testing (e.g., permutation testing, false discovery rate correction) to assess significance of connectivity changes.
- Validate findings with alternative metrics or split-half reliability.
- Consider multiple comparison correction across frequency bands, connections, and time windows.

### 5. Advanced Analyses
- **Time-Varying Connectivity**: sliding window or adaptive methods to track dynamic changes.
- **Cross-Frequency Coupling**: phase-amplitude coupling between different frequency bands.
- **Network-Based Statistics (NBS)**: identify subnetworks showing significant differences.
- **Graph Theory Analysis**: compute network metrics (degree, clustering coefficient, path length, small-worldness, modularity).

### 6. Reporting and Visualization
- Visualize connectivity matrices using heatmaps or circular layouts.
- Display significant connections on brain surfaces or volumetric templates.
- Report effect sizes, confidence intervals, and corrected p-values.
- Include detailed methodology for reproducibility (software versions, parameters).

## Pitfalls
- **Volume Conduction**: Can cause spurious zero-lag correlations; always apply leakage correction.
- **Source Localization Errors**: Inaccurate head model or sensor registration leads to mislocalized sources.
- **Multiple Comparisons**: Testing many connections increases false positives; use appropriate correction.
- **Non-Stationarity**: Brain dynamics change over time; ensure stationarity within analysis windows or use time-varying methods.
- **Reference Dependence**: EEG referencing can affect results; consider using average reference or reference-free techniques.

## References
- arXiv:2607.17602v1 – Exploring Brain Networks Using Noninvasive Electrophysiological Measurements: Methods and Applications.
- Brainstorm documentation: https://neuroimage.usc.edu/brainstorm/
- MNE-Python: https://mne.tools/
- EEGLAB: https://sccn.ucsd.edu/eeglab/
- References within the paper for detailed methodology.

## Usage Example
To analyze resting-state EEG for default mode network connectivity:
1. Preprocess data (filter 0.1-45 Hz, remove artifacts).
2. Compute forward model using a standard head template.
3. Apply LORETA source localization.
4. Extract time series from posterior cingulate cortex and medial prefrontal cortex.
5. Compute magnitude squared coherence and PLV in alpha band (8-12 Hz).
6. Correct for leakage using imaginary part of coherency.
7. Test significance with permutation testing (1000 shuffles).
8. Report coherence increase with p<0.01 FDR-corrected.