---
name: rag-compositionality
description: "RAG Compositionality: tests whether isolated gains from RAG techniques (embedding, chunking, retrieval, reranking, etc.) survive composition."
paper_id: 2610.29722
utility_score: 0.80
categories: [cs.CL, cs.AI]
date: 2026-10-21
tags: [rag, retrieval-augmented-generation, compositionality, pipeline-evaluation]
---

# Retrieval Augmented Generation Compositionality

## Key Contribution
Tests whether isolated gains from modern RAG pipeline techniques (embedding, chunking, retrieval, reranking, query augmentation, context compression, agentic verification) survive composition. Evaluates whether retrieval quality and answer faithfulness compose predictably.

## Core Method
- **Problem**: Modern RAG pipelines combine many techniques, but each is typically evaluated in isolation. It's unclear whether gains compose or interact negatively.
- **Techniques evaluated**: Embedding models, chunking strategies, retrieval methods, reranking, query augmentation, context compression, agentic verification
- **Evaluation framework**: 
  - Test each technique in isolation
  - Test pairwise and full composition
  - Measure retrieval quality (recall, precision) and answer quality (faithfulness, relevance)
  - Identify interaction effects (positive/negative composition)
- **Key questions**: 
  - Do isolated gains survive when combined?
  - Are there interaction effects that degrade performance?
  - What's the optimal pipeline configuration?

## Why It Matters
- First systematic study of RAG pipeline compositionality
- Practical guidance for building production RAG systems: which techniques compose well, which conflict
- Reveals that some "best practices" may not compose — e.g., aggressive chunking + aggressive compression may lose critical context
- Helps avoid suboptimal pipeline designs where techniques cancel each other out

## Application Scenarios
- Designing production RAG pipelines
- Debugging RAG systems where individual components work but full pipeline underperforms
- Choosing which techniques to combine (and which to avoid)
- Understanding trade-offs in pipeline complexity vs. performance

## Implementation Notes
- Techniques tested: embedding (dense/sparse), chunking (fixed/semantic), retrieval (top-k/threshold), reranking (cross-encoder/LLM), query augmentation (HyDE/step-back), context compression (extractive/abstractive), agentic verification (self-check/external)
- Evaluation: retrieval metrics (recall@k, MRR) + generation metrics (faithfulness, relevance, hallucination rate)
- Key finding: not all gains compose — some techniques interact negatively
- Recommendation: test composition on your domain, don't assume isolated gains carry over
