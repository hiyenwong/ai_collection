---
name: time2-neural-dynamics-visual-perception
title: Time² Framework for Neural Dynamics of Visual Perception
description: Time² (Time-squared) framework methodology for analyzing neural dynamics by simultaneously considering both processing time and stimulus time dimensions in visual perception research using reverse correlation.
trigger: When studying neural dynamics of visual perception, especially when needing to disentangle processing time from stimulus time using reverse correlation methods.
---

# Time² Framework for Neural Dynamics of Visual Perception

## Overview
The Time² (Time-squared) framework is a novel methodological approach based on reverse correlation that simultaneously considers both temporal facets of visual perception:
- **Processing time**: The time it takes for the brain to process visual information after it reaches the retina
- **Stimulus time**: The continuous duration during which visual information is received on the retina

Traditional studies typically focus on only one of these dimensions, but the Time² framework enables researchers to characterize neural phenomena more comprehensively by measuring both simultaneously.

## Core Methodology

### Experimental Design
1. **Stimulus Creation**: Create three-dimensional stimuli where two dimensions represent pixel space and one dimension represents stimulus time
2. **Spatio-temporal Noise**: Fill the 3D array with three-dimensional Gaussian apertures ("Spacetime Bubbles")
3. **Element-wise Multiplication**: Multiply the noise array element-wise with a base image replicated across stimulus time
4. **Presentation**: Present the resulting spacetime stimulus with randomly sampled spatial parts across time

### Data Collection
- Record temporally resolved brain activity (e.g., MEG, EEG) concurrent with stimulus presentation
- Ensure high temporal resolution to capture both stimulus and processing dynamics

### Analysis Pipeline
1. **Regression Analysis**: For each brain source and processing latency, regress brain activity onto Spacetime Bubbles values for each pixel/spatial feature and stimulus moment across trials
2. **Time² Map Generation**: Arrange regression coefficients to create Time² maps for each brain location and spatial feature
3. **Map Interpretation**: 
   - Y-axis: Stimulus time (from bottom to top)
   - X-axis: Processing time (from left to right)
   - Diagonal patterns indicate constant processing delays
   - Complex patterns reveal hierarchical processing dynamics

## Applications
The Time² framework enables precise characterization of:
- **Rhythmic perception**: How oscillatory brain activity processes temporal information
- **Predictive processing**: How the brain uses early stimulus information to predict later content
- **Coarse-to-fine sampling**: How visual processing evolves from global to detailed features over time
- **Neural hierarchy analysis**: Different processing patterns across cortical areas (early vs. higher visual areas)

## Implementation Considerations
- Requires high-temporal-resolution neuroimaging (MEG/EEG preferred over fMRI)
- Stimulus presentation must be precisely controlled with millisecond accuracy
- Statistical power requires sufficient trial numbers due to the multidimensional nature of the analysis
- Clustering analysis can identify distinct Time² map types across brain regions

## Key References
- Caplette, L., & Gosselin, F. (2026). Time²: A framework for the neural dynamics of visual perception. arXiv:2608.04218
- Caplette et al. (2020, 2023). Previous foundational work on spatio-temporal reverse correlation
- VanRullen & MacDonald (2012). Processing time studies using EEG cross-correlation
- Neri & Levi (2007). Stimulus time studies using reverse correlation

## Activation Keywords
time2, time-squared, neural dynamics, visual perception, processing time, stimulus time, reverse correlation, spacetime bubbles, temporal facets