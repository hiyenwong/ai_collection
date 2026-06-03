---
name: stepwise-reasoning-subgraph
category: research
created: "2026-05-19"
source: "arXiv:2605.16117v1"
description: Stepwise reasoning framework that builds query-specific subgraphs from external knowledge bases to ground intermediate reasoning steps, improving LLM reasoning accuracy and factual reliability.
tags: [llm, reasoning, knowledge-graph, subgraph, multi-step]
---

# SGR: Stepwise Reasoning with External Subgraph Generation

**Source**: arXiv:2605.16117v1 - "SGR: A Stepwise Reasoning Framework for LLMs with External Subgraph Generation"

## Summary

Enhances LLM reasoning by grounding intermediate steps in structured external knowledge. Constructs query-specific subgraphs from knowledge bases and guides the model to reason progressively over them, combining multiple reasoning trajectories for the final prediction.

## Core Methodology

### Three-Stage Pipeline
1. **Subgraph Construction**: Build a query-specific subgraph from external knowledge bases
   - Extracts entities and relations relevant to the input question
   - Filters out irrelevant or noisy knowledge
2. **Progressive Reasoning**: Guide the LLM to reason step-by-step over the subgraph structure
   - Each step grounded in structured external knowledge
   - Model concentrates on relevant entities, relations, and supporting evidence
3. **Trajectory Combination**: Combine multiple reasoning trajectories to produce the final prediction
   - Reduces reliance on any single reasoning path
   - Improves robustness and factual reliability

### Key Insight
LLMs trained on large text corpora generate irrelevant, noisy, or factually inconsistent content during complex reasoning. Grounding intermediate steps in structured knowledge mitigates this.

## When to Use
- LLM reasoning on knowledge-intensive tasks (QA, fact-checking, logical inference)
- Scenarios where hallucination or factual inconsistency is a concern
- Multi-hop reasoning requiring external knowledge grounding

## Implementation Considerations
- Requires access to a structured knowledge base (e.g., Wikidata, domain-specific KB)
- Subgraph construction must be query-specific to avoid context overload
- Multiple reasoning trajectories increase compute but improve reliability

## Activation
stepwise reasoning, subgraph generation, knowledge grounding, external KB reasoning, SGR
