---
name: cros-causality-reward-on-scrambled-cots
description: "CRoS: Causality Reward on Scrambled CoTs Improves ..."
tags: [cs.CL, cs.AI]
source: arxiv
arxiv_id: 2610.42054v1
utility: 0.85
published: 2026-10-30
---

# CRoS: Causality Reward on Scrambled CoTs Improves Accuracy and Reasoning Faithfulness

**Authors:** Xiao Yu, Justin Chih-Yao Chen, Zaid Khan, Hyunji Lee, Mohit Bansal
**Published:** 2026-10-30
**arXiv:** [2610.42054v1](https://arxiv.org/abs/2610.42054v1)
**Categories:** cs.CL, cs.AI
**Utility Score:** 0.85

## Abstract

Reinforcement learning with verifiable rewards (RLVR) has become the standard method for training language models to reason. However, RLVR typically relies solely on outcome correctness, which does not guarantee that the CoT causally contributes to the final answer. Without this connection, outcome rewards may fail to reinforce high-quality reasoning. Existing causality metrics assess CoT causality by perturbing the CoT, such as deleting reasoning steps or injecting errors, and measuring changes in the final answer. However, these perturbations inevitably alter information in each step. Consequently, high causality scores may reflect sensitivity to information changes introduced by perturbation rather than true causality. Such confounding effects further induce undesirable reasoning behaviors when these metrics are used as training rewards, including generating less informative CoTs and reducing exploration and self-correction. To address this problem, we propose CRoS (Causality Reward on Scrambled CoTs), a novel CoT causality metric that perturbs the order of reasoning steps without altering content, thereby preserving information within each step. On Reasoning Gym with Gemma-3-4B, CRoS outperforms existing causality and outcome rewards in out-of-domain accuracy, CoT quality, and CoT faithfulness. Specifically, CRoS achieves 46.8% accuracy on five unseen logic and games datasets, outperforming the strongest baseline (43.8%). It also achieves better CoT quality, consistently 

## Key Contributions

- Novel research in cs.CL, cs.AI
- Published 2026-10-30

## Activation

cros, causality, reward, scrambled, cots, improves, accuracy, reasoning, faithfulness
