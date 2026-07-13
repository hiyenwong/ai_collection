---
name: latent-rag-continuous
description: Shift RAG reasoning and retrieval from discrete language to continuous latent space for ~90% latency reduction. Based on arXiv 2605.06285.
category: llm-reasoning
---

# LatentRAG: Latent Reasoning and Retrieval for Efficient Agentic RAG

## Overview
Agentic RAG generates lengthy intermediate thoughts and subqueries token-by-token, causing substantial latency. LatentRAG shifts both reasoning and retrieval from discrete language space to continuous latent space, reducing inference latency by ~90% while maintaining comparable performance.

## Core Methodology
1. **Latent token generation**: Produce thoughts and subqueries directly from hidden states in a single forward pass (no autoregressive generation)
2. **Latent space alignment**: Align LLMs with dense retrieval models in latent space for retrieval over latent subquery tokens
3. **End-to-end joint optimization**: Train retrieval and reasoning together in latent space
4. **Parallel latent decoding**: Translate latent tokens back to natural language for transparency

## Key Findings
- Single forward pass replaces token-by-token generation
- ~90% inference latency reduction vs explicit agentic RAG
- Performance comparable on 7 benchmark datasets
- End-to-end joint optimization of retrieval and reasoning

## Implementation Steps
1. Extract hidden states from LLM for query encoding
2. Generate latent tokens via linear projection (single forward pass)
3. Align LLM latent space with dense retriever
4. Retrieve documents using latent subquery tokens
5. Jointly optimize retrieval and reasoning end-to-end
6. Add parallel latent decoder for interpretability

## Applicable Use Cases
- Agentic RAG systems needing lower latency
- Multi-step retrieval pipelines
- Real-time QA with complex questions
- Resource-constrained deployment

## Triggers / Keywords
agentic RAG, latent reasoning, retrieval optimization, latency reduction, continuous space, dense retrieval
