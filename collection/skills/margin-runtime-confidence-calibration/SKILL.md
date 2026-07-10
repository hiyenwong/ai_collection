---
name: margin-runtime-confidence-calibration
description: "Multi-Agent Runtime Grading via Incremental Normalization (MARGIN) — online confidence calibration for multi-agent AI coordination. Use when building multi-agent systems that need to weight agent trustworthiness at runtime: (1) coordinating responses from multiple foundation models, (2) selecting which agent's output to trust when self-reported confidence is unreliable, (3) calibrating confidence under distribution shift without held-out data or retraining.
arxiv_id: "2605.22949"
published: "2026-05-21"
authors: "Joss Armstrong"
tags: [multi-agent, confidence-calibration, online-learning, foundation-models, agent-coordination, trustworthiness]
---

# MARGIN: Runtime Confidence Calibration for Multi-Agent Coordination

Core methodology from arXiv:2605.22949 (2026).

## Core Concept

MARGIN (Multi Agent Runtime Grading via Incremental Normalization) is an online calibration method that learns per-agent, per-confidence-band calibration factors from the task stream itself. It requires **no model access, no held-out data, and no retraining** — making it ideal for black-box multi-agent deployments.

**Key insight**: Foundation model confidence is systematically miscalibrated and, on hard tasks, inversely correlated with accuracy. Design-time calibration (temperature scaling, Platt scaling) degrades under distribution shift. MARGIN fixes this by learning online from the task stream.

## Algorithm

MARGIN uses **symmetric exponentially weighted moving averages with Bayesian shrinkage blending**:

1. **Confidence bands** — Partition [0,1] confidence into B bands
2. **Per-band calibration factors** — For each agent a and band b, maintain:
   - `E_win[a][b]` — exponentially weighted average of correct answers
   - `N[a][b]` — effective sample count for shrinkage
3. **Bayesian shrinkage** — Blend per-band accuracy towards global average when counts are low
4. **Symmetric updates** — Update both the chosen agent AND non-chosen agents to avoid strategic manipulation

Three hyperparameters with robust defaults:
- `α` (smoothing rate, default 0.05) — Controls how quickly old observations decay
- `κ` (shrinkage floor, default 5) — Minimum effective count before per-band estimate dominates
- `β` (bias toward prior, default 0.5) — Strength of shrinkage towards global mean

## Key Findings

- Raw verbalized confidence produces pairwise resolution worse than random (45-56%) on hard benchmarks
- MARGIN corrects this completely, raising pairwise resolution to 70-89%
- Surpasses the always-best-model oracle on 3 of 4 benchmarks
- Achieves 3-6x lower calibration error than best design-time baseline under distribution shift
- Validated across 19 foundation models, 8 benchmarks, 50,000+ observations

## Implementation Pattern

```
def margin_calibrate(agent_confidence: dict[str, float],
                     calibration_factors: dict) -> dict[str, float]:
    # Shrink per-band factor toward global mean
    for agent, conf in agent_confidence.items():
        band = discretize(conf, num_bands=N_BANDS)
        factor = calibration_factors[agent][band]
        if factor.count < KAPPA:
            factor = blend_with_global(factor, global_avg, BETA)
        agent_confidence[agent] *= factor
    return agent_confidence

def margin_update(selected_agent: str, was_correct: bool,
                  all_agents: list[str],
                  calibration_factors: dict) -> None:
    # Symmetric update: update all agents
    for agent in all_agents:
        if agent == selected_agent:
            update_factor(agent, was_correct, ALPHA)
        else:
            # Non-selected agents: they would have been wrong
            # if chosen (conservative bound)
            update_factor(agent, not was_correct, ALPHA)
```

## Applications

- **Multi-agent routing** — Select which agent to query per task
- **Ensemble weighting** — Weight model votes by calibrated confidence
- **Confidence-aware abstention** — Only act when calibrated confidence exceeds threshold
- **Online adaptation** — Deploy to continuously changing data streams

## Activation Keywords

MARGIN, Multi-agent confidence calibration, runtime calibration, online calibration, agent coordination, foundation model trust, confidence band calibration, Bayesian shrinkage smoothing, multi-agent selection, self-reported confidence correction, ensemble weighting calibration
