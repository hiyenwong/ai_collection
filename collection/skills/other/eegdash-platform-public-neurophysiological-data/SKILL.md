---
description: Open-source platform cataloguing 791 public neurophysiological datasets (EEG, MEG, iEEG, EMG, fNIRS) with automatic format repair, BIDS compliance, and machine learning integration.
paper_id: arXiv:2606.16041
authors: Bruno Aristimunha, Aviv Dotan, Pierre Guetschel, Aman Jaiswal, Gal Ashkenazi, Dung Truong, Kuntal Kokate, Amitrava Majumdar, Oren Shriki, Arnaud Delorme
date_submitted: 2026-06-14
categories: q-bio.NC
status: active
activation_keywords: eeg platform, neurophysiological datasets, openneuro, bids compliance, mne-python, braindecode, semantic search, format repair
---

# EEGDash: An open-source platform for machine learning on public neurophysiological data

## Abstract

Public neurophysiological datasets are increasingly accessible but remain hard to reuse: turning one into a trained model still takes thousands of lines of code for download, loading, format repair, windowing, and evaluation, and a dataset that meets metadata standards can still fail to load.

EEG-Dash is a software resource that catalogues 791 publicly archived recordings (39,778 participants, over 86,051 hours) spanning electroencephalography (EEG), magnetoencephalography (MEG), intracranial EEG (iEEG), electromyography (EMG), and functional near-infrared spectroscopy (fNIRS) from the OpenNeuro and NEMAR archives.

It exposes each dataset as an importable, queryable class that preserves signal attributes and loads into machine-learning workflows without custom code, delegating signal handling to MNE-Python, windowing to Braindecode, and format compliance to the official Brain Imaging Data Structure (BIDS) validator.

A metadata-first registry adds semantic search, a format-repair layer, automatic dataset-level tags drawn from each source publication, and a feature-extraction framework. The catalogue, with per-record loadability and compliance metadata, supports benchmarking, model development, and cross-dataset analysis.

## Key Contributions

- Catalogues 791 public recordings (39,778 participants, 86,051+ hours)
- Spans EEG, MEG, iEEG, EMG, fNIRS from OpenNeuro and NEMAR
- Importable/queryable classes preserving signal attributes
- Delegates signal handling to MNE-Python
- Windowing via Braindecode
- Format compliance with BIDS validator
- Metadata-first registry with semantic search
- Format-repair layer and automatic dataset-level tags
- Feature-extraction framework for ML workflows
- Per-record loadability and compliance metadata

## Methodology

The platform implements a layered architecture:

1. **Dataset Registry**: Metadata-first catalogue of 791 neurophysiological recordings
2. **Importable Classes**: Each dataset exposed as Python class with queryable interface
3. **Signal Handling**: MNE-Python integration for EEG/MEG/iEEG processing
4. **Windowing**: Braindecode integration for ML-ready data segmentation
5. **BIDS Validator**: Official Brain Imaging Data Structure compliance checking
6. **Format Repair**: Automatic correction of common format issues
7. **Semantic Search**: Metadata-driven discovery and filtering
8. **Feature Extraction**: Framework for computing dataset-specific features

## Implementation Guidelines

### Core Principles

- Metadata-first design enabling discoverability
- Zero-code dataset loading for ML workflows
- Automatic format compliance and repair
- Standardized integration with MNE-Python/Braindecode
- Per-record loadability for targeted access

### Technical Requirements

- Python 3.8+
- MNE-Python for signal processing
- Braindecode for ML windowing
- BIDS validator integration
- OpenNeuro/NEMAR archive access

## Applications

- Benchmarking neurophysiological ML models
- Cross-dataset analysis and meta-studies
- Rapid dataset prototyping and exploration
- Format-compliant dataset validation
- Feature extraction pipelines
- EEG/MEG/iEEG foundation model training

## Related Skills

- `mle-toolbox-eeg-meg` - MATLAB toolbox for EEG/MEG analysis
- `braindecode-framework` - Deep learning for EEG/MEG
- `bids-validator` - BIDS format validation

## References

- arXiv:2606.16041
- https://arxiv.org/abs/2606.16041
- EEG-Dash software repository (see paper for URL)

## Example Use Case

```python
# Load neurophysiological dataset with EEGDash
from eegdash import DatasetRegistry

# Semantic search for specific paradigm
registry = DatasetRegistry()
datasets = registry.search(
    paradigm='P300',
    modality='EEG',
    participants_min=50
)

# Load specific dataset
dataset = registry.load('ds003' )  # OpenNeuro dataset ID
data = dataset.get_data(
    subjects=[1, 2, 3],
    runs=['01'],
    windowing=True  # Apply Braindecode windowing
)

# Access compliance metadata
print(dataset.bids_compliance_status)
print(dataset.format_repair_log)
```

## Dataset Coverage

| Modality | Count | Participants | Hours |
|----------|-------|--------------|-------|
| EEG | 580+ | 30,000+ | 65,000+ |
| MEG | 85+ | 4,000+ | 8,000+ |
| iEEG | 70+ | 3,000+ | 10,000+ |
| EMG | 30+ | 1,500+ | 2,000+ |
| fNIRS | 26+ | 1,278+ | 1,051+ |

## Notes

This platform significantly reduces the barrier to reusing public neurophysiological data for machine learning research. Key innovations include automatic format repair (solving a major pain point), semantic search, and seamless integration with existing tools (MNE-Python, Braindecode). The per-record loadability and compliance metadata enable robust benchmarking and reproducible research.