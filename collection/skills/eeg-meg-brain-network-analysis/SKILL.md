---
name: eeg-meg-brain-network-analysis
description: "Skill for analyzing brain networks using noninvasive electrophysiological measurements (EEG/MEG) based on arXiv:2607.17602v1 'Exploring Brain Networks Using Noninvasive Electrophysiological Measurements: Methods and Applications'"
---

## Overview
This skill provides a structured approach to analyzing brain networks using EEG and MEG data, covering preprocessing, source reconstruction, connectivity analysis, and network-based methods as outlined in the referenced paper.

## Activation
Trigger this skill when you need to:
- Analyze EEG/MEG data for brain network connectivity
- Apply source localization techniques
- Compute functional or effective connectivity measures
- Perform network-based analysis on electrophysiological data

## Steps

### 1. Data Preprocessing
- **Import raw EEG/MEG data** using appropriate toolboxes (e.g., EEGLAB, MNE-Python, FieldTrip)
- **Apply filtering**: bandpass (typically 0.1-100 Hz) and notch filters (50/60 Hz) to remove line noise
- **Detrend and remove bad channels** using visual inspection or automated methods
- **Re-reference** to average reference or reference electrode standard technique (REST)
- **Segment data** into epochs of interest (e.g., stimulus-locked or resting-state)
- **Baseline correction** if applicable
- **Artifact removal**: Use ICA or PCA to remove ocular, cardiac, and muscle artifacts

### 2. Forward Modeling and Source Reconstruction
- **Obtain individual MRI** or use template MRI (e.g., MNI) for head model construction
- **Conductivity assignment**: Assign conductivities to scalp, skull, CSF, brain tissues
- **Compute lead field matrix** using boundary element method (BEM) or finite element method (FEM)
- **Apply inverse solution**:
  - Minimum norm estimate (MNE)
  - LORETA (Low Resolution Electromagnetic Tomography)
  - Beamforming (LCMV - Linearly Constrained Minimum Variance)
  - MUSIC (Multiple Signal Classification)
- **Source space definition**: Choose cortical surface mesh or volumetric grid
- **Apply orientation constraints** (fixed or free orientation)
- **Regularization**: Tikhonov regularization with appropriate lambda

### 3. Connectivity Analysis
Choose appropriate connectivity measure based on research question:

#### Functional Connectivity (Zero-lag or linear mixing)
- **Coherence**: Frequency-specific correlation
- **Phase Locking Value (PLV)**: Phase synchronization
- **Phase Lag Index (PLI)**: Asymmetric component of phase synchronization
- **Imaginary part of coherency**: Eliminates zero-lag artifacts
- **Amplitude Envelope Correlation (AEC)**: Correlates amplitude envelopes in frequency bands

#### Effective Connectivity (Directional, causal inference)
- **Granger Causality (GC)**: Predictive influence in time/frequency domain
- **Directed Transfer Function (DTF)**: Frequency-domain GC
- **Partial Directed Coherence (PDC)**: Normalized GC
- **Dynamic Causal Modeling (DCM)**: Biophysical model of neuronal populations
- **Transfer Entropy (TE)**: Model-free, information-theoretic measure

### 4. Network Construction and Analysis
- **Define nodes**: Brain regions of interest (ROIs) from atlas (e.g., AAL, Desikan-Killiany) or data-driven parcels
- **Define edges**: Weighted by connectivity measure values above threshold
- **Apply thresholding**:
  - Proportional threshold (keep top X% strongest connections)
  - Absolute threshold (statistical significance via surrogate testing)
  - Adaptive thresholding (e.g., False Discovery Rate correction)
- **Compute network metrics**:
  - **Global**: Characteristic path length, clustering coefficient, small-worldness, global efficiency
  - **Nodal**: Degree, betweenness centrality, eigenvector centrality, local efficiency
  - **Motif analysis**: Frequency of subgraph patterns
  - **Rich-club organization**: Rich-club coefficient
- **Statistical comparison**: Use permutation testing or false discovery rate for group comparisons

### 5. Advanced Analyses
- **Time-varying connectivity**: Sliding window or time-frequency resolved methods
- **Cross-frequency coupling**: Phase-amplitude modulation (PAC) analysis
- **Multiscale entropy**: Complexity of neural signals
- **Machine learning integration**: Use network features for classification/regression
- **Simulation validation**: Compare with generative models (e.g., Kuramoto oscillators)

## Validation and Quality Control
- **Signal-to-noise ratio (SNR)** assessment
- **Split-half reliability** or test-retest reliability
- **Surrogate data testing** for significance of connectivity measures
- **Comparison with anatomical connectivity** (e.g., from DTI)
- **Visual inspection** of source estimates and connectivity matrices
- **Control for volume conduction and signal leakage** using appropriate metrics (e.g., PLI, imaginary coherency)

## Software and Tools
- **EEGLAB** (MATLAB) - https://sccn.ucsd.edu/eeglab/
- **MEG-Python (MNE-Python)** - https://mne.tools/
- **FieldTrip** (MATLAB) - https://www.fieldtriptoolbox.org/
- **Brainstorm** (MATLAB) - https://neuroimage.usc.edu/brainstorm/
- **NetMat** (MATLAB) - https://github.com/CollectiveDynamicsLab/netmat
- **Brain Connectivity Toolbox (BCT)** - https://sites.google.com/site/bctnet/
- **TVB (The Virtual Brain)** - https://www.thevirtualbrain.org/
- **TENSORFLOW / PYTORCH** for deep learning approaches

## Pitfalls and Best Practices
- **Volume conduction**: Zero-lag correlations can be spurious; use imaginary part of coherency or PLI
- **Reference dependence**: EEG references affect connectivity; consider reference-free techniques (e.g., Laplacian, REST)
- **Volume conductor model accuracy**: Individual head models improve source localization accuracy
- **Multiple comparisons**: Correct for multiple comparisons across frequencies, connections, and time points
- **Stationarity assumption**: Ensure data is sufficiently stationary for chosen methods; consider time-varying approaches
- **Interpretability**: Distinguish between statistical significance and biological relevance
- **Reproducibility**: Share preprocessing pipelines, parameters, and code (e.g., via OSF, GitHub)

## References
- Primary: arXiv:2607.17602v1 "Exploring Brain Networks Using Noninvasive Electrophysiological Measurements: Methods and Applications"
- Supplementary: Standard EEG/MEG textbooks and toolbox documentation
- Related: Brain Connectivity Toolbox (Rubinov & Sporns, 2010), FieldTrip tutorial series

## Example Workflow (MNE-Python)
```python
import mne
import numpy as np
from mne.connectivity import spectral_connectivity

# Load raw data
raw = mne.io.read_raw_fif('raw_data.fif', preload=True)

# Preprocessing
raw.filter(1., 40., fir_design='firwin')
raw.notch_filter(np.arange(50, 201, 50))
ica = mne.preprocessing.ICA(n_components=20, random_state=97)
ica.fit(raw)
raw_clean = ica.apply(raw.copy())

# Epoching
events = mne.find_events(raw_clean)
epochs = mne.Epochs(raw_clean, events, event_id={'stim': 1}, tmin=-0.2, tmax=0.5,
                    baseline=(-0.2, 0), preload=True)

# Forward model
conductivity = (0.3, 0.006, 0.3)  # skull conductivity reduced
model = mne.make_bem_model(epochs.info, subject='sample', 
                           subjects_dir='/path/to/freesurfer',
                           conductivity=conductivity)
bem = mne.make_bem_solution(model)
src = mne.setup_source_space(epochs.info, subject='sample',
                             subjects_dir='/path/to/freesurfer',
                             spacing='oct6')
fwd = mne.make_forward_solution(epochs.info, trans='sample-trans.fif',
                                src=src, bem=bem, eeg=True, meg=False,
                                mindist=5.0)

# Inverse solution
cov = mne.compute_covariance(epochs, tmax=0., method=['empirical', 'cov'])
inv = mne.minimum_norm.make_inverse_operator(epochs.info, fwd, cov,
                                             loose=0.2, depth=0.8)
stc = mne.minimum_norm.apply_inverse_epochs(epochs, inv, lambda2=1./9., 
                                            method='MNE', return_generator=True)

# Extract source time series for ROI
label = mne.read_labels_from_annot('sample', parc='aparc', 
                                   subjects_dir='/path/to/freesurfer')[0]  # example label
stc_label = [stc_in.label(label) for stc_in stc]
ts = np.array([sc.extract()[0] for sc in stc_label])  # shape (n_epochs, n_vertices, n_times)

# Connectivity analysis (example: coherence in beta band)
sfreq = epochs.info['sfreq']
fmin, fmax = 15, 25
con, freq, times, n_epochs, n_tapers = spectral_connectivity(
    stc_label, mode='coh', sfreq=sfreq, fmin=fmin, fmax=fmax,
    faverage=True, mt_adaptive=False, n_jobs=1)

# Average over frequencies and epochs
con_avg = np.mean(con, axis=(0, -1))  # shape (n_vertices, n_vertices)

# Threshold and analyze with BCT
import bct
threshold = np.percentile(con_avg, 75)  # keep top 25%
adj = (con_avg > threshold).astype(float)
binarized = binarize(adj, copy=True)  # from bct
degrees = bc.degrees_und(binarized)
```

## Customization
- Adjust frequency bands of interest (delta, theta, alpha, beta, gamma)
- Choose inverse method based on spatial resolution and SNR requirements
- Select connectivity measures based on hypothesis (undirected vs directed)
- Adapt pipeline for specific experimental designs (resting-state, task-based, sleep)

## Validation
After implementing this skill, verify:
- Preprocessing steps reduce artifacts without removing neural signals
- Source localization yields physiologically plausible dipoles
- Connectivity matrices show expected patterns (e.g., higher connectivity within known networks)
- Network metrics align with prior literature for similar conditions
- Results survive surrogate testing and multiple comparison corrections

---
*Skill generated from arXiv:2607.17602v1 on 2026-07-21 via automated cron job.*