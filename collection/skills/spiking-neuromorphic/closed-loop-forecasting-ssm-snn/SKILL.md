---
name: closed-loop-forecasting-ssm-snn
description: "Use when forecasting with autoregressive SSM/SNN models whose own predictions must become their own inputs. Two closed-loop feedback strategies (model-level, layer-level) beat zero-masking and match SpaceTime on ETT."
category: ai_collection
metadata:
  arxiv_id: "2610.28495"
---

# Closed-Loop Forecasting with SSM-Based Spiking Neural Networks

Source: arXiv:2610.28495 (Stolt, Karilanova, Ozcelikkale, Oct 2026). Deep state-space models (S4-family) and SNNs (spikes as single-bit events) process time series autoregressively, but **forecasting** (predicting future values from past observations alone) breaks the loop: the network's own generated values are not available as inputs during the forecasting phase. The standard fix (S4) is **zero-masking** of missing inputs.

## Two closed-loop strategies

1. **Model-level closed-loop**: feed the network's own generated outputs back into the input as if they were observed past values (outer feedback around the whole model).
2. **Layer-level closed-loop**: feed predicted values back **per layer** (inner feedback between SSM layers).

Both treat the model as a generative closed-loop system during the forecast horizon instead of masking.

## Results (ETT-small benchmark)

- Evaluated under both **spike-based and continuous activation functions**.
- Both closed-loop approaches perform **comparably to or better than zero-masking with S4**, and in most cases **match SpaceTime** (SOTA).
- Highlights the trade-off between continuous and low-bit quantized activations for forecasting quality.

## Reuse pattern

- Any autoregressive sequence model used for *forecasting* (not teacher-forced reconstruction) faces the missing-input problem; choose deliberately between:
  - zero-masking (baseline, discards the model's own dynamics),
  - model-level closed loop (single outer feedback, simplest),
  - layer-level closed loop (richer, per-layer self-conditioning).
- For SNN/SSM hybrids, closed-loop feedback is the step that makes spike-based low-bit activations actually usable for multi-step prediction.
- Evaluate with spike vs continuous activations separately — quantization changes which strategy wins.

Related: S4/S5 zero-masking, SpaceTime, SpikingJelly forecasting models, scheduled sampling (older autoregressive feedback trick), world-model rollout chains.
