---
name: qc-stark-llm-quantum-benchmark
description: Auto-verifiable LLM quantum computing benchmark with IRT.
---

# QC-Stark: Multi-Task LLM Benchmark on Quantum Computing

**Source**: arXiv:2609.35581 (Gupta, 2026-09-28)

## Benchmark Design

- **11 quantum computing tasks**: circuit construction, debugging, compilation, error
  correction, simulation (spanning the QC workflow).
- **2,750 evaluations**: 10 models × 11 tasks × 5 difficulty levels × 5 seeds.
- **All tasks auto-verifiable** — no human grading, no LLM-as-judge; exact programmatic
  checks (executability, output correctness against known answers).

## Core Methodology: Capability Dissociations

Overall aggregate rankings **mask substantial per-task variation**. The Spearman
rank correlation between the overall ranking and per-task rankings is statistically
insignificant for **4 of 11 tasks** — a model's leaderboard position does not predict
its standing on those subtasks.

**Practice**: always report per-task scores alongside aggregates; check overall-vs-
per-task Spearman ρ per task; flag tasks where ρ is insignificant as "dissociated
capabilities" that the aggregate hides.

## Measurement Validation (reusable for any benchmark)

1. **2-parameter Item Response Theory (IRT)**: fits per-item difficulty and
   discrimination, validating that the benchmark separates models meaningfully
   rather than by noise.
2. **Prompt sensitivity analysis**: rerun under multiple prompt conditions; confirm
   ranking robustness (rank stability across prompts = differences are model
   capability, not prompt artifacts).
3. **Seed replication**: 5 seeds per cell to quantify run-to-run variance before
   claiming model differences.

## Auto-Verifiable Scientific Benchmark Recipe

1. Choose tasks with ground-truth-checkable outputs (circuits → simulate and compare
   unitaries/states; programs → execute against test vectors).
2. Grade programmatically: parse output format, run exact checks; difficulty levels
   scale the task (qubit count, circuit depth, error rate).
3. Sweep models × tasks × difficulty × seeds; aggregate per task AND overall.
4. Fit a 2-param IRT model; drop items with poor fit; report discrimination stats.
5. Run prompt perturbations; verify rank correlation stability.
6. Report dissociations explicitly: per-task Spearman vs overall, with significance.

## Key Takeaways for LLM Evaluation
- Auto-verifiable design eliminates judge bias and enables large evaluation grids
  (thousands of cells) cheaply.
- Difficulty levels within a task give graded separation beyond binary pass/fail.
- Per-task dissociation analysis is the headline output — it converts a single
  leaderboard number into a capability profile.
- IRT provides a principled check that the benchmark measures a latent ability,
  not prompt idiosyncrasies.
