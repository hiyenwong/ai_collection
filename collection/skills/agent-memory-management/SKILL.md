---
name: agent-memory-management
description: Memory forgetting techniques for autonomous AI agents - adaptive budgeted forgetting, relevance-guided scoring, and bounded optimization for managing long-horizon agent memory systems. Prevents temporal decay and false memory propagation. Source: arXiv:2604.02280. Activation: agent memory, memory forgetting, relevance scoring, memory budget, false memory prevention, adaptive forgetting.
---

# Agent Memory Management

## Description

Adaptive memory management techniques for autonomous AI agents. Addresses the challenge of balancing persistent memory needs with controlled forgetting to prevent temporal decay and false memory propagation.

**Source Paper:** Novel Memory Forgetting Techniques for Autonomous AI Agents: Balancing Relevance and Efficiency (arXiv:2604.02280)

**Problem Addressed:**
- Long-horizon agents require persistent memory but uncontrolled accumulation causes:
  - Temporal decay of relevant memories
  - False memory propagation (78.2% accuracy with 6.8% false memory rate)
  - Performance degradation (0.455 to 0.05 across stages in LOCOMO benchmark)

## Activation Keywords

- agent memory
- memory forgetting
- memory management
- relevance scoring
- memory budget
- false memory
- adaptive forgetting
- memory efficiency
- budgeted forgetting
- relevance-guided memory

## Tools Used

- exec: Run Python scripts for memory scoring algorithms
- read: Load memory state and relevance configurations
- write: Save memory state and scoring results
- edit: Update memory entries

## Core Concepts

### Adaptive Budgeted Forgetting Framework

| Component | Description |
|-----------|-------------|
| **Relevance Scoring** | Dynamic scoring of memory entries based on usage patterns |
| **Memory Budget** | Bounded memory capacity with controlled eviction |
| **Temporal Decay** | Time-based relevance decay for stale memories |
| **False Memory Prevention** | Confidence thresholds to prevent propagation |

### Relevance-Guided Scoring Formula

```python
def compute_relevance(memory_entry, current_context, decay_rate=0.1):
    """
    Compute relevance score for a memory entry.
    
    Factors:
    - Recency: time since last access
    - Frequency: number of times accessed
    - Context match: similarity to current task
    - Confidence: reliability of the memory
    """
    recency_score = exp(-decay_rate * time_since_access)
    frequency_score = log(1 + access_count)
    context_score = cosine_similarity(memory_entry.embedding, current_context.embedding)
    confidence_score = memory_entry.confidence
    
    # Weighted combination
    relevance = 0.3 * recency_score + 
                0.2 * frequency_score + 
                0.3 * context_score + 
                0.2 * confidence_score
    
    return relevance
```

## Usage Patterns

### Pattern 1: Initialize Memory Budget

```python
# Set memory budget parameters
memory_budget = {
    "max_entries": 1000,
    "eviction_threshold": 0.3,  # Relevance below this triggers eviction
    "decay_rate": 0.05,         # Per-hour decay
    "false_memory_threshold": 0.8  # Confidence below this flagged as potential false
}
```

### Pattern 2: Score and Evict

```python
# Periodic memory scoring and eviction
def manage_memory(memory_store, budget, current_context):
    # Score all entries
    scores = []
    for entry in memory_store.entries:
        score = compute_relevance(entry, current_context, budget["decay_rate"])
        scores.append((entry, score))
    
    # Sort by relevance
    scores.sort(key=lambda x: x[1], reverse=True)
    
    # Evict low-relevance entries
    kept = []
    evicted = []
    for entry, score in scores:
        if score < budget["eviction_threshold"]:
            evicted.append(entry)
        else:
            kept.append(entry)
    
    # Ensure budget constraint
    if len(kept) > budget["max_entries"]:
        kept = kept[:budget["max_entries"]]
    
    return kept, evicted
```

### Pattern 3: False Memory Detection

```python
def detect_false_memory(memory_store, threshold=0.8):
    """Flag potential false memories for review."""
    flagged = []
    for entry in memory_store.entries:
        if entry.confidence < threshold:
            flagged.append(entry)
        # Also check for contradictory entries
        for other in memory_store.entries:
            if is_contradictory(entry, other):
                flagged.extend([entry, other])
    return flagged
```

## Instructions for Agents

### Step 1: Assess Memory State

When memory management is needed:

1. Check current memory size and distribution
2. Identify high-relevance and low-relevance entries
3. Detect potential false memories
4. Calculate memory pressure (size vs budget)

### Step 2: Apply Forgetting Strategy

Based on memory pressure:

| Pressure Level | Action |
|----------------|--------|
| Low (< 50%) | Light maintenance, update relevance scores |
| Medium (50-80%) | Active eviction of low-relevance entries |
| High (> 80%) | Aggressive eviction, review all entries |
| Critical (> 100%) | Emergency eviction, keep only top entries |

### Step 3: Update Memory State

After eviction:

1. Update relevance scores for remaining entries
2. Record eviction decisions for audit
3. Adjust decay rate based on task demands
4. Flag any suspicious entries for human review

### Step 4: Prevent False Memory Propagation

Key strategies:

- **Confidence scoring**: Tag uncertain memories
- **Contradiction detection**: Cross-check related memories
- **Evidence linking**: Maintain provenance chains
- **Human review triggers**: Flag low-confidence entries

## Configuration

### Memory Budget Parameters

```yaml
memory_budget:
  max_entries: 1000
  eviction_threshold: 0.3
  decay_rate: 0.05  # per hour
  
scoring_weights:
  recency: 0.3
  frequency: 0.2
  context: 0.3
  confidence: 0.2
  
false_memory:
  confidence_threshold: 0.8
  contradiction_check: true
  human_review_threshold: 0.5
```

## Examples

### Example 1: Managing Agent Memory

```
User: "My agent is accumulating too many memories and getting confused"

Agent:
1. Analyzes current memory state
2. Identifies low-relevance entries (relevance < 0.3)
3. Detects potential false memories (confidence < 0.8)
4. Recommends eviction strategy

Output:
- Current entries: 850 (budget: 1000)
- Low relevance: 120 entries (recommend eviction)
- Potential false memories: 15 entries (flag for review)
- Recommended action: Evict 100 lowest-relevance entries, review 15 flagged
```

### Example 2: Preventing False Memory Propagation

```
User: "The agent sometimes 'remembers' things that never happened"

Agent:
1. Runs contradiction detection across memories
2. Identifies entries without evidence/provenance
3. Flags low-confidence memories for review
4. Implements confidence-based filtering

Output:
- Found 8 contradictory memory pairs
- 23 memories lack provenance evidence
- Implemented confidence threshold of 0.7
- Created audit log for human review
```

## Benchmarks Reference

From source paper:

| Benchmark | Metric | Result |
|-----------|--------|--------|
| LOCOMO | Stage degradation | 0.455 → 0.05 |
| MultiWOZ | Accuracy with persistence | 78.2% |
| MultiWOZ | False memory rate | 6.8% |

## Best Practices

1. **Regular scoring**: Update relevance scores at least every hour
2. **Budget awareness**: Monitor memory pressure continuously
3. **Evidence tracking**: Maintain provenance for all memories
4. **Human review**: Flag suspicious entries for oversight
5. **Adaptive decay**: Adjust decay rate based on task complexity

## Limitations

- Requires embedding model for context similarity
- Computational overhead for scoring large memory stores
- May evict useful but infrequently accessed memories
- False memory detection is heuristic-based

## Related Skills

- **chat-history-lancedb**: For chat history storage (different focus)
- **indexed-memory**: For structured memory indexing
- **memory-retrieval**: For memory search and retrieval

## References

- arXiv:2604.02280: Novel Memory Forgetting Techniques for Autonomous AI Agents
- LOCOMO Benchmark: https://github.com/amazon-science/locomo
- MultiWOZ Dataset: https://github.com/budzianowski/multiwoz