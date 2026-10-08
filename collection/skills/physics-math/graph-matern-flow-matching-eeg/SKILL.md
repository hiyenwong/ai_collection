---
name: graph-matern-flow-matching-eeg
description: Graph-Matérn sensor-geometry source prior for EEG flow matching, zero parameters.
category: ai_collection
trigger_words: flow matching, EEG generation, graph Matérn, sensor geometry, source prior, PSD-KL, volume conduction, data augmentation, SF2M, stochastic interpolants
---

# Graph-Matérn Source Prior for Multi-Channel Brain-Signal Flow Matching

**Source**: Jaedong Hwang (MIT), "Sensor Geometry as a Flow-Matching Prior for Multi-Channel Brain Signals", arXiv:2610.08355 (Oct 2026, cs.LG).

## Core Insight

Flow-matching generative models default to an isotropic Gaussian source N(0, I), but multi-channel brain recordings have **known spatial structure before any data is seen**: electrodes sit at fixed head positions and volume conduction makes nearby channels co-vary (empirically the channel covariance is effectively low-rank — top-3 eigenvectors carry 61–100% of variance, participation-ratio d_eff ≈ 1–7 for 16–64 channels). Putting this structure into the **source distribution** — instead of leaving the drift network to learn it — cuts spectral discrepancy (PSD-KL) by 12–17% geometric mean, up to 40% on dense montages, with **zero added parameters**, any coupling, any drift network, and the same three hyperparameters (k=4, τ=1, α=2) on every dataset.

## Construction (from sensor coordinates ONLY — never the signals)

```
1. k-NN graph: connect sensors when either is in the other's k nearest neighbors (k=4)
   edge weights  W_ij = exp(−‖p_i − p_j‖² / h²),  h² = mean squared k-NN distance
2. Symmetric normalized Laplacian:  L = I − D^(−1/2) W D^(−1/2) = U Λ Uᵀ,  0 ≤ λ_m ≤ 2
3. Matérn spectral density per eigenmode:  φ(λ_m) = (1 + τ λ_m)^(−α)   (τ=1, α=2)
   normalize so (1/C)Σ_m φ(λ_m) = 1  (same total variance as isotropic)
4. Source sample:  x₀ = U·diag(√φ(Λ))·z₀,   z₀ ~ N(0, I_{C×T})
   (left-multiply each time slice by U; IT in temporal slot = no temporal structure imposed)
```

**Only change to training**: the marked "sample prior batch" line in the flow-matching loop — coupling π, drift v_θ, loss all untouched. Inference: draw X₀ from prior, integrate probability-flow ODE (50 Euler steps).

## Why it works (ablation-driven, TUAB/SI)

| Ablation | PSD-KL | Verdict |
|---|---|---|
| isotropic source | 1.85 ± 0.18 | baseline |
| **graph-Matérn (position graph)** | **1.08 ± 0.41** | **the winner** |
| shuffled sensor positions | 3.70 ± 2.79 | eigenvectors are the payload |
| uniformly random orthonormal basis | 4.42 ± 2.97 | any wrong basis is worse than none |
| empirical-covariance eigenvectors + graph spectrum | 2.76 ± 2.93 | data-derived basis hurts |
| empirical covariance (deff=5.2) | 4.61 ± 2.40 | fitting the data covariance directly FAILS |
| Ledoit–Wolf shrunk empirical covariance | 3.56 ± 2.43 | shrinkage doesn't rescue it |
| heat-kernel spectrum exp(−τλ) (same eigvecs) | 1.38 ± 0.86 | spectrum only needs to be smooth |
| hard low-pass (zero top half modes) | 71.40 ± 12.50 | flow can't create missing variance |
| fully connected Gaussian graph | 2.53 ± 1.81 | graph must be sparse & local |
| correlation-graph k-NN on \|corr\| | 1.39 ± 1.70 | competitive but 4× seed variance |

**Mechanism**: the gain is carried by the **eigenvectors of a sparse local graph over physical sensor coordinates** — smooth spatial modes get more variance, so the flow starts from spatially coherent patterns instead of channel-independent noise. Concentrating variance in the *wrong* directions is worse than no structure at all; a hard low-pass fails because an invertible drift must otherwise manufacture all missing high-mode variance. Data-driven bases (empirical covariance, correlation graphs) inherit recording artifacts — coordinates are artifact-free.

## Results Summary

- **8 EEG datasets** (TUAB, TUEV, Mumtaz-MDD, BCI-IV 2a, FACED, SHU, SEED-V, PhysioNet-MI; 16–64 ch) × **4 flow-matching methods** (SF2M, SI stochastic-interpolants, OT-CFM, RF+reflow): geometric-mean GP/iso ratio 0.83–0.88. Largest: PhysioNet-MI 33–35 → 20–22 (64ch, full scalp); SHU 111–116 → 81–85.
- **Generalizes unchanged**: MEG (Wakeman–Henson 102 magnetometers, −6%), intracranial ECoG with patient-specific grids (CCEP, 5 patients, −34–40%), and PEMS-BAY traffic sensors (325 GPS nodes, −11%) — the bias is not electrophysiology-specific, it is "fixed spatial sensor layout with local smoothness".
- **Downstream utility**: augmenting Mumtaz-MDD depression classification (EEGNet-8,2, subject-disjoint) lifts balanced accuracy 60.8% → 83.3% (minority-class recall 0.284 → 0.794); class-weighted training alone reaches only 54.5%. Amplitude-match synthetic windows before augmenting.
- **Failure cases**: BCI-IV 2a (22 electrodes cover only centro-parietal patch — too little spatial structure); FACED at 5× noise scale (β/γ bands); a few method/dataset pairs within seed std.

## Metrics

- **PSD-KL** (primary): symmetric KL between Gaussian fits to log band power per channel × clinical band (δ θ α β γ), averaged; lower = better; only comparable within dataset.
- **wPLI correlation** (secondary): Pearson corr between real/generated weighted phase-lag-index matrices; graph prior shapes zero-lag covariance which wPLI deliberately discards → small but consistent gains (+0.01–0.03 avg; +0.05–0.12 on densest montages).

## When to Use

- Any flow-matching/diffusion generator over **multi-channel signals with fixed sensor geometry** (EEG/MEG/iEEG/traffic/IoT arrays/weather stations).
- EEG data augmentation for small clinical datasets (minority-class rescue).
- As a drop-in replacement for isotropic noise when the network has no spatial inductive bias (e.g., 1D U-Net convolving over time with channels as input dims).

## Pitfalls

- **Never fit the prior to empirical data covariance** — it underperforms isotropic noise; coordinates only.
- **Keep the graph sparse/local** (k-NN, not fully connected).
- **Spectrum must be smooth AND full-rank** — zeroing modes breaks the flow (invertibility constraint).
- Prior encodes only spatial covariance; temporal structure is left for the drift to learn (temporal GP prior = Kronecker extension, untested in paper).
- PSD-KL is not comparable across datasets; always compare within dataset.
- Sparse montages covering a small head region gain little — check electrode coverage first.

## Implementation Sketch (PyTorch)

```python
# W: (C, C) k-NN Gaussian-weighted adjacency from 3D coords; L = I - D^-1/2 W D^-1/2
eigvals, U = torch.linalg.eigh(L)                       # (C,), (C, C)
phi = (1 + tau * eigvals).pow(-alpha)                   # Matérn density, tau=1, alpha=2
phi = phi / phi.sum() * C                               # normalize mean to 1
scale = U @ torch.diag(phi.sqrt())                      # (C, C)

def sample_prior(B, C, T, device):
    z = torch.randn(B, C, T, device=device)
    return scale @ z                                    # left-multiply each time slice
# training loop unchanged except: x0 = sample_prior(...) instead of torch.randn
```

## References

- arXiv:2610.08355; project page jd730.github.io/projects/GraphPrior
- Borovitskiy et al., "Matérn Gaussian processes on graphs" (AISTATS 2021) — the φ(λ) spectral density
- Flow matching: Lipman et al. 2023; stochastic interpolants: Albergo et al. 2025 (JMLR); OT-CFM: Tong et al. 2024; SF2M: Tong et al. 2024; RF: Liu et al. 2023
- Kollovieh et al., TSFlow (ICLR 2025) — temporal GP source prior (complementary axis, composable via Kronecker product)
