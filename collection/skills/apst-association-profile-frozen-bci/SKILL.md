---
name: apst-association-profile-frozen-bci
description: "Use for cross-session BCI decoding with frozen weights. APST."
category: ai_collection
trigger_words: [cross-session intracortical decoding, frozen-weight BCI adaptation, association profile, FALCON benchmark, permutation-invariant set attention, few-shot calibration, unit drift, directional tuning profile, SVD-compressed profile, sliding-window causal transformer, FiLM conditioning, streaming neural decoding]
---

# APST: Association Profile-Conditioned Set-Temporal Transformer for Cross-Session Intracortical Motor Decoding (Frozen Weights)

**Source**: arXiv:2609.39080 — Zhang, Mo, Wen, Liang, Yang, Zeng, Wang, Wang (HKU + SUSTech, 30 Sep 2026)
**Code**: https://github.com/HsinyuanZhang/APST

## Core Problem

Intracortical BCI decoders degrade across recording sessions because electrode-tissue motion **changes the unit set**: units are lost, gained, and *drift* (a persisting unit can keep its firing statistics while changing its behavioral association — the Rokni et al. 2007 "unstable representations" problem). Existing fixes split into two camps, each with a flaw:

- **Gradient-based adaptation** (NDT2 fine-tuning, RNN-FT): needs backprop at deployment, risks overfitting a few calibration trials, and (on FALCON H1) costs 2.29× normalized latency.
- **Gradient-free, unsupervised adaptation** (SPINT, latent alignment): uses *unlabeled* activity — cannot resolve drift where firing statistics are preserved but the tuning changed.

**Key insight**: clinical BCIs already run periodic cued-movement calibration with a handful of labeled trials. Those labels are sufficient to estimate, **in closed form**, a compact per-unit "functional identity" that re-anchors the decoder — no gradient step needed.

## Method Architecture (three reusable patterns)

### Pattern 1 — Closed-form association profile (the 4-D interface)

Per unit u, from M labeled calibration trials (M as low as 4–8):

**Generic weighted ridge form** (Eq. 1):
```
a_raw[u] = argmin_v Σ_t ω[t]·(r[t,u] − φ[t]ᵀv)² + η‖v‖²
```
Behavior enters via design φ or weights ω. Two task-specific instantiations, both collapsed to the **same 4-D profile interface**:

1. **Directional tuning** (2-D cursor/finger tasks, FALCON M2 + DANDI688): first-harmonic cosine tuning (Georgopoulos 1982). φ = [1, cosθ, sinθ], uniform weights. Profile = [a, d, ρ=√(a²+d²), b] (cos/sin coefficients, modulation depth, baseline), z-scored by source-session moments (μ_dir, σ_dir).
2. **SVD-compressed association** (high-dim tasks, FALCON M1 16-ch EMG, H1 7-D velocity): behavior-weighted association matrix A[u,k] with softplus-split weights (K=16/14 states), normalized responses (Poisson-floor rate scale), then project onto **top-4 right singular vectors V₄ of pooled uncentered source associations** + source standardization. The source SVD basis is the cross-session bridge: target profiles live in the same 4-D space as source ones.

Cost: **< 15k operations** (< 0.1% of total calibration MACs). One calibration pass, zero target gradients.

### Pattern 2 — Profile-conditioned unit identity (FiLM at zero-init)

Calibration activity → trial-averaged signature h[u]; profile p[u] modulates it:
```
[γ,β] = W_o·ReLU(W_i·p + b_i) + b_o     (W_o, b_o ZERO-initialized — adaLNZero)
h̃[u] = (1+γ)⊙h[u] + β
e[u] = MLP([h̃[u]; p[u]])                  ← unit identity, computed once, cached
```
Zero-init means training starts from concatenation alone; the FiLM path is a pure residual add-on. **The cached identity costs nothing at streaming time.**

### Pattern 3 — Permutation-invariant set-temporal decoder

Two conditioning sites, dual use:
- **Site 1** (calibration): identity e[u] as above.
- **Site 2** (streaming token): live activity → 5-bin causal conv → add projected identity, concat profile → token z[u,t].

Unit tokens aggregate via **8 learned slot queries + masked multi-head set-attention** (Set Transformer / Perceiver style) — invariant to any unit count/order, padding mask handles variable N_s. Population token (256-D) feeds a **4-layer pre-LN causal transformer** with per-layer ALiBi-style relative-time bias and **sliding-window KV cache bounded by receptive field R = 5 + Σ(w_ℓ−1)** — streaming state is O(R), not O(session length). Inference-only EMA (α=1/3, resets at session boundary) smooths output. **Whole-unit dropout during source training** teaches the set encoder to survive unit loss.

## Headline Results

| Benchmark | APST (frozen) | Activity-only | RNN-FT (gradient) | SPINT (unlabeled) |
|---|---|---|---|---|
| DANDI688 Sub-C (held-out) | **0.78** | 0.40 | 0.77 (FT) | — |
| DANDI688 Sub-M (held-out) | **0.81** | 0.58 | 0.70 | — |
| FALCON M1 (private held-out) | 0.65 | 0.62 | 0.59 (NDT2) | 0.66 |
| FALCON M2 | **0.42** | 0.24 | 0.43 (NDT2) | 0.26 |
| FALCON H1 | **0.44** | 0.24 | 0.52 (NDT2) | 0.29 |

- **Sample efficiency**: 8 APST calibration trials beat 16-trial RNN fine-tuning on Sub-C (0.75 vs 0.74); on Sub-M APST leads by 0.11–0.38 at *every* budget 4–32.
- **Compute asymmetry**: APST calibration = 3.83–21.75M MACs vs RNN fine-tune = 383–1195 *billion* forward MACs (~5 orders of magnitude).
- **Held-in vs held-out gap (HI−HO)**: APST (0.12/0.22/0.16) — gains don't trade away within-session accuracy; smaller gaps than SPINT on M2/H1.
- **Drift robustness**: on the most distant session (Sub-C 12-01, 138 days post-source), APST retains 0.58 vs RNN-FT 0.48; on Sub-M sessions 8–11 days out, APST beats both baselines on all three.
- **Latency**: 0.09–0.15 normalized (real-time capable), vs 2.29 for NDT2 Multi on H1.

## Critical Ablations (why it works)

1. **Profile shuffle scores BELOW activity-only** (0.00/0.03 on Sub-C/Sub-M): profiles act as *unit-specific identities*, not session-level summaries — shuffling keeps the session profile set constant but destroys per-unit binding.
2. **Static identity table fails** (−0.32 to 0.38): units re-sorted per session can't be tracked by one frozen table — recalibration is genuinely needed.
3. **Token-only ≈ dual conditioning** (Δ ≤ 0.01); identity-only site drops H1 to 0.40 vs 0.48 — the streaming token conditioning carries most benefit; site-1 kept because it's free (cached).

## Reusable Patterns & Transfer Guide

1. **Closed-form identity estimation beats fine-tuning on few shots**: whenever a domain gives a few labeled probes + a stable low-dim basis (here: motor manifold SVD / cosine tuning), project per-sensor associations into it analytically instead of backprop-ing. Applicable to any drifting-sensor decoding (neuropixels across days, wearable IMU re-placement, EEG cap shifts).
2. **Two-level conditioning — cache the static part**: split conditioning into calibration-time (identity, cached forever) vs streaming-time (live token concat). Zero-init (adaLNZero/FiLM) makes the added path a safe residual.
3. **Permutation-invariance is the correct inductive bias for unit-set drift**: set-attention over unit tokens with slot queries handles any N; whole-unit dropout during source training is essential regularization.
4. **Shared low-dim interface across heterogeneous tasks**: directional tuning (cos/sin) and SVD-projection both land in the SAME 4-D space — one decoder conditioned on a unified "functional fingerprint" interface. Generalizes the idea: design per-task estimators, share the conditioning interface.
5. **Bounded streaming state**: sliding-window causal attention with per-layer KV cache + ALiBi bias keeps decoding O(R) — for clinical streaming decoders this matters as much as R².

## Limitations (stated honestly)

- Profile estimators and SVD bases are **still designed per task** (directional vs SVD variants); unified learned estimators are future work.
- Division of labor between the two conditioning sites not fully characterized.
- Uses target labels (unlike SPINT) — requires the clinical recalibration workflow to exist.
- FALCON M1: SPINT slightly ahead (0.66 vs 0.65) — unlabeled methods can win where tuning profiles are weak (EMG association).

## Key References

- FALCON benchmark: Karpowicz et al., NeurIPS 2024
- SPINT (main competitor): Le et al., NeurIPS 2025 — permutation-invariant unit embeddings from unlabeled activity
- NDT2 Multi: Ye et al., NeurIPS 2023 — labeled few-shot fine-tuning baseline
- Rokni et al., Neuron 2007 — unstable neural representations (the drift problem origin)
- Gallego et al., Nat Neurosci 2020 — motor manifold stability (DANDI688 source)
- Set Transformer: Lee et al., ICML 2019; Perceiver: Jaegle et al., ICML 2021
