---
name: eeg-microstate-tokenizer-representation
description: "Universal EEG microstate tokenizer for representation learning across downstream tasks. Clusters continuous EEG into discrete microstate tokens that serve as universal building blocks for sleep staging, emotion recognition, seizure detection, and motor imagery. Provides a tokenization-first approach to EEG encoding, distinct from variational embedding or feature extraction methods. Activation: eeg tokenization, microstate tokenizer, universal eeg representation, discrete eeg tokens, eeg representation learning, microstate-based encoding, EEG atoms of thought."
---

# EEG Microstate Tokenizer for Universal Representation Learning

> Universal microstate tokenizer converts continuous EEG signals into sequences of discrete microstate tokens, enabling representation learning across diverse downstream tasks via a single unified encoding.

## Metadata
- **Source**: arXiv:2605.20182
- **Published**: 2026-05-20
- **Categories**: cs.LG, q-bio.NC

## Core Methodology

### Key Innovation
Treats EEG microstates as "atoms of thought" — building blocks of brain activity patterns at microscopic time scales. Instead of treating EEG as a raw multivariate temporal signal (time/frequency features), this approach:
1. Clusters continuous EEG into discrete microstate sequences
2. Trains a universal tokenizer from large-scale medical EEG data
3. Uses microstate tokens as universal input representation for diverse downstream tasks

### Technical Framework
1. **Microstate Discovery**: Cluster continuous EEG signals using k-means on global field power (GFP) peaks to identify canonical microstate topographies (typically 4-8 states)
2. **Tokenization**: Map each time point to its nearest microstate, producing a discrete token sequence
3. **Universal Representation**: The tokenizer is trained once on large medical EEG data, then applied universally across tasks without re-training
4. **Downstream Tasks**: Sleep staging, emotion recognition, seizure detection, motor imagery — all use the same microstate token representation

### Difference from Existing Approaches
- **vs eeg-microstate-variational-embedding**: Variational embedding uses deep latent space learning for microstate discovery; tokenizer uses clustering → discrete tokens → representation learning pipeline
- **vs eeg-foundation-model-adapters**: Foundation models learn continuous embeddings; tokenizer produces discrete symbolic tokens
- **Key distinction**: Tokenizer is a fixed encoding step, not an end-to-end learned representation

## Implementation Guide

### Prerequisites
- EEG data (any format — .edf, .bdf, .set)
- MNE-Python for EEG preprocessing
- scikit-learn for k-means clustering

### Step-by-Step
1. **Preprocess EEG**: Bandpass filter (1-40 Hz), re-reference, artifact removal
2. **Compute GFP**: Calculate Global Field Power at each time point
3. **Select GFP Peaks**: Identify local maxima in GFP time series
4. **K-means Clustering**: Cluster scalp topographies at GFP peaks into K microstates (K=4-8)
5. **Back-fit**: Assign each time point to nearest microstate → discrete token sequence
6. **Downstream**: Feed token sequences into task-specific models (e.g., Transformers for sequence modeling)

### Code Example
```python
import mne
import numpy as np
from sklearn.cluster import KMeans

# Load and preprocess EEG
raw = mne.io.read_raw_edf('data.edf', preload=True)
raw.filter(1, 40)
data = raw.get_data()  # (channels, time)

# Compute Global Field Power
gfp = np.std(data, axis=0)

# Find GFP peaks (local maxima)
from scipy.signal import argrelextrema
peaks = argrelextrema(gfp, np.greater, order=10)[0]

# Extract topographies at peaks
topographies = data[:, peaks].T  # (n_peaks, n_channels)

# K-means clustering
kmeans = KMeans(n_clusters=6, random_state=42)
microstate_maps = kmeans.fit(topographies).cluster_centers_  # (6, n_channels)

# Back-fit: assign each time point to nearest microstate
from sklearn.metrics.pairwise import euclidean_distances
distances = euclidean_distances(data.T, microstate_maps)  # (time, 6)
microstate_sequence = np.argmin(distances, axis=1)  # discrete token sequence

# Use microstate_sequence as input to downstream models
```

## Applications
- Sleep stage classification
- Emotion recognition from EEG
- Epileptic seizure detection
- Motor imagery BCI
- Cross-task transfer learning with unified EEG encoding

## Pitfalls
- Microstate number K is not universally agreed upon; typically 4-8 states
- Requires sufficient EEG data for stable microstate estimation
- Tokenizer trained on one dataset may not generalize to different EEG montages
- Loses continuous amplitude information — only topology matters

## Related Skills
- eeg-microstate-variational-embedding
- eeg-foundation-model-adapters
- eeg-foundation-sae-interpretability
