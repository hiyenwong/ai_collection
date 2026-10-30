---
name: distributional-reward-calibration-and-budget-neutral-credit-
description: "Distributional Reward Calibration and Budget-Neutral Cr..."
tags: [cs.AI]
source: arxiv
arxiv_id: 2610.40250v1
utility: 0.92
---

# Distributional Reward Calibration and Budget-Neutral Credit Assignment for Multimodal RLVR

**arXiv ID:** [2610.40250v1](https://arxiv.org/abs/2610.40250v1)
**Published:** 2026-10-29
**Authors:** Lang Chen, Zongxin Xu, Borui Wang, Anran Liu, Shitong Chen
**Utility Score:** 0.92

## Abstract

We revisit advantage estimation in Group Relative Policy Optimization (GRPO) and observe that any token-level advantage admits a two-stage factorization: a \emph{sample-level baselining} step that converts scalar verifier rewards into a comparable sequence-level signal, and a \emph{token-level credit assignment} step that distributes that signal over the trajectory. Existing estimators typically address only one of these stages: affine baselines preserve the shape of each task's reward law, so heavy tails and binary cliffs propagate into the gradient, while token-level credit rules tie the size of each token's update to raw confidence scales and need not conserve the total credit issued by the verifier. We propose \textbf{TACE} (Two-stage Advantage and Credit Estimation), a two-stage estimator that addresses both stages. At stage~(S1), we replace linear standardization with a one-dimensional optimal-transport map to a standard normal, which gives a common population reward law across tasks and caps finite-sample outliers deterministically. At stage~(S2), we rank-calibrate a stop-gradient evidence contrast within each trajectory and renormalize the clipped token weights to have mean one, so credit is redistributed across tokens while its total mass and sign are conserved. We prove population-level inter-task moment equity, a deterministic tail bound, and mass-conservation, boundedness, and sign-anchoring properties that affine baselines and unnormalized token weights do not sa

## Key Contributions

- Research in multi-agent-rl domain with practical applications
- Published in top arXiv categories: cs.AI

## Activation

cs.AI, arxiv paper, utility 0.92
