---
name: designing-transformers-for-continuous-diffusion-language
description: "Designing Transformers for Continuous Diffusion La..."
tags: [cs.AI]
source: arxiv
arxiv_id: 2610.22330v1
utility: 0.85
published: 2026-10-15
---

# Designing Transformers for Continuous Diffusion Language Models

**Authors:** Weijian Luo, Yujian Chen, Hao Jiang, Guang Cheng, Tianyang Hu
**Published:** 2026-10-15
**arXiv:** [2610.22330v1](https://arxiv.org/abs/2610.22330v1)
**Categories:** cs.AI
**Utility Score:** 0.85

## Abstract

Continuous diffusion language models (CDLMs) offer an alternative approach to parallel language generation; however, most existing studies directly use transformer architectures from either causal large language models (LLMs) or Diffusion Transformers (DiTs) for image generation, which were not optimized for CDLMs. In this paper, we conduct a systematic study on Transformer architectures for CDLMs and introduce Language Diffusion Transformer (LangDiT), combining feature and query-key normalization, wider noise conditioning, likelihood-shortcut gradient routing and calibration, and confidence-gated training self-conditioning. LangDiT significantly reduces generation perplexity in matched LangFlow comparisons, establishing a new state of the art in continuous language generation across different model formulations. Using LangFlow as a representative CDLM, LangDiT as a plug-and-play backbone leads to a new state-of-the-art model with a generation perplexity (GenPPL) of 21.72 using 1024 NFEs and 44.72 GenPPL using 128 NFEs on the unconditional generation of 1024-token sequences on the OpenWebText dataset. When adapted to Plaid-style CDLM formulations, LangDiT results in a new leading GenPPL of 11.33 using 1024 denoising NFEs, and 27.51 GenPPL using 128 denoising NFEs. These gains are achieved while retaining each model's underlying representation, training objective, and inference sampler, isolating transformer architecture as a fundamental source of improvement. Our study identi

## Key Contributions

- Novel research in cs.AI
- Published 2026-10-15

## Activation

designing, transformers, continuous, diffusion, language, models
