---
name: connectome-reconstruction-robustness-audit
description: Robustness audit for connectome-constrained circuit models.
category: ai_collection
arxiv_id: "2610.29205"
trigger: connectome-constrained model trained on single reconstruction, connectome individuality claims, circuit model transfer across connectomes
---

# Connectome Reconstruction Robustness Audit

Source: Ashraf Yad & Nazifa Tabassum Nabila, "Reconstruction differences rival individual differences in the fly compass connectome and break trained circuit models", arXiv:2610.29205 (cs.NE, 21 Oct 2026). Preregistered: Zenodo 10.5281/zenodo.23382486.

## Thesis

Connectome-constrained models are built from ONE animal through ONE pipeline, and nobody tests whether the model depends on that reconstruction. Using nine versions of the Drosophila head-direction circuit (4 flies: male CNS v1.0, hemibrain v1.2.1, FlyWire FAFB v783, BANC v888; plus 5 same-fly variants differing only in synapse detector, proofreading release, or filtering), this paper shows: (1) a single pipeline step change within one fly moves wiring 78-83% as far as the smallest between-fly difference; (2) models trained on any wiring form knife-edge ring attractors that break under 1% weight changes; (3) trained models transfer to NO other connectome — including other reconstructions of the SAME fly. Real flies tolerate wiring distances (0.11-0.21) that kill the models (fail at 0.022).

## When to use

- You trained a circuit model on a connectome (fly compass, C. elegans, zebrafish, any synapse-resolution wiring) and want to know if conclusions survive reconstruction choice
- You are comparing two connectomes and want to attribute differences to individuality vs measurement
- You are reviewing/auditing a connectome-constrained model's claims

## Core methodology

### 1. Same-fly variant ladder (separate measurement from biology)
Build variants of ONE animal's circuit where exactly one pipeline step changes:
- Filtering pipeline (Codex vs neuPrint; threshold changes)
- Proofreading release (early vs final, e.g. BANC v626 vs v888)
- Synapse detector (Princeton/Yu et al. vs Buhmann et al. on the same FAFB fly)
Extraction rules held fixed: cell types EPG/PEG/PEN/Delta7/ER[1-6], >=3 synapses per pair, no self-connections, signs assigned by cell type (Delta7/ER inhibitory). Circuits: 409-434 neurons, 15,440-28,942 connections.

### 2. Wiring-map distance (one scale for all differences)
For each direction-tuned pathway p (EPG, PEN_a, PEN_b, PEG, Delta7): build m^p = normalized 8-bin (45 deg) histogram of angular offset from presynaptic to postsynaptic neuron's inferred compass position. Distance:

    d(a,b) = sum_p w_p * 0.5 * ||m_a^p - m_b^p||_1

with w_p = pathway's fraction of total synapses. Total-variation form, so noise floors are interpretable.
Calibrated values (compass circuit):
- Filter change within fly: 0.022-0.038; random removal of 10% of connections: 0.032 (SD 0.003) = noise floor
- Synapse-detector change within one fly: 0.084-0.090 = 78-83% of the SMALLEST between-fly distance
- Between-fly: 0.108-0.212
- Proofreading (BANC v626 vs v888): 0.104 = near the smallest between-fly distance
- Bilateral asymmetry (L vs R of same fly): 0.060 vs 0.068 random halves (male CNS), 0.100 vs 0.111 (BANC) — NO detectable left-right asymmetry at this resolution

### 3. Wiring-only compass position inference
EPG positions from classical multidimensional scaling of cosine-similarity of concatenated in/out connectivity; all other neurons placed at synapse-weighted circular mean of their EPG partners. Validate against anatomical labels: circular agreement 0.99-1.00 (vs 0.24-0.55 shuffled). Cross-fly 1:1 neuron maps by rank-matching after rotation+mirror alignment chosen by direction-tuned synapse correlation (never by task performance); 91-99% of source neurons mapped.

### 4. Knife-edge detection
Train rate networks (per-neuron or per-cell-type gains) to hold a cued heading. Trained models: 0.3-1.6 deg error, slowest Jacobian multiplier 0.998-1.014 (near-continuous attractor), round ring in top-2 PCs (radius variation 0.17). Then perturb:
- Uniform +/-1% rescale of ALL weights: error 10.3-27.9 deg (+/-2%: 20.5-50.9 deg)
- Diagnosis: continuous attractors need slowest multiplier == 1; any uniform weight change moves it off 1 (Seung 1996 fine-tuning problem). Check the multiplier, not just task error.
- Shuffled-wiring controls ALSO hold heading (on distorted loops, radius variation 0.50-0.54, multipliers 0.900-0.997) and are equally fragile — approximate attractor shape alone does not confer robustness.

### 5. Transplant test (zero-shot transfer)
Evaluate a network on every other wiring through the 1:1 neuron maps, no retraining. Result: ALL transplants at chance (median 82-92 deg, chance 90 deg; 101/108 > 80 deg registered failure level). Failure does NOT correlate with distance for clean networks (nothing left to predict at chance level). Controls: self-map reproduces own-wiring success; maps validated on labeled flies; networks fail on SAME-fly variant (no cross-fly alignment involved); best global gain rescale improves only 87 -> 83 deg.

### 6. Cell-type gain refit (~30 numbers)
Refit one gain offset per target cell type (about 30 parameters), keep everything else fixed:
- Same-fly FILTERING variants: 45 -> 8 deg (92% of transplants < 30 deg) — repaired
- Detector change: -> 61 deg (33%); different fly: -> 57 deg (21%) — NOT repaired
- Post-refit error correlates with wiring distance (rho=+0.67, p=0.001): a detector change in one fly is as bad as a fly change at the same distance. Transfer depends on distance, not on the difference's source.

### 7. Noise training (precision-robustness tradeoff)
Train with weight-scale jitter / synaptic / dropout / activity noise (levels 0.25/0.5/1.0):
- Own-wiring error rises 0.6 -> 7.9 / 11.7 / 21.4 deg (rho=+0.83)
- Fragility (error after 0.95 global rescale) falls 67 -> 46 / 25 / 22 deg (rho=-0.86)
- Transplant error: 79 -> 53 deg at noise 0.5 — partial; hard pairs (different pipelines) stay at 87-90 deg
Rule: robustness must be TRAINED IN; clean-trained optimizers land on knife-edge solutions.

### 8. Reality check against recordings
E-PG calcium imaging (DANDI 000289, 15 flies): bump-heading offset MSD grows smoothly (diffusion-like), never breaks. At 40 s lag: 40.4 rad^2 darkness, 18.1 low-contrast cue, 5.2 bright cue. Diffusion floor 0.047 rad^2/s (dark) vs 0.023 (bright); short-timescale excess drift NOT established (difference CI includes 0). Real compasses function despite wiring differences far larger than what breaks trained models — whatever provides this robustness (developmental noise, plasticity, other-circuit feedback) is absent from clean-trained networks.

## Modeler checklist (from the paper)
1. Report full reconstruction provenance: dataset, version, synapse table, connection threshold, proofreading release.
2. Treat a model trained on one connectome as a separate entity until reproduced on another; tune parameters per-connectome, do not transplant.
3. Always run two trivial robustness checks before interpreting a model: (a) error after +/-1% uniform weight rescale; (b) error on a second reconstruction of the same circuit (ideally same animal).
4. Use same-fly variant distances as the measurement floor BEFORE attributing between-connectome differences to individuality. Filter-level floor is small (0.022-0.038); detector/proofreading floors are NOT.
5. Report the slowest Jacobian multiplier of the trained map — proximity to 1 flags knife-edge continuous attractors.
6. Static fits (each connectome independently mapped to an ideal attractor, cf. Biswas et al. 2024) and transplant tests answer DIFFERENT questions; a handful of cell-type rescalings fitting each connectome does not mean one connectome's trained parameters work on another.

## Pitfalls

- Degeneracy: many parameter configs produce the target dynamics on ONE wiring; the one training lands on need not be near any good config on another wiring.
- Between-fly distances are upper bounds (maps add residual error); only one fly pair shares a pipeline family, so between-fly distance mixes biology + pipeline.
- Mapping procedure artifacts: ruled out here by self-map control + same-fly-variant failures, but must be re-ruled-out per-circuit.
- Noise sweep / refit analyses were exploratory (unregistered); registered hypotheses were about transplant ratio and attractor criteria.
