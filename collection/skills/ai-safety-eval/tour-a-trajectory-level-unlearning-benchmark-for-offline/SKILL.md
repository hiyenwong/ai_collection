---
name: tour-a-trajectory-level-unlearning-benchmark-for-offline
description: 'TOUR: A Trajectory-Level Unlearning Benchmark for Offline Reinforcement Learning'
metadata:
  {
    "arxiv_id": "2607.21111",
    "utility": 1.0,
    "date_added": "2026-07-26"
  }
---

# TOUR: A Trajectory-Level Unlearning Benchmark for Offline Reinforcement Learning

arXiv: 2607.21111  
Published: 2026-07-23  
Utility: 1.0

## Summary
Offline Reinforcement Learning (RL) agents are trained on fixed behavioral trajectories, which makes trajectory-level deletion important when selected data must be removed after training. Evaluating such deletion is difficult because a lower membership score can reflect trajectory removal, residual memorization visible to another attack, or policy collapse that destroys useful behavior. We introduce Trajectory-level memOrization and Unlearning in offline RL (TOUR), a benchmark that combines trajectory-level partitioning, matched non-member controls, retraining references, retained-performance anchors, and multi-attack privacy auditing. Across D4RL locomotion experiments and an exploratory AntMaze extension, TOUR shows that common deletion baselines have environment-dependent privacy-utility behavior. Retraining and fine-tuning often provide stronger retained-utility references than uniform GA+Refit, while TrajDeleter remains a useful comparator but is not uniformly stronger under the same audit. Reference-model, threshold, deviation, equivalence, action-error, representation-based, and query-limited attacks further show that a single likelihood-based membership score can overstate deletion quality. In the evaluated settings, conclusions about offline RL unlearning are therefore not stable under single-score auditing. They depend on matched non-member construction, retraining-relative calibration, attack family, retained utility, and explicit scope for diagnostic architecture ...

## Key Information
- **Title**: TOUR: A Trajectory-Level Unlearning Benchmark for Offline Reinforcement Learning
- **Authors**: [Extract from entry]
- **Primary Category**: cs.LG

## Potential Skill Application
This paper presents research relevant to AI agent systems. Consider extracting methodologies, algorithms, or frameworks for skill development.

## Reference
- arXiv: https://arxiv.org/abs/2607.21111
