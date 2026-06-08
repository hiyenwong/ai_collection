---
name: qpredsgg-hybrid-quantum-predicate
category: quantum
description: Hybrid quantum predicate classifier for long-tailed scene graph generation. Replaces classical predicate head with QP-Head using amplitude embedding + strongly entangling layers.
arxiv: 2606.04689
published: 2026-06-03
categories: quant-ph, cs.LG
activation: "qpredsgg, quantum-predicate, scene-graph, long-tail, hybrid-quantum, q-head, amplitude-embedding, strongly-entangling"
---

# QPredSGG: Hybrid Quantum Predicate Learning for Long-Tailed Scene Graph Generation

## Overview

QPredSGG introduces a **hybrid quantum predicate classifier** for scene graph generation that replaces the classical predicate head in Causal Feature Enhancement Network (CFEN) with a Quantum Predicate Head (QP-Head). This achieves superior long-tail performance with dramatically fewer parameters.

## Core Methodology

### Architecture
- **Classical backbone**: CFEN extracts object features
- **Quantum head**: QP-Head replaces classical predicate classifier
- **Feature compression**: 4096D → 16D quantum-compatible (256× reduction)
- **Training**: Weighted cross-entropy loss for long-tail imbalance

### Quantum Circuit Design
- **Encoding**: Amplitude Embedding for compact state preparation
- **Layers**: Strongly Entangling Layers for relational reasoning
- **Measurement**: Pauli-Z observables for predicate classification

### Performance Results
| Configuration | mR@100 | Parameters | Notes |
|--------------|--------|-----------|-------|
| Classical CFEN | 41.1% | - | Baseline |
| 4-qubit QP-Head | 57.25% | 96 | Best result |
| 8-qubit QP-Head | 55.38% | 384 | Strong long-tail |

### Key Findings
1. **Parameter efficiency**: 96 quantum params outperform classical reference
2. **Compression**: 256× feature reduction maintains relational accuracy
3. **Depth trade-off**: Expressibility vs runtime overhead analysis
4. **Long-tail improvement**: Significant gains on rare predicates

## Implementation Patterns

### Hybrid Quantum-Classical Pipeline
```
Object Features (4096D) 
    ↓
Amplitude Embedding
    ↓
Strongly Entangling Layers
    ↓
Pauli-Z Measurement
    ↓
Predicate Classification
```

### When to Use

- Scene graph generation with long-tail predicate distributions
- Parameter-efficient relational reasoning
- Hybrid quantum-classical computer vision pipelines
- Visual reasoning tasks requiring fine-grained semantic classification

## Pitfalls

- Qubit count doesn't monotonically improve performance (4 > 8 qubits)
- Runtime overhead increases with circuit depth
- Amplitude embedding requires careful normalization
- Strongly entangling layers may overfit on small predicate sets

## Verification Steps

1. Validate amplitude embedding normalization (unit vector constraint)
2. Check entangling layer depth vs expressibility trade-off
3. Evaluate long-tail predicate recall specifically
4. Compare parameter efficiency against classical baselines

## Research Directions

- Hybrid architectures for other relational reasoning tasks
- Quantum predicate heads for video scene understanding
- Integration with larger vision-language models
- Transfer learning across visual reasoning domains
