---
name: reki-registering-knowledge-vlas
description: "REKI: Registering Knowledge in VLAs"
tags: [arxiv, paper, nlp-llm]
arxiv_id: "2610.22178"
utility: 0.96
date: "2026-10-17"
---

# REKI: Registering Knowledge in VLAs

**arXiv:** [2610.22178](https://arxiv.org/abs/2610.22178)
**Authors:** Juliette Marrie, Paul Pacaud, Adrien Ramanana Rahary, Shizhe Chen, Moritz Böhle
**Published:** 2026-10-15
**Categories:** cs.RO, cs.CV, cs.LG
**Utility Score:** 0.96

## Abstract

We introduce REKI, a 2.4B vision-language-action model (VLA) pretrained exclusively on public data that sets a new Pareto frontier between performance and model size: on LIBERO-Plus, RoboTwin Clean2Rand and RoboCasa365, it is outperformed only by models about twice its size. REKI consists of a vision-language model (VLM) followed by a flow-matching action expert, and is pretrained on a curated mixture of public robot, egocentric human and vision-language data. Additionally, we endow it with a memory that gives the policy access to its recent past at negligible cost: a few register tokens in the action expert summarise the output of the VLM at each frame and persist in the expert's cache. This memory improves success in simulation and on real robots, and makes oscillations between poses about four times rarer. REKI uses a simple model design and training paradigm, and is optimised to be efficient at training and inference. We release the full code across data curation, training, inference and evaluation, deployment, and all pretrained and finetuned model weights: https://github.com/kyutai-labs/reki.

## Key Contributions

- Novel research in cs.RO, cs.CV
- High utility score (0.96) indicating significant research value

## Activation

reki, registering, knowledge, vlas

## Notes

Added by arXiv cron job on 2026-10-17.
