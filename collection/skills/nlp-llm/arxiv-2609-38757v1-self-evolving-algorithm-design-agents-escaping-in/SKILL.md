---
name: arxiv-2609-38757v1-self-evolving-algorithm-design-agents-escaping-in
description: "arXiv paper: Self-Evolving Algorithm-Design Agents: Escaping In-Context Evolutionary Stagnation via Population-Curated Policy Optimization"
tags: [arxiv, cs.AI, research]
created: 2026-10-04
utility: 1.0
---

# Self-Evolving Algorithm-Design Agents: Escaping In-Context Evolutionary Stagnation via Population-Curated Policy Optimization

**arXiv ID:** 2609.38757v1
**Authors:** Chen Lu, Ke Xue, Siyuan Xu et al.
**Published:** 2026-09-30
**Category:** cs.AI
**Utility Score:** 1.0
**URL:** https://arxiv.org/abs/2609.38757v1

## Abstract

Large language models are increasingly participating in complex real-world tasks in the form of algorithm-design agents, designing and refining algorithms. Many successful algorithm-design agents adopt pure in-context evolutionary frameworks, but they may quickly plateau in domains that require specialized knowledge. Parametric adaptation offers a way to internalize specialized knowledge, but conventional training requires abundant domain-specific corpora while high-quality algorithms are scarce in complex algorithm-design scenarios. In this paper, we propose sample-efficient parametric self-evolution where agents can explore and learn from self-generated algorithms. First, we characterize in-context evolutionary stagnation and analytically propose the Improvement Chain proposition, showing how learning successive self-generated algorithms can locally increase the likelihood of neighboring algorithms. Motivated by this local-transfer perspective, we further propose Population-Curated Policy Optimization (PCPO) to utilize a global population and a hybrid policy update scheme for retaining and reusing high-quality, diverse self-generated algorithms, shifting the policy towards stronger algorithms. In the task of learning rate schedule design for global placement in electronic design automation, trained only on 4 chip cases, PCPO outperforms the state-of-the-art in-context evolutionary methods (e.g., OpenEvolve and ShinkaEvolve) on average across 16 chip cases. With an 8B-size base model, PCPO achieves competitive performance compared to frontier closed-source models such as GPT-5.5. PCPO also reduces inference-time token cost by internalizing grounded domain knowledge and prompt distillation. Moreover, PCPO achieves significant speedups on four GPU kernel designs, with an average of 8.27$\times$ speedup against the PyTorch Eager baseline.

## Key Contributions

- Novel research in cs.AI
- Published on arXiv: 2026-09-30

## Related Work

See arXiv for citations and references.
