---
name: rated-tool-retrieval
description: 'RATED: Reliability-aware AI agent tool retrieval via execution dynamics. Use when building tool-using agents needing dynamic reliability adaptation beyond semantic matching.'
arxiv_id: '2610.13889'
utility: 0.86
authors: Weiliang Chen, Song Liao
categories: [cs.AI, cs.IR]
tags: [tool-retrieval, reliability, execution-dynamics, contextual-bandit, agent-tools]
---

# RATED: Reliability-Aware AI Agent Tool Retrieval

## Key Innovation

AI agents rely on external tools, but existing retrieval methods optimize semantic relevance while ignoring tool availability during execution. RATED combines robust semantic matching with dynamic reliability adaptation via contextual bandits.

## Method

- **Dual-encoder**: Frozen contrastive fine-tuning for semantic matching
- **Contextual bandit**: Lightweight module re-ranking candidates based on real-time execution feedback
- **Dynamic adaptation**: Updates reliability estimates from execution outcomes
- **Integration**: Semantic relevance + execution reliability = robust retrieval

## Architecture

```
Query → Dual Encoder (semantic) → Candidates
                                    ↓
                        Contextual Bandit (reliability)
                                    ↓
                        Re-ranked Results → Agent
```

## Results

- Improved tool retrieval accuracy vs semantic-only methods
- Adapts to tool availability changes over time
- Handles execution failures gracefully

## Practical Use

- Building reliable tool-using agents
- Dynamic tool selection in changing environments
- Improving agent robustness to tool failures

## URL

https://arxiv.org/abs/2610.13889
