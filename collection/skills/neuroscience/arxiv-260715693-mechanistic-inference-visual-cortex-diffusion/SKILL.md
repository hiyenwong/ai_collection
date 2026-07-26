---
name: arxiv-260715693-mechanistic-inference-visual-cortex-diffusion
description: A skill for understanding and applying the methods from the arXiv paper: Toward a mechanistic understanding of inference in visual cortex and diffusion models
---

# Toward a mechanistic understanding of inference in visual cortex and diffusion models

**arXiv ID**: [2607.15693v1](http://arxiv.org/abs/2607.15693v1)
**Authors**: Zeyu Yun, Alexander Belsten, Dasheng Bi, Zahra Kadkhodaie, Yubei Chen, Bruno A. Olshausen
**Date**: 2026-07-17
**Categories**: q-bio.NC, cs.AI

## Abstract

We describe a model of perceptual inference in primary visual cortex (V1) equivalent to a minimal diffusion model whose function can be readily understood from its parameters. The model is based on sparse coding with a non-factorial prior over latent variables in the form of an unconstrained, pairwise interaction matrix, extending standard sparse coding inference to a general recurrent dynamical system. We efficiently train these recurrent dynamics using a denoising score-matching objective and implicit differentiation. After training on natural images, the learned interaction matrix mirrors the structure of horizontal connections in superficial layers of V1 that link neurons of similar orientation tuning. This model exhibits exceptionally good denoising performance, restoring image features such as extended contours amid extreme visual ambiguity, nearly matching the behavior of standard, black-box diffusion architectures in generalization regime. Owing to the model's simplicity, the network's Jacobian can be decomposed directly in terms of the interaction matrix between latent variables, revealing mechanistically how the recurrent dynamics assign high probability over a continuous family of natural structural deformations. Intriguingly, within this circuit, a large fraction of latent variables learn to disconnect from visual input altogether, essentially forming a hierarchical representation that appears to enforce global consistency among image features. Together, the model and results bridge two distinct domains: for neuroscience, it generates concrete, testable hypotheses regarding functional connectivity in recurrent neural circuits during perceptual inference tasks; for machine learning, it elucidates the internal mechanisms learned by diffusion models that allow them to generate infinitely many novel images from a finite training set.

## Core Contributions

1. Proposes a recurrent neural network model of V1 that is mathematically equivalent to a diffusion model, providing a mechanistic bridge between neuroscience and machine learning.
2. Shows that the learned interaction matrix in the model corresponds to the known horizontal connectivity patterns in V1, suggesting that the brain may implement inference similar to diffusion models.
3. Demonstrates that the model can achieve high denoising performance, matching state-of-the-art diffusion models, while being more interpretable.
4. Identifies that a subset of latent units become disconnected from visual input, forming a hierarchical representation that enforces global consistency in image features.

## Methodology

The authors define a linear generative model with a prior over latent variables that is a pairwise Markov random field (i.e., an energy function with quadratic terms). They show that the posterior inference in this model is equivalent to a recurrent neural network where the recurrent weights are given by the inverse covariance of the prior. They derive a learning rule based on denoising score matching and implicit differentiation to learn the prior from natural images. The learned weights are then compared to the known connectivity in V1.

## How to Use This Skill

This skill provides a framework for understanding how structured recurrent connections in neural circuits can implement probabilistic inference akin to diffusion models. Researchers can use this insight to:
- Interpret experimental data on V1 functional connectivity in terms of inference algorithms.
- Design new neural network architectures for vision tasks that incorporate structured recurrence inspired by biological circuits.
- Generate testable hypotheses about the role of lateral connections in perceptual inference and noise robustness.

## Activation Keywords

arxiv-260715693-mechanistic-inference-visual-cortex-diffusion, mechanistic inference, visual cortex, diffusion models, sparse coding, recurrent neural networks, neuroscience, machine learning
