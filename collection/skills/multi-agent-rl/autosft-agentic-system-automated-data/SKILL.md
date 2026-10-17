---
name: autosft-agentic-system-automated-data
description: "AutoSFT: An Agentic System for Automated Data Research in Supervised Fine-Tuning"
tags: [arxiv, paper, multi-agent-rl]
arxiv_id: "2610.22194"
utility: 0.97
date: "2026-10-17"
---

# AutoSFT: An Agentic System for Automated Data Research in Supervised Fine-Tuning

**arXiv:** [2610.22194](https://arxiv.org/abs/2610.22194)
**Authors:** Bingxiang He, Pengqi Sun, Shihao Peng, Shaoxuan Li, Huiyu Xiao...
**Published:** 2026-10-15
**Categories:** cs.AI, cs.CL
**Utility Score:** 0.97

## Abstract

Language model agents increasingly automate post-training, but when given the full training stack they converge on supervised fine-tuning and spend most effort revising training data. Existing systems give the agent one kind of control, selecting rows from a fixed pool or calling a generator, whereas a human data engineer adjusts proportions, prunes, repairs, replaces and synthesizes the data. We design a data action space for these changes and ask whether an automated system can make the full range rather than one of them, and what structure that requires. We first run this loop with a single agent, and it reaches only one action, adjusting category proportions, while its context fills with execution output and is discarded mid-search. We therefore introduce \textbf{AutoSFT}, a multi-agent system where a meta agent separates execution from analysis, gathers proposals from independent angles, and calls a synthesis subagent for capabilities the pool cannot cover, with the model, the trainer, and the budget fixed within each comparison. Adding each component in turn helps: the executor halves context loss, the analysis subagents lift the best IFEval by $+6.5$, and synthesis adds $+3.4$ IFEval and $+2.9$ IFBench. The same loop transfers to code, where analysis adds $+3.7$ MBPP+ over a single agent that does not improve. Every result comes from runs that retrain from the base model each round, so each component's effect is individually attributable. Our findings suggest that automating SFT data research depends more on covering diverse data actions than on a stronger single action.

## Key Contributions

- Novel research in cs.AI, cs.CL
- High utility score (0.97) indicating significant research value

## Activation

autosft, agentic, system, automated, data, research, supervised, finetuning

## Notes

Added by arXiv cron job on 2026-10-17.
