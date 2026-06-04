---
name: self-organising-transformer
description: "Self-organising transformer architectures that determine their own structure during training. DDCL-INCRT pattern with hierarchical prototype structure. Use when designing adaptive neural architectures, self-organising networks, or architectures that evolve structure. Activation: self-organising transformer, DDCL, adaptive architecture, self-organising network, 自组织架构, prototype learning."
---

# Self-Organising Transformer Architecture

Architecture that determines its own structure during training, combining Deep Dual Competitive Learning (DDCL) with incremental representation.

## Core Innovation

Traditional transformers have fixed architecture. DDCL-INCRT learns the optimal structure:
- **DDCL**: Replaces feedforward blocks with learned prototype vectors
- **INCRT**: Incrementally builds representation hierarchy
- **Self-determination**: Network discovers its own optimal structure

## Key Components

### 1. Deep Dual Competitive Learning (DDCL)

```python
# Instead of fixed feedforward:
# x -> Linear -> ReLU -> Linear -> output

# DDCL uses learned prototypes:
# x -> match_prototypes(x) -> select_best -> combine -> output

class DDCLBlock:
    prototypes: Tensor  # Learned dictionary of patterns
    
    def forward(x):
        # Competitive learning: match input to prototypes
        similarities = cosine_similarity(x, self.prototypes)
        best_matches = top_k(similarities)
        return weighted_combination(best_matches)
```

### 2. Hierarchical Prototype Structure

Multi-level prototypes capture patterns at different scales:
- **Level 1**: Basic features (edges, textures)
- **Level 2**: Combinations (shapes, parts)
- **Level 3**: High-level concepts

### 3. Self-Organising Mechanism

Architecture evolves during training:
- Add prototypes when novelty detected
- Merge similar prototypes for efficiency
- Prune unused prototypes
- Adjust hierarchy depth

## Implementation Patterns

### Pattern 1: Replace Transformer FFN

```python
class SelfOrganisingTransformer(nn.Module):
    def __init__(self, d_model, n_prototypes):
        self.ddcl = DDCLBlock(d_model, n_prototypes)
        
    def forward(self, x):
        # Attention remains standard
        attn_out = self.attention(x)
        # FFN replaced by DDCL
        return self.ddcl(attn_out)
```

### Pattern 2: Incremental Hierarchy

```python
# Start with minimal structure
# Grow during training based on data complexity

def grow_hierarchy(model, data):
    novelty_score = compute_novelty(data, model.prototypes)
    if novelty_score > threshold:
        model.add_prototype_level()
```

### Pattern 3: Prototype Pruning

```python
# Remove unused prototypes periodically
def prune_prototypes(model):
    usage_counts = model.get_prototype_usage()
    unused = find_unused_prototypes(usage_counts)
    model.remove_prototypes(unused)
```

## Benefits

| Aspect | Fixed Architecture | Self-Organising |
|--------|-------------------|-----------------|
| Efficiency | Over-parameterized | Optimal for data |
| Adaptation | Manual tuning | Automatic |
| Interpretability | Hidden layers | Visible prototypes |
| Memory | Fixed size | Dynamic allocation |

## Activation Keywords

- self-organising transformer
- DDCL
- DDCL-INCRT
- adaptive architecture
- prototype learning
- 自组织架构
- competitive learning
- dynamic neural network

## Use Cases

1. **Adaptive models**: Networks that adjust to task complexity
2. **Interpretable AI**: Prototypes are human-readable patterns
3. **Efficient inference**: Only activate needed prototypes
4. **Incremental learning**: Add new knowledge without retraining

## Related Skills

- **transformer-architecture**: Standard transformer patterns
- **competitive-learning**: Learning with competition
- **prototype-networks**: Prototype-based models

## Resources

- arxiv.org/abs/2604.01880 - DDCL-INCRT paper
- Competitive learning literature
- Prototype networks research

## Notes

- Requires careful initialization of prototypes
- Trade-off: flexibility vs training stability
- Best for domains with clear prototype patterns