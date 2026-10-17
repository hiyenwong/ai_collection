---
name: librarian-agents-training-llms-curate
description: "Librarian Agents: Training LLMs to Curate Long-Context Workspaces that Anticipat"
tags: [arxiv, paper, multi-agent-rl]
arxiv_id: "2610.22273"
utility: 0.99
date: "2026-10-17"
---

# Librarian Agents: Training LLMs to Curate Long-Context Workspaces that Anticipate Future Queries

**arXiv:** [2610.22273](https://arxiv.org/abs/2610.22273)
**Authors:** Anikait Singh, Teresa Zhang, Yoonho Lee, Roshen Sanjay Nair, Aviral Kumar...
**Published:** 2026-10-15
**Categories:** cs.LG, cs.AI, cs.CL
**Utility Score:** 0.99

## Abstract

Reasoning over long document contexts remains a challenge for large language models (LLMs). Standard retrieval methods are inherently reactive, bottlenecking agents with complex, cross-document reasoning at inference time, while precomputed structures like knowledge graphs often fall short because they rely on rigid heuristics. Instead, can we allow agents to perform anticipatory directed curation: learning to proactively reorganize unstructured corpora prior to inference to efficiently serve diverse future queries. We build on a key asymmetry in modern agentic harnesses (e.g., Claude Code): while LLM agents are adept at navigating existing filesystems to solve an immediate task, they are rarely trained to construct reusable workspaces for future use. To instantiate this capability, we introduce Librarian Agents, a framework in which a builder agent transforms raw documents into a hierarchical filesystem of synthetic files and reference links, which forms a workspace tailored for a downstream answering agent. We formulate workspace construction as a Markov decision process and optimize the builder policy via reinforcement learning to directly maximize downstream answering accuracy. Empirically, Librarian Agents outperforms the strongest retrieval and precomputation baselines by 33 percentage points on BrowseComp-Plus, amortizes upfront construction costs across repeated queries, and generalizes zero-shot to unseen domains on BRIGHT with a 31-point average accuracy improvement.

## Key Contributions

- Novel research in cs.LG, cs.AI
- High utility score (0.99) indicating significant research value

## Activation

librarian, agents, training, llms, curate, longcontext, workspaces, anticipate, future, queries

## Notes

Added by arXiv cron job on 2026-10-17.
