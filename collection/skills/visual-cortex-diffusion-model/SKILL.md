---
name: visual-cortex-diffusion-model
description: "Skill for understanding and applying the mechanistic model of inference in visual cortex equivalent to a minimal diffusion model, linking sparse coding with recurrent dynamics and horizontal connections in V1. Based on arXiv:2607.15693."
activation: visual cortex diffusion model, sparse coding inference, recurrent diffusion model
## Overview of the model:
   - Sparse coding with non-factorial prior over latent variables via pairwise interaction matrix.
   - Recurrent dynamical system equivalent to a minimal diffusion model.
   - Parameters: interaction matrix (horizontal connections), denoising score-matching objective.

2 Training procedure:
   - Train recurrent dynamics using denoising score-matching on natural images.
   - Use implicit differentiation for efficient gradient computation.
   - Learned interaction matrix mirrors horizontal connections in superficial V1 linking similar orientation tuning.

3 Analysis and interpretation:
   - Compute Jacobian of the recurrent dynamics; decompose via interaction matrix.
   - Reveals how recurrent dynamics assign probability to continuous family of natural structural deformations (e.g., extended contours).
   - Identify subset of latent variables that disconnect from visual input, forming hierarchical representation enforcing global consistency.

4 Applications:
   - Neuroscience: generates testable hypotheses about functional connectivity in recurrent circuits during perceptual inference.
   - Machine learning: provides interpretable mechanism inside diffusion models, explaining generalization and sample quality.

5 Experimental validation:
   - Denoising performance matches black-box diffusion models in generalization regime.
   - Qualitative analysis of learned interaction matrix vs. known V1 horizontal connectivity.

## Pitfalls
- Ensure proper normalization of input images when implementing the denoising score-matching loss.
- The interaction matrix is unconstrained pairwise; symmetry may be enforced for stability.
- Implicit differentiation requires careful handling of fixed-point iteration to avoid divergence.

## References
- arXiv:2607.15693v1 "Toward a mechanistic understanding of inference in visual cortex and diffusion models"
- Related sparse coding and diffusion model literature.

## References Files
- references/arxiv-2607.15693.md (optional)