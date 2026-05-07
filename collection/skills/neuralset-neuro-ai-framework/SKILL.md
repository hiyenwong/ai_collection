---
name: neuralset-neuro-ai-framework
description: "NeuralSet: unified Python framework for Neuro-AI research that harmonizes multi-modal neural recordings (fMRI, M/EEG, spikes) with complex stimuli (text, audio, video) via pretrained deep learning embeddings. Provides lazy, memory-efficient data extraction and PyTorch-ready interface scaling from local prototyping to HPC clusters. Activates: neuralset, neuro-ai framework, neural recording preprocessing, multi-modal brain data, brain-AI alignment, fMRI MEG EEG pipeline, lazy data extraction, neural dataset harmonization."
---

# NeuralSet: Unified Neuro-AI Framework

> Python framework from Meta FAIR (Jean-Rémi King et al.) that unifies processing of diverse neural recordings and complex experimental stimuli with pretrained deep learning embeddings, providing a single PyTorch-ready interface for next-generation neuro-AI research.

## Metadata
- **Source**: arXiv:2605.03169
- **Authors**: Jean-Rémi King, Corentin Bel, Linnea Evanson, et al. (Meta FAIR)
- **Published**: 2026-05-04

## Core Methodology

### Key Innovation
NeuralSet addresses the fragmented software ecosystem in neuro-AI by providing a unified framework that:
1. **Decouples experimental metadata from lazy data extraction** — metadata loaded in memory, neural data extracted on-demand
2. **Harmonizes preprocessing pipelines** across modalities (fMRI, M/EEG, spikes) with pretrained DL embeddings for stimuli (text, audio, video)
3. **Scales seamlessly** from local prototyping to high-performance cluster execution
4. **Ensures full computational provenance** — eliminates manual data wrangling

### Architecture
```
NeuralSet Framework:
├── Experimental Metadata Layer (in-memory)
│   ├── Trial info, conditions, events
│   └── Stimulus descriptions
├── Lazy Data Extraction Layer (on-demand)
│   ├── fMRI → 4D volumes, spatial resampling
│   ├── M/EEG → epoched data, frequency decomposition
│   └── Spikes → spike trains, PSTHs
├── Stimulus Embedding Layer (pretrained models)
│   ├── Text → language model embeddings
│   ├── Audio → speech/audio embeddings
│   └── Video → visual embeddings
└── PyTorch Dataset Interface
    └── Unified batched loading for model training
```

### Design Principles
1. **Lazy loading** — neural data never loaded fully into memory; extracted per-sample during training
2. **Modality-agnostic** — same API for fMRI, EEG, MEG, spike recordings
3. **Embedding-first** — stimuli transformed via pretrained models before alignment with neural data
4. **Provenance tracking** — all preprocessing steps logged and reproducible

## Implementation Guide

### Prerequisites
- Python 3.9+
- PyTorch
- Modality-specific libraries (MNE for EEG/MEG, nibabel for fMRI)

### Usage Pattern
```python
# 1. Define experiment from metadata
experiment = NeuralSetExperiment(
    neural_data_path="/path/to/recordings/",
    stimulus_path="/path/to/stimuli/",
    modality="meg"  # or "fmri", "spikes"
)

# 2. Configure preprocessing
experiment.set_preprocessing(
    filtering=dict(low_pass=40, high_pass=0.1),
    resampling=200,  # Hz
)

# 3. Configure stimulus embeddings
experiment.set_stimulus_model(
    text="transformer",      # pretrained language model
    audio="wav2vec",          # pretrained audio model
    video="clip",             # pretrained visual model
)

# 4. Create PyTorch Dataset
dataset = experiment.to_dataset()
loader = torch.utils.data.DataLoader(dataset, batch_size=32)

# 5. Train brain-AI alignment model
for neural_batch, stimulus_batch in loader:
    # neural_batch: (batch, channels, time) or (batch, voxels)
    # stimulus_batch: (batch, embedding_dim)
    predictions = model(stimulus_batch)
    loss = criterion(predictions, neural_batch)
```

## Applications
- Brain-AI alignment studies (neural predictivity of language/vision models)
- Multi-modal neural decoding (EEG+fMRI joint analysis)
- Naturalistic stimulus experiments (movie watching, reading, listening)
- Transfer learning across recording modalities
- Large-scale neuro-AI benchmarking

## Pitfalls
- Requires significant storage for raw neural data (lazy loading assumes fast I/O)
- Pretrained embedding models add computational overhead during data loading
- Cross-modal harmonization requires careful temporal alignment

## Related Skills
- eeg-foundation-model-adapters
- brain-foundation-model-inversion
- multimodal-brain-connectivity-gnn
- computational-neuroscience-in-llm-era
- neuroscience-of-transformers
