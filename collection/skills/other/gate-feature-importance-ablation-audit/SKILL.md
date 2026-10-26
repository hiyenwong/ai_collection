---
description: Use when reading learned gates/attention as importance.
name: gate-feature-importance-ablation-audit
category: ai_collection
version: 1.0
author: neuro-cron-2026-10-26
license: MIT
metadata:
  hermes:
    tags: [sbi, feature-importance, ablation, interpretability, eeg, neural-posterior-estimation, cautionary-tale, attention-not-explanation, jansen-rit]
    related_skills: [llm-rater-multiplicity-audit, correspondence-score-audit-alignment, minimal-pair-latent-reasoning-probing, eeg-sae-interpretability]
---

# Gate-Based Feature Importance in SBI: A Cautionary Tale

Methodology from arXiv:2610.30364 — "Gate-Based Feature Importance in Simulation-Based Inference for EEG: A Cautionary Tale" (Deshmukh, Brenner, Knösche, Scherf; MPI CBS Leipzig + UMN; NeurIPS 2026 workshop, q-bio.NC, 21 Oct 2026).

## One-Line Summary

A feature gate trained end-to-end with a neural posterior estimator is **plausible but not faithful**: across 9 seeds its importance ranking was **negatively correlated** with gold-standard retrain-based ablation (Spearman ρ = −0.607 sigmoid, −0.556 softmax, both p = 0.0039 = unanimous sign-flip floor), while costing negligible accuracy (R² 0.791→0.792/0.761) and staying calibrated. Never report learned gate/attention weights as feature importance without validating against causal retrain ablation.

## When to Use / Activation

- Reading learned gates, input masks, attention scores, or variable-selection layers as "feature importance" in SBI / EEG / scientific ML pipelines.
- Designing an interpretability validation for a scientific ML model before publishing importance claims.
- Reviewing a paper that reads jointly-trained weights as mechanistic evidence.
- Deciding whether a cheap importance proxy can replace leave-one-feature-out retraining.

## The Audit Protocol (reusable)

1. **Ground truth = retrain-based ablation.** For each feature, retrain the FULL pipeline from scratch with that feature excluded (same seed, same training set). Importance = drop in mean R² (or held-out likelihood) vs the same-seed full model. This is causal by construction; post-hoc masking is not.
2. **Compare rankings, not values.** Spearman ρ between proxy and ablation rankings, computed per seed. Test the seed-averaged ρ with an **exact sign-flip permutation test** over all 2^k sign assignments of k per-seed statistics (k=9 → 512 assignments, min attainable p = 2/512 ≈ 0.0039; report "all seeds agreed", not tiny p).
3. **Separate magnitude from weight.** Report both |z|·α (magnitude-weighted proxy) and raw gate weight α alone — if the mismatch weakens with raw weights, feature magnitude was partly driving it (here: −0.607 → −0.298, still negative).
4. **Robustness sweeps.** (a) Recompute ρ excluding any single feature; (b) jointly exclude the top-scoring feature of each method; (c) check the proxy's internal consistency across its own variants (here sigmoid vs softmax ρ = 0.643 — internally consistent, still wrong).
5. **Rule out "the model is just bad".** Show the gated model matches baseline accuracy (R² 0.791/0.792/0.761 across ungated/sigmoid/softmax), credible-interval coverage at nominal 50/90/95%, and stable per-parameter performance ranking. The readout fails *despite* a healthy model — that is the dangerous case.

## Reference Setup (Jansen–Rit EEG NPE, for reproducibility)

- Model: 6-state Jansen–Rit neural mass, 1 kHz Euler; infer 4 params (connectivity C, input drive μ, joint E/I time-constant scale κ, inhibitory gain g), log-uniform priors, E/I gain degeneracy excluded by construction (fixed ratio 2:1).
- Forward: MNE fsaverage 3-layer BEM, visual-cortex source, 5 electrodes chosen by |lead field|, projected with **signed** values, pink 1/f noise, SNR ~ U[5,25] dB per trial.
- Features: 7 per channel (skewness, kurtosis, spectral slope, total power, dominant frequency, Hjorth mobility, Hjorth complexity), z-scored; gate MLP 7→32→7 pooled across channels, tiled back multiplicatively; jointly trained, **no auxiliary sparsity loss, no gradient blocking**.
- Inference: single-round NPE (sbi package), neural spline flow (5 transforms, 125 hidden); 9 seeds; 250 held-out sims; 1,000 posterior samples; R² + coverage.

## Headline Numbers

- Ablation: total signal power dominates, ΔR² = 0.210 (SD 0.009) ≈ 5× the next feature (kurtosis 0.042, skewness 0.041, Hjorth complexity 0.041, mobility 0.031, dominant freq 0.012; spectral slope n.s.).
- Gates: rank total power 7/7 (sigmoid) and 6/7 (softmax); favor Hjorth mobility + dominant frequency, whose ablation effects are ~10× smaller.
- Mismatch survives: any-single-feature exclusion, joint top-3 exclusion, raw-weight variant, both activations.

## Why It Happens / How to Frame It

- A jointly trained selector only needs the *products* z_i·α_i to be informative; it can down-weight a feature while another pathway (or a different feature carrying the same information) compensates. Predictive optimization does not force weights to equal marginal causal effects.
- Jacovi–Goldberg framing: the gate is **plausible** (stable across seeds/variants) but not **faithful** (contradicts ablation). Plausibility is not evidence.
- Same family as: attention-not-explanation (Jain & Wallace), TabNet masks vs KernelSHAP on UCI Adult, EEG saliency failing model-randomization checks. This paper extends the pattern to simulation-based inference.

## Action Rules

- Treat learned weights as a *hypothesis generator*, never as the importance estimate.
- Before reporting: run the retrain-ablation benchmark on a subset (it costs one retraining per feature — budget it).
- Gates remain useful as differentiable feature selectors — validate their **selections** (top-k features) against ablation, not their continuous weights.
- With few seeds, use the exact sign-flip test rather than t-tests; report the p-value floor honestly.

## Limitations

- Simulated EEG only (clean ground truth by design); real-data ablation must score against a proxy (held-out likelihood), which weakens the benchmark.
- What the gate tracks instead of ablation is not established; NPE-specific (amortized, single-round); 7 features is small — rankings in higher dimensions may behave differently.

## References

- arXiv:2610.30364; code: github.com/Shrivatsa-Deshmukh/sbi-gate-vs-ablation
- Jacovi & Goldberg 2020 (plausibility vs faithfulness); Jain & Wallace 2019 (attention is not explanation); Gonçalves et al. 2020 (NPE for neuroscience).