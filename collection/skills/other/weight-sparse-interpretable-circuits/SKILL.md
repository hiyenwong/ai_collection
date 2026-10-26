---
description: Use when training weight-sparse LMs for interpretability.
name: weight-sparse-interpretable-circuits
category: ai_collection
version: 1.0
author: openai-research-cron-2026-10-26
license: MIT
metadata:
  hermes:
    tags: [weight-sparsity, mechanistic-interpretability, minimal-circuits, circuit-discovery, pruning, mean-ablation, disentanglement, capability-interpretability-frontier, sparse-transformers]
    related_skills: [attention-mechanisms, sparsified-kan-quantum-tomography, activation-region-decision-tree-networks]
---

# Weight-Sparse Transformers Have Interpretable Circuits

Methodology from OpenAI "Understanding neural networks through sparse circuits" (Nov 13, 2025) and paper arXiv:2511.13653 "Weight-sparse transformers have interpretable circuits".

## One-Line Summary

Instead of post-hoc analysis of dense models, train transformers where the vast majority of weights are forced to zero (L0-constrained, ~1 in 1000 nonzero): each neuron reads/writes only a few residual channels, so concepts cannot spread across superposed channels — minimal task circuits come out ~16× smaller than dense baselines at matched pretraining loss, are fully reverse-engineerable, and validate via necessity + sufficiency ablations.

## When to Use / Activation

- Designing interpretability-by-training experiments (interpretability as a training constraint, not an afterthought).
- Extracting and validating minimal circuits for specific behaviors (node-based pruning + mean-ablation).
- Mapping the capability–interpretability frontier (sparsity vs. size tradeoffs).
- Predicting model behavior adversarially from a reverse-engineered mechanism (mechanism-grounded red-teaming).
- Bridging findings from sparse pilot models to dense production models (cross-model steering bridges).

## Core Construction (reusable machinery)

1. **Weight-sparsity training.** GPT-2-style decoder-only transformer; after each AdamW step keep only the top-magnitude entries of every weight matrix, bias, and token embedding, zeroing the rest; anneal the nonzero fraction toward a target. Extreme setting: ~1/1000 nonzero weights; add mild activation sparsity (~1/4 nonzero) at all nodes. Hold L0 (nonzero-parameter count) fixed while varying width to isolate sparsity from scale.
2. **Hand-curated algorithmic task suite.** Simple Python next-token tasks with knowable ground-truth algorithms (single/double quote closing, set_or_string `.add` vs `+=`, bracket nesting depth) to keep circuit ground truth checkable.
3. **Minimal-circuit extraction.** Node-based pruning where a node = (MLP neuron at a layer) | (attention head) | (residual channel). Pruned nodes are mean-ablated (replaced by mean activation over the pretraining distribution). Learn continuous mask parameters with a Heaviside-style gate optimized via straight-through estimator (surrogate gradient). Circuit size metric: count of active edges between retained nodes; report geometric mean across tasks.
4. **Necessity + sufficiency validation.** Sufficiency: mean-ablate everything outside the circuit → task loss preserved. Necessity: ablate only the circuit's few nodes → task loss destroyed. This is the rigor bar a "circuit" claim must pass.
5. **Worked example (quote closing).** Layer-0 MLP builds a quote-detector neuron (residual ch 985, fires on both quote types) and a quote-type classifier (ch 460, +double/−single); a layer-10 attention head (10.attn.head82) uses the detector as key and the type classifier as value, with a constant positive query at the final token → copies the opening quote type to the closing position. Total: ~5 residual channels, 2 MLP neurons, 1 QK + 1 V channel.
6. **Scaling finding.** At matched pretraining loss, weight-sparse models yield ~16× smaller minimal circuits than dense models; increasing model size shifts the capability–interpretability frontier outward (bigger AND sparser = more capable while still interpretable); beyond tens of millions of nonzero parameters, preserving interpretability remains open.
7. **Mechanistic adversarial prediction.** From the recovered bracket-counting mechanism (residual ch 1249 encodes nesting depth as an activation magnitude averaged over context): a long flat list "dilutes" the mean → model mispredicts `]`; the same attack transfers to similarly-capable dense models — evidence the mechanism, not sparsity idiosyncrasy, is shared.
8. **Sparse→dense bridge.** Perturb the sparse model's quote-type channel at the input to its final attention layer, then map ("bridge") the perturbation into a dense counterpart → dense model's closing-quote probability flips accordingly. Preliminary path to explaining existing dense models rather than only training new sparse ones.

## Pitfalls / Lessons

- Sparse models are inefficient to train and deploy and unlikely to reach frontier capability — position them as interpretability testbeds, complements to post-hoc dense analysis.
- A validated circuit is guaranteed only on the task distribution it was pruned on; off-distribution behavior can route through other components.
- Sparsity trades away raw capability; report pretraining loss alongside circuit size so "interpretable" doesn't silently mean "much weaker".
- Two escape hatches when de novo training is impractical: extract sparse circuits from dense models, or use sparse→dense bridges.

## References

- OpenAI blog: https://openai.com/index/understanding-neural-networks-through-sparse-circuits/
- Paper: arXiv:2511.13653 (Weight-sparse transformers have interpretable circuits)
- Pruning-as-mask-learning lineage: straight-through Heaviside gates; mean-ablation validation protocol.
