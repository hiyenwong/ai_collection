---
name: time2-neural-dynamics-visual-perception
title: Time² Framework for Neural Dynamics of Visual Perception
version: 1.0.0
description: Time² (Time-squared) framework methodology for analyzing neural dynamics in visual perception by distinguishing between processing time and stimulus time dimensions. Enables characterization of rhythmic perception, predictive processing, and coarse-to-fine sampling through reverse correlation analysis.
tags:
  - neuroscience
  - neural dynamics
  - visual perception
  - time-series analysis
  - MEG/EEG
  - reverse correlation
  - computational neuroscience
authors:
  - Laurent Caplette
  - Frédéric Gosselin
paper: "Time²: A framework for the neural dynamics of visual perception"
arxiv_id: "2608.04218"
date: "2026-08-04"
---

# Time² Framework for Neural Dynamics of Visual Perception

## Overview

The Time² (Time-squared) framework is a novel experimental and analytical methodology that disentangles two critical temporal dimensions in visual perception:

1. **Processing time**: The time it takes for the brain to process visual information after it reaches the retina (typically 100-150ms)
2. **Stimulus time**: The duration during which visual information is continuously received on the retina while viewing an object

Traditional neuroscience methods often conflate these two temporal facets or consider only one dimension at a time. Time² enables simultaneous measurement and analysis of both dimensions using reverse correlation techniques.

## Key Concepts

### Dual Temporal Dimensions
- **Processing time** represents neural computation latency across the cortical hierarchy
- **Stimulus time** represents the continuous sampling of visual input during fixation
- Both dimensions must be considered together to obtain a complete portrait of visual perception

### Reverse Correlation Implementation
The Time² method uses spacetime stimuli created by:
1. Generating 3D noise arrays (spacetime bubbles) with Gaussian apertures across pixel space and stimulus time
2. Multiplying these noise arrays element-wise with base images replicated across stimulus time
3. Presenting dynamic spacetime stimuli to participants while recording neural activity (MEG/EEG)

### Analysis Framework
For each brain source and processing latency, regression is performed against spacetime bubble values for each pixel and stimulus moment across trials. This produces Time² maps where:
- **Y-axis**: Stimulus time (from bottom to top)
- **X-axis**: Processing time (from left to right)
- **Diagonal patterns**: Indicate constant processing delays
- **Off-diagonal patterns**: Reveal complex temporal dynamics

## Applications

### Rhythmic Perception
- Characterizes how ongoing neural oscillations interact with continuously incoming visual information
- Distinguishes between **oscillatory sampling** (information received at successive moments processed rhythmically) vs **oscillatory processing** (single snapshot processed rhythmically across time)

### Predictive Processing
- Analyzes how changes in early stimulus portions affect processing of later portions
- Reveals adaptive sampling mechanisms in response to prediction errors

### Information Maintenance
- Studies how representations of sequential scenes overlap in time
- Examines temporal binding of asynchronously processed features

### Coarse-to-Fine Sampling
- Tracks how different spatial frequencies are processed across both temporal dimensions
- Reveals hierarchical processing dynamics

## Implementation Guidelines

### Experimental Design
1. **Stimulus Creation**: Use 3D Gaussian apertures (spacetime bubbles) spanning 200-500ms stimulus duration
2. **Base Images**: Select appropriate visual categories (faces, objects, scenes)
3. **Neural Recording**: MEG preferred for source localization, EEG acceptable with appropriate referencing
4. **Task Design**: Include behavioral measures (detection, discrimination, recognition) for filter gain analysis

### Data Analysis
1. **Preprocessing**: Standard MEG/EEG preprocessing (filtering, artifact rejection, source localization for MEG)
2. **Reverse Correlation**: Regress neural activity against spacetime bubble values
3. **Time² Map Construction**: Create 2D maps for each brain source and spatial feature
4. **Statistical Analysis**: Use clustering to identify map types, compare across conditions/regions

### Interpretation Framework
- **Slope-of-1 diagonal**: Constant processing delay regardless of stimulus moment
- **Above diagonal**: Processing of later stimulus moments occurs earlier than expected
- **Below diagonal**: Processing of later stimulus moments occurs later than expected
- **Oscillatory patterns**: Reveal rhythmic sampling or processing at specific frequencies

## Advantages Over Traditional Methods

1. **Simultaneous temporal measurement**: Captures both processing and stimulus time dimensions
2. **High temporal resolution**: Millisecond-level precision in both dimensions
3. **Spatial specificity**: Can analyze specific brain regions and visual features
4. **Model constraint**: Provides rich data to constrain computational models of vision
5. **Phenomenon unification**: Integrates multiple temporal phenomena under single framework

## Limitations and Considerations

1. **Computational complexity**: Requires substantial data collection and processing
2. **Signal-to-noise ratio**: May require many trials for reliable estimates
3. **Source localization**: MEG source reconstruction adds complexity; EEG has limited spatial resolution
4. **Stimulus design constraints**: Base images must be compatible with spacetime bubble multiplication

## Use Cases

- **Fundamental vision research**: Understanding temporal dynamics of visual processing
- **Clinical applications**: Characterizing temporal processing deficits in neurological disorders
- **Computational modeling**: Constraining and validating neural network models of vision
- **Brain-computer interfaces**: Optimizing temporal parameters for visual BCI systems
- **Cognitive neuroscience**: Studying attention, prediction, and consciousness mechanisms

## Trigger Conditions

Use when: studying neural dynamics of visual perception, analyzing MEG/EEG time-series data, investigating rhythmic brain activity, or developing computational models of vision that require precise temporal characterization.

## References

- Caplette, L., & Gosselin, F. (2026). Time²: A framework for the neural dynamics of visual perception. arXiv:2608.04218 [q-bio.NC].
- Caplette, L., et al. (2023). [Related work on oscillatory sampling patterns]
- VanRullen, R., & MacDonald, C. (2012). [Foundational work on processing time analysis]

## Verification Steps

1. Successfully implement spacetime bubble stimulus generation
2. Obtain significant reverse correlation coefficients above chance level
3. Identify expected Time² map patterns (diagonal, oscillatory, etc.)
4. Replicate known phenomena (e.g., alpha-band oscillatory sampling)
5. Validate with behavioral performance correlations