---
name: temporal-simplicial-eeg-decoding
description: T-SNN temporal simplicial network for EEG decoding. Use when higher-order brain interactions or dynamic connectivity matter.
category: ai_collection
---

# T-SNN: Temporal Simplicial Neural Network for EEG Decoding

**Paper**: arXiv:2609.34002 (27 Sep 2026) — Malik, Roy, Kataria, Herath, Yadav, García-Redondo, Bhaskar (IIT Delhi/Gandhinagar, Pitt, Tübingen, UW–Madison)
**Code**: https://github.com/UW-Madison-CBML/temporal-simplicial-nn

## When to Use

- EEG/multivariate neural decoding where interactions among **groups of channels** (not just pairs) may carry signal (synergistic information beyond pairwise graphs)
- Trials with **time-varying connectivity** — reorganization of group-level interactions within a trial
- Multimodal brain-state decoding (EEG + eye movement / physiology) needing a late-fusion embedding

## Method Pipeline (5 steps)

### 1. Simplicial Lift (per overlapping window)
- Sliding windows: **8 s window, 4 s stride** over each trial
- Per window: pairwise Pearson correlations ρ_ij among channels
- Retain pairs with |ρ_ij| above the **97th percentile** within that window
- Build **clique complex up to rank R=2**: channel = 0-simplex; retained pair = 1-simplex; triple of channels with all 3 edges = 2-simplex (triangle)
- Node features: **Welch log-band-power** per frequency band (Delta 1-4, Theta 4-8, Alpha 8-14, Beta 14-31, Gamma 31-50 Hz; F=5)
- Simplex weight: ω_s = mean correlation over channel pairs in s; simplex feature x_s = ω_s × mean of member node features
- Per window: same-rank adjacency A_r^(t) (sparse) + incidence B_r^(t) between ranks r-1 and r

### 2. Encoding + Temporal Phase
- Per-rank linear encoder: H_r^(t) = X_r^(t) W_r ∈ R^{n_r×d} (shared width d)
- Window position τ_t = t/T ∈ [0,1] expanded on geometric sinusoidal basis [τ, sin(2^kπτ), cos(2^kπτ)]_{k=0}^{K-1}, K=8 frequencies
- Phase embedding projected to R^d, broadcast to every cell at every rank

### 3. Simplicial Message Passing (SCCN layer)
Aggregate for each rank-r cell: same-rank neighbors (A_r), boundary cells of rank r-1 (B_r^T), co-boundary cells of rank r+1 that it bounds (B_{r+1}):

```
H_r' = σ( A_r H_r Θ_{r→r} + B_r^T H_{r-1} Θ_{r-1→r} + B_{r+1} H_{r+1} Θ_{r+1→r} )
```

- Separate learned Θ for each message direction; σ = sigmoid (sum aggregation)
- Omit terms with ranks outside [0, R]

### 4. Joint Spatiotemporal Blocks (SCCN + LSTM per rank)
- L=2 blocks, **weights shared across windows**
- Per rank: LSTM summarizes previous-window state into H_p; stack [H^(t); H_p] and augment operators:

```
Ã_r = [[A_r, I], [0, 0]],  B̃_r = [[B_r B_e^T ...]]   (route messages to current cells from current + past features, same and adjacent ranks)
H_r^(t,ℓ+1) = SCCN([H_r^(t,ℓ); H_{p,r}], Ã, B̃)[1:n^(t)]
```

- **Simplex-identity state tracking**: because simplices disappear/reappear as connectivity changes across windows, recurrent states are keyed by **simplex identity** (not row position) — a returning simplex resumes its previous state. This is the critical implementation detail.

### 5. Readout + Multimodal Fusion
- Mean-pool cells per rank → concat ranks → z_t ∈ R^{(R+1)d}
- Extra modality: standardize (train-fold stats), MLP → e_t ∈ R^d; concat with z_t
- Average across windows; linear classifier: ŷ = softmax(W [z_t; e_t] + b)

## Training Recipe

- Adam, lr 3e-4, cross-entropy, gradient-norm clip 5.0, 100 epochs, select best validation macro-F1
- d=512, L=2, K=8, R=2, ε=1e-8 in log-power
- Block-diagonal minibatches with sparse ops: batch 64 (trial-wise) / 256 (cross-subject)
- Cost: ~50 s/epoch on H200 — 2.5–9× faster than JODIE/GraphMixer/TGN despite larger width (baselines d=100)

## Results (SEED-VII, 7-class emotion, N=20 subjects × 80 trials)

| Setting | T-SNN | Best baseline |
|---|---|---|
| Trial-wise EEG-only (all bands) | **70.94 ± 1.86** acc / 70.58 F1 | MAET 58.11 / GCNCA 58.04 |
| Theta band only | **72.62 ± 1.67** | Transformer 53.96 |
| Leave-one-subject-out | **69.87 ± 6.49** acc / 68.26 F1 | MAET 40.90 |
| EEG + eye movement | **77.50 ± 0.68** acc / 77.45 F1 | MAET 71.28 |

- +12.8 points over prior SOTA trial-wise; +29 points LOSO — generalization gap nearly closed
- Strongest band for T-SNN is **theta** (baselines peak in beta/gamma) — higher-order structure adds orthogonal signal
- Temporal-graph event models (JODIE/GraphMixer/TGN ≤27%) are unsuited to window-based connectivity

## Key Takeaways for Reuse

1. **Clique-complex lift of a thresholded correlation graph** is a cheap, general way to expose higher-order interactions in any windowed multivariate signal
2. **97th-percentile adaptive threshold** (per window) controls simplex count without tuning an absolute ρ cut
3. **Simplex-identity recurrent state** handles birth/death of cells across windows — reusable wherever topology is time-varying
4. **Augmented-operator SCCN pass** (stack current + summarized past, then one convolution) implements joint spatial-temporal message passing in a single operation, instead of alternating spatial-then-temporal passes
5. Late fusion of a standardized non-EEG modality via small MLP + concat is enough for large gains (+6.6 points) with reduced variance
6. Generalizes beyond EEG: any time-varying higher-order interaction data (molecular/cellular systems, population dynamics)

## Limitations / Extensions (from authors)

- Interpretation of inferred simplices in neurophysiological terms is future work
- Clique-complex construction could be replaced by Granger-causality-based simplices
