---
name: when-the-harness-decides-success-state
description: "When the harness decides success: state that canno..."
tags: [cs.AI, cs.CL, cs.LG]
source: arxiv
arxiv_id: 2610.26632v1
utility: 0.93
published: 2026-10-19
---

# When the harness decides success: state that cannot be re-observed

**Authors:** Raimondas Lencevicius
**Published:** 2026-10-19
**arXiv:** [2610.26632v1](https://arxiv.org/abs/2610.26632v1)
**Categories:** cs.AI, cs.CL, cs.LG
**Utility Score:** 0.93

## Abstract

Agent harnesses decide what a language model sees across turns: they drop old turns, summarize them, or replay the model's own earlier reasoning. We ask when these choices change whether an agent succeeds, not only what it costs, and report three findings. First, in a pre-registered synthetic probe, truncating the context window costs a low-cost reasoning model nothing in success when a needed fact can be looked up again (it looks the fact up instead), but drops its success to chance when the fact cannot be re-observed: the two penalties differ by 92.5 percentage points (90% CI [89.5, 95.5]). A pre-registered replication on one model from a second provider showed the same contrast. Once the fact was lost, that model chose no answer rather than guessing. Second, on ARC-AGI-3, where the benchmark's Standard harness trails its Provider Adapter harness by a wide margin, we decompose that gap one component at a time, for one model on four games. Summarizing old turns instead of dropping them, while keeping the Standard harness's invitation to take notes, recovers 86% of a 63-point gap without replaying the model's reasoning. The same harness without the invitation recovers 43%, and adding the provider's native replay of the model's reasoning recovers the remaining 57%. These are point estimates from one counted run per configuration and game, and the replay share depends on a single run. Third, in the benchmark's published runs and in ours, the Adapter's advantage in the probabili

## Key Contributions

- Novel research in cs.AI, cs.CL
- Published 2026-10-19

## Activation

when, harness, decides, success, state, that, cannot, reobserved
