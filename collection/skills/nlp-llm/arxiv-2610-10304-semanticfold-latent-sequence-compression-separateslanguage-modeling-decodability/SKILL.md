---
name: arxiv-2610-10304-semanticfold-latent-sequence-compression-separateslanguage-modeling-decodability
description: 'SemanticFold: Latent Sequence Compression SeparatesLanguage Modeling, Decodability, and Reasoning (arXiv: 2610.10304)'
metadata:
  {
    "arxiv_id": "2610.10304",
    "utility": 1.0,
    "title": "SemanticFold: Latent Sequence Compression SeparatesLanguage Modeling, Decodability, and Reasoning",
    "authors": "Mingyan Liu, Min Huang",
    "url": "https://arxiv.org/abs/2610.10304v1",
    "categories": ["cs.LG", "cs.AI", "cs.CL"],
    "published": "2026-10-07"
  }
---

# SemanticFold: Latent Sequence Compression SeparatesLanguage Modeling, Decodability, and Reasoning

**arXiv ID:** 2610.10304
**Authors:** Mingyan Liu, Min Huang
**URL:** https://arxiv.org/abs/2610.10304v1
**Utility Score:** 1.00
**Published:** 2026-10-07
**Categories:** cs.LG, cs.AI, cs.CL

## Summary

We study whether latent sequence compression of prompt prefixes preserves the capabilities that large language models rely on during inference. We introduce SemanticFold, a compression scheme that folds prefix hidden states at learned boundaries, and evaluate it across five model scales: Qwen3-1.7B, Qwen3-8B, SmolLM2-1.7B, Pythia-1.4B, and Pythia-6.9B. We use a fixed-target protocol: a frozen prefix is executed natively or compressed, and both arms teacher-force identical continuation tokens. This design rules out target-selection explanations for likelihood changes. We examine five endpoint families: fixed-target negative log-likelihood, finite-label reasoning accuracy, linear probe accessibility, open-ended generation, and systems-level memory and latency. We find that compression moves these endpoints non-monotonically and that they do not share a single compression threshold. On Qwen3-1.7B at compression ratio R=1.7, compressed-minus-native mean NLL decreases by 0.135 under paired bootstrap with 10000 draws. On SmolLM2 at R=1.2, the mean change is 0.013 higher than native. On both Pythia checkpoints, NLL is effectively unchanged. An NLL decomposition separating sequence shortening from the learned residual transform shows that the favorable Qwen likelihood is attributable primarily to residual adaptation rather than to shortening alone. MLP-only, which applies the transform without shortening, achieves 0.082 lower NLL than Full SemanticFold. Linear probe accuracy and macro AUC change by less than 0.03 in absolute value across conditions, with confidence intervals crossing zero. We conclude that preservation under latent compression has no single scalar certificate: language-model fit, decodability, and reasoning behavior answer different questions and can move in different directions under the same compression operation.

## Usage

This skill was automatically generated from the arXiv paper. It can be used to reference the paper's concepts, methodologies, or findings in agent workflows.

## References

- arXiv: https://arxiv.org/abs/2610.10304v1
