---
name: recontext-evidence-replay
description: Recursive Evidence Replay as LLM Harness for Long-Context Reasoning. Training-free inference method that uses model-internal relevance signals to construct query-conditioned evidence pool and replays before final generation, improving long-context reasoning without training, external memory, or context pruning.
trigger: recursive evidence replay, ReContext, long context reasoning, evidence retrieval, context utilization
category: ai_collection/collection/skills
---

# ReContext: Recursive Evidence Replay for Long-Context Reasoning

## Overview
RECONTEXT (Recursive Evidence Replay as LLM Harness for Long-Context Reasoning) is a training-free inference method that separates evidence organization from answer generation to improve LLM long-context reasoning.

## Core Mechanism
1. **Evidence Pool Construction**: Use model-internal relevance signals to identify query-relevant passages from the full context
2. **Recursive Replay**: Replay the evidence pool before final generation while preserving the original full context
3. **Associative Memory Theory**: 
   - Context = memory store
   - Question = retrieval cue  
   - Attention = cue-trace association
   - Replay = trace reactivation

## Implementation Steps
1. Feed the full context + query to the LLM
2. Extract relevance signals from model attention weights or internal states
3. Construct a query-conditioned evidence pool from the most relevant passages
4. Prepend this evidence pool to the original prompt and generate the final answer
5. Optionally repeat the process (recursive) for multi-hop reasoning

## Key Benefits
- **Training-free**: No model fine-tuning required
- **No external memory**: Works with existing model parameters
- **No context pruning**: Preserves full original context
- **Consistent improvement**: Works across Qwen3-4B, Qwen3-8B, and Llama3-8B
- **128K context**: Tested on long-context datasets

## Activation Keywords
recursive evidence replay, long context reasoning, evidence pool, context utilization, attention retrieval, associative memory

## Source
arXiv: 2607.02509 (2026-07-02)
