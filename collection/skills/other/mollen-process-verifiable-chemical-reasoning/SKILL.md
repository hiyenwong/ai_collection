---
name: mollen-process-verifiable-chemical-reasoning
description: "Process-verifiable language for chemical reasoning: a layered Lean-based kernel checks state transitions and assertions over an explicit molecular state; a typed witness protocol separates native structural checks from externally supplied measurements; MolLean-MCP exposes transitions/checks/readouts during generation with rejected actions leaving state unchanged. Three execution modes (one-pass, whole-trace refinement, interactive MCP). Use when building verifiable domain reasoning or process-supervised tool protocols."
category: ai_collection
trigger: MolLean, Lean verification, chemical reasoning, process supervision, hallucinated claims, molecular state, witness protocol, MCP tool interface, stateful tool protocol, trace refinement, formal verification LLM
---

# MolLean: A Process-Verifiable Language for Chemical Reasoning

Methodology from arXiv:2610.20459 (Li, Bian; 2026-10-14, cs.CL/cs.CE/cs.PL).

## The Problem

Chemical chain-of-thought can contain **hallucinated structural and property claims** —
free-form text cannot enforce that asserted molecules, edits, and readouts are real.

## Architecture (three reusable layers)

1. **Layered Lean-based kernel**: chemical reasoning is grounded in an **explicit molecular
   state**. The kernel checks **state transitions and assertions over molecular readouts**,
   from primitive graph edits to compound transformations. Every claim becomes a checkable
   commitment.
2. **Typed witness protocol**: separates **native structural checks** (verifiable purely from
   the state: graph properties, valence, connectivity) from **externally supplied
   measurements** (properties that must come from tools/measurements and are typed as
   witnessed facts). This boundary keeps the kernel honest about what it can and cannot prove.
3. **MolLean-MCP stateful tool interface**: exposes transitions, checks, and readouts **during
   generation**. The model receives verification feedback to decide its next action;
   **rejected actions leave the state unchanged** (transactional semantics — bad steps never
   contaminate downstream reasoning).

## Three Execution Modes

- **One-pass trace execution**: execute a full written trace, checking each step.
- **Whole-trace refinement**: refine the entire trace against kernel feedback.
- **Interactive reasoning through MolLean-MCP**: stepwise verification feedback during
  generation.

## Results

- 8,800 matched examples, 12 tasks (molecular generation, editing, optimization, reactions),
  Qwen3.6-27B: **whole-trace refinement beats direct CoT on all 12 tasks**; MolLean-MCP
  complements it, reaching better performance specifically on **reaction tasks**.

## Reusable Patterns

- **Explicit state + checked transitions**: for any domain reasoning with checkable structure,
  ground claims in a typed state machine rather than free text; check each transition.
- **Native-vs-external proof separation**: type every predicate by whether it is decidable
  from internal state or requires external evidence — prevents the verifier from silently
  trusting ungrounded inputs.
- **Transactional tool protocol**: rejected actions must not mutate state; this makes
  stepwise interactive verification safe (failed actions are free, not corrupting).
- **Refine-whole-trace vs stepwise-interactive tradeoff**: batch refinement wins broadly;
  interactive feedback wins where early steps gate later ones (reactions: step order matters).

## When to Use

- Designing process-supervised verification for scientific/domain reasoning (chemistry,
  materials, hardware description).
- Building MCP-style tool interfaces with state + transactional semantics.
- Deciding between post-hoc trace checking and in-generation interactive verification.
