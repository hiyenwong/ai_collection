---
name: sparse-linear-expert-transformer
description: "Sparsely gated tiny linear experts (sgatlin) methodology — replacing transformer feedforward layers with networks of sparsely-gated linear neurons for improved compute efficiency and interpretability. Covers isoflop comparison, linear expert removal of nonlinearity, semantic cluster interpretation, and causal factual recall. Activation: sparse linear expert, sgatlin, tiny linear expert, sparsely gated linear, linear MoE, sparse transformer FFN."
---

## Context

Mixture-of-Experts (MoE) models achieve scalability through sparsity — routing to a subset of experts per token. However, individual experts typically remain large and dense. This paper demonstrates that further increasing sparsity by shrinking each expert to a **single linear neuron** and selecting a tiny fraction of many available neurons improves both compute efficiency and interpretability.

Source paper: arXiv:2606.07414 "Sparsely gated tiny linear experts" (Simon Schug — Jun 2026).

## Core Methodology

### 1. Sparsely Gated Linear Neurons (sgatlin)

**Key Insight**: Removing the nonlinearity typically applied to MoE experts, while dramatically increasing the number of experts (each being a single neuron), yields better performance at the same compute budget.

- Replace all transformer feedforward (FFN) layers with sgatlin layers
- Each "expert" is a single linear neuron (no activation function)
- Sparse gating selects a tiny fraction of available neurons per token
- Total parameters scale with number of neurons, not with expert size

### 2. Isoflop Comparison Protocol

- Match compute budget (FLOPs) between baseline FFN and sgatlin
- Compare perplexity across language models at different compute budgets
- Key finding: sgatlin improves perplexity across all tested compute budgets
- The improvement comes from better parameter utilization through sparsity + linearity

### 3. Interpretability via Linearity + Sparsity

- **Semantic clustering**: Feedforward circuits in sgatlin form semantically structured clusters
- **Causal implication**: Individual linear neurons are causally implicated in factual recall
- **No replacement models needed**: Unlike standard FFN interpretation, sgatlin circuits can be interpreted directly without training additional replacement models
- The linearity of experts enables direct attribution analysis

### 4. Sparse Gating Mechanism

- Router computes scores over all available linear neurons
- Top-k selection (very small k relative to total neurons)
- Weighted sum of selected neurons produces the layer output
- Gating function is typically softmax or top-k with temperature

## Implementation Steps

1. **Replace FFN with sgatlin**: For each transformer layer, replace `FFN(x) = W2 * activation(W1 * x)` with `sgatlin(x) = Σ_{i∈topk} g_i(x) * (w_i^T x) * v_i`
2. **Scale neuron count**: Increase total neurons to match or exceed original parameter count
3. **Configure routing**: Set top-k value (typically k << total_neurons) for desired sparsity level
4. **Isoflop matching**: Ensure total FLOPs match baseline for fair comparison
5. **Training**: Train with standard language modeling objective
6. **Interpretability analysis**: After training, analyze semantic clusters via neuron weight inspection

## Key Results

- sgatlin improves perplexity over standard FFN at matched FLOPs
- Feedforward circuits form semantically structured clusters
- Neurons are causally implicated in factual recall
- Direct interpretation without auxiliary replacement models
- Path toward compute-efficient and interpretable transformer FFN layers

## Pitfalls

- **Nonlinearity removal is critical**: The key finding depends on removing the activation function from experts — adding it back degrades both performance and interpretability
- **Routing collapse**: With many tiny experts, routing may collapse to a subset — use entropy regularization on gating distribution
- **Gradient flow**: Linear experts may have different gradient dynamics — monitor training stability
- **Interpretability is not automatic**: Semantic clusters emerge but require careful analysis (weight inspection, causal intervention)

## Verification

- Reproduce isoflop comparison: same FLOPs, different architectures
- Verify perplexity improvement at matched compute budget
- Check semantic clustering via neuron weight analysis
- Perform causal intervention on individual neurons for factual recall

## Related Skills

- `emo-emergent-moe-modularity` — modular Mixture-of-Experts design
- `unipool-shared-expert-moe` — globally shared expert pool MoE
- `hierarchical-moe-detection` — hierarchical MoE for object detection
- `moe-optimal-transport-routing` — MoE routing via optimal transport
- `routing-distraction-multimodal-moe` — routing analysis in multimodal MoE

## Activation

sparse linear expert, sgatlin, tiny linear expert, sparsely gated linear, linear MoE, sparse transformer FFN, sparse gating interpretability, linear neuron expert, compute-efficient transformer
