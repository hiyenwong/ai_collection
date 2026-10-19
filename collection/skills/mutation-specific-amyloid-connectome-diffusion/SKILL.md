---
name: mutation-specific-amyloid-connectome-diffusion
description: Mutation-aware Aβ aggregation-fragmentation model coupled to connectome graph diffusion for familial AD. Use for network propagation of protein aggregation, mutation kinetics on brain graphs.
category: ai_collection
---

# Mutation-Aware Aβ Aggregation–Fragmentation–Diffusion on the Connectome

Source: "Connectome-Based Modeling of Mutation-Specific Amyloid-β Aggregation in Familial Alzheimer's Disease" (Chowdhury & Shaheen, arXiv:2610.09583, q-bio.NC, 7 Oct 2026)

## Core Framework

Couple a local coarse-grained Smoluchowski-type aggregation–fragmentation reaction system to interregional diffusion on a structural connectome Laplacian, with **mutation-specific kinetic scaling** injected at one reaction channel.

### 1. Three-species local reaction system (per brain region i)

Species: monomers c₁, oligomers c₂, fibrils c₃. Reaction channels:

| Process | Reaction | Propensity aᵢ | Stoichiometry |
|---|---|---|---|
| Monomer production | ∅ → c₁ | s | (+1, 0, 0) |
| Primary nucleation (seed-gated) | n·c₁ → α_nuc·c₂ | χᵢ·k_nuc·c₁ⁿ | (−n, +α_nuc, 0) |
| Secondary nucleation | m·c₁ + c₃ → α_sec·c₂ + c₃ | k_sec·c₁^m·c₃^p | (−m, +α_sec, 0) |
| Elongation | c₁ + c₃ → (1+β)·c₃ | k_elong·c₁·c₃ | (−1, 0, +β) |
| Conversion | c₂ → c₃ | k_conv·c₂ | (0, −1, +1) |
| Fragmentation | c₃ → c₂ | k_frag·c₃ | (0, +1, −1) |
| Clearance (x∈{1,2,3}) | cₓ → ∅ | δₓ·cₓ | (−1, 0, 0)/… |

Primary nucleation is **restricted to seed regions** via indicator χᵢ; all other channels run at every node.

### 2. Mutation-aware kinetic scaling (the key trick)

Experimental nucleation scores NS_μ from deep mutational scanning (GSE151147) are mapped exponentially to rate multipliers:

```
f_μ = exp(NS_μ),   NS_WT = 0  →  k_nuc^(μ) = k_nuc^(WT) · exp(NS_μ)
```

Generalize with a scaling exponent γ: `k_nuc^(μ) = k_nuc^(WT) · exp(γ·NS_μ)`.
Mutation-score uncertainty propagates as NS̃_μ ~ N(NS_μ, σ²_μ), 500 Monte Carlo realizations.
Mechanism-uncertainty variants: map mutation factor to primary nucleation only / secondary only / both.

### 3. Connectome coupling via graph diffusion

Normalized adjacency A = A_raw/κ (κ = max node strength), Laplacian L = D − A. Per species x:

```
dcₓ,ᵢ/dt = Σ_r Δx_r · a_r,i(c) − ρ·dₓ·(L cₓ)ᵢ
```

with relative mobility d₁=1, d₂=2^(−1/3), d₃=3^(−1/3), nominal global transport ρ=0.05. Negative sign before L ⇒ ordinary diffusion toward structurally connected lower-concentration regions. RK4, Δt=0.25, T=300 model-time units, non-negativity clipped.

Seeds: posterior cingulate + precuneus (early-amyloid default-mode regions), top-18 by structural strength out of 36 candidates; fibril seed c₃(0)=1e−6 at seeds only, c₁(0)=1 everywhere.

## Key Results (numbers to reuse)

- **E22G (Arctic) dominates**: threshold-crossing at 8.80 vs WT 110.67 model-time units; largest cumulative oligomer AUC 0.7225 vs WT 0.6326. E22Q/D23N intermediate-fast, E22K smaller, H6R/A21G ≈ WT, A2V slowest (AUC 0.6027).
- **Kinetics vs topology separation (the headline finding)**:
  - Global sensitivity (LHS 500 sets, 0.1–10×, PRCC): threshold timing driven by monomer production (−0.654), conversion (+0.601), primary nucleation (−0.411), monomer clearance (+0.400). **Diffusion scale ρ ≈ irrelevant for timing/peak/AUC (−0.029) but matters for spatial spread (+0.317)**. Elongation dominates spatial spread (PRCC 0.878).
  - All 20 degree-preserving randomized connectomes **preserve mutation rankings** (timing/peak/AUC ρ=1) but **destroy regional burden patterns** (empirical-vs-null spatial Spearman only 0.19–0.35; top-10% Jaccard 0.07–0.13).
  - Distance–arrival coupling: weighted connectome distance from seeds vs oligomer arrival time, **Spearman ρ ≈ 0.92** for every mutation; burden at reference time vs distance ρ ≈ −0.82 to −0.93.
- **Robustness asymmetry**: timing & cumulative burden (AUC) stable; **exact peak-amplitude ordering is NOT** (posterior mean rank ρ = −0.177, exact recovery only 36% of draws). Report timing/AUC, distrust peak distinctions.
- **ABC-SMC parameter recovery** (γ, k_sec, k_frag, k_conv; 32-dim summary = 4 stats × 8 mutations): generating values inside 95% posterior intervals; γ posterior median 0.950 (gen 1.0); k_sec ↔ k_conv trade-off (compensatory identifiability).
- **Chemical Langevin stochasticity**: ensemble medians preserve deterministic ordering exactly (2400 trajectories); individual trajectories overlap near-WT mutations (H6R/A21G cross earlier than WT only ~50–54%; E22Q/E22G ~99%). E22G strictly fastest in 76.7% of single realizations. nRMSE → 0.008 as Ω: 100→2000.

## Implementation Skeleton

```python
import numpy as np

def rhs(c, A, L, p, chi, mu_factor):
    # c: (3, N) species × nodes; p: param dict; chi: (N,) seed indicator
    c1, c2, c3 = np.maximum(c[0], 0), np.maximum(c[1], 0), np.maximum(c[2], 0)
    a_prod = p['s']
    a_nuc  = chi * p['knuc'] * mu_factor * c1**p['n']        # mutation-scaled, seed-gated
    a_sec  = p['ksec'] * c1**p['m'] * c3**p['p']
    a_elg  = p['kelong'] * c1 * c3
    a_cnv  = p['kconv'] * c2
    a_frg  = p['kfrag'] * c3
    d1 = p['d1'] - a_nuc*p['n'] - a_sec*p['m'] - a_elg - p['delta1']*c1
    d2 = a_nuc*p['alpha_nuc'] + a_sec*p['alpha_sec'] + a_frg - a_cnv - p['delta2']*c2
    d3 = a_elg*(1+p['beta']) + a_cnv - a_frg - p['delta3']*c3
    # graph diffusion: -rho * d_x * (L c_x)
    return np.stack([d1 - p['rho']*1.0     *(L @ c1),
                     d2 - p['rho']*2**(-1/3)*(L @ c2),
                     d3 - p['rho']*3**(-1/3)*(L @ c3)])
# RK4 loop with dt=0.25, clamp ≥0 each step
```

## Analysis Checklist (the paper's 10-part robustness suite)

1. Mutation-score uncertainty MC (score variance → rate distribution)
2. Mechanism-uncertainty: which reaction channel carries the mutation factor
3. Global sensitivity: Latin hypercube 0.1–10× all 10 params + PRCC + bootstrap CIs
4. Seed-robustness: alternative seed configurations (region subsets, random draws)
5. Edge-weight robustness: weighted vs binary vs sqrt-transformed
6. Degree-preserving null connectomes (connected double-edge rewiring, weight set preserved) — separates kinetics (rank-stable) from topology (spatial patterns)
7. Distance–arrival analysis: effective edge length ℓᵢⱼ = 1/max(A_raw,ij, 1e−12); weighted shortest path from seeds; Spearman arrival correlation
8. Synthetic ABC-SMC recovery (internal identifiability, NOT clinical calibration)
9. Posterior-predictive propagation through full connectome (100 draws)
10. Chemical Langevin reaction noise (Euler–Maruyama; transport stays deterministic)

## Reusable Lessons

- **Mutation/condition effects enter as exp(score) multipliers on ONE channel** — a clean pattern for injecting experimentally measured variant effects into mechanistic ODE systems without re-parameterizing the whole model.
- **Kinetics sets the clock, topology sets the map**: rank-based outputs (timing, cumulative burden) survive null-network randomization; spatial-pattern outputs don't. Any network-diffusion disease model should report this separation explicitly.
- **Rank-stability > point-estimate stability**: evaluate conclusions as rank correlations under uncertainty (posterior draws, stochastic trajectories), and explicitly flag which outputs are unstable (here: peak amplitude).
- **Synthetic ABC-SMC before real fitting**: verify the summary statistics can recover known generating values; expose parameter trade-offs (k_sec ↔ k_conv) before trusting any fit to real data.
- Limitations to carry over: nominal (not calibrated) parameters, model-time units, healthy consensus connectome, no tau/neuroinflammation/vascular/clearance heterogeneity.

## Key References

- Seuma et al. — deep mutational scanning of Aβ42 nucleation (GSE151147), the score source
- Raj et al. 2012; Iturria-Medina et al. 2018 — connectome network-diffusion models of neurodegeneration (predecessors without mutation-specific kinetics)
- Nilsberth et al. 2002 — Arctic (E22G) enhanced protofibril formation; Messa et al. — A2V atypical assembly pathway
- Budapest Reference Connectome v3.0 (540-node LCC used here); GSE247583 auxiliary QC dataset
