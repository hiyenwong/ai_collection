---
name: set-level-diversity-rl-ideation
version: v1.0.0
last_updated: 2026-10-17
description: "Set-level RL: reward ideas by quality x marginal novelty."
arxiv_id: "2610.22324"
authors: "Manya Wadhwa, Pranav Narayanan Venkit, Hiroaki Hayashi, Yu Li, Tuhin Chakrabarty et al."
tags: [ideation, reinforcement-learning, diversity, reward-design, llm-training]
---

# Training Reasoning Models to Generate Diverse Scientific Ideas

From arXiv:2610.22324 (2026-10-15).

## Problem

LLM ideation work optimizes the quality of individual ideas and overlooks diversity — models propose sets of near-duplicate ideas. Document-grounded ideation needs ideas that are each high-quality, clearly distinct from one another, and grounded in source papers.

## Method

**Set-level RL objective:**

1. In a single generation, the model writes K structured idea cards grounded in the source papers.
2. The **set is scored jointly**: each idea's quality is weighted by its distance from the ideas written before it in the same set.
3. This teaches the model to steer each new idea away from its predecessors — diversity is rewarded as marginal novelty, not as deviation from a fixed reference.

## Results

- Trained 8B model beats Claude Opus 4.8 and GPT-6 Astra on creative utility (quality × diversity) on a contamination-free benchmark.
- Human study (4 experts): sets judged as promising as Claude Opus 4.8's, marginally more unique ideas.
- Coding agent running proof-of-concept experiments: success@k comparable to Claude Opus 4.8 — **added diversity costs no executability**.

## Reusable Pattern

**Marginal-novelty weighting for set-level RL.** Whenever a model must emit a *set* of outputs (ideas, hypotheses, designs, candidate solutions), score the set jointly with each element's value weighted by its distance from previously generated elements in the same sample. This turns set diversity from a post-hoc filter into a trainable objective, and because weighting is internal to the set, no external diversity metric or reference corpus is needed. Applicable to brainstorming agents, test-case generation, molecule/program candidate enumeration, and any sampling-then-select pipeline.

## Resources

- Paper: https://arxiv.org/abs/2610.22324
