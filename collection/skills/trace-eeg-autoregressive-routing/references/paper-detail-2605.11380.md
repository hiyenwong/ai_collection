# TRACE — Paper Detail (arXiv:2605.11380)

**Authors**: Fan Ma, Qier An, Peng Chen, Lingfei Qian, Xiang Lan, Mingyang Jiang, Zhiling Gu, Xenophon Papademetris, Hua Xu
**Institution**: Yale University, Dept. of Biomedical Informatics and Data Science
**Published**: 2026-05-12 | **Categories**: cs.LG, cs.AI

## Pre-Training Corpus

| Corpus | Type | Channels | Segments |
|---|---|---|---|
| TUEG | Clinical | Variable | Part of 1.5M total |
| HBN | Healthy population | High-density | Part of 1.5M total |
| Task datasets | Various | 16-128 | Part of 1.5M total |

Total: **1.5M+ EEG segments**, 4-30 second windows, band-pass 0.5-75 Hz, notch 60 Hz, resampled 200 Hz.
Pre-trained on **4 NVIDIA H100 GPUs**.

## Autoregressive Objective

Multi-horizon: H = {1, 2, 4} steps ahead. Captures short-term dynamics and longer-range transitions.

## Downstream Evaluation

| Task | Datasets | Transfer Type |
|---|---|---|
| Sleep Staging | ISRUC | Seen-domain |
| Emotion Recognition | SEED-V, FACED | Unseen/Seen |
| Motor Imagery | PhysioNet-MI, SHU-MI | Seen/Unseen |
| Seizure Detection | CHB-MIT | Seen-domain |
| Imagined Speech | BCIC2020-3 | Unseen |
| Event Classification | TUEV | Unseen |

## Why Not Token-Wise MoE

Token-wise routing assigns each channel patch independently. This **breaks cross-channel coherence** because channels at the same time step are different observations of a **shared latent brain state**. TRACE routes all channels at the same temporal step to the same experts based on causal cross-channel history.

## Key Design Decision

Instead of projecting all recordings onto a common montage, TRACE encodes each available channel as a temporal patch sequence with channel positional encoding. This enables true heterogeneous pre-training.
