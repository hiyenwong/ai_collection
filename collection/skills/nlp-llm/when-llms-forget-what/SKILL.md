---
title: "When LLMs Forget What They Believe: Characterizing State Integrity Collapse in Long-Horizon Dialogues"
authors: "Yancheng Zhu, Yifan Yuan"
published: "2026-10-22"
arxiv_id: "2610.31314v1"
url: "https://arxiv.org/abs/2610.31314v1"
categories: ["cs.CL", "cs.AI"]
utility_score: 0.89
tags: [arxiv, paper, nlp-llm]
---

# When LLMs Forget What They Believe: Characterizing State Integrity Collapse in Long-Horizon Dialogues

**Authors:** Yancheng Zhu, Yifan Yuan
**Published:** 2026-10-22
**arXiv:** [2610.31314v1](https://arxiv.org/abs/2610.31314v1)
**Categories:** cs.CL, cs.AI
**Utility Score:** 0.89

## Abstract

Large language models can repeat an instruction while failing to keep obeying it. We study this recall-compliance dissociation in long-horizon dialogue and define State Integrity Collapse: a model preserves a stated constraint in memory but stops applying it to later turns. We introduce StateTrack-Bench, a controlled suite of conversations covering numerical, format, role/persona, factual-memory, and logical-rule constraints. Across seven provider-pinned model snapshots and five dialogue-depth probes, strict joint retention ranges from 62.4% to 100.0%, with degradation concentrated in symbolic constraints and in one especially brittle model. A forked recall audit shows that 88.6% of observed failures are behavioral-drift failures rather than ordinary forgetting; excluding the brittle outlier preserves this diagnosis (84.4% of failures). Extended evaluations at depths up to 50 turns confirm that the dissociation persists beyond the core benchmark, while Structured State Anchoring recovers up to 24.4 points on immutable constraints. The results show that reliability cannot be inferred from single-turn instruction following alone; evaluation must track whether remembered constraints remain operational as dialogue state grows. Code and artifacts are available at: https://github.com/xzzvsxd/StateTrack.

## Key Contributions

- Research paper from arXiv, auto-processed by Hermes cron job
- Utility score >= 0.85 indicates high relevance for AI/ML research
- Category: nlp-llm

## Related Skills

Check the `nlp-llm` directory for related papers and tools.
