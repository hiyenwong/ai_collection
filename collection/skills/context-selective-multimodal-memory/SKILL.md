---
name: context-selective-multimodal-memory
description: "Human-inspired context-selective multimodal memory architecture for social robots. Combines hippocampal-inspired memory consolidation with context-dependent retrieval across visual, auditory, and textual modalities. Use when building embodied AI agents, social robots, or any system needing human-like context-aware multimodal memory. Activation: context-selective memory, multimodal memory, social robot memory, hippocampal-inspired memory, embodied AI memory, context-aware retrieval."
---

# Context-Selective Multimodal Memory

## Overview

A **human-inspired context-selective multimodal memory architecture** designed for social robots and embodied AI agents. The system mimics hippocampal memory processes to selectively encode, consolidate, and retrieve multimodal experiences based on contextual relevance. Unlike flat memory systems, it prioritizes contextually relevant memories and implements sleep-inspired consolidation.

## Source Paper

- **arXiv**: 2604.14859v1
- **Published**: 2026-04-19
- **Categories**: cs.AI, cs.RO, cs.HC

## Core Architecture

### Three-Phase Memory System
```
Encoding (Hippocampal) → Consolidation (Cortical) → Retrieval (Context-Selective)
```

### 1. Encoding Phase (Online)
- Rapid, context-tagged multimodal encoding
- Each memory stores: content (text/image/audio), context (location, time, social cues), emotional valence
- Inspired by hippocampal rapid plasticity

```python
from dataclasses import dataclass, field
from datetime import datetime
from typing import List, Optional
import numpy as np

@dataclass
class MemoryTrace:
    """A single multimodal memory trace."""
    content: dict  # {modality: data}
    context: dict  # {location, time, people, activity, mood}
    timestamp: datetime
    emotional_valence: float  # -1.0 to 1.0
    retrieval_count: int = 0
    consolidation_level: float = 0.0  # 0 (raw) to 1 (fully consolidated)
    context_vector: np.ndarray = None  # Embedding for similarity
    
    def compute_salience(self):
        """Compute memory salience for encoding priority."""
        # Novelty + emotional intensity + context relevance
        novelty = 1.0 - self.consolidation_level
        emotional = abs(self.emotional_valence)
        return 0.5 * novelty + 0.3 * emotional + 0.2 * (1.0 - self.consolidation_level)

class HippocampalEncoder:
    """Fast, context-tagged multimodal encoding."""
    
    def __init__(self, embedding_model, max_capacity=1000):
        self.embedding_model = embedding_model
        self.max_capacity = max_capacity
        self.short_term_buffer: List[MemoryTrace] = []
    
    def encode(self, content, context, emotional_valence=0.0):
        """Encode a new multimodal memory."""
        trace = MemoryTrace(
            content=content,
            context=context,
            timestamp=datetime.now(),
            emotional_valence=emotional_valence,
            context_vector=self.embedding_model.encode_context(context)
        )
        self.short_term_buffer.append(trace)
        
        # Evict if over capacity (keep most salient)
        if len(self.short_term_buffer) > self.max_capacity:
            self._evict_least_salient()
        
        return trace
```

### 2. Consolidation Phase (Offline / Sleep-inspired)
- Transfers important memories from short-term to long-term storage
- Priority based on: emotional salience, retrieval frequency, contextual importance
- Implements memory replay and integration with existing knowledge

```python
class CorticalConsolidator:
    """Sleep-inspired memory consolidation."""
    
    def __init__(self, long_term_store):
        self.long_term_store = long_term_store
    
    def consolidate(self, short_term_buffer, replay_ratio=0.3):
        """Consolidate memories from short-term to long-term."""
        # Sort by salience
        sorted_memories = sorted(short_term_buffer, 
                                  key=lambda m: m.compute_salience(),
                                  reverse=True)
        
        # Keep top memories for consolidation
        n_consolidate = int(len(sorted_memories) * replay_ratio)
        
        consolidated = []
        for memory in sorted_memories[:n_consolidate]:
            # Memory replay: strengthen connections
            memory.consolidation_level = min(1.0, memory.consolidation_level + 0.2)
            memory.retrieval_count += 1  # Replay counts as retrieval
            
            # Integrate with related long-term memories
            self._integrate_with_existing(memory)
            consolidated.append(memory)
            self.long_term_store.add(memory)
        
        # Prune non-consolidated memories
        remaining = [m for m in short_term_buffer if m not in sorted_memories[:n_consolidate]]
        short_term_buffer.clear()
        short_term_buffer.extend(remaining[:len(remaining)//2])  # Keep some
        
        return consolidated
    
    def _integrate_with_existing(self, memory):
        """Find and link to related existing memories."""
        # Semantic similarity search in long-term store
        related = self.long_term_store.find_similar(memory.context_vector, threshold=0.7)
        for rel in related:
            # Strengthen associative links
            memory.context_vector = 0.8 * memory.context_vector + 0.2 * rel.context_vector
```

### 3. Retrieval Phase (Context-Selective)
- Retrieves memories most relevant to current context
- Uses context similarity + recency + salience for ranking
- Implements pattern completion (partial cues retrieve full memories)

```python
class ContextSelectiveRetriever:
    """Retrieve memories based on current context."""
    
    def __init__(self, long_term_store):
        self.long_term_store = long_term_store
    
    def retrieve(self, current_context, top_k=5, modality_filter=None):
        """Retrieve most contextually relevant memories."""
        context_vector = self.long_term_store.embedding_model.encode_context(current_context)
        
        # Score memories by context similarity + recency + salience
        candidates = []
        for memory in self.long_term_store.all_memories():
            if modality_filter and memory.content.get('modality') not in modality_filter:
                continue
            
            similarity = np.dot(context_vector, memory.context_vector)
            recency = np.exp(-0.1 * (datetime.now() - memory.timestamp).days)
            salience = memory.compute_salience()
            
            score = 0.6 * similarity + 0.2 * recency + 0.2 * salience
            candidates.append((score, memory))
        
        candidates.sort(reverse=True)
        return [m for _, m in candidates[:top_k]]
    
    def pattern_complete(self, partial_context, modality='text'):
        """Retrieve full memories from partial contextual cues."""
        # Similar to retrieve but with sparse/partial context
        return self.retrieve(partial_context, top_k=3, modality_filter=[modality])
```

## Practical Applications

### Social Robot Memory
```python
# Example: Social robot remembering interactions
robot_memory = SocialRobotMemory()

# After interaction with person
robot_memory.encode(
    content={'text': "User asked about weather", 'visual': face_image},
    context={'person': 'Alice', 'location': 'kitchen', 'activity': 'conversation'},
    emotional_valence=0.3  # Mildly positive
)

# Later, when Alice returns
relevant = robot_memory.retrieve(
    current_context={'person': 'Alice', 'location': 'kitchen'},
    top_k=3
)
# Robot recalls: Alice asked about weather last time, was mildly positive
```

### Embodied AI Agent Memory
- Remember past interactions with users
- Context-aware task memory
- Cross-modal experience integration (what was seen + heard + felt)

## Limitations
- Requires context embeddings (depends on embedding model quality)
- Consolidation parameters need tuning for specific domains
- Multimodal alignment is challenging
- Computational cost grows with memory size (needs efficient indexing)

## Activation Keywords
- context-selective memory
- multimodal memory architecture
- social robot memory
- hippocampal-inspired memory
- embodied AI memory
- context-aware retrieval
- sleep-inspired consolidation


## Tools Used

- `read` - 读取技能文档
- `write` - 创建输出
- `exec` - 执行相关命令


## Instructions for Agents

1. 理解技能的核心方法论
2. 根据用户问题提供针对性回答
3. 遵循最佳实践


## Examples

### Example 1: 基本查询

**User:** 请解释 Context Selective Multimodal Memory

**Agent:** Context Selective Multimodal Memory 是关于...
