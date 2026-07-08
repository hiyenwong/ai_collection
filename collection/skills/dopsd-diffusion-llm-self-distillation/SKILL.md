---
name: dopsd-diffusion-llm-self-distillation
category: ai_collection
description: "dOPSD methodology for on-policy self-distillation in diffusion language models. Derives teacher privilege from student's own denoising trajectory rather than external labels, enabling reasoning improvement without tractable sequence likelihoods."
tags: [diffusion-language-model, on-policy-self-distillation, masked-denoising, reasoning-improvement, Dream, LLaDA]
---

# dOPSD: On-Policy Self-Distillation for Diffusion Language Models

## Core Problem

Diffusion LLMs (dLLMs) generate text by iterative denoising of masked sequences. Post-training is difficult because:
- SFT is off-policy → exposure bias
- RL gives sparse sequence-level rewards and needs tractable sequence likelihoods
- On-policy self-distillation (OPSD) needs privileged information (PI), typically ground-truth references unavailable at inference
- Without PI, student distills a weak PI-free consensus policy → little improvement

## Methodology

**dOPSD** derives teacher privilege from the student's OWN denoising trajectory:
1. Evaluate masked positions using LATER, more-decoded steps of the same trajectory
2. Teacher advantage emerges from the model's own decoding process (no external label needed)
3. One model acts as both student and teacher
4. Dense, token-level, on-policy supervision

## Key Innovation

Instead of requiring external ground-truth as privileged information, dOPSD uses temporal progression within a single denoising trajectory — later steps are naturally "more correct" than earlier steps, providing the teacher advantage for free.

## Results

- Improves both in-domain math reasoning AND out-of-domain code generation
- Outperforms supervised and on-policy baselines on Dream and LLaDA models
- No need for tractable sequence likelihoods

## When to Use

- Post-training diffusion/masked denoising language models
- When RL is infeasible due to lack of tractable likelihoods
- When SFT exposure bias is limiting performance
- For reasoning tasks (math, code) in non-autoregressive architectures

## Pitfalls

- Requires the denoising trajectory to have meaningful temporal progression
- May not work if early and late decoding steps are equally noisy
- Specific to diffusion/masked architectures, not autoregressive models

## Reference

arXiv:2607.04428 - "dOPSD: On-Policy Self-Distillation for Diffusion Language Models" (Dat et al., 2026)

## Activation

dOPSD, diffusion language model, diffusion LLM, on-policy self-distillation, Dream model, LLaDA, masked denoising LM, diffusion reasoning, exposure bias diffusion LM
