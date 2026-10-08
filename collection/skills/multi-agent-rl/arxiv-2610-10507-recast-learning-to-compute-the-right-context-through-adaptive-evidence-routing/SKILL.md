---
name: arxiv-2610-10507-recast-learning-to-compute-the-right-context-through-adaptive-evidence-routing
description: 'RECAST: Learning to Compute the Right Context through Adaptive Evidence Routing (arXiv: 2610.10507)'
metadata:
  {
    "arxiv_id": "2610.10507",
    "utility": 1.0,
    "title": "RECAST: Learning to Compute the Right Context through Adaptive Evidence Routing",
    "authors": "Yilun Hao, Krishna Sayana, Isabella Ye, James S Ren, Sukhdeep Sodhi...",
    "url": "https://arxiv.org/abs/2610.10507v1",
    "categories": ["cs.AI"],
    "published": "2026-10-07"
  }
---

# RECAST: Learning to Compute the Right Context through Adaptive Evidence Routing

**arXiv ID:** 2610.10507
**Authors:** Yilun Hao, Krishna Sayana, Isabella Ye, James S Ren, Sukhdeep Sodhi...
**URL:** https://arxiv.org/abs/2610.10507v1
**Utility Score:** 1.00
**Published:** 2026-10-07
**Categories:** cs.AI

## Summary

Large language models are increasingly applied to tasks grounded in long, heterogeneous information sources. Conventional Retrieval-Augmented Generation (RAG) relies on fixed similarity-based retrieval, while agentic variants adapt queries and tool use but remain largely retrieval-centric. However, in many tasks, the evidence required for a solution is not explicitly present in any single source item. Instead, it must be derived through filtering, aggregation, or computation across multiple source items. In this work, we introduce RECAST (Routing Evidence through Computation, Access, and Synthesized Tools), a learned framework that formulates evidence construction as a sequential decision process over heterogeneous retrieval and computation operations, allowing evidence to be actively derived rather than merely retrieved. A lightweight RouterLM iteratively selects and formulates primitive operations or specifies customized operations for a frozen CompilerLM to translate into executable code. Once it judges the evidence sufficient, RouterLM passes the accepted evidence to a frozen AnswerLM to produce the final solution. We train RouterLM with supervised fine-tuning (SFT) followed by group relative policy optimization (GRPO). Across six heterogeneous benchmark families, RECAST achieves a mean success rate of 75.6%, outperforming the strongest large-model baseline by 15.9%. Moreover, training enables the Qwen3.5-9B RouterLM to outperform a training-free Gemini 3.5 Flash RouterLM by 5.0%. On three held-out benchmarks, RECAST improves over the strongest baseline by 15.0% on average, demonstrating strong zero-shot generalization across tasks and heterogeneous source representations.

## Usage

This skill was automatically generated from the arXiv paper. It can be used to reference the paper's concepts, methodologies, or findings in agent workflows.

## References

- arXiv: https://arxiv.org/abs/2610.10507v1
