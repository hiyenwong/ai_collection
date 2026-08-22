---
name: arxiv-2608-20009-exphy-a-benchmark-for-explicit-physical-property-l
description: 'ExPhy: A Benchmark for Explicit Physical Property Learning in Multi-Object Trajectory Forecasting (arXiv: 2608.20009)'
category: physics-math
version: "1.0"
date: 2026-08-22
---

# ExPhy: A Benchmark for Explicit Physical Property Learning in Multi-Object Trajectory Forecasting

**Authors:** Rui Wang, Yeteng Wu, Xianlin Zhang, Mengshi Qi
**arXiv:** 2608.20009
**Utility:** 1.00
**Published:** 2026-08-20T13:24:13Z
**Link:** http://arxiv.org/abs/2608.20009

## Abstract

Understanding object dynamics requires not only predicting future trajectories but also examining whether a model captures the physical properties that govern motion. However, existing benchmarks rarely expose object-level physical properties as explicit evaluation targets alongside trajectory forecasting. To address this gap, we introduce \emph{ExPhy}, a multi-object trajectory forecasting benchmark containing 24,000 simulated physical scenes with explicit object-level labels for mass, friction, and restitution. ExPhy provides observed and future trajectories together with an in-distribution (ID) split and two out-of-distribution (OOD) splits over physical parameters (OOD-Parameter) and initial states (OOD-Initial) for jointly evaluating trajectory forecasting and physical property estimation. We further instantiate \textsc{PhyODE}, a physics-guided model with an explicit property interface that estimates physical properties from observed trajectories and uses them for differentiable future rollout. On the long-horizon OOD-Initial setting, \textsc{PhyODE} reduces ADE and FDE by 33.1\% and 31.0\%, respectively, compared with the strongest baseline. Zero-shot evaluation on ComPhy further assesses cross-benchmark transfer. Property-level analyses reveal that accurate trajectory forecasting does not necessarily imply accurate recovery of the underlying physical properties. Code and data are available at https://github.com/Zest86/ExPhy.

## Summary

This skill encapsulates the key contributions and methods from the arXiv paper "ExPhy: A Benchmark for Explicit Physical Property Learning in Multi-Object Trajectory Forecasting". 
The paper presents novel ideas in physics-math that can be applied to agent systems.

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

- arXiv:2608.20009
