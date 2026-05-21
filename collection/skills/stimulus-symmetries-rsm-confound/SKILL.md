---
name: stimulus-symmetries-rsm-confound
description: Stimulus symmetries can confound representational similarity analyses — demonstrates how stimulus symmetries in neural network inputs cause functionally-equivalent representations to produce different, drifting RSM geometries. Based on arXiv:2605.21324.
---

# Stimulus Symmetries Can Confound Representational Similarity Analyses

**arXiv**: 2605.21324 | **Authors**: Farhad Pashakhanloo, Jacob A. Zavatone-Veth (Harvard University)

Shows that symmetries in network inputs can confound RSM-based analyses of neural representations. Stimulus symmetries render many representations functionally equivalent, but different configurations can lead to different representational similarity matrices with qualitatively different geometries.

## Key Contributions

1. **Gauge-dependence of RSMs**: Demonstrates formally that stimulus symmetries create gauge freedom in representations — functionally equivalent codes can yield different RSMs
2. **Drifting RSMs**: SGD or energetic regularization can produce sparse, drifting neural codes, causing RSMs to drift over training without change in task performance
3. **Latent symmetry in real data**: Shows these phenomena occur in networks trained on natural image data where the symmetry is latent (e.g., orientation/phase symmetries)
4. **Beyond rotation equivalence**: Functionally-equivalent representations may not be related by simple rotation, challenging the assumption underlying RSM invariance

## Key Results

- RSMs depend on the specific gauge choice (parameterization) of functionally-equivalent representations
- Gauge-dependence persists even as network width → ∞ in certain regimes
- Energy-minimizing codes (via SGD or explicit regularization) converge to sparse representations that tile the stimulus manifold, producing qualitatively different RSMs than their dense counterparts
- Drifting RSM geometries reflect real geometric variability, not just noise
- Image-trained networks exhibit these effects despite not having explicit symmetric input structure

## Method

- Theoretical formalism linking input symmetries (group actions) to RSM gauge-dependence
- Toy model: orientation-tuned neurons with circular stimulus symmetry
- Spherical stimulus spaces with reflection symmetries
- Real image data (MNIST, CIFAR) autoencoder training
- Comparison of RSM variability across training seeds, checkpoints, and regularizers

## When to Use

- Analyzing representational similarity across neural networks (biological or artificial)
- Interpreting RSA/CKA results where symmetry in stimuli exists
- Comparing representations across training runs, seeds, or initializations
- Evaluating whether RSM differences reflect meaningful representational change
- Designing benchmarking studies for neural code similarity

## Activation Keywords

representational similarity analysis, RSM gauge dependence, stimulus symmetry, RSA confound, neural code comparison, drifting representations, representational geometry, functionally equivalent representations, neural manifold tiling, CKA limitations, RSA robustness, stimulus invariance
