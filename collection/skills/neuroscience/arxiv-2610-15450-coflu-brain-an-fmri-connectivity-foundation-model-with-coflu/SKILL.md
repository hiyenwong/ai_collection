---
name: arxiv-2610-15450-coflu-brain-an-fmri-connectivity-foundation-model-with-coflu
description: 'CoFlu-Brain: An fMRI Connectivity Foundation Model with Cofluctuation-Based Pret (arXiv: 2610.15450)'
metadata:
  {
    "arxiv_id": "2610.15450",
    "utility": 0.86,
    "title": "CoFlu-Brain: An fMRI Connectivity Foundation Model with Cofluctuation-Based Pretraining",
    "authors": "",
    "url": "https://arxiv.org/abs/2610.15450"
  }
---

# CoFlu-Brain: An fMRI Connectivity Foundation Model with Cofluctuation-Based Pretraining

**arXiv ID:** 2610.15450
**URL:** https://arxiv.org/abs/2610.15450
**Utility Score:** 0.86

## Abstract

Functional magnetic resonance imaging (fMRI) commonly characterizes large-scale brain organization through functional connectivity (FC). However, an observed FC matrix is not a fixed brain graph but a statistical estimate determined by the finite BOLD frames used to compute it. Conventional FC-based approaches typically represent each scan with a single Pearson-correlation matrix, leaving frame-resolved variations in regional interactions unexploited. To address this limitation, we introduce CoFlu-Brain, which organizes framewise cofluctuation observations into multiple retained and dropped views, each summarized as an FC matrix. The model learns connectivity structure reproducible across retained views and predicts the representations of the corresponding dropped views, while adopting SIGReg from LeJEPA to prevent representation collapse. We pretrained CoFlu-Brain on 13,444 subjects from eight dataset groups and evaluated its representations via frozen-encoder linear probing on seven classification and two age-prediction tasks across seven datasets. CoFlu-Brain showed strong transfer across demographic, developmental, and clinical prediction tasks, outperforming the evaluated released models on most tasks. Random frame partitioning improved aggregate transfer, while the complete objective achieved the strongest overall performance. Code is available.

## Key Topics

brain, fmri, foundation model, pretrain

## Usage

This skill references the paper's concepts, methodologies, and findings for use in agent workflows.

## References

- arXiv: https://arxiv.org/abs/2610.15450
