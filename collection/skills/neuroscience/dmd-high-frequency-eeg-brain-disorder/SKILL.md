---
name: dmd-high-frequency-eeg-brain-disorder
description: "Detecting high-frequency brain disorder signals using dynamic mode decomposition from EEG - methodology for extracting consistent and persistent dynamical changes in the high-frequency band from EEG signals of neurologically relevant channels, with applications in distinguishing alcohol-dependent groups from controls. Use when analyzing high-frequency EEG dynamics, brain disorder detection, or Dynamic Mode Decomposition applications in neuroscience."
metadata:
  arxiv_id: "2608.02804"
  published: "2026-08-05"
  authors: "Jacob Kang, Jong-Hyeon Seo"
  tags: [dynamic-mode-decomposition, eeg, high-frequency, brain-disorders, alcohol-dependence, signal-processing]
license: Complete terms in LICENSE.txt
---

# DMD High-Frequency EEG Brain Disorder Detection

## Overview

This skill implements the methodology from the paper "Detecting high-frequency brain disorder signals using dynamic mode decomposition from EEG" (arXiv:2608.02804) which utilizes Dynamic Mode Decomposition (DMD) to extract consistent and persistent dynamical changes in the high-frequency band from EEG signals of neurologically relevant channels.

The key innovation is using high-frequency DMD modes as features to compose a feature table, then applying post-processing with a random distribution test to identify consistent high-frequency dynamics within specific EEG channels.

## Core Methodology

### 1. Signal Processing Pipeline

1. **Extract high-frequency band** from EEG signals of neurologically relevant channels
2. **Apply Dynamic Mode Decomposition (DMD)** to extract consistent and persistent dynamical changes
3. **Use high-frequency DMD modes as features** to compose a feature table
4. **Post-process with random distribution test** to identify consistent dynamics
5. **Apply PCA** to feature table components that pass the test

### 2. Key Findings

- Approximately 70% of samples exhibited consistent high-frequency dynamics within specific channel signals
- PCA components of feature table that passed the random distribution test formed consistent patterns
- These patterns successfully distinguished alcohol-dependent group from control group
- Method provides robust detection of brain disorder signals in high-frequency EEG ranges

### 3. Implementation Steps

1. **Preprocess EEG data** to isolate high-frequency bands (>30 Hz)
2. **Select neurologically relevant channels** based on disorder type
3. **Apply DMD algorithm** to extract dominant modes
4. **Filter modes** by consistency across time windows
5. **Construct feature table** from consistent high-frequency modes
6. **Apply statistical validation** using random distribution tests
7. **Perform classification** using PCA-reduced validated features

## Applications

- High-frequency EEG analysis
- Brain disorder detection (epilepsy, alcohol dependence, etc.)
- Dynamic Mode Decomposition in neuroscience
- EEG biomarker discovery
- Signal processing for neurological conditions

## Pitfalls and Considerations

- **Channel selection**: Critical to choose neurologically relevant channels for specific disorders
- **Frequency band definition**: High-frequency range may vary by application (typically >30 Hz)
- **Statistical validation**: Random distribution test is essential to filter spurious dynamics
- **Sample size**: Requires sufficient samples to achieve reliable classification performance
- **Cross-validation**: Essential for validating generalizability across different populations

## Activation Keywords

- DMD EEG high-frequency
- dynamic mode decomposition brain disorder
- high-frequency EEG biomarkers
- alcohol dependence EEG classification
- consistent dynamical changes EEG
- random distribution test EEG
- neurologically relevant EEG channels