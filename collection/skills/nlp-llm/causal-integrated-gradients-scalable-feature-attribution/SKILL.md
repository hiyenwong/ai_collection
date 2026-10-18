---
name: causal-integrated-gradients-scalable-feature-attribution
description: "Causal Integrated Gradients: Scalable Feature Attr..."
tags: [cs.LG, cs.AI]
source: arxiv
arxiv_id: 2610.22126v1
utility: 0.85
published: 2026-10-15
---

# Causal Integrated Gradients: Scalable Feature Attribution Along Causal Paths

**Authors:** Joran Michiels, Anis Ismail, Maarten De Vos, Alejandro Sifrim
**Published:** 2026-10-15
**arXiv:** [2610.22126v1](https://arxiv.org/abs/2610.22126v1)
**Categories:** cs.LG, cs.AI
**Utility Score:** 0.85

## Abstract

Existing feature attribution methods that account for feature dependencies do not scale to high dimensions. We propose causal integrated gradients (CIG) and causal expected gradients (CEG), which extend integrated gradients to incorporate prior causal structure among input features while retaining its computational efficiency and, under conditions on the causal graph, its axiomatic guarantees. In many settings, some causal structure between features is already known, for example, that a transcription factor causally regulates a target gene's expression. Yet existing gradient-based methods cannot exploit this structure, instead crediting a feature's downstream effects over its true upstream cause, such as ranking the target gene above the transcription factor that regulates it. Our key idea is to embed this causal structure by routing the integration path along the causal graph. The method thereby decomposes each feature's attribution into a direct effect and effects mediated through its causal descendants. We evaluate CIG in three settings of increasing realism. First, on a synthetic benchmark with a known causal model, CIG's attributions best match the ground-truth causal effect from Pearl's do-calculus, matching the accuracy of causal Shapley values at a fraction of the computational cost. Second, on simulated single-cell gene expression data with a known gene regulatory network (Dyngen), CIG most accurately recovers the transcription factors driving the simulation. Third, 

## Key Contributions

- Novel research in cs.LG, cs.AI
- Published 2026-10-15

## Activation

causal, integrated, gradients, scalable, feature, attribution, along, causal, paths
