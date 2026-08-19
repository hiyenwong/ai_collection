---
name: phase-based-spatial-ordinal-patterns-oscillatory-dynamics
description: "Phase-based spatial ordinal patterns analysis."
metadata:
  arxiv_id: "2608.17196"
  published: "2026-08-17"
  authors: "Robison J. Santos-Silva, Bruno R. R. Boaretto, Thiago L. Prado, Roberto C. Budzinski"
  categories: ["nlin.AO", "q-bio.NC"]
license: Complete terms in LICENSE.txt
---

# Phase-Based Spatial Ordinal Patterns for Oscillatory Dynamics

## Overview

This framework characterizes spatiotemporal dynamics in oscillatory systems by acting directly on the phase rather than the amplitude. It introduces spatial ordinal patterns that encode local spatial ordering relations, capturing both phase gradients and synchronized clusters within a single framework.

## Key Concepts

### Spatial Ordinal Patterns
- Acts on phase values from oscillatory systems (e.g., neural populations, EEG)
- Introduces additional patterns to account for near-equal phases
- Creates symbolic representation of local spatial ordering relations
- Captures both phase gradients and synchronized clusters simultaneously

### Spatial Permutation Entropy
- Quantifies diversity of spatiotemporal patterns at each point in time
- Enables detection of transient dynamics and regime transitions as they occur
- Distinguishes phase-locked states with identical global synchronization but distinct spatial organization
- Characterizes partially synchronized states

## Methodology

### Step 1: Phase Extraction
Extract phase time series from oscillatory signals (e.g., using Hilbert transform for EEG data).

### Step 2: Spatial Ordinal Pattern Construction
For each time point and spatial location:
1. Compare phase values with neighboring locations
2. Encode local spatial ordering relations as ordinal patterns
3. Handle near-equal phases with special pattern categories

### Step 3: Entropy Calculation
Compute spatial permutation entropy over sliding windows to track pattern diversity over time.

### Step 4: Analysis and Interpretation
- Identify regime transitions through entropy changes
- Detect transient dynamics in real-time
- Compare spatial organization across different conditions

## Applications

### Neuroscience
- Resting-state EEG analysis to distinguish different conditions within individual volunteers
- Characterizing neural population dynamics in synthetic oscillator networks
- Detecting transient brain states and regime transitions

### Engineering Networks
- Monitoring spatiotemporal patterns in engineered oscillatory systems
- Real-time detection of system state changes
- Characterizing synchronization properties beyond global measures

## Implementation Notes

- Works with any oscillatory system where phase can be extracted
- Robust to amplitude variations since it focuses on phase relationships
- Can be applied to both synthetic and real-world data
- Computationally efficient for real-time applications

## Pitfalls

### Phase Extraction Quality
Poor phase extraction (e.g., from noisy signals) will affect pattern quality. Ensure proper preprocessing and filtering before phase extraction.

### Spatial Resolution
The method's effectiveness depends on adequate spatial sampling. Sparse spatial coverage may miss important local ordering relations.

### Near-Equal Phase Handling
The choice of tolerance for defining "near-equal" phases can significantly impact results. Calibrate this parameter based on your specific application and noise characteristics.

## References

- Original paper: [arXiv:2608.17196](https://arxiv.org/abs/2608.17196)
- Related work on ordinal patterns and permutation entropy
- Applications in neuroscience and complex systems analysis