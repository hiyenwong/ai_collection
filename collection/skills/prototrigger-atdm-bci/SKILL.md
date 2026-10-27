---
name: prototrigger-atdm-bci
description: "Use for ATDM BCI: prototype-based EEG evidence encoding."
category: ai_collection
trigger_words: [adaptive temporal decision-making, ATDM, dynamic window BCI, early stopping EEG, prototype learning BCI, evidence accumulation BCI, variable-length EEG encoding, ITR optimization, dueling DQN stop policy, human-in-the-loop BCI]
---

# ProtoTrigger: Prototype-Based EEG State Encoding for Adaptive Temporal Decision-Making BCIs

**Source**: arXiv:2609.22088 — Cao, Zhao, Jiang, Leong, Ren, Do, Chang, Lin (Australian AI Institute, UTS, Chin-Teng Lin group)

## Core Problem

Fixed-window (FW) BCI decoding wastes observation time on easy trials and produces unreliable predictions on hard ones. Adaptive temporal decision-making (ATDM) lets an RL policy decide *when to stop* accumulating EEG evidence, but requires an encoder whose state representation stays **temporally comparable across variable observation lengths** — a property conventional CNN/Transformer EEG encoders (EEGNet, Conformer, TCNet) do not guarantee (cross-length drift). Prior ATDM encoders (CCA/correlation-template for SSVEP, CSP for MI) are paradigm-specific.

## Method (two-stage prototype encoder)

### 1. Local Feature Extraction (LFE) — stability
Maps variable-length observation X ∈ R^(C×L) to a sequence of local embeddings via three stacked **prototype-matching** stages (temporal → spatial → refinement):

- Prototype-matching operator: Ψ(v, p) = α·exp(-γ·(1 - v·pᵀ/(‖v‖‖p‖ + ε))) + β (cosine-similarity kernel with learnable sharpness γ, scale α, bias β)
- Temporal matching: per-channel 1D patches (length L_TP) vs F₁=16 temporal prototypes → BN
- Spatial matching: channel-wise patches vs 2 spatial prototypes → BN+ELU+MaxPool(factor D=4)
- Refinement: temporal patches over response maps vs refinement prototypes (L_RP=31) → PConv fusion → AvgPool → E ∈ R^(L_em×F₃), F₃=32
- Similarity-to-shared-prototypes = **common reference space** → temporally comparable states across lengths

### 2. Global Evidence Aggregation (GEA) — decision timing
- Linear projection of E to anchor space; **L_pa=24 learnable evidence anchors**
- Anchor-response matrix Ω normalized across anchors
- Shared MLP **PTES** (prototype temporal evidence scorer) maps each ω_l to a scalar → softmax over positions = temporal attention α (NOT self-attention: each local embedding scored against shared anchors, not pairwise)
- Fuse: S = E + φ_re(α ⊙ Z); temporal mean → fixed-dim state s_t

### 3. Cross-length supervised pretraining
Encoder + MLP head trained with CE loss **summed over ALL decision steps t=0..M** on progressively extended observations (T₀ + tΔT, ΔT=0.25s, max 4s). This anchors representations at every length the policy will visit.

### 4. RL stopping policy (dueling DQN)
- MDP state sequence s = {s₀..s_M}; actions {0=extend, 1=stop & predict}
- Reward: r_t = (1−a_t)·r_E + a_t·r_S; r_E=−0.03 (time penalty), r_correct=+0.6, r_wrong=−0.4; γ=0.99
- Q(s,a) = V(s) + A(s,a) − mean_a A(s,a); greedy stop at argmax or max length
- Encoder frozen after pretraining; DQN is a 3-layer MLP (256/128/64)

## Key Results

| Dataset | ProtoTrigger ITR | Best baseline | Metric
|---|---|---|---|
| SSVEP | **163.06 bits/min** (DT 0.97s) | FBCCA 152.55 | ITR |
| MI | **25.32 bits/min**, ACC 69.13% | CSP 22.13 | ITR |
| RFH-VEP (hybrid rotation-freq VEP) | **134.24 bits/min**, ACC 73.49%, DT 0.99s | Conformer 119.30 | ITR |

- Ablation (C-P/C-T/P-T/P-N/C-N vs P-P): prototype LFE→accuracy; prototype GEA→early stopping (DT); removing GEA hurts everywhere (p<0.05)
- Online HITL AR-SSVEP (HoloLens 2 + LiveAmp 64, 10 subjects, zero calibration): PTATDM 90.33% ACC @ 1.80s DT → ITR 67.51 vs 40.47 (3s FWPT, same ACC) and 45.45 (1.5s FWPT, ACC 70.33%). Lower NASA-TLX workload than FW. Total inference latency 2.132 ms << 0.25s decision interval (RTX 4070).
- Reward-grid sensitivity: ITR stable 129.56–135.99 across 5×5×5 reward grid → conclusions robust to reward tuning.

## State-Quality Evaluation Metrics (reusable for any RL-state encoder)

- **CCD** (class-center drift): mean ‖μ_{k,t+1} − μ_{k,t}‖ across adjacent lengths → cross-length consistency
- **PFR** (prediction flip rate): frequency of prediction changes between adjacent lengths → temporal decision stability
- **CM** (classification margin): mean top1−top2 logit gap → state discriminability
Good ATDM states: low CCD, low PFR, high CM. ProtoTrigger: best CM everywhere, competitive CCD/PFR (TCNet wins CCD/PFR but collapses on CM).

## Implementation Notes

- Preprocessing: Butterworth 2–70 Hz bandpass + channel-wise z-score; initial window 0.5s (SSVEP/VEP) or 1.0s (MI); extend 0.25s steps to 4s
- 5-fold CV: 3 train / 1 val(+DQN) / 1 test; sliding-window augmentation only during training
- AdamW 500 epochs (encoder, lr 1e-4), then DQN 300 epochs (lr 2e-4), batch 64
- Prototype counts: F1=16 temporal, F2=2 spatial; spatial prototype length = #channels (8/17/22)

## Reusable Patterns

1. **Shared-reference encoding for variable-length streams**: replace self-attention with similarity-to-learnable-anchors when downstream policy needs cross-length comparable states
2. **All-steps supervised pretraining**: supervise the encoder at every truncation length the policy will encounter, not just full length
3. **Evidence-anchored attention**: shared anchors score temporal segments for informativeness — applicable to any progressive-observation early-stopping system (medical triage, streaming classification)
4. **CCD/PFR/CM triplet** for diagnosing why an RL state encoder fails under variable-length input
5. ITR = (60/T)·[log₂N + P log₂P + (1−P)log₂((1−P)/(N−1))] as the joint accuracy-time objective

## Limitations (from authors)
Online validation only on small AR-SSVEP; encoder and DQN trained separately (joint optimization open); DQN is standard, no uncertainty-aware policy.

## Related Local Skills
- eeg-brain-connectivity-bci, saliency-aware-eeg-decoding, meta-learning-in-context-brain-decoding, va-net-eeg-motor-decoding
