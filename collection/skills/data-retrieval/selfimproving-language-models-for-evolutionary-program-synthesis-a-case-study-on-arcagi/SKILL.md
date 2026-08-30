# Self-Improving Language Models for Evolutionary Program Synthesis: A Case Study on ARC-AGI

**arXiv ID:** 2507.14172
**Authors:** Julien Pourcel, Cédric Colas, Pierre-Yves Oudeyer
**Published:** 2025-07-10T15:42:03Z
**Abstract:**
Many program synthesis tasks prove too challenging for even state-of-the-art language models to solve in single attempts. Search-based evolutionary methods offer a promising alternative by exploring solution spaces iteratively, but their effectiveness remain limited by the fixed capabilities of the underlying generative model.
  We propose SOAR, a method that learns program synthesis by integrating language models into a self-improving evolutionary loop.
  SOAR alternates between (1) an evolutionary search that uses an LLM to sample and refine candidate solutions, and (2) a hindsight learning phase that converts search attempts into valid problem-solution pairs used to fine-tune the LLM's sampling and refinement capabilities\, -- \,enabling increasingly effective search in subsequent iterations.
  On the challenging ARC-AGI benchmark, SOAR achieves significant performance gains across model scales and iterations, leveraging positive transfer between the sampling and refinement finetuning tasks. These improvements carry over to test-time adaptation, enabling SOAR to solve 52\% of the public test set. Our code is open-sourced at: https://github.com/flowersteam/SOAR

## Skill Description

This skill is generated from the arXiv paper: Self-Improving Language Models for Evolutionary Program Synthesis: A Case Study on ARC-AGI (2507.14172).

## How to Use

[To be filled in by the user or by future automation]

## References

- [arXiv:2507.14172](http://arxiv.org/abs/2507.14172v2)
