---
name: code-primitives-lego-repository-engineering
description: "Use when building repositories with LLM agents. Reusable primitives with resident LLMs adapt themselves."
category: ai_collection
---

# Code Primitives + LEGO: Repository-Scale Engineering via Agent-Native Reusable Components

**Paper**: Large-scale Repository Engineering via Agent-Native Reusable Code Primitives (arXiv: 2610.09079, 2026-10-06, cs.SE/cs.CL/cs.CV)
**Category**: Systems Engineering (cs.SE) — repository-scale LLM code generation

## Activation

- repository-scale code generation, LLM coding agent, repo construction
- code reuse, code primitive, component adaptation
- LEGO framework, CodeFace, repository reconstruction benchmark

## Problem

LLM coding environments can generate files, but complete repositories require interacting modules, interfaces, configurations, tests, and dependencies to work together. Strongest of 13 evaluated backbones reaches delivery score 0.318 and scores ZERO on 41% of repository reconstruction tasks.

## Core Abstraction: Code Primitive

A reusable executable component **equipped with a resident LLM** as its natural-language interface:

```
P_i = (C_i, I_i, D_i, V_i, X_i, M_i)
  C_i: implementation
  I_i: exposed interface + behavioral contract
  D_i: dependency closure
  V_i: carried validation tests (own test suite)
  X_i: supporting context + provenance
  M_i: resident LLM
```

Median primitive: 214 lines, 2 files, 4 exported symbols, 9 validation tests. Boundary = functional coherence + dependencies for independent execution.

**Key operation — reuse by ADAPTATION (not invocation)**:
```
(s_i, u_i) = M_i.assess(P_i, r, C)       # relevance + usage proposal
(P'_i, µ_i) = M_i.adapt(P_i, r, C)       # adapted variant + requirements imposed on other components
```
Adaptation may modify interfaces, representations, dependencies, config, implementation — while preserving the intended capability. Operates only on its own state + bounded context (target location, required exports, interfaces to bind). Then reruns its carried validation V_i.

**CodeFace**: library of 1,424 validated primitives (871 mined, 343 harvested, 210 web-sourced).

## LEGO Pipeline — Three Coordinating Mechanisms

1. **Retrieval and Activation** — decompose request q into ordered capability requirements Π_t = (r_1...r_K); retrieve m=2 candidate primitives per requirement; each candidate self-assesses relevance; activate smallest mutually compatible set
2. **Primitive Collaboration** — activated primitives adapt implementations while propagating interface/dependency requirements µ to connected components (resolve cross-component constraints)
3. **Diagnosis and Verification** — execute available + synthesized tests; localize failures to components or their interactions; **reactivate affected primitives** for revision. Loop until validation succeeds or budget exhausted.

## Mining Pipeline (six steps)

parse repo → program entities + relations → dependency graph → segment into components (boundaries refined against neighboring code/docs/tests) → infer interface from exported symbols + observed usage → collect tests/config/docs into V_i, X_i (local helpers internalized, external deps → D_i) → synthesize + validate in isolation (build/import/runtime/test failures guide boundary refinement).

## Results (LEGO-REPO: 522 executable reconstruction tasks, 7 domains, 22 capability tracks, D1–D5, scored against native test suites)

- LEGO improves **all 13 evaluated backbones** by +0.1474 mean absolute (+76.5% relative)
- GPT-5.6-terra: 0.3180 → 0.5134 (**+61.4%**)
- Outperforms OpenHands (matched backbone) by 57.3%, Claude Code (Sonnet 5) by 56.2%
- Adapted primitives > retrieved-code-as-context > vendored-unchanged (controlled comparison)
- GPT-OSS-20B for adaptation/diagnosis retains 95.1% of score at 24.0% lower cost
- Gains persist on 3 external benchmarks + disjointly re-mined CodeFace

## Reusable Patterns

### Pattern 1 — Component-owns-adaptation
Delegate adaptation to the component being reused (via its resident LLM), not to a central generator agent. The component knows its own contract, dependencies, and tests. Central orchestrator only decides WHO to activate and HOW requirements propagate.

### Pattern 2 — Carried validation as the reuse differentiator
A reusable component that carries its own validation tests can verify its own adaptation. This distinguishes primitive adaptation from generic LLM editing — the tests gate every adapted variant.

### Pattern 3 — Requirement propagation graph
When a primitive adapts, it emits requirements µ_i→j on other components. Modeling cross-component constraints as explicit propagation (rather than hoping the central agent notices) is what makes repository-scale integration tractable.

### Pattern 4 — Empty-package floor / original-source ceiling scoring
Benchmark repository construction between an empty-package floor and original-source ceiling, scored by the package's native test suite. Measures true delivery, not file similarity.

## Related

- [[agents-k1-knowledge-orchestration]] — agent-native knowledge graphs
- [[qusema-semantic-oracle-bug-detection]] — agentic testing with semantic oracles (same-day SE papers)
- [[shared-state-architecture]] — PSI shared-state agent coordination
