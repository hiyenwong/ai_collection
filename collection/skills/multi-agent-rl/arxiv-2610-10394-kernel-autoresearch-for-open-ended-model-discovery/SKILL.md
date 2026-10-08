---
name: arxiv-2610-10394-kernel-autoresearch-for-open-ended-model-discovery
description: 'Kernel Autoresearch for Open-Ended Model Discovery (arXiv: 2610.10394)'
metadata:
  {
    "arxiv_id": "2610.10394",
    "utility": 0.98,
    "title": "Kernel Autoresearch for Open-Ended Model Discovery",
    "authors": "Richard Cornelius Suwandi, Feng Yin, Kevin Murphy",
    "url": "https://arxiv.org/abs/2610.10394v1",
    "categories": ["cs.LG"],
    "published": "2026-10-07"
  }
---

# Kernel Autoresearch for Open-Ended Model Discovery

**arXiv ID:** 2610.10394
**Authors:** Richard Cornelius Suwandi, Feng Yin, Kevin Murphy
**URL:** https://arxiv.org/abs/2610.10394v1
**Utility Score:** 0.98
**Published:** 2026-10-07
**Categories:** cs.LG

## Summary

Kernels encode the inductive bias of a wide range of machine learning models, yet automated kernel design faces a fundamental dilemma. A fixed grammar of base kernels and operators guarantees validity but limits the search to structures expressible by those building blocks. Conversely, unrestricted programs remove this limitation but no longer guarantee validity. In our stress tests, 22-58% of LLM-generated kernels that pass numerical checks on random inputs fail when evaluated at different scales or dimensions. We propose Kernel Autoresearch (Kernaut), which treats kernel design as open-ended model discovery. Coding agents write kernels as programs, while construction contracts ensure that every accepted kernel is valid. A quality-diversity archive retains high-performing kernels with distinct behaviors, and novelty screening steers agents toward functionally new candidates. Our experiments demonstrate that the discovered kernels encode reusable inductive biases that generalize to unseen tasks. On held-out black-box optimization families, a discovered kernel outperforms a meta-learned deep kernel trained on the same episodes. Furthermore, kernels discovered from ten enzyme-kinetic rate laws achieve lower error than tuned ARD and deep kernel baselines on five unseen mechanisms. The discovered kernels are also interpretable programs that human researchers can refine: a human-refined version of one further reduces the held-out predictive error by 5.7% and optimization regret by 7.8%.

## Usage

This skill was automatically generated from the arXiv paper. It can be used to reference the paper's concepts, methodologies, or findings in agent workflows.

## References

- arXiv: https://arxiv.org/abs/2610.10394v1
