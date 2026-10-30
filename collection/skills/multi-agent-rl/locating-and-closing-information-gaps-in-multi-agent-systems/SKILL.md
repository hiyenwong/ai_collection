---
name: locating-and-closing-information-gaps-in-multi-agent-systems
description: "Locating and Closing Information Gaps in Multi-Agent Sy..."
tags: [cs.AI]
source: arxiv
arxiv_id: 2610.40186v1
utility: 0.97
---

# Locating and Closing Information Gaps in Multi-Agent Systems

**arXiv ID:** [2610.40186v1](https://arxiv.org/abs/2610.40186v1)
**Published:** 2026-10-29
**Authors:** Yaxin Gong, Chongming Gao, Gangyi Zhang, Chenxiao Fan, Leyang Shen...
**Utility Score:** 0.97

## Abstract

Multi-step Web tasks often require several LLM agents to gather and combine evidence. The communication graph of a fixed workflow restricts which agents can read each other's outputs: evidence retrieved by one agent may never reach the agent that needs it, leaving an information gap and an incomplete or incorrect answer. Adding a connection can deliver the missing evidence, but can also lead the receiver to adopt an incorrect upstream conclusion that displaces a correct answer; the final output alone does not separate the two. We propose Selective Probing and Link Insertion for Closing information gaps in multi-agent Execution (SPLICE), which locates information gaps per query and decides what to adopt after adding an edge. After the original workflow runs, SPLICE uses the query and node outputs to locate a possible gap, adds one directed edge from a source to a receiver to deliver the relevant evidence, and re-executes the receiver and affected downstream nodes, producing a candidate answer. The adoption decision reads both the final answers of the two runs and the process changes the edit caused inside the workflow: how far the receiver moved, where its new content came from, and whether the change reached the final answer. A selector trained on these process features chooses between adopting the candidate answer and retaining the original. On five benchmarks, SPLICE raises the task score on Web tool use by 8.0% and the mean score on four reasoning and planning benchmarks b

## Key Contributions

- Research in multi-agent-rl domain with practical applications
- Published in top arXiv categories: cs.AI

## Activation

cs.AI, arxiv paper, utility 0.97
