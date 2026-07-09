---
name: where-to-intervene-benchmarking-fairness-aware-learning-on-differentially
description: 'Machine learning models are increasingly deployed in high-stakes domains, raising concerns about both privacy and fairness. Differential Privacy (DP) has become a gold standard for privacy-preserving. Based on arXiv:2607.07471.'
---

# Where to Intervene? Benchmarking Fairness-Aware Learning on Differentially Private Synthetic Tabular Data

**arXiv**: 2607.07471 | **Authors**: Vinícius Gabriel Angelozzi, Héber H. Arcolezi | **Utility**: 0.85

## Overview

Machine learning models are increasingly deployed in high-stakes domains, raising concerns about both privacy and fairness. Differential Privacy (DP) has become a gold standard for privacy-preserving data analysis, while fairness-aware mechanisms aim to mitigate discrimination against underrepresented groups. However, these objectives can conflict: DP often amplifies disparities across demographic groups, and little is known about whether established fairness interventions remain effective under DP constraints. In this work, we present, to our knowledge, the first systematic evaluation of fairness interventions on differentially private synthetic tabular data. Our benchmark centers on the Adaptive Iterative Mechanism (AIM), identified as the state-of-the-art marginal-based DP synthesizer (Cormode et al. 2025). We thus evaluate fairness interventions across four datasets, multiple group fairness metrics, and three categories of mitigation strategies (pre-processing, in-processing, and post-processing) under a wide range of privacy budgets. We compare four pipeline configurations: (Baseline) training on original data; (DP-only) training on DP synthetic data; (Fair-only) applying fairness mechanisms on original data; and (DP+Fair) combining fairness mechanisms with DP synthetic data. Our results demonstrate that while DP alone can degrade both utility and fairness, applying fairness interventions can partially restore equitable outcomes. Among them, post-processing methods tend to provide more stable fairness-utility trade-offs across privacy budgets and synthesizers, achieving strong fairness improvements while preserving competitive utility relative to other intervention stages. We release all code, data, and experimental artifacts in an open-source repository to ensure full reproducibility and to support future research on the privacy-fairness-utility trade-off.

## Key Contributions

1. Machine learning models are increasingly deployed in high-stakes domains, raising concerns about both privacy and fairness.
2. Differential Privacy (DP) has become a gold standard for privacy-preserving data analysis, while fairness-aware mechanisms aim to mitigate discrimination against underrepresented groups.
3. However, these objectives can conflict: DP often amplifies disparities across demographic groups, and little is known about whether established fairness interventions remain effective under DP constraints.
4. In this work, we present, to our knowledge, the first systematic evaluation of fairness interventions on differentially private synthetic tabular data.

## Implementation Notes

- **Keywords**: benchmark, privacy, fairness, graph-neural-network
- **Categories**: cs.LG, cs.AI, cs.CR
- **Published**: 2026-07-08

## Activation Criteria

Use this skill when working on tasks involving: benchmark, privacy, fairness, graph-neural-network.
