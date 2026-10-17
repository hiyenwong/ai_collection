---
name: language-security-surface-agent-guards
description: "Language Is a Security Surface for Agent Guards"
tags: [arxiv, paper, multi-agent-rl]
arxiv_id: "2610.22244"
utility: 0.85
date: "2026-10-17"
---

# Language Is a Security Surface for Agent Guards

**arXiv:** [2610.22244](https://arxiv.org/abs/2610.22244)
**Authors:** Hasan Demirkiran, Jens Ernstberger
**Published:** 2026-10-15
**Categories:** cs.CR, cs.AI, cs.CL, cs.LG
**Utility Score:** 0.85

## Abstract

Step-level guards decide, before each tool call, whether an agent's next action is safe given the user's request and the trajectory so far. Users write those requests in many languages, while guard prompts and the benchmarks on which purpose-built guards are trained and evaluated are English. We ask whether a guard's verdict depends on the language of the request. We build LinguaGuardBench from the 1,220 labelled steps of TS-Bench AgentDojo-Traj: we translate only the user instruction into German, French, Turkish, Swahili and Amharic, and keep every tool call, observation and label byte-identical, so any change in a verdict is attributable to language alone. Six English rewordings and a whitespace placebo serve as controls, and managed guards are run three times to measure their noise. Across 19 guards, from frontier APIs to 4B open models and four purpose-built agent guards, most open, small and purpose-built guards change verdicts under translation beyond their own noise floor, and the effect grows with the rarity of the language: among the nine guards below 13B parameters, the mean placebo-adjusted flip rate rises from +1.5 pp on French to +4.4 pp on Amharic. Purpose-built guards are the most sensitive. The direction of the damage tends to follow guard size: open guards of 12-30B parameters block more benign steps (up to +5.0 pp false positives), and every significant loss of recall is in a guard below 10B (up to -7.4 pp). Frontier guards shift by at most about one point; the strongest, Gemini 3.8 Flash, returns identical verdicts with and without the request. The damage is concentrated in a few instructions and, in a post-hoc analysis, falls on steps where the agent's reasoning restates the English request, consistent with guards reacting to inconsistency between channels. English paraphrase moves every guard less than translation does. We release the benchmark and all 489k verdicts.

## Key Contributions

- Novel research in cs.CR, cs.AI
- High utility score (0.85) indicating significant research value

## Activation

language, security, surface, agent, guards

## Notes

Added by arXiv cron job on 2026-10-17.
