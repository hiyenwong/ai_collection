---
name: nonlocal-operator-fmri-encoding
description: "Neural integral operator framework for fMRI encoding and decoding tasks — uses latent neural integral operators with fixed-point iterations to model spatiotemporal brain dynamics, with systematic analysis of spatiotemporal context effects on performance and latent-space geometry."
arxiv_id: "2605.20389"
published: "2026-05-19"
authors: "Andreas Kramer, Saugat Acharya, Alice Giola, Emanuele Zappala"
tags: [fmri-encoding, neural-operator, fmri-decoding, spatiotemporal-context, brain-dynamics, representation-learning]
---

# Nonlocal Operator Learning for fMRI Encoding and Decoding

## Core Concept

Proposes a **neural integral operator** framework for modeling fMRI dynamics, treating brain activity as a nonlocal spatiotemporal process. The model performs fixed-point iterations in an auxiliary latent space, from which both stimulus classification (decoding) and fMRI dynamics prediction (encoding) are performed.

## Key Contributions

1. **Neural Integral Operator Architecture**: Implements a latent neural integral operator framework that captures **nonlocal spatiotemporal dependencies** in fMRI data — dependencies that standard convolutional or recurrent architectures struggle with.

2. **Systematic Context Analysis**: Compares short vs. long temporal windows and visual cortex vs. whole-brain recordings to quantify how spatiotemporal context affects:
   - Decoding performance (stimulus → fMRI)
   - Encoding performance (fMRI → stimulus)
   - Latent-space geometry and class separation

3. **Key Findings**:
   - Larger temporal windows consistently improve both encoding and decoding
   - Learned latent space often provides clearer class separation than raw fMRI data
   - Exploiting **distributed nonlocal structure** requires architectures specifically designed for such dependencies
   - Encoding remains moderately challenging, but benefits consistently from longer temporal context

## Methodology

### Model Architecture
1. **Input**: fMRI time-series data (spatiotemporal)
2. **Neural Integral Operator**: Fixed-point iterations in auxiliary latent space
   - Captures nonlocal interactions between brain regions across time
   - Architecture naturally handles varying temporal windows
3. **Decoder**: Maps latent representations to:
   - Stimulus predictions (decoding task)
   - Future fMRI states (encoding task)

### Experimental Design
- **Datasets**: Two open-source fMRI datasets
- **Variables manipulated**:
  - Temporal window length (short vs. long)
  - Spatial coverage (visual cortex vs. whole brain)
- **Evaluation metrics**: Prediction accuracy, latent-space geometry analysis

## Relationship to Existing Methods

- **Vs. CNNs/RNNs**: Integral operators explicitly model nonlocal dependencies that sequential/recurrent models capture only indirectly
- **Vs. Transformers**: Shares attention-like global connectivity but with mathematically principled operator-theoretic foundation
- **Vs. Standard encoding models**: Provides a unified framework for both encoding and decoding

## Applications

- **fMRI encoding/decoding**: End-to-end modeling of brain-response dynamics
- **Brain-computer interfaces**: Leveraging spatiotemporal context for improved decoding
- **Cognitive state decoding**: Using learned latent representations for brain-state classification
- **Computational neuroscience**: Understanding how distributed nonlocal brain dynamics support information processing

## Activation Keywords
- neural-operator-fmri, nonlocal-fmri, integral-operator-brain, spatiotemporal-fmri, fmri-encoding-decoding, latent-dynamics-fmri, context-dependent-fmri, fmri-representation-learning, nonlocal-neural-operator
