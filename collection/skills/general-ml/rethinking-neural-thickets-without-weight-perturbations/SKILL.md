---
name: rethinking-neural-thickets-without-weight-perturbations
description: "Rethinking Neural Thickets Without Weight Perturba..."
tags: [cs.LG, cs.AI, cs.CV]
source: arxiv
arxiv_id: 2610.40649v1
utility: 0.85
published: 2026-10-29
---

# Rethinking Neural Thickets Without Weight Perturbations

**Authors:** Nicolas Dufour, Elouan Gardès, Amil Dravid, Patrick Pérez, Loic Landrieu
**Published:** 2026-10-29
**arXiv:** [2610.40649v1](https://arxiv.org/abs/2610.40649v1)
**Categories:** cs.LG, cs.AI, cs.CV
**Utility Score:** 0.85

## Abstract

The Neural Thickets hypothesis posits that pretrained language models lie in dense neighborhoods of task-specific experts in weight space, which random Gaussian perturbations can uncover. We reproduce the reported gains, but show that they do not require this geometric explanation. Perturbing a single decoder block already recovers much of the improvement, while keeping the model entirely frozen and adding a random bias to its output logits matches or exceeds full-weight perturbations on most reasoning tasks. This suggests an alternative explanation based on output diversity, validation-based selection, and voting. We formalize this view as Perturb-Select-Vote (PSV), a general procedure that generates perturbed predictors, selects high-performing members on a small validation set, and aggregates their predictions. This interpretation connects Neural Thickets to established inference-time methods, including sampling, self-consistency, and verifier-guided selection. A first-order analysis further shows that small weight perturbations act primarily through their induced logit shifts. We extend this analysis to vision, where logit PSV substantially improves performance under domain shift, including on Earth observation, while full-weight perturbations provide little additional benefit. Together, these results suggest that the gains attributed to nearby weight-space experts can instead be obtained through output diversity, selection, and voting. Logit PSV realizes these benefits w

## Key Contributions

- Novel research in cs.LG, cs.AI
- Published 2026-10-29

## Activation

rethinking, neural, thickets, without, weight, perturbations
