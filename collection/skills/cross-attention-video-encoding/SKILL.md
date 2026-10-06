---
name: cross-attention-video-encoding
description: "Video fMRI encoding via joint spatiotemporal attention."
metadata:
  arxiv_id: "2609.36366"
  published: "2026-09-28"
  authors: "Iishaan Inabathini, Margaret M. Henderson (Carnegie Mellon University)"
  source: "arXiv q-bio.NC"
  tags: [computational-neuroscience, fmri-encoding-model, cross-attention, V-JEPA-2, naturalistic-video, visual-cortex, NeuroAI, interpretability, dynamic-vision]
---

# Cross-Attention Video Encoding Models: Joint Spatiotemporal Routing in Higher Visual Cortex

**arXiv 2609.36366** (2026-09-28) — Inabathini & Henderson (CMU). Per-parcel cross-attention encoding model for video-evoked fMRI: a learned query per cortical parcel attends jointly over space AND time on the token grid of a frozen self-supervised video backbone (V-JEPA-2), replacing fixed/linear readouts. Joint 3D routing beats factorized and spatial-only attention in lateral/face/body and parietal cortex, and the attention maps double as interpretable, stimulus-specific spatiotemporal receptive fields that track moving objects. Data: BOLD Moments Dataset (10 subjects, 1102 3-s clips).

**Activation keywords**: fMRI encoding model, video encoding, cross-attention, V-JEPA-2, spatiotemporal routing, parcel query, BOLD Moments Dataset, visual cortex, attention map, category-selective regions, dorsal stream, NeuroAI, brain alignment, representational similarity

## Architecture (one screen)

Frozen backbone: V-JEPA-2 ViT-g/16, **layer 32 of 40** (best in ridge sweep over layers), D=1408. Each 3-s clip → token grid X ∈ R^{T×H×W×D}, T=16, H=W=24, N=9216 tokens, channels z-scored over training clips. All learning lives in the readout.

1. **Per-parcel query**: each Schaefer-1000 parcel r (423–433 queries/subject incl. unlabeled voxels) has a learned query q_r ∈ R^D, stimulus-independent — it encodes a stable preference; the attention map shows where/when each clip meets it.
2. **Keys carry position, values carry content**: `k_n = W_k·LN(x_n) + α·PE(t_n,h_n,w_n)` (α=1, fixed sinusoidal 3D PE split into t/h/w blocks), `v_n = W_v·x_n`. PE in keys-not-values lets a query prefer locations AND moments while attended features stay content-only.
3. **Single softmax over all N tokens** (one attention head): `a_rn = exp(q_r·k_n/√D) / Σ_m exp(q_r·k_m/√D)` → attention map a_r(t,h,w). This is the only difference from factorized models — a parcel can attend to *different locations at different moments*.
4. **Attended feature → shared MLP**: `z_r = Σ_n a_rn·v_n`; `h_r = W_o·z_r`; `h_r ← h_r + FFN(LN(h_r))` (2-layer MLP, GELU, hidden 4D). W_k, W_v, W_o, FFN **shared across parcels** — parcels differ only in query + voxel readout.
5. **Per-voxel linear readout** from h_r, trained jointly with attention by AdamW + early stopping. All voxels of a parcel share one attention map but weight features differently.
6. Fitting: per-subject, MSE over all voxels, ensemble of 10 members (900/100 train/val splits), member predictions averaged voxel-by-voxel before evaluation. Report signed r² per voxel on 102 test clips; region means over voxels with noise ceiling ≥5%.

## Routing-as-ablation family (the reusable experimental design)

All constrained models differ from joint ONLY in attention weights; temporal/spatial factors each uniform | fixed | routed (routed = softmax of parcel query against keys computed from tokens averaged over the other axis):

| Model | T-factor | S-factor | All-voxel r² | What it tests |
|---|---|---|---|---|
| Ridge (mean-pooled 1408-d) | — | — | .174 | linear baseline |
| Mean pool | uniform | uniform | .180 | no routing |
| Temporal | routed | uniform | .180 | time selection alone = zero gain |
| Spatial | uniform | routed | .187 | space selection alone |
| Factorized | routed | routed | .186 | separable a(t)·a(h,w), can't follow motion |
| **Joint 3D** | single softmax over (t,h,w) | | **.191** | coupled routing |
| Noise ceiling | | | .34 | |

## Key results (numbers to cite)

1. **Joint > everything, every subject** (10/10): joint−spatial t(9)=5.85, p_FDR<.001. Of the 0.010 joint gain over mean-pool, 0.006 is recovered by spatial routing alone; **temporal routing alone adds nothing** (0.180 = mean-pool), and stacking temporal on spatial (factorized) does not exceed spatial (0.186). ⇒ the joint gain is specifically *coupled* routing — different locations at different moments.
2. **Stimulus dependence is the driver**: a *fixed* learned spatial distribution per parcel (static RF) does not exceed mean-pooling (0.181). The benefit is not "learned receptive fields", it's input-dependent selection.
3. **Region dissociation** (region-mean r², noise-ceiling ≥5% voxels):
   - Lateral/face/body (MT, EBA, FFA, OFA, LOC, STS): joint **.263 = 66% of noise ceiling** (.40); exceeds factorized/spatial/mean-pool/ridge in every subject (joint−factorized t(9)=6.60).
   - Parietal: joint advantage over all others.
   - Early visual: spatial = factorized = joint (.189) — spatial selection accounts for the whole gain; no benefit from following content over time.
   - Scene (PPA/RSC/TOS): no model significantly exceeds ridge — global layout may be captured by clip-averaged features.
   ⇒ Dynamic spatiotemporal tracking is a **lateral + parietal** demand (motion/social-action regions), not a general cortical mechanism.
4. **Backbone generality + failure modes**: joint > factorized in lateral regions also with late layers of VideoMAE v2, DINOv2, CLIP (t(9)=2.88/2.49/3.47, FDR over 192 tests). BUT with early-layer features joint is *worse* than spatial-only, and for CLIP's last stage ridge wins everywhere except early visual ⇒ the routing benefit requires sufficiently abstract features; always sweep backbone layers.
5. **Interpretability for free**: joint attention of an EBA parcel follows a fencer's body → arm/sword through the swing; STS parcel tracks a panda's head/body while climbing. Factorized maps concentrate on a few frames but spread over background (its single spatial map must serve both wide shot and close-up).
6. **Attention maps recover category selectivity without localizers**: IoU of each parcel's top-1% attended tokens with SAM-3 segmentation masks, z-scored across parcels: FFA/OFA/EBA attend faces/bodies/animals > average parcel; PPA/RSC show the reverse. Localizer contrasts computed from attention alone overlap fROIs above chance: face 0.19 (chance 0.09), body 0.14 (0.02), scene 0.28 (0.10), all p_FDR<.05.

## Reusable patterns

- **Routing-as-ablation**: express attention as factorizable T×S distributions with each factor ∈ {uniform, fixed, routed}; all models share backbone/readout/training. General recipe for isolating *which* flexible-routing component earns its keep — portable to any token-grid modality (MEG/EEG, audio, neural time series).
- **Keys-not-values PE**: positional/temporal encodings enter only keys → queries can be location/time-preferring while values stay pure content. Prevents position leakage into readout features.
- **Shared projections + per-region queries**: one W_k/W_v/W_o/FFN across parcels; regions differ only in a D-dim query + voxel linear head. Cheap (thousands of queries, one attention module) and keeps maps comparable across regions.
- **Attention maps as validated interpretability**: quantify maps against segmentation (SAM) category masks instead of eyeballing; report chance-level overlap.
- **Noise-ceiling-normalized reporting** (e.g., "66% of ceiling") for cross-model comparison.
- **Ensemble-averaged per-voxel predictions** with early stopping on held-out clips.

## Honest boundaries

- 3-s clips only (BMD); longer-movie temporal integration untested. fMRI TR 1.75 s is slow — MEG/EEG extensions needed for temporal claims.
- Scene-selective cortex and early-layer features show no joint-routing benefit; CLIP last stage flips to ridge. Region- and layer-specific conclusions, not universal.
- Attention ≈ normalization hypothesis (scaled dot-product attention approximating divisive normalization) is suggested, not tested — compare against Reynolds-Heeger/Carandini-Heeger models before claiming cortical mechanism.
- Predictive gain over spatial-only is real but small (+0.004 all-voxels; concentrated in lateral/parietal).

## Replication pointers

Data: BOLD Moments Dataset (Lahner et al. 2024) — 1102 clips, GLMsingle betas, per-voxel noise ceilings released. Parcels: Schaefer 1000/7-networks resampled to voxel grid; 23 functional ROIs (retinotopic Wang-2015, HCP parietal, video-based category localizers). Backbone: V-JEPA-2 ViT-g/16 layer 32. Baseline: voxelwise ridge on time×space-mean-pooled 1408-d features. Stats: two-sided paired t-tests across 10 subjects, FDR-corrected.
