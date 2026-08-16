---
name: trophic-structure-seizure-propagation
description: "Trophic structure predicts seizure propagation."
metadata:
  arxiv_id: "2608.12382"
  authors: "Kissack, Peter; Drysdale, Catherine; Johnson, Samuel"
  published: "2026-07-30"
  tags: [brain-networks, epilepsy, seizure-propagation, trophic-coherence, spectral-radius, directed-networks]
license: Complete terms in LICENSE.txt
---

# Trophic Structure Predicts Seizure Propagation in Brain Network Models

## Overview

This research investigates how structural properties of directed brain networks affect seizure propensity in epilepsy. Using a model of seizure dynamics on directed networks, the authors demonstrate that properties such as trophic coherence, spectral radius, strong connectivity, and non-normality are closely related to seizure propensity.

The key finding is that the overall directionality of information processing in the brain may be fundamentally related to a propensity for epileptic seizures, providing new insights into the structural basis of epilepsy as a network disorder.

## Core Contributions

1. **Structural Property Analysis**: Comprehensive analysis of how trophic coherence, spectral radius, strong connectivity, and non-normality relate to seizure propensity in directed brain networks.

2. **Theoretical Relationship Proof**: Mathematical proof of the theoretical relationship between spectral radius and cycle structure in directed networks.

3. **Model Robustness**: Demonstrated that results are robust to different coupling mechanisms used in the seizure dynamics model.

4. **Network Size Scaling**: Showed that the relationships become stronger as network size increases, suggesting scalability to real brain networks.

## Methodology

### Network Model
- **Directed Networks**: Brain connectivity represented as directed graphs capturing information flow directionality
- **Trophic Coherence**: Measure of hierarchical organization in directed networks
- **Spectral Properties**: Analysis of eigenvalue spectra and spectral radius
- **Connectivity Measures**: Strong connectivity and non-normality as structural indicators

### Seizure Dynamics Model
- **Dynamical System**: Simulated seizure-like activity propagation on network structures
- **Coupling Variants**: Tested multiple coupling mechanisms to ensure robustness
- **Propensity Metrics**: Quantified seizure propensity based on network response characteristics

### Analysis Framework
1. **Network Generation**: Create directed networks with varying structural properties
2. **Dynamics Simulation**: Run seizure dynamics model on each network
3. **Propensity Correlation**: Correlate structural properties with seizure propensity measures
4. **Statistical Validation**: Validate findings across network sizes and coupling types

## Key Findings

- **Trophic Coherence**: Higher trophic coherence (more hierarchical structure) correlates with lower seizure propensity
- **Spectral Radius**: Larger spectral radius correlates with higher seizure propensity
- **Strong Connectivity**: Networks with stronger overall connectivity show increased seizure susceptibility  
- **Non-normality**: Higher non-normality in adjacency matrices relates to greater seizure propensity
- **Directionality**: Overall directionality of information processing is a key factor in seizure susceptibility

## Applications

- **Epilepsy Research**: Provides structural biomarkers for seizure susceptibility prediction
- **Brain Network Analysis**: Framework for analyzing directed functional connectivity in neurological disorders
- **Therapeutic Targeting**: Identifies network structural properties as potential intervention targets
- **Computational Neuroscience**: Advances understanding of how network topology influences neural dynamics

## Implementation Considerations

- **Data Requirements**: Requires directed connectivity data (e.g., from Granger causality, dynamic causal modeling)
- **Computational Complexity**: Spectral analysis scales with network size but remains tractable for typical brain networks
- **Validation**: Should be validated against empirical seizure data from EEG/MEG/ECoG recordings
- **Individual Variability**: Account for individual differences in brain network structure

## Activation Keywords

- trophic structure seizure propagation
- brain network epilepsy
- directed network seizure dynamics
- trophic coherence epilepsy
- spectral radius brain networks
- seizure propensity prediction

## References

- Original paper: Kissack, Peter; Drysdale, Catherine; Johnson, Samuel. "Trophic structure predicts seizure propagation in brain network models" (arXiv:2608.12382)
- Related work: seizure-suppression-hub-stimulation, brain-network-controllability, hermes-brain-connectivity