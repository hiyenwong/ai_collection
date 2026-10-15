---
name: hybra-eeg-hyperbolic-region-aggregation
description: Montage-invariant EEG SSL via hyperbolic region tokens.
category: ai_collection
---

# HyBRA-EEG: Hyperbolic Global-Local Brain-Region Aggregation for Self-Supervised EEG Representation Learning

**Source**: arXiv:2610.16589 (Xin Liu, Feng Lu, Wei Li, v1, 12 Oct 2026, cs.LG)
**Trigger**: EEG foundation model, montage heterogeneity, channel-to-region tokenization, hyperbolic matching, EEG self-supervised pretraining, 跨数据集 EEG 迁移, 电极蒙太奇差异, region token, Poincaré ball, EEG 蒙太奇不变性

## Problem

EEG self-supervised pretraining across datasets is blocked by **montage heterogeneity**: different labs use different channel counts/layouts. Channel-aware designs (BIOT, LaBraM, CBraMod, CSBrain) keep spatial meaning attached to channel identity — a channel token from one dataset has no counterpart in another, and same-named electrodes behave differently under different reference schemes. This entangles task-relevant neural patterns with dataset-specific spatial regularities, limiting cross-paradigm transfer.

**Key insight**: map montage-dependent channel observations into a **fixed region-token space** (K scalp regions shared by all datasets), and preserve fine-grained channel evidence through a parallel injection pathway.

## Architecture (5 components)

```
EEG X ∈ R^{B×C×T}
  → [1] Coordinate-Aware Patch Encoding  (C channel tokens × P patches, + 10-05 coord embed)
  → [2] Hyperbolic Region Mixer           (channel→region matching in Poincaré ball)
  + [3] Channel-Evidence Injection         (parallel: raw channel evidence → region tokens)
  → [4] Region-Time Transformer            (4-layer axial: temporal attn within region, region attn across)
  → [5] Masked region-time SSL             (latent feature prediction + region-level signal reconstruction)
```

### 1. Coordinate-Aware Patch Encoding (Eq. 1–2)
Each channel is split into P temporal patches, encoded by a shared multi-scale CNN encoder fθ:
- `H_{b,c,p} = fθ(X^p_{b,c,p})`, H ∈ R^{B×C×P×D}
- Add 3D electrode coordinate (10-05 system) encoding: `H̃ = H + φ(q_c)` where φ: R³→R^D

### 2. Hyperbolic Region Mixer (Eq. 3–5) — the core novelty
Given montage-specific channel-to-region prior A ∈ [0,1]^{C×K} (which channels may serve which region; C_k = {c | A_{c,k} > 0}):
- Map channel tokens and learnable region prototypes to the Poincaré ball: `z_{b,c,p} = exp_0^κ(W_h h̃_{b,c,p} + b_h)`, `ρ_k = exp_0^κ(µ_k)`
- Compute hyperbolic distance `d_{b,c,k,p} = d^κ_B(z_{b,c,p}, ρ_k)`
- **Prior-constrained, feature-dependent matching weights**:
  `α_{b,c,k,p} = softmax_{c∈C_k}( ℓ_{c,k} − λ·d_{b,c,k,p} )` where `ℓ_{c,k} = log(max(A_{c,k}, ε))`, λ = softplus(β) > 0
  (prior sets initial weights when entries differ; distance adapts them to current features; channels outside C_k get zero weight)
- Aggregate back in tangent space: `r^agg_{b,k,p} = Σ_c α_{b,c,k,p} · log_0^κ(z_{b,c,p})`
- Empty-region fallback: uniform α = 1/C. Output keeps a **fixed region axis** R ∈ R^{B×K×P×D} — identical shape for every montage.

### 3. Channel-Evidence Injection (Eq. 6–8)
Many-to-one aggregation attenuates channel-level cues (e.g., sleep spindles, beta bursts). A parallel branch preserves them:
- Region-specific linear scorer on pre-aggregation tokens: `s_{b,c,k,p} = w_k^T LN(h̃_{b,c,p})`
- Evidence weights: `η_{b,c,k,p} = softmax_{c∈C_k}( s_{b,c,k,p} + ℓ_{c,k} )`, evidence `e^ch_{b,k,p} = Σ_c η_{b,c,k,p} h̃_{b,c,p}`
- Feature-wise gated injection: `R_{b,k,p} = r^agg_{b,k,p} + σ(γ_k) ⊙ Dropout(W_o LN(e^ch_{b,k,p})) + b_o`
  (γ_k ∈ R^D controls per-dimension injection strength)

### 4. Region-Time Transformer (Eq. 9–10)
Axial attention on the K×P grid with learnable region/time embeddings:
- Temporal attention (within region, across patches) → Region attention (across regions, per patch) → FFN, pre-norm + residual, L=4 blocks.

### 5. Self-Supervised Pretraining (Eq. 11–12)
Mask ratio 0.4 over region-time tokens (masked positions replaced by learnable token m):
- **L_feat**: cosine loss between predicted and pre-mask token features (target detached + LayerNorm + ℓ2-normalized)
- **L_raw**: reconstruction of a normalized region-level signal (derived from input patches via the channel-to-region prior)
- Total: `L_SSL = L_feat + λ_raw·L_raw` (λ_raw = 0.5). Pretrain 200 epochs, AdamW peak lr 3e-4, cosine schedule.

## Results

| Setting | Result |
|---|---|
| 6 downstream datasets (MI/clinical/workload) | Highest mean BAcc on **all 6**; macro 0.7278 |
| vs CSBrain / LaBraM / BIOT / EEGPT (macro) | +5.03% / +8.48% / +15.29% / +18.29% |
| Parameters | **1.45M** vs CSBrain 44.86M (30.9×), EEGPT 25.32M (17.4×) |
| OpenBMI-MI (subject-group 6-fold) | 81.17% BAcc ≈ CSBrain 81.04%, but +1.84 AUROC, +5.23 AUPRC, 96.8% fewer params |
| TUEV | 71.40% BAcc vs CSBrain 69.03% (+2.37) |
| MentalArithmetic | 76.63% vs LaBraM 69.64% (+6.99) |
| Hyperbolic vs Euclidean/cosine matching (parameter-matched) | Hyperbolic wins on TUAB & TUEV |

Ablations (BAcc drop):
- Remove coordinate encoding: −1.67 (TUAB) / −5.85 (TUEV)
- Remove region tokenization (channel-time tokens directly): −2.44 / −9.74
- Remove channel-evidence injection: −1.01 / −6.72
- Remove region-level signal reconstruction: −9.8 on TUEV (0.7140→0.6158)
- Remove SSL pretraining (random init): −1.01 / −4.36

Region granularity: 11-region partition (bilateral lobar + **dedicated midline token for z-electrodes**) > 10-region bilateral > 5-region lobar. Hemispheric separation alone: +8.65 pts on OpenBMI-MI (72.25→80.90).

Interpretability: IG attribution for hand motor imagery concentrates in left/right-central tokens (~30%); token-perturbation confirms faithfulness (replace top-attributed token → BAcc 0.8117→0.7248; five lowest → no drop). t-SNE: best Silhouette 0.200, best Davies-Bouldin 1.621 vs 5 baselines.

## Implementation Recipe

```python
# Pseudocode — Hyperbolic Region Mixer
# prior A: (C, K) binary/soft; per-montage, built from electrode names/coords
ell = torch.log(A.clamp_min(1e-8))                    # (C, K) prior logits
z = expmap0(h + coord, c=-1.0)                       # channel tokens → Poincaré ball
rho = expmap0(region_prototypes)                      # (K, D) learnable prototypes
d = poincare_dist(z.unsqueeze(2), rho)               # (B, C, K, P)
logits = ell - softplus(beta) * d                     # prior + feature-dependent distance
logits = logits.masked_fill(A.T == 0, -inf)           # zero weight outside C_k
alpha = softmax(logits, dim=1)                        # over channels within region
r_agg = (alpha.unsqueeze(-1) * logmap0(z).unsqueeze(2)).sum(1)  # (B, K, P, D)
```

Pretraining data: 7 public subsets (SSVEP/MI/EMO: BETA, Tsinghua, Cho2017, PhysioNet-MI, FACED, SEED-V), resampled to 200 Hz. Fine-tune end-to-end with a compact CNN head on the full region-time grid.

## When to Use / Alternatives

- **Use HyBRA** when: pretraining across EEG datasets with different montages; wearable/low-channel transfer to high-channel clinical settings; parameter budget matters (edge/BCI).
- **Channel-token approaches** (LaBraM, CBraMod, CSBrain) when: single-montage setting, need absolute spatial specificity, no coordinate metadata.
- Related skills: `eeg-foundation-model-adapters` (lightweight adaptation), `fc-guided-band-selection-bci` (spectral priors), `hyperbolic-gcn-brain-network` (hyperbolic for fMRI graphs — different substrate).

## Pitfalls

1. **Prior leakage**: ℓ_{c,k} must be log of the *prior*, not learned free weights — the hyperbolic distance adapts the prior, it does not replace it. Without the prior mask, out-of-region channels contaminate tokens.
2. **Evidence injection is critical for waveform tasks**: removing it costs −6.72 pts on TUEV (event/graphoelement classification) — aggregation alone attenuates spikes/spindles.
3. **Midline token matters**: z-electrodes (Cz, Fz, Pz...) get a dedicated region token; lumping them into lobar groups loses midline generators (ERPs, sleep).
4. **Empty regions**: datasets whose montage covers no electrode for a region need the uniform 1/C fallback, else softmax over an empty set yields NaN.
5. **Region-signal reconstruction is the strongest SSL term for event tasks** (−9.8 TUEV); latent-feature-only prediction is insufficient when downstream classes are waveform-defined.
6. **Curvature κ is fixed** (not learned) — the paper's gains come from the matching geometry, not curvature tuning.
