---
name: texture-misalignment-cnn-perception
description: Perceptual misalignment of texture representations in convolutional neural networks — finds no connection between CNN Brain-Score and alignment with human texture perception, suggesting texture perception involves mechanisms distinct from object recognition CNNs. Based on arXiv:2604.01341.
---

# Perceptual Misalignment of Texture Representations in Convolutional Neural Networks

**arXiv**: 2604.01341 (v2, updated 18 May 2026) | **Authors**: Ludovica de Paolis, Fabio Anselmi, Alessio Ansuini, Eugenio Piasini

Investigates whether texture representations (Gram matrix-based feature correlations) in CNNs spontaneously align with human texture perception, and whether models with higher Brain-Score also possess more human-like texture representations.

## Key Contributions

1. **No correlation between Brain-Score and texture alignment**: CNNs regarded as better models of the visual system (higher Brain-Score) do NOT have more human-like texture representations
2. **Texture perception ≠ object recognition**: Texture perception involves mechanisms distinct from standard CNN object recognition approaches
3. **Gram matrix representations are perceptually misaligned**: The popular texture synthesis approach using CNN feature correlations does not capture perceptual texture content
4. **Systematic quantification**: Evaluated a diverse pool of CNNs, comparing feature correlation-based texture representations to perceptual judgments

## Method

- Diverse pool of CNNs evaluated (varying architecture, depth, training objective)
- Gram matrix-based texture representations extracted from multiple network layers
- Texture similarity judgments compared against human perceptual data
- Brain-Score used as conventional measure of model alignment with mammalian visual system
- Correlation analysis between Brain-Score and texture perception alignment

## Key Findings

- Texture representations from CNNs do not align with human texture perception
- No single layer or architecture consistently produces perceptually aligned texture features
- Models trained on object recognition develop representations that are partially misaligned with texture perception
- Contextual integration may be necessary for human-like texture perception
- Julesz's original insight (texture perception based on local correlations) may require higher-order statistics beyond linear feature correlations

## Implications

- Challenges the use of Gram matrix-based texture representations as perceptually meaningful
- Suggests texture perception in humans relies on mechanisms beyond what standard object recognition CNNs capture
- Indicates need for different computational approaches for texture perception modeling
- Raises questions about the validity of using CNN feature correlations for texture-related applications

## When to Use

- Evaluating CNN models as models of human visual perception
- Studying texture perception in biological and artificial vision
- Designing perceptually-aligned texture representations
- Analyzing limitations of Gram matrix-based texture methods
- Comparing Brain-Score with other perceptual alignment metrics

## Activation Keywords

texture perception, CNN texture representation, Gram matrix, Brain-Score, visual perception alignment, perceptual misalignment, Julesz texture, feature correlation, human vision modeling, texture synthesis evaluation
