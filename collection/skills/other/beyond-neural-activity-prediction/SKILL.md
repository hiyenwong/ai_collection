---
name: beyond-neural-activity-prediction
description: Multi-level representational probing framework for evaluating digital twins of sensory cortex beyond standard prediction accuracy. Probes latent representations (linear decodability, latent-unit tuning, population geometry) in mouse V1 digital twins. Based on arXiv:2605.23122 (May 2026). Use when evaluating brain digital twins, comparing model architectures for neural prediction, or studying latent representations in vision models.
---

# Beyond Neural Activity Prediction: Probing Latent Representations in Mouse V1 Digital Twins

Methodology from arXiv:2605.23122 (May 2026).
Authors: Adriano Lima, Yuchen Hou, Michael Beyeler, Marius Schneider
Subjects: q-bio.NC

## Overview

This paper addresses a critical gap in evaluating digital twins of sensory cortex: although prediction accuracy is the central metric, it provides limited insight into the latent representations that support those predictions. Models with similar prediction accuracy may rely on **different latent representations**, which matters increasingly as digital twins are used for in silico experimental design.

## Key Findings

### 1. Prediction Accuracy Correlates with Representation Quality
- Across architectures, better neural-response prediction correlates with:
  - Stronger probe accuracy (linear decodability of visual features)
  - Flatter hidden-population eigenspectra (higher-dimensional representations)
  - Closer population-geometry signatures to mouse V1

### 2. Comparable Accuracy ≠ Comparable Representations
- Digital twins with comparable prediction scores can differ substantially in:
  - Probe performance
  - Latent-unit tuning properties

### 3. Multi-Level Probing Framework
Three levels of latent representation characterization:

#### Level 1: Linear Decodability
- Controlled visual probes of orientation, contrast, and motion
- Tests whether visual features are linearly accessible in latent space

#### Level 2: Latent-Unit Tuning
- Orientation selectivity index
- Contrast response functions
- Spatial-frequency tuning

#### Level 3: Population Geometry
- Hidden-layer activity eigenspectra
- Dimensionality of representations
- Comparison with mouse V1 population signatures

## Methodology

1. **Train digital twins** of mouse V1 with different visual-encoder architectures sharing:
   - Same training data (naturalistic videos from freely moving mice)
   - Same neural-prediction objective

2. **Freeze models** after training

3. **Systematically probe** latent representations at three levels

4. **Correlate** representation quality with prediction accuracy

5. **Compare** models with comparable prediction but different representations

## Implications
- **Digital twin validation**: Prediction accuracy alone is insufficient — latent representation quality matters
- **Model selection**: Different architectures with similar accuracy may support different in silico experiments
- **Brain-AI alignment**: Representation probing provides mechanistic understanding beyond correlation-based evaluation

## Activation Keywords
- digital twin, neural prediction, latent representation
- V1 modeling, mouse cortex, representational probing
- population geometry, linear decodability, neural encoding
- model comparison, brain digital twin evaluation
