---
name: hyperbolic-learning-brain-graphs
category: ai_collection
description: 超曲率脑图学习方法论，利用Lorentzian超曲空间建模脑网络层次结构，结合Graph-aware Mamba捕获长程依赖。arXiv:2607.07077，2026-07-08 更新。
source: "arXiv:2607.07077"
arxiv_id: "2607.07077"
trigger_words:
  - hyperbolic brain graph
  - lorentzian hyperbolic space
  - geometric entailment constraints
  - graph-aware mamba
  - bram network hierarchy
  - roi-community modeling
  - brain disorder diagnosis
created: "2026-07-11"
updated: "2026-07-11"
---

# Hyperbolic Learning on Brain Graphs (HLBG) for Disorder Diagnosis

> **Paper**: Li, Y. et al. "Navigating Hierarchy: Hyperbolic Learning on Brain Graphs for Disorder Diagnosis" — arXiv:2607.07077 [cs.CV], July 8, 2026

## Abstract Summary

Functional brain networks exhibit hierarchical organization across ROI, community, and whole-brain levels. Existing brain graph modeling methods struggle with ROI-community interactions, failing to exploit the full hierarchy. This paper proposes HLBG — a framework using deep hyperbolic learning to model hierarchical brain structures in Lorentzian hyperbolic space, combined with a novel Graph-aware Mamba (GaMamba) for capturing long-range dependencies while preserving graph topology.

## Key Innovations

1. **Lorentzian Hyperbolic Projection**: Projects ROI, community, and whole-brain representations into Lorentzian hyperbolic space, exploiting its natural capacity for encoding hierarchical/tree-like structures.

2. **Geometric Entailment Constraints**: Two constraints that enforce the multi-level hierarchy:
   - ROI representations are geometrically entailed by community representations
   - Community representations are geometrically entailed by whole-brain representations

3. **Graph-aware Mamba (GaMamba)**: Novel Mamba variant incorporating topology-derived structural prompts to capture long-range dependencies while preserving graph topological information.

4. **Multi-level Hierarchy Modeling**: First framework to jointly model ROI-community-whole-brain hierarchy with geometric constraints in hyperbolic space.

## Technical Framework

### Architecture Pipeline

```
Input (fMRI/EEG) → ROI Features → Community Features → Whole-brain Features
       ↓                  ↓                    ↓                    ↓
   Hyperbolic Projection (Lorentzian Space)
       ↓                  ↓                    ↓                    ↓
   Geometric Entailment Constraints
       ↓                  ↓                    ↓                    ↓
   GaMamba Processing (topology-aware)
       ↓
   Classification / Biomarker Identification
```

### Hyperbolic Space Advantages

- **Exponential volume growth**: Naturally encodes tree/hierarchical structures
- **Lorentzian model**: Mathematically rigorous hyperbolic geometry with well-defined distance, entailment, and projection operations
- **Preserves hierarchy**: Unlike Euclidean space, hyperbolic space can represent hierarchical relationships without distortion

### GaMamba Architecture

- Standard Mamba state-space model enhanced with:
  - **Topology-derived structural prompts**: Graph structure encoded as additional input
  - **Preserves graph topology**: Maintains spatial relationships during sequential processing
  - **Long-range dependencies**: Captures cross-region interactions that standard GNNs miss

## Experimental Results

| Dataset | Task | Performance |
|---------|------|------------|
| ABIDE-I | Autism classification | Outperforms SOTA methods |
| REST-MDD | Depression classification | Outperforms SOTA methods |
| Both | Biomarker identification | Identifies disorder-relevant functional biomarkers |

## Comparison with Existing Methods

| Aspect | Standard GNN | Euclidean Methods | HLBG (This Paper) |
|--------|-------------|-------------------|-------------------|
| Hierarchy modeling | Limited | Distorted | Natural in hyperbolic space |
| ROI-community interaction | Not modeled | Not modeled | Geometric entailment constraints |
| Long-range dependencies | Local only | Limited | GaMamba captures globally |
| Interpretability | Low | Low | High (geometric structure) |

## Applications

- **Brain disorder diagnosis**: Autism (ABIDE), Depression (REST-MDD)
- **Biomarker identification**: Disorder-relevant functional biomarkers
- **Brain network analysis**: Hierarchical structure modeling
- **Neurological classification**: Multi-level brain graph classification

## Connection to Other Skills

- Related to `hyperbolic-gcn-brain-network` and `hyperbolic-learning-brain-graphs` existing skills
- Complements `gnn-transformer-fusion` for brain network analysis
- Related to `sa-hgnn-sample-adaptive-hyperbolic-eeg-depression` for hyperbolic brain analysis
- Builds on `brain-graph-neural` for functional connectivity analysis

## Activation Keywords

hyperbolic brain graph, lorentzian hyperbolic space, geometric entailment constraints, graph-aware mamba, brain network hierarchy, roi-community modeling, brain disorder diagnosis, abide classification, rest-mdd, hierarchical brain representation, hyperbolic embedding
