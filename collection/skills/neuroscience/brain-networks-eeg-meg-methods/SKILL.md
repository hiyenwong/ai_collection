---
name: brain-networks-eeg-meg-methods
description: Skill for EEG/MEG-based brain network analysis covering forward/inverse problems, connectivity measures, and pipelines.
category: ai_collection/neuroscience
---

## Context
This skill provides a structured approach to analyzing brain networks using noninvasive electrophysiological measurements (EEG/MEG) based on the arXiv chapter "Exploring Brain Networks Using Noninvasive Electrophysiological Measurements: Methods and Applications" (arXiv:2607.17602). It covers the full pipeline from preprocessing to connectivity analysis, emphasizing methodological rigor and practical implementation.

## Core Methodology

1. **Understand the physical principles of EEG and MEG**
   - Recognize EEG measures electrical potentials, MEG measures magnetic fields.
   - Appreciate their complementary spatiotemporal characteristics and sensitivity to different neural sources.

2. **Model the forward problem**
   - Construct a subject-specific head model (e.g., using individual MRI for conductivity boundaries).
   - Compute the lead field matrix that maps neural sources to sensor signals.

3. **Address the inverse problem**
   - Apply source reconstruction techniques (e.g., minimum norm estimate, beamforming) to estimate neural activity from sensor data.
   - Prioritize accurate anatomical modeling to improve source localization accuracy.

4. **Mitigate volume conduction and signal leakage**
   - Use techniques such as orthogonalization, imaginary part of coherence, or source-space orthogonalization to reduce spurious zero-lag correlations.
   - Apply leakage-corrected connectivity metrics (e.g., phase lag index, imaginary coherence).

5. **Select appropriate connectivity measures**
   - For functional connectivity: coherence, amplitude envelope correlation.
   - For directional/effective connectivity: Granger causality, transfer entropy, dynamic causal modeling.
   - Choose based on hypotheses about interaction directionality and linearity/nonlinearity.

6. **Implement analysis pipelines**
   - Use established open-source toolboxes like Brainstorm, FieldTrip, or MNE-Python for reproducibility.
   - Follow best practices for preprocessing (filtering, artifact removal, epoching).

7. **Explore advanced connectivity analyses**
   - Investigate time-varying connectivity (e.g., sliding window, wavelet coherence).
   - Examine cross-frequency interactions (e.g., phase-amplitude coupling).
   - Apply network-based analyses (graph theory metrics) to characterize brain network topology.

8. **Validate and interpret results**
   - Compare findings with known anatomy and physiology.
   - Validate using simulations or alternative methods.
   - Relate network properties to behavioral or clinical variables.

## Implementation Steps
- Obtain high-quality EEG/MEG recordings with proper electrode/sensor placement.
- Preprocess data: bandpass filter, remove line noise, detect and reject artifacts (e.g., eye blinks, muscle activity).
- Coregister sensors with individual anatomical MRI if available.
- Compute forward model using a realistic head model (e.g., BEM or FEM).
- Apply inverse solution to obtain source time series (optional, depending on analysis level).
- Perform connectivity analysis in sensor or source space using chosen metrics.
- Correct for volume conduction/spurious interactions as needed.
- For network analysis, construct adjacency matrices and compute graph metrics (e.g., clustering coefficient, path length, small-worldness).
- Statistical testing: use non-parametric permutation tests or FDR correction for multiple comparisons.
- Visualize results using brain plotting tools (e.g., BrainNet Viewer, matplotlib with cortical surfaces).

## Pitfalls
- Ignoring individual anatomy can lead to significant localization errors.
- Misinterpreting zero-lag correlations as genuine interactions without correcting for volume conduction.
- Using inappropriate connectivity measures for the research question (e.g., using correlation for directed influences).
- Overlooking multiple comparisons corrections in network-based statistics.
- Assuming stationarity when analyzing non-stationary brain signals without time-varying approaches.

## Verification
- Verify that preprocessing steps adequately remove artifacts without distorting neural signals.
- Check that forward model accurately predicts sensor signals from known dipoles (simulation).
- Ensure inverse solution yields spatially plausible source distributions.
- Confirm that connectivity results change plausibly with known manipulations (e.g., eyes open vs closed).
- Validate pipeline on simulated data with known ground truth connections.

## Activation Keywords
- EEG MEG brain network connectivity
- noninvasive electrophysiology source reconstruction
- coherence Granger causality dynamic causal modeling
- volume conduction leakage correction
- Brainstorm MNE-Python FieldTrip pipeline
- time-varying connectivity cross-frequency coupling
- graph theory brain network analysis