---
name: explore-or-confirm-llm-agents-misallocate
description: "Explore or Confirm? LLM Agents Misallocate Measure..."
tags: [cs.AI, cs.MA]
source: arxiv
arxiv_id: 2610.25111v1
utility: 1.0
published: 2026-10-18
---

# Explore or Confirm? LLM Agents Misallocate Measurements Under Noise

**Authors:** Abdul Karim, Matt Keon
**Published:** 2026-10-18
**arXiv:** [2610.25111v1](https://arxiv.org/abs/2610.25111v1)
**Categories:** cs.AI, cs.MA
**Utility Score:** 1.0

## Abstract

As model reasoning gets cheaper, the physical experiment becomes the slow and costly step in discovery. Each experiment returns a noisy reading: a high value can mean a good candidate or a lucky draw. With a fixed budget, an AI agent must keep choosing between exploring a new candidate and confirming a promising one by re-testing it. We measure that choice in Wellocate, a simulated assay campaign with known true values. It is built on a generated landscape and on two real protein datasets, GB1 and PhoQ, scrambled so no model can answer from memory. We test five language models as minimal agents, with no tools and no memory beyond the history in each prompt. They misallocate in both directions. Three over-confirm, spending most of the budget re-testing. On the generated landscape one under-confirms, trusting single readings, and there every model ends with a worse final pick than a basic scripted strategy. Each failure has its own cause. The over-confirmers run short of new candidates worth trying: a list of untried candidates cuts their re-testing and, on real protein data, makes two of them pick much better. A running summary of their readings or a description of the landscape changes it by at most five percentage points. For the under-confirmer, re-testing its top candidates in a final round, replayed on its own campaigns, recovers only about a quarter of what it loses by picking the wrong candidate. This suggests confirmation has to run through the whole campaign. We relea

## Key Contributions

- Novel research in cs.AI, cs.MA
- Published 2026-10-18

## Activation

explore, confirm, agents, misallocate, measurements, under, noise
