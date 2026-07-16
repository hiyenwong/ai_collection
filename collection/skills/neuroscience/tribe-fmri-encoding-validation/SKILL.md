---
name: tribe-fmri-encoding-validation
description: "Validation methodology for deep multimodal brain-encoding models (TRIBE, the 2025 Algonauts challenge winner) against behavioral engagement metrics. Tests whether predicted fMRI signals forecast aggregate population behavior (YouTube replay heatmaps, neuroforecasting). Shows predicted neural drive fails to predict re-watch despite high encoding accuracy — null result with Bayes factor bounds and equivalence tests. Activation: brain encoding validation, TRIBE, neuroforecasting, predicted fMRI, fMRI engagement, brain encoding behavioral prediction, Algonauts challenge, fMRI replay heatmap, global field power fMRI, YouTube replay"
metadata:
  arxiv_id: "2607.01400"
  published: "2026-07-01"
  authors: "Barada Sahu, Shivesh Pandey"
  tags: [brain-encoding, TRIBE, neuroforecasting, fMRI, behavioral-prediction, validation]
---

# TRIBE fMRI Encoding Validation

Deep multimodal brain-encoding models (TRIBE: Llama-3.2 + V-JEPA2 + Wav2Vec-BERT) predict fMRI responses to naturalistic video with high accuracy. This methodology tests whether **predicted** neural signals inherit the behavioral predictive power of **measured** neural signals (neuroforecasting).

## Key Finding: Null Result with Strong Bounds

Running TRIBE on 48 YouTube videos, reduced predicted cortical response to per-second engagement curve (global field power). Correlated against "most replayed" heatmap:

- Pooled position-controlled partial correlation: **r = +0.058** (95% CI [-0.04, 0.15]; p = 0.23)
- Not significantly above loudness/motion baselines (loudness r = 0.12; paired p = 0.42)
- Bayes Factor: **BF₀₁ = 3.2** (moderate evidence for null)
- Equivalence test excludes effects above r = 0.14
- Split-half reliability of target: 0.82 (ceiling r = 0.90) — rules out noisy-label artifact
- Null holds across 6 cortical-network readouts + value/salience ROIs

## Methodology

### Global Field Power Reduction

1. Run TRIBE on each video → per-TR predicted fMRI response on fsaverage5 surface
2. Reduce to per-second engagement curve via Global Field Power (GFP) — spatial standard deviation across all predicted vertices
3. Align with YouTube "most replayed" heatmap (temporal position control)

### Readouts Tested

- Whole-cortex GFP
- 6 cortical-network readouts (visual, auditory, language, default mode, frontoparietal, salience)
- Value/salience ROIs
- Inter-Subject Correlation (ISC) — fitted own per-subject encoders on Algonauts fMRI (in-domain r = 0.15, cross-domain Friends-to-film r = 0.10)

### Controls

- **Temporal position control**: partial correlation controlling for temporal position in video
- **Low-level baselines**: audio loudness + visual motion features
- **Autocorrelation-preserving permutation test**
- **Per-input-stream dissociation**: ran probe on TRIBE's text/video/audio input streams separately — at most small borderline visual-stream signal (p = 0.004-0.06), none in audio/text/predicted-cortex

## Implications

1. **Predicted fMRI ≠ Measured fMRI for behavior prediction**: Accurate encoding models regress behaviorally-relevant structure toward group mean
2. **Genre-specific artifact**: Moderate correlations for music videos reflect onset-replay artifact, not content prediction
3. **Supervised probe illusion**: Leave-one-video-out probe appears to reach r = 0.47 but collapses to temporal-shape artifact under proper position control
4. **ISC unavailable from subject-averaged released model** — requires per-subject encoders

## Pitfalls

- **Moderate r for music videos is artifact**: Onset-replay pattern (intro music replayed) mimics content prediction. Always check genre stratification.
- **Supervised probes overfit temporal structure**: Leave-one-out cross-validation can leak temporal autocorrelation. Position control is essential.
- **ISC readout requires per-subject encoders**: The released TRIBE model is subject-averaged, making ISC computation impossible without retraining on Algonauts per-subject fMRI.
- **YouTube SABR streaming**: Standard download tools fail on YouTube's SABR-only streaming. Custom acquisition pipeline needed.
- **Domain saturation warning**: This paper already has `tribe-fmri-encoding-validation` skill. Check before creating variants.

## References

- d'Ascoli et al. (2025): TRIBE — winning model of 2025 Algonauts challenge
- Berns & Moore (2012): Neural signals predict cultural popularity
- Dmochowski et al. (2014): Neural reliability predicts engagement
- Code: https://github.com/mercurialsolo/tribe-replay-heatmaps
