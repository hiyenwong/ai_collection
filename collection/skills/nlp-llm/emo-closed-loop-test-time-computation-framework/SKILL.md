---
name: emo-closed-loop-test-time-computation-framework
description: "EMO: A Closed-Loop Test-Time Computation Framework via Alternating Context Optim"
tags: [arxiv, paper, nlp-llm]
arxiv_id: "2610.22160"
utility: 0.9
date: "2026-10-17"
---

# EMO: A Closed-Loop Test-Time Computation Framework via Alternating Context Optimization and Logits Steering

**arXiv:** [2610.22160](https://arxiv.org/abs/2610.22160)
**Authors:** Wei Xia, Yehui Tang, Zhi-Hong Deng
**Published:** 2026-10-15
**Categories:** cs.CL, cs.AI
**Utility Score:** 0.9

## Abstract

Test-time context optimization adapts frozen language models through textual feedback, but ordinary conditional generation provides no separate control over how strongly to reinforce the distributional changes induced by a context update. We introduce EMO, a training-free framework inspired by expectation--maximization that alternates question-specific context estimation (E-step) and distribution refinement (M-step). The E-step revises a system context using textual gradients from an external judge without access to gold answers. The M-step contrasts next-token distributions under the revised and preceding contexts at a shared prefix to construct a confidence-constrained logit correction. Feedback on the steered response drives the next context update, coupling adaptation across rounds with intervention within each generation. Theoretically, we connect parameter and context optimization through a shared target-KL objective and additive logit representations, and derive the steering vector from context-induced logit displacements. Under context-improvement and faithful-steering assumptions, we prove a one-round decrease in target KL divergence for sufficiently small steering strength. Under greedy decoding across eight models and six benchmarks, EMO improves the zero-shot baseline in 39 of 40 aggregated settings, averaging $+9.10$ percentage points. With the same judge, it adds $+1.53$ points on average over context-only optimization (TextGrad), with consistent MMLU-Pro gains across models. At matched target-model generation budgets, accuracy advantages over best-of-$N$ are strongest on Llama, while oracle coverage is higher in most comparisons despite fewer candidates. The coverage--selection gap motivates allocating test-time computation jointly to candidate generation and verification.

## Key Contributions

- Novel research in cs.CL, cs.AI
- High utility score (0.9) indicating significant research value

## Activation

closedloop, testtime, computation, framework, alternating, context, optimization, logits, steering

## Notes

Added by arXiv cron job on 2026-10-17.
