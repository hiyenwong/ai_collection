---
name: scff-support-compiled-feature-folding
description: Use when running tabular foundation models on wide tables under GPU memory limits. Training-free inference framework converting quadratic feature-interaction cost to linear-in-width with bounded working set, no ensembling or new parameters.
trigger: tabular foundation model, wide table inference, feature folding, quadratic feature mixing, GPU memory tabular, support-ranked features, frozen backbone inference, TabICLv2 TabPFN
category: ai_collection
---

# SCFF: Support-Compiled Feature Folding for Wide-Table Tabular FMs

**Source**: arXiv:2609.28208v1 (2026-09-23) — Zhou, Jin, Wang, Yang, Wang et al. (9 authors).

## Problem

Tabular foundation models (TabICL, TabPFN, etc.) face a **feature-side scaling dilemma**: full-width pairwise feature mixing grows **quadratically** with column count, while feature selection saves memory but **discards evidence**.

## SCFF Mechanism (training-free, frozen backbone)

1. **Support-ranked features** are routed through **bounded leaves** of the native feature encoder — each leaf processes only a bounded working set of columns (fitting encoder's native width limit).
2. **Support-checks the residual evidence**: features left out of a leaf get checked for relevance (support scores) rather than silently dropped.
3. **Merges encoded messages** across leaves before a **single contextual prediction** — not an ensemble of predictions.
4. Result: quadratic feature-interaction work → **linear-in-width** work with bounded local working set.

## Verified Results

18-dataset wide-table slice of AMLB-29 / TabZilla / TabArena snapshots, 6 backbones:

| Metric | Result |
|---|---|
| Dataset-macro accuracy & NLL | improved on **all six** backbones |
| Relative error reduction (matched width) | up to **26.1%** (95% bootstrap CIs favorable) |
| Median paired GPU-memory savings | **2.09×–2.36×** |
| Max peak-memory ratio | **34.3×** |
| Under fixed memory ceiling: reuse saved budget for more evidence | +4.06 / +3.72 points over widest single leaf (TabICLv2 / TabPFN-3 wide-Core strata) |

Key insight: saved memory buys back *evidence* (more support-selected features processed), not just speed.

## Implementation Checklist

1. Freeze backbone; compute feature support scores (e.g., permutation importance or the FM's native attention/feature attribution).
2. Rank features by support; partition into bounded leaves ≤ encoder native width.
3. Encode each leaf with the native feature encoder; run a support check on residual features (cheap relevance test).
4. Merge per-leaf message embeddings (concat/add/attention-pool) → single context row → one contextual prediction.
5. Under a memory ceiling: allocate leaves to maximize support-weighted evidence coverage, not uniform width.

## When to Use

- Wide tables (hundreds–thousands of columns) exceeding FM native width.
- Deployment with hard GPU memory ceilings.
- Need to keep ALL weak-but-real evidence (feature selection would discard it) while staying within budget.

## Related Skills

- `wind-solar-csfs-feature-selection` — classic feature selection contrast
- `zeta-law-biomedical-scaling` — tabular data scaling laws
