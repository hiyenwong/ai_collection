---
name: arxiv-2608-20055-echocot-extracting-hidden-chain-of-thought-from-la
description: 'EchoCoT: Extracting Hidden Chain-of-Thought from Large Reasoning Models (arXiv: 2608.20055)'
category: nlp-llm
version: "1.0"
date: 2026-08-22
---

# EchoCoT: Extracting Hidden Chain-of-Thought from Large Reasoning Models

**Authors:** Yiting Qu, Ziqing Yang, Chi Cui, Ye Leng, Junjie Chu, Yang Zhang
**arXiv:** 2608.20055
**Utility:** 1.00
**Published:** 2026-08-20T13:52:07Z
**Link:** http://arxiv.org/abs/2608.20055

## Abstract

Hidden chain-of-thought (CoT) traces, especially those from frontier proprietary large reasoning models (LRMs), are valuable model assets. Yet whether these hidden CoTs can be directly extracted from black-box models remains largely unexplored. In this work, we systematically study whether hidden CoTs can be extracted near-verbatim from black-box LRMs through API interactions. We identify a previously overlooked reasoning replay surface between tool calls and develop EchoCoT, a multi-step attack that iteratively extracts hidden CoTs using API-returned fidelity signals. We further develop an LLM-based optimization framework that automatically searches for an effective universal injection trajectory across various datasets. We evaluate EchoCoT on three open-source and five frontier proprietary LRMs. On open-source LRMs, EchoCoT achieves up to 66.4\% near-verbatim extraction success, with the extracted trace length within 10\% of the target and at least 90\% of tokens exactly matching the target CoT. The same injection trajectory also generalizes to unseen datasets, achieving up to 80\% extraction success under the same criterion. For tested frontier proprietary LRMs, a substantial fraction of extracted CoTs closely align with provider-reported reasoning lengths and available CoT summaries. EchoCoT can also extract very long CoTs: on Gemini-2.5, it extracts 33,463 tokens from a 32,948-token target. These results establish hidden-CoT extraction as a practical security risk and highlight the need to better protect hidden CoT assets.

## Summary

This skill encapsulates the key contributions and methods from the arXiv paper "EchoCoT: Extracting Hidden Chain-of-Thought from Large Reasoning Models". 
The paper presents novel ideas in nlp-llm that can be applied to agent systems.

## How to Use

1. Review the paper's methodology and findings.
2. Identify applicable components for your agent workflow.
3. Implement the core techniques as described in the paper.
4. Validate improvements in your specific use case.

## Pitfalls

- Ensure the paper's assumptions match your agent's environment.
- Validate implementation details before deployment.
- Consider computational complexity and resource requirements.

## References

- arXiv:2608.20055
