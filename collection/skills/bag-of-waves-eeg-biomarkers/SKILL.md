---
name: bag-of-waves-eeg-biomarkers
description: "Interpretable EEG biomarkers with bag-of-waves: Spatial and temporal waveform dictionaries for low-data regimes. Use when analyzing EEG data in low-data scenarios, needing interpretable biomarkers, or working with clinical EEG classification. Activation: bag-of-waves, EEG biomarkers, interpretable EEG, waveform dictionaries, low-data EEG"
metadata:
  arxiv_id: "2607.22508"
  published: "2026-07-24"
  authors: "Athanasios Papastathopoulos-Katsaros, Steven T. Lee, Lin Yao, Ajay Thomas, Junseok Park, Matthew J. McGinley, Zhandong Liu"
  tags: [eeg, biomarkers, interpretable, bag-of-waves, low-data, neuroscience]
license: Complete terms in LICENSE.txt
---

# Bag-of-Waves EEG Biomarkers

## Overview

The bag-of-waves framework provides an interpretable approach to EEG analysis that learns a small dictionary of recurring EEG waveform templates (called "atoms") using shift-invariant k-means without labels. This method operates effectively in low-data regimes where deep neural networks and foundation models are poorly suited.

## Core Methodology

### 1. Atom Learning
- Uses shift-invariant k-means clustering to learn waveform templates from continuous EEG data
- No labels required during the atom learning phase
- Each atom corresponds to an inspectable waveform that can be validated by neurophysiologists

### 2. Tokenization
- Continuous EEG is converted into a sequence of atom tokens
- Token counts feed simple downstream classifiers or clustering steps

### 3. Temporal Extensions
- Adds atom-to-atom transitions (n-grams) to capture temporal structure
- Enables modeling of sequential patterns in EEG data

### 4. Spatial Extensions
- Extends from single-channel atoms to regional and cross-channel spatial atoms
- Handles multichannel EEG data effectively

## Applications

The method has been tested on three complementary datasets:

1. **Single-channel mouse genotype clustering** (16 animals) - low-data and temporal case
2. **Resting-state dementia classification** - spatial case  
3. **TUEV benchmark** - six-way classification of clinical EEG events (high-data comparison)

## Advantages

- **Competitive performance**: Achieves results comparable to state-of-the-art deep and foundation models
- **Low parameter count**: Operates with a fraction of the parameters of heavy models
- **Full interpretability**: Every atom corresponds to an inspectable waveform
- **Clinical validation**: Explicitly recovers known clinical morphologies
- **Low-data capability**: Works effectively where heavier models fail

## Implementation Guidelines

### When to Use
- Low-data EEG analysis scenarios (<100 samples)
- Clinical settings requiring interpretable results
- Resource-constrained environments
- When predefined spectral features are insufficient

### Workflow Steps
1. Preprocess EEG data (filtering, artifact removal as needed)
2. Apply shift-invariant k-means to learn waveform atoms
3. Tokenize continuous EEG into atom sequences
4. Extract features (counts, n-grams, spatial patterns)
5. Apply simple classifier or clustering algorithm
6. Validate atoms with domain experts

### Pitfalls to Avoid
- Overfitting atom dictionary size to small datasets
- Ignoring temporal dependencies in high-frequency applications
- Failing to validate clinical relevance of learned atoms
- Not comparing against baseline spectral features

## References

- Original paper: [Interpretable EEG biomarkers with bag-of-waves](https://arxiv.org/abs/2607.22508)
- Related work: EEG foundation models, interpretable machine learning for neuroscience
- Clinical validation: Consult with neurophysiologists for atom interpretation

## Activation Keywords

- bag-of-waves
- EEG biomarkers  
- interpretable EEG
- waveform dictionaries
- low-data EEG
- shift-invariant k-means
- EEG atoms
- clinical EEG classification