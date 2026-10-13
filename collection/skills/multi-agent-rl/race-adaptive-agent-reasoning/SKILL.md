---
name: race-adaptive-agent-reasoning
description: Adaptive reasoning for LLM agents - decide per turn when to think vs act directly, using likelihood-drop signals from reasoning ablation (LoGiC) distilled into SFT/RL policies.
category: ai_collection
trigger: adaptive reasoning, when to think, reasoning budget, agent trajectory, cross-turn reasoning, reasoning skip, token cost reduction, agentic RL, likelihood probe
---

# RACE: Adaptive Reasoning via Cross-Turn Estimation

Methodology from arXiv:2610.12061 (Cheng et al., 2026-10-08, cs.AI/cs.CL): LLM agents do not need
to reason before every action — earlier reasoning keeps supporting later actions. RACE trains
agents to **decide when to reason**, cutting reasoning cost while maintaining task performance.

## Core Idea

Reasoning turns are only valuable when they change what subsequent actions the policy can produce.
Measuring this via generation-based verification is expensive; RACE uses a cheap proxy:
**the drop in likelihood of the subsequent reference actions when the reasoning turn is removed**.

- If removing reasoning turn r barely changes the likelihood of the reference actions
  (current + future), then r was redundant — the earlier context already "covers" those actions.
- If likelihood drops sharply, r is load-bearing → the agent should think there next time.

This likelihood-ablation signal is a **training-time estimator**; the trained policy internalizes
the decision and needs no probe at inference.

## LoGiC: Likelihood-Guided Progressive Reasoning-Cover Detection

Given a successful (or logged) trajectory with reasoning turns r_1..r_n interleaved with actions:

1. For each candidate reasoning turn r_i, compute the **likelihood change** of the reference
   actions at turn i and all subsequent turns j>i under (a) full trajectory vs
   (b) trajectory with r_i ablated.
2. Progressively mark turns whose removal has **limited impact** as *covered* (redundant);
   keep turns whose removal significantly lowers reference-action likelihood as *necessary*.
3. Result: a binary per-turn label — think / act-directly — plus a "reasoning cover" set
   that reproduces the trajectory's action support at minimal reasoning cost.

Implementation notes:
- Likelihood = log p(actions | context with/without r_i); use the reference policy or base model.
- Process turns in an order that avoids re-labeling covered turns (progressive pass),
  keeping the procedure O(n) forward passes per trajectory rather than exponential subsets.

## Training: Injecting the Signal

Two integration paths, both standard machinery:

- **SFT**: relabel trajectory turns — emit reasoning tokens only on "think" turns, skip reasoning
  and emit the action directly on "act" turns; fine-tune on the edited trajectories.
- **Agentic RL**: add reward shaping / turn-level credit that matches the LoGiC labels, or simply
  initialize from the SFT-edited policy then run policy optimization with the same action spaces.
  The policy learns the *meta-decision* of when reasoning pays off from data, not hand rules.

## Results

- Four representative agent benchmarks; substantial reduction in reasoning tokens/turns with
  maintained or improved end-task performance vs always-reason baselines.
- Applicable beyond agents: any multi-turn pipeline with expensive intermediate computation
  (tool calls, retrieval, self-reflection) where past computation amortizes.

## Reusable Pattern

"Likelihood-ablation as a cheap counterfactual": to decide whether a trajectory step is
necessary, measure Δ log-likelihood of the *future reference tokens* when that step is removed.
Steps with near-zero Δ are candidates for skipping/distillation. This generalizes to:
- skipping redundant retrieval calls (ablate the retrieved context, measure answer likelihood Δ)
- pruning chain-of-thought prefixes (cot-prefix-scoring pitfall family)
- deciding when to re-plan vs continue with an existing plan
