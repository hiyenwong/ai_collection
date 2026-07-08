---
name: representation-steering
description: "LLM representation steering and activation patching methodology for mechanistic interpretability. Use when analyzing how steering vectors affect LLM internals, conducting activation patching experiments, or investigating causal mechanisms in neural networks. Keywords: representation steering, activation patching, mechanistic interpretability, steering vectors, OV circuit, QK circuit, refusal steering."
---

# Representation Steering Skill

## Description
Framework for analyzing and applying steering vectors to LLMs, based on mechanistic interpretability methods from recent research.

## Activation Keywords
- representation steering
- activation patching
- mechanistic interpretability
- steering vectors
- OV circuit analysis
- QK circuit analysis
- refusal steering
- 机制可解释性
- 表示转向
- 激活修补

## Tools Used
- `exec`: Run Python scripts for activation analysis
- `read`: Load model configurations and weights
- `write`: Save analysis results and patching configurations

## Key Concepts

### Steering Vectors
Vectors applied to model activations to control behavior without modifying weights. Effective for alignment tasks like refusal.

### Activation Patching
Method to trace causal mechanisms by replacing activations at specific layers/positions.

### Circuit Analysis
- **OV circuit**: Output-Value pathway, where steering primarily operates
- **QK circuit**: Query-Key pathway, largely ignored by steering

## Workflow

### Step 1: Identify Target Layer
Locate layer where steering has maximal effect:
```python
# Typical effective layers: middle layers (e.g., layer 10-15 for 32-layer models)
target_layer = find_critical_layer(model, behavior_type)
```

### Step 2: Extract Steering Vector
Compute difference between positive/negative examples:
```python
steering_vector = positive_activation - negative_activation
```

### Step 3: Apply Multi-Token Patching
Apply steering across multiple tokens, not just first position:
```python
for token_pos in target_positions:
    patched_activation = activation[token_pos] + alpha * steering_vector
```

### Step 4: Analyze OV Circuit
Decompose attention contributions:
```python
ov_contribution = analyze_ov_circuit(layer_activations)
```

### Step 5: Sparsification
Reduce dimensions while preserving performance:
```python
sparse_vector = sparsify(steering_vector, keep_ratio=0.01)  # 99% sparse
```

## Findings from Research

1. **Different steering methods use interchangeable circuits** at same layer
2. **OV circuit is primary pathway** (QK frozen → only 8.75% performance drop)
3. **Steering vectors can be sparsified 90-99%** without major performance loss
4. **Semantically interpretable concepts** emerge in OV decomposition

## Error Handling

### Steering Not Effective
- Check target layer (may need adjustment)
- Increase alpha (steering magnitude)
- Verify multi-token patching is applied

### Model Instability
- Reduce alpha magnitude
- Apply to fewer layers
- Use sparse steering vector

## Resources

- Reference paper: arxiv:2604.08524
- Key finding: Freezing all attention scores drops performance by only 8.75%