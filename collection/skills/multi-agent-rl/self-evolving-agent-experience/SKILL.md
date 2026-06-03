---
name: self-evolving-agent-experience
category: research
created: "2026-05-19"
source: "arXiv:2605.15461v1"
description: Framework for LLM agents that accumulates and reuses cross-task experience including verified skills, statistical evidence of effective strategies, and recurring error-fix patterns. Enables zero-test-time search on new tasks.
tags: [agent, memory, self-evolving, experience-reuse, drug-discovery]
---

# Self-evolving Agent Experience (DrugSAGE)

**Source**: arXiv:2605.15461v1 - "DrugSAGE: Self-evolving Agent Experience for Efficient State-of-the-Art Drug Discovery"

## Summary

Proposes a framework for LLM-based agents that accumulates cross-task memory of verified skills, statistical evidence about effective strategies, and recurring error-fix patterns. Eliminates redundant trial-and-error search on new tasks, achieving SOTA performance without test-time search after sufficient experience accumulation.

## Core Methodology

### Key Problem
Current LLM agents can find SOTA solutions through extensive trial-and-error but do not retain experience across tasks, paying the full search cost on every new task.

### Experience Components
1. **Verified Skills**: Solutions that worked on previous tasks
2. **Statistical Evidence**: Data about which strategies are most effective
3. **Error-Fix Records**: Recurring errors and their fixes

### Operating Modes
1. **Direct Transfer**: Apply a working solution from memory without any test-time search
2. **Guided Search**: Use accumulated experience to inform and narrow the search space

### Results
- 33 molecular property prediction tasks: ranks 1st among 9 SOTA agents in single-task setting
- Cross-task: 0.935 normalized score on 17 held-out tasks after learning from 16 smaller tasks
- Outperforms all baselines by 10-30% in zero-test-time search regime

## When to Use
- LLM agents performing repetitive task families (drug discovery, ML engineering, etc.)
- Scenarios where agents repeatedly rediscover the same solutions
- Any domain where experience accumulation can eliminate redundant search

## Implementation Considerations
- Requires structured memory across task boundaries
- Need mechanisms for verifying and indexing successful strategies
- Error-fix patterns should be generalized, not task-specific
- Can generalize beyond drug discovery to any agent-based workflow

## Activation
self-evolving agent, cross-task memory, experience reuse, agent skill accumulation, drugSAGE
