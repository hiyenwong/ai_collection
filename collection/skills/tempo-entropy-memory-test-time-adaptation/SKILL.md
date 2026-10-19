---
name: tempo-entropy-memory-test-time-adaptation
description: "Test-time adaptation for RL robot policies under deployment shift: frozen critic as reward-free performance surrogate, entropy regularization against critic overconfidence, score-based memory prioritizing hard observations. Use when adapting robot/control policies online without rewards or retraining."
category: ai_collection
trigger: test-time adaptation, TTA, robot policy adaptation, deployment shift, frozen critic, reward-free adaptation, entropy-regularized policy update, score-based memory, importance sampling deployment, locomotion robustness
---

# TEMPO: Entropy-Regularized, Memory-Guided Test-Time Adaptation for Robot Policies

Methodology from arXiv:2610.20318 (Alfarra, Mazzaglia, Peschl, Dijkman, Louizos; 2026-10-14,
cs.RO/cs.LG). Problem: RL locomotion policies fail at deployment when conditions shift
(rough/slippery terrain, payload change, sensing degradation), and retraining or manual
recalibration is infeasible under on-device latency and memory constraints.

## The Lightweight Baseline (starting point)

Adapt a pretrained policy **online, self-supervised, without rewards**:
- Update **only the actor**; keep the **pretrained critic frozen** and use it as a
  deployment-time **performance surrogate** (a reward substitute requiring no environment reward).
- This alone already gives a non-trivial adaptation signal, but it is unstable under severe shift.

## TEMPO's Two Stabilizers

1. **Entropy-promoting regularizer on the critic's predictive distribution.**
   Under shift the frozen critic extrapolates overconfidently, and following its gradients
   naively amplifies the error. Regularize the critic's distribution toward higher entropy to
   mitigate overconfident extrapolation before trusting its gradient direction.
2. **Score-based memory (prioritized-replay-inspired).**
   Maintain a memory of deployment observations scored by the frozen critic.
   Prioritize **low-value ("hard") observations** and apply **importance sampling** so the
   limited on-device compute focuses on the most informative deployment conditions —
   compute allocation follows difficulty, not uniform time.

## Reusable Design Pattern

- **Frozen-critic-as-surrogate**: when you cannot access rewards at deployment, a pretrained
  value function is a dense self-supervised signal for policy improvement — but only if you
  correct for its overconfidence under distribution shift (entropy regularization) and
  allocate updates non-uniformly (score-based memory + importance sampling).
- Budget-constrained TTA pipeline: surrogate signal → confidence correction → informative-sample
  focusing. Each stage addresses a distinct failure mode (no reward / extrapolation / wasted compute).

## Results (reusable calibration numbers)

- Go1, Go2, G1 robots in MuJoCo Playground, 4 representative shifts, multiple policy
  architectures: consistent gains, **up to 80% improvement** in single-device setting.
- Physical Unitree Go2 with added calf payload: fully on-device adaptation improves over the
  non-adapted baseline across real-world episodes.

## When to Use

- Deploying RL policies where environment conditions drift from training.
- On-device adaptation with hard latency/memory budgets and no reward access.
- Any setting with a pretrained value function + actor pair where online self-supervised
  correction is cheaper than retraining.
