---
name: chaotic-topological-preictal-eeg
description: CDRTL framework coupling Lorenz oscillator networks with persistent Laplacian fingerprints for preictal EEG node classification. Use for EEG topology-dynamics feature engineering.
category: ai_collection
metadata:
  arxiv_id: "2609.23317"
  published: "2026-09-17"
  authors: "Zihan Wang, Daixin Li, Guilin Wang, Mushal Zia, Xiaoqi Wei, Xiang Xiang Wang, Jian Jiang"
  tags: [epilepsy, eeg, persistent-laplacian, lorenz-oscillator, topological-data-analysis]
---

# CDRTL: Chaotic Dynamics-Regulated Topological Learning for Preictal EEG

## Overview

CDRTL (arXiv:2609.23317) fuses three feature families — **dynamical (Dyn_FPs), topological (Top_FPs), geometric (Geo_FPs)** — extracted from patient-specific EEG correlation networks, for transductive preictal/interictal channel-node classification on CHB-MIT (23 patients, cohort accuracy 0.994, sensitivity 0.995 under complete nested CV).

**Headline insight**: The Lorenz-oscillator-derived **dynamical fingerprints alone carry nearly all discriminative power** (selected for 18/23 patients; configs without D drop to 0.541-0.616 accuracy while D-containing configs reach 0.988-0.996). The paper is also a model of **honest scope reporting**: it repeatedly flags that results are transductive (fixed network, held-out node labels), NOT cross-patient or prospective seizure prediction.

## The Pipeline (5 steps)

### 1. Preprocessing
- 10-s nonoverlapping windows, 18 shared channels, bandpass 0.5-70 Hz, notch 60 Hz, normalize
- Per patient: 13 preictal windows (within 30 min before onset) + 13 interictal (≥3h from any onset, ≥1h after termination) → 468 channel-level nodes (234+234)

### 2. Functional differentiation (multiscale sub-networks)
- Pairwise Pearson correlation P_ij between channels; negative edges zeroed
- Partition edges into **10 decile intervals of correlation strength** → ten sub-networks with comparable edge density but different coupling regimes (strong=epileptogenic hubs, intermediate=transition zones, weak=long-range communication)

### 3. Coupled chaotic oscillator embedding → Dyn_FPs
- Every node = Lorenz oscillator (δ=10, γ=60, β=8/3), coupled through rescaled adjacency:
  `du_i/dt = f(u_i) + φ Σ_j A_ij u_j − u_i` with global coupling φ=0.42
- Integrate RK4, dt=0.01, 100 steps; discard transient, keep final 50 steps of x-traces
- Pool ALL node x-trajectories into one response vector → 6 stats (mean, median, variance, max, min, std) = **Dyn_FPs (60-dim per sub-network)**

### 4. Persistent Laplacian → Top_FPs + Geo_FPs
- Filtration K_0 ⊆ ... ⊆ K_m; q-th order p-persistent Laplacian Δ_q^{t,p} = ∂_{q+1}^{t,p}(∂_{q+1}^{t,p})* + (∂_q^t)* ∂_q^t
- **Harmonic spectra** (zero eigenvalues count) = topological invariants (Betti) → Top_FPs (~27-dim)
- **Non-harmonic spectra** (nonzero eigenvalues) = homotopic geometric evolution → Geo_FPs (~30-dim)
- Unlike persistent homology, PL captures BOTH invariants AND geometric deformation during filtration

### 5. Topological differentiation (node importance)
- Vectorize global features; remove node i; recompute; Euclidean distance ‖v − v_{−i}‖ = node influence
- Node-level local features = these difference vectors, concatenated across 10 sub-networks

### Classification
- Nested CV: 5 outer folds (eval only) × 3 inner folds (select among 7 feature configs × 5 classifiers × hyperparameters)
- Classifiers: LR, SVM, KNN, RF, GBDT — LR modal for 16/23 patients (features ≈ linearly separable within-patient)

## Control Experiments (the reusable scientific pattern)

| Control | Result | Interpretation |
|---------|--------|----------------|
| Sigmoid instead of Lorenz | acc 0.508 (chance) | Generic pointwise nonlinearity fails |
| tanh instead of Lorenz | acc 0.774 | Monotone nonlinearity partially works |
| Rössler instead of Lorenz | acc 0.998 | Robust to WHICH chaotic system — chaos matters, not Lorenz specifically |
| Shuffle connectivity weights (keep distribution) | 0.980 vs 0.982 | Dyn_FPs use collective/distribution-level response, not exact edge placement |
| Remove coupling (φ=0) | 0.516 (chance) | **Coupling is the mechanism** — uncoupled oscillators carry no signal |

The pair (weight-shuffle preserved + coupling-removal collapsed) is the cleanest demonstration that the discriminative signal lives in the **coupled collective temporal response**, not in the static connectivity pattern.

## Results Summary

- Cohort accuracy 0.994 (0.993-0.995 bootstrap CI), sensitivity 0.995, AUC 1.000
- Stable across 10 window-selection replicates: 0.994 ± 0.001
- Reimplemented SET-SVD-1D-CNN control under identical protocol: 0.534 (gap 0.460)
- Cumulative multiscale fusion: single-scale 0.780-0.979 → all 10 intervals 0.994 (monotone improvement)
- Ensemble consensus: 5-10 models per feature domain suffice for stable predictions; G+T (no D) stays at chance 0.5 regardless of ensemble size
- Preictal nodes overrepresented in top-25 importance ranks (21/25) — preictal state = higher network vulnerability (removal-induced feature change)

## Critical Limitations (as stated by authors — preserve these)

1. **Transductive only**: complete unlabeled network (all channels) used in feature construction BEFORE CV. No inductive out-of-network mapping exists → cannot classify new windows/patients
2. **No leave-one-seizure-out**: withholding a seizure leaves its windows without a feature mapping
3. **No prospective validation**: event-level metrics (sensitivity, false alarms/hour, prediction horizons, refractory periods) require continuous recordings; balanced windows cannot support them
4. **Spectral fingerprints' cost unjustified**: no runtime benchmark of PL computations; Dyn-only implementation would skip them
5. **Channel-level nodes inherit window labels** — classification unit is a channel, not a seizure event

## Implementation Sketch

```python
# 1. Correlation network
P = np.corrcoef(X)  # X: channels × time
P[P < 0] = 0
# 2. Decile partition → 10 adjacency matrices A_k (exponential rescale)
# 3. Coupled Lorenz per sub-network
#    du_i/dt = f_lorenz(u_i; δ=10, γ=60, β=8/3) + 0.42 * Σ_j A_k[i,j] (u_j − u_i)
#    RK4, dt=0.01, 100 steps, keep last 50 x-values of all nodes
#    Dyn_FPs = [mean, median, var, max, min, std] of pooled x-traces
# 4. Persistent Laplacian per sub-network (harmonic counts + nonzero eigenvalues)
# 5. Node removal: ‖feat(G) − feat(G∖i)‖ → local features
# 6. Nested CV with config+classifier selection in inner folds ONLY
```

## Pitfalls

- **Do not cite this as seizure prediction** — it is transductive channel-node discrimination; authors explicitly disclaim warning-system validity
- **φ=0.42 coupling is load-bearing** — verify coupling survives any adaptation (φ=0 → chance)
- **Negative correlations zeroed** — simple choice, limits information; consider abs() variant
- **18 channels, 10-s windows, 13+13 balanced windows** — small per-patient sample; window-selection sensitivity was tested (stable) but budget is fixed
- **Lorenz γ=60** (not standard 28) — steeper attractor; the Rössler control suggests the class of chaotic systems matters, not parameter-fidelity to the classic attractor

## Applications

- Patient-specific feature engineering for any channel-level EEG state discrimination (not only epilepsy: sleep stages, BCI states, anesthesia depth)
- The **coupled-oscillator response vector** is a cheap general-purpose network descriptor — 6 pooled statistics of x-traces beat 57 spectral features
- Topological differentiation gives interpretable node-importance maps (epileptogenic zone candidates)
- Controls suite (sigmoid/tanh/Rössler/shuffle/uncoupled) is a template for validating any "dynamics-as-features" pipeline

## Related Skills

- [[topological-ml-eeg-classification]] — TDA for EEG/iEEG
- [[higher-order-topological-ad-alzheimer]] — higher-order topological features
- [[seizure-suppression-hub-stimulation]] — seizure network control
- [[chaotic-regularization-discrete-signaling]] — chaos in recurrent networks

## Source

arXiv:2609.23317 — Wang, Li, Wang, Zia, Wei, Wang, Jiang, "Chaotic Dynamics-Regulated Topological Learning for Patient-Specific Preictal State Identification" (2026). Data: CHB-MIT (PhysioNet).
