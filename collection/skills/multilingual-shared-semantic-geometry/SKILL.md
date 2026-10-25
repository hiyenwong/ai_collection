---
name: multilingual-shared-semantic-geometry
description: Multilingual decoding; shared cortical semantic geometry.
category: neuroscience
---

# Shared Cortical Semantic Geometry Across Languages (SemDecoder)

Source: "Multilingual Brain Decoding Reveals Shared Cortical Semantic Geometry" (Guo, Hu, Ng, Wang — SIAT CAS / HKU / HKBU, arXiv:2610.26927, Oct 2026). fMRI from **227 participants** across Chinese, English and French. Core finding: cortical semantic representations exhibit consistent geometry (similarity relationships) across languages and individuals; this cross-language consistency **increases from sensorimotor toward higher-order association cortex**, forming a shared-semantic-geometry gradient tightly aligned with the principal cortical functional gradient (Spearman ρ = 0.80, spin-test P < 0.001; G2 ρ=0.15 P=0.54, G3 null — the alignment is specific to G1).

Use when: building multilingual or cross-subject brain decoding, analyzing representational geometry across conditions/groups, testing geometry–behavior/gradient correspondences, or designing LM-proposes/neural-selects text generation.

## SemDecoder Architecture (reusable pipeline)

1. **Subject-specific alignment into a shared space**: X̃ᵤ,ᵢ = (Xᵤ,ᵢWᵤ + bᵤ) ⊙ (1 + γᵤ) + βᵤ — per-subject linear projection (Wᵤ ∈ ℝ^{c×p}) plus feature-wise scaling/shifting (γᵤ, βᵤ learnable per subject). Each subject gets a private pathway into one shared multilingual space; everything downstream is shared. Inputs: stimulus-aligned responses at Lₙ = 7 haemodynamic delays, p = 256.
2. **Shared neural feature extractor**: pretrained by **masked neural modelling** — withhold neural tokens, predict from remaining spatiotemporal context, no semantic supervision (SMN4Lang trunk). Captures spatiotemporal structure before any decoding objective.
3. **Attention pooling over delays** + projection head → d-dim space of BLOOM-1.1B **layer-20** sentence representations (align brain embeddings to an intermediate LM layer, not token space).
4. **Training loss**: L = L_NCE + L_CS — symmetric InfoNCE (s_ij = cos(ŷᵢ, yⱼ)/τ, learnable temperature τ, both directions averaged) plus cosine loss (1 − cos(yᵢ, ŷᵢ)), equal weights; mini-batch negatives.
5. **Generation — LM proposes, brain selects**: beam search where BLOOM-1.1B proposes the M = 96 most probable next tokens (conditioned on preceding 15 tokens); candidate continuations are embedded (layer-20, standardized with training-story stats) and scored by accumulated cosine similarity to the decoded neural vector ŷ; keep k = 12 beams; detokenize with the LM's tokenizer. The LM constrains fluency; neural data alone decides content.

Evaluation: WER, BLEU-1, METEOR, BGEScore vs a no-brain-data "Random" control; beats Tang et al. 2023 (semantic reconstruction) on every metric and dataset; decoded content temporally aligned with the narrative (time-similarity matrices diagonal).

## Geometry Analysis Methodology

- Sentence-level responses via **LSS GLMs** (one GLM per target sentence: target regressor + all-other-sentences regressor + DCT drift, 128 s cutoff; boxcars convolved with canonical HRF), z-standardized per vertex per story; 59,412 fsLR-32k grayordinates.
- 24 evenly spaced **anchor sentences** per story, matched indices across language versions (bilingual data: matched by normalized story progress).
- **RDMs**: correlation distance on anchor responses per participant; language-level RDM = participant average. Cross-language RSA = Spearman between vectorized upper triangles.
- **Searchlight RSA** (8-mm geodesic): neural RDM vs semantic RDM (cosine distance of BLOOM layer-20 anchor representations), Fisher-averaged over stories.
- **Shared semantic geometry map**: g_sem(v) = mean of the three language-pair RSA maps (CN–EN, CN–FR, EN–FR) — Eq (7). Reliability-adjusted variant still ρ = 0.63 with G1.
- **Gradient comparison**: Margulies et al. principal functional gradient G1 (sensorimotor → transmodal/default-mode) via neuromaps, same fsLR-32k space; correspondence = Spearman over Schaefer-400 parcels; significance via **spin tests** (1,000 bilaterally-coupled spherical rotations).
- **Nulls**: anchor-label permutation within stories (max-stat FWE across cortex), circular-shift on narrative time (min displacement = max(10 sentences, 10% story)), phase-randomized BOLD for the whole estimation chain, split-half story stability, BH-FDR across locations.
- **Neurosynth decoding**: 24 Margulies-term z-maps; "apex enrichment" = mean term-z difference between top-5% g_sem parcels and top-5% G1 parcels, re-tested after regressing g_sem on G1 and rotating residuals — high-g_sem regions are transmodal (default mode, social/theory-of-mind vocabulary) beyond what G1 alone predicts.

## Key Findings

1. **Shared geometry**: individual-participant cross-language RDM correspondence ρ ≈ 0.46–0.57 (language-pair group values 0.499/0.461/0.574 + one bilingual-reading pair 0.216), all above nulls — semantic relationships, not raw response patterns, are preserved across languages and individuals.
2. **Geometry–hierarchy law**: cross-language consistency increases from sensorimotor to association cortex; g_sem ∝ G1 (ρ=0.80, spin P<0.001) — semantic commonality lives at the transmodal apex of the cortical hierarchy.
3. **Zero-shot cross-language decoding**: decoders trained on one language generalize to unseen languages (EN→CN, EN→FR, CN→EN all beat Random, P<0.0001), using per-target-subject pathways averaged over source subjects.
4. **Geometry predicts transfer**: regions with higher g_sem contribute more to cross-language decoding; cross-language neural response prediction (vertex-wise ridge on BLOOM layer-20 PCA-64 features) is more accurate in high-consistency regions; limited target-language data (30–70% stories) is rescued by transfer from source languages. Regional identification accuracy tracks the three-pair mean g_sem map.
5. **Semantic attribute directions** (concreteness, socialness, arousal from published English norms, assigned to aligned CN/FR sentences): upper-minus-lower centroid directions are parallel across the three languages (mean cosine of participant directions to other languages' group directions, above 200-draw random controls).
6. Bilingual validation (NEBULA101): Chinese-trained decoder identifies French/English passages above untrained controls; transfer with restricted cortical inputs works best through high-g_sem cortex.

## Reusable Patterns

- **Subject-specific affine pathway + shared trunk** is the cheapest inter-individual alignment that preserves cross-subject decoding (contrast: hyperalignment or full per-subject models).
- **Masked-neural-modelling pretraining** gives a semantic-free initialization for any neural encoder before contrastive alignment to an LM layer.
- **RDM/RSA geometry consistency** is the right currency for "is the representation shared?" questions — invariant to rotation/affine noise in raw patterns; combine with searchlights for maps and with spin tests for spatial significance.
- **Gradient-vs-gradient regression + residual spin test** (apex enrichment) is a clean template for claiming a map is informative beyond a known hierarchy gradient.
- Align to an **intermediate LM layer** (layer-20 of BLOOM-1.1B), standardize candidates with training-story statistics, and let a small LM propose while neural evidence selects — generalizes to any modality-conditioned generation.

## Related
- [[platonic-representations-brain]] — cross-subject shared geometry; this extends the sharing across languages.
- [[llm-semantic-convergence-human-neural-representations]], [[heterogeneous-neural-predictivity-lm]] — brain–LM representational alignment methodology.
- [[noema-fmri-naturalistic-speech-decoding]], [[brain-to-text-unified-decoding]] — adjacent fMRI speech-decoding stacks.
- Margulies et al. 2016 principal gradient; Tang et al. 2023 (Nature Neurosci) semantic reconstruction baseline.
