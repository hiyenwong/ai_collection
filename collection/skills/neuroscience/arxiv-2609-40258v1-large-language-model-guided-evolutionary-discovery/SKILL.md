---
name: arxiv-2609-40258v1-large-language-model-guided-evolutionary-discovery
description: "arXiv paper: Large Language Model-Guided Evolutionary Discovery of Native Neural Architectures for Spiking Sequence Modeling"
tags: [arxiv, cs.NE, research]
created: 2026-10-04
utility: 0.87
---

# Large Language Model-Guided Evolutionary Discovery of Native Neural Architectures for Spiking Sequence Modeling

**arXiv ID:** 2609.40258v1
**Authors:** Ruoyu Zhao, Jiaqi Wu, Chenyu Zhu et al.
**Published:** 2026-09-30
**Category:** cs.NE
**Utility Score:** 0.87
**URL:** https://arxiv.org/abs/2609.40258v1

## Abstract

Spiking neural networks (SNNs) offer low-energy sequence modeling through sparse, event-driven computation. However, interactions among spike encoding, neuronal dynamics, and information propagation complicate architecture design. Existing SNN sequence models often adapt artificial neural network (ANN) architectures designed for real-valued activations, potentially underusing spike-based communication and temporal state updates, motivating automated discovery of native SNN architectures. Most evolutionary neural architecture search (ENAS) methods operate within predefined configuration spaces, limiting discovery to mechanisms expressible within those spaces. We introduce OpenArchEvo, which uses large language models (LLMs) to evolve executable architecture code in an open program space under spiking-projection constraints. In this space, code differences need not reflect architectural novelty, while direct performance evaluation requires costly training. We construct a three-view representation spanning code, design rationale, and a behavioral fingerprint to support novelty estimation and performance prediction. The search treats predicted performance and estimated novelty as two objectives, using surrogate predictions to select candidates for expensive training evaluations. With an estimated candidate-training cost of 132 V100 GPU-days, the search uncovers multiple native SNN architectures, exemplified by three designs featuring mechanisms such as spike-activity-dependent control of state updates and residual pathways. The discovered NeuroGate surpasses the ANN DeltaNet on WikiText-103, and the discovered architectures reduce estimated architecture-level arithmetic energy by up to 50.6x (LoopMem) relative to a common dense Transformer (ANN) baseline. All code and all discovered architectures will be made publicly available soon.

## Key Contributions

- Novel research in cs.NE
- Published on arXiv: 2026-09-30

## Related Work

See arXiv for citations and references.
