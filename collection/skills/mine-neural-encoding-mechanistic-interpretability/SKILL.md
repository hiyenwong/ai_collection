---
name: mine-neural-encoding-mechanistic-interpretability
description: "Mechanistically Interpretable Neural Encoding (MINE) — applying mechanistic interpretability tools (feature attribution, counterfactual editing) to open the black box of voxel-level neural encoding models. Use when: (1) analyzing which image features drive specific voxel responses, (2) generating interpretable descriptions of neural selectivity, (3) performing causal validation of encoding model features, (4) discovering fine-grained functional organization within category-selective brain regions."
arxiv_id: "2605.16468"
published: "2026-05-15"
authors: "Idan Daniel Grosbard, Mor Geva, Galit Yovel"
tags: [mechanistic interpretability, neural encoding, fMRI, voxel-wise encoding, counterfactual editing, visual cortex, language-aligned representations, functional selectivity]
---

# MINE: Mechanistically Interpretable Neural Encoding

Core concept from arXiv:2605.16468 (Grosbard, Geva & Yovel, 2026).

## Core Concept

MINE opens the black box of neural encoding models by applying mechanistic-interpretability tools (originally developed for LLMs) to localize the specific image features that drive millimeter-scale (voxel-level) brain activity. Rather than treating the encoder as a correlational black box that predicts fMRI responses, MINE produces semantically interpretable descriptions of what each voxel "cares about" and provides causal validation through counterfactual image editing.

## Key Technical Insights

1. **Language-aligned encoding**: Predicts each voxel's response using language-aligned image representations (CLIP-like), enabling the attribution of voxel responses to specific semantic features.

2. **Per-voxel functional profiles**: Generalizes per-image feature attributions into per-voxel functional profiles — a compact description of what visual features each voxel is selective to.

3. **Causal validation via image synthesis**: Shows that per-image feature descriptions are sufficient to generate synthetic images that elicit matching voxel responses, more accurately than random or low-attribution controls.

4. **Counterfactual editing**: Inserting or removing predicted features from natural images shifts voxel activation in the expected direction, providing causal evidence. Per-voxel activation profiles produce even stronger shifts than per-image descriptions.

5. **Fine-grained organization**: Reveals unique voxel-level structure within well-studied category-selective regions (e.g., FFA, PPA), showing that individual voxels within a region have distinct, fine-grained functional selectivity beyond the region's known categorical preference.

## Implementation Approach

The framework consists of several stages:
- Train a voxel-wise encoding model using language-aligned image features
- Apply feature attribution (e.g., integrated gradients, attention rollout) to identify which features drive each voxel
- Aggregate per-image attributions into stable per-voxel functional profiles
- Validate through: (a) image generation from descriptions, (b) counterfactual feature manipulation in natural images
- Use the validated profiles to discover novel functional organization within known brain regions

## Applications

- **Neuroscience**: Discover fine-grained functional organization of visual cortex at the voxel level
- **Brain-Model alignment**: Probe which specific features of artificial neural networks align with biological representations
- **Clinical**: Identify voxel-level biomarkers for visual processing deficits
- **Interpretability**: Generate human-readable descriptions of neural selectivity

## Activation Keywords

- MINE framework, mechanistically interpretable neural encoding, voxel-wise mechanistic interpretability, neural encoding interpretability, counterfactual brain encoding, functional selectivity profiling, voxel functional profiles, language-aligned brain encoding, fMRI mechanistic interpretability, fine-grained visual cortex organization, feature attribution neural encoding, causal validation encoding models
