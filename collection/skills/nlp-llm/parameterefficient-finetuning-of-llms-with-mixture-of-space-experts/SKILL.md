# Parameter-Efficient Fine-Tuning of LLMs with Mixture of Space Experts

**arXiv ID:** 2602.14490
**Authors:** Buze Zhang, Jinkai Tao, Zilang Zeng, Neil He, Ali Maatouk, Menglin Yang, Rex Ying
**Published:** 2026-02-16T06:07:32Z
**Abstract:**
Large Language Models (LLMs) have achieved remarkable progress, with Parameter-Efficient Fine-Tuning (PEFT) emerging as a key technique for downstream task adaptation. However, existing PEFT methods mainly operate in Euclidean space, fundamentally limiting their capacity to capture complex geometric structures inherent in language data. While alternative geometric spaces, like hyperbolic geometries for hierarchical data and spherical manifolds for circular patterns, offer theoretical advantages, forcing representations into a single manifold type ultimately limits expressiveness, even when curvature parameters are learnable. To address this, we propose Mixture of Space (MoS), a unified framework that leverages multiple geometric spaces simultaneously to learn richer, curvature-aware representations. Building on this scheme, we develop MoSLoRA, which extends Low-Rank Adaptation (LoRA) with heterogeneous geometric experts, enabling models to dynamically select or combine appropriate geometric spaces based on input context. Furthermore, to address the computational overhead of frequent manifold switching, we develop a lightweight routing mechanism. Moreover, we provide empirical insights into how curvature optimization impacts training stability and model performance. Our experiments across diverse benchmarks demonstrate that MoSLoRA consistently outperforms strong baselines, achieving up to 5.6% improvement on MATH500 and 15.9% on MAWPS.

## Skill Description

This skill is generated from the arXiv paper: Parameter-Efficient Fine-Tuning of LLMs with Mixture of Space Experts (2602.14490).

## How to Use

[To be filled in by the user or by future automation]

## References

- [arXiv:2602.14490](http://arxiv.org/abs/2602.14490v1)
