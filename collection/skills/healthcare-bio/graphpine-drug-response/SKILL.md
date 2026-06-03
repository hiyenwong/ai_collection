---
name: graphpine-drug-response
description: Graph Importance Propagation (GraphPINE) methodology for interpretable drug response prediction. Propagates importance scores through biological knowledge graphs to constrain explanations to biologically relevant structures. Activation: drug response prediction, interpretable ML, graph importance propagation, biomedical explainability, pharmacogenomics.
---

# GraphPINE: Interpretable Drug Response Prediction

## Overview

Based on arXiv:2504.05454 — **Graph Importance Propagation for Interpretable Drug Response Prediction**. Addresses a critical gap in biomedical explainability: existing methods (attention, gradients, Shapley values) do not handle data with strong prior knowledge and fail to constrain explanations to biologically relevant structures.

## Core Problem

Standard explainability methods for drug response prediction:
- **Attention weights**: Highlight features but don't respect biological pathway structure
- **Gradient-based**: Identify influential features but produce noisy, uninterpretable attributions
- **Shapley values**: Computationally expensive and ignore known biological relationships

GraphPINE solves this by **propagating importance scores through biological knowledge graphs**, ensuring explanations align with known drug-gene-pathway relationships.

## Methodology

### Graph Construction

```
Drug ──→ Target Gene ──→ Pathway ──→ Cellular Response ──→ Clinical Outcome
         (PPI edges)    (KEGG/Reactome)
```

- **Nodes**: Drugs, genes, pathways, cellular features
- **Edges**: Known biological relationships (PPI, pathway membership, drug-target)
- **Prior knowledge**: Constrains importance propagation to biologically plausible paths

### Importance Propagation

```python
# 1. Compute initial importance scores (e.g., gradient-based)
initial_scores = compute_feature_importance(model, drug_features)

# 2. Propagate through knowledge graph
for step in range(num_steps):
    for node in graph.nodes:
        propagated_score = 0
        for neighbor in graph.neighbors(node):
            edge_weight = graph.edge_weight(neighbor, node)
            propagated_score += edge_weight * node_scores[neighbor]
        # Blend original and propagated
        node_scores[node] = α * initial_scores[node] + (1-α) * propagated_score

# 3. Normalize to produce interpretable explanations
explanations = normalize(node_scores)
```

### Key Properties

1. **Structure-constrained**: Explanations follow known biological pathways
2. **Transductive**: Leverages graph structure during both training and explanation
3. **Prior-aware**: Existing knowledge guides what explanations are plausible
4. **Computationally efficient**: Propagation is O(|E|) per step

## Implementation Pattern

```python
class GraphPINE:
    def __init__(self, knowledge_graph, alpha=0.3, steps=5):
        self.graph = knowledge_graph
        self.alpha = alpha  # Blend between raw and propagated
        self.steps = steps
    
    def explain(self, model, features):
        raw_scores = self.compute_initial_importance(model, features)
        scores = raw_scores.copy()
        
        for _ in range(self.steps):
            scores = self.propagate(scores)
            scores = self.alpha * raw_scores + (1 - self.alpha) * scores
        
        return self.normalize(scores)
    
    def propagate(self, scores):
        new_scores = scores.copy()
        for node in self.graph.nodes:
            neighbors = self.graph.get_neighbors(node)
            for n in neighbors:
                w = self.graph.get_weight(n, node)
                new_scores[node] += w * scores[n]
        return new_scores
```

## When to Use

- Drug response prediction in cancer/precision medicine
- Pharmacogenomics with known gene-drug interactions
- Any biomedical ML where explanations must respect domain knowledge
- Situations where standard SHAP/LIME produce biologically implausible explanations

## Pitfalls

- Knowledge graph quality directly constrains explanation quality
- Missing edges in the graph may hide important mechanisms
- Propagation depth must be tuned — too shallow misses indirect effects, too deep dilutes signal
- α parameter balances fidelity vs. interpretability — requires validation

## Related Papers

- 2504.05454: GraphPINE: Graph Importance Propagation for Interpretable Drug Response Prediction
- 2605.19050: Generative Pseudo-Force Fields for Molecular Generation
