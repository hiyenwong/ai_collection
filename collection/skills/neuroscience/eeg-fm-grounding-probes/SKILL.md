---
name: eeg-fm-grounding-probes
description: Use when auditing EEG-FM spatial or spectral grounding.
trigger: EEG foundation model audit, spatial grounding, spectral grounding, perturbation probe, electrode identity, IAAFT surrogate, clinical morphology, LaBraM BIOT CBraMod CSBrain REVE evaluation
version: 1.0
author: neuro-cron 2026-10-23
license: MIT
category: ai_collection
metadata:
  hermes:
    tags: [eeg-foundation-model, interpretability, perturbation-probe, evaluation, grounding]
    related_skills: [braincodes-lightweight-eeg-fm, eeg-fm-audit-systematic-evaluation, matched-input-eeg-fm-audit]
---

# EEG Foundation-Model Grounding Probes

Source: Avramidis, Tashev, Emmanouilidou, "Probing Spatial and Spectral Grounding in EEG Foundation Models" (arXiv:2610.29367, USC + Microsoft Research, Oct 2026).

## When to Use
- Evaluating an EEG foundation model beyond downstream accuracy — testing whether representations encode physiologically meaningful structure
- Auditing spatial (electrode identity, topographic locality) or spectral (phase structure, oscillations, clinical morphology) grounding
- Comparing EEG-FM architectures (BIOT, LaBraM, CBraMod, CSBrain, REVE) on WHAT they encode vs what their predictions rely on

## The Three-Dissociation Framework

Downstream accuracy cannot tell WHAT an EEG foundation model (EEG-FM) uses. Split evaluation into three independent questions:

1. **Access** — can the architecture even see the property (electrode coords input? magnitude-only input?)
2. **Encoded** — does the frozen representation change when the property is perturbed (latent displacement)
3. **Relied-upon** — does a downstream prediction change when ONLY that property is perturbed at test time

Empirical law: **encoding ≠ reliance**. LaBraM: permuting positional codes displaced embeddings by 80.5% yet dropped motor-imagery accuracy by only 1.2 points. Conversely REVE: smallest identity displacement but the clearest decision-level effects.

## Spatial Probes (SPA1–SPA3)

**SPA1 — identity sensitivity.** Derange positional labels π→π′ with waveforms fixed; measure relative displacement S_id = ‖f_π′(X) − f_π(X)‖₂ / ‖f_π(X)‖₂. S_id=0 means the representation ignores assigned channel positions. Variants: S_ord (permute channel input order — only affects order-consuming models like CBraMod), S_sig (permute waveforms across channels keeping IDs — breaks signal-to-location correspondence). 10 derangements per intervention; fit 64-component PCA on clean embeddings and apply unchanged to perturbed ones to control dimensionality.

**SPA2 — topographic locality.** Perturb channel i with white noise at 10 dB SNR (relative to that sample's channel power). Influence on output channel j: d_ij = ‖f_j(X+ε_i) − f_j(X)‖_F / ‖f_j(X)‖_F. Summarize: (a) fraction of displacement off the perturbed channel Σ_{j≠i}d_ij / Σ_j d_ij, (b) Spearman ρ between off-channel d_ij and inter-electrode distance. Apply after EVERY transformer block — locality is depth-dependent (LaBraM peaks at intermediate layers, ρ=−0.811; REVE ρ=−0.829; BIOT flat; CSBrain/CBraMod no distance structure).

**SPA3 — decision reliance.** Fit a linear head on clean features (subject-disjoint 5-fold CV); at TEST time permute only the positional input (REVE coords, LaBraM electrode indices, BIOT slot tokens, CSBrain region labels) with waveforms unchanged and the readout frozen. Report BOTH latent displacement ‖δf‖/‖f‖ AND Δ balanced-accuracy.

## Spectral Probes (SPE1–SPE3)

**SPE1 — structure beyond power.** Generate IAAFT surrogates (preserve each channel's amplitude distribution + approx power spectrum; randomize phase with the SAME phase sequence across channels to keep inter-channel phase stats). Train a linear head to distinguish original vs surrogate embeddings. ALWAYS benchmark against a phase-free spectral-power baseline (log-PSD features on the same task) — models with magnitude-spectrum pathways (CSBrain, CBraMod) score at/below this control; only REVE and LaBraM beat it.

**SPE2 — narrowband oscillation sensitivity.** Inject into 1 of 4 canonical bands (δ 1–4, θ 4–8, α 8–13, β 13–30 Hz) an independent carrier per channel (white noise → 4th-order Butterworth at band edges). Injection power measured RELATIVE to the recording's own power in that band, sweep −20…+5 dB. Train a 4-way linear head on the UNIT-NORMALIZED latent displacement (band identity must not leak from displacement magnitude). REVE/LaBraM identify bands at much lower injection levels; magnitude-pathway models collapse on weak θ/α injections but recover at β.

**SPE3 — clinical morphology specificity.** Train a linear seizure classifier on clean data; at test time inject into held-out NON-seizure segments (0 dB) one of: (a) ictal chirp 10→3 Hz with growing amplitude, (b) spike-wave at 3 Hz — Gaussian-derivative spike with extrema 70 ms apart, followed 100 ms later by a 100 ms Gaussian slow wave, (c) power-matched pink noise control. Inject into a contiguous 20–40% channel subset (seed electrode + nearest neighbors). **Specificity = mean ΔP(seizure) for the two epileptiform patterns − ΔP(seizure) for the noise control.** Only REVE exceeded its log-PSD control (+0.158); LaBraM responded to noise as strongly as to epileptiform (specificity −0.022): spectral sensitivity ≠ clinical selectivity.

## Verified Dissociation Profiles (5 public EEG-FMs)

| Model | Spatial mechanism | Key dissociation |
|---|---|---|
| BIOT (3.2M) | learned slot tokens | largest S_id (0.687 MI) yet no decision reliance (readout near chance) |
| LaBraM (5.8M) | electrode-name indices | heavy latent displacement (0.805), MI accuracy −1.2 pts only; strong surrogate/band decoding, NO morphology specificity |
| CBraMod (4.0M) | channel order only (conv) | insensitive to both spatial & spectral conditioning |
| CSBrain (8.9M) | anatomical region grouping | relies on region code for MI decisions (+0.104 Δ) without topographic locality |
| REVE (69M) | continuous 3D coords in attention | smallest S_id (0.272) but clearest positional + morphological decision grounding; only model above spectral baseline on SPE3 |

Off-channel displacement fraction converges to 0.720–0.868 for ALL models — representations become broadly mixed; mixing alone says nothing about spatial grounding.

## Design Lessons

- Slot tokens / name indices can ENCODE identity strongly while downstream heads ignore it — never infer reliance from embedding sensitivity.
- Continuous 3D coordinates consumed by attention yield the best decision-level spatial grounding.
- Magnitude-spectrum input pathways produce power-dominated representations (fail SPE1/SPE2) — include phase/temporal structure.
- Evaluation protocols must test whether downstream DECISIONS are sensitive to the perturbed structure, not just whether the representation is discriminable.

## Limitations
Linear readouts on frozen encoders capture only linearly accessible structure; small Siena cohort (14 participants); may not reflect fully fine-tuned models.

## Reference
- arXiv:2610.29367 — probes applied to PhysioNet-MI (64ch motor imagery) + Siena Scalp (29ch seizure); encoders frozen, PCA-controlled, subject-disjoint splits.
- Related: IAAFT surrogate method (Schreiber & Schmitz 1996); multichannel surrogates (Prichard & Theiler 1994); aperiodic spectral bias of reconstruction EEG-FMs (Kommineni et al., arXiv:2605.26434).
- Companion architecture paper: BrainCodes (arXiv:2610.29320) — designed to pass these probes; see skill [[braincodes-lightweight-eeg-fm]].