---
name: cross-scale-spatial-generative-neurodegeneration
description: "Cross-scale spatially-aware generative modeling of transcriptomic programs under... (arXiv: 2606.05870). Cross-domain neuroscience methodology combining computational physics/ML with brain dynamics analysis. Activation: psychosis, scaling, critical regime, renormalization group, generative modeling, neurodegeneration, transcriptomic."
---

## Context

Cross-scale spatially-aware generative modeling of transcriptomic programs underlying neurodegenerative brain organization

**Authors**: Krishnakumar Vaithianathan (for Alzheimer's Disease Neuroimaging Initiative)

**arXiv**: 2606.05870

**Submitted**: 2026-06-04

**Categories**: q-bio.NC, cs.LG, q-bio.QM

## Abstract

Neurodegenerative disorders such as Alzheimer's disease exhibit highly organized patterns of regional brain vulnerability, yet the biological mechanisms underlying this spatial selectivity remain incompletely understood. Existing imaging-transcriptomic studies have largely relied on correlation-based analyses between gene expression and neuroimaging phenotypes, limiting their ability to model how molecular organization gives rise to neurodegeneration. Here, we introduce a cross-scale spatially-aware generative framework for modeling transcriptomic programs underlying cortical neurodegeneration. Regional transcriptomic profiles were derived from the Allen Human Brain Atlas using 910 landmark genes across 68 cortical regions. Neurodegenerative vulnerability maps were constructed from ADNI FreeSurfer cortical thickness measurements by computing regional cortical thinning differences between cognitively normal controls (NC = 926) and Alzheimer's disease subjects (AD = 426). A variational generative architecture was used to learn latent biological programs linking regional gene-expression organization to cortical degeneration while incorporating graph-based spatial smoothness regularization to preserve cortical organization. The proposed framework achieved strong prediction of regional neurodegenerative vulnerability, yielding an explained variance of 0.8604 and a significant spatial correlation between predicted and observed cortical degeneration profiles (r = 0.9439, p < 0.001). The learned latent representations revealed structured transcriptomic organization associated with distributed disease susceptibility.

## Core Methodology

### Key Framework Components

1. **Variational Generative Architecture**
   - Latent biological programs linking gene-expression to degeneration
   - Graph-based spatial smoothness regularization preserving cortical organization

2. **Transcriptomic-Imaging Integration**
   - Allen Human Brain Atlas: 910 landmark genes × 68 cortical regions
   - ADNI FreeSurfer cortical thickness (NC=926, AD=426)

3. **Neurodegenerative Vulnerability Prediction**
   - Regional cortical thinning differences as vulnerability maps

## Key Results

- 86.04% explained variance in neurodegenerative vulnerability prediction
- Significant spatial correlation r=0.9439 (p<0.001)
- Variational generative architecture with graph-based spatial regularization
- 910 landmark genes across 68 cortical regions (Allen Human Brain Atlas)
- ADNI dataset: NC=926, AD=426 subjects
- Cross-scale modeling: microscale molecular → macroscale degeneration

## Implementation Steps

### Neurodegeneration Generative Modeling

1. Extract regional transcriptomic profiles from Allen Human Brain Atlas
2. Construct neurodegenerative vulnerability maps from cortical thickness measurements
3. Train variational generative model with graph-based spatial regularization
4. Validate with explained variance + spatial correlation metrics

## Pitfalls

- **Gene atlas coverage**: Allen Human Brain Atlas has limited donor samples — validate regional coverage
- **Cortical parcellation**: FreeSurfer parcellation quality affects vulnerability map accuracy — use validated pipelines

## Verification

- Achieved 86.04% explained variance, r=0.9439 (p<0.001) spatial correlation
- Validate latent representations reveal structured transcriptomic organization
- Reference: arXiv:2606.05870 (26 pages, 5 figures)

## Activation

neurodegeneration, generative modeling, transcriptomic, cortical degeneration, Alzheimer, variational, graph regularization, spatial correlation

## References

- arXiv paper: https://arxiv.org/abs/2606.05870
- DOI: https://doi.org/10.48550/arXiv.2606.05870
