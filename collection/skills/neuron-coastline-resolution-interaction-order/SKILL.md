---
name: neuron-coastline-resolution-interaction-order
description: "Use when inferring neural mechanism from low-order statistical fits. Scale-indexed decomposition shows apparent interaction order depends on the ruler."
tags: [neuroscience, information-theory, coarse-graining, dendrites, maximum-entropy]
category: ai_collection
---

# How Long Is the Coast of a Neuron? Resolution-Dependent Interaction Order and Computational Capacity

**Source**: Nima Dehghani (MIT McGovern Institute + IAIFI), arXiv:2610.19487, submitted 14 Oct 2026, q-bio.NC + cond-mat.dis-nn + physics.bio-ph. Code: github.com/neurovium/CoastOfNeuron

## Core Claim

Mandelbrot's coastline paradox applied to neural computation: **measurement is a joint property of the object and its ruler**. A direct (pairwise/additive) model that explains most output entropy at a coarse recording scale characterizes an *effective relation among surviving variables* — it does NOT identify the cellular computation that generated it. Apparent **interaction order is not invariant under many-to-one projection**: strictly third-order dependence can appear pairwise after coarse-graining (or vice versa).

This is a formal response to Lynn (Nature Physics 2026) "Simple input–output dependencies explain neuronal activity" (>90% mouse, 62% C. elegans entropy from direct dependencies): predictive adequacy ≠ mechanistic identification.

## The Scale-Indexed Decomposition

At ruler ε with observables X_ε and output Y, define the direct family:

```
Q_{θ,ε}(y=1|x) = σ(b + Σ_i u_i(x_i))     [categorical-additive: arbitrary 1-coordinate functions]
```

Information partition (exact):
- **I_avail = S_tot − S_true = I(Y;X_ε)** — available predictive information
- **I_dir = S_tot − S_dir** — captured by optimal direct model
- **I_higher = S_dir − S_true = E_X[KL(P_ε(Y|X_ε) ‖ Q*_ε(Y|X_ε))]** — conditional-KL residual (non-additive structure)

Two ratios answer DIFFERENT questions:
- **R(ε) = I_dir/S_tot** — fraction of total output entropy explained (Lynn's reported quantity)
- **F(ε) = I_dir/I_avail** — fraction of *surviving* information that is direct

**R ≤ F always. Projection cannot increase I_avail (data-processing inequality), but F can rise toward 100% even as I_avail collapses** — the "denominator trap": a coarse model can be perfect relative to the little information left at its own resolution.

### Closure condition (when does I_higher contract?)
If the projected direct surrogate Q*(y,x)=P(x)Q*(y|x) remains within the direct family at the coarse scale, then KL-contraction guarantees I_higher(Z) ≤ I_higher(X). Without closure, NO universal ordering of I_higher holds.

## Key Constructions (exact enumeration)

### 1. Three-spin projection: order conversion
Fine: P_K(s) ∝ exp(K·s1s2s3)/8cosh(K) — pure third-order coupling, ALL pairwise marginals uniform (pairwise MaxEnt = uniform, entropy 3 bits). Connected info I(3) = 3 − H(P_K); at K=1.8: 0.823 bits.
- Projection x=s1, z=s2∧s3: pairwise MI = 0.261 bits (partial conversion)
- Projection z=1[s2=s3] (parity/XNOR): pairwise MI = 0.823 bits = FULL I(3) — the entire third-order dependence becomes an ordinary pairwise dependency
**Same fine distribution: no pairwise dependence in native coordinates, partial under one projection, complete under another.**

### 2. Branch-to-soma cascade (the neuron example)
Ground truth: P(Y=1|x) = 0.06 + 0.40(x1x2x3 + x4x5x6) — two NMDA-like 3-input coincidence detectors (dendritic branches), 64 states enumerated exactly.

Cascade of rulers:
| Ruler | Observable | I_avail (bits) | I_higher | F (categorical) | R |
|---|---|---|---|---|---|
| 6 contacts | x∈{0,1}⁶ | 0.1567 | 0.0706 | 55.0% | 13.6% |
| 2 branches | B_i=min(Σx,2) saturated | 0.0286 | 0.0011 | 96.1% | 4.3% |
| 1 soma | Z=(B1+B2)/2 | 0.0235 | ~0 | **100.0%** | 3.7% |

**F rises 55%→96%→100% while available information collapses 85%.** At the somatic ruler, one coordinate remains so I_higher=0 *by construction* — the 100% is the denominator trap in sharpest form. The saturation map erases exactly the distinction (2 vs 3 active contacts) on which the triplet gate depends.

Control: asymmetric mixing Z=0.6B1+0.4B2 (electrotonic attenuation) breaks the degeneracy → linear-family F drops 98.9%→78.4%. **Directness is a property of (distribution, coordinates, model family, projection map) jointly — not a label attachable to the neuron.**

### 3. Anatomical vs informational directness
A_ij=1 (monosynaptic) ⇏ I_higher(ε)=0. Counterfactual: logit P(Y=1|x_j,n) = b+αx_j+βn+γx_j·n — anatomy identical for all γ, but γ≠0 makes the contribution context-dependent (Δ_j(n)=α+γn) and pushes the law outside the direct family. NMDA voltage dependence (I_k = ḡ_k·x_k·M(V_loc)·(V_rev−V_loc), M = Mg²⁺ unblock) is the biophysical realization: same contact, different effect depending on local depolarization.

### 4. Sparsity is scale-dependent
Cell-level edge: A_cell_ij = 1[Σ_a A_ij^(ε) > 0]. Resolved graph has MORE edges (|E_ε|≥|E_cell|) but LOWER density whenever χ(ε) < s̄(ε) (compression factor < mean subunit count): ρ_ε/ρ_cell = χ(ε)/s̄(ε). Multi-contact connections clustered on few branches of a many-branched arbor → resolved graph far sparser than cell-level projection while carrying many more edges. **Sparsity, degree, directness, capacity must all be indexed by the ruler at which nodes/edges are defined.**

### 5. Refinement expands approximation space (the inverse direction)
Target: f(x)=σ{2.5[x1x2+x3x4+x5x6+1.2x1x3x5]−1.8}, x~U[−1,1]⁶ (centered inputs — methodological safeguard: zero-mean makes products orthogonal to first-order coordinates, preventing leakage).

- Point neuron (6 linear coords): held-out MSE 0.0437
- Shuffled contacts (18 contacts, 3 subunits, randomized assignment): 0.0393
- Aligned contacts (subunits match pair structure): 0.0309
- Generic sigmoid random features: need width 40 to match 3 aligned subunits

**Organization > contact count**: the gain comes from WHICH inputs share a nonlinear domain, not how many parameters.

Nested sigma-pi hierarchy (24 subunits exposed progressively, I(Y;Φ_n)=I(Y;x) fixed — no new information, only larger hypothesis class H_n⊆H_{n+1}):
- MSE: 0.0421 (n=1) → 0.0152 (n=24), C_approx ∝ n^0.31 [0.30,0.32]
- Participation ratio r_eff: 6.86 → 14.03, scaling ~n^0.24, log-space R²=0.9907

**Refinement moves structure from I_higher into I_dir** (x1x2 is a joint dependence at coarse ruler, a direct coordinate if z12=x1x2 is resolved) WITHOUT changing the target. Exponents characterize this ensemble, not biological universality.

## Methodological Toolkit

### Reading low-order fit claims correctly
1. Compute R AND F — a high F with unstated I_avail is meaningless
2. Check the sampling-geometry caveat (Safaai & Sabatini 2026 "feature leakage"): hippocampal first-order attribution fell 0.75 (empirical) → 0.68 (product-marginal) → 0.46 (balanced weights) at FIXED conditional responses
3. Bound what a high R does prove: I(Y;U|X_ε) ≤ (1−R)·S_tot — with R>0.9, an unobserved dendritic variable can add at most 10% of output entropy **under the same distribution of states** (in-distribution only!)
4. Observational sufficiency test: hold output fixed, ask whether I(Y;X|Z)=0, i.e., P(Y|X)=P(Y|Z) — then perturb (branch-targeted inhibition, input clustering shifts, temporal regime changes) and check whether adequacy persists out-of-domain

### Ruler-specification checklist (before any mechanistic claim)
i) the ruler (which variables resolved), ii) the target observable, iii) the perturbation class of interest, iv) the domain of conditions. Cable theory bound: passive dendrites → superposition → weighted-sum sufficiency holds; active conductances / NMDA / saturation violate it. Point-neuron = weak-input regime, not a computational property.

### For neuro-inspired architecture design
- Don't match cell counts and scalar weights; match contact-to-subunit organization (which inputs share nonlinear compartments)
- Choice: rich internal variables per unit (local interactions) vs simple units + larger network to reconstruct interactions — a biological neuron and artificial unit need not occupy the same computational scale
- Connectome-constrained initialization (MICrONS activity-derived weights + geometry) helps but cannot recover within-cell organization lost to projection

## Related Skills
- [[multi-view-o-information-brain-hoi]] — higher-order information measures
- [[correspondence-score-audit-alignment]] — auditing representational similarity claims
- [[reciprocity-three-way-tradeoff-recurrent-circuits]] — same-day companion paper on connectome reciprocity
- [[atoms-of-thought-eeg-microstates]] — scale-dependent observables in EEG

## Key References
Mandelbrot 1967; Lynn 2026 Nature Physics (the claim being scoped); Schneidman/Berry/Segev/Bialek 2006 + Roudi/Nirenberg/Latham 2009 (pairwise MaxEnt adequacy conditions); Ganmor 2011; Poirazi/Mel 2003 (two-layer neuron); Beniaguev/Segev/London 2021 (single neuron as deep net); Polsky 2004 + Gidon 2020 (dendritic spikes, human L2/3); Safaai & Sabatini 2026 (feature leakage); Schneidman/Still/Berry/Bialek 2003 (connected info); Herz/Gollisch/Machens/Jaeger 2006 (detail vs abstraction balance).
