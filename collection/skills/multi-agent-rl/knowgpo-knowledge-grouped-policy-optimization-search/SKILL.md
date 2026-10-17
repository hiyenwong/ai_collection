---
name: knowgpo-knowledge-grouped-policy-optimization-search
description: "KnowGPO: Knowledge-Grouped Policy Optimization for Search Agents"
tags: [arxiv, paper, multi-agent-rl]
arxiv_id: "2610.22331"
utility: 0.99
date: "2026-10-17"
---

# KnowGPO: Knowledge-Grouped Policy Optimization for Search Agents

**arXiv:** [2610.22331](https://arxiv.org/abs/2610.22331)
**Authors:** Siqi Chen, Zhengxi Lu, Yuchen Yan, Xingyu Wu, Qipeng Chen...
**Published:** 2026-10-15
**Categories:** cs.AI
**Utility Score:** 0.99

## Abstract

Deep search agents solve knowledge-intensive tasks through long-horizon, multi-turn interactions, where assigning credit to individual search decisions is fundamentally difficult. Outcome-based reinforcement learning provides only a single terminal reward shared across an entire trajectory. Recent process-supervision methods aim to assign credit at finer granularity, but they typically anchor credit to either surface-level trajectory states or model-internal signals, both of which become unreliable in deep search where observations are heterogeneous and retrieved contexts are long and noisy. We propose KnowGPO, a reinforcement learning framework that aligns trajectories by the task-relevant knowledge they have acquired rather than by their surface observations. For each query, KnowGPO decomposes the information required to derive the answer into atomic knowledge conditions, and represents the state of a trajectory at each step by the subset of conditions it has satisfied. Trajectories sharing the same knowledge state are grouped for within-group comparison, and the incremental knowledge gain between consecutive steps serves as an environment-grounded process reward. Experiments on Xbench, BrowseComp-ZH, and GAIA show KnowGPO consistently outperforms outcome-only (GRPO) and process-supervision baselines (GiGPO, IGPO) by 3.8 to 4.2 points, with our 8B model rivaling or exceeding most 32B open-source systems.

## Key Contributions

- Novel research in cs.AI
- High utility score (0.99) indicating significant research value

## Activation

knowgpo, knowledgegrouped, policy, optimization, search, agents

## Notes

Added by arXiv cron job on 2026-10-17.
