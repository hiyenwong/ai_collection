---
name: qusema-semantic-oracle-bug-detection
description: "Use when testing quantum libraries (Qiskit/PennyLane) for silent bugs. Semantic-oracle agentic loop."
category: ai_collection
---

# QuSema: Semantic-Oracle Silent Bug Detection for Quantum Libraries

**Paper**: QuSema: Detecting Silent Bugs in Quantum Libraries via Quantum-knowledge-enhanced Agents (arXiv: 2610.10258, Song et al., NTU/HKUST/ZJUT, 2026-10-07)
**Category**: Systems Engineering (cs.SE) × Quantum (quant-ph) — Thursday crossover

## Activation

- quantum library testing, silent bug, Qiskit bug, PennyLane bug
- semantic oracle, agentic testing, LLM bug detection
- API-local defect, defect hypothesis generation

## Problem

Quantum libraries (Qiskit, PennyLane) are critical infrastructure but contain **silent bugs**: non-crash defects that return incorrect results without exceptions. Existing oracles (failure-based, differential comparison, metamorphic) miss bugs when no comparable implementation or known output-relation exists. Missed bugs propagate into experimental conclusions, simulation studies, and algorithm designs.

**Key empirical finding**: ALL examined historical silent bugs (20 maintainer-confirmed in Qiskit/PennyLane) are **API-local** — the semantic deviation can be localized to the first library API that transforms a valid input into an invalid output. This leaves semantic evidence in implementation logic + documentation.

## Method: Three-Stage Agentic Workflow

### Stage I — Contextual Unit Preparation
- Analysis unit = **code segment** (function/method), NOT whole file (too much unrelated context) or isolated function (missing dependencies)
- Each contextual unit = target code segment + documentation constraining intended behavior + call relations to related implementation logic
- Python: extract via standard `ast` module (module functions, class methods)
- Example: Qiskit's 7,778-line `standard_gates_commutations.rs` — analyze extracted segments with attached commutation tables, not the full file

### Stage II — Semantic Defect Detection
1. Interpret quantum semantics + documented behavior as **semantic constraints** on each code segment (source-level semantic oracle)
2. Identify conditions where a **valid input → invalid output**
3. Convert each suspected violation into a **testable defect hypothesis**: (triggering input, predicted erroneous behavior, violated quantum-semantic/documented constraint)
4. Validate via execution; retain supported hypotheses as candidate defects

Example: Qiskit #13079 HoareOptimizer — when control qubit is |1⟩, CX simplifies to X on target; X² = I means adjacent X gates should cancel; the buggy implementation still processes the original node after replacement — violating quantum semantics (X² = I) AND documentation simultaneously.

### Stage III — Library API Triggering & Bug Validation
1. Search for API entries that can **reach** the defective implementation (reverse call-chain guidance)
2. Construct user-level inputs preserving the triggering condition
3. Verify the semantic deviation is exposed at API level
4. Classify by input validity + API documentation → distinguishes internal defects from **user-triggerable library bugs**

## Results

| Configuration | Mean relocation (of 20) | Cost (USD) |
|---|---|---|
| QuSema + Opus 5 | 16.00 | 1,603 |
| QuSema + DeepSeek-V4.1-Flash | 15.67 | 162 |
| Claude Code + Fable 5 | 14.67 | 425 |
| Codex + GPT-5.6-Sol | 13.33 | 117 |

- **40 previously unknown bugs** confirmed by developers in Qiskit 2.4.1 + PennyLane 0.45.0, incl. **30 silent bugs**; 5 beyond reach of differential AND metamorphic testing
- 10 of 20 benchmark bugs lacked comparable implementations → differential testing impossible; metamorphic also insufficient (equivalent circuit transformations don't guarantee unchanged resource estimates)
- DeepSeek backend delivers 98% of Opus performance at 10% of cost

## Reusable Patterns

### Pattern 1 — Semantic oracle from domain semantics + docs (no execution oracle needed)
When no execution-based oracle exists (no reference implementation, no metamorphic relation), derive correctness constraints from: (a) domain semantics (e.g., X² = I, unitarity, commutation rules) and (b) API documentation contracts. This is the **source-level semantic oracle** paradigm.

### Pattern 2 — API-locality scoping
Scope bug-hunting to defects where "valid input → invalid output" first occurs at a library API. This dramatically narrows the search space and justifies source-level analysis.

### Pattern 3 — Hypothesize-then-validate loop
LLM generates testable defect hypotheses (input + predicted wrong behavior + violated constraint), then validates by execution. Unsupported hypotheses are filtered — controls hallucination.

### Pattern 4 — Valid-input triggering requirement
A source-level defect only counts as a bug if triggered through **valid, documented API use**. Distinguishes internal implementation defects from user-facing bugs.

## Implementation Sketch

```python
# Agentic loop (pseudo)
for segment in extract_code_segments(library_source):
    unit = attach_docs_and_call_relations(segment)
    constraints = llm_infer_semantic_constraints(unit)  # quantum semantics + docs
    for violation in llm_find_constraint_violations(unit, constraints):
        hypothesis = to_defect_hypothesis(violation)  # (trigger, predicted_error, constraint)
        if execution_supports(hypothesis):
            candidates.append(hypothesis)
for hyp in candidates:
    api_path = find_reaching_api(hyp, call_graph)
    user_input = construct_valid_api_input(hyp, api_path)
    if api_execution_exposes(user_input, hyp):
        report_bug(api_path, user_input, hyp)
```

## Related

- [[fault-equivalent-circuit-reduction]] — automated FT circuit reduction (SE×quantum, same week)
- [[design-time-conformance-pulse-quantum-control]] — pulse-program conformance checking
- [[self-verification]] — multi-round generate-verify iteration
