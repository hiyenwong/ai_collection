---
name: hlbg-hyperbolic-learning-brain-graphs
description: Hyperbolic Learning on Brain Graphs (HLBG) — exploits hierarchical geometry of hyperbolic space to model ROI-community-whole-brain relationships for brain network analysis and disorder diagnosis.
trigger_words:
  - hyperbolic learning brain graphs
  - HLBG
  - brain network hierarchy
  - Lorentzian hyperbolic space
  - graph-aware Mamba
  - GaMamba
  - ROI community whole-brain hierarchy
  - hyperbolic brain network
  - geometric entailment constraints
  - brain graph disorder diagnosis
categories:
  - neuroscience
  - computational neuroscience
  - brain networks
  - hyperbolic learning
created: "2026-07-12"
source: "arXiv:2607.07077v1"
---

# Hyperbolic Learning on Brain Graphs (HLBG)

## Paper

**Title:** Navigating Hierarchy: Hyperbolic Learning on Brain Graphs for Disorder Diagnosis  
**Authors:** Yapeng Li, Bo Jiang, Ziyan Zhang, Dongdong Chen, Zhengzheng Tu  
**Published:** arXiv:2607.07077v1  
**Date:** July 8, 2026  

## Problem

Functional brain networks exhibit hierarchical organization across ROI, community, and whole-brain levels, supporting local processing, inter-community coordination, and global integration. However:

- Existing brain graph modeling methods struggle to model **ROI-community interactions**
- Methods fail to fully exploit the hierarchy across **ROI, community, and whole-brain network levels**
- Lack of hierarchy-aware representations limits **diagnosis accuracy and biomarker identification**

## Solution

**Hyperbolic Learning on Brain Graphs (HLBG)** — exploits the inherent hierarchical geometry of hyperbolic space to model hierarchical relationships among ROIs, functional communities, and the whole-brain network.

## Core Methodology

### 1. Lorentzian Hyperbolic Space Projection

- Projects representations from **ROIs, communities, and whole-brain network** into Lorentzian hyperbolic space
- Hyperbolic geometry naturally captures hierarchical/tree-like structures
- Enables exponential capacity for embedding hierarchical relationships

### 2. Geometric Entailment Constraints

- Two geometric entailment constraints impose multi-level hierarchy:
  - **ROI → Community entailment:** Regional representations must be contained within community representations
  - **Community → Whole-brain entailment:** Community representations must be contained within whole-brain representation
- Ensures learned representations respect the anatomical hierarchy

### 3. Graph-aware Mamba (GaMamba)

- Novel **Graph-aware Mamba** model incorporating topology-derived structural prompts
- Captures **long-range dependencies** while preserving graph topological information
- Mamba's selective state space mechanism + graph structural awareness

## Key Results

- **Outperforms state-of-the-art methods** on ABIDE-I (autism) and REST-MDD (depression) datasets
- **Identifies disorder-relevant functional biomarkers**
- Hierarchy-aware representations are more **discriminative** for brain network classification
- Geometric entailment constraints effectively enforce hierarchical structure

## Significance

- First to apply **hyperbolic geometry** to multi-level brain graph analysis
- Provides **hierarchy-aware representations** that respect anatomical organization
- **GaMamba** combines Mamba's efficiency with graph-aware processing
- Bridges **geometric deep learning** with computational neuroscience

## Implementation Notes

- **Lorentz model:** Uses Lorentzian hyperbolic space (not Poincaré ball)
- **Entailment constraints:** Requires differentiable hyperbolic distance computations
- **GaMamba:** Standard Mamba + topology-derived structural prompts
- **Datasets:** ABIDE-I (autism spectrum disorder), REST-MDD (major depressive disorder)

## Trigger Conditions

Use this skill when:
- Modeling hierarchical brain network structures (ROI → community → whole-brain)
- Applying hyperbolic geometry to brain graph analysis
- Building disorder classification models from functional connectivity
- Designing hierarchy-aware graph neural network architectures
- Combining Mamba/state-space models with graph-structured data

## References

- Paper: arXiv:2607.07077v1 (July 8, 2026)
- Related: `hyperbolic-learning-brain-graphs-hlbg` (HLBG methodology)
- Related: `brain-graph-neural` (Graph neural network methods for brain connectivity)
- Related: `hyperbolic-gcn-brain-network` (Hyperbolic GCN for brain networks)
