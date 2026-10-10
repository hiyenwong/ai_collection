---
name: small-world-connectivity-llms
description: Use when analyzing LLM internal representations as networks. Small-world connectivity correlates with reasoning performance.
tags: [network-analysis, small-world, reasoning, interpretability, neuroscience-inspired, representational-geometry]
---

# Small-World Connectivity in LLMs

## Paper Metadata

- **arXiv ID**: 2610.12304
- **Authors**: arXiv authors
- **Categories**: cs.CL, cs.LG
- **Utility Score**: 0.86
- **Date**: 2026-10
- **Link**: https://arxiv.org/abs/2610.12304

## Key Contributions

- Identifies small-world connectivity as structural signature of LLM reasoning performance
- Draws on neuroscience findings linking intelligence to brain network organization
- Provides network-theoretic metrics for characterizing internal representations
- Suggests that reasoning capability correlates with specific topological properties

## Core Methodology

The work analyzes the internal representations of LLMs by constructing networks from activation patterns or attention structures, then measuring their topological properties. The key finding is that models with stronger reasoning capabilities exhibit small-world connectivity — high clustering (local structure) combined with short path lengths (global integration).

This finding is inspired by neuroscience research showing that human intelligence correlates with small-world organization in brain networks. The parallel suggests that similar organizational principles may underlie intelligent computation in both biological and artificial systems, regardless of substrate.

The analysis provides a new lens for understanding LLM capabilities: rather than just measuring input-output behavior, the internal network topology reveals structural properties that correlate with reasoning ability. This opens the door to architecture search and training objectives that explicitly optimize for small-world properties.

## Relevance to nlp-llm

Bridges neuroscience and LLM interpretability: suggests that network topology metrics can serve as proxies for reasoning capability, potentially guiding architecture design and training.

## Activation

network-analysis, small-world, reasoning, interpretability, neuroscience-inspired, representational-geometry
