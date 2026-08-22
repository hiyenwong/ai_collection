---
name: graph-analysis-neuronal-culture-reservoir-computing
description: "Graph analysis of neuronal cultures using Reservoir Computing-derived connectivity maps. Extracts Intrinsic Connectivity Maps (ICM) from neural activity and applies graph centrality measures to quantify network dynamics."
metadata:
  arxiv_id: "2608.09773"
  authors: "Auslender, Ilya; Letti, Giorgio; Heydari, Yasaman; Pavesi, Lorenzo"
  published: "2026-08-10"
  tags: [neuronal culture connectivity, reservoir computing connectivity, ICM graph analysis, MEA graph theory, neuronal network centrality, in vitro connectivity inference, graph analysis reservoir computing]
license: Complete terms in LICENSE.txt
---

# Graph Analysis of Neuronal-Culture Connectivity Derived from a Reservoir-Computing Model

## Overview
This skill provides a framework for analyzing neuronal culture connectivity using Reservoir Computing (RC) to extract Intrinsic Connectivity Maps (ICM) from multichannel electrophysiological recordings, followed by graph-theoretical analysis to quantify network dynamics.

## Key Methodology
1. **Reservoir Computing Framework**: Reconstructs network connectivity from MEA recordings by training to extract Intrinsic Connectivity Matrix (ICM)
2. **Graph-Theoretical Analysis**: Interprets ICM as effective adjacency matrix for comprehensive graph analysis including node centrality measures and global network metrics
3. **Validation**: Benchmarks RC-derived connectivity against known ground-truth adjacency matrix through simulation

## Performance Metrics
- ROC AUC up to 0.922
- F1 scores up to 0.796  
- NMWA Pearson correlation up to 0.692

## Applications
- Functional network characterization in neuronal culture systems
- Understanding emergent dynamics in in vitro cortical cultures
- Bridging computational neuroscience with experimental electrophysiology
- Potential applications in neurotoxicity screening and drug discovery

## Activation Keywords
- neuronal culture connectivity
- reservoir computing connectivity
- ICM graph analysis
- MEA graph theory
- neuronal network centrality
- in vitro connectivity inference
- graph analysis reservoir computing

## References
- Original paper: https://arxiv.org/abs/2608.09773
- Related work: Auslender et al., 2025 (RC framework foundation)