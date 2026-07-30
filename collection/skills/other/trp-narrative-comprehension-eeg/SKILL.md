---
name: trp-narrative-comprehension-eeg
description: Transition-Related Potentials (TRPs) methodology for analyzing narrative comprehension in continuous EEG recordings using deep neural networks to detect cinematic cuts and extract context-dependent brain responses.
trigger: When analyzing continuous EEG data for narrative comprehension, naturalistic stimuli processing, or detecting transition-related brain potentials in film viewing experiments.
---

# Transition-Related Potentials as Markers of Narrative Comprehension in Continuous EEG

## Overview
This methodology extracts Transition-Related Potentials (TRPs) from continuous EEG recordings during naturalistic film viewing. TRPs are ERP-like responses aligned to sharp cinematic transitions (cuts) that exhibit canonical temporal structure and are systematically shaped by narrative context. A compact deep neural network can detect these signatures directly from group-averaged continuous recordings, providing a semi-automated framework for analyzing how viewers process and understand narratives.

## Core Methodology

### 1. Data Collection Setup
- Collect continuous EEG while participants watch short films
- Use both coherent films and scene-scrambled versions with matched post-cut sensory input
- Ensure proper electrode placement and signal quality for naturalistic viewing conditions

### 2. Transition Detection
- Manually annotate cinematic cuts in films as ground truth
- Train a compact deep neural network (DNN) to detect cut-related EEG signatures directly from continuous recordings
- The DNN should generalize across different films and subject groups

### 3. TRP Extraction and Analysis
- Extract potentials aligned to detected transitions (both manual and DNN-detected)
- Compare TRPs between coherent films vs. scene-scrambled versions
- Analyze temporal structure of TRPs to identify canonical ERP-like components
- Measure context-dependent effects on amplitude, latency, and topography

### 4. Validation Framework
- Verify that DNN-detected TRPs reproduce main context-dependent effects observed with manually annotated cuts
- Test generalization across different film types and subject populations
- Validate that narrative context (not just sensory changes) shapes the responses

## Key Applications

### Naturalistic Neuroscience
- Move beyond traditional ERP paradigms to study brain responses in natural viewing conditions
- Analyze how narrative structure influences neural processing during continuous stimulation
- Provide insights into real-world cognitive processing during media consumption

### Semi-Automated EEG Analysis
- Reduce manual annotation burden for large-scale continuous EEG studies
- Enable scalable analysis of naturalistic stimuli across multiple experiments
- Provide robust detection of meaningful neural events in noisy continuous recordings

### Cross-Modal Integration
- Study how visual transitions integrate with narrative comprehension
- Investigate temporal dynamics of information processing during scene changes
- Explore individual differences in narrative processing styles

## Implementation Guidelines

### Neural Network Architecture
- Use a compact DNN architecture suitable for detecting transient EEG signatures
- Train on group-averaged data to improve signal-to-noise ratio
- Include temporal context windows around potential transition points

### Experimental Design
- Include control conditions with matched sensory input but disrupted narrative structure
- Use diverse film types to test generalizability
- Consider individual differences in narrative comprehension abilities

### Analysis Pipeline
1. Preprocess continuous EEG data (filtering, artifact removal)
2. Apply DNN detector to identify transition-related timepoints
3. Extract epochs around detected transitions
4. Compute average TRPs for different conditions
5. Perform statistical comparisons between coherent vs. scrambled narratives
6. Analyze spatial topography and source localization if applicable

## Pitfalls and Considerations

- **Signal-to-Noise Ratio**: Continuous EEG has higher noise than traditional ERP paradigms; group averaging and robust detection algorithms are essential
- **Narrative vs. Sensory Confounds**: Ensure that effects are truly due to narrative context rather than low-level visual features
- **Individual Variability**: Account for differences in attention, comprehension, and viewing behavior across participants
- **Generalization**: Test whether the DNN detector works across different types of transitions and media formats

## Activation Keywords
transition-related potentials, TRP, continuous EEG, narrative comprehension, naturalistic neuroscience, cinematic cuts, deep neural network EEG detection, film viewing EEG, context-dependent brain responses

## References
- Csanády, B., Vedres, P., Makó, K. Z., Papp-Zipernovszky, O., Volosin, M., Apagyi, D., Lukács, A., Kovács, A. B., & Nadasdy, Z. (2026). Transition-Related Potentials as Markers of Narrative Comprehension in Continuous EEG. arXiv:2607.20720 [q-bio.NC]