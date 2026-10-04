---
name: field-closure-ice-neurons-dendritic-motifs
description: "Field closure (ephaptic feedback γ) turns growth-rule dendrites into dynamical motifs; ice-neuron limit separates silhouette from function."
category: ai_collection
tags: [neuroscience, dendritic-computation, ephaptic-coupling, morphogenesis, fitzhugh-nagumo, mullins-sekerka, motif-detection, cable-theory]
arxiv_id: 2610.00184
paper_title: "Field closure, ice neurons, and when a dendrite is a motif"
paper_url: https://arxiv.org/abs/2610.00184
authors: "Nima Dehghani (MIT McGovern Institute / IAIFI)"
published: 2026-09-17
---

# Field Closure, Ice Neurons, and When a Dendrite Is a Motif

Methodology from arXiv:2610.00184 (Dehghani, MIT, 2026): a single continuum system contains the "ice neuron" (Mullins–Sekerka growth instability without internal state) as the **zero-gain limit γ=0**, and shows that finite **field closure** (the interface writes back into the driving field — the ephaptic-coupling loop) is what turns a grown dendritic tree into a genuine **dynamical motif**, not a structural spandrel.

## Core Methodology

### 1. The Central Distinction — Two Readings of "Motif"
- **Census motif** (subgraph overrepresentation): produced by ANY growth rule (Solé spandrels — pond ice shares branching statistics with neurons because both share a growth instability). Cheap; says nothing about function.
- **Dynamical motif** (wiring exists because of what it does): requires the tree to DO something when driven.
- Ice neuron = growth structure WITHOUT internal state. Active cable (γ=0 with FHN state) = internal dynamics without field feedback. Field-closed neuron (γ>0) = the biophysical loop biological neurons have (transmembrane currents → extracellular field → ephaptic feedback onto membrane).

**Hierarchy (Table 1):** growth structure ⊂ +internal dynamics (active cable) ⊂ +field feedback (γ>0) ⊂ (computation = further question about what the loop implements).

### 2. The Coupled System
- **Morphological sector**: quasi-static exterior field ∂tφ = D∇²φ; Gibbs–Thomson φ|Γ = Δ − d₀κ; Stefan flux v_n = −K(n·∇φ − γψ).
- **Interfacial state**: FitzHugh–Nagumo pair (ψ fast, w slow) ON the moving front, with tangential diffusion D_ψ∂²_s ψ; φ feeds ψ via βφ|Γ (β coupling), ψ writes back via γψ source term — **bidirectional field closure**.
- Isolated oscillator parked SUBcritical (tr J₀ = −0.055 < 0): any oscillation that appears must be a property of the coupled system, not the isolated FHN.

### 3. Linear Theory — Coupled Cubic Spectrum
Normal modes ζ ∼ e^{ωt+iky} give dispersion:
- ω = p(k)|k| + Kγχ(k,ω), p(k) = K(G_eff − d₀k²)
- At γ=0 factors into (ω − p_k)·[isolated FHN quadratic] — two independent spectral branches.
- Finite γ deforms spectrum: lifts long-wavelength side more strongly (closure term lacks the |k| factor), shifts selected instability toward smaller k; opens a **complex-dominant region** in the (G,γ) plane where the isolated oscillator is still quiescent → γ-driven Hopf.
- Cubic characteristic ω³ + Aω² + Bω + C = 0; classify each (G,γ) cell by winning root: planar / real-dominant / complex-dominant.

### 4. Motif Assay on a Frozen Tree (the key experiment)
1. **Grow** tree at γ=0 with memoryless self-avoiding tip-splitting rule (split prob 0.07, daughters ±0.62 rad; Solé class, NOT Laplacian growth).
2. **Freeze** geometry; resample to N compartments (working tree N=117; ensemble N=29–358, median 226).
3. Two operators: graph Laplacian L (cable, g_c=0.12) + screened ephaptic matrix (G_eph)ij = 0.12·e^{−r_ij/λ}/r_ij, λ=6 (screening is REQUIRED — unscreened 1/r destabilizes at vanishing γ).
4. Compartmental dynamics: Ẏ = [[f_ψI − g_cL + βγG_eph, −I],[εI, −εγ_wI]]Y + I_ext(t).
5. **Persistence index** 𝒫 = ∫_{t*}^T |ψ_out|dt / ∫_0^{t*}|I_ext|dt — post-stimulus L¹ mass at a DISTAL readout after DISTAL pulse drive (distal-to-distal avoids the ill-conditioned somatic ratio on leaky cables).

### 5. First-Order Excess Kernel (perturbative motif work)
DC gain Q(γ) = −e_out^⊤ A(γ)⁻¹ e_in; resolvent expansion:
- **Q(γ) − Q(0) = γQ₁ + O(γ²)**, Q₁ = z_out^⊤ B z_in (B = βG_eph; z_in/z_out solve adjoint systems)
- Pair decomposition Q₁ = Σ_ij z_out,i B_ij z_in,j maps the motif's work onto the tree: the 40 largest pairs carry **99.9%** of the contribution — a few DIRECT FIELD SHORTCUTS between drive and readout, not the silhouette.
- Working tree: Q₁ = 9.6×10⁻⁴; measured excess follows γQ₁ with mean relative error 0.027.

### 6. Ensemble Robustness (80 seeds)
- **Q₁ > 0 on ALL 80 trees** (1.7×10⁻⁶ – 1.7×10⁻², median 1.1×10⁻³): sign of first-order closure effect is geometry-independent.
- Stable window generic: γ* median 0.14 (IQR 0.12–0.17).
- First-order law holds across four decades of γ_pQ₁ (median deviation 0.06); diagonal is NOT a fit — prediction from each tree's own γ=0 operator.
- Persistence FOLD deliberately not promoted to ensemble statistic (γ=0 baseline collapses with depth, Q(0) spans 3×10⁻⁵⁴ – 2×10⁻⁴ — fold measures death of denominator).

### 7. Amplitude-Regime Dependence
- **Subthreshold pulse (amp 0.05)**: nonlinear tracks linear 𝒫 through the stable window; at γ* linear 𝒫 undefined but nonlinear continues smoothly — "closure is almost the transmission" (P(0.17)/P(0) ≈ 4.7×).
- **Spike-sized pulse (amp 0.8)**: cable already transmits (𝒫≈17 → 19.6 at γ=0.35); closure is a fractional correction to a regenerative cable event — "a correction to a cable spike that ice still does not have, because ice has no cubic."

## Implementation Recipe

```python
# Frozen-tree motif assay
# 1. Grow: tips step + angular noise + self-avoidance; split p=0.07, ±0.62 rad
# 2. Freeze; resample to N compartments; build L (graph Laplacian)
# 3. G_eph[i,j] = 0.12 * exp(-r_ij/6) / r_ij   # screened; MUST screen 1/r
# 4. A(gamma) = [[f_psi*I - g_c*L + beta*gamma*G_eph, -I],
#                [eps*I, -eps*gamma_w*I]]
# 5. Q1 = z_out.T @ (beta*G_eph) @ z_in   # adjoint solves: A0 z_in = e_in, A0.T z_out = e_out
#    → Q1 > 0 certifies first-order motif work; pair-decompose for shortcut localization
# 6. Persistence: distal pulse (t*=1.2), distal readout, P = ∫|psi_out|/∫|I_ext|, dt=0.02, T=40
# 7. Hopf check: cubic roots of omega^3 + A omega^2 + B omega + C below isolated tr J0 < 0
```

## Falsification Criteria (from paper)
- First-order law Q(γ)−Q(0)=γQ₁ failing on honest Mullins–Sekerka/Laplacian-grown trees (not just tip-splitting rule)
- Q₁ sign flipping on some growth-rule ensemble
- A growing-tip Hopf absent in amplitude-equation analysis (the complex-dominant region ≠ "the tip rings")

## When to Use
- Distinguishing structural (census) motifs from dynamical motifs in connectomic data
- Modeling ephaptic/field-mediated dendritic computation beyond cable theory
- Growth-rule dendrite generation + functional assay (motif work localized via adjoint kernels)
- Physical-computation hierarchy arguments (growth ⊂ dynamics ⊂ field closure ⊂ computation)
- Any "does this morphology compute?" question — use the γ-sweep + Q₁ kernel, not subgraph counts

## Related Skills
- [[dn-synaptic-placement-shared-input]] — dendritic topology vs subcellular placement specificity
- [[second-order-synaptic-motifs-nonlinear-dynamics]] — mean-field for synaptic motif effects
- [[connectome-wiring-specificity-null-models]] — nested rewired nulls for wiring specificity
- [[plastic-arbor-simulation]] — synapse-to-network plasticity simulation framework

## Citation
Dehghani, N. (2026). Field closure, ice neurons, and when a dendrite is a motif. arXiv:2610.00184. https://neurovium.science/posts/pblog-IceNeuron
