---
name: transformer-prototype-readout
description: "Use prototype-based readout layers for transformer encoders to replace pooling methods (mean pooling, class token). Avoid information collapse with learned compression mechanism. Activation: prototype readout, transformer output layer, collapse-free attention, DDCL-Attention."
---

# Transformer Prototype Readout

Improve transformer encoder output layers using prototype-based methods instead of simple pooling.

## Core Concept

Traditional transformer encoders use simple pooling (mean pooling, class tokens) to aggregate token representations. This can cause **information collapse** - losing important token-level details.

**Solution**: Use **learned prototype vectors** for compression:
- Small set of global prototypes
- Soft probabilistic matching assigns tokens to prototypes
- Preserves diversity of token information
- More expressive than fixed pooling

## Key Components

### 1. Prototype Learning

```python
# Initialize prototypes
prototypes = nn.Parameter(torch.randn(K, D))  # K prototypes, D dimensions

# Soft assignment via attention
def prototype_attention(tokens, prototypes):
    # tokens: [N, D], prototypes: [K, D]
    similarity = torch.matmul(tokens, prototypes.T)  # [N, K]
    assignment = F.softmax(similarity, dim=-1)  # [N, K]
    output = torch.matmul(assignment.T, tokens)  # [K, D]
    return output, assignment
```

### 2. Collapse-Free Mechanism

Key insight: Prototype diversity must be maintained:

```python
# Avoid collapse with regularization
def collapse_penalty(prototypes):
    # Penalize similar prototypes
    similarity = torch.matmul(prototypes, prototypes.T)
    identity = torch.eye(K)
    penalty = torch.norm(similarity - identity)
    return penalty
```

### 3. Attention-Based Assignment

Use attention mechanism for token-to-prototype matching:

```python
class PrototypeReadout(nn.Module):
    def __init__(self, num_prototypes, hidden_dim):
        super().__init__()
        self.prototypes = nn.Parameter(torch.randn(num_prototypes, hidden_dim))
        self.query_proj = nn.Linear(hidden_dim, hidden_dim)
    
    def forward(self, encoder_output):
        # encoder_output: [batch, seq_len, hidden_dim]
        queries = self.query_proj(encoder_output)  # Project tokens
        attention = torch.matmul(queries, self.prototypes.T)  # [batch, seq_len, K]
        weights = F.softmax(attention, dim=-2)  # [batch, seq_len, K]
        
        # Aggregate tokens to prototypes
        output = torch.matmul(weights.transpose(-1, -2), encoder_output)  # [batch, K, hidden_dim]
        return output, weights
```

## Implementation Guidelines

### When to Use

1. **Multi-task transformers** - Different tasks need different output representations
2. **Diverse token semantics** - Tokens have different importance (not uniform pooling)
3. **Information preservation** - Avoid losing token-level details
4. **Hierarchical outputs** - Multiple levels of abstraction

### When NOT to Use

- Simple classification tasks (single label per sequence)
- Uniform token importance (mean pooling sufficient)
- Memory constraints (prototypes add parameters)

### Best Practices

1. **Prototype count**: Start with K=2-4, increase for more diverse outputs
2. **Regularization**: Add collapse penalty to maintain prototype diversity
3. **Initialization**: Initialize prototypes from random token embeddings
4. **Fine-tuning**: Pre-train transformer first, then add prototype readout

## Related Concepts

- **Attention Pooling**: Weighted attention over tokens
- **Set Transformers**: Permutation-invariant set processing
- **Prototype Learning**: Nearest prototype classification
- **Collapse-Free Models**: Avoiding representation collapse

## Resources

- Paper: "Collapse-Free Prototype Readout Layer for Transformer Encoders" (2604.03850v1)
- DDCL-Attention: Prototype-based readout with attention mechanism

## Usage Examples

### Example: Multi-task Transformer

```python
class MultiTaskTransformer(nn.Module):
    def __init__(self, base_model, num_prototypes=4):
        super().__init__()
        self.encoder = base_model
        self.readout = PrototypeReadout(num_prototypes, hidden_dim)
        
    def forward(self, input_ids):
        encoder_output = self.encoder(input_ids)
        prototype_output, assignment = self.readout(encoder_output)
        
        # Different tasks use different prototype combinations
        task1_output = prototype_output[0]  # Use prototype 0
        task2_output = torch.mean(prototype_output[1:3], dim=0)  # Use prototypes 1-2
        
        return task1_output, task2_output
```

### Example: Hierarchical Classification

```python
# Use prototypes for hierarchical outputs
class HierarchicalClassifier(nn.Module):
    def forward(self, x):
        prototype_output = self.readout(x)  # [K, D]
        
        # Level 1: High-level category (use all prototypes)
        level1 = self.classifier_level1(torch.mean(prototype_output, dim=0))
        
        # Level 2: Fine-grained category (use individual prototypes)
        level2 = self.classifier_level2(prototype_output)
        
        return level1, level2
```

---

**Source**: arxiv paper 2604.03850v1 - "Collapse-Free Prototype Readout Layer for Transformer Encoders"
**Created**: 2026-04-07 by research-skill-creation-hourly cron job