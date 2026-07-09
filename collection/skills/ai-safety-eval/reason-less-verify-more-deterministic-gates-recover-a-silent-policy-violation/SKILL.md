---
name: reason-less-verify-more-deterministic-gates-recover-a-silent-policy-violation
description: 'Tool-using LLM agents can violate the very policies they are deployed to enforce while appearing to complete the task successfully. In policy-permissive environments, a tool may execute any well-forme. Based on arXiv:2607.07405.'
---

# Reason Less, Verify More: Deterministic Gates Recover a Silent Policy-Violation Failure Mode in Tool-Using LLM Agents

**arXiv**: 2607.07405 | **Authors**: Vikas Reddy, Sumanth Reddy Challaram, Abhishek Basu | **Utility**: 0.9

## Overview

Tool-using LLM agents can violate the very policies they are deployed to enforce while appearing to complete the task successfully. In policy-permissive environments, a tool may execute any well-formed call even when the corresponding state transition is forbidden by domain policy. The result is a silent wrong state (a booking cancelled, a passenger count changed, a claim acted on without verification) that neither the tool nor the agent's self-report exposes. We study this failure mode in the $τ^2$-bench airline domain. On a budget agent, 78% of observed failures are silent wrong-state failures with no tool error, and the aggregate failure rate is reproducible across disjoint seeds, not sampling noise. We then evaluate a lightweight intervention: deterministic, read-only pre-execution gates that inspect the proposed call and current state before allowing a write. A four-gate suite raises full-benchmark success from 29.6% to 42.0% on gpt-4o-mini (+12.4pp; paired task-level bootstrap P=0.0012), and the lift reproduces on a disjoint 15-seed set (+12.3pp; P=0.0008). The effect is concentrated where the gates fire: on the 26/50 firing tasks, success rises by +19.2pp, while movement on the 24 non-firing tasks does not exclude zero. Two negative controls (a self-enforcing retail domain and BFCL) bound the mechanism: gates help when tools are policy-permissive and add little where tools already self-enforce. As suggestive evidence, not a central claim, the same failure mode persists at the frontier: gpt-5.2 at default reasoning still attempts policy-violating writes, and the same suite improves success from 61.2% to 71.6% (+10.4pp; P=0.020; n=5, no replication). The contribution is a bounded evaluation and reliability result: deterministic gates do not guarantee task success, but they can deterministically prevent a known class of silent policy-violating writes at the action boundary.

## Key Contributions

1. Tool-using LLM agents can violate the very policies they are deployed to enforce while appearing to complete the task successfully.
2. In policy-permissive environments, a tool may execute any well-formed call even when the corresponding state transition is forbidden by domain policy.
3. The result is a silent wrong state (a booking cancelled, a passenger count changed, a claim acted on without verification) that neither the tool nor the agent's self-report exposes.
4. We study this failure mode in the $τ^2$-bench airline domain.

## Implementation Notes

- **Keywords**: llm, policy-optimization, tool-use
- **Categories**: cs.AI, cs.CR
- **Published**: 2026-07-08

## Activation Criteria

Use this skill when working on tasks involving: llm, policy-optimization, tool-use.
