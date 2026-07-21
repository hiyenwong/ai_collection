---
name: v1-digital-twin-probing
description: >
  Beyond Neural Activity Prediction: Probing Latent Representations in Mouse V1
  Digital Twins. Systematic multi-level probing framework for evaluating latent
  representations in sensory cortex digital twins, across linear decodability,
  latent-unit tuning, and population geometry.
  Activation: V1 digital twin, latent representation probing, neural prediction,
  population geometry, representational similarity, mouse V1 encoding, digital
  twin evaluation, sensory cortex modeling
---

# V1 Digital Twin Probing: Beyond Neural Activity Prediction

Paper: arXiv:2605.23122 (May 22, 2026)
Authors: Adriano Lima, Yuchen Hou, Michael Beyeler, Marius Schneider
Affiliations: University of California, Santa Barbara

## Core Problem

Digital twins of sensory cortex serve as powerful response oracles, but **prediction accuracy alone provides limited insight** into the latent representations that support those predictions. As digital twins are increasingly used as in silico experimental systems for stimulus design and hypothesis generation, understanding their internal representations becomes critical — models with similar prediction accuracy may rely on fundamentally different latent representations.

## Multi-Level Probing Framework

The authors propose a **three-level systematic probing framework** applied to a family of digital twins of mouse V1 trained to predict neural activity from naturalistic videos in freely moving mice:

### Level 1: Linear Decodability
- Controlled visual probes of **orientation, contrast, and motion**
- Measures how readily latent features can be linearly decoded from hidden representations
- Directly tests whether the model encodes these elementary visual features

### Level 2: Latent-Unit Tuning
- Characterizes individual hidden-unit selectivity to canonical visual features:
  - **Orientation selectivity** (tuning curve width, preferred orientation)
  - **Contrast response** (contrast gain, response saturation)
  - **Spatial frequency tuning** (peak spatial frequency, bandwidth)
- Compares tuning properties to in vivo V1 physiology

### Level 3: Population Geometry
- Hidden-layer population activity analyzed via:
  - **Eigenspectra** of the neural covariance matrix
  - **Dimensionality** (participation ratio, explained variance)
  - **Geometry comparisons** to population signatures in mouse V1

## Key Findings

1. **Prediction accuracy correlates with probe performance**: Better neural-response prediction correlates with stronger probe accuracy across all three levels.

2. **Flatter eigenspectra in better models**: Highly predictive models exhibit flatter hidden-population eigenspectra, indicating **higher-dimensional representations** — closer to population geometry signatures reported in mouse V1.

3. **Divergence despite equal prediction**: Digital twins with comparable prediction scores can still differ substantially in probe performance and latent-unit tuning, revealing that **prediction accuracy is not a complete evaluation metric**.

4. **Architecture matters**: The visual-encoder architecture choice shapes the latent representational geometry independently of pure prediction performance.

## Methodology

- **Training Data**: Naturalistic videos from freely moving mice + corresponding V1 neural activity
- **Model Family**: Multiple visual-encoder architectures sharing the same training objective
- **Probes**: Synthesized stimuli spanning orientation, contrast, and motion parameter spaces
- **Analysis**: Linear decoding, tuning curve fitting, and population geometry (eigenspectrum analysis)

## Implications

- Digital twins should be evaluated not just on prediction accuracy but on **representational fidelity**
- The probing framework provides a **complement to standard neural-prediction evaluation**
- Enables understanding digital twins as **substrates for studying visual computations**, not just as predictors
- Framework is transferable to other sensory modalities and brain regions

## References

- Lima et al. (2026). Beyond Neural Activity Prediction: Probing Latent Representations in Mouse V1 Digital Twins. arXiv:2605.23122
- Schneider et al. (2023). Digital twins of the brain: current state and future directions.
- Yamins & DiCarlo (2016). Using goal-driven deep learning models to understand sensory cortex.
