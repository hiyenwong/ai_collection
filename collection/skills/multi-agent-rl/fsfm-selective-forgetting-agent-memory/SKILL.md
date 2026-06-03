---
name: fsfm-selective-forgetting-agent-memory
description: "FSFM: Biologically-inspired framework for selective forgetting of LLM agent memory. Taxonomy of forgetting mechanisms (passive decay, active deletion, safety-triggered, adaptive reinforcement) inspired by hippocampal indexing and Ebbinghaus forgetting curve. Results: +8.49% access efficiency, +29.2% SNR, 100% security risk elimination."
category: ai_collection
tags: [agent-memory, forgetting, hippocampus, memory-management, llm-agent, vector-database, cognitive-neuroscience, privacy, security]
---

# FSFM: Selective Forgetting of Agent Memory

## Paper
- **arXiv:** 2604.20300
- **Date:** 2026-04-22
- **Authors:** Yingjie Gu, Bo Xiong, Yijuan Guo, Chao Li, Xiaojing Zhang et al.
- **Categories:** cs.AI
- **URL:** https://arxiv.org/abs/2604.20300

## Abstract
For LLM agents, memory management critically impacts efficiency, quality, and security. While much research focuses on retention, selective forgetting—inspired by human cognitive processes (hippocampal indexing/consolidation theory and Ebbinghaus forgetting curve)—remains underexplored. The framework argues that in resource-constrained environments, a well-designed forgetting mechanism is as crucial as remembering.

## Core Methodology

### Biological Inspiration
1. **Hippocampal Indexing Theory**: The hippocampus creates temporary indices for memories that are gradually consolidated into neocortex. FSFM models this as a dual-store memory with time-dependent transfer.
2. **Ebbinghaus Forgetting Curve**: Memory strength decays exponentially: R(t) = e^{-t/S}, where S is memory stability. This governs passive decay rates.
3. **Active Forgetting**: Inspired by proactive interference suppression in biological memory.

### Taxonomy of Forgetting Mechanisms

#### 1. Passive Decay-Based Forgetting
- Exponential decay of memory relevance scores over time
- Governed by Ebbinghaus curve parameters
- Automatic, requires no explicit triggers
- Implementation: timestamp-weighted scoring in vector databases

#### 2. Active Deletion-Based Forgetting
- Explicit removal of redundant, outdated, or low-value memories
- Triggered by relevance threshold crossing
- Includes: deduplication, version replacement, conflict resolution
- Implementation: periodic pruning sweeps over memory store

#### 3. Safety-Triggered Forgetting
- Immediate removal of malicious, sensitive, or privacy-compromising content
- Compliance-driven (GDPR right-to-erasure, data retention policies)
- Pattern-based and rule-based detection of harmful content
- Implementation: content scanning pipelines with safety classifiers

#### 4. Adaptive Reinforcement-Based Forgetting
- Strengthening frequently accessed, high-utility memories
- Weakening rarely accessed, low-utility memories
- Analogous to synaptic long-term potentiation (LTP) and depression (LTD)
- Implementation: access-frequency weighted scoring with reinforcement

### Architecture Components
- **Memory Encoder**: Converts experiences into vector embeddings with metadata
- **Forgetting Scheduler**: Orchestrates when and how memories decay or are removed
- **Relevance Evaluator**: Scores memories against current context
- **Safety Filter**: Real-time scanning for harmful/sensitive content

## Key Results
| Metric | Improvement |
|--------|-------------|
| Access Efficiency | +8.49% |
| Signal-to-Noise Ratio | +29.2% |
| Security Risk Elimination | 100% |

## Implementation Patterns

### Passive Decay Scoring
```python
import numpy as np

def compute_memory_score(memory, current_time, half_life_hours=24):
    """Ebbinghaus-inspired decay scoring."""
    age_hours = (current_time - memory.timestamp).total_seconds() / 3600
    decay_factor = np.exp(-0.693 * age_hours / half_life_hours)
    return memory.base_score * decay_factor * memory.access_frequency
```

### Adaptive Reinforcement Update
```python
def reinforce_memory(memory, access_reward, decay_rate=0.95):
    """LTP/LTD-inspired memory strength update."""
    memory.strength = decay_rate * memory.strength + (1 - decay_rate) * access_reward
    if memory.strength < threshold:
        trigger_forgetting(memory)
```

### Safety-Triggered Forgetting
```python
def safety_scan(memory_store, safety_classifier):
    """Immediate removal of harmful content."""
    flagged = []
    for mem in memory_store:
        risk_score = safety_classifier.predict(mem.content)
        if risk_score > SAFETY_THRESHOLD:
            flagged.append(mem)
    memory_store.batch_delete(flagged)
    return len(flagged)
```

## Applications
- **LLM Agent Memory Management**: Long-term conversation agents, autonomous task agents
- **Vector Database Optimization**: Reducing index size while maintaining retrieval quality
- **Privacy Compliance**: GDPR right-to-erasure, data retention policy enforcement
- **Security**: Removing injected malicious prompts or jailbreak artifacts

## Connections to Neuroscience
- Hippocampal indexing theory → dual-store memory architecture
- Ebbinghaus forgetting curve → passive decay scheduling
- Synaptic plasticity (LTP/LTD) → adaptive reinforcement
- Sleep-dependent memory consolidation → periodic memory reorganization

## Pitfalls
- Over-forgetting can degrade agent performance on long-horizon tasks
- Safety triggers may have false positives, removing useful memories
- Decay parameters need domain-specific tuning
- Reinforcement-based forgetting requires sufficient access history

## References
- arXiv:2604.20300
- Ebbinghaus, H. (1885). Memory: A Contribution to Experimental Psychology
- Teyler, T.J. & DiScenna, P. (1986). The Hippocampal Memory Indexing Theory
