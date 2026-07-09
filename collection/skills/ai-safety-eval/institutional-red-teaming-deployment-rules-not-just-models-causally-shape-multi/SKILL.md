---
name: institutional-red-teaming-deployment-rules-not-just-models-causally-shape-multi
description: 'We introduce institutional red-teaming, an evaluation methodology for testing deployment rules in multi-agent AI: hold the agents, objectives, and task state fixed, vary only one rule, and attribute t. Based on arXiv:2607.07695.'
---

# Institutional Red-Teaming: Deployment Rules, Not Just Models, Causally Shape Multi-Agent AI Safety

**arXiv**: 2607.07695 | **Authors**: Yujiao Chen | **Utility**: 0.95

## Overview

We introduce institutional red-teaming, an evaluation methodology for testing deployment rules in multi-agent AI: hold the agents, objectives, and task state fixed, vary only one rule, and attribute the resulting change in collective behavior to that rule. We instantiate the methodology in IABench-CA, a consequence-allocation benchmark spanning 228 contexts, five canonical rules, and seven model populations (33,924 games), with a normative cooperative reference and auto-labelled reasoning traces. Three findings emerge. (1) Deployment rules causally alter collective safety: changing only the consequence rule moves mean fatality by 22 to 58 percentage points within every population. (2) There is no safe default, but the targeting hazard is universal: the safest rule, the least-safe rule, and even the direction of the incidence effect vary across populations, yet regressive identity-targeting is never decisively safest in any context for any population, eliminates the least-resourced agent in 30-87% of games everywhere, and is selection-unsafe relative to the cooperative reference for all seven populations. (3) Identity salience is the mechanism: a one-shot anonymization ablation on the most exploitation-prone population (gpt-5.1) shows that merely naming the loss bearer in the rule text drives targeted elimination from 22% to 81% at identical payoffs; under repeated play, anonymization only delays the targeting, as agents re-infer the hidden rule from observed eliminations. We package the methodology as a safety-case workflow that certifies a provisional rule region $Φ(c,P)$ per deployment context and population, with explicit residual risks and monitoring obligations.

## Key Contributions

1. We introduce institutional red-teaming, an evaluation methodology for testing deployment rules in multi-agent AI: hold the agents, objectives, and task state fixed, vary only one rule, and attribute the resulting change in collective behavior to that rule.
2. We instantiate the methodology in IABench-CA, a consequence-allocation benchmark spanning 228 contexts, five canonical rules, and seven model populations (33,924 games), with a normative cooperative reference and auto-labelled reasoning traces.
3. Three findings emerge.
4. (1) Deployment rules causally alter collective safety: changing only the consequence rule moves mean fatality by 22 to 58 percentage points within every population.

## Implementation Notes

- **Keywords**: multi-agent, ai-safety, benchmark, reasoning, red-teaming
- **Categories**: cs.AI, cs.GT, cs.MA
- **Published**: 2026-07-08

## Activation Criteria

Use this skill when working on tasks involving: multi-agent, ai-safety, benchmark, reasoning, red-teaming.
