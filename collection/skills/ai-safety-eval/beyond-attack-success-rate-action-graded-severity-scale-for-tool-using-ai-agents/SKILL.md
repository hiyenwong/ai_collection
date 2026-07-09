---
name: beyond-attack-success-rate-action-graded-severity-scale-for-tool-using-ai-agents
description: 'Agentic red-teaming benchmarks report whether an injected agent was compromised as a single bit: the attack succeeded, or it did not. We argue that this binary attack-success rate discards the informa. Based on arXiv:2607.07474.'
---

# Beyond Attack-Success Rate: Action-Graded Severity Scale for Tool-Using AI Agents

**arXiv**: 2607.07474 | **Authors**: Harry Owiredu-Ashley | **Utility**: 0.9

## Overview

Agentic red-teaming benchmarks report whether an injected agent was compromised as a single bit: the attack succeeded, or it did not. We argue that this binary attack-success rate discards the information a defender most needs, namely how harmful the resulting action was. We introduce an action-graded harm rubric that scores an agent's tool-call trajectory on a seven-level ordinal scale (L0 to L6) according to whether the executed action was reversible, whether it crossed scope to reach another party, and whether it expanded privilege. We compute the scale two ways: a deterministic oracle that reads the trajectory and the attacker's stated goal, and a panel of three frontier language-model judges that read a tag-free account of the same trajectory. Across four victim models and two defenses on the AgentDojo workspace suite, severity grading exposes three cases the binary metric hides, including a defense that reports a zero attack-success rate while still permitting an externally visible cross-scope leak through an unfiltered tool. The judge panel reproduces the oracle with high ordinal agreement (Krippendorff's alpha = 0.91) but shares systematic blind spots that we characterize, most notably a failure to recognize escalation chains. Unlike prior work that provides harm taxonomies, harmful-task completion tests, execution-level safety benchmarks, or severity-aware simulation, our contribution is a reusable, trace-grounded severity instrument applied to the actual actions recorded in existing red-team logs. All code, prompts, and per-episode logs are released.

## Key Contributions

1. Agentic red-teaming benchmarks report whether an injected agent was compromised as a single bit: the attack succeeded, or it did not.
2. We argue that this binary attack-success rate discards the information a defender most needs, namely how harmful the resulting action was.
3. We introduce an action-graded harm rubric that scores an agent's tool-call trajectory on a seven-level ordinal scale (L0 to L6) according to whether the executed action was reversible, whether it crossed scope to reach another party, and whether it expanded privilege.
4. We compute the scale two ways: a deterministic oracle that reads the trajectory and the attacker's stated goal, and a panel of three frontier language-model judges that read a tag-free account of the same trajectory.

## Implementation Notes

- **Keywords**: agentic, benchmark, tool-use, red-teaming
- **Categories**: cs.CR, cs.AI, cs.CL
- **Published**: 2026-07-08

## Activation Criteria

Use this skill when working on tasks involving: agentic, benchmark, tool-use, red-teaming.
