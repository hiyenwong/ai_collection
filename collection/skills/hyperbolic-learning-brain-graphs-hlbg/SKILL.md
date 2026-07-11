---
name: hyperbolic-learning-brain-graphs-hlbg
description: >
  Hyperbolic Learning on Brain Graphs (HLBG) methodology for brain
  disorder diagnosis using Lorentzian hyperbolic space and Graph-aware
  Mamba (GaMamba). Models hierarchical relationships among ROIs,
  functional communities, and whole-brain networks via geometric
  entailment constraints. Activation: hyperbolic brain graphs, brain
  network diagnosis, GaMamba, hyperbolic space brain, Lorentz model
  brain, hierarchical brain representation.
---

# Hyperbolic Learning on Brain Graphs (HLBG)

From: **"Navigating Hierarchy: Hyperbolic Learning on Brain Graphs for Disorder Diagnosis"** (arXiv:2607.07077, July 2026) — Yapeng Li, Bo Jiang, Ziyan Zhang, Dongdong Chen, Zhengzheng Tu.

## Core Concept

Functional brain networks exhibit **hierarchical organization** across ROI, community, and whole-brain levels. HLBG exploits the **inherent hierarchical geometry of hyperbolic space** (Lorentz model) to model these relationships, learning hierarchy-aware and highly discriminative representations for brain network analysis.

### Problem
Existing brain graph modeling methods struggle to model **ROI–community interactions**, failing to fully exploit the hierarchy across ROI, community, and whole-brain network levels.

### Solution
Project representations from ROIs, communities, and whole-brain network into Lorentzian hyperbolic space, then impose multi-level hierarchy via geometric entailment constraints.

## Architecture

### 1. Hierarchical Brain Graph Construction
- Build graphs at three levels:
  - **ROI level**: individual brain regions as nodes
  - **Community level**: functional communities as nodes
  - **Whole-brain level**: global network
- Each level captures different scales of brain organization

### 2. Graph-aware Mamba (GaMamba)
- **Novel contribution**: incorporates topology-derived structural prompts into Mamba architecture
- Captures **long-range dependencies** while preserving **graph topological information**
- Mamba's state-space model adapted for graph-structured data

### 3. Hyperbolic Projection
- Project representations from all three levels into **Lorentzian hyperbolic space**
- Hyperbolic space naturally encodes hierarchical structure with minimal distortion
- Uses the Lorentz model (not Poincaré ball) for numerical stability

### 4. Geometric Entailment Constraints
- Two geometric entailment constraints impose the multi-level hierarchy:
  - **ROI → Community entailment**: ROI representations are geometrically "contained" within their community representations
  - **Community → Whole-brain entailment**: community representations are contained within whole-brain representation
- These constraints force the model to learn the hierarchical organization

### 5. Fusion and Learning Loss
- Fuse multi-level representations for final classification
- Task-specific loss for disorder diagnosis

## Experiments

- **ABIDE-I**: autism spectrum disorder (ASD) dataset
- **REST-MDD**: major depressive disorder (MDD) dataset
- HLBG outperforms state-of-the-art methods on both datasets
- Identifies disorder-relevant functional biomarkers

## Key Innovations

1. **Hierarchical hyperbolic modeling**: first to exploit hyperbolic geometry for multi-level brain graph learning
2. **GaMamba**: novel graph-aware Mamba module with structural prompts
3. **Geometric entailment**: formal constraints encoding brain hierarchy
4. **Biomarker detection**: interpretable identification of disorder-relevant regions

## Relationship to Existing Skills

- Extends `hyperbolic-gcn-brain-network` (which uses Lorentz model for single-level brain networks)
- Adds: multi-level hierarchy, GaMamba module, geometric entailment constraints
- Complementary: HLBG is for diagnosis/classification; `hyperbolic-gcn-brain-network` is for general brain network analysis

## When to Use

- Brain disorder diagnosis (ASD, MDD, etc.)
- Brain network classification with hierarchical structure
- Biomarker identification from fMRI functional connectivity
- Hyperbolic graph representation learning
- When ROI-community-whole-brain hierarchy matters for the task

## Pitfalls

- **Lorentz model numerics**: hyperbolic space operations require careful numerical handling (clipping, stability)
- **Entailment constraint tuning**: geometric entailment parameters need careful calibration
- **Multi-level graph construction**: community detection quality affects downstream performance
- **GaMamba complexity**: state-space model for graphs is more complex than standard GNN layers
- **Dataset requirements**: benefits most from datasets with clear hierarchical brain organization
