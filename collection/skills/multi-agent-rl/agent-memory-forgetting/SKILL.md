---
name: agent-memory-forgetting
description: 'Implement adaptive memory forgetting for autonomous AI agents. Use when building long-horizon conversational agents, managing agent memory growth, preventing false memory propagation, or implementing relevance-guided memory scoring. Based on arXiv:2604.02280 - Novel Memory Forgetting Techniques for Autonomous AI Agents.'
---

# Agent Memory Forgetting

Implement structured forgetting for autonomous AI agents to balance memory relevance and efficiency.

## Key Problem

Long-horizon conversational agents face:
- Uncontrolled memory accumulation causing temporal decay
- False memory propagation (MultiWOZ: 78.2% accuracy with 6.8% false memory rate)
- Performance degradation (LOCOMO: 0.455 → 0.05 across stages)

## Adaptive Budgeted Forgetting Framework

The paper proposes a framework with three core mechanisms:

### 1. Relevance-Guided Scoring

Score memories based on:
- **Recency**: Recent interactions weighted higher
- **Frequency**: Frequently referenced memories prioritized
- **Semantic Alignment**: Semantic similarity to current context

### 2. Bounded Optimization

Maintain memory under constrained context budget:
- Prevent unbounded growth
- Optimize for stability under limited capacity
- Trade-off between retention and efficiency

### 3. Structured Forgetting

Actively forget memories when:
- Relevance score falls below threshold
- Memory budget exceeded
- Semantic drift detected

## Implementation Guidelines

When implementing agent memory forgetting:

1. **Define relevance function**: Combine recency, frequency, semantic alignment
2. **Set memory budget**: Maximum tokens/entries to retain
3. **Implement forgetting trigger**: When budget exceeded, forget lowest-scoring memories
4. **Monitor false memories**: Track and suppress false memory propagation
5. **Validate stability**: Ensure forgetting preserves reasoning performance

## Key Metrics

- Long-horizon F1 > 0.583 baseline
- False memory rate reduction
- Retention consistency across conversation stages
- Context usage efficiency

## When to Apply

- Building multi-turn conversational agents
- Implementing persistent agent memory
- Managing long-running agent sessions
- Preventing memory-related hallucinations

## Paper Reference

arXiv:2604.02280 - "Novel Memory Forgetting Techniques for Autonomous AI Agents: Balancing Relevance and Efficiency" (Apr 2026)
## Activation Keywords

- agent-memory-forgetting
- agent-memory-forgetting 技能
- agent-memory-forgetting skill

## Tools Used

- `read` - Read documentation and references
- `web_search` - Search for related information
- `web_fetch` - Fetch paper or documentation

## Instructions for Agents
Follow these steps when applying this skill:

### Step 1: Define relevance function

### Step 2: Set memory budget

### Step 3: Implement forgetting trigger

### Step 4: Monitor false memories

### Step 5: Validate stability

## Examples

### Example 1: Basic Application

**User:** I need to apply Agent Memory Forgetting to my analysis.

**Agent:** I'll help you apply agent-memory-forgetting. First, let me understand your specific use case...

**Context:** Apply the methodology

### Example 2: Advanced Scenario

**User:** Complex analysis scenario

**Agent:** Based on the methodology, I'll guide you through the advanced application...

### Example 2: Advanced Application

**User:** What are the key considerations for agent-memory-forgetting?

**Agent:** Let me search for the latest research and best practices...
