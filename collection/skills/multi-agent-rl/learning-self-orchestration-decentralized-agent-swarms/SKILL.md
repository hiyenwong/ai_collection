---
name: learning-self-orchestration-decentralized-agent-swarms
description: "Learning Self-Orchestration in Decentralized Agent Swarms"
tags: [arxiv, paper, multi-agent-rl]
arxiv_id: "2610.22322"
utility: 0.99
date: "2026-10-17"
---

# Learning Self-Orchestration in Decentralized Agent Swarms

**arXiv:** [2610.22322](https://arxiv.org/abs/2610.22322)
**Authors:** Guowei Xu, Zhenting Qi, Amani Kiruga, Himabindu Lakkaraju, Yilun Du
**Published:** 2026-10-15
**Categories:** cs.MA, cs.AI, cs.CL
**Utility Score:** 0.99

## Abstract

The capabilities of an agent swarm depend on both its individual members and how they coordinate. Yet existing multi-agent systems often train agents within fixed orchestration structures, separating the learning of individual capabilities from the organization of collective behavior. We introduce market-based post-training (MPT), a framework for jointly learning action policies and self-orchestration in decentralized agent swarms. Agents express their willingness to participate through bids, which determine who acts and how collective outcomes provide local training credit. Learning both action and bidding behavior allows individual capabilities and patterns of participation to adapt together without a central coordinating agent. We evaluate MPT on embodied crafting, robot navigation, and deep research. Results show gains over monolithic post-training and confirm that agent participation indeed evolves with learning. With the same post-trained action policies, learned self-orchestration outperforms alternative coordination strategies. Ablations show that both action and bidding benefit from learning, and that learned bids provide more effective action-training signals. Beyond the original training objectives, trained swarms adapt faster to related tasks and achieve better performance with larger populations at inference time. Larger populations also suffer smaller performance losses under agent dropout, demonstrating that learned self-orchestration supports reuse, scaling, and robustness in decentralized agent swarms. Code and trained models are available at https://github.com/Embodied-Minds-Lab/MPT.

## Key Contributions

- Novel research in cs.MA, cs.AI
- High utility score (0.99) indicating significant research value

## Activation

learning, selforchestration, decentralized, agent, swarms

## Notes

Added by arXiv cron job on 2026-10-17.
