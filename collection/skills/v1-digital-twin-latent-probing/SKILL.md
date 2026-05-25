---
name: v1-digital-twin-latent-probing
description: "Multi-level representational probing framework for digital twins of mouse V1. Systematically probes latent representations in neural activity-predicting models across three levels: (i) linear decodability from controlled visual probes, (ii) latent-unit tuning to canonical visual features, (iii) population geometry of hidden-layer activity. Reveals that digital twins with comparable prediction accuracy can differ substantially in internal representations. Activation: digital twin probing, V1 latent representations, population geometry, neural activity prediction, representational analysis, visual cortex modeling."
arxiv_id: "2605.23122"
published: "2026-05-22"
authors: "Adriano Lima, Yuchen Hou, Michael Beyeler, Marius Schneider"
tags: [digital-twins, V1-cortex, neural-representations, population-geometry, visual-neuroscience]
---

# Beyond Neural Activity Prediction: Probing Latent Representations in Mouse V1 Digital Twins

> Digital twins of sensory cortex are powerful response oracles, but models with similar prediction accuracy may rely on different latent representations. This paper systematically probes a family of mouse V1 digital twins across three representational levels to reveal hidden architecture differences.

**Source**: arXiv: [2605.23122](https://arxiv.org/abs/2605.23122)

## Core Methodology

### Key Innovation
While digital twin models of V1 are typically evaluated solely on neural activity prediction accuracy, this paper argues that prediction accuracy alone is insufficient to understand the latent representations driving those predictions. It introduces a multi-level probing framework as a complementary evaluation approach.

### Technical Framework

1. **Model Family**: Train a family of digital twins of mouse V1 on the same naturalistic video data from freely moving mice, differing only in visual-encoder architecture
2. **Level 1 — Linear Decodability**: Probe with controlled visual stimuli (orientation, contrast, motion); measure how linearly decodable these features are from hidden-layer activity
3. **Level 2 — Unit Tuning**: Characterize latent-unit selectivity for canonical visual features: orientation selectivity, contrast response, spatial-frequency tuning
4. **Level 3 — Population Geometry**: Analyze hidden-layer activity using eigenspectra — measure eigenvalue decay rates as a proxy for representational dimensionality
5. **Cross-Architecture Correlation**: Correlate neural-response prediction accuracy with each probing metric

### Key Results
- **Better neural prediction correlates** with stronger probe accuracy across all architectures
- **Highly predictive models** exhibit flatter hidden-population eigenspectra, indicating higher-dimensional representations closer to population-geometry signatures reported in mouse V1
- **Representational properties covary** with prediction accuracy overall
- **But models with comparable prediction scores** can still differ substantially in probe performance and latent-unit tuning
- Establishes multi-level representational probing as a **necessary complement** to standard neural-prediction evaluation

## Applications

- **Digital twin validation**: Go beyond prediction accuracy to understand what models actually learn
- **Model comparison**: Distinguish between models that achieve similar loss but through different computational strategies
- **Architecture design**: Guide visual encoder choices by how they affect latent representations
- **In silico experiments**: Ensure digital twins used for stimulus design and hypothesis generation rely on biologically plausible representations
- **Benchmark development**: Create multi-level benchmarks for evaluating sensory cortex models

## Related Skills

- brain-digital-twins-execution-semantics
- neural-manifold-learning-dynamics
- neural-population-decoding
- feedforward-dynamics-stimulus-encoding
