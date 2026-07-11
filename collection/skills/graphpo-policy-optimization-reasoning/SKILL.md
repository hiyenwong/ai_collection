---
name: graphpo-policy-optimization-reasoning
description: Graph-based Policy Optimization (GraphPO) for reasoning models. Represents rollouts as DAGs, merges semantically equivalent paths, and improves advantage estimation variance through graph structure.
version: 1.0.0
tags: [reinforcement-learning, reasoning, graph-optimization, policy-optimization, DAG, RLVR]
activation_keywords: [graph-based policy, DAG rollouts, semantic equivalence, reasoning graph, advantage variance, process supervision, token budget, reasoning optimization]
---

# GraphPO: Graph-based Policy Optimization

## Overview

Reinforcement Learning framework for reasoning models that represents rollouts as directed acyclic graphs (DAGs). Merges semantically equivalent reasoning paths, reallocates budget to diverse exploration, and provides finer-grained advantage estimation than tree-based methods.

## Problem Context

Traditional RLVR (Reinforcement Learning with Verifiable Rewards) limitations:

1. **Independent sampling**: Similar intermediate steps → redundant exploration
2. **Sparse rewards**: Final-answer only → hard to identify useful steps
3. **Tree limitations**: Independent branch expansion, no cross-branch sharing
4. **High variance**: Local comparisons within separate branches

## Core Methodology

### 1. DAG Representation of Rollouts

```
Traditional: Chain → Tree → DAG

Chain: step1 → step2 → step3 → step4
Tree:  step1 → [step2a, step2b] → [step3a, step3b, step3c]
DAG:   nodes (semantic states) + edges (reasoning steps)
```

#### Graph Construction
```python
# Nodes: Semantic states (summarized from reasoning paths)
node = summarize_semantic_state(reasoning_path)

# Edges: Individual reasoning steps
edge = reasoning_step

# Directed Acyclic Graph structure
graph = {
    nodes: [state_1, state_2, ..., state_n],
    edges: [(state_i, step, state_j)]
}
```

### 2. Semantic Equivalence Merging

#### Key Innovation
When different branches reach **similar reasoning states**:
- Tree: Continue independently (duplicate work)
- Graph: **Merge into equivalence classes**, share suffixes

```python
def merge_equivalent_states(graph, similarity_threshold=0.95):
    # Identify semantically equivalent nodes
    equivalence_classes = {}
    
    for node in graph.nodes:
        # Semantic similarity check
        for existing_class in equivalence_classes:
            if semantic_similarity(node, existing_class) > threshold:
                equivalence_classes[existing_class].add(node)
                break
        else:
            equivalence_classes[node] = {node}
    
    # Merge paths, share suffixes
    merged_graph = merge_paths(equivalence_classes)
    return merged_graph
```

### 3. Budget Reallocation Strategy

```
Redundant budget → Diverse exploration

# Before: Multiple branches explore same state
for branch in branches:
    if same_state:
        explore_branch(state)  # Repeated work

# After: Single exploration + share
merged_state = merge_equivalent(states)
explore_once(merged_state)
share_to_all_origins(merged_state)
```

### 4. Advantage Assignment

#### Efficiency Advantages (Incoming Edges)
```
# Edges leading to efficient reasoning
efficiency_score = path_length / token_count

# Incoming edges get efficiency advantage
for edge in incoming_edges(node):
    advantage_efficiency = efficiency_score * edge_weight
```

#### Correctness Advantages (Outgoing Edges)
```
# Edges leading to correct answers
correctness_score = answer_accuracy

# Outgoing edges get correctness advantage
for edge in outgoing_edges(node):
    advantage_correctness = correctness_score * edge_weight
```

### 5. Variance Reduction Theorem

**Theory**: GraphPO reduces advantage-estimation variance vs. tree methods.

```
# Tree: Independent branch comparisons
variance_tree = σ² / n_branches

# Graph: Cross-branch comparisons (merged states)
variance_graph = σ² / (n_equivalence_classes)

Since n_equivalence_classes < n_branches:
    variance_graph < variance_tree
```

## Implementation Pattern

```python
class GraphPOPolicy:
    def __init__(self, reasoning_model, reward_fn):
        self.model = reasoning_model
        self.reward = reward_fn
        self.graph = ReasoningGraph()
        
    def optimize(self, query, token_budget):
        # Generate rollouts
        rollouts = self.model.sample_rollouts(query, n_samples)
        
        # Build DAG
        self.graph.build_from_rollouts(rollouts)
        
        # Merge equivalent states
        self.graph.merge_semantic_states(threshold=0.95)
        
        # Reallocate budget
        self.graph.reallocate_budget(token_budget)
        
        # Compute graph advantages
        advantages = self.compute_graph_advantages()
        
        # Update policy
        self.update_policy(advantages)
        
    def compute_graph_advantages(self):
        # Efficiency advantages (incoming)
        for edge in self.graph.incoming_edges():
            efficiency = self.graph.get_path_efficiency(edge)
            edge.advantage += efficiency
        
        # Correctness advantages (outgoing)
        for edge in self.graph.outgoing_edges():
            correctness = self.reward(edge.destination)
            edge.advantage += correctness
        
        return self.graph.get_advantages()
```

## Key Benefits

1. **Reduced variance**: Cross-branch comparisons via merged states
2. **Efficient exploration**: Budget reallocation to diverse paths
3. **Process supervision**: Derive from outcome via edge advantages
4. **Token-budget control**: Explicit budget management

## Performance

- Consistent improvements over chain/tree baselines
- Same token budget or response budget
- Tested on 3 LLMs across reasoning + agentic search benchmarks

## Use Cases

- Reasoning model fine-tuning
- Agentic search optimization
- Multi-path reasoning
- RLVR improvements
- Efficient policy optimization

## Reference

- Paper: "GraphPO: Graph-based Policy Optimization for Reasoning Models" (arXiv:2606.18954v1)
- Authors: Yuliang Zhan et al. (2026-06-17)