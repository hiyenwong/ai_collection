# Humains-Junior: A 3.8B Language Model Achieving GPT-4o-Level Factual Accuracy by Directed Exoskeleton Reasoning

**arXiv ID:** 2510.25933
**Authors:** Nissan Yaron, Dan Bystritsky, Ben-Etzion Yaron
**Published:** 2025-10-29T20:12:36Z
**Abstract:**
We introduce Humans-Junior, a 3.8B model that matches GPT-4o on the FACTS Grounding public subset within a $\pm 5$ pp equivalence margin.
  Results. On Q1--Q500 under identical judges, GPT-4o scores 73.5% (95% CI 69.5--77.2) and Humans-Junior 72.7% (95% CI 68.7--76.5); the paired difference is 0.8 pp (bootstrap 95% CI $-3.1$ to $+4.7$; permutation $p = 0.72$; Cohen's $d = 0.023$). TOST establishes equivalence at $\pm 5$ pp (not at $\pm 3$ pp). When purchased as managed APIs, Humans-Junior's base model (Phi-3.5-mini-instruct) is $\approx 19\times$ less expensive than GPT-4o on Microsoft AI Foundry pricing; self-hosted or edge deployments can drive incremental inference cost toward zero. Measured vs estimated pricing sources are tabulated in Appendix E.
  Method. Our approach combines minimal directed "Exoskeleton Reasoning" scaffolds with behavioral fine-tuning that teaches protocol compliance (epistemic discipline) rather than domain answers. Fine-tuning alone adds little; combined, they synergize (+17.7 pp, $p < 0.001$) and reduce variance ($\approx 25\%$). In prompt-only settings on frontier models (Q1--Q100; non-comparable), directed reasoning improved GPT-4o by +11.8 pp to 85.3% and Gemini-2.5-Pro by +5.0 pp to 93.3% (baseline 88.3%, $n = 100$); see Section~5.
  TL;DR. A 3.8B model achieves GPT-4o-level FACTS accuracy (equivalent within $\pm 5$ pp on Q1--Q500). Cloud pricing shows $\approx 19\times$ lower cost versus GPT-4o, and self-hosted/edge deployments can approach zero marginal cost. Pricing sources are listed in Appendix E. Frontier prompt-only gains (Q1--Q100; non-comparable) and optimized-prompt exploratory results under earlier judges are summarized in Appendix F.
  Keywords: Small Language Models, Factual Grounding, Directed Reasoning, Fine-Tuning, Model Alignment, Cost-Efficient AI

## Skill Description

This skill is generated from the arXiv paper: Humains-Junior: A 3.8B Language Model Achieving GPT-4o-Level Factual Accuracy by Directed Exoskeleton Reasoning (2510.25933).

## How to Use

[To be filled in by the user or by future automation]

## References

- [arXiv:2510.25933](http://arxiv.org/abs/2510.25933v1)
