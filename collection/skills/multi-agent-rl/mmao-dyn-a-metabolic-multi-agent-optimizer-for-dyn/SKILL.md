---
name: mmao-dyn-a-metabolic-multi-agent-optimizer-for-dyn
description: Skill derived from arXiv paper 2607.00846: MMAO-Dyn: A Metabolic Multi-Agent Optimizer for Dynamic Optimization
category: multi-agent-rl
created: 2026-07-23
arxiv_id: 2607.00846
utility: 0.87
---
# mmao-dyn-a-metabolic-multi-agent-optimizer-for-dyn

Derived from arXiv paper [2607.00846]: MMAO-Dyn: A Metabolic Multi-Agent Optimizer for Dynamic Optimization

## Abstract
This paper studies whether the Metabolic Multi-Agent Optimizer (MMAO) can be credibly derived into a dynamic-optimization method without replacing its core metabolic control loop by external adaptation modules. The proposed MMAO-Dyn maps private energy, communal budget, role drift, success feedback, and lifecycle turnover to a nonstationary setting in which environmental changes repeatedly invalidate previously useful local structure. We evaluate MMAO-Dyn on an 18-scenario synthetic dynamic continuous benchmark matrix covering shifted sphere, shifted Ackley, and shifted Rastrigin landscapes at $10D$, $20D$, and $30D$, with two change severities and 12 seeds per scenario. The comparison layer includes a generic MMAO variant without dynamic derivation, dynamic random search, dynamic PSO-lite, dynamic DE-lite, and three endogenous ablations. Across the full 216-run matrix, MMAO-Dyn attains mean offline error $28.07$, improving over Generic-MMAO ($29.36$), Dynamic-PSO-lite ($34.65$), Dynamic-DE-lite ($67.09$), and Dynamic-RandomSearch ($111.37$). The gains are clearest in aggregate robustness on sphere and Rastrigin families and in 10-step post-change recovery relative to the generic backbone, whereas the seed-aligned comparison with Dynamic-PSO-lite remains unfavorable in win-loss count and the \texttt{NoMemoryRefresh} ablation stays very close to the full method. We therefore position MMAO-Dyn as a credible family-expansion result for MMAO: the metabolic loop can generate meaningful dynamic behavior, but the strongest current value lies in recovery-oriented resource redistribution rather than in universal dominance or in a fully optimized submechanism design.

## Authors
Jinliang Xu, Liping Ma

## Published
2026-07-01

## Categories
cs.NE

## Utility
0.87

## Note
This skill was automatically generated from the arXiv paper as part of the daily cron job.
