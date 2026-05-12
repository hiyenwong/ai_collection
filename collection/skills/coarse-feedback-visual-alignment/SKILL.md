---
name: coarse-feedback-visual-alignment
description: >
  Coarse feedback for human-aligned visual representations. Use when: studying how supervisory signal
  granularity affects brain alignment in neural networks, designing brain-aligned vision models with
  minimal supervision, comparing coarse vs fine-grained training objectives, deriving coarse category
  labels from pretrained embeddings (PCA-based splits), representational similarity analysis (RSA) of
  neural/behavioral alignment, building AI systems aligned with human perception, or investigating what
  optimization objectives shape biological vision. Covers: coarse-supervised training, PCA-derived
  category labels, RSA methodology, macaque/monkey electrophysiology alignment, human fMRI alignment,
  behavioral similarity benchmarking (THINGS dataset), convolutional/transformer architectures.
  arXiv: 2605.05556 (Mehta & Bonner, 2026).
---

# Coarse Feedback for Human-Aligned Visual Representations

Core finding: neural networks trained on as few as **2–8 broad categories** learn representations
that match or exceed the brain alignment of 1000-class supervised models, and achieve the highest
alignment with human perceptual similarity judgments among all tested architectures.

## Key Results

### Neural Alignment (RSA vs brain recordings)
- **Macaque V1**: 2 coarse classes suffice to match 1000-class alignment
- **Macaque IT**: 8 coarse classes suffice to match 1000-class alignment
- **Human early visual stream**: 2 classes suffice
- **Human ventral stream**: 8 classes suffice
- Validated across AlexNet-derived and CLIP-derived labels; pixel-based labels fail

### Behavioral Alignment (RSA vs human similarity judgments)
- Coarse-trained models **substantially exceed** 1000-class models in alignment with THINGS dataset
- Peak at 4–8 categories, then plateau
- Outperforms all tested pretrained models (CNNs, Transformers, self-supervised, large-scale)
- **80%+ of 1,854 object concepts** better captured by coarse model vs fine-grained
- Advantage extends across **all semantic categories** (animals, food, tools, vehicles, etc.)

### Data Efficiency
- Coarse models trained on ~1% of ImageNet outperform 1000-class models trained on 100% of ImageNet
  in behavioral alignment

### Architecture Generality
- Pattern holds across ResNet-50, ConvNeXt, and ViT-B/16
- Most pronounced for ConvNeXt and ViT-B/16

## Method: Deriving Coarse Category Labels

### PCA-Based Recursive Splitting
1. Encode all training images using a pretrained model (AlexNet or CLIP)
2. Compute PCA on the embedding space
3. Recursively split data along PCA median: each split doubles category count
4. This yields 2, 4, 8, 16, 32, 64 categories — data-driven, no manual annotation
5. Apply same splits to source model's training data

### Key Design Choices
- Labels must reflect **high-level visual content** structure, not low-level pixel statistics
- Source model choice (AlexNet vs CLIP) does not qualitatively change results
- Categories must be derived from semantic/representational structure, not raw features

## RSA Protocol

### Neural Alignment
1. Extract activations from each layer of the test network
2. Compute Representational Dissimilarity Matrix (RDM) for each layer
3. Compare to neural RDMs from macaque spiking (TVSD) or human fMRI (NSD)
4. Measure Spearman ρ between RDMs; bootstrap 95% CIs
5. Evaluate across early and late ventral visual regions separately

### Behavioral Alignment
1. Use THINGS behavioral embeddings (66-dim, from 4.7M odd-one-out trials)
2. Compute RDM from network activations for THINGS stimuli
3. Compare to behavioral RDM via Spearman ρ
4. Decompose by individual concept and semantic category

## Implications for Brain-Model Alignment

### What This Changes
- Field has moved toward **finer-grained** objectives (self-supervised, contrastive)
- This work shows **coarser is better** for human alignment
- Challenges assumption that complex supervision is necessary for brain-aligned representations
- Suggests biological vision may use rudimentary optimization objectives

### Biological Plausibility
- Developing brain shows coarse categorical distinctions (animate/inanimate) by 2 months
- Potential coarse feedback pathways: prefrontal→IT, dopaminergic modulation, amygdala projections,
  thalamic feedback
- Suggests hierarchical curriculum: coarse scaffold → fine-grained elaboration

### Practical Applications
- Build brain-aligned vision models with minimal supervision
- No manual annotation needed — data-driven category derivation
- Scales to any pretrained model and any modality
- Potential for coarse-to-fine curriculum learning

## Benchmark Comparison

When benchmarked against pretrained models, coarse-supervised models (8 classes) achieve:
- Higher behavioral alignment than DINOv2, CLIP, and other leading vision models
- Better alignment despite being trained on ImageNet (smaller dataset than many competitors)
- Consistent advantage across all semantic categories

## References
- arXiv: 2605.05556
- Mehta, Y. & Bonner, M.F. (2026). An extremely coarse feedback signal is sufficient for
  learning human-aligned visual representations. Johns Hopkins University.
- THINGS dataset: Hebart et al. (2020) — 4.7M triplet judgments, 1,854 concepts
- RSA methodology: Kriegeskorte et al. (2008)
