---
name: biophysical-hh-model-extracellular-neurostimulation
description: Learning biophysical Hodgkin-Huxley models from extracellular MEA measurements using differentiable simulation and simulation-based inference. Enables precise neurostimulation prediction from minutes of recording instead of hours of stimulus testing.
trigger_words:
  - biophysical HH model
  - extracellular MEA
  - neurostimulation prediction
  - differentiable biophysical simulation
  - Hodgkin-Huxley inference
  - simulation-based inference
  - multi-electrode array HH fitting
  - precise neurostimulation
  - neural dynamics prediction
categories:
  - neuroscience
  - computational neuroscience
  - neuroengineering
created: "2026-07-12"
source: "arXiv:2607.04063v1 (ICML 2026)"
---

# Learning Biophysical Hodgkin-Huxley Models from Extracellular MEA Data

## Paper

**Title:** Learning Biophysical Models of Large-Scale Multineuronal Data to Enable Precise Neurostimulation  
**Authors:** Amrith Lotlikar, Ian Christopher Tanoh, Praful Vasireddy, Andrew Lanpouthakoun, Ramandeep Vilkhu, Michael Sommeling, A.J. Phillips, Alexander Sher, Alan Litke, Scott W. Linderman, E.J. Chichilnisky, Subhasish Mitra  
**Published:** arXiv:2607.04063v1 (Accepted at ICML 2026)  
**Date:** July 5, 2026  

## Problem

Multi-compartment Hodgkin-Huxley (HH) models provide a principled framework for predicting neural dynamics and responses to electrical stimulation. However:

- **Invasive requirement:** Fitting HH biophysical parameters traditionally requires intracellular recordings, which are invasive and low-throughput
- **Scalability limit:** Cannot capture the geometry and cell-specific properties of many neurons in a given neural circuit simultaneously
- **Clinical inefficiency:** Predicting neural spiking responses to candidate neurostimulation patterns takes hours of clinical testing

## Solution

A framework to rapidly infer HH parameters from designed features of extracellular MEA measurements using:

1. **Differentiable biophysical simulation** — Enables gradient-based optimization of HH parameters through the full biophysical model
2. **Simulation-based inference (SBI)** — Bayesian inference framework that learns the posterior over biophysical parameters from extracellular data alone
3. **Extracellular-only fitting** — No intracellular recordings needed; uses only high-density extracellular measurements from full neural populations

## Key Results

- **90.6% accuracy** predicting previously unseen multi-electrode stimulation responses
- HH models fit from **only a few minutes of recording** (vs. hours of stimulus testing)
- Validated on **hundreds of hours of stimulation and recording data** from isolated macaque retina
- Used **30 μm-pitch 512-electrode array** for high-density extracellular measurements

## Methodology Details

### Differentiable Biophysical Simulation

The key innovation is making the full multi-compartment HH model differentiable, enabling:

- **Gradient-based parameter estimation** — Compute gradients of the simulation output with respect to biophysical parameters (ion channel conductances, membrane capacitance, etc.)
- **End-to-end optimization** — Directly optimize HH parameters to match extracellular voltage traces
- **Amortized inference** — Once trained, the inference model can rapidly predict parameters for new neurons

### Simulation-Based Inference (SBI)

SBI learns a mapping from observed data features to the posterior distribution over HH parameters:

- **Feature extraction** — Designed features from extracellular MEA measurements (spike waveforms, temporal patterns, spatial spread)
- **Posterior learning** — Neural density estimator trained on simulated data pairs (parameters → features)
- **Amortized inference** — Single inference model works across many neurons without re-fitting

### Validation Pipeline

1. **Data collection:** Hundreds of hours of stimulation + recording from macaque retina (512-electrode array, 30 μm pitch)
2. **Parameter fitting:** Fit HH models from minutes of spontaneous + stimulated recording
3. **Prediction validation:** Predict responses to novel stimulation patterns never seen during fitting
4. **Accuracy metric:** 90.6% prediction accuracy on held-out stimulation responses

## Practical Applications

### Translational Neuroengineering
- **Clinical neurostimulation planning:** Predict patient-specific responses to candidate stimulation patterns before delivery
- **Deep brain stimulation (DBS):** Optimize DBS parameters using patient-specific biophysical models
- **Retinal prosthetics:** Predict response patterns for retinal implant stimulation

### Research Applications
- **Circuit-level modeling:** Fit biophysical models for entire neural populations from extracellular data
- **Cell-type classification:** Extract biophysical signatures for cell-type identification
- **Drug effect prediction:** Model how pharmacological interventions alter HH parameters

## Implementation Notes

- **Differentiable simulators:** Tools like JAX-based HH simulators or TorchDiffEq for gradient computation
- **SBI libraries:** sbi (simulation-based inference) Python package, or custom neural density estimators
- **MEA data:** Requires high-density extracellular recordings (e.g., Neuropixels, CMOS arrays)
- **Compute:** Training requires significant GPU resources for differentiable simulation + SBI

## Trigger Conditions

Use this skill when:
- Inferring biophysical neuron model parameters from extracellular recordings
- Predicting neural responses to electrical stimulation patterns
- Designing neurostimulation protocols for clinical or research applications
- Building differentiable biophysical neuron simulators
- Applying simulation-based inference to neuroscience problems

## References

- Paper: arXiv:2607.04063v1 (ICML 2026)
- Related: `pinn-neuronal-parameter-estimation` (PINN-based HH parameter estimation from partial voltage observations)
- Related: `differentiable-biophysical-simulation-neurostimulation` (Differentiable biophysical simulation framework)
