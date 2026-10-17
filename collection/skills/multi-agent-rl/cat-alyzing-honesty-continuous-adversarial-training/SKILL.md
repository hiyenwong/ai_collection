---
name: cat-alyzing-honesty-continuous-adversarial-training
description: "CAT-alyzing Honesty: Continuous Adversarial Training for Transferable LLM Honest"
tags: [arxiv, paper, multi-agent-rl]
arxiv_id: "2610.22292"
utility: 0.99
date: "2026-10-17"
---

# CAT-alyzing Honesty: Continuous Adversarial Training for Transferable LLM Honesty

**arXiv:** [2610.22292](https://arxiv.org/abs/2610.22292)
**Authors:** Yuan-Chen Chang, Niklas Herbster, Gauthier Gidel, Tommaso Tosato
**Published:** 2026-10-15
**Categories:** cs.LG, cs.CL, cs.CY
**Utility Score:** 0.99

## Abstract

Large language models (LLMs) are becoming prevalent in scenarios where honesty is critical. However, despite alignment training, these models still exhibit dishonest behaviour, such as outputting claims that contradict some knowledge or are not supported by what is accessible in context. We introduce Continuous Adversarial Training for Consistent Honesty (CATCH), inspired by a method originally developed to robustly refuse harmful queries. CATCH trains the model towards an honest answer and away from a dishonest one while maintaining the model's capabilities. We evaluate two architectures (Llama-3.3-70B-Instruct and Qwen3-3.6-27B). We show that trained with only hundreds of targets built from self-reporting scenarios, CATCH learns an honest behaviour that robustly generalizes and transfers across distinct benchmarks. It consistently reduces dishonesty under pressure on MASK, increases confessions in the multi-agent game of Among Us, and improves the discovery rates of the model's hidden behaviours in AuditBench. We show that CATCH outperforms prompting and supervised fine-tuning in improving honesty, and it is on par with state-of-the-art honesty activation steering. However, CATCH surpasses honesty steering in maintaining utility, thanks to a novel choice of utility data.

## Key Contributions

- Novel research in cs.LG, cs.CL
- High utility score (0.99) indicating significant research value

## Activation

catalyzing, honesty, continuous, adversarial, training, transferable, honesty

## Notes

Added by arXiv cron job on 2026-10-17.
