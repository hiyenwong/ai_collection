---
name: arxiv-2608-20319-inducing-task-models-from-computer-use-traces
description: 'Inducing Task Models from Computer-Use Traces (arXiv: 2608.20319)'
category: multi-agent-rl
version: "1.0"
date: 2026-08-22
---

# Inducing Task Models from Computer-Use Traces

**Authors:** Yucheng Jiang, Zora Zhiruo Wang, Ruishi Chen, Diyi Yang
**arXiv:** 2608.20319
**Utility:** 1.00
**Published:** 2026-08-20T17:57:00Z
**Link:** http://arxiv.org/abs/2608.20319

## Abstract

Naturalistic computer-use traces, passively recorded screenshots and mouse or keyboard actions, are a valuable resource for deriving symbolic, auditable, and reusable models of how everyday work is done. Such models matter as computer-use agents enter real work, where agents need to learn how tasks are actually performed, and organizations need to audit and reuse that knowledge. However, inducing such task models is challenging, as activity is observed only as low-level events and real-world work is multi-threaded with interleaved goals. Existing methods assume a given task or a single workflow, and produce step-level summaries rather than structured task models. We introduce Task Model Induction (TMI), which (i) discovers the latent tasks in an unconstrained trace, disentangling concurrent activity, and (ii) for each latent task, induces a task model pairing a hierarchical objective model of recursive goal decomposition with a procedure model of the control flow that organized the execution. Intrinsically, on controlled human and agent trajectories, TMI recovers interleaved tasks with 0.974 agreement against ground-truth groupings and reconstructs 74.9% of the observed execution steps, far more than the strongest workflow induction baseline. Extrinsically, skills derived from TMI's task models improve held-out task accuracy by 30.0% over the strongest baseline.

## Summary

This skill encapsulates the key contributions and methods from the arXiv paper "Inducing Task Models from Computer-Use Traces". 
The paper presents novel ideas in multi-agent-rl that can be applied to agent systems.

## How to Use

1. Review the paper's methodology and findings.
2. Identify applicable components for your agent workflow.
3. Implement the core techniques as described in the paper.
4. Validate improvements in your specific use case.

## Pitfalls

- Ensure the paper's assumptions match your agent's environment.
- Validate implementation details before deployment.
- Consider computational complexity and resource requirements.

## References

- arXiv:2608.20319
