---
name: differentiable-biophysical-simulation-neurostimulation
description: "Differentiable biophysical simulation framework for inferring Hodgkin-Huxley parameters from extracellular MEA data. Enables rapid biophysical inference and precise neurostimulation prediction without invasive intracellular recordings."
tags: [neuroscience, biophysical-modeling, hodgkin-huxley, neurostimulation, differentiable-simulation, MEA]
source: arXiv:2607.04063v1
date: 2026-07-05
---

# Learning Biophysical Models of Large-Scale Multineuronal Data to Enable Precise Neurostimulation

## Paper Information
- **Title**: Learning Biophysical Models of Large-Scale Multineuronal Data to Enable Precise Neurostimulation
- **Authors**: Amrith Lotlikar, Ian Christopher Tanoh, Praful Vasireddy, Andrew Lanpouthakoun, Ramandeep Vilkhu
- **arXiv**: 2607.04063v1
- **Date**: 2026-07-05
- **Categories**: q-bio.NC

## Core Problem
Multi-compartment Hodgkin-Huxley (HH) models provide principled neural dynamics prediction but require **invasive intracellular recordings** for parameter fitting. This limits scalability to large neural populations and prevents capturing cell-specific properties in circuits.

## Key Innovation
Framework to infer HH biophysical parameters from **extracellular MEA (Multi-Electrode Array) measurements** using:
1. Differentiable biophysical simulation
2. Simulation-based inference
3. Designed features of extracellular signals

## Methodology

### Differentiable Biophysical Simulation
```
Extracellular MEA Data
        ↓
Feature Extraction (waveform shape, spike timing, etc.)
        ↓
Differentiable HH Model Simulation
        ↓
Gradient-Based Parameter Inference
        ↓
Predicted Biophysical Parameters
```

### Key Components
1. **Feature Engineering**: Extract informative features from extracellular recordings:
   - Extracellular waveform shapes
   - Spike timing patterns
   - Population activity features

2. **Differentiable Simulation**: Make HH model differentiable to enable gradient-based optimization:
   - Backpropagation through biophysical equations
   - Efficient parameter updates
   - Scalable to large neuron populations

3. **Simulation-Based Inference**: Use simulated data to train inference models:
   - Generate training data from known parameters
   - Learn mapping: features → biophysical parameters
   - Generalize to real experimental data

## Applications

### Predicting Neurostimulation Responses
Central translational neuroengineering goal: **predict neural spiking responses to electrical stimulation**

Use cases:
- Optimize stimulation parameters for therapeutic effect
- Minimize side effects by predicting off-target activation
- Personalize deep brain stimulation (DBS) protocols
- Design closed-loop stimulation systems

### Large-Scale Circuit Modeling
- Fit HH parameters for hundreds of neurons simultaneously
- Capture cell-type specific properties
- Build biologically realistic circuit models
- Enable in-silico testing of interventions

## Technical Advantages

| Traditional Approach | This Framework |
|---------------------|----------------|
| Intracellular recordings (invasive) | Extracellular MEA (scalable) |
| Single-cell fitting | Population-scale inference |
| Manual parameter tuning | Automated gradient-based optimization |
| Limited to simple models | Full multi-compartment HH models |

## Implementation Notes
- Simulation framework: Differentiable HH model
- Inference method: Simulation-based inference with gradient optimization
- Data source: High-density MEA recordings
- Output: Biophysical parameters (conductances, time constants, morphology)

## Validation
- Predict spiking responses to electrical stimulation
- Match experimental data from MEA recordings
- Generalize across neurons and conditions

## Related Work
- Hodgkin-Huxley models (classic biophysics)
- Neural mass models (population-level)
- Differentiable programming in neuroscience
- Simulation-based inference (SBI)
- Brain stimulation optimization

## Activation Triggers
- Hodgkin-Huxley, HH model, biophysical modeling
- neurostimulation, DBS, brain stimulation
- differentiable simulation, simulation-based inference
- MEA, multi-electrode array, extracellular recordings
- parameter inference, neural parameter estimation
- computational neuroscience, biophysical parameters
