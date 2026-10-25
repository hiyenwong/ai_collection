---
title: "Questioning Instrumental Convergence in RLVR: Checkpoint Evidence from OLMo-3"
authors: "Barış Alparslan, Sandy Tanwisuth, Caleb Petterson"
published: "2026-10-22"
arxiv_id: "2610.31624v1"
url: "https://arxiv.org/abs/2610.31624v1"
categories: ["cs.LG", "cs.AI"]
utility_score: 0.97
tags: [arxiv, paper, multi-agent-rl]
---

# Questioning Instrumental Convergence in RLVR: Checkpoint Evidence from OLMo-3

**Authors:** Barış Alparslan, Sandy Tanwisuth, Caleb Petterson
**Published:** 2026-10-22
**arXiv:** [2610.31624v1](https://arxiv.org/abs/2610.31624v1)
**Categories:** cs.LG, cs.AI
**Utility Score:** 0.97

## Abstract

Instrumental convergence is often invoked as a general reason to expect capable agents to acquire or express power-seeking subgoals: self-preservation, resource acquisition, deception, or resistance to oversight which poses an important threat to the society. For LLMs, reinforcement learning is the first stage of post-training that directly optimizes behavior against an objective; therefore, it is the stage where convergent instrumental behavior, on IC grounds, likely to appear. Does reinforcement learning with verifiable rewards (RLVR) make a model more likely to express instrumental-convergence behavior, or does this depend on the training regime, evaluation frame, and stage of post-training? We study this question as a checkpoint-conditioned behavioral trajectory rather than as a single before/after safety score. Using InstrumentalEval, we evaluate OLMo-3-7B-Think across SFT, DPO, 13 intermediate RLVR checkpoints, and the final RLVR model. The trajectory is nonmonotonic: instrumental rate rises from 25.0% at SFT to 46.1% near RLVR step 200, then falls to 11.8% at the final checkpoint. Paired item-level tests and step-wise regression support the final SFT-to-RLVR reduction. Prompt framing does not explain this pattern: a harmful-prompt indicator combined with other framing effects explains only 15% of within-checkpoint score variance on average, and Iterative Null-space Projection (INLP) removes a detectable framing direction without changing the SFT-to-final-RLVR gap. Together with preliminary 32B endpoint results (35.53% SFT to 22.37% RLVR final), these findings indicate that RLVR does not monotonically increase instrumental behavior in this setting: the rate rises early, then falls below the SFT baseline. The result is specific to this model family and benchmark, and judge agreement is moderate, so absolute rates should be read cautiously.

## Key Contributions

- Research paper from arXiv, auto-processed by Hermes cron job
- Utility score >= 0.85 indicates high relevance for AI/ML research
- Category: multi-agent-rl

## Related Skills

Check the `multi-agent-rl` directory for related papers and tools.
