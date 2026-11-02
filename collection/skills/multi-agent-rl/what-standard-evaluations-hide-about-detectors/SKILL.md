---
name: what-standard-evaluations-hide-about-detectors
description: "What Standard Evaluations Hide About Detectors of ..."
tags: [cs.CR, cs.LG]
source: arxiv
arxiv_id: 2610.41803v1
utility: 0.87
published: 2026-10-30
---

# What Standard Evaluations Hide About Detectors of Hijacked LLM Agents: Rare Attacks, Unseen Tools and Benchmark Transfer

**Authors:** Mahmoud Abbasi, Juan M. Núñez V., Amin Shahraki
**Published:** 2026-10-30
**arXiv:** [2610.41803v1](https://arxiv.org/abs/2610.41803v1)
**Categories:** cs.CR, cs.LG
**Utility Score:** 0.87

## Abstract

Detectors can flag hijacked large language model (LLM) agents from the traces of the tools they call. In the eleven evaluations we audited, attacks or anomalies make up 16% to 86% of the test samples, no evaluation varies that share, and six report no test on data from a second benchmark or source. We ask what such evaluations hide. On the AgentDrift and AgentDojo benchmarks we test trained detectors that read tool identities, behavior, call sequences, step embeddings or text, and a released LLM action monitor, AlignmentCheck, with thresholds fixed on training data or set by the monitor's released decision rule. First, at a 2% attack rate a detector with an area under the receiver operating characteristic curve (AUROC) of 0.879 reaches a precision of 0.076, and the mix of negatives alone moves that precision between 0.039 and 0.117. Second, as tool coverage, the share of test tool calls whose tool was seen in training, falls, detector rankings cross near 50% coverage and reverse below it, because unseen tools map to inputs that training never reached. Dropout on tool inputs largely removes the reversal. Third, no detector trained on AgentDrift ranks AgentDojo traces better than chance (AUROC 0.47 to 0.52), including one that reaches 0.996 within AgentDojo. The monitor, trained on neither, reaches 0.930, but with its open backbone its released decision rule would still mostly raise false alerts at a 2% attack rate (precision 0.096). We turn these findings into a checklist for 

## Key Contributions

- Novel research in cs.CR, cs.LG
- Published 2026-10-30

## Activation

what, standard, evaluations, hide, about, detectors, hijacked, agents, rare, attacks
