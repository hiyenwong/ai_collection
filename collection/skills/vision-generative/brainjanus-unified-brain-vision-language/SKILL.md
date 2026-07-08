---
name: brainjanus-unified-brain-vision-language
description: "BrainJanus: first unified brain model integrating brain, vision, and language via autoregressive Transformer. Unified Brain Tokenizer quantizes neural dynamics into discrete tokens aligned with visual/linguistic representations. Supports any-to-any generation (image-to-brain, text-to-brain, brain-to-image, brain-to-text). Use when researching unified brain encoding/decoding, brain-vision-language integration, discrete brain tokenization, or autoregressive brain modeling."
metadata:
  arxiv_id: "2606.30319"
  published: "2026-06-29"
  venue: "ICML 2026"
  authors: ["Haitao Wu", "Qirui Zhang", "Zhouheng Yao", "Shangquan Sun", "Qihao Zheng", "Mianxin Liu", "Chi Zhang", "Wanli Ouyang", "Chunfeng Song", "Changqing Zhang", "Jiamin Wu"]
  affiliations: ["Tianjin University", "Shanghai AI Lab", "CUHK"]
  tags: ["brain-encoding", "brain-decoding", "unified-model", "autoregressive", "brain-tokenizer", "fMRI", "EEG", "multimodal"]
  github: "https://github.com/HaitaoWuTJU/BrainJanus"
---

# BrainJanus: Unified Brain-Vision-Language Autoregressive Model

First unified brain model integrating brain, vision, and language modalities within a single autoregressive framework. Replaces task-specific pipelines with any-to-any generation.

## Core Innovation

Unlike prior methods treating encoding/decoding as isolated tasks with separate adapters, BrainJanus uses a single Transformer backbone for all four directions: image→brain, text→brain, brain→image, brain→text.

## Key Components

### 1. Unified Brain Tokenizer (UBT)
- Quantizes continuous neural dynamics (fMRI/EEG) into discrete tokens
- Aligns brain tokens with vision and language tokens in shared Omni space
- Uses residual VQ-VAE style quantization with hierarchical codebooks
- Preserves biological topography (cortical spatial structure)

### 2. All-in-One Autoregressive Model
- Single Transformer backbone for next-token prediction across all modalities
- Task switching via prefix tokens (no separate heads needed)
- Supports zero-shot generalization to unseen tasks
- Joint multi-task learning promotes cross-modal knowledge transfer

## Training Strategy

1. **Stage 1**: Pre-train brain tokenizer (reconstruction objective)
2. **Stage 2**: Joint training on all 4 tasks with unified vocabulary
3. **Cross-modal alignment**: brain tokens share embedding space with visual+text tokens

## Key Results

- Surpasses task-specific models on encoding AND decoding benchmarks
- Zero-shot generalization: model trained on all tasks outperforms single-task models on held-out tasks
- Preserves interpretable cortical topography in generated fMRI
- Biological variability captured (inter-subject differences preserved)

## Biological Motivation

Human brain is intrinsically multimodal:
- Visual stimuli elicit both visual AND linguistic/semantic responses
- Semantic representations tile the entire cortex (Huth et al., 2016)
- Prior methods only use unimodal CLIP alignment → insufficient exploitation of brain's multimodal semantics

## Comparison with Prior Work

| Method | Paradigm | Modalities | Unified? |
|--------|----------|------------|----------|
| MindEye2 | brain→image (task-specific) | brain→vision only | No |
| BrainCLIP | brain↔CLIP alignment | unimodal | No |
| BrainFLORA | brain representation pretraining | brain only | No |
| **BrainJanus** | **any-to-any** | **brain+vision+language** | **Yes** |

## Pitfalls

- Discrete tokenization may lose fine-grained continuous information (trade-off for unification)
- Requires large paired brain-image-text datasets (NSD, GOD for training)
- Biological interpretability depends on tokenizer quality
- Zero-shot claims depend on task overlap in training distribution
