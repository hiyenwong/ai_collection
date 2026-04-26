---
name: tda-epileptic-eeg-classification
version: v1.0.0
last_updated: 2026-04-16
description: "Topological Data Analysis (TDA) framework for epileptic seizure detection from iEEG signals. Uses persistence diagrams, Carlsson coordinates, persistence images, and template functions for classification of preictal, ictal, and interictal brain states. Use for epilepsy detection, neurological state classification, or applying topological methods to time-series neural data."
---

# TDA Epileptic iEEG Classification

Based on "Classification of Epileptic iEEG using Topological Machine Learning" (arXiv:2604.11971v1)

## Description

This skill implements topological data analysis methods for classifying epileptic brain states from intracranial EEG (iEEG) recordings.

## Methodology

### Data
- **Patients**: 55 epilepsy patients
- **States**: Preictal, ictal, interictal
- **Channels**: Multichannel iEEG recordings

### Topological Features

1. **Persistence Diagrams**: Derived from iEEG signals
   - Capture topological features at different scales
   - Encode birth and death of topological structures

2. **Vectorization Methods**:
   - **Carlsson coordinates**: Algebraic topology-based features
   - **Persistence images**: Kernel-based vectorization
   - **Template functions**: Domain-specific feature templates

## Workflow

### Step 1: Preprocess iEEG

Apply bandpass filtering (0.5-100 Hz) and normalization.

### Step 2: Compute Persistence Diagrams

Use Takens embedding followed by persistent homology.

### Step 3: Vectorize Persistence

Convert persistence diagrams to feature vectors using multiple methods.

### Step 4: Train Classifier

Use ensemble methods (Random Forest) for classification.

## Activation Keywords

- tda eeg classification
- topological data analysis neural
- epileptic seizure detection
- persistence diagrams iEEG
- carlsson coordinates
- persistence images

## Tools Used

- GUDHI or Ripser for persistent homology
- scikit-learn for classification
- NumPy/SciPy for signal processing

## References

- Paper: https://arxiv.org/abs/2604.11971v1
- Authors: Sunia Tanweer et al. (2026-04-13)
