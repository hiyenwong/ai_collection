---
name: neural-disco-counterfactual-neural-editing
description: Use when counterfactual-editing neural population activity.
category: ai_collection
trigger: counterfactual editing of neural activity, spike editing with label preservation, disentangled residual latent, source-conditioned what-if neural generation, label-specific neuron attribution
---

# Neural-DISCO: Source-Conditioned Counterfactual Editing of Neural Population Activity

**Source**: arXiv:2610.33145 (NeurIPS 2026) — Policzer*, Ho*, Soo*, Tang (UBC Michael Smith Labs). Code: github.com/TangLab-UBC/Neural-DISCO-neurips

## Problem definition: source-conditioned counterfactual editing

Given a recorded source response x (binned spike counts from n neurons) and K observed behavioral/stimulus labels y = (y1..yK), replace ONE label ya → ŷa and generate neural activity for the edited condition while:

1. Preserving the other observed labels y−a
2. Preserving source-specific variability NOT explained by labels (internal state, spontaneous movement, unmeasured task variables)

This differs from plain label-conditioned generation p(x' | ŷa, y−a): without source conditioning the model marginalizes over internal state. The source-conditioned setting must retain residual content OF THIS SOURCE TRIAL. "Counterfactual" is operational (model-based edit), not causal identification from observational data.

## Architecture: supervised factorization with bottlenecked residual

- **Label embeddings**: za = φa(ya) — one MLP per label; can carry only information available through that observed label
- **Residual encoder**: u = φres(x) ∈ R^m — maps source spikes; carries idiosyncratic source content
- **Generator**: rates r = Gθ(z1..zK, ũ) via MLP + softplus; independent Poisson likelihood p(x|z) = Πℓ Poisson(xℓ | rℓ)
- **Training-time residual bottleneck**: corrupt residual with Gaussian noise ũ = u + ε, ε ~ N(0, σ²Im), ONE Monte-Carlo noise sample per example per minibatch (clean u at test time)
- **Loss**: L = (1/N)Σs Σℓ [rℓ(s) − xℓ(s) log rℓ(s)] + λ·(1/N)Σs ||u(s)||² (Poisson NLL, log x! constants dropped)

## Capacity bound (Prop 1): why the bottleneck blocks label leakage

I(S; Ũ) ≤ (m/2)·log(1 + P̂/(mσ²)) in nats, where P̂ = (1/N)Σs ||φres(x(s))||² is the empirical residual power.

This is the AWGN channel-capacity argument: Gaussian noise caps the residual channel. Since I(Ya; Ũ) ≤ I(S; Ũ) and I(Za; Ũ) ≤ I(Ya; Ũ), observed-label information cannot exceed the channel capacity → labels must route through their dedicated latents. Cautions:

- Bounds only the NOISY TRAINING channel S → Ũ, not the clean test-time channel S → U
- No disentanglement guarantee (identifiability needs paired pre/post-intervention observations or factorial priors)

## Editing + attribution procedures

1. Encode: za = φa(ya) for all a; u = φres(x)
2. Edit: replace ONLY za ← φa(ŷa); keep u and all other label latents fixed: ẑ = (z1..ẑa..zK, u)
3. Decode: r̂ = Gθ(ẑ); optionally sample x̂ℓ ~ Poisson(r̂ℓ)
4. Attribution: integrated gradients on generator pre-softplus outputs along a straight path from zeroed labels + zero residual to the source input; average SIGNED attributions over 32 random source samples, then mean absolute value over each label's input dimensions (or residual dims) → per-neuron label-specific attribution

λ selection criterion: maximize validation edit fidelity while minimizing observed-label decodability from the CLEAN residual, averaged over 10 validation folds.

## Verified experimental results

**RatInABox simulation** (100 place + 100 head-direction + 100 speed cells; position + HD observed, speed WITHHELD → must flow through residual):
- Position-shift and HD-reversal edits match simulator ground-truth target rates while preserving withheld speed-cell activity through the residual
- Cell-type recovery AUC (place/HD/speed from respective attributions) increases with λ; residual PCA organizes by held-out speed
- Unregularized ablation (λ=σ=0) fails: residual pathway carries label info, edits don't take effect

**Macaque reaching electrophysiology** (Neural Latents Benchmark, 137 units; joint edit of hand-position + hand-velocity + eye-position latents):
- CEBRA decoder trained ONLY on real spikes decodes counterfactuals at R² = 0.895 (hand pos), 0.772 (hand vel), 0.630 (eye pos) vs target-spike reference 0.909/0.845/0.656; source spikes decode poorly (negative control)
- Unregularized ablation stays source-like (negative target-decoding R²) — the leakage failure mode
- Synthetic constant-rate control neurons receive low attribution (sanity check)

**Allen Visual Coding Neuropixels** (32 sessions, drifting gratings):
- Speed edit to fold-mean: speed RMSE 3.63±0.57 cm/s vs Gaussian GLM 6.02±1.04; withheld temporal frequency preserved (bal-acc 0.541, above chance)
- Orientation edit (rotate 180°): target-orientation bal-acc 0.949±0.006 vs GLM 0.714±0.016; withheld source TF preserved 0.823±0.012 vs 0.532±0.015
- Attributions align with dataset metrics: running-modulation AUC (p<0.05 threshold) and orientation selectivity gOSI correlation both increase with λ
- **Reverse edit** (swap residual between two same-label sources): predicted per-neuron tuning variability recovers the withheld TF modulation → interface for probing unobserved brain-state modulation

**Baselines**: w/o reg (λ=σ=0), zero residual, pi-VAE, NEDS, Gaussian/Poisson GLMs. GLMs edit by replacing the source-label projection with target-label projection.

## Failure modes and trade-offs

- No bottleneck → label info hides in residual → edits ineffective
- Zero residual → source-specific variability lost (pure label-conditioned behavior)
- Weak residual channel harms reconstruction/preservation; overly strong channel leaks labels — the capacity bound characterizes but does not guarantee the sweet spot
- Correlated labels, missing variables, dataset shift break the assumptions
- Model is STATIC (no temporal/transition dynamics); validation in real data is indirect (decoder-based), cannot replace perturbation experiments
- Attribution scores = model sensitivity, NOT proof of causal or exclusive encoding by individual neurons

## Adaptation notes

- Extends LORD/biolord asymmetric-noise separation to Poisson spike counts, multiple labels, source-conditioned editing, and neuron-level attribution
- Interventions leaving unedited labels + source state fixed + true factorized Poisson generator + recovered maps ⇒ Poisson sampling after latent replacement = interventional distribution (strong assumptions)
- Applicable to any paired (neural activity, labels) dataset for in-silico what-if hypothesis generation before costly perturbation experiments
