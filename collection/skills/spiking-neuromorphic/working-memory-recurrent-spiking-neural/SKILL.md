---
name: working-memory-recurrent-spiking-neural
description: "Working memory -- the ability to store and recall precise temporal patterns of neural activity -- remains an open challenge for spiking neural networks (SNNs). We propose a recurre..."
---

# Working Memory in a Recurrent Spiking Neural Networks With Heterogeneous Synaptic Delays

## Overview
Working memory -- the ability to store and recall precise temporal patterns of neural activity -- remains an open challenge for spiking neural networks (SNNs). We propose a recurrent SNN of $N$ neurons in which each synapse is equipped with $D = 41$ delays, modelled as a weight tensor $\mathbf{W} \in \mathbb{R}^{N \times N \times D}$ and trained end-to-end with surrogate-gradient backpropagation through time. The network stores $M$ arbitrary target spike patterns by representing each as a sequential chain of overlapping Spiking Motifs: contiguous windows of length $D$ that uniquely predict spikes at the next time step. On a synthetic benchmark of $M=16$ patterns ($N=512$ neurons, $T=1000$ steps), training achieves a mean F1 score of $1.0$, with recall emerging first near the clamped initialisation window and propagating forward in time. This result demonstrates that heterogeneous delays provide an efficient substrate for working memory in SNNs, enabling energy-efficient neuromorphic edge deployment.

## Source
- **arXiv:** 2604.14096v1
- **Date:** 2026-04-15
- **Authors:** Laurent U Perrinet
- **Categories:** q-bio.NC

## Methods
- Spiking Neural Networks
- Network Analysis
- Working Memory

## Applications
- Brain data analysis and neural modeling
- Neuroscience research and development

## References
Laurent U Perrinet et al. arXiv:2604.14096v1

## Keywords
- neuroscience
- q-bio.NC


## Latest Paper Reference (Updated: 2026-04-18)

- **Title:** Working Memory in a Recurrent Spiking Neural Networks With Heterogeneous Synaptic Delays
- **Authors:** Laurent U Perrinet et al.
- **arXiv:** 2604.14096v1
- **Published:** 2026-04-15
- **PDF:** https://arxiv.org/pdf/2604.14096v1