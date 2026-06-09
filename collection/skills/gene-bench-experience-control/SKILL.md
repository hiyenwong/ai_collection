---
name: gene-bench-experience-control
description: "Strategy Gene methodology for experience-driven test-time control in LLM agents. Compact control-oriented experience representation (~230 tokens) outperforms documentation-heavy Skill (~2500 tokens) by +3.0pp. Core principle: encode experience as control signal, not documentation. Includes GEP protocol for gene evolution, AVOID directive patterns, and selective experience accumulation. Trigger: experience reuse, test-time control, skill representation, agent memory, experience evolution, strategy gene, GEP, prompt engineering for agents."
---

# Strategy Gene: Control-Oriented Experience Representation

Paper: "From Procedural Skills to Strategy Genes" (arXiv:2604.15097, Wang et al., Tsinghua/EvoMap, 2026-04)

## Core Insight

Experience reuse effectiveness depends on **representation form**, not content quantity. A compact Gene (~230 tokens, +3.0pp) beats a full Skill (~2500 tokens, -1.1pp). The key shift: from documentation-oriented to control-oriented experience objects.

## Gene Structure

g = (m, u, pi, alpha, c, v) -- all fields compact, control-facing:

- **m (signals_match)**: Keywords/trigger cues for task matching (2-5 terms)
- **u (summary)**: One-sentence compact description of the strategy
- **pi (strategy)**: Short ordered strategy steps, **include explicit AVOID directives**
- **alpha (avoid cues)**: Failure-aware warnings -- what NOT to do
- **c (constraints)**: Optional execution constraints (time, API limits)
- **v (validation)**: Optional executable checks or validation hooks

## Gene Template

```
signals: [keyword1, keyword2, ...]
summary: One sentence describing what this gene controls
strategy:
  1. Step one (concrete action)
  2. Step two
  AVOID:
  - Common failure mode A
  - Common failure mode B
constraints: (optional)
validation: (optional)
```

## Key Design Principles

### 1. Control-Oriented, Not Documentation-Oriented
- DO: Focus on actionable steps and failure warnings
- AVOID: Overview sections, background context, API reference dumps, example code blocks
- Rule of thumb: If removing a section does not hurt control, remove it

### 2. AVOID Directives Are High-Value
Failure warnings alone outperform strategy+failure bundles (+4.6pp vs +0.7pp). Distill failures into compact AVOID cues, not verbose logs.

### 3. Structure Matters Beyond Content
Same content in structured form (54.0%) vs flattened prose (50.5%) -- 3.5pp gap. Use explicit schema, not flowing text.

### 4. Selective Compression Over Additive Growth
- Appending raw failure history to a working Gene dilutes it (-2.0pp)
- Best practice: compress failures into focused AVOID warnings, replace rather than accumulate

### 5. Single Targeted Gene Over Multiple Composed Genes
Naive multi-gene composition collapses performance (54.0% to 44.9%). Select ONE most relevant gene per inference context. If multiple apply, prioritize by specificity.

### 6. Outdated Framing Still Useful
A gene with stale algorithm but correct problem framing (56.6%) beats no guidance. Preserve problem-structure insights even when specific solutions evolve.

## GEP Protocol (Gene Evolution Protocol)

Object hierarchy:
- **Gene**: Atomic control unit (the reusable experience chunk)
- **Capsule**: Validated task-level execution path with audit trail
- **Event**: Immutable evolution log (intent, mutations, outcome)

Evolution loop: trial -> validation -> solidification
- New experience enters as candidate mutation
- Validated via execution checkpoint pass rate
- If improved: solidify into canonical Gene form
- If degraded: discard, log failure as AVOID cue

## When Writing Skills/Genes for Hermes

Apply these principles to Hermes skill creation:
1. Keep description field focused on control triggers, not general background
2. Include explicit Pitfalls / AVOID sections with concrete failure modes
3. Prefer structured lists over prose explanations
4. When updating skills, compress rather than append -- replace stale content with distilled warnings
5. One skill per control domain; avoid loading multiple overlapping skills simultaneously

## Pitfalls

- DO NOT expand a compact gene into a fuller document expecting better performance
- DO NOT naively combine multiple genes/skills in one inference context
- DO NOT append raw failure logs -- distill into AVOID warnings
- DO NOT assume token count alone determines effectiveness -- organization matters
- DO NOT make overview/introduction sections -- they hurt Pro models (-4.7pp)
