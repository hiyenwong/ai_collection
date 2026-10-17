---
name: orionmoe-tabular-sparse-moe-foundation
description: "Compact tabular foundation model combining distribution-aware representations with dataset-conditioned sparse mixture-of-experts on a dual-axis Transformer: experts activate along the feature axis with routing informed by both individual feature representations and broader dataset context; pretrained entirely on synthetic classification tasks from a structured causal prior; downstream prediction without gradient adaptation. Use for tabular in-context learning with heterogeneous datasets, small-context or high-dimensional tables, class imbalance."
category: ai_collection
trigger: OrionMoE, tabular foundation model, mixture of experts, feature-axis routing, dataset-conditioned routing, dual-axis transformer, synthetic causal pretraining, in-context learning tabular, class imbalance, small-context prediction
---

# OrionMoE-v1.0: Sparse MoE for Tabular In-Context Learning

Methodology from arXiv:2610.20418 (Bouadi, Bouarour, Tanna, Sankarapu; 2026-10-14,
cs.LG/cs.AI).

## The Gap

Tabular foundation models predict unseen observations from a labeled support table without
task-specific parameter updates. Existing approaches are **dense**: the same transformations
applied across all features and datasets — wasteful and suboptimal when tabular problems vary
wildly in feature heterogeneity.

## The Architecture (three design moves)

1. **Dual-axis Transformer**: attention spans both the example axis and the feature axis —
   tabular rows and columns are both first-class.
2. **Dataset-conditioned sparse MoE along the feature axis**: routing decisions are informed
   by **both individual feature representations and the broader dataset context**, so
   computation is adaptively allocated across heterogeneous tabular problems while retaining a
   **shared computational pathway across tasks**.
3. **Pretraining entirely on synthetic classification tasks generated from a structured
   causal prior** — no real-data licensing or domain collection; downstream prediction
   proceeds **without gradient-based adaptation**.

## Results

- Competitive with **substantially larger** tabular foundation models across benchmarks.
- Particularly strong on **small-context** and **high-dimensional** datasets.
- Favorable relative performance under **class imbalance**; feature composition matters.

## Reusable Patterns

- **Feature-axis expert routing**: in domains where inputs are sets of heterogeneous
  attributes (tabular, multimodal sensor bundles, configuration spaces), route compute per
  feature, conditioned on dataset-level context — not per example only.
- **Synthetic causal-prior pretraining**: generate pretraining distributions from structured
  causal models instead of scraped data — controlled diversity, no leakage, infinite support.
- **Dense→sparse conversion for foundation models**: when serving many heterogeneous
  downstream tasks, a shared sparse pathway often beats a larger dense backbone at the same
  or better quality.

## When to Use

- Designing or selecting tabular foundation models for in-context prediction.
- Handling small-context or high-dimensional tabular problems.
- Pretraining data strategy: deciding between real curated corpora vs synthetic causal
  generators.
