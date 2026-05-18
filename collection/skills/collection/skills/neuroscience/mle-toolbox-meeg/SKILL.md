---
name: mle-toolbox-meeg
title: "MLE-Toolbox: Comprehensive EEG/MEG Data Analysis"
category: neuroscience
source: arXiv:2604.16463
paper_title: "MLE-Toolbox: An Open-Source Toolbox for Comprehensive EEG and MEG Data Analysis"
authors:
  - Xiaobo Liu
date: 2026-04-08
subjects:
  - q-bio.NC (Quantitative Biology - Neurons and Cognition)
  - cs.AI (Artificial Intelligence)
  - cs.SE (Software Engineering)
description: >
  Open-source MATLAB toolbox for end-to-end EEG/MEG analysis with unified GUI.
  Covers preprocessing, source localization (MNE, dSPM, sLORETA, beamforming),
  functional connectivity, oscillatory analysis, PAC, graph-theoretic network
  analysis, and ML/DL classification. Interoperable with Brainstorm, FieldTrip,
  EEGLAB, FreeSurfer.
keywords:
  - MLE-Toolbox
  - EEG analysis toolbox
  - MEG analysis toolbox
  - source localization
  - MNE
  - dSPM
  - sLORETA
  - beamforming
  - functional connectivity
  - phase-amplitude coupling
  - PAC
  - graph theory brain network
  - ICA artifact rejection
  - SSP
  - SSS
  - MATLAB toolbox
  - neuroimaging pipeline
  - 脑电分析工具箱
  - 脑磁图分析工具箱
  - 源定位
  - 功能连接
  - 相位幅度耦合
  - 图论脑网络
activation_keywords:
  - MLE-Toolbox
  - MLE toolbox
  - EEG MEG analysis toolbox
  - MATLAB EEG toolbox
  - open-source EEG analysis
  - brain analysis GUI
  - 脑电分析工具箱
---

# MLE-Toolbox: Comprehensive EEG/MEG Data Analysis

## Overview

**MLE-Toolbox** is a comprehensive open-source MATLAB toolbox for end-to-end analysis of **magnetoencephalography (MEG)** and **electroencephalography (EEG)** data. It integrates the full analysis pipeline within a unified GUI, inspired by Brainstorm and FieldTrip but with additional automation, interactive visualization, and one-click academic report generation.

- **arXiv**: [2604.16463](https://arxiv.org/abs/2604.16463)
- **Author**: Xiaobo Liu
- **Published**: 2026-04-08
- **License**: Non-commercial use

---

## Feature Summary

### 1. Data Import & Preprocessing

| Feature | Description |
|---------|-------------|
| Raw data import | Multiple EEG/MEG formats (EDF, BDF, FIF, BrainVision, etc.) |
| ICA artifact rejection | Independent component analysis for eye, muscle, cardiac artifacts |
| SSP | Signal-space projection for artifact removal |
| SSS | Signal-space separation (MEG-specific) |
| Filtering | Bandpass, notch, highpass, lowpass with configurable parameters |
| Epoching | Event-based segmentation with baseline correction |

### 2. Source Localization

| Method | Description |
|--------|-------------|
| MNE | Minimum norm estimation |
| dSPM | Dynamic statistical parametric mapping |
| sLORETA | Standardized low-resolution brain electromagnetic tomography |
| Beamforming | Data-driven adaptive spatial filtering |
| Multi-atlas parcellation | Anatomical visualization with multiple atlas support |

### 3. Functional Analysis

| Analysis | Description |
|----------|-------------|
| Spectral power | Frequency-band brain mapping (delta, theta, alpha, beta, gamma) |
| Functional connectivity | Correlation, coherence, PLV, wPLI, imaginary coherence |
| Phase-amplitude coupling (PAC) | Cross-frequency coupling analysis |
| Graph-theoretic network analysis | Network metrics (degree, clustering, path length, modularity) |

### 4. Machine Learning & Deep Learning

| Feature | Description |
|---------|-------------|
| ML classifiers | SVM, Random Forest, LDA, etc. |
| DL classifiers | Neural network architectures for EEG/MEG classification |
| Feature extraction | Automated feature pipeline |
| Cross-validation | Built-in CV frameworks |

### 5. Interoperability

| Platform | Integration |
|----------|-------------|
| Brainstorm | Import/export compatible formats |
| FieldTrip | Shared data structures |
| EEGLAB | Data format compatibility |
| FreeSurfer | Cortical surface import for source localization |

### 6. GUI & Reporting

- **Unified graphical interface** for all analysis steps
- **Interactive visualization** of scalp maps, source maps, connectivity matrices
- **One-click academic report generation**

---

## Usage Workflow

```
1. Data Import
   └── Load EEG/MEG raw data (EDF, FIF, BrainVision, etc.)
   
2. Preprocessing
   ├── Filtering (bandpass, notch)
   ├── Artifact rejection (ICA, SSP, SSS)
   └── Epoching & baseline correction
   
3. Source Localization
   ├── Head model computation (BEM, spherical)
   ├── Forward model (leadfield matrix)
   └── Inverse solution (MNE, dSPM, sLORETA, beamforming)
   
4. Functional Analysis
   ├── Spectral power analysis
   ├── Functional connectivity
   ├── Phase-amplitude coupling
   └── Graph-theoretic network analysis
   
5. Classification
   ├── Feature extraction
   ├── Model training (ML/DL)
   └── Cross-validation & evaluation
   
6. Visualization & Reporting
   ├── Interactive plots
   └── One-click report generation
```

---

## Installation

```matlab
% Add MLE-Toolbox to MATLAB path
addpath(genpath('/path/to/MLE-Toolbox'));

% Verify installation
mle_toolbox_info

% Launch GUI
mle_toolbox_gui
```

### Dependencies

- MATLAB R2020a or later
- Signal Processing Toolbox
- Statistics and Machine Learning Toolbox
- Optional: Deep Learning Toolbox (for DL classifiers)
- Optional: FreeSurfer (for cortical surface-based source localization)

---

## Example: EEG Source Localization Pipeline

```matlab
% ─── 1. Load Data ──────────────────────────────────────────────────────────
raw_data = mle_load_data('subject01_eeg.edf');

% ─── 2. Preprocessing ─────────────────────────────────────────────────────
% Bandpass filter 1-45 Hz
filtered = mle_bandpass_filter(raw_data, [1 45]);

% Notch filter 50/60 Hz
filtered = mle_notch_filter(filtered, 50);

% ICA artifact rejection
[ica_data, removed_components] = mle_ica_artifact_rejection(filtered);

% ─── 3. Epoching ──────────────────────────────────────────────────────────
epochs = mle_epoch(ica_data, events, [-0.2 0.8], 'baseline', [-0.2 0]);

% ─── 4. Source Localization ───────────────────────────────────────────────
% Load head model (from FreeSurfer or template)
head_model = mle_load_head_model('subject01_head.mat');

% Compute leadfield
leadfield = mle_compute_leadfield(head_model, epochs.info);

% MNE source reconstruction
sources_mne = mle_source_localization(epochs, leadfield, ...
    'method', 'MNE', 'lambda', 0.1);

% dSPM
sources_dspm = mle_source_localization(epochs, leadfield, ...
    'method', 'dSPM');

% ─── 5. Spectral Analysis ─────────────────────────────────────────────────
[power, freqs] = mle_spectral_power(sources_mne, 'band', [8 12]); % Alpha

% ─── 6. Functional Connectivity ───────────────────────────────────────────
conn = mle_functional_connectivity(sources_mne, ...
    'method', 'wPLI', 'freq_band', [8 12]);

% ─── 7. Graph Analysis ───────────────────────────────────────────────────
graph_metrics = mle_graph_analysis(conn, ...
    'metrics', {'degree', 'clustering', 'path_length', 'modularity'});

% ─── 8. Visualization ─────────────────────────────────────────────────────
mle_plot_source_map(sources_dspm, 'time_window', [0.1 0.3]);
mle_plot_connectivity_circle(conn, 'threshold', 0.3);

% ─── 9. Report ────────────────────────────────────────────────────────────
mle_generate_report('output_dir', './results');
```

---

## Comparison with Existing Toolboxes

| Feature | MLE-Toolbox | Brainstorm | FieldTrip | EEGLAB |
|---------|:----------:|:----------:|:---------:|:------:|
| GUI | ✓ Unified | ✓ | ✗ | ✓ |
| Source Localization | ✓ 4 methods | ✓ | ✓ | Limited |
| Functional Connectivity | ✓ | ✓ | ✓ | ✓ |
| PAC Analysis | ✓ | ✓ | ✓ | Limited |
| Graph Analysis | ✓ Built-in | Limited | Limited | ✗ |
| ML/DL Classification | ✓ Built-in | Limited | Limited | Limited |
| One-click Reports | ✓ | ✗ | ✗ | ✗ |
| Interoperability | ✓ All 3 | Limited | Limited | Limited |

---

## When to Use This Skill

- Setting up an **end-to-end EEG/MEG analysis pipeline** in MATLAB
- Comparing multiple **source localization methods** (MNE, dSPM, sLORETA, beamforming)
- Performing **functional connectivity** and **graph-theoretic** analysis
- Running **machine learning classification** on EEG/MEG features
- Generating **academic reports** automatically
- Migrating between **Brainstorm/FieldTrip/EEGLAB** workflows

---

## References

```
@article{liu2026mle,
  title = {MLE-Toolbox: An Open-Source Toolbox for Comprehensive EEG and MEG Data Analysis},
  author = {Liu, Xiaobo},
  journal = {arXiv preprint},
  year = {2026},
  eprint = {2604.16463},
  primaryClass = {q-bio.NC},
  secondaryClass = {cs.AI},
  url = {https://arxiv.org/abs/2604.16463},
  date = {2026-04-08}
}
```

---

## Related Skills

- `hermes-brain-connectivity`
- `eeg-brain-connectivity-bci`
- `eeg-hopfield-emotion-energy`
- `geometric-brain-dynamics-mapping-v7`
- `brain-network-controllability`
