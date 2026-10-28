---
name: ts2vec-fm-compact-time-series-foundation
description: "Use when a compact per-dataset SSL encoder needs to become a reusable time-series foundation model. Three-change recipe: synthetic-corpus pretraining, dual amplitude/shape view stems, per-view specialist distillation — 1.6M params within 0.3pp of SOTA."
category: ai_collection
metadata:
  arxiv_id: "2610.28602"
---

# TS2Vec-FM: Turning a Per-Dataset SSL Encoder into a Time-Series Foundation Model

Source: arXiv:2610.28602 (Feofanov, Tai, Ermakov, Rish — Mila, Oct 2026). TS2Vec (2022) is a strong self-supervised time-series encoder but designed to be retrained per dataset. The field moved to foundation models (one encoder reused across datasets) — usually attention-heavy, patch-tokenized, and large. This work keeps TS2Vec's compact convolutional design (variable-length inputs, no resampling) and converts it to a foundation model with **three changes**.

## The three-change recipe

1. **Pre-train on a synthetic corpus** (once) instead of per-target datasets.
2. **Dual-view input**: feed the encoder a raw **amplitude** view and an instance-normalized **shape** view through two small stems — separating scale information from shape information.
3. **Distill one specialist encoder per view into a single encoder** — merge the two-view specialists back into one frozen backbone.

## Results

- TS2Vec-FM: **1.6M-parameter** dilated convolutional network, kept **frozen**, linear probing: **83.3% UCR-128, 75.3% UEA-27** — within 0.3pp of MantisV2 (current SOTA) and **above TS2Vec trained separately on each target**.
- Design contrast worth remembering: near-parity reached **without attention, without a patch tokenizer, without intermediate-layer extraction** — an "old-school" conv encoder with a two-layer MLP stem.

## Reuse pattern

- Converting any compact SSL encoder into an FM: synthetic pretraining corpus (cheap, unlimited, diverse) + multi-view stems (disentangle nuisance factors like amplitude vs shape) + specialist-per-view → distill to single backbone.
- Prefer this when deployment budgets rule out attention-based FMs; linear-probe evaluation keeps the backbone frozen and cheap.
- Dual-view disentanglement generalizes: pick the two nuisance axes of your domain (scale/shape, trend/seasonality, speaker/content) and give each its own stem.

Related: TS2Vec, Mantis/MantisV2, lightweight EEG foundation models (frozen-encoder + small readout), tabular FMs (TabPFN-style frozen inference).
