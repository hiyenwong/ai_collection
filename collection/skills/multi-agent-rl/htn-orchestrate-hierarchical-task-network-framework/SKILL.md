---
name: htn-orchestrate-hierarchical-task-network-framework
description: "HTN-Orchestrate: A Hierarchical Task Network Framework for Multi-Agent Orchestra"
tags: [arxiv, paper, multi-agent-rl]
arxiv_id: "2610.22195"
utility: 0.99
date: "2026-10-17"
---

# HTN-Orchestrate: A Hierarchical Task Network Framework for Multi-Agent Orchestration

**arXiv:** [2610.22195](https://arxiv.org/abs/2610.22195)
**Authors:** Yanchen Deng, Jianguo Huang, Yao Long Teng, Yixuan Li, Handuo Zhang...
**Published:** 2026-10-15
**Categories:** cs.AI, cs.CL
**Utility Score:** 0.99

## Abstract

Orchestrating multiple agents on a complex task requires reconciling local subtask execution with global task planning. Dynamic dispatch approaches provide execution flexibility but do not explicitly model subtask hierarchies or dependencies, while predefined workflows impose this structure but fix the decomposition before execution begins. Therefore, we introduce HTN-Orchestrate, a two-layer framework that separates these responsibilities through a hierarchical task network (HTN). The Planner maintains subtask hierarchies and dependencies, deferring decomposition until prerequisite results become available, while local Orchestrators schedule workers to execute each leaf subtask. Results propagate upward under \textbf{AND} semantics, and accumulated findings inform a rebuilt task network when the current decomposition cannot resolve the task. On five benchmarks spanning web research, scientific reasoning, and research workflows, HTN-Orchestrate outperforms ReAct, Agent Team, and DeepSeek Harness using the same base model, achieving 89.73% accuracy on BrowseComp and 73.44% on SUPERChem, exceeding Agent Team by 2.45 and 4.69 percentage points, respectively.

## Key Contributions

- Novel research in cs.AI, cs.CL
- High utility score (0.99) indicating significant research value

## Activation

htnorchestrate, hierarchical, task, network, framework, multiagent, orchestration

## Notes

Added by arXiv cron job on 2026-10-17.
