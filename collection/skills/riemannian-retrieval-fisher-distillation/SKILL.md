---
name: riemannian-retrieval-fisher-distillation
description: Information-geometry unified memory architecture combining Riemannian retrieval (Fisher-Rao metric) with Fisher-guided discrete token distillation for resource-efficient long-term memory in dialogue agents.
version: 1.0.0
tags: [retrieval, distillation, information-geometry, riemannian, fisher-information, memory, edge-computing]
activation_keywords: [riemannian, fisher information, fisher-rao metric, mahalanobis distance, long-term memory, edge memory, dialogue memory, hubness problem, woodbury acceleration, syntax protection]
---

# CoreMem: Riemannian Retrieval + Fisher-Guided Distillation

## Overview

Information-geometry unified architecture for edge-cloud memory systems. Replaces isotropic cosine similarity with locally adaptive Fisher-Rao metric, and provides principled compression through Fisher information-guided token distillation.

## Problem Context

- **Edge deployment constraint**: 8 GB VRAM budget
- **Hubness problem**: High-dimensional retrieval favors frequent items
- **Syntactic fragmentation**: Heuristic compression breaks sentence structure
- **Lack of unified theory**: Isolated solutions without mathematical foundation

## Core Methodology

### 1. Riemannian Retrieval (Fisher-Rao Metric)

#### Traditional Approach (Cosine Similarity)
```python
similarity = dot(a, b) / (norm(a) * norm(b))
# Problem: Isotropic, hubness-prone, no adaptivity
```

#### Fisher-Rao Metric (Locally Adaptive)
```python
# Mahalanobis distance with local covariance
distance = sqrt((x - y)^T * Σ^{-1} * (x - y))

# Fisher-Rao metric on statistical manifold
metric = Fisher_information_matrix(θ)

# Advantages:
# 1. Penalizes hub memories (high-variance directions)
# 2. Adaptively rescales based on local density
# 3. Information-geometric optimality
```

#### Woodbury Acceleration
```
# O(Ndr) instead of O(Nd²) for N memories
Σ^{-1} = Σ₀^{-1} - Σ₀^{-1} U (I + V Σ₀^{-1} U)^{-1} V Σ₀^{-1}

where:
- Σ₀: Prior covariance (precomputed)
- U, V: Incremental updates from new memories
- d: embedding dimension
- r: rank of update (r << d)
```

### 2. Fisher-Guided Discrete Token Distillation (FDTD)

#### Hierarchical Compression
```
Sentence-level → Token-level

# Step 1: Sentence sensitivity scores
sentence_sensitivity = trace(Fisher_info_sentence)

# Step 2: Token-level sensitivity within sentences
token_sensitivity = Fisher_info_trace_per_token

# Step 3: Compression with KL tradeoff
compressed = select_tokens(sentence_sensitivity, token_sensitivity, 
                           KL_budget, syntax_protection=True)
```

#### Fisher Information Trace
```python
def compute_sensitivity(model, context, tokens):
    """
    Fisher information trace = Σ_i (∂log p/∂θ_i)²
    Higher trace = more informative tokens
    """
    log_prob = model.log_prob(tokens, context)
    gradient = compute_gradient(log_prob, model.params)
    
    # Fisher information approximation
    sensitivity = gradient.T @ gradient  # Diagonal approximation
    
    return trace(sensitivity)
```

#### Syntax Protection Mechanism
```
# Protected syntax regions (cannot compress)
protected_regions = {
    "subject_verb": [begin:end],
    "noun_phrase": [begin:end],
    "predicate": [begin:end]
}

# Only compress non-protected tokens
compression_mask = ~is_protected(token_position)
```

### 3. Compression-KL Tradeoff

```
Objective: minimize KL(memory_compressed || memory_full)
           subject to VRAM_budget

Solution:
1. Compute sensitivity scores (Fisher traces)
2. Rank tokens by sensitivity
3. Greedy selection with syntax constraints
4. Verify KL divergence < threshold
```

## Implementation Pattern

```python
class CoreMemMemory:
    def __init__(self, embedding_dim=768, vram_budget=8GB):
        self.metric = FisherRaoMetric(embedding_dim)
        self.distillation = FDTD(vram_budget)
        
    def retrieve(self, query, memories):
        # Riemannian retrieval
        distances = self.metric.mahalanobis_distance(query, memories)
        # Woodbury acceleration for online updates
        return ranked_memories(distances)
    
    def compress(self, context):
        # Fisher-guided distillation
        sensitivities = self.distillation.compute_sensitivity(context)
        compressed = self.distillation.select_tokens(
            sensitivities, 
            syntax_protection=True,
            kl_budget=0.1
        )
        return compressed
```

## Key Benefits

1. **Theoretical foundation**: Information geometry unifies retrieval + compression
2. **Hubness mitigation**: Mahalanobis distance penalizes frequent items
3. **Real-time**: O(Ndr) Woodbury acceleration
4. **Syntax preservation**: Structural protection in compression
5. **Edge-compatible**: Operates within 8 GB VRAM

## Performance

- Open-domain reasoning: +4.51 pp
- Temporal reasoning: +4.17 pp
- Strict 8 GB VRAM constraint satisfied
- Benchmarks: LOCOMO, LongMemEval-S

## Use Cases

- Long-term dialogue memory
- Edge-deployed conversational agents
- Resource-constrained memory systems
- Privacy-preserving local memory
- Lifetime learning agents

## Reference

- Paper: "CoreMem: Riemannian Retrieval and Fisher-Guided Distillation for Long-Term Memory in Dialogue Agents" (arXiv:2606.18406v1)
- Authors: Jiaqi Chen et al. (2026-06-16)