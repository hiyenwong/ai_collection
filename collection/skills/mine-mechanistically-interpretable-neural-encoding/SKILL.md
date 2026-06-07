---
name: mine-mechanistically-interpretable-neural-encoding
category: ai_collection
description: "MINE (Mechanistically Interpretable Neural Encoding) — a framework that applies mechanistic interpretability tools from LLMs to vision encoding models, revealing fine-grained functional selectivity at the voxel level in human visual cortex. (arXiv:2605.16468)"
tags: [mechanistic-interpretability, neural-encoding, visual-cortex, fmri, encoding-models, counterfactual-validation, functional-profiles, vision-science]
---

# MINE: Mechanistically Interpretable Neural Encoding

**Paper**: [arXiv:2605.16468](https://arxiv.org/abs/2605.16468) — Submitted 15 May 2026
**Authors**: Idan Daniel Grosbard, Mor Geva, Galit Yovel
**Categories**: cs.CV, cs.AI, cs.CL, cs.LG, q-bio.NC

## Overview

Traditional encoding models in vision neuroscience predict brain responses to natural images using DNNs, but treat the encoder as a **black box** — leaving open which specific image features drive each voxel's response. MINE opens this black box by adapting **mechanistic interpretability** techniques from LLM research to vision encoding models.

## Core Innovation

MINE predicts each voxel's response using **language-aligned image representations** (CLIP-like embeddings), then applies attribution methods to identify which image regions and semantic features are critical for each voxel's activation. Key components:

1. **Per-image attribution**: Attribution maps localizing critical features within specific natural images
2. **Per-voxel functional profiles**: Generalized descriptions of what each voxel responds to, aggregated across images
3. **Counterfactual validation**: Inserting/removing predicted features shifts activation in the expected direction — causal evidence

## Key Findings

### Fine-Grained Selectivity

- MINE recovers known categorical preferences of category-selective regions (FFA for faces, PPA for places, etc.)
- Reveals **fine-grained unique voxel structure** within each region — individual voxels within FFA show distinct face-part preferences
- Functional profiles are sufficiently precise to generate synthetic images that elicit matched responses

### Causal Validation

- **Counterfactual editing**: Removing predicted features reduces activation; inserting them increases it
- Per-voxel profiles enable even stronger activation shifts than per-image descriptions
- Demonstrates that mechanistic interpretability can provide **causal** (not just correlational) insight

### Application to Category-Selective Regions

Applied to well-studied regions, MINE:
- Recovers known selectivity patterns (faces, scenes, bodies, objects)
- Discovers novel within-region heterogeneity not visible in standard fMRI analyses
- Provides semantically interpretable descriptions of voxel function

## Methodology

```
Natural Image → CLIP/VLM Encoder → Voxel Response Prediction
                                    ↓
                    Attribution Analysis (per image)
                                    ↓
                    Per-Voxel Functional Profiles
                                    ↓
                    Counterfactual Validation
```

The framework uses:
- Language-aligned vision models (CLIP) for semantically meaningful representations
- Attribution methods (gradient-based or perturbation-based) to identify important features
- Generative models to synthesize validation stimuli
- Counterfactual editing for causal testing

## Significance

This bridges two fields:
- **Mechanistic interpretability** (from LLM research) — tools for understanding what model components do
- **Vision neuroscience** — understanding what drives neural responses

MINE demonstrates that these tools can reveal **new science** about the brain, not just about neural networks.

## Activation Keywords

- MINE framework, mechanistically interpretable neural encoding, voxel functional profiles, counterfactual brain validation, vision encoding interpretability, fine-grained voxel selectivity

## Related Skills

- [[target-space-recovery-profiles-brain-alignment]] — Different approach to model-brain evaluation
- [[naturality-violation-score]] — Category-theoretic brain-DNN alignment
