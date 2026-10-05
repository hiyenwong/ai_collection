---
name: spikelite-snn-forecasting
version: v1.0.0
last_updated: 2026-09-30
description: "SpikeLite methodology — lightweight SNN time-series forecasting via FSSE (exploit LIF low-pass behavior to split input into frequency-selective components) and SSCA (binary-masked sparse cross-channel spiking attention), with a channel-independent fallback. Use when: (1) energy-efficient forecasting on edge, (2) SNN attention is too heavy, (3) frequency-aware temporal encoding for spike models. Keywords: SNN forecasting, frequency-selective encoding, sparse channel attention, LIF low-pass, energy efficiency."
arxiv_id: "2609.35097"
authors: "Bang Hu, Changze Lv, Mingjie Li et al. (6 authors)"
tags: [snn, time-series, forecasting, attention, energy-efficiency, edge]
---

# SpikeLite: Lightweight Spiking Forecasting with Frequency-Selective Encoding

From arXiv:2609.35097 (2026-09-28).

## Position

Recent SNN forecasters chase accuracy with heavy attention or exotic neuron dynamics — defeating the lightweight purpose of SNNs. SpikeLite goes the other way: two small modules, both spike-driven, plus a **channel-independent fallback** when cross-channel interaction isn't needed.

## Module 1: FSSE — Frequency-Selective Spiking Encoder

**Key trick: exploit the LIF neuron's own low-pass filtering as a feature, not a bug.**

- LIF membrane dynamics attenuate high frequencies — so feeding the input at **different effective time constants / decompositions** yields components with different frequency sensitivity.
- Reorganize each input sequence into **frequency-sensitive components** while collectively preserving the full input at the decomposition stage (no information loss before selection).

## Module 2: SSCA — Sparse Spiking Channel Attention

- Learn a **binary mask** from encoded channel representations.
- Use it inside spike-driven self-attention to **selectively exchange** cross-channel information: retain informative interactions, suppress redundant ones.
- Binary mask = no dense softmax over channels = keeps the spike-driven, event-friendly computation.

## Routing

```
if task needs cross-channel structure:
    input → FSSE → SSCA(masked spiking attention) → readout
else:                          # lighter path
    input → FSSE → readout     # channel-independent
```

## Key Results (SeqSNN + SpikF protocols, 4 multivariate + 8 long-term benchmarks)

| Metric | Result |
|---|---|
| Aggregate R² / RSE | best: 0.790 / 0.440 |
| Long-term MSE / MAE | best average: 0.343 / 0.345 |
| Energy (ECL dataset) | lowest reported SNN forecasting consumption |

## When to Use

- Multivariate or long-horizon forecasting under energy budgets (edge/IoT).
- Building SNN encoders: the **LIF-as-filters** decomposition (FSSE) transfers to any spike-based temporal encoder.
- Whenever adding attention to an SNN — SSCA's binary-mask pattern keeps it sparse and spike-compatible.

## Design Notes

- FSSE insight generalizes: neuron dynamics ARE differentiable-ish filters — parameterize their time constants instead of bolting on FFT blocks.
- Always benchmark the channel-independent path: on several benchmarks it matched the full model, and the paper's protocol explicitly reports both.
- Spiking attention should mask *interactions*, not tokens — masks over the channel axis preserve event sparsity.
