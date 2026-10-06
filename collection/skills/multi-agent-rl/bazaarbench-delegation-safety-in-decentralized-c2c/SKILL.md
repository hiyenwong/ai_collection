---
name: bazaarbench-delegation-safety-in-decentralized-c2c
description: "BazaarBench: Delegation Safety in Decentralized C2..."
tags: [cs.MA, cs.AI, cs.LG]
source: arxiv
arxiv_id: 2610.06748v1
utility: 0.99
published: 2026-10-05
---

# BazaarBench: Delegation Safety in Decentralized C2C Marketplaces Run by LLM Agents

**Authors:** Ziyan Wang, Shuqing Shi, James Oldfield, Samuele Marro, Jialin Yu...
**Published:** 2026-10-05
**arXiv:** [2610.06748v1](https://arxiv.org/abs/2610.06748v1)
**Categories:** cs.MA, cs.AI, cs.LG
**Utility Score:** 0.99

## Abstract

In decentralized consumer-to-consumer (C2C) marketplaces, people list goods, negotiate with strangers, and rate one another, so trust rests on reputation. Large language model (LLM) agents now act for users, raising risks to their money, privacy, and reputation. We introduce BazaarBench, a simulated C2C marketplace and benchmark for evaluating the safety of these agents. It tracks ownership, item condition, and commitments across transactions, combining record checks with rubric-based LLM judgments to identify six failure types across five stages. We run three base markets for 30 simulated days, each with 100 agents using one model and inventories drawn from a public eBay sample. Across 45 continuations, we evaluate five models under ordinary instructions, deadline pressure, or adversarial instructions to exploit other traders. Each continuation runs for seven simulated days from a copy of a market's day-30 state. The tested model controls the same 20 selected agents, retaining their personas, inventories, and histories, while the other 80 keep the base model. All five models attempt to promise the same item to multiple buyers under ordinary instructions. Adding targets and deadlines increases these attempts for every model. Under adversarial instructions, the share of tested sellers' committed transactions completed despite unavailable items or overstated conditions rises from 15.4% to 33.4%, reaching 55.5% for GPT-5.4. Averaged across models and markets, simulated weekly ea

## Key Contributions

- Novel research in cs.MA, cs.AI
- Published 2026-10-05

## Activation

bazaarbench, delegation, safety, decentralized, marketplaces, agents
