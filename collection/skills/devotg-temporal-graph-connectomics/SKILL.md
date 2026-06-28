---
name: devotg-temporal-graph-connectomics
description: "DevoTG: Temporal Graph Neural Networks for modeling C. elegans developmental connectomics, capturing dynamic wiring through continuous-time and discrete-time dynamic graphs."
activation: developmental connectomics, temporal graph neural networks, C. elegans, connectome development, wiring dynamics
tags: [neuroscience, graph-neural-networks, temporal-networks, developmental-biology]
arxiv_id: "2606.21940"
authors: ["Jayadratha Gayen", "Bradly Alicea"]
---

# DevoTG: Temporal Graph Neural Networks for Developmental Connectomics

## Problem
Understanding how a nervous system wires itself from birth to adulthood is fundamental in developmental neuroscience. Static graph models cannot capture the **temporal dynamics** of neural development.

## Core Methodology

### Dual Graph Representations
1. **Continuous-Time Dynamic Graph (CTDG)**: Models cell division events from cell lineage data
   - Each division is a temporal event
   - Captures neurogenesis timing and cell fate decisions
   
2. **Discrete-Time Dynamic Graph (DTDG)**: Models developing synaptic connectome
   - Spanning 8 reconstructed electron-microscopy datasets
   - Tracks 225 neurons and 858 to 2,496 connections over development

### Temporal Graph Neural Network (TGN)
- **Temporal memory**: Maintains hidden state that evolves with graph events
- **Node embeddings**: Updated based on temporal neighborhood aggregation
- **Link prediction**: Predicts future connections based on historical dynamics

### Key Results
- **Lineage prediction**: Mean test AUC = 0.839 ± 0.007 (5 seeds)
- **Temporal advantage**: Outperforms static GNN by 26 AUC points (0.577 ± 0.080)
- **Connection stability classes**: Identifies three classes (stable, developmental, variable)

## Activation Triggers
- "developmental connectomics"
- "temporal graph neural networks"
- "C. elegans neural development"
- "wiring dynamics"
- "cell lineage prediction"
- "connectome over time"

## Methodological Innovation
- Demonstrates that **temporal memory is decisive** for developmental prediction
- Bridges cell lineage and synaptic connectome development
- Identifies connection stability classes across development

## Comparison with Static Methods
- Static GNN: 0.577 AUC (fails to capture temporal dynamics)
- Temporal GNN: 0.839 AUC (45% improvement)
- Temporal information is critical for developmental processes

## Related Work
- Static Graph Neural Networks (GCN, GAT)
- Temporal Graph Networks (TGN)
- Neural development models
- C. elegans connectomics

## Use Cases
- Developmental neuroscience
- Neurogenesis modeling
- Critical period identification
- Evolutionary developmental biology (evo-devo)

## Reference
Gayen, J., & Alicea, B. (2026). DevoTG: Temporal Graph Neural Networks for Modeling C. elegans Developmental Connectomics. arXiv:2606.21940