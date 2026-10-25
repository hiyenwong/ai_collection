---
name: eval-harness-retained-reasoning-compaction
description: "Agent evals measure harness settings, not just models"
---

# Eval Harness Settings: Retained Reasoning & Compaction

Methodology from OpenAI's ARC-AGI-3 analysis (Jul 2026): benchmark scores for agentic models are dominated by harness/API settings, not just model capability. Two production settings — retained reasoning and context compaction — tripled GPT-5.6 Sol's ARC-AGI-3 public-set score (13.3% → 38.3% RHAE) while cutting output tokens 6x.

## When to Use

- Benchmarking agentic/LLM systems on long-horizon tasks (games, computer use, multi-step research)
- Diagnosing surprisingly low scores on a public benchmark
- Designing an eval harness, or auditing one for external validity
- Reviewing benchmark claims that compare models run under different harnesses

## Core Failure Modes of Generic Harnesses

1. **Discarded reasoning**: if private reasoning messages are dropped after each action/turn, the model must re-derive the task from scratch every step — long-horizon learning collapses. Model "looks dumb" (long dwell time, no progress) but the harness is the cause.
2. **Rolling truncation**: dropping oldest messages once a char/token limit is hit means the model loses its own action history AND runs with a chronically full context window (which itself degrades performance).

## The Two Settings (production-matched)

- **Retained reasoning**: pass previous response ID (Responses API style) so reasoning persists across tool calls and turns. Effects: less per-action thinking, coherent strategies over time.
- **Compaction**: on context overflow, summarize-and-continue instead of truncating. Preserves learned task state; fewer output tokens for the same or better score.

## Rules of Thumb

- An eval measures a bundle: model + API settings + harness design + prompting. Attribute low scores to the bundle before the model.
- Compare models only under harnesses that match real deployment settings; a generic "fair" harness can systematically understate models trained with persistent reasoning.
- For your own agent stack: retain reasoning across steps, compact instead of truncate, and log which of these was active during any eval run.
- Models that beat hard games under product harnesses but fail under eval harnesses are a signature of this mismatch (e.g., Slay the Spire via computer use vs. near-zero on a truncated harness).

## Pitfalls

- Retained reasoning inflates cost per run; compaction quality varies — measure tokens AND score, not score alone.
- Don't overfit a benchmark by tuning harness per-benchmark; the point is matching deployment conditions, not maximizing one leaderboard.
- Contamination and metric choice still apply (RHAE vs raw pass rate tell different stories).

## Activation Keywords

- harness settings benchmark
- retained reasoning
- context compaction vs rolling truncation
- eval external validity
- ARC-AGI-3
- low benchmark score diagnosis
