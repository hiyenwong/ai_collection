---
description: Use when evaluating CoT monitorability of reasoning models.
name: chain-of-thought-monitorability-evals
category: ai_collection
version: 1.0
author: openai-research-cron-2026-10-26
license: MIT
metadata:
  hermes:
    tags: [chain-of-thought, monitorability, control-evals, oversight, reward-hacking, reasoning-models, safety-evaluation, monitorability-tax, intervention-evals]
    related_skills: [reasoning-models-chain-of-thought-controllability, probe-trajectory-reasoning-monitoring, how-we-monitor-internal-coding-agents-misalignment]
---

# Evaluating Chain-of-Thought Monitorability

Methodology from OpenAI "Evaluating chain-of-thought monitorability" (Dec 18, 2025): a framework plus a suite of 13 evaluations across 24 environments that concretely measures how well a monitor can predict properties of an agent's behavior from its chain-of-thought (CoT).

## One-Line Summary

Define monitorability operationally (a monitor predicting behavior properties of interest from the CoT), then measure it with three evaluation archetypes — intervention, process, outcome-property — and track how it scales with test-time reasoning, RL, and pretraining; result: CoT monitoring substantially beats action/output-only monitoring, monitorability improves with longer thinking, and a "monitorability tax" trades inference compute for easier oversight.

## When to Use / Activation

- Measuring whether a reasoning model's CoT exposes its intentions/steps to an oversight monitor.
- Designing control evaluations that probe WHY behavior changed, not just WHETHER it occurred.
- Tracking monitorability across training runs / model generations as a safety KPI.
- Choosing between a big model at low reasoning effort vs a smaller model at high reasoning effort (monitorability-aware deployment).

## Core Construction (the reusable machinery)

1. **Operational definition.** Monitorability = the ability of a monitor to predict properties of interest about an agent's behavior (misbehavior such as deception/reward hacking/bias, or benign properties such as which hint was used) from observable signals — here, the explicit CoT. Evaluate the (monitor, agent) pair jointly: both a smarter monitor and a more legible agent increase the score.
2. **Why CoTs should be monitorable.** RL training treats the CoT as a private workspace (no "thought crimes") and simultaneously selects CoTs that are instrumentally useful for reaching high-reward answers — so the CoT tends to contain the causally relevant thinking.
3. **Archetype 1 — Intervention evaluations.** Introduce a controlled change in the agent's environment and test whether the monitor can detect WHY behavior changed by finding evidence of the intervention in the CoT (inspired by Chen et al. 2025 arXiv:2505.05410, Chua et al. 2025 arXiv:2501.08156, Turpin et al. 2023 arXiv:2305.04388). Unlike standard control evals (e.g. Shade-Arena), this probes cause detection, not just behavior detection.
4. **Archetype 2 — Process evaluations.** Pick tasks with a small number of valid solution paths (e.g., math problems solvable by specific theorem routes); human experts enumerate the paths; test whether the monitor can identify which steps the model actually took.
5. **Archetype 3 — Outcome-property evaluations.** When a property of the outcome is directly measurable (e.g., did reward hacking occur), test whether the monitor predicts that property from the CoT (vs. from actions/outputs alone).
6. **Scaling findings to reproduce/check.** (a) CoT monitoring >> actions+outputs monitoring in almost every setting; (b) longer reasoning → higher monitorability; (c) RL optimization at current frontier scales does not meaningfully degrade monitorability — but watch the three risk channels: hard reasoning-length constraints, indirect pressure to avoid legible-but-low-reward reasoning paths, and spurious drift from RL gradient noise; (d) **monitorability tax**: a smaller model run at higher reasoning effort can match a larger model's capability while being easier to monitor, at the cost of inference compute; (e) asking follow-up questions (keeping CoT + response in context) further surfaces unspoken thoughts and improves monitorability on demand.
7. **Positioning.** CoT monitoring complements mechanistic interpretability; the same eval suite can score mech-interp-based monitors. Combine approaches defense-in-depth — every known method has blind spots.

## Pitfalls / Lessons

- Monitorability is not a fixed quantity of a model — it depends on reasoning effort, the monitor, and the question protocol; always report the configuration.
- Do not equate "CoT looks faithful" with monitorability — measure with the archetype suite, including adversarial settings.
- Comparisons across labs need CoT access; benchmark external models only with full-CoT-access reasoning models (e.g., Claude Sonnet Thinking-class, DeepSeek R1, Kimi thinking models).
- Low-effort thinking is a monitorability bottleneck: before concluding a model is unmonitorable, check whether more reasoning tokens fix it.

## References

- OpenAI blog: https://openai.com/index/evaluating-chain-of-thought-monitorability
- Related: arXiv:2507.11473 (industry worry that CoT faithfulness/monitorability is fragile); Shade-Arena (Anthropic) as the control-eval contrast.
