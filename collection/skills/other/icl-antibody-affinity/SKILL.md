---
name: icl-antibody-affinity
description: In-context learning methodology for antigen-specific antibody affinity ranking in computational immunology
category: computational-biology
activation: antibody affinity, antigen binding, in-context learning, computational immunology, antibody ranking, AbICL
arxiv_id: "2607.05846"
---

# In-Context Learning for Antibody Affinity

## Overview
In-context learning (ICL) methodology for antigen-specific antibody affinity ranking — applying LLM-style contextual learning to computational immunology for predicting and ranking antibody-antigen binding affinities.

## Core Methodology
1. **Context Construction**: Build contextual examples from known antibody-antigen pairs with measured affinities
2. **ICL Prompt Design**: Format binding data as in-context examples for affinity prediction
3. **Ranking Inference**: Use model's contextual understanding to rank unseen antibody-antigen pairs
4. **Calibration**: Validate rankings against experimental binding data (Kd, IC50)

## Key Components
- **Sequence Context**: Antibody CDR sequences + antigen epitope sequences as context
- **Binding Data Encoding**: Numerical affinity values encoded in contextual examples
- **Zero/Few-Shot Transfer**: Predict affinities for novel antigens from contextual examples
- **Structure-Aware Encoding**: Optional 3D structural information as additional context

## Applications
- Antibody therapeutic development
- Vaccine design optimization
- Computational antibody engineering
- Rapid affinity maturation screening

## Implementation Notes
- Requires curated antibody-antigen affinity datasets
- Benefits from diverse antigen coverage in context examples
- Can complement traditional molecular docking methods
- Enables rapid in-silico screening of antibody candidates
