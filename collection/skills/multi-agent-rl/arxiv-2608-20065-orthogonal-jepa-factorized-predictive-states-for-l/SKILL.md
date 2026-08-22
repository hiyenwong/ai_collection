---
name: arxiv-2608-20065-orthogonal-jepa-factorized-predictive-states-for-l
description: 'Orthogonal JEPA: Factorized Predictive States for Latent World Models (arXiv: 2608.20065)'
category: multi-agent-rl
version: "1.0"
date: 2026-08-22
---

# Orthogonal JEPA: Factorized Predictive States for Latent World Models

**Authors:** Taoyong Cui, Pheng Ann Heng, Wanli Ouyang
**arXiv:** 2608.20065
**Utility:** 1.00
**Published:** 2026-08-20T13:59:57Z
**Link:** http://arxiv.org/abs/2608.20065

## Abstract

World models construct latent states that support prediction, planning, and reasoning about an underlying system. Joint-embedding predictive architectures (JEPAs) offer a direct way to learn such states by predicting targets in representation space instead of reconstructing every detail of the observation. Standard JEPAs, however, organize all predictable content through one target embedding and one prediction pathway. In complex systems, this monolithic state can allocate redundant capacity to dominant signals while providing weak or conflicting gradients to less dominant predictive structure. We introduce \method, a latent world-modeling framework based on orthogonal predictive factorization. Learned basis matrices analyze each target state into multiple components, and a dedicated prediction branch estimates each component from a shared context representation. Predictive regression preserves the factor magnitudes required for state synthesis, an orthogonality objective discourages repeated directions, factor-activity regularization maintains variation in projected targets, and online variance regularization discourages coordinate-wise encoder collapse. Predicted components are synthesized into a complete latent state that can be used by a readout, decoder, planner, or autoregressive rollout. The same predictive-state mechanism applies when the target is temporally future, spatially hidden, or another partial observation of the same system. Experiments on controlled vision, single-cell transcriptomics, longitudinal health records, continuous control, and molecular dynamics evaluate representation quality, forecasting, planning, and long-horizon stability.

## Summary

This skill encapsulates the key contributions and methods from the arXiv paper "Orthogonal JEPA: Factorized Predictive States for Latent World Models". 
The paper presents novel ideas in multi-agent-rl that can be applied to agent systems.

## How to Use

1. Review the paper's methodology and findings.
2. Identify applicable components for your agent workflow.
3. Implement the core techniques as described in the paper.
4. Validate improvements in your specific use case.

## Pitfalls

- Ensure the paper's assumptions match your agent's environment.
- Validate implementation details before deployment.
- Consider computational complexity and resource requirements.

## References

- arXiv:2608.20065
