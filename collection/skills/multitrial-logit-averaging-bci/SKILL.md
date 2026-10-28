---
name: multitrial-logit-averaging-bci
description: Multi-trial BCI aggregation via train-time logit averaging.
category: neuroscience
---

# Multi-Trial Aggregation for Non-Invasive Neural Decoding — Train-Time Logit Averaging

Source: "Logit Averaging During Training Sets a New State of the Art for Non-Invasive Speech BCI" (Özdogan, Elvers, Bronstein, Parker Jones — Oxford, arXiv:2610.26347, Oct 2026). First systematic comparison of multi-trial aggregation strategies for non-invasive neural decoding; a one-line change to the training objective sets a new SOTA on the 2025 PNPL phoneme benchmark (+17.4 balanced-accuracy points over the competition-winning Conformer).

Use when: decoding from low-SNR non-invasive recordings (MEG/EEG/fMRI) with repeated trials of the same stimulus, designing multi-trial BCI pipelines, or analyzing why joint/ensemble training succeeds or fails.

## The Six Aggregation Paradigms

A group G = {x₁,…,x_g} of g trials of the same stimulus passes through one shared backbone f_θ producing per-trial logits ℓᵢ = f_θ(xᵢ). The paradigms differ ONLY in where aggregation happens:

1. **Input averaging** (prior work, LibriBrain/PNPL): average raw signals first, x̄ = (1/g)Σxᵢ, ℓ̂ = f_θ(x̄). Train and test on averaged data.
2. **Post-hoc probability averaging** (prior work, d'Ascoli et al.): train per-trial with standard CE; at test time average bounded probabilities p̂ = (1/g)Σ softmax(ℓᵢ).
3. **Logit averaging during training** (proposed, WINNER): ℓ̂ = (1/g)Σ ℓᵢ, L = CE(ℓ̂, y). Gradients flow through the mean to every per-trial forward pass, so the backbone learns per-trial logits that are useful *after averaging*. Same aggregation at eval.
4. **Learned weighted averaging** (LWA): time-pool each trial's first-conv feature map to a token, MLP → per-trial score, softmax over trials → weights, weighted-sum the feature maps.
5. **Cross-trial attention** (CTA): multi-head self-attention over trial tokens so each trial's weight depends on all others.
6. **Learned query attention** (LQA): trainable queries attend over trial tokens; residual to the elementwise mean via gate h̄ = mean(hᵢ) + α·Attn, α = σ(β)·w_t with β init −3 (gate ≈0.05) and linear warmup over 10 epochs.

All are permutation-invariant by construction (positions 1–3 trivially; 4–6 by design).

## Key Results (balanced accuracy, 5 seeds)

| Condition | Input avg | Post-hoc | Logit avg (train) |
|---|---|---|---|
| LibriBrain Phoneme g=10 | .176 | .076 | **.241** |
| LibriBrain Phoneme g=100 | .565 | .113 | **.641** |
| LibriBrain Voicing g=10 | .780 | .508 | **.794** |
| LibriBrain Word top-10 g=10 | .544 | .400 | **.564** |
| MegNIST Digit g=10 (imagined) | .432 | **.526** | .418 |
| Armeni Phoneme g=10 | .213 | .079 | **.240** |
| Armeni Voicing g=10 | .790 | .524 | **.791** |

- vs 2025 PNPL Conformer winner (g=100): **0.641±0.051 vs 0.467±0.048** (p=0.022), F1 macro 0.605 vs 0.440 (+16.5 pts).
- Attention-based methods (4–6) never consistently beat logit averaging despite more capacity.
- **Task-structure dependence**: on imagined speech (MegNIST) the ranking INVERTS — post-hoc wins. Heard-speech trials are exchangeable noisy copies of one signal (uniform averaging captures everything); imagined-speech trials may not be.

## Mechanisms (numerically verified)

- **Gradient saturation escape**: per-trial CE gradient on the true-class logit is exactly |dL/dz_true| = 1−p_true, which vanishes as a trial becomes confident (0.4 at p=.6 vs 0.7 at p=.3 — "about half", confirmed 0.57). Under the logit-averaged loss a trial keeps receiving gradient until the GROUP-AVERAGED prediction is correct — even confident trials keep learning while weaker group members lag.
- **Logit-space differences accumulate**: a per-trial logit advantage d survives averaging and softmax(g·d) sharpens exponentially with group size (verified: P(true) = 0.574 → 0.953 → 1.000 for g = 1, 10, 100 at d=0.3). Probability space has no such accumulation.
- **Post-hoc minority-class collapse**: averaging i.i.d. bounded probabilities preserves their mean, so a class with lower per-trial probability than a frequent distractor can NEVER overtake it in expectation (verified). Empirically post-hoc macro-recall on low/mid-frequency phoneme tertiles = 0.000/0.008 at g=10 and 0.000/0.000 at g=100 — it predicts only the top-4 most frequent phonemes.
- **Logit statistics**: logit-averaged models develop per-trial logits with 5–11× larger max-mean margins and sharper softmax (max prob 0.91 vs 0.40 on MegNIST) — per-trial logits are deliberately "uncalibrated" but complementary.

## Joint-Ensemble Connection (theory)

Jeffares et al. 2023 claimed joint training of ensembles fails via "learner collusion" inflating the diversity term. Krogh–Vedelsby/Heskes decomposition: ERR_joint = ERR_ind − DIV with DIV = (1/M)Σⱼ KL(q̄‖pⱼ), q̄ = ensemble prediction.

**Verified insight**: this identity is EXACT when q̄ = softmax(mean logits) — the logarithmic opinion pool, i.e. precisely logit averaging (max |LHS−RHS| = 6.7e-16 over 200 random trials) — and FAILS for arithmetic mean of probabilities (error 0.44). The decomposition is logit-averaging-specific.

Re-reading: ERR_ind = ERR_joint + DIV means the per-member objective *penalizes* diversity at fixed joint loss. There is no free lunch on the training set (opposing movements that keep the joint loss fixed must raise individual losses), so "collusion" cannot inflate train diversity for free. Logit averaging succeeds here, and its train-time diversity generalizes to held-out data — so the ensemble failure is more plausibly about deep-ensemble inductive biases/loss landscapes than the joint objective itself.

## Practical Recipe

```
# training step, group of g trials sharing label y
logits = model(torch.stack([x1, ..., xg]))     # (g, K)
loss = CE(logits.mean(dim=0), y)               # class-weighted: w_c ∝ 1/sqrt(freq_c)
```
- Train and evaluate with the SAME aggregation (mean logits → argmax).
- Match group size between training and deployment when possible; post-hoc averaging needs no training-time grouping but collapses on rare classes.
- Tune LR per (dataset, paradigm, g) — logit averaging used 7e-5…1e-3 grid; early stop on validation balanced accuracy.
- Expect poor single-trial calibration (ECE up to 0.9) — fine, because group-level ECE is BETTER than post-hoc (0.036 vs 0.124 on phonemes) and confidence rankings stay informative (top vs bottom decile: 0.43 vs 0.13). Do not ship single-trial probabilities from a logit-averaged model.
- Limitations: MEG-only evidence; cross-entropy-only (contrastive losses untested); imagined speech may favor post-hoc.

## Related
- [[brain-to-text-unified-decoding]], [[simpleb2t-timing-shortcut-brain-to-text]] — B2T decoding pipelines that should adopt this default.
- [[deep-portfolio-optimization-framework]]-style joint-training analyses — the ERR_ind = ERR_joint + DIV reading applies wherever members are averaged at the logit level.
