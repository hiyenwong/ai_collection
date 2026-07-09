---
name: think-big-search-small-where-capacity-matters-in-hierarchical-search-agents
description: 'Large language model based search agents increasingly adopt multi-agent architectures in which a main agent decomposes a complex question into sub-queries and dispatches them to parallel sub-agents. H. Based on arXiv:2607.07548.'
---

# Think Big, Search Small: Where Capacity Matters in Hierarchical Search Agents?

**arXiv**: 2607.07548 | **Authors**: Qinnan Cai, Yibo Zhao, Xiang Li | **Utility**: 0.85

## Overview

Large language model based search agents increasingly adopt multi-agent architectures in which a main agent decomposes a complex question into sub-queries and dispatches them to parallel sub-agents. However, existing systems instantiate all roles from a single model of identical scale, leaving open how model capacity should be distributed across roles. We factorize hierarchical search into three roles: a delegation role responsible for task decomposition, an execution role responsible for retrieval and evidence extraction, and an answer generation role held fixed as a confound control. We then conduct controlled capacity sweeps along the delegation and execution axes on five multi-hop QA benchmarks. The experiments yield three findings. First, role factorization consistently outperforms a single-agent baseline, improving exact match from 4.5 to 8.6 points across six model scales. Second, capacity sensitivity is asymmetric: scaling the delegation backbone improves EM by ~11 points, whereas scaling the execution sub-agent moves EM by only ~2.6 points, identifying decomposition as the capability bottleneck. Third, a 1.7B-parameter executor trained via quality-filtered trajectory distillation matches a frontier sub-agent in accuracy while consuming 37% fewer sub-agent tokens, advancing the Pareto frontier. These results suggest a concrete recipe for building hierarchical search agents: concentrate capacity at delegation and downsize execution without sacrificing accuracy. Our code is available at https://github.com/QinnanCai0115/role-factorized-search.

## Key Contributions

1. Large language model based search agents increasingly adopt multi-agent architectures in which a main agent decomposes a complex question into sub-queries and dispatches them to parallel sub-agents.
2. However, existing systems instantiate all roles from a single model of identical scale, leaving open how model capacity should be distributed across roles.
3. We factorize hierarchical search into three roles: a delegation role responsible for task decomposition, an execution role responsible for retrieval and evidence extraction, and an answer generation role held fixed as a confound control.
4. We then conduct controlled capacity sweeps along the delegation and execution axes on five multi-hop QA benchmarks.

## Implementation Notes

- **Keywords**: multi-agent
- **Categories**: cs.CL
- **Published**: 2026-07-08

## Activation Criteria

Use this skill when working on tasks involving: multi-agent.
