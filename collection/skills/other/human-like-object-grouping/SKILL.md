---
name: human-like-object-grouping
description: "Behavioral benchmark and object-centricity analysis for self-supervised vision transformers. Uses two-dot same/different judgment task with 1020+ trials to measure human object grouping, and proposes Gram matrix alignment as a mechanism for improving behavioral alignment. Use when: vision transformer evaluation, object segmentation, self-supervised learning, DINO models, behavioral neuroscience benchmarks, Gram matrix distillation, human-AI visual alignment, psychophysics."
metadata:
  arxiv_id: "2603.13994"
  published: "2026-03-14"
  authors: "Hossein Adeli, Seoyoung Ahn, Andrew Luo, Mengmi Zhang, Nikolaus Kriegeskorte, Gregory Zelinsky"
  tags: [vision-transformer, self-supervised, object-segmentation, behavioral-benchmark, gram-matrix, dino, neuroscience]
---

# Human-like Object Grouping in Self-supervised Vision Transformers

**arXiv**: [2603.13994](https://arxiv.org/abs/2603.13994) (cs.CV, cs.AI, q-bio.NC)
**Authors**: Hossein Adeli, Seoyoung Ahn, Andrew Luo, Mengmi Zhang, Nikolaus Kriegeskorte, Gregory Zelinsky (Columbia, HKU, NTU, Stony Brook)
**Updated**: v3, 2026-07-09

## Core Insight

Self-supervised vision transformers (especially DINO family) implicitly learn object-centric representations that align with human perceptual grouping behavior. The key mechanism is **Gram matrix structure** — pairwise feature similarity across image patches encodes object boundaries.

## Methodology

### Behavioral Benchmark: Two-Dot Paradigm
- **Task**: Participants judge whether two dots on a natural scene are on the same object or different objects
- **Measure**: Reaction time (RT) reveals object grouping difficulty
- **Scale**: 72 participants, 255 images × 4 conditions = 1020 trials (COCO2017 images)
- **Conditions**: same-close, same-far, different-close, different-far
- **Key effect**: "Same-object advantage" — faster RTs when dots are on same object

### Object-Centricity Metric
- Compute **affinity maps**: cosine similarity of each patch token with all others
- **ROC analysis**: True Positive Rate (within-object patches) vs False Positive Rate (outside-object)
- **AUC**: single number quantifying object-centric structure in representations
- Result: DINOv3 ViT-B achieves highest AUC; deeper layers → stronger object-centricity

### Behavioral Prediction
- MLP readout on concatenated patch features from two dot locations
- Predict trial-by-trial RTs, normalized to human noise ceiling
- DINOv3 ViT-B: highest noise-normalized Spearman correlation
- Training objective > architecture in driving object-centricity

### Gram Matrix Alignment (Key Mechanism Finding)
- Fine-tune supervised models to match Gram matrix of DINOv3 while maintaining classification
- **Result**: +8-18pp grouping accuracy, substantial object-centric AUC gains
- Transformers more responsive than ConvNets (self-attention naturally encodes pairwise relations)

## Key Results

| Model | Architecture | Training | Grouping Acc | Object-Centric AUC |
|-------|-------------|----------|-------------|-------------------|
| DINOv3 ViT-B | Transformer | Self-supervised | 91.9% | Highest |
| DINOv2 ViT-B | Transformer | Self-supervised | 89.0% | High |
| DINOv3 ConvNeXt-B | Convolutional | Distilled | 86.7% | High |
| MAE ViT-B | Transformer | Self-supervised | 80.7% | Medium |
| IN21k ViT-B | Transformer | Supervised | 72.2% | Low |
| IN1K ConvNeXt-B | Convolutional | Supervised | 60.0% | Lowest |

- Object-centric AUC ↔ behavioral alignment: Spearman r=0.950, p=0.0001
- Stronger object-centric structure → better human RT prediction across ALL model types

## Significance

1. **Neuroscience bridge**: Self-supervised vision models capture object-level organization similar to human visual cortex
2. **Training objective matters more than architecture**: DINO > supervised with same architecture
3. **Gram matrix as active ingredient**: Pairwise feature correlation structure drives object-centricity
4. **Distillation path**: Supervised models can be improved via Gram alignment without retraining from scratch

## Activation Keywords

- vision transformer evaluation, object segmentation, self-supervised learning, DINO, behavioral benchmark
- psychophysics, two-dot paradigm, Gram matrix alignment, object-centric representations
- human-AI visual alignment, patch similarity, affinity maps, behavioral prediction
- perceptual grouping, Gestalt, same-object advantage, noise ceiling