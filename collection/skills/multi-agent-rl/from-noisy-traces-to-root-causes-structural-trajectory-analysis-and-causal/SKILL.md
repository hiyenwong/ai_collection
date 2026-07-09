---
name: from-noisy-traces-to-root-causes-structural-trajectory-analysis-and-causal
description: 'The optimization of long-horizon agents increasingly relies on reflection-based mechanisms, where a large language model (LLM) acts as an optimizer to diagnose agent failures and improve agent policie. Based on arXiv:2607.07702.'
---

# From Noisy Traces to Root Causes: Structural Trajectory Analysis and Causal Extraction for Agent Optimization

**arXiv**: 2607.07702 | **Authors**: Ying Chang, Jiahang Xu, Xuan Feng, Chenyuan Yang, Peng Cheng et al. | **Utility**: 0.87

## Overview

The optimization of long-horizon agents increasingly relies on reflection-based mechanisms, where a large language model (LLM) acts as an optimizer to diagnose agent failures and improve agent policies. However, real execution traces are difficult to use directly for optimization: large trace collections are often redundant and heterogeneous, making optimization inefficient and prone to overfitting to low-value failures; meanwhile, each individual trajectory also contains many irrelevant steps, while naive context reduction methods such as truncation or sliding windows can discard causally important evidence and produce misleading optimization signals. To resolve this dilemma, we introduce STRACE (Structural TRajectory Analysis and Causal Extraction), a framework that constructs high signal-noise optimization contexts for more precise and effective optimization. At the batch level, STRACE mines failure patterns to filter redundant traces and retain representative failures; within each selected trace, it performs causal localization over a textual dependency graph to remove non-causal steps and identify the true root-cause module for optimization. Empirical results demonstrate that STRACE significantly outperforms standard context-filtering baselines. Notably, on a challenging formal verification task (VeruSAGE-Bench), it successfully optimizes human-expert designed agents, delivering $1.4\times$ success-rate improvement (42.5% to 58.5%). The code is available at https://github.com/moomight/STRACE .

## Key Contributions

1. The optimization of long-horizon agents increasingly relies on reflection-based mechanisms, where a large language model (LLM) acts as an optimizer to diagnose agent failures and improve agent policies.
2. However, real execution traces are difficult to use directly for optimization: large trace collections are often redundant and heterogeneous, making optimization inefficient and prone to overfitting to low-value failures; meanwhile, each individual trajectory also contains many irrelevant steps, while naive context reduction methods such as truncation or sliding windows can discard causally important evidence and produce misleading optimization signals.
3. To resolve this dilemma, we introduce STRACE (Structural TRajectory Analysis and Causal Extraction), a framework that constructs high signal-noise optimization contexts for more precise and effective optimization.
4. At the batch level, STRACE mines failure patterns to filter redundant traces and retain representative failures; within each selected trace, it performs causal localization over a textual dependency graph to remove non-causal steps and identify the true root-cause module for optimization.

## Implementation Notes

- **Keywords**: llm
- **Categories**: cs.CL
- **Published**: 2026-07-08

## Activation Criteria

Use this skill when working on tasks involving: llm.
