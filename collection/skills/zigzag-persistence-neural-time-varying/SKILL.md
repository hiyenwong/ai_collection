---
name: zigzag-persistence-neural-time-varying
version: 1.0
date: 2026-04-22
paper: "2603.03037"
title: "Zigzag Persistence of Neural Responses to Time-Varying Stimuli"
description: "Topological data analysis of neural population activity using zigzag persistent homology on cubical complexes. Captures evolving topological structure in neural responses to video stimuli via persistence landscapes."
category: topological-data-analysis
tags: [zigzag-persistence, topological-data-analysis, neural-coding, visual-cortex, cubical-complex, persistence-landscape]
---

# Zigzag Persistence of Neural Responses to Time-Varying Stimuli

## Summary
Applies topological data analysis (TDA) to study neural population activity in the Sensorium 2023 dataset. Uses zigzag persistent homology on frame-by-frame cubical complexes to capture evolving topological structure of neural responses to video stimuli.

## Core Methodology

### Problem
- Understanding neural population coding of time-varying stimuli
- Need compact representations of temporal neural dynamics
- Standard persistence homology requires static point clouds — not suitable for time-varying data

### Approach
1. **Data**: Sensorium 2023 dataset — thousands of mouse visual cortex neurons responding to diverse video stimuli
2. **Cubical Complexes**: Build frame-by-frame cubical complexes from neuronal activity
3. **Zigzag Persistent Homology**: Capture how topological structure evolves over time
4. **Persistence Landscapes**: Summarize dynamics as compact vectorized representations of temporal features
5. **1D Features (Loops)**: Focus on loops reflecting coordinated, cyclical patterns of neural co-activation

### Analysis Pipeline
1. For each video stimulus, construct cubical filtration from neural activity
2. Apply zigzag persistent homology across temporal frames
3. Convert to persistence landscapes for vectorization
4. Cluster topological representations to distinguish stimuli
5. Validate that topological descriptors reliably distinguish neural responses to distinct stimuli

### Key Results
- Topological descriptors reliably distinguish neural responses to different video stimuli
- 1D topological features (loops) capture coordinated cyclical neural co-activation patterns
- Persistence landscapes provide interpretable temporal signatures

## Applications
- Neural coding analysis of time-varying stimuli
- Stimulus discrimination from population activity
- Topological feature extraction for neural data
- Visual cortex coding analysis

## Activation Triggers
zigzag persistence, topological data analysis, TDA, neural coding, cubical complex, persistence landscape, visual cortex, time-varying stimuli, Sensorium
