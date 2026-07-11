---
name: fase-semantic-entropy-code
description: "Fast Adaptive Semantic Entropy (FASE) methodology for quantifying uncertainty in multi-agent code generation. Approximates functional correctness via minimum spanning tree of structural and semantic dissimilarity graphs, achieving 25% improvement in Spearman correlation and 19% increase in ROCAUC over LLM-driven semantic entropy, at ~0.3% of the computational cost. Activation: semantic entropy, code uncertainty, multi-agent code quality, FASE, functional correctness estimation."
category: software-engineering
source: arxiv
arxiv_id: "2606.09800"
paper_title: "FASE: Fast Adaptive Semantic Entropy for Code Quality"
paper_authors: "Shizhe Lin, Ladan Tahvildari"
trigger: ["semantic entropy code", "FASE", "fast adaptive semantic entropy", "code quality uncertainty", "multi-agent code generation", "functional correctness estimation", "code uncertainty quantification"]
version: "1.0.0"
created: "2026-06-09"
---

# FASE: Fast Adaptive Semantic Entropy for Code Quality

## Overview

FASE (Fast Adaptive Semantic Embedding) is a novel metric for quantifying uncertainty in multi-agent code generation workflows. It approximates functional correctness based on the minimum spanning tree (MST) of structural and semantic dissimilarity graphs, eliminating the need for costly LLM-driven equivalence checks used by traditional semantic entropy methods.

**Key Results (arXiv:2606.09800):**
- 25% average improvement in Spearman correlation vs. LLM-based semantic entropy
- 19% increase in ROCAUC score against Pass@1 from ground-truth test cases
- Requires only ~0.3% of the runtime cost of traditional semantic entropy approaches
- Evaluated on HumanEval and BigCodeBench using Qwen3-Embedding-8B model

## Core Methodology

### 1. Structural Dissimilarity Graph

Build a graph where nodes are generated code samples and edges encode structural dissimilarity:

- Parse code into AST (Abstract Syntax Tree)
- Compute structural distance between ASTs (tree edit distance, node type distribution)
- Weight edges by structural dissimilarity

### 2. Semantic Dissimilarity Graph

Using embedding models (e.g., Qwen3-Embedding-8B):

- Embed each code sample into a semantic vector space
- Compute pairwise cosine distances between embeddings
- Weight edges by semantic dissimilarity

### 3. Minimum Spanning Tree (MST) Entropy

The key innovation:

- Combine structural and semantic graphs into a unified dissimilarity graph
- Compute the MST of this combined graph
- MST total weight serves as a proxy for semantic entropy:
  - **Low MST weight**: samples cluster tightly → high confidence in correctness
  - **High MST weight**: samples are scattered → high uncertainty, likely hallucination

### 4. Adaptive Thresholding

- Use the MST weight distribution to adaptively set confidence thresholds
- No ground-truth test cases required at inference time
- Calibrate thresholds on a small validation set

## Implementation Steps

### Step 1: Generate Multiple Code Samples

```python
# Generate N code samples from the multi-agent system
samples = generate_code_samples(prompt, n=10)
```

### Step 2: Build Structural Dissimilarity Matrix

```python
import ast
import numpy as np

def ast_distance(code_a, code_b):
    """Compute structural distance between two code samples."""
    tree_a = ast.parse(code_a)
    tree_b = ast.parse(code_b)
    # Use tree edit distance or node-level features
    features_a = extract_ast_features(tree_a)
    features_b = extract_ast_features(tree_b)
    return np.linalg.norm(features_a - features_b)

def build_structural_matrix(samples):
    n = len(samples)
    matrix = np.zeros((n, n))
    for i in range(n):
        for j in range(i+1, n):
            d = ast_distance(samples[i], samples[j])
            matrix[i, j] = matrix[j, i] = d
    return matrix
```

### Step 3: Build Semantic Dissimilarity Matrix

```python
from sentence_transformers import SentenceTransformer

def build_semantic_matrix(samples, model_name="Qwen/Qwen3-Embedding-8B"):
    model = SentenceTransformer(model_name)
    embeddings = model.encode(samples)
    # Cosine distance matrix
    from sklearn.metrics.pairwise import cosine_distances
    return cosine_distances(embeddings)
```

### Step 4: Compute MST Entropy

```python
from scipy.sparse.csgraph import minimum_spanning_tree

def compute_fase_entropy(structural_matrix, semantic_matrix, alpha=0.5):
    """
    Compute FASE entropy from combined dissimilarity graph.
    alpha: weight balancing structural vs semantic dissimilarity.
    """
    combined = alpha * structural_matrix + (1 - alpha) * semantic_matrix
    mst = minimum_spanning_tree(combined)
    # MST total weight = FASE entropy
    return mst.sum()
```

### Step 5: Adaptive Confidence Scoring

```python
def fasi_confidence_score(fase_entropy, threshold_low, threshold_high):
    """
    Convert FASE entropy to confidence score.
    Low entropy → high confidence (samples agree).
    High entropy → low confidence (samples diverge).
    """
    if fase_entropy < threshold_low:
        return 1.0  # High confidence
    elif fase_entropy > threshold_high:
        return 0.0  # Low confidence
    else:
        return 1.0 - (fase_entropy - threshold_low) / (threshold_high - threshold_low)
```

## When to Use

Use FASE methodology when:
- Running **multi-agent code generation** workflows
- Need **uncertainty quantification** without ground-truth test cases
- **LLM-based semantic entropy** is too costly (computationally or financially)
- Want to **filter hallucinated code** before deployment
- Optimizing **real-time multi-agent pipelines** for code quality

## Key Concepts

| Concept | Description |
|---------|-------------|
| Semantic Entropy | Measures disagreement among multiple generated samples |
| MST Weight | Total weight of minimum spanning tree — proxy for sample divergence |
| Structural Dissimilarity | AST-based code structure comparison |
| Semantic Dissimilarity | Embedding-based code meaning comparison |
| FASE Score | Combined MST entropy → confidence in code correctness |

## Comparison with Existing Approaches

| Aspect | LLM Entailment | Test-Based | FASE |\n|--------|---------------|------------|------|\n| Cost per Sample | High (LLM calls) | Medium (test execution) | Very Low (~0.3%) |\n| Ground Truth Needed | No | Yes | No |\n| Spearman Correlation | Baseline | Reference | +25% over baseline |\n| ROCAUC | Baseline | Reference | +19% over baseline |\n| Scalability | Poor | Good | Excellent |\n\n## Pitfalls

- **Embedding Model Choice**: Results depend on code embedding quality. Qwen3-Embedding-8B was validated in the paper; other models may need recalibration.
- **Alpha Tuning**: The structural vs semantic balance (alpha) may need adjustment for different code domains.
- **Threshold Calibration**: Confidence thresholds should be calibrated on a domain-specific validation set.
- **AST Parsing**: Some generated code may be syntactically invalid and fail AST parsing — handle gracefully.

## Research Context

**Paper:** FASE: Fast Adaptive Semantic Entropy for Code Quality (arXiv:2606.09800)
**Authors:** Shizhe Lin, Ladan Tahvildari
**Date:** June 2026
**Categories:** cs.SE, cs.AI, cs.MA
**Benchmarks:** HumanEval, BigCodeBench

## Related Skills

- adversarial-testing-framework
- agent-integration-testing
- validation-driven-llm-workflow

## Activation

Keywords: semantic entropy, code uncertainty, multi-agent code quality, FASE, functional correctness estimation, fast adaptive semantic entropy, code generation uncertainty, MST entropy code
