---
name: driada-cross-scale-neural-analysis
description: "DRIADA: Open-source Python toolkit for cross-scale analysis of single-neuron selectivity and population dynamics. Unifies neural signals and behavior in shared data model for selectivity testing, dimensionality reduction, and network analysis. Activation: DRIADA toolkit, cross-scale neural analysis, single-neuron selectivity, population dynamics, hippocampal calcium imaging, neural coding toolkit, information-theoretic selectivity."
tags: [neuroscience, computational-toolkit, neural-coding, calcium-imaging, population-dynamics, selectivity-analysis, python-framework, hippocampal-analysis]
version: 1.0.0
author: agent
arxiv_id: "2607.00851"
paper_title: "DRIADA: A Python Toolkit for Cross-Scale Analysis of Single-Neuron Selectivity and Population Dynamics"
authors: ["Nikita Pospelov", "Viktor Plusnin", "Olga Rogozhnikova", "Anna Ivanova", "Vladimir Sotskov"]
date: "2026-07-01"
subjects: ["q-bio.NC"]
---

# DRIADA: Cross-Scale Neural Analysis Toolkit

## Core Innovation

### Problem
Brain activity spans single-neuron, population, and network levels. Core questions in neural coding require moving between these scales. However, existing tools target single paradigms with incompatible data formats, making cross-level questions hard to address.

### Solution
**DRIADA** — an open-source Python framework that:
- Unifies neural signals and time-aligned behavior in a **shared data model**
- Enables selectivity testing, dimensionality reduction, and network analysis within a **unified workflow**
- Bridges individual neuron characterization with population structure and functional network analysis

## Methodology

### Unified Data Representation
- Neural signals (spike trains, calcium traces) mapped to a consistent format
- Time-aligned behavioral events integrated into same data structure
- Cross-session tracking via CellReg-matched neurons

### Information-Theoretic Selectivity Testing
- Quantifies how individual neurons encode behavioral features
- Conservative statistical thresholds for reliable within-session detection
- Tested on hippocampal CA1 neurons across 13 mice in open field

### Dimensionality Reduction
- Population-level structure analysis
- Reveals nonlinear manifold structure in neural population activity
- Validated on toroidal attractor network simulations with known ground truth

### Network Analysis
- Functional connectivity analysis from neural time series
- Graph-based analyses organized around single unified network representation
- Bridges selectivity findings with population-level functional networks

## Key Findings

### Hippocampal Selectivity Landscape
- **Single-feature dominance**: Of neurons selective to ≥1 feature, 90.1% selective to exactly one feature (contrasts with strong mixed selectivity in PFC)
- **Representational drift**: Only 1.1% run-selective and 0.3% place-selective neurons retained labels across all 3 sessions
- **Systematic organization**: Feature prevalence rank ordering consistent across all 13 mice (Kendall's W = 0.53)

### Scale-Bridging Insights
- Population analysis benefits from individual neuron characterization
- Nominally non-selective neurons contribute collectively to spatial manifold
- Cross-scale analysis reveals organizational properties invisible at single scale

### Attractor Network Validation
- Nonlinear manifold structure recovered from toroidal attractor simulation
- Individual neurons predominantly single-feature selective
- Collective population activity forms coherent spatial representation

## Software Architecture

### Pipeline Components
1. **Unified data model**: Neural signals + behavioral events
2. **Selectivity testing**: Information-theoretic feature encoding analysis
3. **Dimensionality reduction**: Population structure extraction
4. **Network analysis**: Functional connectivity + graph theory
5. **Time series analysis**: Network dynamics from temporal data

### Validation Strategy
- Synthetic data with known ground truth
- Hippocampal calcium imaging from 13 mice (open field behavior)
- Continuous attractor network simulation (toroidal manifold)

## Implications

### For Neural Coding Research
- First toolkit enabling seamless cross-scale analysis in single workflow
- Resolves tool fragmentation (incompatible formats, single-paradigm focus)
- Enables new questions requiring single-neuron ↔ population movement

### For Hippocampal Research
- Demonstrates predominantly single-feature selectivity in CA1
- Quantifies representational drift with CellReg cross-session matching
- Reveals systematic organizational property across animals

## Key Concepts

- **Cross-scale analysis**: Moving between single-neuron, population, and network levels
- **Information-theoretic selectivity**: Quantifying feature encoding in individual neurons
- **Representational drift**: Changes in neural tuning across sessions despite stable behavior
- **Continuous attractor networks**: Neural models with continuous family of stable states
- **CellReg**: Cross-session cell registration for tracking same neurons over days
- **Toroidal manifold**: 2D ring-like structure in neural population activity space

## Activation

DRIADA toolkit, cross-scale neural analysis, single-neuron selectivity, population dynamics, hippocampal calcium imaging, neural coding toolkit, information-theoretic selectivity, representational drift analysis, continuous attractor network, CA1 selectivity landscape, neural data integration

## References

- arXiv: 2607.00851v1 [q-bio.NC]
- Authors: Nikita Pospelov, Viktor Plusnin, Olga Rogozhnikova, Anna Ivanova, Vladimir Sotskov, et al.
- Institute for Advanced Brain Studies, Lomonosov Moscow State University
- License: CC BY-NC-SA 4.0
