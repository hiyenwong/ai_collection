---
name: saas-self-aware-agentic-search
description: Self-Aware Reinforcement Learning for Over-Search Mitigation - dynamic self-awareness that regulates search behavior without compromising accuracy
version: 1.0.0
author: Hermes Agent (from arXiv 2605.29796)
tags: [agentic, RL, search-optimization, self-awareness, LLM]
activation_keywords: [over-search, agentic search, search boundary, self-awareness, reasoning, multi-hop]
---

# SAAS: Self-Aware Reinforcement Learning for Over-Search Mitigation

## Overview

SAAS addresses over-search in agentic search systems - agents fail to recognize knowledge boundaries, triggering unnecessary searches and failing to terminate even with adequate evidence. This framework cultivates dynamic self-awareness that precisely regulates search behavior.

## Problem Statement
- **Over-Search**: Agents blindly trigger searches when internal knowledge suffices
- **Incomplete Termination**: Agents fail to stop search when evidence is adequate
- **Cost Impact**: Substantial inference latency and prohibitive computational cost

## Core Components

### 1. Search Boundary Modeling
```python
def identify_search_boundary(policy, prompt):
    # Contrast search-disabled and search-enabled rollouts
    without_search = policy.generate(prompt, search_enabled=False)
    with_search = policy.generate(prompt, search_enabled=True)
    
    # Identify boundary where search becomes necessary
    boundary = detect_knowledge_gap(without_search, with_search)
    return boundary
```

### 2. Boundary-Aware Reward Module
```python
def compute_saas_reward(trajectory, search_boundary):
    base_reward = outcome_reward(trajectory)
    
    # Penalty for unnecessary/redundant searches
    over_search_penalty = 0
    for step in trajectory:
        if step.search_triggered and step.state < search_boundary:
            over_search_penalty += search_penalty_weight
    
    return base_reward - over_search_penalty
```

### 3. Stage-Wise Optimization Strategy
- **Stage 1**: Prioritize reasoning accuracy (no search regularization)
- **Stage 2**: Introduce search boundary awareness
- **Stage 3**: Full boundary-aware reward integration
- Sequential curriculum avoids reward hacking

## Implementation Protocol

### Phase 1: Baseline Training
- Train reasoning model without search capability
- Establish internal knowledge performance baseline

### Phase 2: Search Boundary Detection
- Enable search capability
- Collect contrastive rollouts (search-disabled vs enabled)
- Learn boundary classifier

### Phase 3: Self-Aware Policy Training
```python
def saas_training_loop(agent, env, episodes):
    for episode in episodes:
        trajectory = agent.run_with_search(env)
        boundary = get_current_boundary(agent)
        reward = compute_saas_reward(trajectory, boundary)
        agent.update_policy(trajectory, reward)
```

## Key Results
- Substantial reduction in over-search
- Maintained accuracy (no performance drop)
- Code: https://github.com/XMUDeepLIT/SAAS

## When to Use
- Multi-hop question answering systems
- RAG systems with search/lookup capability
- Agentic systems with external tool access
- When inference cost is a concern

## Pitfalls
- Avoid early search regularization (causes reward hacking)
- Need sufficient internal knowledge baseline first
- Boundary model needs continuous updates as policy evolves

## References
- arXiv: 2605.29796v1
- Authors: Yunbo Tang, Chengyi Yang, Shiyu Liu et al.
- Published: 2026-05-28
- Code: https://github.com/XMUDeepLIT/SAAS