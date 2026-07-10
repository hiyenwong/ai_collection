---
name: mine-neural-encoding-mechanistic-interpretability
description: "Mechanistically Interpretable Neural Encoding (MINE) — applying mechanistic interpretability tools (feature attribution, counterfactual editing) to open the black box of voxel-level neural encoding models. Use when: (1) analyzing which image features drive specific voxel responses, (2) generating interpretable descriptions of neural selectivity, (3) performing causal validation of encoding model features, (4) discovering fine-grained functional organization within category-selective brain regions."
arxiv_id: "2605.16468"
published: "2026-05-15"
authors: "Idan Daniel Grosbard, Mor Geva, Galit Yovel"
tags: [mechanistic interpretability, neural encoding, fMRI, voxel-wise encoding, counterfactual editing, visual cortex, language-aligned representations, functional selectivity]
---

# MINE: Mechanistically Interpretable Neural Encoding

**Paper**: arXiv:2605.16468 - "Mechanistically Interpretable Neural Encoding Reveals Fine-Grained Functional Selectivity in Human Visual Cortex"

**Authors**: Idan Daniel Grosbard, Mor Geva, Galit Yovel

**Published**: 2026-05-15 (40 pages, 28 figures)

## Overview

MINE (Mechanistically Interpretable Neural Encoding) opens the black box of neural encoding models by applying mechanistic interpretability tools (originally developed for LLMs) to localize and causally validate the specific visual features that drive millimeter-scale (voxel-level) brain activity in human visual cortex.

## Core Concept

Rather than treating the encoder as a correlational black box that predicts fMRI responses, MINE:

1. **Identifies** which specific visual features drive each voxel's response
2. **Generates** semantically interpretable descriptions of each voxel's selectivity
3. **Validates causally** through counterfactual image editing
4. **Generalizes** per-image attributions into per-voxel functional profiles

## Key Technical Insights

1. **Language-aligned encoding**: Predicts each voxel's response using language-aligned image representations (CLIP embeddings), enabling attribution of voxel responses to specific semantic features. Trains voxel-wise linear encoding models on the Natural Scenes Dataset (NSD).

2. **Per-voxel functional profiles**: Generalizes per-image feature attributions into a compact description of what visual features each voxel is selective to. These profiles capture stable selectivity that generalizes across diverse stimuli.

3. **Causal validation via image synthesis**: Shows that per-image feature descriptions are sufficient to generate synthetic images that elicit matching voxel responses — more accurately than random or low-attribution controls. This is a generative validation step.

4. **Counterfactual editing**: Inserting or removing predicted features from natural images shifts voxel activation in the expected direction, providing causal evidence. Per-voxel activation profiles produce even stronger shifts than per-image descriptions alone.

5. **Fine-grained organization**: Recovers known category-selective region preferences (FFA → faces, PPA → places, EBA → bodies) while revealing unique voxel-level structure within each region — individual voxels in the same region have distinct, heterogeneous selectivity beyond the region's known preference.

## Methodology Detail

### Stage 1: Encoding Model
- Use CLIP vision encoder to extract language-aligned image features
- Train ridge regression voxel-wise encoding models on NSD fMRI data
- Each voxel gets a weight vector over CLIP feature dimensions

### Stage 2: Feature Attribution
- For each image-voxel pair, compute attribution scores identifying which CLIP features drive the voxel's response
- Methods: integrated gradients, attention rollout, or direct weight analysis
- Threshold attributions to identify the most predictive visual features

### Stage 3: Profile Construction
- Aggregate per-image attributions across hundreds of natural images
- Build per-voxel functional profiles: semantic descriptions of selectivity
- Validate profile stability through split-half reliability

### Stage 4: Causal Validation
- **Generation test**: Use profile descriptions to guide text-to-image generation (e.g., DALL-E, SD); measure whether synthetic images activate the voxel as predicted
- **Counterfactual test**: Use diffusion-based inpainting to add/remove predicted features from natural images; measure whether activation shifts in expected direction
- **Profile-guided editing**: Use per-voxel profiles for targeted feature manipulation

## Key Findings

| Finding | Description |
|---------|-------------|
| Region recovery | MINE recovers known preferences (FFA→faces, PPA→places, EBA→bodies) |
| Fine-grained structure | Voxels within same region have unique, heterogeneous selectivity |
| Causal evidence | Counterfactual editing produces activation shifts in expected direction |
| Profile generalization | Per-voxel profiles generalize across diverse stimulus sets |
| Profile superiority | Profile-guided editing outperforms per-image description-guided editing |

## Applications

- **Neuroscience**: Discover fine-grained functional organization of visual cortex at voxel-level resolution
- **Brain-Model alignment**: Probe which specific features of artificial neural networks align with biological representations
- **Clinical**: Identify voxel-level biomarkers for visual processing deficits
- **Interpretability**: Generate human-readable descriptions of neural selectivity

## Related Skills

- [[platonic-representations-brain-universal-geometry]] - Cross-subject neural geometry alignment
- [[brain-dnn-transformation-alignment]] - Brain-DNN representational analysis
- [[feature-visualization-brain-encoder]] - Feature visualization for brain encoders

## References

- Grosbard, I. D., Geva, M., & Yovel, G. (2026). Mechanistically Interpretable Neural Encoding Reveals Fine-Grained Functional Selectivity in Human Visual Cortex. arXiv:2605.16468.
- NSD: Allen et al. (2022) - Natural Scenes Dataset
- CLIP: Radford et al. (2021) - Learning Transferable Visual Models From Natural Language Supervision

## Activation

Use this skill when:
- Analyzing neural encoding models beyond prediction accuracy
- Interpreting voxel-level functional selectivity in visual cortex
- Designing causal validation experiments for brain encoding models
- Studying fine-grained organization of category-selective visual regions
- Applying mechanistic interpretability methods to neuroscience data

## Activation Keywords

- MINE framework, mechanistically interpretable neural encoding, voxel-wise mechanistic interpretability, neural encoding interpretability, counterfactual brain encoding, functional selectivity profiling, voxel functional profiles, language-aligned brain encoding, fMRI mechanistic interpretability, fine-grained visual cortex organization, feature attribution neural encoding, causal validation encoding models
