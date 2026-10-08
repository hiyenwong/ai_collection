---
name: arxiv-2610-10455-phrbench-a-behavioral-evaluation-of-post-hallucination-reasoning-in-llms
description: 'PHRBench: A Behavioral Evaluation of Post-Hallucination Reasoning in LLMs (arXiv: 2610.10455)'
metadata:
  {
    "arxiv_id": "2610.10455",
    "utility": 0.89,
    "title": "PHRBench: A Behavioral Evaluation of Post-Hallucination Reasoning in LLMs",
    "authors": "Linghao Meng, Feng He, Xuan Yang, Junyuan Mao, Pinze Ren...",
    "url": "https://arxiv.org/abs/2610.10455v1",
    "categories": ["cs.CL", "cs.AI"],
    "published": "2026-10-07"
  }
---

# PHRBench: A Behavioral Evaluation of Post-Hallucination Reasoning in LLMs

**arXiv ID:** 2610.10455
**Authors:** Linghao Meng, Feng He, Xuan Yang, Junyuan Mao, Pinze Ren...
**URL:** https://arxiv.org/abs/2610.10455v1
**Utility Score:** 0.89
**Published:** 2026-10-07
**Categories:** cs.CL, cs.AI

## Summary

Hallucinated information can propagate through multi-stage LLM systems and become part of the context for subsequent reasoning. Existing studies of post-hallucination reasoning (PHR) mainly characterize changes in final outcomes and aggregate reasoning dynamics, leaving how models resolve hallucinated premises at the response level insufficiently understood. In this work, we introduce PHRBench, a controlled benchmark for behaviorally structured PHR across four domains and 18 large language models. PHRBench characterizes each reasoning trajectory independently of final-answer correctness through Hallucination Compliance, Hallucination Avoidance, and Heuristic Correction, and defines an insightful trajectory as successful correction that ultimately reaches the correct answer. Across 4820 controlled instances, we find that successful recovery remains relatively rare and is associated with more frequent belief updates along the reasoning trajectory. We further find that properties of the hallucinated prompt contain substantial predictive signal for successful recovery, with a lightweight predictor achieving an AUROC of 0.847. These findings provide a behavioral view of post-hallucination reasoning, characterizing how LLMs resolve erroneous context and when successful recovery is likely to occur.

## Usage

This skill was automatically generated from the arXiv paper. It can be used to reference the paper's concepts, methodologies, or findings in agent workflows.

## References

- arXiv: https://arxiv.org/abs/2610.10455v1
