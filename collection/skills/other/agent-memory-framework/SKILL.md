---
name: agent-memory-framework
description: "Design and implement memory-augmented AI agents using modular architecture (extraction, update, retrieval, response). Inspired by MemFactory (arxiv:2603.29493) - unified training/inference framework for agent memory with RL-driven policy optimization (GRPO). Use when building long-term AI agents, memory management systems, or implementing Memory-R1/RMM/MemAgent paradigms. Keywords: agent memory, memory-augmented LLM, MemFactory, Memory-R1, memory lifecycle, GRPO, memory extraction, memory retrieval."
---

# Agent Memory Framework

Design memory-augmented AI agents with modular, RL-optimized memory management.

## Core Concepts

### Memory Lifecycle (6 Stages)

```
Conversation → [Extraction] → [Update Decision] → [Storage] → [Organization] → [Retrieval] → [Response] → Answer
```

| Stage | Function | Implementation |
|-------|----------|----------------|
| Extraction | Extract key info from conversation | LLM-based extraction |
| Update Decision | ADD/UPDATE/DELETE/NOOP | RL policy (GRPO) |
| Storage | Store memory entries | Vector DB / Knowledge Graph |
| Organization | Structure memory | Hierarchical / Temporal |
| Retrieval | Find relevant memories | Semantic search |
| Response | Generate answer | LLM reasoning |

### Memory Operations

| Operation | Trigger | Example |
|-----------|---------|---------|
| ADD | New information | User: "My name is Alice" → ADD name=Alice |
| UPDATE | Information change | User: "I moved to NYC" → UPDATE location=NYC |
| DELETE | Outdated info | Time-based expiration → DELETE old entries |
| NOOP | No new info | Irrelevant conversation → NOOP |

### RL Policy Optimization (GRPO)

**Group Relative Policy Optimization:**
- Fine-tune memory management policies
- Multi-dimensional rewards:
  - Answer quality
  - Memory efficiency
  - Conversation coherence

## Architecture Patterns

### Pattern 1: Dual-Agent Architecture (Memory-R1)

```
Memory Manager Agent:
  Input: Conversation history
  Output: Memory operation sequence
  Training: RL (GRPO/PPO)

Answer Agent:
  Input: Question + Retrieved memories
  Output: Answer
  Training: RL + Supervised
```

**Advantages:**
- Specialization: Each agent focuses on its task
- Scalability: Can train agents separately
- Efficiency: 152 QA pairs sufficient for training

### Pattern 2: Modular Memory Pipeline

```python
class MemoryPipeline:
    def __init__(self):
        self.extractor = MemoryExtractor()
        self.updater = MemoryUpdateDecision()
        self.storage = MemoryStorage()
        self.retriever = MemoryRetriever()
        self.responder = ResponseGenerator()
    
    def process(self, conversation, query):
        # 1. Extract from conversation
        new_info = self.extractor.extract(conversation)
        
        # 2. Decide memory operations
        operations = self.updater.decide(self.storage, new_info)
        
        # 3. Execute operations
        self.storage.apply(operations)
        
        # 4. Retrieve relevant memories
        memories = self.retriever.retrieve(query, self.storage)
        
        # 5. Generate response
        return self.responder.generate(query, memories)
```

### Pattern 3: RL Training Loop

```python
# GRPO training for memory management
def train_memory_policy(agent, episodes):
    for episode in episodes:
        # Simulate conversation
        conversation = simulate_dialogue()
        
        # Get memory operations
        operations = agent.get_operations(conversation)
        
        # Execute and evaluate
        outcome = execute_operations(operations)
        reward = compute_reward(outcome)
        
        # Update policy
        agent.policy.update(operations, reward)
```

## Implementation Guide

### Step 1: Design Memory Schema

```python
# Memory entry structure
memory_entry = {
    "id": "mem_001",
    "content": "User preference: dark mode",
    "type": "preference",  # fact, preference, event, context
    "timestamp": 1703275200,
    "importance": 0.8,
    "source": "conversation_123",
    "metadata": {"category": "ui_settings"}
}
```

### Step 2: Implement Extraction

```python
def extract_memory(conversation: str) -> List[MemoryEntry]:
    """Extract key information from conversation."""
    # LLM-based extraction
    prompt = f"""
    Extract key facts, preferences, and events from this conversation.
    Return as structured JSON.
    
    Conversation: {conversation}
    """
    extracted = llm.generate(prompt)
    return parse_to_memories(extracted)
```

### Step 3: Implement Update Decision

```python
class MemoryUpdatePolicy:
    def decide(self, storage: MemoryStorage, new_info: List) -> List[Operation]:
        """Decide which memory operations to perform."""
        operations = []
        for info in new_info:
            existing = storage.search(info.content)
            if not existing:
                operations.append(Operation("ADD", info))
            elif info.is_update(existing):
                operations.append(Operation("UPDATE", existing.id, info))
            # ... check for DELETE, NOOP
        return operations
```

### Step 4: Implement Retrieval

```python
def retrieve_memories(query: str, storage: MemoryStorage, k: int = 60) -> List:
    """Retrieve top-k relevant memories."""
    # Semantic search
    candidates = storage.vector_search(query, k)
    
    # Filter and rank
    relevant = filter_by_relevance(candidates, query)
    
    # Return subset (Memory-R1: up to 60 candidates, distilled to subset)
    return select_top_subset(relevant, threshold=0.7)
```

### Step 5: RL Training

```python
# Reward function for memory policy
def compute_reward(outcome: Outcome) -> float:
    reward = 0.0
    reward += outcome.answer_quality * 0.5
    reward += outcome.memory_efficiency * 0.3
    reward += outcome.conversation_coherence * 0.2
    return reward
```

## Supported Paradigms

### Memory-R1 (arxiv:2508.19828)

- Dual-agent architecture
- Operations: ADD, UPDATE, DELETE, NOOP
- Training: PPO/GRPO, 152 QA pairs
- Benchmarks: LoCoMo, MSC, LongMemEval

### RMM (Retrieval-Augmented Memory Management)

- Focus: Memory retrieval optimization
- RL-based retrieval policy
- Semantic + temporal retrieval

### MemAgent

- Focus: Long-context handling
- Memory for extended conversations
- Context compression and summarization

## Best Practices

### 1. Modular Design

- Each memory stage as independent module
- Plug-and-play architecture
- "Lego-like" composition

### 2. RL-Driven Policies

- Learn when to add/update/delete memories
- Multi-dimensional rewards
- Minimal supervision (152 pairs sufficient)

### 3. Specialization

- Separate memory management from answer generation
- Different agents for different tasks
- Targeted training

### 4. Evaluation

- Cross-benchmark testing
- Generalization across diverse questions
- Multiple model scales (3B-14B)

## Tools Used

- `read`: Load conversation history, existing memories
- `write`: Create/update memory entries
- `edit`: Modify memory content
- `exec`: Run RL training, vector search
- `sqlite3`: Memory storage (kg.db pattern)

## Activation Keywords

- agent memory
- memory-augmented LLM
- MemFactory
- Memory-R1
- memory lifecycle
- GRPO
- memory extraction
- memory retrieval
- memory management
- long-term AI agent

## Related Skills

- `memory-retrieval`: Memory search and retrieval
- `indexed-memory`: Indexed memory management
- `chat-history-lancedb`: LanceDB for chat history
- `knowledge-graph`: Knowledge graph integration

## References

- **MemFactory** (arxiv:2603.29493): Unified framework
- **Memory-R1** (arxiv:2508.19828): RL-driven memory management
- **LLaMA-Factory**: Inspiration for modular design
- **ReContext** (arxiv:2607.02509): [references/recontext-associative-memory-pattern.md](references/recontext-associative-memory-pattern.md) — neuroscience-inspired associative memory mapping for LLM retrieval systems

## GitHub

- https://github.com/MemTensor/MemFactory
- https://github.com/Valsure/MemFactory

## Notes

- Modular design enables easy customization
- RL training requires minimal data (152 pairs)
- Performance gains up to 14.8% over base models
- Dual-agent architecture separates concerns effectively