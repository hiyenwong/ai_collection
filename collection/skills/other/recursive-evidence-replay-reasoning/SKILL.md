---
name: recursive-evidence-replay-reasoning
description: "ReContext framework — recursive evidence replay for long-context reasoning, mapping LLM attention to associative memory mechanisms from neuroscience"
---

# Recursive Evidence Replay for Reasoning (ReContext)

## Description

ReContext (Recursive Evidence Replay as LLM Harness for Long-Context Reasoning) is a **training-free inference method** that improves long-context reasoning by constructing a query-conditioned evidence pool from model-internal relevance signals, then replaying it before final generation. Its theoretical framework maps directly to neuroscience concepts of associative memory: context as memory store, question as retrieval cue, attention as cue-trace association, and replay as trace reactivation.

## Activation Keywords

- recursive evidence replay
- long-context reasoning
- associative memory reasoning
- evidence replay LLM
- context retrieval reasoning
- ReContext framework
- trace reactivation reasoning
- cue-trace association
- 递归证据回放
- 长上下文推理
- 联想记忆推理
- memory store reasoning

## Core Concepts

### Associative Memory Mapping

The ReContext framework establishes a precise correspondence between LLM mechanisms and biological memory:

| LLM Component | Neuroscience Analog | Function |
|--------------|-------------------|----------|
| Context window | Memory store | Repository of stored information traces |
| Query/question | Retrieval cue | Signal that activates relevant memory traces |
| Attention weights | Cue-trace association | Strength of connection between cue and stored memory |
| Evidence replay | Trace reactivation | Re-presentation of activated memories to strengthen retrieval |

### Key Mechanisms

1. **Evidence Pool Construction**: Uses model-internal relevance signals (attention patterns, hidden state similarity) to identify and extract the most relevant evidence from long context
2. **Recursive Selection**: Iteratively refines evidence selection by re-running the relevance computation on the selected subset
3. **Trace Reactivation**: Replays selected evidence before final generation, preserving full original context while emphasizing key information

## Usage Patterns

### Pattern 1: Long-Context Reasoning Enhancement
When an LLM needs to reason over documents >100K tokens:
1. Extract relevance signals from the model's attention patterns
2. Build a query-conditioned evidence pool from top-k relevant segments
3. Recursively refine by re-computing relevance on the evidence pool
4. Concatenate: [original context] + [refined evidence pool] + [generation prompt]
5. Generate final answer with enhanced evidence utilization

### Pattern 2: Evidence-Based QA
For questions requiring specific evidence from long documents:
1. Identify query keywords and semantic similarity to context segments
2. Score each segment by attention-based relevance to query
3. Select top segments forming the evidence pool
4. Replay evidence before generation to prime the model

### Pattern 3: Neuroscience-Inspired Memory Systems
When building AI memory architectures:
1. Model the context window as a Hopfield-like associative memory
2. Use attention as the retrieval mechanism (cue-trace association)
3. Implement replay cycles to strengthen weak memory traces
4. Apply recursive selection to handle interference between competing traces

## Instructions for Agents

### Step 1: Evidence Identification
- Parse the input context into meaningful segments (paragraphs, sections, or logical units)
- For each segment, compute relevance to the query using:
  - Attention weight aggregation from transformer layers
  - Cosine similarity between query embedding and segment embeddings
  - Cross-attention scores if available

### Step 2: Evidence Pool Construction
- Rank segments by relevance score
- Select top-k segments (k typically 5-20 depending on context length)
- Ensure diversity: avoid selecting redundant segments that cover the same information

### Step 3: Recursive Refinement
- Re-compute relevance scores using the evidence pool as the new context
- This allows the model to identify sub-evidence within already-selected evidence
- Repeat 1-2 times (diminishing returns beyond 2 iterations)

### Step 4: Generation with Replayed Evidence
- Format: `[Full original context]` + `\n\n**Key Evidence:**\n` + `[Refined evidence pool]` + `\n\n` + `[Original query]`
- The full context preserves completeness; the evidence pool primes relevant information

## Error Handling

### Evidence Pool Too Small
- If recursive refinement reduces evidence pool below 2 segments, stop recursion
- Use the pool from the previous iteration instead

### Irrelevant Evidence Selected
- Apply a relevance threshold (e.g., top 5% of attention weights)
- Use diversity constraints to prevent concentration on a single topic

### Context Window Overflow
- If evidence pool + original context exceeds token limit, prioritize evidence pool
- Truncate original context to fit while preserving evidence pool integrity

## Resources

- Paper: "ReContext: Recursive Evidence Replay as LLM Harness for Long-Context Reasoning" (arXiv: 2607.02509)
- Code: https://github.com/Yanjun-Zhao/ReContext
- Related neuroscience: Associative memory theory, Hopfield networks, memory consolidation

## Related Skills

- `agent-memory-framework` — memory architecture design
- `brain-inspired-memory-agents` — neuroscience-inspired memory systems
- `context-selective-multimodal-memory` — context-selective memory retrieval
- `worldkv-world-memory` — world model memory systems
- `hippocampal-replay-credit-assignment` — hippocampal replay mechanisms
