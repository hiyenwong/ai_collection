---
name: mosaic-multi-session-agentic-reinforcement-learning
description: "Mosaic: Multi-Session Agentic Reinforcement Learning"
tags: [arxiv, paper, multi-agent-rl]
arxiv_id: "2610.22174"
utility: 0.99
date: "2026-10-17"
---

# Mosaic: Multi-Session Agentic Reinforcement Learning

**arXiv:** [2610.22174](https://arxiv.org/abs/2610.22174)
**Authors:** Yilong Xu, Minrui Xu, Xinyu Zhou, Xiang Long, Haochen Tan...
**Published:** 2026-10-15
**Categories:** cs.CL, cs.AI, cs.LG
**Utility Score:** 0.99

## Abstract

Most existing agentic reinforcement learning methods assume single-session trajectories, where interaction proceeds within one continuously accumulated context. However, agentic techniques such as context compaction and subagent forking may produce trajectories spanning multiple sessions, creating a mismatch between the single-session training assumption and inference-time execution. Therefore, we introduce Multi-Session Agentic Reinforcement Learning, a more general setting that supports an arbitrary number of sessions within a trajectory. Under this setting, a widely adopted method is to broadcast trajectory-level advantages to all sessions, but this does not distinguish contributions from various sessions or guide session allocation within trajectories. To address this issue, we propose Mosaic, a multi-session agentic RL method with critic-free hierarchical optimization. At the trajectory level, it incorporates session-usage signals into advantage estimation. At the session level, it shapes each session's advantage according to the estimated marginal contribution. Experiments on BrowseComp with Qwen3.5-4B show that Mosaic outperforms broadcasting in both context compaction and subagent forking scenarios while using fewer sessions on average. Further analyses show that our method achieves improvements in session utility and allocation, which we suggested is a promising target for future advances in multi-session agentic RL.

## Key Contributions

- Novel research in cs.CL, cs.AI
- High utility score (0.99) indicating significant research value

## Activation

mosaic, multisession, agentic, reinforcement, learning

## Notes

Added by arXiv cron job on 2026-10-17.
