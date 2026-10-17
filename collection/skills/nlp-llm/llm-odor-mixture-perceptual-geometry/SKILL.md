---
name: llm-odor-mixture-perceptual-geometry
description: "Learn perceptual geometry of natural odor mixtures from LLM-derived descriptors via low-rank molecular kernels. Use when predicting mixture similarity or olfactory perception from composition. Activation: odor mixture, olfactory perception, LLM sensory surrogate, low-rank molecular embedding, RSA alignment."
category: ai_collection
---

# LLM-Derived Perceptual Geometry of Natural Odor Mixtures

> **Source**: Pashakhanloo & Murthy (Harvard, arXiv:2610.17164, Oct 2026) — Learning Perceptual Geometry of Natural Odor Mixtures from LLM-Derived Descriptors
> Use LLMs as a scalable surrogate for mixture-level perceptual descriptions, then learn a composition→perception similarity metric with low-rank molecular embeddings.

## Core Insight

Natural odor sources (1,200+ food items, 8,500+ volatile molecules, VCF database) are richly represented in LLM pretraining corpora (culinary/ecological/everyday contexts), making LLM-generated smell descriptions a viable **scalable supervision signal** for perceptual modeling — bypassing scarce human psychophysical data on complex mixtures. Molecules are treated ONLY as arbitrary identity labels (no chemical features); a low-rank kernel learns molecule-molecule relationships purely from mixture-level perceptual targets.

## Pipeline (5 stages)

### 1. Composition data
- Binary mixture×molecule matrix X ∈ {0,1}^{N×P}: x_m indicates which of P≈8,500 molecules occur in mixture m (1,240 mixtures; concentration unavailable → binary presence only).

### 2. LLM perceptual targets
- Prompt Llama-3.1-8B-Instruct with each mixture's NAME (not molecule list): "return 10 smell adjectives" OR free-form smell paragraph. No fixed vocabulary constraint; 5 generations per mixture for uncertainty.
- Three target constructions:
  - **Adjective word-embedding** (d=300): map each adjective to GloVe (glove-wiki-gigaword-300), average → mixture vector.
  - **Llama adjective activations** (d=4096): residual-stream activations at layer 18, pooled (averaged) over generated tokens.
  - **Llama free-form activations** (d=4096): same pooling over paragraph tokens.
- Perceptual similarity: cosine of z-scored target vectors; z-scoring fit on train mixtures only.

### 3. Kernel ladder in composition space (the key ablation)
Mixture representation z_m = (1/n_m)·1^T E x_m, kernel K = EE^T ⪰ 0, rank ≤ k:
- **Identity kernel (K=I)**: = binary cosine; vanishes for zero-overlap pairs; r=0.292 held-out.
- **Diagonal kernel (K=diag)**: per-molecule weights; still zero for zero-overlap; r=0.368.
- **Low-rank kernel (K=EE^T, k<P)**: cross-molecular terms K_ab = e_a^T e_b let mixtures be similar with NO shared molecules; r=0.545 [0.526,0.563]. On ~9,800 zero-overlap test pairs alone: r=0.432 — generalization does not rely on component overlap.

### 4. Training objective (similarity-matching)
- Ê = argmin_E [−ρ(S^comp(E), S^perc) + λR(E)], ρ = Pearson corr between vectorized upper triangles of the two RSMs.
- Regularization: R_norm(E)= (1/P)Σ_p(‖e_p‖²−1)² (pulls norms to 1) + R₂(E)=‖E‖²_F/(Pk); λ_norm=1e-2, λ₂=1e-5.
- Init: Gaussian σ=1/√k; Adam lr=0.03, grad-norm clip 10, ≤50 steps, full batch.
- Splits: 60/20/20 BY MIXTURE (not by pair) — train/val/test similarities computed only within split; ~276k train pairs, ~31k test pairs. 5 generations × 5 splits; Fisher-z aggregation; 5,000 crossed-bootstrap CIs; shuffled-label controls retrain kernels per permutation.
- Validation-selected k: mean 141 [99,200] — same order as the number of human odorant receptor types (a biological bottleneck analogy).

### 5. Validation against independent human data
- GS-LF (GoodScents-Leffingwell, 137-138 descriptors/molecule) as external check: learned molecule geometry aligns above chance WITHOUT any single-molecule supervision. Alignment strengthens when restricted to (a) geometrically STABLE molecules across fits (top-20 → r=0.57), (b) best-conditioned (observable) subspaces of the composition matrix (→ r≈0.69). Sparse/rarely-occurring molecules are weakly identified (Appendix B identifiability analysis) — always report stability-filtered alignment.

## Key Findings

1. **Cross-molecular generalization**: low-rank kernel predicts perceptual similarity even for pairs with zero component overlap (r=0.432) — the model infers that distinct molecules can play similar perceptual roles.
2. **Chemosensory specificity**: smell/taste prompts align best with composition AND GS-LF; visual/texture/color/object-identity prompts align worse on GS-LF despite comparable mixture-level predictability. Object-identity targets have HIGHER effective dimensionality (participation ratio) but LOWER odor alignment → information content alone doesn't recover odor geometry; the nature of supervision matters.
3. **Cross-modal structure**: smell–taste ρ_adj=0.81 (word-embedding space); smell–visual 0.279; adjective word-embeddings separate modalities more cleanly than Llama internal activations (identity info stripped).
4. **LLM consistency**: natural-mixture descriptions are more consistent across generations than single-molecule queries (Fig. S9) — natural objects are richer contextual anchors in pretraining corpora.
5. **External molecular features (GS-LF/OpenPOM/MolFormer/Mordred)**: modest zero-shot alignment (r≈0.24–0.35 < learned 0.53); help most in LOW-SUPERVISION regimes (inductive bias), add nothing at full data. Random high-dim features nearly match after supervised ridge — beware capacity-driven geometry preservation (Fig. S8).

## Implementation Guide

```python
import torch

# X: (N, P) binary composition; Y: (N, d) z-scored perceptual targets
# Learn E: (P, k) so that cosine similarity of Z = XE/n_m matches cosine of Y

def rsm_upper(vectors):  # representational similarity matrix → upper-tri
    v = vectors / vectors.norm(dim=1, keepdim=True).clamp_min(1e-8)
    S = v @ v.T
    n = v.shape[0]
    iu = torch.triu_indices(n, n, offset=1)
    return S[iu[0], iu[1]]

def train_lowrank_kernel(X, Y, k=141, steps=50, lr=0.03, lam_norm=1e-2, lam2=1e-5):
    N, P = X.shape
    E = torch.randn(P, k) / k**0.5
    counts = X.sum(1, keepdim=True).clamp_min(1.0)
    y_upper = rsm_upper(Y)
    E.requires_grad_(True)
    opt = torch.optim.Adam([E], lr=lr)
    for _ in range(steps):
        Z = (X @ E) / counts
        rho = torch.corrcoef(torch.stack([rsm_upper(Z), y_upper]))[0, 1]
        R_norm = ((E.norm(dim=1)**2 - 1)**2).mean()
        R_2 = (E**2).sum() / (P * k)
        loss = -rho + lam_norm * R_norm + lam2 * R_2
        opt.zero_grad(); loss.backward()
        torch.nn.utils.clip_grad_norm_([E], 10.0); opt.step()
    return E.detach()

# Zero-overlap evaluation: select test pairs (x_m·x_n = 0) and report
# corr(kernel-similarity, perceptual-similarity) on those pairs only.
```

- Diagonal-kernel variant: K=diag(softplus-free exp(θ)), θ init 0, clip [-8,8], mean-rescale to 1; lr=0.05, 100 steps.
- For layer choice in the LLM: default layer 18 of 32 (mid-network); sweep layers if targets are noisy (Fig. S6); pool over generated tokens only (not the prompt).
- Adjective count sweep {3,5,7,10,15,20,30,50}: 10 is default; more adjectives dilute, fewer are high-variance.

## Applicability & Extensions

- **Any modality with object-level language anchors**: replace "smell of {food}" with taste/texture/appearance prompts; same pipeline measures whether a feature space is perceptually organized.
- **Zero-overlap generalization test** transfers to any set-composition domain: drug combinations, ingredient lists, microbiome species assemblages — the low-rank kernel handles non-overlapping sets where Jaccard/cosine are structurally blind.
- **Inverse design**: embed a target description in perceptual space, then search composition-space directions (add/remove/substitute components) that move a mixture toward it.
- **Data-limited inductive bias**: when mixture-level supervision is scarce, initialize E rows from external molecular features (MolFormer/Mordred/OpenPOM); let low-rank training take over as data grows.
- **Limitations**: binary composition (no concentrations); VCF entries compiled across heterogeneous studies; LLM targets carry non-olfactory semantic correlations (use modality-specific prompts + object-identity controls to isolate).

## Related Skills

- [[adult-neurogenesis-olfactory-representational-stability]] — olfactory coding stability (biological complement)
- [[fisher-memorization-geometry]] — another geometry-of-learned-representations methodology
- [[eeg-speech-decoding-detection-floor-audit]] — rigorous-audit methodology pattern (stability filtering analogous to detection floors)
