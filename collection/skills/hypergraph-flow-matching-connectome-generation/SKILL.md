---
name: hypergraph-flow-matching-connectome-generation
description: Use when generating or translating brain SC-FC connectomes. Hypergraph encoders plus latent flow matching, 8x faster than diffusion.
category: ai_collection
---

# Multimodal Hypergraph Flow Matching for Connectome Generation (MHG-FM)

**Paper**: "Structural-Functional Brain Connectivity Generation via Multimodal Hypergraph-based Flow Matching" — Poh, Tew, Loo, Phan, Noman, Yap, Ting (Monash Malaysia / NTU / UNC), arXiv:2610.02722, cs.LG, Oct 2026.

## Core Contribution

Joint generative model over **paired structural (SC, DTI) + functional (FC, rs-fMRI) connectomes** with three novelties over prior connectome generators (BrainNetDiff, SFC-GAN, HYGENE):
1. **Hypergraph (higher-order) message passing** — hyperedges group >2 ROIs, capturing polyadic interactions pairwise graphs miss.
2. **Bidirectional SC↔FC coupling** via Dual Cross-Attention fusion — models structure-function constraint in both directions instead of one-way translation.
3. **Latent conditional flow matching** replaces diffusion's iterative denoising — ~8× faster sampling (106 ms vs 848 ms/sample, 32 vs 250 NFE) at comparable fidelity.

## Architecture Recipe

### Stage 1 — Hypergraph construction (deterministic, fixed during training)
- **SC hyperedges**: from population-mean structural matrix, region i + all j with mean-SC > τ_s=0.01 (anatomy-grounded).
- **FC hyperedges**: 4 motif groups on population-mean FC: (1) triangle cliques |A^F_ij|>0.7; (2) hub-and-spoke: top-80th-percentile-degree hubs to k*=8 strongest correlates; (3–4) k-NN groups k=5, k=10.
- Dedupe exact-duplicate memberships → joint incidence matrix; **majority vote across subjects (retain hyperedges in ≥30% of subjects)** → population-level fixed scaffold.
- Incidence matrices are **structural priors only** — the generative target remains the N×N adjacency matrices (SC/FC), never the hypergraphs.

### Stage 2 — Encoders
- SC encoder: 2 stacked HGNN layers + residual + BN, mean-pool → z_SC (2 layers chosen to avoid hypergraph over-smoothing).
- FC encoder: dual-stream DualStream blocks (parallel HGNN node/hyperedge streams with intra-block cross-attention).
- **DCA fusion**: symmetric cross-attention — Attn_SC→FC = Softmax(Q_SC K_FC^T/√d) V_FC (and mirror), then h = MLP([z̃_SC, z̃_FC, z_SC, z_FC]) — 4-way concat keeps both attended cross-modal AND original unimodal signals.
- VAE projection to shared latent q(z0|h)=N(μ, diag(σ²)), d_z=128; KL annealed 0→5e−5 over 9k steps.

### Stage 3 — Latent flow matching
- Rectified-linear interpolant x_t = (1−t)x0 + t·x1; target velocity u_t = x1 − x0; CFM loss = E‖v_θ(x_t,t) − u_t‖².
- Sampling: adaptive dopri5 ODE solver (atol 1e−5, rtol 1e−4) from x0=[η,η], η~N(0,I); split trajectory halves into ẑ_SC, ẑ_FC → modality decoders. SC/FC divergence from shared noise is an **emergent** property of the learned velocity field.

### Stage 4 — Decoders
- SC decoder: HGNN layers → node features → symmetric pairwise MLP head, sigmoid×3 output range, plus **sparsity loss** L_sp (white-matter biology prior), topology-weighted MSE (w_ij = 1+19·1[A^SC_ij>0.01]).
- FC decoder: **highway gate** blends local HGNN pairwise prediction with global MLP: Â = g·Â_global + (1−g)·Â_local, g=σ(W_g z).

### Loss (5 terms)
L = 7·L_SC + 16·L_FC + 0.02·L_CFM + β·L_KL + 0.05·L_sp; Pearson-r auxiliary terms (λ_r=3.0 SC / 0.5 FC); modality dropout p∅=0.25 for translation training.

### Cross-modal translation (zero extra cost)
FC→SC: zero-fill missing SC, encode observed FC, DCA-fuse, decode SC only — **single deterministic pass, no ODE**. Works because modality dropout (p∅=0.25) during training makes zero-filled inputs in-distribution.

## Key Results (HCP-YA 3T, AAL-116, 562/70/70 split)

- Matrix-level: SC r≈0.95 (R²≈0.87–0.89), FC r≈0.83 (R²≈0.66) — MHG-DiT slightly better on SC, MHG-FM better on FC.
- **Topology-level (the differentiator)**: MHG-FM best overall Deg-W1 (SC 0.498/FC 1.30 vs DiT 10.05/8.89) and NMI (SC 0.42, FC 0.37); the diffusion backbone attains high matrix fidelity with **collapsed degree/community structure** — Pearson r alone is a misleading metric for generative connectomes.
- Coupling: |ΔMI| SC–FC gap 0.0072 (DiT) vs 0.0188 (FM), both ≪ baselines (HYGENE 0.81).
- Translation: FC→SC r=0.941 (best all metrics); SC→FC r=0.573 — structural constrains but does not determine function (asymmetric difficulty is expected).
- Ablations: removing DCA cross-attention → weaker FC + larger coupling gap; pairwise GNN instead of HGNN → worse on ALL metrics (hypergraph message passing matters); AdaLN > additive time conditioning; score-based backbone close but larger coupling gap.
- Seeds 42/123/456: SC r SD 0.0009 — reported ± reflects inter-subject variability, not instability.

## Reusable Patterns

1. **Fixed-incidence hypergraph scaffold**: build population hyperedges once (motif pooling + 30% subject-vote), use as message-passing prior, generate plain adjacency matrices. Decouples higher-order representation from generation target.
2. **DCA fusion for bidirectional modality coupling**: prefer explicit symmetric cross-attention over fixed fusion rules when two modalities constrain each other (applies to any paired-graph generation: gene-regulatory + protein-interaction, SC-FC, multimodal road networks).
3. **Modality dropout (p=0.25) enables free cross-modal translation** at inference via zero-filling — no separate translation model needed.
4. **Evaluate generative connectomes with topology metrics (Deg-W1, NMI/ARI with permutation-averaging, |ΔMI|), never Pearson r alone.**
5. Flow matching in VAE latent space as a drop-in diffusion replacement when sampling cost matters (~8× speedup, 32 NFE adaptive).

## Related Skills

- [[multi-scale-hypergraph-brain-connectivity]] (MuHL — discriminative hypergraph learning; MHG-FM adds the generative direction)
- [[evolvable-graph-diffusion-ot]] (EDT-PA — diffusion-based generation; MHG-FM is flow-matching + explicit SC-FC coupling)
- [[linear-structure-function-coupling]] (predicts FC from SC; MHG-FM generates joint pairs + bidirectional translation)
- [[sd3mf-multimodal-brain-network]] (matrix-factorization fusion vs hypergraph cross-attention)
