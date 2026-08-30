# An Interpretable Automated Mechanism Design Framework with Large Language Models

**arXiv ID:** 2502.12203
**Authors:** Jiayuan Liu, Mingyu Guo, Vincent Conitzer
**Published:** 2025-02-16T12:33:03Z
**Abstract:**
Mechanism design has long been a cornerstone of economic theory, with traditional approaches relying on mathematical derivations. Recently, automated approaches, including differentiable economics with neural networks, have emerged for designing payments and allocations. While both analytical and automated methods have advanced the field, they each face significant weaknesses: mathematical derivations are not automated and often struggle to scale to complex problems, while automated and especially neural-network-based approaches suffer from limited interpretability. To address these challenges, we introduce a novel framework that reformulates mechanism design as a code generation task. Using large language models (LLMs), we generate heuristic mechanisms described in code and evolve them to optimize over some evaluation metrics while ensuring key design criteria (e.g., strategy-proofness) through a problem-specific fixing process. This fixing process ensures any mechanism violating the design criteria is adjusted to satisfy them, albeit with some trade-offs in performance metrics. These trade-offs are factored in during the LLM-based evolution process. The code generation capabilities of LLMs enable the discovery of novel and interpretable solutions, bridging the symbolic logic of mechanism design and the generative power of modern AI. Through rigorous experimentation, we demonstrate that LLM-generated mechanisms achieve competitive performance while offering greater interpretability compared to previous approaches. Notably, our framework can rediscover existing manually designed mechanisms and provide insights into neural-network based solutions through Programming-by-Example. These results highlight the potential of LLMs to not only automate but also enhance the transparency and scalability of mechanism design, ensuring safe deployment of the mechanisms in society.

## Skill Description

This skill is generated from the arXiv paper: An Interpretable Automated Mechanism Design Framework with Large Language Models (2502.12203).

## How to Use

[To be filled in by the user or by future automation]

## References

- [arXiv:2502.12203](http://arxiv.org/abs/2502.12203v1)
