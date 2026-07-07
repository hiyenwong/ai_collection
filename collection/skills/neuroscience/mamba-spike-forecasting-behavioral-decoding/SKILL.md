---
name: mamba-spike-forecasting-behavioral-decoding
description: "Implicit Behavioral Decoding from Next-Step Spike Forecasts at Population Scale — Mamba forecaster methodology for closed-loop BCI. A single Mamba model trained on next-step spike counts at Neuropixels scale simultaneously predicts future neural activity and decodes behavioral state via a lightweight linear readout. Use when: analyzing neural population spike data, building closed-loop BCI decoders, applying state-space models (Mamba/SSM) to neural time series, or studying implicit behavioral decoding from spike forecasts. Keywords: Mamba, spike forecasting, behavioral decoding, Neuropixels, closed-loop BCI, state-space model, neural population dynamics"
---
# Mamba Spike Forecaster for Implicit Behavioral Decoding

Methodology from arXiv:2605.12999 — "Implicit Behavioral Decoding from Next-Step Spike Forecasts at Population Scale" (May 2026, submitted to NeurIPS 2026 Neuroscience & Cognitive Science Track).

## Core Idea

A single Mamba (state-space model) forecaster, trained only on next-step spike counts at Neuropixels scale, delivers both a neural activity forecast AND an implicit behavioral readout in one forward pass. A lightweight per-session linear head reading the predicted firing rates decodes behavior better than the same linear head reading raw spike counts under matched temporal context.

## Key Findings

- **Dual function**: Mamba predicts next-step spike counts AND produces latent representations that encode behavioral state
- **Benchmark**: Steinmetz visual-discrimination benchmark — 39 sessions, ~27,000 neurons, 1,994 held-out trials
- **Mouse choice decoding**: 75.7±0.2% trial vote (~2.3x chance)
- **Stimulus side decoding**: 66.1±0.6% trial vote (~2x chance)
- **vs. Linear baseline**: Mamba beats 500ms-context linear decoder on raw spike counts by 4-6pp on both metrics
- **Fast calibration**: ~100-150 trials brings readout within 1-2pp of asymptote
- **Real-time feasible**: Full pipeline fits within 50ms bin budget on workstation GPUs

## Methodology

### Model Architecture
1. **Mamba backbone**: SSM-based sequence model processes binned spike counts across all recorded neurons
2. **Forecasting objective**: Train on next-step spike count prediction (self-supervised)
3. **Linear readout**: Lightweight per-session linear head on Mamba's hidden states for behavior decoding

### Training Pipeline
1. Bin spike trains to 50ms non-overlapping windows
2. Train Mamba with teacher-forcing on next-step prediction
3. After training, attach linear readout head
4. Calibrate with 100-150 trials per new session

## Key Technical Details

- **Input**: Population spike counts (Neuropixels scale, ~27k neurons across sessions)
- **Output**: Next-bin spike rate forecasts + behavioral state (choice, stimulus side)
- **Architecture**: Mamba state-space model (not Transformer)
- **Training signal**: Self-supervised (next-step prediction only, no behavior labels needed for the backbone)
- **Calibration**: Session-start calibration block with few trials
- **Hardware**: Workstation GPUs typical of tethered chronic Neuropixels recordings

## Why It Works

Mamba's sequential processing compresses the high-dimensional neural population activity into a lower-dimensional latent state that implicitly encodes task-relevant behavioral variables. The forecasting objective forces the model to learn the generative dynamics of the neural population, which naturally captures behaviorally relevant structure — even without explicit behavioral supervision.

## Activation

- spike forecasting
- behavioral decoding
- Mamba neural
- Neuropixels decoder
- closed-loop BCI
- implicit decoding
- neural population forecasting
- SSM neural time series
