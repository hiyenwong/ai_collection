---
name: the-structure-gap-when-more-data
description: "Research paper: The Structure Gap: When More Data Cannot Replace Structured Reasoning"
tags: [arxiv, paper, cs.LG, cs.AI]
arxiv_id: "2610.37523"
utility: 0.86
---

# The Structure Gap: When More Data Cannot Replace Structured Reasoning

**arXiv:** [2610.37523](https://arxiv.org/abs/2610.37523)
**Authors:** Kheer Sagar Patel, Mojtaba Soltanalian
**Published:** 2026-10-27
**Categories:** cs.LG, cs.AI
**Utility Score:** 0.86

## Abstract

A persistent belief in modern AI is that sufficiently large learners trained on sufficiently much data can make explicit domain knowledge optional. This paper examines a limitation of that belief. We define structure-encoded problems: tasks whose input-output map is determined, or sharply constrained, by known structure such as a solver, symmetry group, graph, physical law, measurement operator, grammar, combinatorial search space, or optimization objective. For such tasks, the central question is not expressivity--a dense neural network may contain the desired map--but finite-data identification, extrapolation, and certification. We introduce the structure gap: the finite-resource gap between a method that receives the governing structure and a learner that receives only examples. The strongest useful form of the claim is asymptotic rather than absolute: structure-agnostic learning may approach a structured solver as coverage grows, but every finite dataset can leave residual uncertainty that the structure resolves by construction. We prove this exactly for a Gaussian inverse problem: the known-operator Wiener solver attains Bayes risk, while the dense empirical learner in the correct linear class has persistent expected excess risk. We also prove a cell-coverage lower bound and an unobserved-orbit non-identifiability result. Controlled experiments in known-operator inversion, sparse recovery, and graph reachability with size extrapolation instantiate the mechanisms. When va

## Key Contributions

- Paper identified as high-utility (≥0.85) from arXiv scan
- Relevant to: cs.LG, cs.AI

## Potential Applications

- Research reference for neuroscience domain
- Building block for future work in this area
