---
name: arxiv-2609-38081v1-traversing-the-solution-space-of-neural-networks-w
description: "arXiv paper: Traversing the solution space of neural networks with Hessian Null Space Continuation"
tags: [arxiv, cs.LG, research]
created: 2026-10-04
utility: 1.0
---

# Traversing the solution space of neural networks with Hessian Null Space Continuation

**arXiv ID:** 2609.38081v1
**Authors:** Ann Huang, Mitchell Ostrow, Zhouyang Lu et al.
**Published:** 2026-09-29
**Category:** cs.LG
**Utility Score:** 1.0
**URL:** https://arxiv.org/abs/2609.38081v1

## Abstract

On a single task, deep networks can learn many solutions, depending on their optimizer, training data, architecture, and hyperparameters. Many of these solutions are mode-connected: rather than isolated points in weight space, they are connected by low-loss regions. Yet how their internal computation varies within these regions is unknown. A parallel line of work has identified the degeneracy of neural representations: many networks reach similar training loss with distinct internal structures. However, it is unclear how these solutions are related in weight space. We unify these subfields and show for the first time that many different internal mechanisms exist within a local mode-connected region in weight space. To do so, we introduce Hessian Null Space Continuation (HNC), a scalable method that uses local curvature to traverse regions of weight space that preserve network function, and can be steered toward solutions with specified properties. In RNNs trained on a memory task, HNC reaches drastically different representations and dynamics with maintained behavior. In ImageNet-trained Vision Transformers, HNC finds representations that differ more from the original network than any independently trained model with a different architecture or objective. In reinforcement-learning agents, HNC uncovers a distinct navigation strategy at comparable return and exposes reward hacking in an AI Safety Gridworld. Finally, HNC measures the local geometry of the solution set, showing how model size and task complexity shape its dimension and functional sensitivity. Our results show that a surprisingly large amount of representational diversity exists near a single trained solution, unseen by standard gradient-based optimization. HNC identifies and quantifies this diversity, opening new possibilities for mechanistic understanding of solution spaces and for model merging, editing, and fine-tuning.

## Key Contributions

- Novel research in cs.LG
- Published on arXiv: 2026-09-29

## Related Work

See arXiv for citations and references.
