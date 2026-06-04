---
name: curverl-distribution-aware-rlvr
description: CurveRL methodology — principled distribution-aware context reweighting for RLVR, using quantile coordinate transform where prompt weights depend on pass-rate rank and density rather than absolute values.
---

# CurveRL: Distribution-Aware Context Reweighting for LLM Reasoning

**Paper**: CurveRL: Principled Distribution-Aware Context Reweighting for LLM Reasoning
**arXiv**: 2605.24331
**Authors**: Ke Sun, Yizhou Zhao, Jiayi Xin, Qi Long, Weijie Su
**Submitted**: 23 May 2026

## Core Idea

Context/prompt-level reweighting is central to RLVR for LLM reasoning, but the principle for optimal weighting is poorly understood. CurveRL formulates prompt reweighting as a **functional derivative in pass-rate function space**, yielding a unified framework accommodating REINFORCE and GRPO. It uses a **quantile coordinate transform**: weight depends on pass-rate rank and density, not absolute values.

## Key Contributions

1. **Unified optimality framework**: Prompt reweighting as functional derivative in pass-rate function space
2. **CurveRL algorithm**: Distribution-aware reweighting via quantile coordinate transform
3. **Outperforms GRPO** consistently across multiple benchmarks
4. **Context-distribution control** as a principled axis for RLVR analysis

## Method Details

### Unified Framework
Given pass rates p_i for prompt i, optimal weight w_i = F'(p_i) in pass-rate function space. Different F recovers REINFORCE (linear) and GRPO (group-based).

### CurveRL Algorithm
1. Map pass rates to quantile values based on rank in current batch
2. Density-aware weighting: weight depends on local density around each prompt
3. Online adaptation as pass-rate distribution evolves

### Key Formula
w_i = φ(rank(p_i) / N) · ψ(density(p_i))

## Implementation
- Maintain running pass-rate distribution estimate
- Quantile buckets adaptive based on batch statistics
- Drop-in replacement for GRPO weighting scheme
- No architecture changes needed

## Activation Keywords
- CurveRL, distribution-aware reweighting, RLVR, prompt reweighting, context reweighting, quantile coordinate transform, LLM reasoning RL, pass-rate reweighting, context-distribution control
