---
name: routerinterp-moe-specialisation
description: "RouterInterp: Superposed Specialisation Hypothesis for MoE models. Experts specialise in disjoint union of fine-grained features rather than one broad domain. ~65% higher detection accuracy than prior methods."
tags: [mixture-of-experts, interpretability, routing, superposition, sparse-autoencoders, feature-analysis]
source: "arXiv:2610.11775"
utility_score: 0.87
---

# RouterInterp: Understanding Superposed Specialisation in Mixture of Experts Routing

## Paper Metadata

- **arXiv ID**: 2610.11775
- **Title**: RouterInterp: Understanding Superposed Specialisation in Mixture of Experts Routing
- **Authors**: Ilya Lasy, Nora Yinuo Cai, Kola Ayonrinde, et al.
- **Published**: 2026-10-08
- **Categories**: cs.AI, cs.CL, cs.LG
- **Link**: https://arxiv.org/abs/2610.11775
- **Venue**: ICML 2026 (conference paper)

## Abstract Summary

Sparse Mixture of Experts (MoE) models scale more efficiently than dense models by routing tokens to modular expert networks that are only active for processing a fraction of tokens. A leading hypothesis for the performance of MoE models is that each expert specialises in a single, coherent domain. However, interpretability efforts that assume this hypothesis have generally been unsuccessful. This work proposes the Superposed Specialisation Hypothesis (SSH): experts specialise in a disjoint union of fine-grained features rather than one broad domain. Leveraging the SSH, RouterInterp identifies Sparse Autoencoder features most predictive of routing decisions and produces unified natural language explanations. On gpt-oss-20b, RouterInterp explains expert routing with ~65% higher detection accuracy than prior token statistics based methods.

## Key Contributions

1. **Superposed Specialisation Hypothesis (SSH)**: Experts specialise in disjoint union of fine-grained features, not one broad domain
2. **RouterInterp method**: Identifies SAE features most predictive of routing decisions
3. **Natural language explanations**: Produces unified explanations for expert routing
4. **Empirical validation**: ~65% higher detection accuracy than prior methods on gpt-oss-20b
5. **Scalable interpretability**: Provides method for understanding previously uninterpretable MoE components

## Research Implications

- **MoE understanding**: Resolves why prior interpretability efforts assuming domain-specialisation failed
- **Superposition evidence**: Supports superposition hypothesis in expert routing
- **Model transparency**: Enables understanding of which features activate which experts
- **Debugging tools**: Helps identify routing failures and expert underutilization
- **Design guidance**: Informs future MoE architectures based on actual specialisation patterns

## Practical Applications

- Interpret expert routing decisions in deployed MoE models
- Debug routing failures and identify underutilized experts
- Guide MoE model design and training
- Create visualizations of expert specialisation patterns
- Develop tools for monitoring expert usage in production

## Related Work

- Sparse autoencoders
- Mechanistic interpretability
- Mixture of Experts architectures
- Feature superposition
- Neural network interpretability
