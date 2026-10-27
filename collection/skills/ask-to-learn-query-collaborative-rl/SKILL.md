---
name: ask-to-learn-query-collaborative-rl
description: "Use when offline RL is coverage-limited but direct online exploration is costly, unsafe, or infeasible. Query-based collaborative RL: adaptively query state-time pairs where a fixed-policy collaborator supplies actions and a simulator returns transitions."
category: ai_collection
metadata:
  arxiv_id: "2610.27606"
---

# Ask to Learn: Query-Based Collaborative Reinforcement Learning

Source: arXiv:2610.27606 (Zhang, Niu, Shi, Li, Qu et al., Oct 2026). Offline RL is fundamentally limited by the **coverage of the dataset**; collecting more trajectories through online exploration may be costly, unsafe, or infeasible. This work asks whether the limitation can be overcome **without directly interacting with the environment**.

## Problem setting (collaborator-mediated simulation)

- Learner starts with a fixed offline dataset.
- Learner **adaptively queries state–time pairs** of its choosing.
- A **collaborator** samples the action according to a **fixed, possibly suboptimal policy** (you do not control actions).
- The simulator returns the corresponding reward and next state.

Key constraint: you choose *where* to probe, not *what action* is taken — information acquisition is the only lever.

## Theory

- For finite-horizon tabular problems: an **instance-dependent information-theoretic lower bound** on the number of additional queries required to identify an ε-optimal policy.
- A **local quadratic approximation** characterizes per-instance query difficulty.

## Algorithm

- **Adaptive query allocation** guided by the local characterization; query complexity **nearly matches the local benchmark** under suitable conditions.
- Experiments on multiple synthetic and semi-synthetic environments confirm empirical efficiency.

## Reuse pattern

- When stuck between offline data and dangerous exploration, look for a **mediated information channel** (a collaborator, an expert oracle, a restricted simulator) and formalize what you control (query selection) vs what you don't (actions).
- Design active-query budgets from an information-theoretic lower bound: allocate queries to state-time pairs where they most reduce policy-identification uncertainty, not uniformly.
- The fixed-policy collaborator models realistic settings: human experts, third-party APIs, legacy controllers that answer "what happens if we are here" without granting control.

Related: offline RL coverage gaps, active learning, oracle distillation with weak queries, realistic-simulator RL, importance-weighted off-policy evaluation.
