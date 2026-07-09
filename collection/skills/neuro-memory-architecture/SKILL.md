---
name: neuro-memory-architecture
description: >
  Neuroscience-inspired memory architecture design for AI agents.
  Maps biological memory systems (working, short-term, episodic, semantic,
  procedural, core, cross-context) to AI agent memory layers. Integrates
  neuroscience models including Hebbian learning, synaptic consolidation,
  sleep-based replay, and active forgetting. Use when designing agent memory
  systems, building neuro-inspired AI architectures, or implementing
  biologically-plausible memory mechanisms. Triggers: neuro memory, brain-inspired
  memory, zenbrain, cognitive memory architecture, hippocampal memory,
  memory consolidation AI, agent long-term memory.
---

# Neuroscience-Inspired Memory Architecture

Design AI agent memory systems modeled on biological brain memory mechanisms.

## Seven Memory Layers

Based on ZenBrain (arXiv:2604.23878) and AI-Meets-Brain (arXiv:2512.23343):

| Layer | Biological Analog | AI Implementation | Retention |
|-------|-------------------|-------------------|-----------|
| Working | Prefrontal cortex | Context window / scratchpad | Seconds |
| Short-term | Hippocampal CA1 | Recent conversation buffer | Minutes-hours |
| Episodic | Hippocampal CA3 | Time-stamped event log | Days-weeks |
| Semantic | Neocortex | Knowledge graph / embeddings | Months-years |
| Procedural | Basal ganglia | Learned skills / tool patterns | Permanent |
| Core | Brainstem | System prompts / identity | Permanent |
| Cross-context | Default mode | Cross-session synthesis | Permanent |

## Key Neuroscience Mechanisms

### Consolidation (Hours → Days)
- Transfer short-term → long-term via replay
- Prioritize emotionally salient / frequently accessed memories
- Implement during idle periods (analogous to sleep)

### Forgetting (Selective)
- Decay unused memories exponentially
- Remove contradictory / superseded information
- Preserve core patterns while losing noise

### Reconsolidation (On Recall)
- Update memories each time they're retrieved
- Merge new context into existing memory traces
- Strengthen frequently accessed paths

### Hebbian Learning
- "Neurons that fire together wire together"
- Strengthen co-occurring memory connections
- Build associative knowledge graphs

## Implementation Patterns

### Pattern 1: Multi-layer Memory Buffer
```
agent.memory = {
    working: [],          # current context
    short_term: deque(maxlen=100),  # recent events
    episodic: SQLite,     # timestamped logs
    semantic: vector_db,  # knowledge embeddings
    procedural: skills,   # learned patterns
    core: system_prompt,  # identity
    cross_context: graph  # cross-session links
}
```

### Pattern 2: Consolidation Cycle
```
on_idle():
    replay = select_salient(short_term)
    for memory in replay:
        consolidate_to(episodic, memory)
        update_semantic_graph(memory)
    prune_expired(short_term)
```

### Pattern 3: Retrieval with Reconsolidation
```
retrieve(query):
    results = vector_search(semantic, query)
    for r in results:
        r.strength += 1  # Hebbian reinforcement
        r.last_accessed = now()
    return merge_and_rank(results)
```

## Design Principles

1. **Separation of concerns** — Each layer has distinct access patterns
2. **Graceful degradation** — Upper layers can fail without breaking core
3. **Energy efficiency** — Only consolidate high-value memories
4. **Anti-catastrophic** — New learning doesn't overwrite old knowledge
5. **Contextual binding** — Memories tagged with situation/emotion metadata

## Validation

- Memory retrieval latency < 100ms for working, < 1s for semantic
- Consolidation doesn't block active operations
- Forgetting rate balances storage cost vs recall accuracy
- Cross-context links enable transfer learning across domains

## Related Research

- ZenBrain: 7-layer architecture with 15 neuroscience models (arXiv:2604.23878)
- AI Meets Brain: cognitive neuroscience → LLM agents survey (arXiv:2512.23343)
- Hippocampal replay credit assignment for deep learning
- Sleep-inspired homeostatic regularization for continual learning
