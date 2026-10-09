---
name: braid-fmri-cross-dataset-clip-decoding
description: BRAID-fMRI cross-dataset fMRI decoding into a shared CLIP space via ROI-token Transformer. Use when aligning heterogeneous fMRI datasets.
tags: [fmri, visual-decoding, clip, cross-dataset, transformer, contrastive-learning, neuroscience]
category: ai_collection
---

# BRAID-fMRI: Cross-Dataset fMRI Decoding into a Shared Visual-Semantic Space

**Source**: Khajehnejad, Tronti, Habibollahi, Boccato, Ferrante, Toschi — "Many Brains, One Geometry: A Shared Visual-Semantic Space for Cross-Dataset fMRI Decoding" (arXiv: 2610.09352, 2026-10-07). Tether Evo / Monash / U. Rome Tor Vergata.

## Core Claim

A single ROI-wise Transformer, trained jointly on eight independently-collected visual-fMRI datasets (MOSAIC: NSD, THINGS, Deeprecon, BOLD5000, BMD, GOD, HAD, NOD — 93 participant entries, 430,007 single-trial responses, 162,839 unique stimuli), maps heterogeneous brain activity into one frozen CLIP ViT-B/32 embedding space, and transfers zero-shot to participants and datasets never seen in training.

## Architecture (Anatomy-Indexed Tokens)

1. **ROI tokenization**: Each of 379 cortical/subcortical ROIs (fsLR32k surface, GLMsingle betas) gets its own two-layer MLP tokenizer `E_r = W2 GELU(W1 b_r + β1) + β2` mapping variable ROI dimensionality m_r into a fixed 512-d token. This absorbs per-region measurement-count differences without resampling.
2. **Identity embeddings**: Each token is augmented `Ê_r = E_r + P_r + S_i` with a learned ROI identity embedding P_r (anatomical correspondence) and an OPTIONAL participant embedding S_i (broadcast to all 379 tokens of participant i). Participant identity is defined jointly by (dataset, participant label).
3. **Shared Transformer encoder**: 4 layers, 4 heads, d=512, FFN 2048, GELU, dropout 0.1, pre-norm. Fully shared across every participant and dataset.
4. **Attention pooling**: two-layer scoring net (hidden 256) → softmax over 379 ROI tokens → weighted sum `B(i) = Σ α_r H_r(i)`.
5. **Projection head**: LN → 512→512 linear → GELU → 512→512 linear → predicted CLIP embedding Ĉ(i) ∈ R^512.

**Key design principle**: participant-specific capacity is confined to the single additive vector S_i; everything else is shared. Disabling S_i (`Ê = E_r + P_r`) yields a participant-agnostic encoder for zero-shot transfer — this separation isolates "can the shared representation generalize" from "can participant identity help".

## Multi-Positive Contrastive Objective

Cross-dataset training means repeated stimuli appear within/across participants and datasets in a batch. Standard InfoNCE would treat same-stimulus pairs as false negatives and push them apart.

Fix: symmetric cross-entropy with uniform target over ALL same-stimulus observations in the distributed batch:
- `y_ij = 1/|P(i)|` if j ∈ P(i) (same stimulus), else 0
- Logits `ℓ_ij = γ·Ĉ(i)ᵀC(j)` with learned logit scale γ init 1/0.07, capped 15
- `L = (L_B2C + L_C2B)/2`, computed over the full global batch (1,024 samples, gathered across 4 GPUs so positives/negatives span the whole batch)

**Optimization**: AdamW lr 1e-4, weight decay 1e-3 (biases/norms/logit-scale excluded), per-epoch cosine annealing, batch 256×4 GPUs, fp32, grad-clip 1.0, seed 42. Early stopping on minibatch Top-5 retrieval proxy (Δ<1e-4 for 5 epochs). CLIP encoder frozen throughout.

**Targets**: static images → frozen CLIP ViT-B/32 image embedding; videos (BMD/HAD) → embedding of the temporally central frame (explicitly does NOT decode temporal dynamics).

## Results

- **Global retrieval** (candidate pool = all unique validation stimuli across 7 eval datasets; chance 0.08%): BMD 38.1%, NSD 21.7%, THINGS 8.7%, GOD 8.6%, BOLD5000 6.6%, Deeprecon 5.6%, NOD 0.3% Top-10.
- **Matched-participant comparison** (8 participants in both BOLD5000 & NSD): BRAID 35.0±11.1% vs MindEye-style pooled-CLIP 27.1±5.1% vs ridge regression 21.1±9.1%; best in 7/8 participants.
- **Zero-shot transfer** (participant embeddings fully disabled; target dataset + all its participants held out; source pool expanded cumulatively): final-vs-initial relative gains NSD **+92.1%**, BMD +69.0%, BOLD5000 +60.9%, NOD +32.0%, THINGS +25.3%, Deeprecon +11.7%, GOD +10.9% — positive for ALL 7 targets. Individual curriculum steps non-monotonic: added datasets are not interchangeable; utility depends on source-target stimulus/participant/acquisition relationships.
- **Graded semantic geometry** (brain–brain cosine, no CLIP in the similarity calc): same-stimulus > same-cluster (+0.094 margin, P=6.4e-12) > different-cluster (+0.043 margin, P=3.9e-10). Ordering persists across datasets.
- **Cross-dataset geometry conservation**: RDMs of semantic-cluster centroids (cosine distances) correlate positively across the 5 evaluable dataset pairs, Spearman 0.61–0.88 (multiple-comparison corrected).
- **Ablations** (baseline pooled Top-10 15.4%): ventral visual/object −4.8pp, early visual −3.5pp, parietal attention −1.2pp, motion −0.9pp (BH-corrected); frontal/cerebellar/subcortical ≈ no effect. Category-specific: people/portraits hit hardest by ventral ablation (−8.0pp); tennis actions by ventral+parietal+early jointly; trains by early visual (−8.2pp).

## Reusable Patterns

1. **ROI-as-token**: replace vertexwise/voxelwise decoding with per-ROI MLP tokenizers + ROI identity embeddings — handles heterogeneous acquisition (different ROI dimensionalities per dataset/atlas) with a single shared backbone. Directly transferable to EEG (electrode-groups-as-tokens), ECoG, cross-species alignments.
2. **Optional-conditioning split**: make subject/participant conditioning an additive embedding that can be disabled at will; evaluate BOTH modes. Separates representation generality from identity-specific capacity — a clean recipe for any "personalized vs foundation" model question.
3. **Multi-positive contrastive**: whenever merging datasets with shared/overlapping stimuli, replace vanilla InfoNCE with the uniform-target symmetric CE over same-stimulus sets. Prevents false-negative repulsion across repeated presentations. Applies to any multi-cohort contrastive training.
4. **Curriculum transfer probe**: hold out an entire dataset (not just subjects), grow the source pool cumulatively, report final-vs-step-0 relative gain per target — a rigorous zero-shot transfer protocol.
5. **Geometry validation beyond accuracy**: verify matched > same-cluster > different-cluster similarity ordering AND cross-dataset RDM correspondence (Spearman on cluster-centroid RDMs) to show the model preserves relational structure, not just retrieval wins.

## Limitations (paper's own)

- Video stimuli represented by central frame only; no dynamic/action decoding.
- Category and dataset composition not disentangled in ablations.
- Curriculum expansion changes diversity and data volume jointly; controlled scaling (trials vs participants vs stimuli vs datasets) left open.
- NOD transfer weak (0.3%) — stimulus-distribution mismatch dominates for some targets.

## Related Skills

- [[platonic-representations-brain]] — isometric participant geometry without visual targets
- [[brain-it-vqa-fmri-visual-question-answering]], [[mindalign-eeg-visual-decoding]] — cross-modal alignment variants
- [[eeg-video-subject-scaling-law]] — subject-cohort scaling onset (S≈50) in EEG-video contrastive training
- [[fc-guided-band-selection-bci]] — functional-connectivity guided input selection
