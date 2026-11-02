---
name: secpo-principled-adversarial-training-for-prompt
description: "SecPO: Principled Adversarial Training for Prompt ..."
tags: [cs.CR, cs.AI]
source: arxiv
arxiv_id: 2610.41998v1
utility: 0.87
published: 2026-10-30
---

# SecPO: Principled Adversarial Training for Prompt Injection Security

**Authors:** Sizhe Chen, Yibo Peng, Jaewon Chang, Chawin Sitawarin, David Wagner
**Published:** 2026-10-30
**arXiv:** [2610.41998v1](https://arxiv.org/abs/2610.41998v1)
**Categories:** cs.CR, cs.AI
**Utility Score:** 0.87

## Abstract

Recognized as a top threat to AI agents, prompt injection allows instructions from untrusted data (email, documents, websites) to manipulate the agent's operation. The existing best-defended LLM, Meta-SecAlign, is trained with the DPO loss but still suffers from attack success rates (ASRs) approaching 100% under adaptive prompt injections. One reason is that DPO anchors the model around the undefended reference model, which is insecure. We show an idealized reference model---an injection-invariant, utility-preserving oracle---can nevertheless be approximated, as its output distribution in training is interestingly accessible. This new observation motivates a theoretically principled SecPO loss. Another Meta-SecAlign shortcoming is that it trains on weak simulated attacks. We implement an efficient adversarial training (AT) pipeline that synthesizes strong injected inputs (best@240), and train the model on them. Our AT reduces ASRs by 1.5-14.5$\times$ across three SoTA adaptive attacks, compared with Meta-SecAlign; the SecPO loss reduces them by a further 2.4-4.6$\times$ compared with using DPO loss. In agentic workflows, our SecPO + AT Qwen3.6-27B is much more secure than Meta-SecAlign: 8.8% vs. 78.8% AgentDojo ASR@800 under the AttackerMovesSecond attack. Moreover, our defended model shows no noticeable reduction in benign utility in nine benchmarks covering agentic tool calling, instruction following, science, and math. We release our $\href{//github.com/Sizhe-Chen/SecPO}{\

## Key Contributions

- Novel research in cs.CR, cs.AI
- Published 2026-10-30

## Activation

secpo, principled, adversarial, training, prompt, injection, security
