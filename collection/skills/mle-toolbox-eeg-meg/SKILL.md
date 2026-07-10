---
name: mle-toolbox-eeg-meg
description: "MLE-Toolbox: Comprehensive open-source MATLAB toolbox for end-to-end EEG/MEG analysis with source localization, connectivity analysis, and ML classifiers. Activation: MLE-Toolbox, EEG analysis, MEG analysis, source localization, brain network analysis, neuroimaging toolbox."
---

# MLE-Toolbox: Comprehensive EEG/MEG Analysis

> Open-source MATLAB toolbox integrating full EEG/MEG analysis pipeline with preprocessing, source localization, functional connectivity, and machine learning classification.

## Metadata
- **Source**: arXiv:2604.16463
- **Authors**: Xiaobo Liu
- **Published**: 2026-04-08
- **Categories**: Neurons and Cognition (q-bio.NC); Artificial Intelligence (cs.AI); Software Engineering (cs.SE)

## Core Methodology

### Design Philosophy
Inspired by established neuroimaging platforms (Brainstorm, FieldTrip, EEGLAB), MLE-Toolbox provides unified, user-friendly GUI for complete EEG/MEG analysis workflow.

### Full Analysis Pipeline
```
Raw Data → Preprocessing → Source Localization → Connectivity → ML Classification
```

## Key Features

### 1. Preprocessing
**Automated Artifact Rejection:**
- Independent Component Analysis (ICA)
- Signal-Space Projection (SSP)
- Signal-Space Separation (SSS)

### 2. Source Localization Methods
Multiple inverse solutions:
- **MNE**: Minimum Norm Estimation
- **dSPM**: Dynamic Statistical Parametric Mapping
- **sLORETA**: Standardized Low-Resolution Brain Electromagnetic Tomography
- **Beamforming**: Adaptive spatial filtering

### 3. Parcellation & Visualization
- Multi-atlas parcellation
- Anatomical visualization
- Brain region segmentation

### 4. Spectral Analysis
- Spectral power analysis
- Frequency-band brain mapping
- Phase-Amplitude Coupling (PAC)

### 5. Connectivity Analysis
- Graph-theoretic brain network analysis
- Functional connectivity estimation
- Network topology metrics

### 6. Machine Learning
- Integrated classifiers
- Deep learning integration
- Feature extraction pipelines

## Implementation Guide

### Prerequisites
- MATLAB (R2018b or later recommended)
- Signal Processing Toolbox
- Statistics and Machine Learning Toolbox
- GPU support optional (for deep learning)

### Installation
```matlab
% Clone or download MLE-Toolbox
% Add to MATLAB path
addpath(genpath('/path/to/mle-toolbox'))
mle_startup
```

### Basic Workflow

#### 1. Data Import
```matlab
% Import raw EEG/MEG data
data = mle_import('filename.eeg', 'format', 'eeglab');
```

#### 2. Preprocessing
```matlab
% Artifact rejection with ICA
[data_clean, ica_weights] = mle_ica_reject(data, 'n_components', 32);

% SSP for environmental noise
[data_clean] = mle_ssp(data_clean, 'n_projectors', 8);
```

#### 3. Source Localization
```matlab
% Compute forward model
headmodel = mle_headmodel(subject);

% Minimum norm estimation
sources = mne_solve(data_clean, headmodel, 'method', 'mne');

% Or beamforming
sources = mne_solve(data_clean, headmodel, 'method', 'beamformer');
```

#### 4. Connectivity Analysis
```matlab
% Compute connectivity matrix
conn_matrix = mle_connectivity(sources, 'method', 'pli');

% Graph theory metrics
metrics = mle_graph_metrics(conn_matrix, 'metrics', {'clustering', 'path_length'});
```

#### 5. Machine Learning
```matlab
% Train classifier
[model, accuracy] = mle_classify(features, labels, 'method', 'svm');

% Cross-validation
[model, cv_accuracy] = mle_classify_cv(features, labels, 'kfold', 10);
```

## Advanced Features

### Interoperability
Native compatibility with major platforms:
- **Brainstorm**: Import/export protocols
- **FieldTrip**: Data format conversion
- **EEGLAB**: .set file support
- **FreeSurfer**: Surface and volume import

### Report Generation
One-click academic report generation:
```matlab
mle_generate_report(analysis_results, 'format', 'pdf', 'template', 'neuroimage');
```

### Interactive Visualization
```matlab
% Brain surface visualization
mle_visualize_brain(sources, 'surface', 'pial', 'colormap', 'jet');

% Time-frequency plots
mle_plot_tfr(data, 'channels', {'Cz', 'Pz', 'Oz'});

% Connectivity graphs
mle_plot_connectivity(conn_matrix, 'atlas', 'aal');
```

## Applications

### Clinical Research
- Epilepsy source localization
- Stroke rehabilitation monitoring
- Sleep disorder analysis

### Cognitive Neuroscience
- Working memory studies
- Attention network analysis
- Language processing research

### BCI Development
- Motor imagery decoding
- P300 spellers
- Error-related potential detection

### Drug Development
- Pharmacological EEG studies
- Biomarker discovery
- Treatment response monitoring

## Comparison with Existing Tools

| Feature | MLE-Toolbox | Brainstorm | FieldTrip | EEGLAB |
|---------|-------------|------------|-----------|--------|
| GUI | ✓ Integrated | ✓ | ✗ | ✓ |
| Source Loc. | MNE, dSPM, sLORETA, Beamforming | Dipole, MNE | Beamforming | Dipole |
| Connectivity | ✓ Graph-theoretic | ✓ | ✓ | Limited |
| ML Integration | ✓ Built-in | ✗ | ✗ | Limited |
| Report Gen | ✓ One-click | Manual | Manual | ✓ |
| Interoperability | All major tools | Limited | Limited | EEGLAB only |

## Pitfalls

### Common Issues
- **Memory**: Large datasets may require downsampling or chunking
- **Head Models**: Accurate source localization requires precise head models
- **ICA Interpretation**: Requires expertise to identify artifact components

### Best Practices
1. Always inspect raw data before preprocessing
2. Use subject-specific head models when possible
3. Validate source localization with known functional landmarks
4. Apply appropriate statistical corrections for multiple comparisons

## License
Freely available for non-commercial use.

## Related Skills
- eeg-hopfield-emotion-energy
- eeg-structure-guided-diffusion
- functional-connectivity-graph-neural-networks

## References
- Liu, X. (2026). MLE-Toolbox: An Open-Source Toolbox for Comprehensive EEG and MEG Data Analysis. arXiv:2604.16463.
- Brainstorm: https://neuroimage.usc.edu/brainstorm
- FieldTrip: https://www.fieldtriptoolbox.org
- EEGLAB: https://sccn.ucsd.edu/eeglab
