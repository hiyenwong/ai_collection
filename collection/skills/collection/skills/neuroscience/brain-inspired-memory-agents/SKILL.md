---
name: brain-inspired-memory-agents
description: "Neuroscience-inspired 7-layer memory architecture for AI agents (ZenBrain). Integrates cognitive-neuroscience models from synaptic plasticity to sleep-based memory consolidation. Use when: designing long-term memory for AI agents, implementing bio-inspired memory systems, improving agent context management, or building persistent knowledge systems with forgetting mechanisms."
---

# Brain-Inspired Memory for AI Agents

## ZenBrain 7-Layer Architecture

Based on 2604.23878 - integrates 15 cognitive-neuroscience models into a coherent memory system.

### Layer 1: Two-Factor Synaptic Edges
- Short-term: Working memory traces (seconds)
- Long-term: Consolidated knowledge (days+)
- Plasticity rule: Combine Hebbian + homeostatic mechanisms

### Layer 2: Hippocampal Replay
- Experience replay for memory consolidation
- Prioritized replay: Important events replayed more often
- Dream replay: Offline consolidation during idle periods

### Layer 3: Prefrontal Working Memory
- Active task-relevant information
- Capacity-limited (like human WM: 4-7 items)
- Refresh mechanism to prevent decay

### Layer 4: Episodic Memory
- Time-stamped experiences
- Indexed by context, emotion, outcome
- Retrieved by similarity + recency + importance

### Layer 5: Semantic Memory
- Abstracted knowledge from episodes
- Concept networks with weighted edges
- Generalization through pattern extraction

### Layer 6: Procedural Memory
- Learned skills and habits
- Automatic execution without conscious recall
- Gradual automation through repetition

### Layer 7: Sleep-Based Consolidation
- Simulation-Selection during offline periods
- Synaptic homeostasis: normalize weights
- Memory prioritization and pruning

## Implementation Guidelines

1. **Start with layers 3+4**: Working + episodic memory are most impactful
2. **Add consolidation**: Implement periodic memory reorganization
3. **Add forgetting**: Not all memories should persist
4. **Add sleep cycle**: Batch consolidation during low-activity periods

## References

- 2604.23878: "ZenBrain: A Neuroscience-Inspired 7-Layer Memory Architecture for AI Agents"
- zenbrain-7layer-memory-architecture: Existing skill with related patterns
- agent-memory-management: Memory forgetting techniques

## Pitfalls

- Unlimited memory growth degrades retrieval performance
- Without forgetting, important memories get buried
- Sleep consolidation is essential but often skipped
- Real-time agents need async consolidation to avoid blocking
