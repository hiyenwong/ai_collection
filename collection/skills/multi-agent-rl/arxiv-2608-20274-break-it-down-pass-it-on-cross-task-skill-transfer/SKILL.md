---
name: arxiv-2608-20274-break-it-down-pass-it-on-cross-task-skill-transfer
description: 'Break It Down, Pass It On: Cross-Task Skill Transfer in LLM Agents (arXiv: 2608.20274)'
category: multi-agent-rl
version: "1.0"
date: 2026-08-22
---

# Break It Down, Pass It On: Cross-Task Skill Transfer in LLM Agents

**Authors:** Yiyang Feng, Biddut Sarker Bijoy, Niranjan Balasubramanian, Jiawei Zhou
**arXiv:** 2608.20274
**Utility:** 1.00
**Published:** 2026-08-20T17:12:08Z
**Link:** http://arxiv.org/abs/2608.20274

## Abstract

Large language model (LLM) agents can induce skills from completed tasks and reuse them later to grow more capable with experience. In practice, induced skills may transfer unreliably and can even harm the agent that retrieves them. When agent-induced skills transfer reliably across tasks remains an open question. We conduct a comprehensive and controlled study of how the way skills are induced shapes their transfer across tasks. Specifically, we compare task-level with subtask-level skill induction and text with code skill formats, the two axes along which existing methods differ. Task-level skills mostly reduce the agent's performance below its no-memory baseline while subtask-level skills raise it above on average, and text skills transfer better than code skills. To further understand our findings, we examine two complementary properties of the induced skills: specificity, which measures how closely a skill matches real tasks, and abstractness, which measures how evenly its relevance spreads across tasks. Neither property alone predicts task success, but their combined effect does, which we propose as a skill utility score. The score correlates consistently with task success when skills are transferred, and subtask-level and text skills score higher. Computing skill utility only needs the skills and task descriptions but not any task execution, so our score serves as a practical diagnostic of a skill memory before any new task runs.

## Summary

This skill encapsulates the key contributions and methods from the arXiv paper "Break It Down, Pass It On: Cross-Task Skill Transfer in LLM Agents". 
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

- arXiv:2608.20274
