---
name: biophysical-hh-model-extracellular-neurostimulation
description: Learning biophysical Hodgkin-Huxley models from extracellular MEA data using differentiable biophysical simulation and simulation-based inference for precise neurostimulation prediction. ICML 2026 accepted.
tags: [Hodgkin-Huxley, neurostimulation, MEA, differentiable simulation, biophysical models, ICML 2026]
created: 2026-07-10
arxiv: 2607.04063v1
authors: [Amrith Lotlikar, Ian Christopher Tanoh, Praful Vasireddy, Andrew Lanpouthakoun, Ramandeep Vilkhu, Michael Sommeling, A.J. Phillips, Alexander Sher, Alan Litke, Scott W. Linderman, E.J. Chichilnisky, Subhasish Mitra]
venue: ICML 2026
---

# Learning Biophysical Models of Large-Scale Multineuronal Data to Enable Precise Neurostimulation

## Core Innovation

This paper (accepted at ICML 2026) introduces a framework to **rapidly infer Hodgkin-Huxley (HH) biophysical parameters from extracellular multi-electrode array (MEA) measurements** using differentiable biophysical simulation and simulation-based inference. This unlocks the ability to predict neural responses to candidate neurostimulation patterns that would take hours to measure clinically — using only minutes of recording data.

## Key Contributions

1. **Extracellular HH Inference**: First framework to infer HH biophysical parameters from extracellular (non-intracellular) data alone
2. **Differentiable Biophysical Simulation**: Leverages differentiable simulation for rapid parameter inference
3. **Clinical Translation**: Predicts multi-electrode stimulation responses with **90.6% accuracy** using models fit from only a few minutes of recording
4. **Massive Time Savings**: Replaces hours of stimulus testing with minutes of recording + prediction

## Problem Statement

Multi-compartment HH models provide principled prediction of neural dynamics and stimulation responses. However:
- Fitting HH parameters typically requires **intracellular recordings** (invasive, low-throughput)
- Cannot capture geometry and cell-specific properties of many neurons simultaneously
- Multi-electrode arrays (MEAs) offer scalable alternative but HH model complexity has precluded reliable biophysical inference from extracellular data alone

## Methodology

### Framework Architecture
1. **Differentiable Biophysical Simulation**: HH models implemented in differentiable framework
2. **Simulation-Based Inference**: Leverage designed features of extracellular MEA measurements
3. **Rapid Parameter Inference**: Extract HH parameters from minutes of recording data
4. **Stimulation Response Prediction**: Use inferred models to predict responses to unseen stimulation patterns

### Validation
- **System**: Isolated macaque retina
- **Hardware**: 30 μm-pitch 512-electrode array
- **Data**: Hundreds of hours of stimulation and recording
- **Result**: 90.6% accuracy on previously unseen multi-electrode stimulation responses
- **Data Required**: Only a few minutes of recording for model fitting

## Technical Details

### Hodgkin-Huxley Model Components
- Multi-compartment morphology
- Ion channel dynamics (Na+, K+, leak)
- Membrane capacitance and resistance
- Spatial cable properties

### Inference Pipeline
1. Collect extracellular MEA recordings
2. Extract features from designed stimulation protocols
3. Run differentiable HH simulation
4. Optimize biophysical parameters via gradient-based methods
5. Validate on held-out stimulation patterns

### Key Innovation: Differentiability
- Traditional HH simulation: forward-only, no gradient information
- This work: makes entire simulation differentiable
- Enables gradient-based parameter optimization from extracellular data
- Bridges gap between biophysical realism and data-driven inference

## Applications

1. **Retinal Prosthetics**: Predict optimal stimulation patterns for visual prostheses
2. **Deep Brain Stimulation**: Personalize DBS parameters based on biophysical models
3. **Neural Interface Design**: Optimize electrode placement and stimulation protocols
4. **Computational Neuroscience**: Study biophysical properties at scale from non-invasive recordings

## Impact

- **Clinical**: Hours of stimulus testing → minutes of recording + prediction
- **Scientific**: Enables biophysical modeling at population scale
- **Engineering**: Informs design of next-generation neural interfaces
- **Scalability**: 512-electrode array demonstrates population-level inference

## Activation Triggers

- Hodgkin-Huxley, biophysical models, neurostimulation
- Extracellular recording, MEA, differentiable simulation
- Retinal prosthesis, deep brain stimulation
- Neural interface design, computational neuroscience
- ICML 2026, simulation-based inference
