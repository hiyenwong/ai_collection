---
name: gnn-drug-toxicity-explainability
description: "GNN-based drug toxicity prediction explainability methodology with Gap Taxonomy (GAP-1 to GAP-4) for systematic analysis of explainability limitations. Uses GNNExplainer on MPNN models trained on Tox21 benchmark."
---

# GNN Drug Toxicity Explainability with Gap Taxonomy

Systematic methodology for analyzing explainability gaps in Graph Neural Network (GNN)-based drug toxicity prediction. Introduces a four-category Gap Taxonomy distinguishing between different types of unexplainable effects.

## Overview

GNNs are structurally natural for molecular toxicity prediction (operating on atomic connectivity), but molecular structure alone cannot encode all pharmacological effects. This methodology systematically identifies and categorizes what molecular structure **cannot** tell us about drug safety.

## Core Framework: Gap Taxonomy

### GAP-1: Principally Non-Encodable Effects
- Effects that fundamentally cannot be derived from molecular structure alone
- Require biological context (metabolism, protein interactions, systemic effects)
- Example: Aspirin's gastrointestinal effects depend on prostaglandin inhibition in vivo, not just molecular structure

### GAP-2: MNAR (Missing Not At Random) Data Gaps
- Bioactivity data that is systematically absent from databases
- Empirically quantified via systematic database queries
- Pattern: 42 documented assays in ChEMBL → 0 retrievable bioactivity entries
- Indicates systematic under-study of certain compound classes

### GAP-3: Assay Panel Mismatches
- Discrepancies between training data assays and real-world pharmacological profiles
- Benchmark datasets (Tox21) may not cover clinically relevant toxicity endpoints
- Regulatory frameworks (GVP guidelines) require endpoints beyond standard panels

### GAP-4: Representation Errors
- Errors localized to specific model components (e.g., MPNN message passing vs. aggregation)
- Attention pooling experiments can isolate the error source
- Message passing layers often lose subtle structural information

## Methodology Steps

### 1. Model Training
```python
# Train MPNN on Tox21 or similar toxicity benchmark
from torch_geometric.nn import MessagePassing

model = MPNN(hidden_channels=64, num_layers=3)
# Train on multi-task toxicity prediction
```

### 2. GNNExplainer Attribution
```python
# Apply GNNExplainer to identify atom-level attributions
explainer = GNNExplainer(model, epochs=100)
node_mask, edge_mask = explainer.explain_graph(x, edge_index)
# Quantify which atoms/substructures the model considers important
```

### 3. Gap Analysis Pipeline
1. **Collect known pharmacological profile** (literature, FDA labels, ChEMBL)
2. **Compare GNN predictions** against known profile
3. **Categorize missing predictions** into GAP-1 through GAP-4
4. **Quantify coverage**: molecular_structure_explains = known_effects_predicted / total_known_effects
5. **Empirical MNAR test**: query databases for bioactivity data → document systematic gaps

### 4. Attention Pooling Localization
```python
# Use attention pooling to isolate representation errors
# Compare model variants with/without attention pooling
# If accuracy difference → error is in aggregation
# If no difference → error is in message passing layers
```

## Key Findings (from ASA/Aspirin case study)
- Molecular structure explains ~45% (5/11) of known adverse effects
- Remaining 55% fall into Gap Taxonomy categories
- MNAR gap is significant: documented assays exist but no bioactivity data retrievable
- Representation errors trace to message passing layers, not aggregation

## Applications
- **Drug safety signal detection**: systematic identification of unmodeled risks
- **Regulatory compliance**: alignment with GVP guidelines and NAMs
- **Model improvement**: targeted fixes for specific gap categories
- **Research prioritization**: identify which compound classes need more study

## Pitfalls
- **Tox21 benchmark limitations**: only covers 11 toxicity endpoints, misses clinical reality
- **GNNExplainer approximation**: attribution maps are approximate, not ground truth
- **MNAR quantification requires systematic querying**: single queries may miss systematic patterns
- **Case study selection bias**: well-characterized drugs (like Aspirin) may not represent typical compounds
