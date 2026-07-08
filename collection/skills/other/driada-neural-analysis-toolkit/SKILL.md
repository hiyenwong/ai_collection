---
name: driada-neural-analysis-toolkit
description: "DRIADA - Python toolkit for cross-scale analysis of single-neuron selectivity and population dynamics. Enables unified analysis from single-cell selectivity to population-level dynamics in neuroscience experiments."
trigger_words: ["driada", "cross-scale neural analysis", "single-neuron selectivity", "population dynamics", "neural toolkit", "neural data analysis pipeline"]
category: "neuroscience"
---

## Overview

DRIADA (arXiv:2607.00851) is a Python toolkit for cross-scale analysis of single-neuron selectivity and population dynamics. Provides unified framework for analyzing neural data from individual neuron response properties to population-level dynamical patterns.

## Core Architecture

### Cross-Scale Analysis Pipeline
```
Single-Neuron Scale → Population Scale → System Scale
    |                     |                  |
Selectivity indices   Dimensionality     Dynamical modes
Tuning curves         Trajectory analysis  State transitions
Response profiles     Manifold geometry    Attractor structure
```

### Key Components

1. **Single-Neuron Selectivity Analysis**
   - Compute selectivity indices for stimulus features
   - Fit tuning curves and response profiles
   - Identify feature-preferential neurons

2. **Population Dynamics Analysis**
   - Dimensionality reduction (PCA, factor analysis, demixed PCA)
   - Trajectory analysis in low-dimensional state space
   - Manifold geometry characterization

3. **Cross-Scale Integration**
   - Link single-neuron selectivity to population patterns
   - Identify which neurons drive specific dynamical modes
   - Map functional subpopulations to dynamical regimes

## Implementation Patterns

### Selectivity Index Computation
```python
# For each neuron, compute selectivity to stimulus features
# Using ANOVA, mutual information, or d-prime metrics
selectivity = compute_selectivity(neural_responses, stimulus_labels)
```

### Population Trajectory Analysis
```python
# Project neural population activity into low dimensions
trajectories = reduce_dimensionality(population_activity, method='dpca')
# Analyze geometry: curvature, speed, fixed points
geometry = analyze_trajectory_geometry(trajectories)
```

## Pitfalls

- **Cross-scale integration**: Linking single-neuron to population scales requires careful normalization
- **Dimensionality choice**: Too few dimensions lose information; too many introduce noise
- **Temporal alignment**: Cross-trial alignment critical for population dynamics analysis

## Verification Steps

1. Validate selectivity indices against known ground-truth tuning
2. Verify dimensionality reduction preserves key dynamical features
3. Cross-validate population dynamics across multiple experimental sessions
4. Compare results with established analysis tools (e.g., MLE-Toolbox)

## Activation

driada, cross-scale analysis, neural toolkit, single-neuron selectivity, population dynamics, neural data analysis, Python neuroscience toolkit, neural selectivity, population trajectories
