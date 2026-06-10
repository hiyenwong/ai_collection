---
name: trajectory-geometry-transformer-representations
description: Trajectory Geometry methodology for understanding transformer representations across layers. Uses computational neuroscience tools (trajectory length, curvature, semantic convergence, layerwise similarity) for probe-free mechanistic interpretability. Applicable to GPT-2, TinyLlama, Qwen2.5. Reveals attractor-like dynamics, computational complexity encoding, and universal three-phase structure.
category: ai_collection
tags: [transformer, interpretability, computational-neuroscience, trajectory-geometry, mechanistic-interpretability, representation-manifold]
activation_keywords: [trajectory geometry, transformer representations, mechanistic interpretability, probe-free, layer dynamics, attractor dynamics]
arxiv_id: 2606.09287
authors: [Vishal Pandey, Gopal Singh]
published: 2026-06-08
paper_link: https://arxiv.org/abs/2606.09287
---

# Trajectory Geometry of Transformer Representations Across Layers

## Overview

This methodology recasts the transformer forward pass as a **discrete population trajectory** through a high-dimensional representation manifold, drawing on geometric tools from computational neuroscience. Unlike traditional probing approaches that search for pre-specified features, this framework characterizes trajectory geometry directly in the ambient representation space.

**Core Innovation**: Probe-free mechanistic interpretability through trajectory metrics.

## Key Metrics

### 1. Trajectory Length
Measures the total distance traveled through representation space across layers.

### 2. Curvature
Quantifies trajectory bending - encoding computational complexity:
- **Reasoning tasks**: Higher curvature (0.71-0.83 rad)
- **Lexical variations**: Lower curvature (0.27-0.31 rad)

### 3. Semantic Convergence Index (CI)
Measures how semantically related prompts converge in representation space:
- Peak convergence in middle-to-late layers (CI 0.41-0.58, p<0.001)
- Evidence of **attractor-like dynamics**

### 4. Layerwise Cosine Similarity
Captures representational similarity between adjacent layers.

### 5. Representational Stability
Measures trajectory consistency across different prompts.

## Key Findings

### Finding 1: Attractor-like Dynamics
- Semantically related prompts **converge significantly** in middle-to-late layers
- Peak semantic convergence index: 0.41-0.58
- Statistical significance: p<0.001 (Mann-Whitney U test)

### Finding 2: Curvature Encodes Computational Complexity
- Reasoning tasks produce trajectories with **greater curvature** (0.71-0.83 rad)
- Lexical variations produce lower curvature (0.27-0.31 rad)
- **Interpretation**: Curvature reflects computational demands

### Finding 3: Trajectory Bifurcation for Ambiguous Tokens
- Ambiguous tokens show **representational bifurcation**
- Up to **5.6x separation** by final layer
- Absent in unambiguous control tokens
- **Implication**: Disambiguation through trajectory divergence

### Finding 4: Universal Three-Phase Structure
All tested architectures (GPT-2, TinyLlama, Qwen2.5) exhibit:
1. **Encoding Phase** (early layers): Input processing
2. **Elaboration Phase** (middle layers): Semantic refinement
3. **Output Preparation Phase** (late layers): Response generation

## Methodology Details

### Data
- **Model Families**: GPT-2, TinyLlama, Qwen2.5
- **Prompt Families**: 5 controlled categories
- **Control Experiments**: Shuffled-layer, random-embedding controls

### Validation
- All effects **vanish under control conditions**
- Confirms trajectory geometry reflects genuine model dynamics

### Implementation Pipeline
- **Fully open-source**
- **Model-agnostic**
- Available with paper publication

## When to Use

### Applicable Scenarios
1. **Mechanistic interpretability research**: Understanding transformer dynamics without probes
2. **Layer-wise analysis**: Investigating how representations evolve across layers
3. **Semantic convergence studies**: Measuring how similar inputs converge
4. **Computational complexity analysis**: Relating task difficulty to trajectory geometry
5. **Disambiguation tracking**: Following how ambiguous inputs resolve

### Model Types
- Transformers with multiple layers
- Decoder-only language models (GPT architecture)
- Encoder-decoder models (adaptation required)

## Technical Implementation

### Basic Workflow
```
1. Extract hidden states from each layer for given input
2. Compute trajectory metrics:
   - Length: Sum of distances between consecutive layer states
   - Curvature: Angle changes along trajectory
   - CI: Inter-trajectory distances for semantic pairs
   - Layerwise similarity: Cosine between adjacent layers
3. Compare across prompt families and conditions
4. Validate with control experiments
```

### Computational Requirements
- Access to model hidden states
- Memory: Proportional to layers × sequence length × hidden dimension
- Compute: O(L) for trajectory length, O(L²) for curvature metrics

## Advantages over Traditional Probing

### Probe-free Approach
- ✅ No need to define target features beforehand
- ✅ Works directly in representation space
- ✅ Captures emergent dynamics

### Comprehensive Analysis
- ✅ Multiple complementary metrics
- ✅ Cross-layer evolution captured
- ✅ Temporal dynamics (trajectory through layers)

### Validation Framework
- ✅ Built-in control experiments
- ✅ Statistical significance testing
- ✅ Model-agnostic applicability

## Limitations

1. **High-dimensional space**: Visualization requires dimensionality reduction
2. **Layer discretization**: Continuous dynamics approximated by discrete samples
3. **Computational cost**: Full trajectory analysis for long sequences
4. **Interpretation**: Metrics require careful interpretation for specific models

## Related Work

### Computational Neuroscience Foundations
- Population trajectory analysis in neural systems
- Attractor dynamics in neural networks
- Geometric methods for neural data

### AI Interpretability Connections
- Probing classifiers
- Layer-wise relevance propagation
- Representation analysis methods

## Practical Applications

### 1. Model Debugging
Identify anomalous trajectory patterns indicating model issues.

### 2. Architecture Comparison
Compare trajectory dynamics across different transformer architectures.

### 3. Task Difficulty Assessment
Use curvature as proxy for computational complexity of tasks.

### 4. Semantic Similarity Studies
Track convergence/divergence of semantically related inputs.

### 5. Disambiguation Analysis
Monitor how ambiguous inputs resolve through layers.

## Key Papers & References

### Primary Source
- **arXiv:2606.09287** - Trajectory Geometry of Transformer Representations Across Layers (Pandey & Singh, 2026)

### Related Computational Neuroscience
- Population trajectory analysis methodologies
- Geometric approaches to neural dynamics
- Attractor theory in neural networks

### Transformer Interpretability
- Probing methods comparison
- Layer-wise analysis frameworks
- Mechanistic interpretability toolkits

## Future Directions

1. **Dynamic trajectory analysis**: Time-varying metrics during training
2. **Cross-model comparison**: Systematic trajectory geometry across architectures
3. **Task-specific patterns**: Characterizing trajectory signatures for different tasks
4. **Intervention studies**: Testing trajectory changes under model modifications
5. **Visualization tools**: Better methods for high-dimensional trajectory display

## Summary

Trajectory Geometry provides a principled, probe-free lens for understanding transformer representations. By recasting the forward pass as a trajectory through representation manifold, we can:

- **Measure** computational complexity (curvature)
- **Detect** semantic convergence (attractor dynamics)
- **Track** disambiguation (trajectory bifurcation)
- **Identify** universal processing phases (three-phase structure)

This neuroscience-inspired approach offers complementary insights to traditional probing methods, enabling deeper understanding of transformer dynamics.