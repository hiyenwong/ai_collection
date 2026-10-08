---
name: specbram-band-power-eeg-fm
description: Use when choosing EEG foundation-model pretext targets. Masked band-power prediction beats waveform reconstruction.
category: ai_collection
trigger: EEG pretraining objective, masked prediction target, band power pretext task, sleep staging foundation model, LaBraM CBraMod alternative, phase ancillarity
---

# SpecBraM: Masked Band-Power Prediction as EEG Foundation Model Target

**Source**: SpecBraM: What Should an EEG Foundation Model Predict? Masked Band-Power Prediction versus Waveform Reconstruction — Xie, Bie, Mao, Chen (HKUST), arXiv:2610.07484 (Oct 2026, cs.LG)

## Core Principle

**Predict the physical quantity that downstream readouts depend on, not a proxy of the signal.** For EEG, a large class of labels (AASM sleep stages, clinical "background slowing", quantitative-EEG band ratios) is defined by spectral energy — while the *phase* of a sub-second patch is ancillary (carries no state information and cannot be inferred from context). A waveform-reconstruction loss therefore spends gradient on an irreducible innovation term.

## Method (Minimal Delta over MAE-style EEG FMs)

- Input: 10-s windows @256 Hz, 19 channels (10–20 montage), per-recording robust normalization (median/IQR). Patches: 200 samples (0.78 s) → token grid C=19 × Tp=12.
- Backbone: 12-layer criss-cross transformer (D=512, 8 heads, 51.3M params), attention alternates channel/time axes; learned channel+time position embeddings. Independent per-patch masking p=0.3 with learned mask token.
- **Target change only**: instead of reconstructing raw samples or VQ codes, regress the **log spectral energy of each masked patch in 5 fixed bands**: y = log(1+P_b), where P_b = mean-square of 65-tap Hann-windowed cosine band-pass filter output (nominal centers 2/6/10/21/38 Hz; measured peaks 4.6/6/10/21/38). Standard-band per-patch FFT variant (0.5–4/4–8/8–13/13–30/30–45 Hz) also works, slightly below main target on HMC.
- Loss: MSE on masked patches' 5-band log energies + 0.05·SIGReg isotropy penalty on encoder outputs.
- **Target filters MUST be fixed, not learnable** — learnable target filters collapse to zero (loss → 4e-4, features uninformative). This is a general failure mode: any self-supervised target whose parameters co-adapt can be minimized degenerately.

## Theoretical Basis (stationary-Gaussian idealization)

- Periodogram sufficient for state θ; phases ancillary (Brillinger/Whittle). Band-averaged periodogram ≈ sufficient statistic + MLE of band levels under flat-in-band assumption (Prop 1–2).
- Var[log P_b] = ψ'(m_b) ≈ 1/m_b independent of state → log is variance-stabilizing, MSE is the right loss (Prop 3). Implemented log(1+P): variance ≈ m⁻¹s²/(1+s)², partially holds at high bands.
- Bayes-risk decomposition for ANY masked target (Prop 5): risk = posterior uncertainty about state (reducible) + patch's own innovation (irreducible). For band power the irreducible term is small; for waveform it scales with signal power and, by Parseval, is dominated by low frequencies under 1/f spectra.

## Key Results (matched backbone/data/steps, 2,388h TUEG, 3 seeds)

| Comparison | Result |
|---|---|
| Band power vs raw-waveform recon (strict linear probe) | +1.6–2.8 BA pts (ISRUC/HMC), all 12 seed×dataset pairs positive |
| With 1% labels | +4.7–7.3 pts; SpecBraM @1% (0.760/0.685) > ALL external FMs @100% (LaBraM 0.752/0.632, CBraMod 0.728/0.619) |
| Data efficiency | BP @epoch 4 > raw recon @epoch 16 (≈4× pretraining efficiency) |
| Tokenizer effect | Smaller than target effect; plain linear patch embedding ≥ learnable filterbank → use the simpler one |
| vs rich handcrafted spectral features | +2.0–2.8 pts all labels, only ~1 pt at 1% labels (self-supervision adds modest consistent gain) |
| Fine-tuned sleep staging | ISRUC 0.8107 / HMC 0.7669 — best published, above CSBrain 0.7925/0.7345 |
| Frozen features vs LaBraM/CBraMod/BIOT | Better on all 7 tasks under identical strict probe |

## Where the Benefit STOPS (honest negative results)

- **Motor imagery**: no advantage (µ/β ERD is spatially localized/lateralized; per-channel band energy over 0.78-s patches doesn't emphasize it).
- **Vigilance (SEED-VIG PERCLOS)**: raw recon better after fine-tuning; high-passing input at 4 Hz restores band power's lead (+5–7 corr pts) — low-frequency ocular artifacts (1–2 orders larger than cortical signal) dominate lowest target bands. Lesson: **spectral-energy target helps only when the energy it measures matches the label, including artifact exposure**.
- Depression screening (Mumtaz): tie.
- After full fine-tuning, gap to raw-recon narrows to ~1 pt — **the target matters most for frozen/low-label deployments**.

## Reusable Patterns

1. **Task-aligned pretext target design**: enumerate what downstream labels physically depend on (spectral energy? spatial pattern? transient shape?), then mask-predict exactly that quantity, discarding ancillary dimensions (phase).
2. **Fixed-target anti-collapse rule**: never co-learn the target extractor; degenerate shrinkage minimizes the loss without learning anything.
3. **Strict-probe evaluation**: frozen encoder + mean-pooled tokens + logistic regression (C on validation) — deterministic, cross-model fair; avoids downstream-head confounds.
4. **Label-efficiency curves** (1/5/10/25/50/100%) reveal target quality far better than full-label endpoints.
5. Concurrent works FAME (per-band standardized log power, corrects 1/f low-freq bias of ℓ2) and MANAS-2 (joint waveform+band-power) — per-band standardization is the natural next refinement.

## Connections

- MaskFeat (HOG targets, vision) / HuBERT-1 (MFCC clusters, speech) — same "predict fixed semantic feature, discard low-level detail" principle.
- Complements [[candle-null-space-eeg]] (learning-based ESI) and [[graph-matern-flow-matching-eeg]] (sensor-geometry priors): all argue for encoding EEG's physical structure into the objective rather than learning it from scratch.
