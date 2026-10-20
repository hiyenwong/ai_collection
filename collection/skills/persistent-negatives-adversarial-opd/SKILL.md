---
name: persistent-negatives-adversarial-opd
description: Persistent-negative adversarial distillation for black-box on-policy distillation - anchor the discriminator with historical teacher-student comparisons to stop the moving-target reward problem. Use when distilling from API-only teachers (no token probabilities), training discriminator-based rewards, or stabilizing adversarial RLHF pipelines.
category: ai_collection
trigger_words: black-box distillation, on-policy distillation, OPD, adversarial distillation, discriminator reward, moving target, GRPO, reward estimation MSE, live-pool negatives, judge training, teacher log-density ratio
---

# Persistent Negatives for Adversarial Black-Box On-Policy Distillation

**Source**: arXiv:2609.30864v1 (2026-09-25) — Ma, Lahrichi, Li, Han, Wu et al. (14 authors), cs.CL/cs.AI.

## Problem: The Moving-Target Discriminator

Black-box OPD improves a student from its own generations when the teacher (API) returns only sampled responses, never token probabilities. Adversarial distillation trains a discriminator/judge on prompt-matched teacher vs. student responses and uses its score as policy reward (GRPO-style). But the naive recipe samples negatives **from the latest student at each step** — after every policy update the negative distribution shifts, so the discriminator chases a target that just moved. Symptoms: unstable reward trajectories, below-chance discriminator dips, coupled reward-policy oscillation.

## Core Mechanism: Live-Pool Historical Negatives

Replace a **fraction** of each discriminator batch with **historical, prompt-matched teacher–student comparisons** (kept in a persistent pool):

- Historical comparisons → train the discriminator (anchored, stable negative distribution)
- Fresh student responses → keep GRPO strictly on-policy for the policy gradient
- The two roles are decoupled: discriminator anchoring does NOT compromise policy on-policyness

## Theory (why it works)

- The **Bayes-optimal reward** for the discriminator is the **teacher-to-negative log-density ratio**: `r*(y|x) ∝ log[p_T(y|x) / p_N(y|x)]` where p_N is the negative distribution.
- With fresh negatives, p_N mutates every policy step → the optimal reward itself mutates → reward-estimation MSE inflates.
- Persistent negatives **anchor p_N** to a mixture over the training history → the log-density ratio target is stable → reward-estimation MSE drops (derived under explicit assumptions in the paper).
- Result: smoother fresh-policy discriminator trajectories, fewer below-chance dips.

## Recipe

1. Run black-box OPD with a judge/discriminator head (teacher samples vs. student samples per prompt).
2. Maintain a **live pool** of (prompt, teacher response, student response) triples from recent training history, resampled each batch.
3. Each discriminator batch = mix of fresh negatives (latest student) + historical negatives (pool). Tune the fraction (paper explores replacement schedules).
4. Keep the policy loss untouched — GRPO / on-policy RL on discriminator scores.
5. Monitor: discriminator score trajectories on fresh student outputs; count below-chance dips; reward-estimation MSE proxy.

## Validation Results

Across 2 student families × 3 judges × 4 judged-chat benchmarks, at **matched discriminator compute**: consistent improvement over fresh-negative adversarial distillation and other black-box OPD methods; smoother discriminator trajectories.

## Reusable Design Principle

**When a learned reward depends on a data distribution that the learner itself shifts, decouple the two rates**: anchor the reward-model's negative/reference distribution to history while the policy stays on fresh data. Applicable to adversarial IRL, GAN-style reward shaping, and any reward model trained against a moving policy output distribution.

**Key axis**: the discriminator's negative distribution is a first-class design axis in black-box distillation — not an implementation detail.
