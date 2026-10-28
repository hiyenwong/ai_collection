---
name: neurocbir-brain-mri-retrieval
description: Use when building brain MRI retrieval or medical CBIR systems. VAE + MPRCL contrastive learning.
category: ai_collection
---

# NeuroCBIR: Multi-Positive Ranking Contrastive Learning for Brain MRI Retrieval

**Paper**: "NeuroCBIR: A Fast and Accurate Image Retrieval System for Whole-Brain and Region-Specific MRI" (arXiv: 2610.06502, Nieto-del-Amor et al., Oct 2026). Code: https://github.com/minnelab/NeuroCBIR — includes >26,000 precomputed T1w MRI embeddings.

## What It Solves

Content-based image retrieval (CBIR) for 3D T1w brain MRI that works at BOTH whole-brain and region level (103 cortical/subcortical regions extracted per scan), generalizes across datasets/scanners/field strengths, and encodes clinically meaningful structure usable zero-shot for age estimation and CN/MCI/AD stratification — without task labels during training.

## Pipeline (two-stage)

### Stage 1: VAE-GAN latent pretraining
- 3D VAE (encoder ϕ, decoder θ) + adversarial discriminator ψ trained alternately per batch (autoencoder update on L_VAE with ψ fixed; ψ updated on real-vs-reconstructed with L_C).
- Purpose: learn anatomical latent space μ_ϕ; using latents instead of raw images in Stage 2 enables batch size 128 for 3D volumes.

### Stage 2: Encoder-projector + MPRCL (the core novelty)
- Convolutional encoder E_ω′ on μ_ϕ latents + FC projector P_ω → L2-normalized embedding z (dim N_f=32 best; searched {16,32,64,128,256}).
- **Label design**: whole-brain → subject identity; region-based → (subject, region) pair. Longitudinal scans of the same subject are hard positives.

### MPRCL: Multi-Positive Ranking Contrastive Loss
Three-way relationship structure per anchor (asymmetric contrastive geometry):
- **Hard positives**: same label (same subject). Loss L_hp = 1 − s_i^{hp,min} (pull minimum hard-positive similarity to 1).
- **Soft negatives**: different-subject samples CLOSE in latent space (VAE cosine similarity above per-anchor upper percentile π_sn) — semantically similar people occupy intermediate distances.
- **Hard negatives**: different-subject samples FAR in latent space (below percentile π_hn).
- Ranking losses: L_sn = [m_i^sn + s_i^{sn,max} − s_i^{hp,min}]₊ (separate positives from soft negatives); L_hn = [m_i^hn + s_i^{hn,max} − s_i^{sn,min}]₊ (separate soft from hard negatives).
- **Adaptive margin scaling**: m_i^sn = α_sn·Δ_i, m_i^hn = α_hn·Δ_i where Δ_i = max_j s_ij − min_j s_ij (anchor-specific similarity range, excluding self) — robust to varying batch similarity distributions.
- Final: L = mean(L_hp) + λ_sn·mean(L_sn) + λ_hn·mean(L_hn).
- **Negative mining via frozen VAE similarity** s̃_ij = μ_ϕ,i^T μ_ϕ,j / (‖μ_i‖‖μ_j‖) treated as fixed non-trainable signal; percentiles computed per anchor per batch.
- Region-based variant: loss computed independently per region; each iteration samples 10 random regions of 103 and averages.
- Batch construction: ≥32 anchors, ≥3 hard positives per anchor.
- Optimizer: AdamW, lr 1e-4.

## Key Results

| Task | Metric | Value |
|---|---|---|
| Whole-brain re-ID | mAP@5 | 98.4–99.6 (external: ADNI 99.3, OASIS3 92.5, AIBL 98.4, MIRIAD/SLIM ~high) |
| Region re-ID (hippocampus, ventricles) | mS@1 | >98% most datasets |
| Embedding speed | 4-core CPU | ~18.7 s/scan; similarity search <0.01 s |
| Zero-shot age est. (top-500 retrieval aggregation) | MAE | 4.3 yr whole-brain (r=0.54); supervised ref baselines 2.67–3.8 yr |
| Zero-shot CN/MCI/AD (top-500) | BAcc | 56.3% whole-brain (chance 33%); regions 49.7–57.9% |
| AD queries age-bias | retrieval | retrieves CN subjects ~6 yr older — disease signal emerges unsupervised |

Datasets: ADNI (20,367 scans/2,389 subj), OASIS3 (2,642/1,303), AIBL (1,276/685), MIRIAD (706/69), SLIM (1,015/571) — multi-manufacturer (Siemens/GE/Philips), 1.5T+3T.

## Ablation Insights (which loss term does what)

- **Remove soft-negative loss (λ_sn=0)**: mAP@5 98.6% → 79.0% — retrieval identity accuracy collapses. Soft-negative term is what keeps same-subject scans tight.
- **Remove hard-negative loss (λ_hn=0)**: mAP@5 stays high BUT ρ_MS-SSIM −0.71 → −0.01 — perceptual/semantic alignment with MS-SSIM is destroyed. Hard-negative term preserves the perceptual ordering of the space, and drives zero-shot utility (age MAE 4.3→5.2 yr, disease BAcc 56.3→38.4%).
- **Remove both**: highest mAP@5 but meaningless geometry → the paper's central lesson: retrieval accuracy ≠ embedding quality; the two ranking terms encode different geometry requirements.

## Reuse Patterns (beyond MRI)

1. **Asymmetric 3-tier contrastive geometry** (positives / soft-negatives / hard-negatives with intermediate-distance ordering) generalizes to any metric learning where "similar but distinct" matters: face re-ID, speaker verification, product dedup, patient re-identification across visits.
2. **Two-stage VAE→contrastive** — pretrain generative latents first, then contrastively refine on latents: makes large-batch contrastive learning tractable for expensive 3D/high-dim modalities.
3. **Frozen-teacher negative mining** — use the Stage-1 (VAE) similarity as a fixed percentile-based miner instead of end-to-end hard-negative feedback loops; per-anchor percentiles adapt to local density.
4. **Adaptive margin scaling by per-anchor similarity range** Δ_i — superior to fixed margins under heterogeneous batch distributions.
5. **Zero-shot task probing of retrieval embeddings** — aggregate labels of top-k retrieved neighbors (no training) as an evaluation protocol AND a weak-supervision signal; age-gap bias of AD retrievals is an emergent biomarker.
6. **Identity-supervised, task-free pretraining** — subject-ID labels only (available in any longitudinal dataset) yield embeddings that transfer to age/disease zero-shot; no task labels needed.

## Related Skills
- [[brain-mri-foundation-clinical]] — SSL brain MRI foundation models (complementary: NeuroCBIR = retrieval-oriented)
- [[braindinobrain-mri-foundation]] — DINO-style brain MRI
- [[federated-brain-trajectory-gnn]] — longitudinal brain trajectories

**Activation**: brain MRI retrieval, CBIR, medical image retrieval, contrastive learning, MPRCL, subject re-identification, zero-shot age prediction, Alzheimer stratification, VAE embedding, metric learning
