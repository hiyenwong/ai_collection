---
name: same-simulation-different-evidence-where-retrieved
description: "Same Simulation, Different Evidence: Where Retriev..."
tags: [cs.AI]
source: arxiv
arxiv_id: 2610.26836v1
utility: 1.0
published: 2026-10-19
---

# Same Simulation, Different Evidence: Where Retrieved Tool Output Costs LLM Agents Accuracy

**Authors:** Ke Zhang, Sahchit Chundur, Jerry Peprah Owusu, Mohammad Javad Abdolhosseini Qomi, Maziar Raissi
**Published:** 2026-10-19
**arXiv:** [2610.26836v1](https://arxiv.org/abs/2610.26836v1)
**Categories:** cs.AI
**Utility Score:** 1.0

## Abstract

LLM agents that compute the right answer can still answer wrongly. Agent harnesses increasingly keep long tool outputs out of the context window, saving them to files that the agent searches or reads on demand. We ask where this costs accuracy with a real scientific tool: PHREEQC, a widely used geochemistry simulator from the USGS, whose reports reach 846.8k characters and whose determinism lets every printed value be traced. Agents use it to answer 158 execution-verified multiple-choice items. When agents read the simulator's report through a section index rather than in context, GPT-5.1 and GPT-5.2 lose 11.3 and 7.9 points of accuracy, while Claude Opus 4.6 and Claude Sonnet 4.6 show no detectable cost. Re-running all 11,007 logged simulator calls shows that both GPT models compute the keyed value about as often as before; what changes is the evidence they answer from. Under retrieval they often skip the report, answer from their own higher-precision output files, and misround to a neighboring option, a failure we call evidence substitution. With the simulation held fixed, retrieval still costs GPT-5.2 9.4 points. For GPT-5.4, more frequent correct simulations mask an evidence-use loss of about ten points, leaving a net change indistinguishable from zero. Naming the authoritative output raises accuracy by 6.3-7.9 points over plain retrieval for the three GPT models; for GPT-5.1 and GPT-5.2, inlining outputs that fit works as well, while asking for correct rounding does not.

## Key Contributions

- Novel research in cs.AI
- Published 2026-10-19

## Activation

same, simulation, different, evidence, where, retrieved, tool, output, costs, agents
