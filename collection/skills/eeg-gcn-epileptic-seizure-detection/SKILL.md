---
name: eeg-gcn-epileptic-seizure-detection
description: "Frequency-aware epileptic seizure detection using graph convolutional networks on multi-band EEG signals. Decomposes EEG into frequency bands and models spatial dependencies with GCN. Activation: seizure detection, EEG analysis, graph CNN, frequency bands, epilepsy"
---

# Epileptic Seizure Detection in Separate Frequency Bands Using GCN

> A frequency-aware framework for epileptic seizure detection that decomposes EEG signals into five bands and employs Graph Convolutional Networks to model spatial electrode dependencies.

## Metadata
- **Source**: arXiv:2604.00163
- **Authors**: [Paper authors]
- **Published**: 2026-04
- **Categories**: cs.LG, cs.AI, cs.NE

## Core Methodology

### Key Innovation
This approach addresses the interpretability gap in deep learning seizure detection by explicitly modeling frequency-specific neural dynamics and spatial dependencies among EEG electrodes, revealing frequency-specific seizure patterns.

### Technical Framework

#### Signal Decomposition
1. **Multi-band decomposition**: Raw EEG split into five frequency bands
   - Delta band
   - Theta band
   - Alpha band
   - Lower beta band
   - Higher beta band

2. **Feature extraction**: Eleven discriminative features extracted from each band

#### Graph Convolutional Network Architecture
- **Graph representation**: EEG electrodes as graph nodes
- **Spatial dependencies**: GCN models relationships between electrodes
- **Ictal-phase analysis**: Focuses on seizure-phase EEG patterns

### Performance Results

#### Band-Specific Accuracies
| Frequency Band | Accuracy |
|----------------|----------|
| Delta | 97.1% |
| Theta | 97.13% |
| Alpha | 99.5% |
| Lower Beta | 99.7% |
| Higher Beta | 51.4% |
| **Broadband (Overall)** | **99.01%** |

#### Key Findings
- **Mid-frequency dominance**: Alpha and lower beta bands show strongest discriminative capability
- **Frequency-specific patterns**: Different seizure types may manifest in specific bands
- **Interpretability gains**: Band-wise analysis reveals neurophysiological insights

## Implementation Guide

### Prerequisites
- CHB-MIT or comparable scalp EEG dataset
- Graph neural network framework (PyTorch Geometric, DGL)
- Signal processing library (MNE, SciPy)

### Processing Pipeline
1. **Preprocessing**: Filter and segment EEG signals
2. **Band decomposition**: Apply bandpass filters for five frequency bands
3. **Feature extraction**: Compute 11 features per band
4. **Graph construction**: Define electrode adjacency matrix
5. **GCN training**: Train graph convolutional network
6. **Evaluation**: Assess band-specific and overall performance

### Feature Engineering
- Time-domain features (variance, skewness, kurtosis)
- Frequency-domain features (power spectral density)
- Connectivity features (coherence, correlation)
- Wavelet features

## Applications
- Clinical epilepsy diagnosis support
- Real-time seizure monitoring systems
- Understanding seizure neurophysiology
- Personalized seizure prediction
- Drug efficacy monitoring

## Pitfalls
- Higher beta band shows poor performance (51.4%) - may need special handling
- Scalp EEG limited by volume conduction effects
- Patient-specific calibration may be required
- Imbalanced datasets common in seizure detection

## Related Skills
- irene-eeg-seizure-detection
- eeg-brain-connectivity-bci
- tda-epileptic-eeg-classification
- topology-signal-processing-brain-networks
