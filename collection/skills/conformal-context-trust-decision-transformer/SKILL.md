---
name: conformal-context-trust-decision-transformer
description: Trust Guided Decision Transformer (TGDT) - use the model's own rolling next-state prediction error, calibrated by split conformal prediction on held-out offline data, to filter unreliable conditioning contexts before applying critic value guidance. Use for long-rollout stability in sequence-mode RL, offline RL with context drift, or any autoregressive policy where conditioning context goes out of distribution.
category: ai_collection
trigger_words: decision transformer, context drift, conformal prediction, trust calibration, offline RL, sequence modeling, rollout stability, context selection, value guidance, out-of-distribution detection, D4RL, next-state prediction error
---

# Trust Guided Decision Transformer (TGDT)

**Source**: arXiv:2609.31586v1 (2026-09-25) — Gautam, Diddigi, Kamanchi, Dayama, Mukherjee et al. (6 authors), cs.LG.

## Problem: Context Drift in Sequence-Model RL

Decision Transformers (return-conditioned policies) degrade on **long rollouts**: as the conditioning context grows, it drifts out of the training distribution and the policy silently becomes unreliable. Value-guided context selection (elastic selection by critic) does not help if the critic picks an action generated from a context the model itself cannot faithfully model.

## Key Insight: The Model Knows When It Drifts

The drift is **visible through the model's own next-state prediction error**: it rises during rollout and stays elevated — a direct, self-supervised signal of when the context has become unreliable. No external uncertainty model needed.

## Core Mechanism: Select Context *Before* Value Guidance

TGDT **reverses the order** used by value-only elastic selection:

1. **Trust filter first**: at each step, evaluate several recent **context suffixes** by their rolling next-state prediction error.
2. **Calibrate**: threshold the error using **split conformal prediction** on held-out offline data → a distribution-free, statistically valid cutoff for "trustworthy context."
3. **Then guide**: among only the *trusted* suffixes, a **frozen critic** selects the highest-value action.

Value-only selection lets the critic choose actions from contexts the model has flagged as unreliable; TGDT never lets value guidance see untrusted contexts in the first place.

## Recipe

1. Train a standard Decision Transformer on offline data (D4RL-style).
2. Hold out a calibration split. Compute per-step rolling next-state prediction error on it; fit a split-conformal quantile (e.g., 90% coverage) → threshold τ.
3. At deployment, maintain candidate context suffixes (several recent truncations).
4. Keep only suffixes whose rolling error stays below τ.
5. Among trusted suffixes, query the frozen critic; execute the argmax-value action.
6. Hard context reset remains available as a fallback when no suffix passes the trust filter.

## Validation Results (D4RL navigation + locomotion)

- Each component alone — state prediction, critic guidance, hard context reset — solves only part of the problem.
- TGDT reduces **persistent high-error runs** and improves return over: vanilla DT, reset-based context control, and value-only context selection.

## Reusable Design Principle

**Trust-then-guide ordering**: when combining any learned uncertainty signal with learned value guidance, filter candidates by the *model's own predictive fidelity* (calibrated conformally, so the cutoff is distribution-free) **before** applying value selection. Otherwise value guidance amplifies errors from contexts the policy cannot model.

Generalizes to: autoregressive agents with growing memory, RAG pipelines (trust retrieved context before reasoning over it), and any setting where conditioning inputs can silently go off-distribution.

**Activation**: decision transformer, context selection, conformal threshold, offline RL, rollout drift, trust calibration, frozen critic.
