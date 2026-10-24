---
name: meg-mamba-ssm-foundation
description: Use for Mamba state-space MEG foundation models and tokenised neural generation.
category: ai_collection
tags: [neuroscience, meg, state-space-models, mamba, foundation-models, autoregressive, tokenizer, lora, generative-model]
arxiv_id: 2610.00746
paper_title: MEG-Mamba: A Scalable State-Space Foundation Model for Magnetoencephalography
paper_url: https://arxiv.org/abs/2610.00746
authors: Chetan Gohil, SungJun Cho, Oiwi Parker Jones, Mark Woolrich
published: 2026-09-30
code: https://github.com/OHBA-analysis/MEG-Mamba
---

# MEG-Mamba: State-Space Foundation Model for MEG

Generative foundation model for source-reconstructed, parcellated MEG built on Mamba-3, replacing the transformer backbone of MEG-GPT. Order-of-magnitude efficiency gain: **22 vs 400 GPU-hours** pre-training and **4 s vs 0.32 s** context on the same corpus.

## Architecture

```
continuous MEG (per-parcel, 250 Hz, z-scored)
  → causal learnable tokenizer (V=92 tokens, near-lossless detokenisation 97.8% var)
  → embeddings: token(256d) + parcel(256d) + session(256d)  [summed]
  → 4× Mamba-3 blocks (width 256, state 64, expansion 2, MIMO rank 4, SwiGLU FFN, RMSNorm pre-norm)
  → linear head → softmax over 92 tokens (next-token prediction, per-parcel independent)
```

- **Tokenizer**: causal variant of Cho et al. sample-level tokenizer — token at time t depends only on current+past signal (no future leakage). Trained on Schaefer-100-parcellated Cam-CAN (63.7 h pooled rest/passive/sensorimotor).
- **Parcel embedding**: learned lookup, one 256-d vector per ROI — PCA of these recovers cortical spatial organisation (frontal/central/parietal/temporal/occipital clusters) with **no spatial supervision**.
- **Session embedding**: MLP (292-d unigram+bigram features → 200-d PCA → 2×128 hidden → 256) computed directly from the recording — gives **zero-shot inference on new sessions** without training; PCA of session embeddings encodes participant age.

## Training

- **Objective**: autoregressive next-token cross-entropy, first W=50 samples excluded (warm-up), context T=1000 (4 s).
- **Data**: Cam-CAN eyes-closed rest, 559 train / 62 held-out sessions, ≈87 h, 7.8M single-parcel sequences per epoch; one parcel at a time.
- **Config**: AdamW (β=(0.9,0.95), wd 0.01), lr 1e-4 (2k-step linear warm-up, constant), batch 512, bfloat16, 3 epochs, 1× A100 80GB, seed 42. Parameters: **3.4M**.
- Result: held-out CE 1.80 nats/token, top-1 accuracy 31.5% (~29× chance 1/92), negligible generalisation gap.

## Stimulus Conditioning (frozen-backbone steering)

Add a 4th embedding: multi-hot boxcar stimulus vector u_t ∈ {0,1}³ over visual/auditory/motor events (1 s from onset, co-occurring events sum additively). h_t ← h_t + u_t·W_stim. Then **LoRA rank 16, α=32** injected into input+output projections of each Mamba-3 block; zero-initialised adapters (identity at start). Only stimulus embedding + LoRA trained: **≈167k params (5% of model)**, 10 epochs on passive+sensorimotor of 530 pre-training subjects, lr 1e-3 cosine, 4.4 h on 1× L4. All else frozen.

Generates realistic task-evoked time-frequency responses (Morlet wavelets 6–30 Hz) for subjects unseen in BOTH pre-training and fine-tuning (8.5k auditory / 8.5k visual / 5.2k button-press trials).

## Evaluation Protocol (generative fidelity)

Compare real vs generated on held-out subjects — prompt with first 4 s, generate 30 s autoregressively (temperature 1, full distribution):
1. **Power spectral density** per parcel (Welch) + band-power Pearson correlation across 100 parcels → r ≥ 0.93 all canonical bands.
2. **Relative power maps** per band — spatial distribution reproduced.
3. **Wavelet time-frequency** — transient non-stationary dynamics reproduced.

## Key Insights

1. **SSM beats transformer for neural signals**: 18× cheaper training, 12.5× longer context, higher generative fidelity than MEG-GPT. Fixed-size recurrent state → constant per-step generation cost (vs growing KV cache) — enables real-time inference.
2. **Parcellation is the key preprocessing**: source reconstruction (unit-noise-gain-invariant LCMV beamformer, rank 60, reg 0.05) + Schaefer-100 PCA-per-parcel makes signals spatially interpretable and comparable across subjects/scanners — MEG's advantage over EEG.
3. **Small models suffice at current corpus scale**: 3.4M params / 87 h data; scaling laws unmeasured.
4. **Interpretable latent state link**: Mamba selective recurrence carries explicit latent state — analogous to HMM state segmentation of fast neural dynamics (e.g. HMM-based transient network identification); interpreting SSM state evolution in those terms is open future work.
5. **Foundation-model recipe for small-domain data**: next-token AR objective + learnable tokenizer + conditioning embeddings + frozen-backbone LoRA steering — portable to EEG, ECoG, fMRI (cf. NeuroMamba), spike trains.

## Related Work Context

- MEG-GPT (transformer predecessor, 400 GPU-h, 0.32 s context); EEG foundation models (BIOT, La BraBrraint, EEGformer lineage); BrainRVQ (EEG AR/MR, 9.2k subjects); CaMBRAIN (EEG BCI Mamba — classifier, not generative); NeuroMamba (fMRI autoregressive); benchmarked SSM spike forecasting.
- Classical MEG state-space lineage: HMMs for transient network states — MEG-Mamba's latent state bridges sequence models with interpretable dynamics.

## Reusable Patterns

- **Session-embedding from token statistics** (unigram/bigram histograms → MLP): zero-shot conditioning for new recordings, no per-session training — general recipe for multi-session physiological corpora.
- **Boxcar stimulus embedding + zero-init LoRA**: cheap task steering of a frozen generative neural model — data augmentation, in-silico experimentation, generative prior for decoding.
- **Per-parcel independent modelling + parcel embeddings**: sidesteps N-parcel joint sequence problem; parcel embedding re-learns spatial structure implicitly.
- **Generative-fidelity evaluation** (spectra + spatial maps + TFR) as foundation-model benchmark, complementary to downstream tasks.

## Pitfalls

- Single-site corpus (Cam-CAN), eyes-closed rest only; no cross-site generalisation tested.
- Summary-statistic fidelity, not formal distributional metrics; single baseline comparison (MEG-GPT only).
- V=92 vocabulary fixed by tokenizer; retokenisation needed for other parcellations/sampling rates.
- Model is per-parcel: no cross-parcel coupling in the backbone itself — spatial correlations live in embeddings/sampling, not the generative dynamics.

## Related Skills

- [[cambrain-realtime-continuous-eeg]] — causal Mamba for EEG inference (BCI task)
- [[jet-eeg-flow-matching]] — generative EEG via flow matching
- [[atoms-of-thought-eeg-microstates]] — microstate tokenisation for EEG representation
- [[neuromorphic-pseudo-random-number-generators]] — small-model efficiency theme
