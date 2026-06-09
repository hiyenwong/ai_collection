---
name: corteg-eeg-ecog-cross-modality
description: "CORTEG: Cross-modality transfer framework that adapts pretrained scalp-EEG foundation models to intracranial ECoG recordings. Combines EEG FM backbone with electrode-aware KNNSoftFourier spatial adapter, dual-stream tokenizer (low-frequency + high-gamma), and leave-one-subject-out fine-tuning. Enables competitive ECoG decoding with only 10-30 minutes of calibration data per patient. Activation: CORTEG, EEG foundation model, ECoG decoding, cross-modality transfer, scalp-to-intracranial, brain-computer interface, cross-patient learning, electrode-aware adapter."
arxiv_id: "2605.10337"
published: "2026-05-11"
authors: "Liuyin Yang, Qiang Sun, Bob Van Dyck, Eva Calvo Merino, Marc M. Van Hulle"
tags: [eeg-foundation-models, ecog-decoding, cross-modality-transfer, brain-computer-interface, transfer-learning]
---

# CORTEG: Cross-Modality Representation Transfer from Scalp to Intracranial Brain Recordings

> Foundation models pretrained on scalp EEG can be adapted for ECoG decoding, enabling cross-patient learning and competitive performance with minimal calibration data.

**Source**: arXiv: [2605.10337](https://arxiv.org/abs/2605.10337)

## Core Methodology

### Key Innovation
The first framework to demonstrate that large pretrained scalp-EEG foundation models can be effectively transferred to the intracranial ECoG domain, bridging the gap between non-invasive and invasive recordings.

### Technical Framework

1. **EEG Foundation Model Backbone**: Leverage large pretrained models (e.g., from LAEEG, BENDR, or similar) that have learned generalizable features from scalp EEG data
2. **Electrode-Aware KNNSoftFourier Spatial Adapter**: A novel spatial adapter that maps ECoG electrode positions to EEG foundation model input space, using k-nearest neighbor interpolation in the Fourier domain with soft assignment weights
3. **Dual-Stream Tokenizer**: Separate processing streams for low-frequency (LFP-like, <100Hz) and high-gamma (>100Hz) activity, as these bands carry complementary information in ECoG
4. **Leave-One-Subject-Out Fine-Tuning**: Train on N-1 patients, fine-tune minimally on held-out patient (10-30 min data, single GPU)
5. **Cross-Patient Decoding**: Achieve competitive performance by sharing information across patients through the pretrained backbone

### Key Results
- **Successful cross-modality transfer**: Scalp EEG foundation models adapt to ECoG with minimal fine-tuning
- **10-30 minute calibration**: Competitive decoding performance on new patients with very limited data
- **Dual-stream tokenization**: Low-frequency + high-gamma streams outperform single-stream baselines
- **Cross-patient learning**: Information sharing across patients significantly outperforms patient-specific models trained from scratch

## Implementation Patterns

```
CORTEG Framework:
1. Load pretrained EEG FM (weights frozen initially)
2. Add KNNSoftFourier spatial adapter for ECoG electrode layout
3. Add dual-stream tokenizer (LF path + HG path)
4. Train decoder head on N-1 subjects
5. Fine-tune spatial adapter + head on held-out subject (10-30 min)
```

## Applications

- **Clinical BCI**: Rapid calibration for new patients using pre-existing EEG foundation models
- **ECoG-based decoding**: Motor imagery, speech decoding, cursor control
- **Minimally-invasive interfaces**: Bridge scalp EEG research to ECoG applications
- **Cross-patient generalization**: Leverage population-level knowledge for individual patients

## Activation Keywords
- CORTEG framework
- EEG foundation model transfer
- ECoG cross-modality decoding
- KNNSoftFourier spatial adapter
- dual-stream brain tokenizer
- scalp-to-intracranial adaptation
- cross-patient ECoG learning
- brain-computer interface calibration

## Related Skills
- neuroatlas-eeg-foundation-benchmark
- eeg-foundation-model-adapters
- nerve-network-aware-bilinear-fc-tokenization
- neural-encoding-evaluation-ground-truth
- what-do-eeg-foundation-models-capture
