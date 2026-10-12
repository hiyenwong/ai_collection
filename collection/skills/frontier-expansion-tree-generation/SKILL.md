---
name: frontier-expansion-tree-generation
description: Use when generating 3D neuron and tree morphologies.
category: ai_collection
---

# Autoregressive Frontier Expansion: Growing Trees with Graph ML

Source: Gupta, Peltonen, Ritzert (2026) "Autoregressive Frontier Expansion: Growing Trees with Graph Machine Learning" (arXiv:2609.38506). A generative framework that constructs branching structures (cortical neurons, botanical trees, vessels) by iterative growth, predicting **topology and geometry jointly** — unlike MorphGrower (fixed seed topology) or MorphoGen (post-hoc skeletonisation of point clouds).

## Core Idea

Generate a tree as a sequence {T⁰,…,Tᴸ} of partial trees. At each level ℓ, operate on the **active frontier** Aℓ (leaves created in the previous step). Each iteration = two operations:

1. **Frontier expansion** — predict binary expansion state Γℓ(v) ∈ {0,1} for each v ∈ Aℓ. Nodes with Γ=1 receive two children (vL, vR), yielding intermediary tree T̃ℓ⁺¹.
2. **Localisation** — predict parent-relative offsets Cℓ⁺¹(v) so that Pℓ⁺¹(v) = Pℓ(π(v)) + Cℓ⁺¹(v).

Shift the expansion prediction forward one level so that (Cℓ, Γℓ) are modelled as ONE conditional distribution given T̃ℓ:

    pθ(T⁰,…,Tᴸ) = ∏ℓ pθ(Cℓ, Γℓ | T̃ℓ)

Generation stops when Γℓ = 0 (empty frontier). Root special-case: soma carries k primary dendrites (Kmax=23), all created in one step with sibling-rank one-hot features (they share a single local frame, so rank is the only distinguishing signal).

**Trees are valid by construction** — no post-hoc spanning-tree repair needed (SemlaFlow: only 76.6% valid on neurons, 12.5% on botanical trees).

## Flow Matching on the Frontier State

Per-level conditional flow matching on the frontier state X = [Č, Γ] ∈ R^{|Aℓ|×4}:
- Linear OT interpolant: Xt = (1−t)X₀ + tX₁, X₀ ~ N(0,Σ) (Σ diagonal: unit variance on expansion coord, per-axis scales from ground-truth offset spread)
- Velocity target: u = X₁ − X₀ (closed form, constant along straight path)
- Binary expansion label mapped to Γ₁ ∈ {−1,+1} (symmetric about prior mean; decision threshold = 0 at sampling)
- Training: single flow time t ~ U[0,1] per graph; MSE loss on frontier nodes only
- Sampling: K=10 explicit Euler steps; integrated state stays in frame coordinates
- Training sequence: coarsen a full tree level-by-level (Tℓ⁺¹→Tℓ removes one layer providing ground-truth targets)

## SO(2)-Equivariant GNN (the key inductive bias)

Biological trees have a preferred axis (trees grow up; dendrites perpendicular to cortical surface). Encode rotation-about-axis symmetry:

**Invariant edge features** — decompose displacement rᵢⱼ into axial dᵢⱼ = rᵢⱼᵀû and perpendicular residual ρᵢⱼ = ‖rᵢⱼ⊥‖². The pair (ρᵢⱼ, dᵢⱼ) is SO(2)-invariant. Enrich with branch angles: azimuth ψᵥ (about axis, from incoming parent direction) and tilt φᵥ (cos φᵥ = rᵥᵀû/‖rᵥ‖).

**Local frames** — for node v with grandparent: fᵥ = normalized projection of incoming branch direction wᵥ onto plane ⊥ û; sᵥ = û × fᵥ; frame (fᵥ, sᵥ, û). Head emits frame coordinates (a,b,c); decode C(v) = a·fᵥ + b·sᵥ + c·û. Frames co-rotate with input rotation ⇒ equivariant output; invariant state + co-rotating frame = each offset maps to QC(v).

**Message passing** — EGNN layer (Satorras 2021) with squared distance replaced by eᵢⱼ, NO coordinate update (coordinates read once, never modified). Tree edges only ⇒ prepend every second layer with induced-set attention block (learned per-graph tokens attend to all nodes; acts on invariant features, preserving invariance) so information spans the tree despite depth.

**Root frame**: f₀ aligned during training with the child whose subtree extends furthest along −û; at sampling f₀ is a random azimuth — precisely the SO(2) degree of freedom the model does not fix.

## Conditioning Modes

1. **Unconditional**: sample from noise
2. **Class-conditioned**: one-hot cell-type (7 MICrONS classes: 23P, 4P, 5P-IT, 5P-ET, 5P-NP, 6P-IT, 6P-CT) at every flow step
3. **Morphology-guided (TMD)**: Topological Morphology Descriptor — filtration by path-length/radial distance from root → 0-dim persistent homology → persistence diagrams → persistence images → embedded → supplied at every flow step. TMD primarily controls overall structure rather than fine geometry (branching angles differ most).

## Preprocessing

- Contract all degree-2 paths (keep root, branch points, leaves only) — shortens graph distances for message passing; local branch shape prediction left as future work
- Binarise non-root multifurcations (3-way: insert node; wider: keep 2 thickest children, drops ~1.25% of nodes)
- Root exempt: k ≤ 23 primary dendrites preserved

## Evaluation Protocol (reusable for morphology generation)

- Marginal stats: normalized 1-Wasserstein W₁/σ_ref on axial extent, radial span, max path length, total edge length, branch length, bifurcation angle, contraction ratio, partition asymmetry
- Joint: ∆MMD² on 9-dim morphometric vector + TMD persistence images (baseline-adjusted: subtract real–real MMD²)
- Density (generated in reference support) / coverage (reference represented)
- TMD-conditioned: compare against fixed-seed random derangement of targets (no-conditioning baseline)

## Key Results

| Metric | Ours (21.6M) | SemlaFlow (22.3M) | MorphoGen (32.6M) |
|---|---|---|---|
| Valid tree % | 100 | 76.6 | 100 (via spanning-tree repair) |
| ∆MMD² morph | 0.0393 | 0.2521 | 0.8436 |
| Density / Coverage | 0.876 / 0.798 | 0.389↓ | ~0 |
| Mean norm. marginal W₁ | 0.133 | 0.389 | 1.515 |

- F=64 model (1.57M params, 14–21× smaller) still beats both baselines
- Class-conditioned W₁: 0.170 vs SemlaFlow 0.355
- TMD-conditioned: 100% valid vs 63.2%; target closer in ~91% of comparisons; 97.9% unique samples across seeds
- Scaling: D20 botanical trees 0.617 s/tree vs SemlaFlow 12.317 s (20× faster); W₁ 0.379 vs 1.837
- Known gap: under-generates tall neurons (24.2% vs 33.5% reference >400µm axial extent)

## Implementation Checklist

1. Represent tree as (V, E, P): nodes = branching points + leaves only
2. Build per-level training sequences by iterated coarsening
3. Implement SO(2)-EGNN: invariant edge scalars (ρ, d, cos ψ, sin ψ, cos φ) + local frames; no coordinate updates in message passing
4. Flow match on 4-dim frontier state; Γ ∈ {−1,+1}; threshold 0
5. Sample with 10 Euler steps per level; loop until frontier empty
6. Validate with W₁/σ_ref marginals + ∆MMD² on TMD persistence images + density/coverage

## Activation Triggers

neuron morphology generation, dendritic arbor synthesis, botanical tree QSM, branching structure generator, graph generative model, flow matching 3D, equivariant GNN, MICrONS, TMD persistence, connectome data augmentation
