---
name: llm-judge-reliability-audit
description: Comprehensive reliability audit of LLM-as-a-Judge across models, prompts, orders, temperatures, and repetitions.
tags: [llm-evaluation, reliability, judge-models, benchmarking, prompt-engineering]
---

# LLM Judge Reliability

## Paper Metadata

- **arXiv ID**: 2610.12083
- **Title**: LLM Judge Reliability
- **Categories**: cs.CL, cs.AI, cs.LG
- **Utility Score**: 0.88
- **Date**: 2026-10-10
- **Link**: https://arxiv.org/abs/2610.12083

## Key Contributions

- Stress-tests 6 frontier models as judges across 4 benchmarks, 5 prompt formats, 2 ordering schemes, 3 temperatures, and 10 repetitions.
- Quantifies judge reliability as a function of prompt design, temperature, and response ordering, revealing substantial variance.
- Identifies which combinations of model, prompt, and temperature yield stable judgments suitable for automated evaluation pipelines.
- Provides actionable guidelines for deploying LLM-as-a-Judge in production evaluation systems.

## Core Methodology

The study treats LLM-as-a-Judge as a measurement instrument and evaluates its reliability using standard psychometric principles. Judges are probed across multiple axes: different prompt templates (zero-shot, few-shot, chain-of-thought, rubric-based, pairwise), different orderings of candidate responses, and different sampling temperatures.

For each configuration, the authors measure agreement across 10 repetitions and compute intra-class correlation coefficients to assess consistency. The analysis reveals that prompt format and temperature interact strongly: some prompts are robust to temperature variation while others degrade sharply.

The work demonstrates that LLM judges are not interchangeable and that reliability must be validated per-use-case rather than assumed from model capability alone. The findings inform both the design of evaluation harnesses and the interpretation of leaderboard results derived from LLM judges.

## Relevance to ai-safety-eval

Directly addresses the trustworthiness of automated evaluation systems. Critical for anyone deploying LLM-as-a-Judge for safety benchmarking, RLHF reward modeling, or content moderation, where unreliable judgments can propagate errors at scale.

## Reference

- Paper: https://arxiv.org/abs/2610.12083
