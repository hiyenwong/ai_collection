---
name: when-visual-evidence-is-insufficient-how
description: "Research paper: When Visual Evidence Is Insufficient: How Instructions, Post-Training, and Inter"
tags: [arxiv, paper, cs.LG, cs.CV]
arxiv_id: "2610.37430"
utility: 0.87
---

# When Visual Evidence Is Insufficient: How Instructions, Post-Training, and Internal Activations Shape Refusal in Multimodal Language Models

**arXiv:** [2610.37430](https://arxiv.org/abs/2610.37430)
**Authors:** Ananth K Suresh, Aveen Dayal, Gouthaman KV, Aditya Pola, Vineeth N Balasubramanian
**Published:** 2026-10-27
**Categories:** cs.LG, cs.CV
**Utility Score:** 0.87

## Abstract

For reliable deployment, multimodal large language models (MLLMs) should recognize when an image provides insufficient evidence to answer a question and withhold unsupported answers. Yet refusal alone is not necessarily evidence of such recognition: models may refuse because of unrelated safety constraints or without identifying the missing evidence. We study how refusal on visually unanswerable questions is shaped by three sources of control: inference-time instructions, post-training, and internal activation interventions. Across three MLLMs on the MoHoBench benchmark, we systematically manipulate the meaning and placement of refusal instructions, compare supervised and preference-based post-training, and intervene on a refusal-related activation direction derived from naturally answered and refused examples. We find that refusal is highly sensitive to both the meaning and placement of instructions, with model-specific changes at the sample level that are obscured by aggregate refusal rates. Evidence-aware and general refusal instructions have stronger effects than an intentionally mismatched safety instruction. Post-training produces larger increases in refusal, but can also induce responses that combine refusal language with attempted answers. In contrast, activation intervention produces smaller yet transferable changes across prompt conditions, without evidence of indiscriminate refusal on tested visually answerable samples. These findings show that refusal is jointly s

## Key Contributions

- Paper identified as high-utility (≥0.85) from arXiv scan
- Relevant to: cs.LG, cs.CV

## Potential Applications

- Research reference for ai safety eval domain
- Building block for future work in this area
