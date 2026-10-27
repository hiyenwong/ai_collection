---
name: sysml-coherent-multidiagram-benchmark
description: SEMAADB multi-view SysML coherence benchmark method.
created: 2026-10-08
version: 1.0
author: hermes-cron (from Aryashad & Jin, arXiv:2610.07356)
license: CC-BY-NC-SA-4.0 (paper); skill text original
source: arXiv:2610.07356
tags: [systems-engineering, MBSE, SysML, benchmark, LLM-evaluation, multi-view]
metadata:
  hermes:
    tags: [systems-engineering, MBSE, SysML, benchmark, LLM-evaluation, multi-view]
    related_skills: [cron-research-workflow]
---

# SEMAADB: Coherent Multi-Diagram SysML Benchmark

**Source:** Aryashad & Jin (UCLA), arXiv:2610.07356, Oct 2026, cs.SE/cs.AI.

**Trigger:** building MBSE datasets, evaluating LLM system-modeling coherence, multi-view consistency checking (SysML/UML/Archimate/AADL).

## Core Idea

Systems engineering uses **sets of linked SysML views** (Requirement, Block Definition, Activity, State Machine, Sequence) that must stay mutually consistent. Existing LLM diagram benchmarks test single artifacts; SEMAADB tests **set-level coherence**: repair one damaged view without collateral edits, and propagate one edit across all related views. Dataset: 3,000 contexts × 5 diagrams = 15,000 diagrams; 100 human-verified benchmark contexts.

## Dataset Construction Pipeline (reusable recipe)

1. **Coverage plan first**: stratify across domain (mechanical / electrical / computer-embedded / mechatronic-control), archetype, scale (component / subsystem / system), and source. ~846 contexts per major domain; medians: 10 blocks, 10 messages, 8 activities, 7 states, 6 requirements, 2 actors.
2. **Grounded description**: LLM + web sources writes a fixed-format system description per context (paraphrased, licenses kept).
3. **Shared entity model**: ONE canonical list of blocks, requirements, states, activities, actors, messages, relations. Every view must use these exact names — this is the consistency anchor. Validation gates: unique names, all relations resolve, sufficient info per view. Failed checks → model self-corrects with the error explanation.
4. **Per-view generation**: each diagram generated separately (focused prompts) from description + relevant shared-list slice + view-specific rules.
5. **Automatic validation (5 checks)**: (i) context completeness; (ii) shared-name/connection integrity; (iii) PlantUML renderability (≤3 repair attempts, renderer errors fed back); (iv) per-view content appropriateness (requirements in Requirement view, states in State Machine...); (v) **cross-diagram comparison** — shared names/relations must agree across views.
6. **Deterministic stratified selection** of 100 contexts for the benchmark core (domain × archetype × difficulty × provenance).
7. **Human verification**: rubric-scored (0–3) on SysML correctness, domain plausibility, cross-diagram consistency, completeness; dual review on 20 contexts with hidden independent scoring + adjudication; corrections limited to local fixes, redesigns rejected.

Full provenance stored: prompts, model, renderer version, repair attempts, token counts — every example traceable and re-renderable.

## Benchmark Tasks

### Task 1: Diagram Repair
Input: description + all 5 views, exactly one damaged. Two damage categories:
- **Syntax**: broken arrow/keyword/stereotype/brace/quote → fails to render; renderer message included in prompt. (557 instances)
- **Semantic**: renderable but inconsistent — rename entity, delete edge, redirect/reverse edge, remove requirement, exchange two names. No renderer hint. (600 instances)

Measure: **exact repair** via typed-graph comparison. Convert original/damaged/returned diagrams to typed element-relation graphs, normalize arrows/aliases: score = adherence (damaged region matches original) AND preservation (everything else unchanged). Parse/render failure = 0.

### Task 2: Cross-Diagram Update
Input: description + 5 views + one edit (Rename / Remove / Add). Model must select affected diagrams, explain, and return complete views. Expected changes derived from shared model as **(diagram, element, operation) tuples**; score tuple-level P/R/F1. (300 instances)

## Key Empirical Findings (GPT-5.6 Luna/Terra/Sol)
- **Syntax repair is nearly solved**: 98.0 / 99.1 / 99.8% exact.
- **Semantic repair is wide open**: 48.3 / 58.5 / 64.3%. Hardest subcategories: remove requirement (8–9%!), delete edge (32–40%), exchange names (22–67%). Easiest: redirect/reverse edge (76–94%), rename (70–84%).
- **Update propagation F1**: 73.0 / 77.5 / 80.7%. Rename ≈100%, Remove 82–99%, but **Addition collapses to ~40%** — models can propagate changes to existing content but fail to *place and connect new information*.
- Diagram selection is uniform (~84%) across models; the separation comes from **avoiding unnecessary edits** (unrelated edits: 9.5% Luna → 0.3% Sol) and resolving residual mismatches (20% → 1%).
- Interpretation: absence-type errors (missing requirement) are harder than substitution-type errors — nothing incorrect to anchor on. Set-level reasoning ≠ rendering ability.
- Cost: full headline eval = $37.40 (cheap, reproducible).

## Reusable Patterns
1. **Shared-entity anchor**: generate all views from one canonical entity list; consistency becomes checkable (and repairable) by construction, not by hope.
2. **Typed-graph evaluation over string diff**: parse artifacts to typed element/relation graphs, normalize, then compare — immune to formatting/order noise; enables adherence+preservation decomposition.
3. **Absence vs substitution damage taxonomy**: when benchmarking repair, separately score errors-of-omission — they expose different (worse) model capabilities.
4. **Tuple-based propagation metrics**: for multi-artifact consistency, derive expected change tuples from the source-of-truth model and score P/R/F1 at tuple level.
5. **Concentrate human review on the eval set**: automatic gates (render + cross-checks) filter scale; humans score only the benchmark core under a fixed rubric with inter-rater agreement on a hidden shared subset.
6. **Provenance as first-class data**: prompts, models, renderer versions, repair attempts stored per instance — benchmark stays auditable across model generations.

## When to Use
- Building MBSE/AI-assisted modeling datasets or benchmarks (SysML, UML, Archimate, AADL...)
- Evaluating LLMs for systems-engineering artifact generation/editing
- Designing consistency checkers for multi-view engineering models
- Diagnosing whether an LLM failure is rendering-level vs semantics-level

## References
- Aryashad, Jin. *A Validated Dataset and Benchmark for Coherent Multi-Diagram SysML Models*. arXiv:2610.07356 (2026) — SEMAADB
- SysMBench (requirements→SysML v2), OmniDiagram, FlowVQA — single-artifact predecessors
