---
name: identifiability-guarantees-delayed-physical-systems
description: Theory-grounded method proving identifiability of structural drivers and drift in stochastic delayed physical systems under permissive assumptions
version: 1.0.0
tags: [stat.ML, cs.LG, math.DS, identifiability, physical-systems, symbolic-regression, causal-discovery]
source: arxiv
arxiv_id: 2609.37944v1
utility: 0.9
---

# Identifiability Guarantees for Drivers and Dynamics of Delayed Physical Systems

**Authors:** Julien Boussard, Antoine Débouchage, Théo Saulus
**Published:** 2026-09-29
**Categories:** stat.ML, cs.LG, math.DS
**arXiv:** https://arxiv.org/abs/2609.37944v1

## Summary

A wide range of methods have been proposed, including physics-informed neural networks, which are powerful but do not guarantee identifiability of the dynamics, symbolic regression, which requires a set of precomputed operations, and causal discovery, which is more principled but usually relies on strong assumptions that physical systems may violate. In this work, we develop a theory-grounded method and prove that under a set of permissive assumptions, the structural drivers and drift of stochastic delayed physical systems can be identified. This provides theoretical guarantees that existing methods lack while maintaining practical applicability to real-world physical systems with delays.

## Key Contributions

- Develops a theory-grounded method for identifying structural drivers and dynamics in delayed physical systems
- Provides formal identifiability guarantees under permissive assumptions
- Addresses limitations of physics-informed neural networks (no identifiability guarantee), symbolic regression (requires precomputed operations), and causal discovery (strong assumptions)
- Bridges the gap between theoretical guarantees and practical applicability for physical systems with delays

## Relevance

This paper is valuable for researchers working on system identification, physics-informed machine learning, and causal discovery in dynamical systems. The identifiability guarantees address a fundamental limitation of existing methods, making it particularly useful for applications where understanding the true underlying dynamics is critical, such as in scientific discovery, control systems, and predictive modeling of physical processes with delays.
