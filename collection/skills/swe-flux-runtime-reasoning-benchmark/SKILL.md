---
name: swe-flux-runtime-reasoning-benchmark
description: Use when evaluating LLM code-execution reasoning or building execution-grounded benchmarks. Repository-level dynamic benchmark with gold answers auto-harvested from instrumented test executions, covering control flow, loops, state, dataflow, exceptions, invariants.
trigger: runtime behavior reasoning, execution-grounded benchmark, repository-level QA, SWE-Flux, oracle harvesting, program state reasoning, input perturbation variants, LLM code reasoning evaluation
category: ai_collection
---

# SWE-Flux: Repository-Level Runtime-Behavior Reasoning Benchmark

**Source**: arXiv:2609.28449v1 (2026-09-23) — Taherkhani, Abdollahi, Sepidband, Dhulipala, Nguyen et al. (6 authors).

## Problem

LLM coding benchmarks evaluate **static code understanding** (often with LLM-judged answers), while execution-reasoning benchmarks are limited to **snippets/functions**. Can LLMs reason about **runtime behavior at repository scale**?

## Benchmark Design

- **480 execution-grounded instances** across **12 real Python repositories**.
- **Gold answers harvested automatically from instrumented test executions** — not written manually, not judged by LLMs (removes judge bias and manual cost).
- Coverage: single-test and multi-test questions over **control flow, loops, program state, dataflow, exceptions, program invariants**.
- **Variant generation via input perturbation**: the oracle-harvesting pipeline generates fresh benchmark variants — valid for ~90% of selected instances, and substantially harder.

## Key Findings (5 LLMs evaluated)

| Result | Detail |
|---|---|
| Best model accuracy | only **37%** — task remains challenging |
| Stronger areas | localized behavior: invariants, intra-procedural control flow, exceptions, simple loops |
| Weaker areas | **dataflow, inter-procedural execution, precise state reasoning, suite-level aggregation** |

## Reusable Pattern: Oracle Harvesting

The methodology generalizes to any codebase:

1. **Instrument** test executions to capture runtime traces (variable states, branch outcomes, exceptions).
2. **Harvest ground truth** from the traces automatically → answers to "what happens at runtime" questions without manual labeling.
3. **Perturb inputs** to generate fresh variants (controls contamination/memorization; produces harder instances).
4. Question types: single-test (one path) vs multi-test (aggregation across a suite).

## Usage

1. **Evaluating agents on code reasoning**: measures dynamic behavior understanding that static QA misses; the 37% ceiling shows large headroom.
2. **Building execution-grounded evals for private codebases**: apply the instrumented-execution harvest pipeline to your own repos.
3. **Diagnosis**: distinguish localized vs global failure — a model strong on invariants but weak on dataflow points to different improvement levers.

## Related Skills

- `dogfood` — exploratory QA of web apps
- `agent-integration-testing` — agent framework testing
- `petri-alignment-tool` — alignment testing toolbox
