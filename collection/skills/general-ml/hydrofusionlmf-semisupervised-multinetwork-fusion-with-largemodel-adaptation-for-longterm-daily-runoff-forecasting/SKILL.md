# HydroFusion-LMF: Semi-Supervised Multi-Network Fusion with Large-Model Adaptation for Long-Term Daily Runoff Forecasting

**arXiv ID:** 2510.03744
**Authors:** Qianfei Fan, Jiayu Wei, Peijun Zhu, Wensheng Ye, Meie Fang
**Published:** 2025-10-04T09:09:06Z
**Abstract:**
Accurate decade-scale daily runoff forecasting in small watersheds is difficult because signals blend drifting trends, multi-scale seasonal cycles, regime shifts, and sparse extremes. Prior deep models (DLinear, TimesNet, PatchTST, TiDE, Nonstationary Transformer, LSTNet, LSTM) usually target single facets and under-utilize unlabeled spans, limiting regime adaptivity. We propose HydroFusion-LMF, a unified framework that (i) performs a learnable trend-seasonal-residual decomposition to reduce non-stationarity, (ii) routes residuals through a compact heterogeneous expert set (linear refinement, frequency kernel, patch Transformer, recurrent memory, dynamically normalized attention), (iii) fuses expert outputs via a hydrologic context-aware gate conditioned on day-of-year phase, antecedent precipitation, local variance, flood indicators, and static basin attributes, and (iv) augments supervision with a semi-supervised multi-task objective (composite MSE/MAE + extreme emphasis + NSE/KGE, masked reconstruction, multi-scale contrastive alignment, augmentation consistency, variance-filtered pseudo-labeling). Optional adapter / LoRA layers inject a frozen foundation time-series encoder efficiently. On a ~10-year daily dataset HydroFusion-LMF attains MSE 1.0128 / MAE 0.5818, improving the strongest baseline (DLinear) by 10.2% / 10.3% and the mean baseline by 24.6% / 17.1%. We observe simultaneous MSE and MAE reductions relative to baselines. The framework balances interpretability (explicit components, sparse gating) with performance, advancing label-efficient hydrologic forecasting under non-stationarity.

## Skill Description

This skill is generated from the arXiv paper: HydroFusion-LMF: Semi-Supervised Multi-Network Fusion with Large-Model Adaptation for Long-Term Daily Runoff Forecasting (2510.03744).

## How to Use

[To be filled in by the user or by future automation]

## References

- [arXiv:2510.03744](http://arxiv.org/abs/2510.03744v1)
