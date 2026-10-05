---
name: auditory-pathway-eeg-foundation-model
description: Audio-to-EEG foundation model for auditory neuroscience.
category: neuroscience
metadata:
  arxiv_id: "2609.20595"
  published: "2026-09-24"
  authors: "Thomas J Stoll, Ross K Maddox (University of Michigan, Kresge Hearing Research Institute)"
  tags: [auditory, eeg, foundation-model, wavenet, abr, trf, binaural-interaction, stft-loss]
---

# Auditory Pathway EEG Foundation Model (Audio→EEG)

**Paper:** A Deep Neural Network for Predicting Continuous Human EEG Across the Auditory Pathway in Response to Sound
**arXiv:** 2609.20595v2 (eess.AS) — 24 Sep 2026
**Authors:** Thomas J Stoll, Ross K Maddox

## Problem Statement

Computational auditory models each target ONE stage/response type (cochlea models, ABR models, cortical TRF models), so findings cannot be synthesized across paradigms and timescales. Existing EEG foundation models extract features FROM EEG; none PREDICT EEG from sound. Goal: a single causal model mapping binaural acoustic waveforms → continuous high-sample-rate EEG, validated against established auditory phenomena at subcortical (ms) AND cortical (100s of ms) timescales.

## Key Innovation

**First audio-to-EEG foundation model** trained on ~250 hours of heterogeneous EEG (92 subjects, 2–64+ channel montages, tonebursts/speech/music) that generalizes across three paradigms it was not specifically tuned for: parallel ABRs, speech TRFs (subcortical + cortical), and the click-evoked binaural interaction component (ABR-BIC). Model–grand-average correlations fall within (sometimes above) the subject-level human distribution.

## Architecture (end-to-end causal)

```
stereo audio (40 kHz)
  → 24-band/ear causal filterbank (100 Hz–16 kHz), log-compression: log(|X|+1)
  → avg-pool downsample 40→5 kHz
  → 9-layer causal WaveNet encoder (kernel 8, dilation 2^d, d=0..8, gated activations, residual)
  → 4-layer 1×1-conv bottleneck → 16 latent neural components
  → montage-specific spatial weights → predicted EEG (5 kHz)
  [conditioned on subject ID + demographic/audiometric metadata]
```

### Critical design elements

1. **Causality everywhere (neural path)** — enables streaming/hearing-aid deployment. Only the artifact path uses symmetric padding (accounts for acoustic-tubing delay).
2. **Parallel linear artifact path** — models stimulus-locked EM artifact (4 ms conv over raw audio + subject/recording-specific spatial projection). Summed with neural prediction during training; disabled at evaluation. Required because high-sample-rate EEG recordings are artifact-contaminated.
3. **Montage-specific spatial readout** — single shared latent (16 components) projected to ANY electrode montage → handles heterogeneous channel counts.
4. **Subject dropout (p=0.1)** — prevents over-reliance on subject embeddings; produces a "default subject" enabling zero-shot population-level predictions.

## Training Recipe (the load-bearing details)

- **STFT-domain loss, NOT MSE.** MSE on raw EEG fails (low-frequency content dominates). Instead: compute prediction error y−ŷ FIRST, then its STFT, then
  `L = (1/F) Σ_f 10·log10(ε + (1/T) Σ_τ |S(f,τ)|²)`, F=251 bins, ε=1e-6.
  Error-before-STFT means **phase (timing) errors are penalized**, not just amplitude. The log emphasizes high frequencies where subcortical (brainstem) information lives.
- 1-minute training segments; Adam lr=1e-4, batch 4; AMP + gradient-norm clipping (max 1.0).
- 10% held-out test; select epoch with lowest test loss.

## Evaluation Protocol (transferable pattern)

**"Is the model a plausible subject?"** Compare model prediction vs human grand averages using Pearson r, then percentile-rank within the leave-one-out subject-level human correlation distribution and run Crawford–Howell tests on Fisher-z-transformed r. This is a much stronger standard than "correlation looks high": the model must be statistically indistinguishable from a typical human subject.

Validated phenomena:
- **pABR**: frequency-dependent wave V amplitude/latency, rate dependence (20–120 stim/s), serial-vs-parallel presentation differences (serial never in training → generalization). r ≥ 0.961 on rate–amplitude curves at every frequency except 8 kHz.
- **Speech TRFs**: subcortical (30–2000 Hz bandpass + glottal-pulse-regressor frequency-domain deconvolution) and cortical (1–15 Hz + envelope ridge regression, λ=10 by CV, lags −200..500 ms). Reproduces larger subcortical TRFs for low-F0 speech.
- **ABR-BIC**: (L+R)−B on clicks (clicks/monaural/periodic never in training). Predicted latency 6.40 ms within published range 5.58–6.90 ms; amplitude 0.439 µV above published 0.13–0.36 µV but n.s. under Crawford–Howell.

Honest negatives: serial-presentation responses overestimated; TRFs slightly small — authors attribute to overestimated neural adaptation/efferent activation.

## Implementation Guidance

- Use this pattern for ANY stimulus→neural-response regression (visual, somatosensory, ecog): causal filterbank front-end + dilated-conv encoder + low-dim latent + montage-specific readout + STFT loss + artifact side-path.
- For foundation-model EEG work: heterogeneous montages are a feature, not a bug — force the model to learn shared latents.
- For in-silico experimentation: freeze weights, use default subject, run novel paradigms through the model before collecting data.

## Pitfalls

- **MSE loss on EEG = failure.** Always use log-STFT error loss with error computed pre-transform (phase matters).
- Artifact path is mandatory for high-rate (≥10 kHz) EEG; without it, the model learns artifact.
- Crawford–Howell (not simple t-tests) for single-case comparisons against a sample.
- STFT loss needs ε stabilizer; log of near-zero bins explodes otherwise.

## Applications

1. In-silico pilot experiments: test paradigms/analysis methods on predicted responses before costly data collection.
2. Streaming hearing-aid optimization: causal model evaluates DSP settings via predicted neural responses.
3. Automated feature extraction front-end for clinical auditory assessment (threshold estimation via pABR, binaural-integration diagnostics via BIC).

## Related Skills

- `earable-eeg-auditory-platform` (in-ear EEG hardware), `brain-to-language-decoding` (reverse direction, EEG→text), `eeg-fm-audit-systematic-evaluation` (EEG foundation model auditing).
