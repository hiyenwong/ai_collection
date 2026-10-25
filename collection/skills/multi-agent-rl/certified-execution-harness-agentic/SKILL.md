---
title: "Certified Execution Harness for Agentic AI: Safe and Least-Intrusive Petri-Net Supervisory Control Between Reasoning and Action"
authors: "Chao Gu, Quanyan Zhu"
published: "2026-10-22"
arxiv_id: "2610.31376v1"
url: "https://arxiv.org/abs/2610.31376v1"
categories: ["cs.AI", "eess.SY"]
utility_score: 0.95
tags: [arxiv, paper, multi-agent-rl]
---

# Certified Execution Harness for Agentic AI: Safe and Least-Intrusive Petri-Net Supervisory Control Between Reasoning and Action

**Authors:** Chao Gu, Quanyan Zhu
**Published:** 2026-10-22
**arXiv:** [2610.31376v1](https://arxiv.org/abs/2610.31376v1)
**Categories:** cs.AI, eess.SY
**Utility Score:** 0.95

## Abstract

This paper studies the problem of safe tool execution for large language model (LLM) agents under prompt injection. Using Petri nets, we formalize the execution harness between the LLM and its tools as a supervisory control problem, in which marks represent capabilities, approvals and budgets. Since a transition fires only if the marks it needs are present, an injected request whose preconditions are unmet or already spent is refused regardless of its wording. Treating tool outcomes as uncontrollable, we enforce safety by the conventional maximally permissive supervisor, and this safety transfers to the running system under four assumptions. Moreover, to capture an agent that may propose again after a refusal, we introduce the notion of a replanning closed loop, in which each retry costs an inference call. We show that, in this loop, the conventional supervisor can be arbitrarily more intrusive than a stricter safe one. Furthermore, for a given proposer model, the maximally permissive least-intrusive supervisor is characterized as a value-threshold refinement of the conventional one. Under precise conditions, this refinement orders two concurrent actions by at most one monitor place. On an autonomous release agent, we find by synthesis that safe deployment requires a step that the supervisor can refuse after a rollout starts.

## Key Contributions

- Research paper from arXiv, auto-processed by Hermes cron job
- Utility score >= 0.85 indicates high relevance for AI/ML research
- Category: multi-agent-rl

## Related Skills

Check the `multi-agent-rl` directory for related papers and tools.
