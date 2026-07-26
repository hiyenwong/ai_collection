---
name: gradrag-cross-component-prompt-adaptation-for-coordinated-multi
description: 'GRADRAG: Cross-Component Prompt Adaptation for Coordinated Multi-Agent RAG'
metadata:
  {
    "arxiv_id": "2607.21324",
    "utility": 1.0,
    "date_added": "2026-07-26"
  }
---

# GRADRAG: Cross-Component Prompt Adaptation for Coordinated Multi-Agent RAG

arXiv: 2607.21324  
Published: 2026-07-23  
Utility: 1.0

## Summary
Retrieval-Augmented Generation (RAG) systems increasingly employ multiple LLM agents. Yet, most prior work optimizes components in isolation rather than coordinating improvements across the pipeline. We introduce GRADRAG, a framework for cross-component prompt adaptation that models the RAG pipeline as a computational graph and propagates structured evaluation feedback to update upstream agents. An Evaluator critiques downstream answers and supporting evidence, producing actionable feedback that a Prompt Optimizer uses to iteratively update adaptive agents, such as retrievers, graph constructors, and answerers. The Evaluator also triggers early stopping when the output is deemed satisfactory. We evaluate GRADRAG on the SQUALITY and QMSUM benchmarks under two retrieval paradigms: flat chunk-based retrieval using IRCoT-style query refinement (Trivedi et al., 2023), and graph-based retrieval that constructs and iteratively enriches an entity-relation graph from the document. Across both settings, GRADRAG consistently outperforms one-step refinement baselines that update only the final generator, achieving a 12-15 percentage point net preference margin in LLM-judged pairwise comparisons, with most gains realized within two refinement iterations....

## Key Information
- **Title**: GRADRAG: Cross-Component Prompt Adaptation for Coordinated Multi-Agent RAG
- **Authors**: [Extract from entry]
- **Primary Category**: cs.AI

## Potential Skill Application
This paper presents research relevant to AI agent systems. Consider extracting methodologies, algorithms, or frameworks for skill development.

## Reference
- arXiv: https://arxiv.org/abs/2607.21324
