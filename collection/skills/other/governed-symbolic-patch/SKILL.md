---
name: governed-symbolic-patch
description: Neuro-symbolic agent methodology for converting recurring failures into governed symbolic edits of process knowledge graphs. Failure-Driven Knowledge Acquisition (FDKA) localizes faults, synthesizes typed patches via constrained LLM generation, validates via multi-dimensional scoring and canary testing before commit. Use when building self-evolving agents, fixing recurring agent failures, implementing knowledge graph repair, or persistent fault elimination. Based on ANNEAL methodology (arXiv: 2605.16309).
---

# Governed Symbolic Patch Learning

Neuro-symbolic methodology for persistent fault elimination in LLM agents (ANNEAL, arXiv: 2605.16309).

## Problem

LLM agents recover from individual errors but repeatedly fail on the same fault when underlying process knowledge (operator schemas, preconditions, constraints) remains unrepaired. Prompt updates and memory patches don't fix structural knowledge gaps.

## Solution: FDKA Pipeline

**Failure-Driven Knowledge Acquisition** converts recurring failures into governed symbolic edits:

### Step 1: Localize
Identify the operator/node in the process knowledge graph responsible for the failure.
```python
# Match failure signature against known operators
failed_op = knowledge_graph.find_operator(failure_trace)
```

### Step 2: Synthesize Patch
Generate a typed patch through constrained LLM output:
```python
patch = llm.generate_patch(
    operator=failed_op,
    failure_context=failure_trace,
    constraints=type_schema,
    output_format="symbolic_edit"
)
```

### Step 3: Validate (Multi-Dimensional)
Before committing any patch:
- **Symbolic guardrails**: Check type consistency, schema compliance
- **Multi-dimensional scoring**: Evaluate correctness, specificity, safety
- **Canary testing**: Run patch against known test cases
- **Rollback capability**: Every edit has deterministic undo

### Step 4: Commit with Provenance
```python
commit = Commit(
    patch=patch,
    provenance={
        'failure_id': failure_id,
        'operator': failed_op.name,
        'timestamp': now(),
        'validation_scores': scores
    },
    rollback_plan=generate_rollback(patch)
)
knowledge_graph.apply(commit)
```

## Key Findings

- ANNEAL reduces recurring failure rates to **0%** (vs 72-100% for ReAct/Reflexion)
- Removes FDKA → success rate drops 26.7 percentage points
- Governed symbolic repair complements weight-level and prompt-level adaptation

## When to Use

- Agent has persistent, recurring failures across multiple runs
- Error recovery works episodically but doesn't prevent future failures
- Need persistent structural repairs without model retraining
- Safety requires governance guarantees on all knowledge modifications

## Pitfalls

- **Don't patch everything**: Only commit patches that pass all validation gates
- **Maintain provenance**: Every edit must be traceable to its originating failure
- **Canary tests are essential**: Never deploy patches without regression testing
- **Rollback is mandatory**: Knowledge graph changes must be reversible
