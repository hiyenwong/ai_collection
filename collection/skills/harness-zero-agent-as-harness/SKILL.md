---
name: harness-zero-agent-as-harness
description: Use when building agent training pipelines or wanting to remove harness dependencies. Distills specialized agent-harness behaviors into model weights so gains survive with a single fixed harness at deployment.
trigger: harness distillation, agent-as-harness, harness removal, agent framework distillation, tool harness internalization, deployment-time harness, code-as-harness, agent training pipeline
category: ai_collection
---

# Harness-Zero: Harness Distillation via Agent-as-Harness

**Source**: arXiv:2609.24974v1 (2026-09-21) — Ye, Lu, Dong, Su, Song (Peking University).

## Problem

Agent harnesses (external systems mediating model-environment interaction: tool wrappers, file systems, browsers, scaffolds) substantially boost agent performance, but gains are tied to the harness at deployment. Since the best harness varies across domains/instances/models, a general-purpose agent must either settle for one suboptimal shared harness or route among ever-growing specialized ones.

## Core Idea: Harness Distillation

Use a domain- or instance-optimized harness as **training-time guidance** and transfer the behaviors it induces **into model weights**, so its gains survive under a single fixed target harness.

**Challenge**: source (optimized) and target harnesses differ in action space and available information — guidance from the optimized harness cannot serve directly as supervision for the target one.

## Agent-as-Harness Mechanism

1. **Harnessing agent**: guided by the optimized harness, a *harnessing agent* corrects student responses **before execution, in the target harness's action space** — turning harness guidance into training demonstrations compatible with the target harness.
2. **Fine-tune** on the resulting trajectories → internalizes harness-induced behavior into the model.
3. **Deploy** without the specialized harness (single fixed harness).

Contrast with **code-as-harness** (Gempt et al. lineage: harness executes/patches student code during training): agent-as-harness corrects in the target action space directly and outperforms code-as-harness for frontier LLMs.

## Verified Results

| Setting | Result |
|---|---|
| Frontier LLMs, same evolved harness | agent-as-harness > code-as-harness |
| Specialized harness removed at deployment | macro success 23.3% → **44.3%**, exceeding the 41.7% reached with harness still attached |
| Behavior recovery | **82.3%** average recovery of harness-induced patterns across 28 patterns in 3 domains (knowledge work, tool use, science) |

Key finding: distillation beats even *keeping the harness attached to the base model* — internalized behavior exceeds external scaffolding.

## Implementation Checklist

1. Identify the specialized harness behaviors worth internalizing (e.g., retry logic, verification steps, decomposition patterns, format checks).
2. Run the optimized harness over training tasks; have the harnessing agent rewrite each student response into the target harness's action space (corrections, not raw harness actions).
3. Treat corrected trajectories as SFT demonstrations; fine-tune.
4. Evaluate under the fixed target harness with the specialized harness removed.
5. Measure pattern recovery rate (fraction of harness-induced behaviors preserved) alongside task success.

## When to Use / Not Use

- **Use**: many specialized harnesses accumulating; deployment constraints forbid per-domain harnesses; want model-only portability of scaffold behaviors.
- **Not use**: behaviors requiring genuinely external state (live retrieval, sandbox execution) that cannot be approximated in weights; small models where correction quality by the harnessing agent is poor.

## Related Skills

- `agent-harness-scaling` — harness design itself
- `deterministic-retrieval-agent-reliability` — agent reliability engineering
- `tscg-tool-schema-optimization` — tool/harness interface design
