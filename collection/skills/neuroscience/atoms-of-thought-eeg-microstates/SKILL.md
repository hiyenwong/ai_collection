---
name: atoms-of-thought-eeg-microstates
description: "Universal EEG representation learning using microstate tokenizers. Builds a discrete microstate tokenizer from large-scale EEG datasets by clustering continuous signals into sequences of quasi-stable brain activity patterns. Outperforms traditional time/frequency features across sleep staging, emotion recognition, and motor imagery. Applicable to EEG representation, BCI, sleep staging, emotion recognition, neuroinformatics. Activation: EEG microstates, universal EEG tokenizer, microstate clustering, brain state representation, EEG foundation model, microstate tokenization."
user-invocable: true
---

# Atoms of Thought: Universal EEG Representation Learning with Microstates

**Source Paper:** arXiv:2605.20182 - Atoms of Thought: Universal EEG Representation Learning with Microstates

**Authors:** Xinyang Tian, Ruitao Liu, Ziyi Ye, Siyang Xue, Xin Wang, Xuesong Chen

**Published:** 2026-05-19 (Accepted by MRAC 2025)

## Core Methodology

### 1. Microstate Tokenizer

Treats EEG microstates as the "atoms" of brain activity, analogous to words in NLP or visual tokens in computer vision.

**Process:**
- Cluster continuous EEG signals into sequences of discrete microstates
- Learn from large medical EEG dataset
- Each microstate represents a quasi-stable brain activity pattern at microscopic time scales

### 2. Universal Representation Learning

The microstate tokenizer is universally applicable across diverse downstream tasks:

**Tasks evaluated:**
- Sleep staging
- Emotion recognition
- Motor imagery classification

**Key finding:** Microstate-based representations consistently outperform:
- Traditional time-domain features (power bands, Hjorth parameters)
- Frequency-domain features (PSD, spectral entropy)
- Raw signal inputs under the same model architectures

### 3. Interpretability and Scalability

**Interpretability:**
- Microstates map to known functional brain networks
- Each state corresponds to a distinct topographical pattern
- Clinically meaningful transitions between states

**Scalability:**
- Tokenizer can be pre-trained once and applied universally
- Efficient discrete representation reduces computational cost
- Compatible with transformer and sequence models

## Key Contributions

1. **Novel representation:** First systematic demonstration that microstates are effective as a universal EEG representation for deep learning
2. **Cross-task generality:** Single tokenizer works across sleep, emotion, and motor tasks
3. **Interpretability:** Microstates offer inherent neurophysiological interpretability compared to continuous features
4. **Efficiency:** Discrete token sequences are more computationally efficient than continuous time-series

## Implementation Notes

### Building a Microstate Tokenizer

```
1. Preprocess EEG: bandpass filter (1-40 Hz), artifact removal
2. Compute GFP (Global Field Power) peaks
3. Extract topographies at GFP peak timepoints
4. Cluster topographies (k-means, typically 4-8 microstates)
5. Assign each timepoint to nearest microstate
6. Use resulting sequence of microstate labels as tokens
```

### Model Architecture Options

- **Transformer encoder** on microstate token sequences
- **LSTM/GRU** on microstate embeddings
- **CNN** with microstate embedding + positional encoding
- Compatible with any sequence model architecture

### Recommended Microstate Configurations

- Number of microstates: 4-8 (standard), can be task-dependent
- Time window: 60-120 ms per microstate
- Embedding dimension: 16-64 for downstream tasks

## Related Skills

- [[eeg-brain-connectivity-bci]] - EEG connectivity analysis for BCI
- [[eeg-hopfield-emotion-energy]] - EEG emotion recognition via energy landscapes
- [[laya-eeg-foundation]] - LeJEPA approach to EEG representation learning
- [[dance-eeg-event-detection]] - End-to-end EEG event detection
