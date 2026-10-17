---
name: eeg-speech-decoding-detection-floor-audit
description: "Audit scalp-EEG speech decoding claims via detection floors."
tags: [eeg, imagined-speech, detection-floor, effect-injection, myogenic-artifact, bci, evaluation-methodology]
---

# EEG Speech Decoding Detection Floor Audit

**Source**: Adeika & Osuagwu, "How large an effect would we have seen? Positive controls, detection floors and dataset pitfalls in scalp-EEG speech decoding" (arXiv:2610.20942, 14 Oct 2026, eess.SP/q-bio.NC/q-bio.QM). Code: github.com/blessadeik/scalp-eeg-speech-decoding

## Activation

Use when: (a) evaluating or reviewing imagined/covert/overt speech decoding from scalp EEG; (b) a null EEG decoding result needs a sensitivity bound, not just "accuracy at chance"; (c) a positive control (overt speech) is used to validate an imagined-speech pipeline; (d) decoding accuracy may come from muscle (EMG) rather than cortex; (e) using ds003626 ("Thinking out loud"), KaraOne, or 2020 BCI Competition Track 3.

## Core Findings

1. **Positive controls are myogenic, not cortical.** On ds003626, two lip electrodes decode overt speech at **0.7430** vs **0.4231** for the full 128-channel scalp montage; eight external EXG channels reach 0.7068; even the earlobe reference pair reaches 0.4769. No decodable signal survived in mu/beta (8-30 Hz). On KaraOne and the competition corpus, within-subject accuracy rose monotonically with frequency into the muscle-dominated range (>30 Hz) — the spectral signature of EMG contamination.

2. **Detection floors differ sharply by decoder.** Band-power logistic regression detects an injected 8-30 Hz desynchronization of **0.54 µV** (10% of ongoing rhythm, criterion fixed in advance); EEGNet (F1=16,D=4) detects **nothing within subject up to 4.31 µV** (~8× the band-power floor). Architecture explains it: EEGNet's ELU+average-pooling nearly removes amplitude modulations of a zero-mean oscillation before classification; ShallowConvNet's square→mean-pool→log IS an explicit band-power estimator and detects at 2.16 µV.

3. **Decoder blindness is effect-type-specific.** Amplitude and covariance (Riemannian) decoders were **blind to phase locking and cross-frequency coupling on every corpus at every injected size**; phase features (wPLI, theta-beta PAC) detect 5-10% lagged mixing/modulation but only because they were built for those effects. A null must name the decoder AND the effect type it bounds.

4. **ds003626 is easily misread** (three silent traps):
   - Condition codes are **reversed from intuition**: 0=pronounced, 1=inner, 2=visualized (verified by acquisition code, block structure 40/80/80, EMG flags, 9× EXG power elevation in condition 0). Inner speech = 2,236 trials, not 1,128.
   - Class encoding changed between releases (v1.0.0 codes 1-4; v2.1.2 codes 0-3) — a pipeline written for the old release silently keeps 75% of trials.
   - **Condition is collinear with time**: pronounced/inner/visualized occupy fixed within-session positions; a single trial-index threshold separates conditions at accuracy 1.0000. The only control is geometric (last w trials of one block vs first w of next).

5. **KaraOne annotation trap**: the first "speaking" segment in the alternating annotation is actually the **pre-imagery interval** (prompt perception + articulator positioning, no speech); in 3 of 14 participants the alternation is offset, mislabeling 138 segments with the wrong prompt.

6. **Reference leakage via channel subsets**: KaraOne stores 68 channels typed as EEG including 6 non-cortical (mastoids, EOG, ECG, EMG) under a 68-channel average reference. Any subset still carries each excluded channel at −1/68 amplitude. Imagery-vs-rest over all 68 channels: **0.9802, with the EMG channel alone accounting for 98.3% of above-chance accuracy**. Fix: re-reference any subset to its own mean.

## Methodology: Effect Injection for Detection Floors

To bound what a pipeline could have detected:

1. **Inject class-dependent effects into REAL recordings** (not simulations): suppress the participant's own ongoing 8-30 Hz rhythm by multiplicative depth k (inherits real phase statistics and spatial covariance). One k unit = 5.392 µV peak desynchronization sustained 1.5 s on ds003626.
2. Randomize topography per participant (rotation/tilt), per-class positional offset, amplitude/latency jitter — so the class→topography mapping differs between people as a real effect would.
3. Sweep k (e.g. 0→0.8); pre-specify detection criterion BEFORE the sweep (e.g. mean accuracy ≥ per-participant binomial threshold, ≥8/10 participants individually significant, group Wilcoxon p<0.05, all seeds must pass).
4. Extend across **effect types**: amplitude (ERS/ERD), evoked deflection, phase locking, cross-frequency coupling. Each decoder family has a floor per effect type — report the grid.
5. Grid criterion (more sensitive): cell detected when participant accuracies exceed the same cell at k=0 under one-sided paired Wilcoxon, mean gain >1pp, Benjamini-Hochberg corrected across all cells (240 here).

## Methodology: Split Integrity by Assertion

- Every trial carries a provenance identifier (corpus, participant, session, trial index, condition, prompt). One module builds all splits.
- Assertions before first optimizer step: no identifier in >1 of train/val/test; test participant absent from training under LOSO; no test class absent from training; no single-class test set.
- SHA-256 hash of sorted identifiers per fold → any split-machinery change is detectable.
- Seven verification checks for suspiciously high results: shuffle-label control (labels permuted within participant, 200 draws), fresh split seeds, replication on second corpus, physiological plausibility of filters, artifact-channel decoding, ablation graceful degradation, expected condition/protocol ordering.
- Append-only run records (code version, data checksum, seed, split hashes, config). Fix thread count — it alone changed accuracy by ~0.0018 via floating-point reduction order.
- **Per-trial band-limiting**: for short concatenated epochs, brick-wall FFT masking within each trial instead of IIR filtering (a 1 Hz high-pass has ~3.3 s impulse response > trial length → cross-fold mixing).

## Reporting Checklist (paper's recommendations)

1. Report accuracy in mu/beta bands alone
2. Report accuracy from peripheral/artifact channels alone; record EMG where possible
3. Report how accuracy changes with frequency — monotonic rise above 30 Hz = contamination until proven otherwise
4. Re-reference any channel subset to its own mean when the original reference included non-cortical channels
5. State a measured detection floor for each decoder × effect type supporting a null
6. Check label semantics and acquisition order against dataset SOURCE CODE; check segment annotations against published trial structure

## Key Pitfalls

- **"LOSO > within-subject accuracy" is not always leakage**: with identical injected effect and asserted splits, the reversal reflects only the 11× training-data difference (2,012 vs 179 rows) — parameter-heavy models order by parameters-per-training-row.
- Overt-speech positive control succeeding is structurally self-confirming: it's expected to decode well, so nobody looks further — yet it validates exactly the articulator-dependent pathway that locked-in users lack.
- Phase effects locked to jittered internal events (~1.9 cycles at 0.10 s jitter for 8-30 Hz) are unreadable at fixed latency; fixed-latency phase features are exploratory only.
- Common average reference manufactures zero-lag phase agreement — use lagged measures (wPLI, imaginary coherency); phase-locking value is the negative control (0.75 vs 0.05 on pure zero-lag source).

## Related Skills

- [[eeg-decoding-scaling-laws]] — data scaling for EEG decoding
- [[brain-to-language-decoding-survey]] — BCI decoding trajectory taxonomy
- [[simpleb2t-timing-shortcut-brain-to-text]] — timing leakage in word-aligned decoding
- [[same-brain-different-prediction]] — decoding reliability methodology
