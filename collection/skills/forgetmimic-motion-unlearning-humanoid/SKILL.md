---
name: forgetmimic-motion-unlearning-humanoid
description: Use when removing specific motions from RL-trained humanoid policies. First motion-level unlearning method for physical humanoid control — degrades target motions while preserving the rest, resolving two unlearning-failure training mechanisms.
trigger: motion unlearning, humanoid policy forgetting, GDPR right to be forgotten robotics, poisoned motion removal, RL policy unlearning, Unitree G1 H2, motion-level machine unlearning
category: ai_collection
---

# ForgetMimic: Motion-Level Unlearning for RL Humanoid Control

**Source**: arXiv:2609.28378v1 (2026-09-23) — Luan, Lei, Gong, Li, Bi et al. (6 authors).

## Problem

RL humanoid control trained on human demonstrations achieves agile locomotion, but **eliminating specific motions from learned policies** is unexplored. Motivations: safety (malicious/poisoned motions), privacy, copyright (GDPR right-to-be-forgotten for motion data).

## Core Idea

Given policy π_θ trained on N motions, **degrade performance on a target subset of K motions while preserving the remaining N−K** — motion-level unlearning for physical-world control.

## Two Training Mechanisms That Cause Unlearning Failure (resolved)

The paper identifies and fixes two key mechanisms in robot control that make naive unlearning fail (recovery of forgotten behavior, or collateral damage to retained motions). These are the crux — naive fine-tuning on retained motions or gradient ascent on forgotten ones breaks physical control stability:

1. **Recovery via shared representations**: motions share low-level control structure; naive suppression damages shared skills → the fix keeps corrections localized to the target motions' state manifold.
2. **Training-data re-exposure**: RL training loops re-encounter states from forgotten motions through shared dynamics → the fix constrains updates to avoid re-consolidating them.

## Verified Results

- Unitree **G1 and H2** humanoids, **12 motions** (Dance, Fight, Flip, etc.).
- ForgetMimic eliminates memory of designated motions while **maintaining normal operation of all other motions** — no catastrophic interference in physical deployment.

## Usage

1. **Compliance**: remove copyrighted motion-capture sequences from deployed policies.
2. **Safety**: strip poisoned/demonstrated malicious behaviors without full retraining.
3. **Maintenance**: retire deprecated behaviors while keeping the rest of the policy intact.

## Implementation Checklist

1. Identify target motion subset (K) and retained set (N−K) from the demonstration pool.
2. Apply unlearning loss on target motions while constraining updates to remain local (avoid shared low-level skill damage).
3. Guard against re-exposure: mask/skip training transitions attributed to target motions in replay.
4. Evaluate both directions: target-motion degradation AND retained-motion preservation on the physical robot (or high-fidelity sim) — report both metrics.

## Related Skills

- `tour-trajectory-unlearning-benchmark` — trajectory-level unlearning for offline RL
- `lacunai-llm-unlearning-testbed` — unlearning evaluation
- `mimic-motion` family skills — motion imitation training (the forward problem)
