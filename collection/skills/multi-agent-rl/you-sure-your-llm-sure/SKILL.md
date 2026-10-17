---
name: you-sure-your-llm-sure
description: "Are You Sure Your LLM Is Sure? Repairing and Auditing Confidence"
tags: [arxiv, paper, multi-agent-rl]
arxiv_id: "2610.22139"
utility: 0.93
date: "2026-10-17"
---

# Are You Sure Your LLM Is Sure? Repairing and Auditing Confidence

**arXiv:** [2610.22139](https://arxiv.org/abs/2610.22139)
**Authors:** Arijit Dey, Bhartendu Kumar, Ramya Hebbalaguppe, Khuushi Maheshwari
**Published:** 2026-10-15
**Categories:** cs.AI
**Utility Score:** 0.93

## Abstract

Confidence scores determine whether an LLM answer is accepted, reviewed, or regenerated, yet scalar recalibration can only correct errors visible through the score itself. We introduce RADAR (Repair, Adopt, and Diagnose After Recalibration), a reliability framework that separates confidence repair from deciding whether to deploy the repair and auditing the errors that remain. Under squared loss, we decompose prediction risk into outcome noise, information hidden by the score, and mapping error; restricting repair to order-preserving maps additionally introduces a pooling gap. For repair, we propose Probe-Anchored Isotonic Calibration (PAIC), which learns a monotone map from correctness-probe predictions on unlabeled target prompts. PAIC's excess risk depends on the probe's score-conditional bias and fitting error rather than its overall accuracy. For adoption, we derive a paired procedure with finite-sample control of false improvements. For auditing, we develop a prompt-clustered kernel test that detects feature-aligned residual errors while accounting for dependent answers from the same prompt. Across multiple LLM checkpoints, benchmarks, and distribution shifts, richer predictors can improve confidence estimation, but projecting their information back to a scalar score can lose these gains, and lower prediction risk need not yield better review decisions. Across 47,400 replayed raw-score allocations, paired betting adopts candidates with lower held-out test risk in 42.95% of allocations, versus 15.09% for one-sided empirical Bernstein. RADAR thus provides a principled workflow to repair what a scalar score can express, adopt a repair only when supported by evidence, and diagnose systematic errors that recalibration leaves behind. Code and data will be released upon acceptance.

## Key Contributions

- Novel research in cs.AI
- High utility score (0.93) indicating significant research value

## Activation

sure, your, sure, repairing, auditing, confidence

## Notes

Added by arXiv cron job on 2026-10-17.
