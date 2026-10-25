---
title: "Same Luck, Different Choice: Twin-World Credit Assignment for Agentic Reinforcement Learning"
authors: "Zeropy Surio, Tobias Engel, Mei-Lin Chou, Anika Raman, Samuel Okafor"
published: "2026-10-22"
arxiv_id: "2610.31544v1"
url: "https://arxiv.org/abs/2610.31544v1"
categories: ["cs.LG"]
utility_score: 0.87
tags: [arxiv, paper, multi-agent-rl]
---

# Same Luck, Different Choice: Twin-World Credit Assignment for Agentic Reinforcement Learning

**Authors:** Zeropy Surio, Tobias Engel, Mei-Lin Chou, Anika Raman, Samuel Okafor
**Published:** 2026-10-22
**arXiv:** [2610.31544v1](https://arxiv.org/abs/2610.31544v1)
**Categories:** cs.LG
**Utility Score:** 0.87

## Abstract

Agentic reinforcement learning rewards a complete episode, yet the policy needs credit for every decision inside it. Counterfactual branching estimates this credit by re-running the episode after an alternative decision, but the branch draws its sampling noise independently of the factual episode, so the outcome difference mixes the effect of the decision with the luck of everything that follows. We observe that in agentic search the retriever, the corpus, and the grader are deterministic, so an episode is a deterministic function of the policy's decisions and its sampling noise. Twin worlds are therefore realizable: the same noise, a different decision. We introduce TWICE (TWIn-world Credit Estimation), which keys the Gumbel noise of every token by turn and line, rolls out counterfactual twins that inherit the factual episode's downstream noise, and turns their paired outcome differences into turn-level advantages for policy-gradient updates on actor-sampled trajectories; only the actor is deployed. Twin credit is unbiased for any coupling quality, its variance is that of an independent counterfactual scaled by $1-ρ$, where $ρ$ is the twins' outcome correlation, and under coupling the number of rollouts needed to resolve an advantage of size $Δ$ falls from $Θ(Δ^{-2})$ to $Θ(Δ^{-1})$. A square-root rule spends the twin budget where outcomes are predicted to disagree per unit cost. On seven question-answering benchmarks, TWICE improves the average exact match of GRPO by 5.3 and 4.5 points on Qwen2.5-3B and 7B, outperforms tree-search and counterfactual-branching baselines, and uses 68% fewer auxiliary tokens than VinePPO.

## Key Contributions

- Research paper from arXiv, auto-processed by Hermes cron job
- Utility score >= 0.85 indicates high relevance for AI/ML research
- Category: multi-agent-rl

## Related Skills

Check the `multi-agent-rl` directory for related papers and tools.
