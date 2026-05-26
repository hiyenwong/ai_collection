---
name: mindalign-eeg-visual-decoding
description: >-
  Tri-modal contrastive framework (EEG, vision, language) for zero-shot visual
  decoding from EEG signals. Achieves 54.1% Top-1 / 83.4% Top-5 accuracy on
  Things-EEG2 benchmark (vs prior 32.4%/64.0%). Two-stage design: masked
  reconstruction pre-training on unlabeled EEG, then contrastive alignment with
  image and text embeddings. Based on arXiv:2605.24523 (May 2026). Use when
  implementing EEG-to-image decoding, brain-computer interfaces for visual
  reconstruction, multi-modal EEG representation learning, zero-shot brain
  decoding, or contrastive learning with neural data.
metadata:
  arxiv_id: "2605.24523"
  published: "2026-05-23"
  authors: "Zexuan Chen, Sichao Liu, Runhao Lu, Huichao Qi, Alexandra Woolgar, Xi Vincent Wang, Lihui Wang"
  categories: [cs.LG, cs.CL, q-bio.NC]
  tags: [eeg-decoding, visual-decoding, contrastive-learning, brain-computer-interface, zero-shot, multi-modal, eeg-encoder, graph-attention, mindalign, things-eeg2]
---

# MindAlign: Bridging EEG, Vision, and Language for Zero-Shot Visual Decoding

**Source:** arXiv: [2605.24523](https://arxiv.org/abs/2605.24523) (May 2026)
**Authors:** Zexuan Chen, Sichao Liu, Runhao Lu, Huichao Qi, Alexandra Woolgar, Xi Vincent Wang, Lihui Wang
**Code:** https://github.com/anon-eeg/eeg_image_decoding

---

## 1. Overview

MindAlign introduces a tri-modal contrastive framework that aligns EEG, visual, and textual representations within a unified latent space for zero-shot visual decoding from non-invasive brain signals. The key insight is that using LLM-generated textual descriptions as a semantic regularizer during contrastive training injects linguistic structure into the shared space without overwhelming the primary EEG-image signal.

**Core results:**
- **Things-EEG2 200-way zero-shot**: 54.1% Top-1, 83.4% Top-5 accuracy (prior best: 32.4%/64.0%)
- Generalizes to Things-MEG dataset
- Compact embedding geometries (CN-CLIP) outperform much larger backbones
- Decoding aligns with established neurophysiology of visual processing

---

## 2. Methodology

### 2.1 Two-Stage Training

**Stage 1: Masked Reconstruction Pre-training**
- Train EEG encoder via masked autoencoder on unlabeled EEG trials
- Learns spatio-temporal regularities that transfer to downstream tasks
- Self-supervised — no labels needed

**Stage 2: Tri-modal Contrastive Alignment**
- Jointly align EEG, image, and LLM-generated textual descriptions
- Contrastive loss pulls matched EEG-image-text triplets together
- Text acts as semantic regularizer (not dominant signal)

### 2.2 EEG Encoder Architecture

The encoder integrates three key components:

1. **Subject-specific adaptation**: Lightweight adaptation layers per subject to handle cross-subject variability
2. **Graph attention over channels**: Models spatial relationships between EEG channels as a graph, using attention to weight channel importance
3. **Temporal-spatial convolutional embeddings**: Convolutional layers extract hierarchical spatio-temporal features

### 2.3 Zero-Shot Decoding Pipeline

1. Record EEG signals during visual stimulation
2. Encode EEG with pre-trained encoder
3. Align EEG embedding with image/text embedding space
4. Retrieve matching image via nearest-neighbor search in embedding space

---

## 3. Key Results

| Benchmark | Metric | MindAlign | Prior Best |
|-----------|--------|-----------|------------|
| Things-EEG2 | Top-1 Accuracy | **54.1%** | 32.4% |
| Things-EEG2 | Top-5 Accuracy | **83.4%** | 64.0% |
| Things-MEG | Generalization | Validated | — |

- Compact CN-CLIP embeddings outperform larger backbones (ViT, CLIP-L/14)
- Decoding accuracy follows known visual processing hierarchy (earlier visual areas → higher accuracy for low-level features)
- Paired Wilcoxon tests confirm significance (p < 0.01) over all in-subject baselines

---

## 4. Implementation Details

### Key Design Choices

| Component | Choice | Rationale |
|-----------|--------|-----------|
| Text supervision | LLM-generated descriptions | Semantic regularization without dominating |
| Backbone | CN-CLIP (compact) | Better than larger models for this task |
| Pre-training | Masked reconstruction | Transfers robustly to downstream tasks |
| Subject adaptation | Lightweight per-subject layers | Handles cross-subject EEG variability |
| Channel modeling | Graph attention | Captures spatial relationships |

### Training Details
- Pre-training on unlabeled EEG trials with masked reconstruction
- Contrastive learning with temperature-scaled InfoNCE loss
- Batch size and learning rate tuned for tri-modal alignment

---

## 5. Applications

- **Brain-computer interfaces**: Visual decoding for communication
- **Neuroscience research**: Understanding visual representations in the brain
- **Zero-shot decoding**: Decode visual stimuli not seen during training
- **Multi-modal alignment**: Framework applicable to other neural modalities (MEG, fMRI)

---

## 6. Activation

- mindalign
- eeg-visual-decoding
- tri-modal-contrastive
- zero-shot-brain-decoding
- eeg-to-image
- things-eeg2
- brain-ai-alignment
