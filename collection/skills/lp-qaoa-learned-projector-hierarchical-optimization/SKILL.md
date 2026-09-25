---
name: lp-qaoa-learned-projector-hierarchical-optimization
category: ai_collection
description: Use when optimizing QAOA on hierarchical problems. Learned projectors.
version: "1.0.0"
source: https://arxiv.org/abs/2609.28888
source_title: Learned-projector QAOA for hierarchical optimization
authors: Kangyun Zhou, Dong An, Jin-Peng Liu
published: 2026-09-24
categories: quant-ph
trigger_words:
  - QAOA
  - learned-projector mixer
  - hierarchical optimization
  - frozen-stage stability
  - projector mixer
  - BCST
  - tunnelling suppression
  - energy gap
  - variational quantum optimization
---

# LP-QAOA: Learned-Projector QAOA for Hierarchical Optimization

**arXiv:2609.28888** — Kangyun Zhou, Dong An, Jin-Peng Liu (Tsinghua/PKU, Sep 2026)

## Overview

Many optimization problems reveal inexpensive structural information before requiring costly final evaluation, whereas conventional QAOA applies a single aggregate objective throughout. **LP-QAOA** is a multistage protocol that freezes optimized circuits and uses their output states to define later projector mixers — moving quantum optimization from flat to hierarchical.

## Core Construction

If stage j prepares |Phi_j>, the projector onto this learned state is Pi_Phi_j = |Phi_j><Phi_j|, and the next stage's learned-projector (LP) mixer uses as generator:

```
M_j = R_Phi_{j-1} = I - |Phi_{j-1}><Phi_{j-1}|,   j >= 2
```

- Stage 1 uses a prescribed mixer M_1 (transverse-field or XY) with diagonal phase Hamiltonian C_1, depth p_1, classical loss L_1
- Each later stage j chooses C_j, p_j, L_j; its mixer is built from the preceding optimized state
- **Circuit realization**: uncompute with A_j dagger, apply selective phase to |0^N>, re-prepare with A_j (Grover-style reflection around the frozen preparation)
- **Recursive nesting**: expanding A_j reveals the frozen stage-j circuit whose LP mixer is built from A_{j-1}; starred parameters fixed

## Strict vs Soft Hierarchy

- **Strict**: stage ground-state sets nest: `G_m subset ... subset G_1`, G_j = argmin_z C_j(z). Early stage concentrates probability in the feasible subspace -> later phase separators may OMIT the corresponding constraint terms, cutting circuit cost per layer
- **Soft**: exact nesting replaced by a measurable enrichment criterion — coarse-stage state assigns greater probability to a prespecified low-energy set of the final objective (validated on stochastic block model instances, N=24 two-community)

## Theorem 2.1 — Frozen-Stage Stability

Error propagation through successive frozen stages. If ideal parameters at stage j prepare the target within error eps_j, and e_j = distance between actual and ideal state after stage j, with B_j = sum of |mixer angles| at an LP-mixer stage (B_j = 0 for fixed-mixer stage):

```
e_m <= sum_{j=1..m} eps_j * prod_{k=j+1..m} (1 + B_k)
```

- The 1+B_j factor reflects the two channels of an imperfect frozen preparation: input-state carryforward + each LP-mixer layer contributing at most |angle| x that error
- **Use**: quantitative basis for ALLOCATING preparation accuracy across the hierarchy — later-stage amplification factors (1+B_k) tell you which eps_j matter most

## Theorem 2.2 — EC3 Feasible-Subspace Gap

Hierarchical Exact Cover 3 (NP-complete) on N bits, feasible set F of configs satisfying m disjoint clauses, |F| = L = 2^N (3/8)^m. Interpolation H_F(s) = (1-s)(I - |F><F|) + s*C_F has minimum gap:

```
g_min = q_N * L^{-1/2} (1 + o(1)),   q_N in [inverse-poly, constant]
```

vs superexponentially small gaps for local mixers: transverse-field ~ 2^{-Theta(N log N)} (Altshuler-style localization, high-order tunnelling between configs separated by Theta(N) bit flips), block-XY ~ exp[-c N log N + O(N)].

**Mechanism**: the learned projector couples any two configurations with nonzero reference amplitudes DIRECTLY (coupling magnitude = product of amplitude magnitudes), irrespective of Hamming distance. Local mixers (transverse-field: 1-bit flips; XY: pairwise exchanges) connect distant configs through long sequences of intermediate moves, suppressing tunnelling to high order.

## Why It Works — Three Consequences

1. **Resource reallocation**: early stages use cheap structural Hamiltonians; expensive final-objective applications reserved for later refinement. Trades mixer resources (frozen prep + inverse + register-wide selective phase) for guided search
2. **Nonlocal mixing**: direct coupling across the feasible set (see Theorem 2.2)
3. **Trainability**: (a) stagewise optimization confines each classical search to 2*p_j current-stage angles with earlier parameters fixed — lower-dimensional than joint optimization; (b) projector mixing avoids exponential loss concentration that standard QAOA suffers at large depth on typical random graphs (MaxCut contrast: standard QAOA exponentially small loss variance vs Grover-mixer QAOA inverse-polynomial lower bound — LP-QAOA inherits the projector-mixer structure)

## Numerical Results (BCST)

**Block-constrained spin tiling (BCST)**: each site = block of binary variables with local cardinality constraint; adjacent sites must not select the same label; each label appears a prescribed total count; final weighted objective ranks satisfying assignments (frequency-assignment interpretation). Each LP-QAOA stage = one level of the strict hierarchy.

- Higher probability of sampling the unique optimum vs two-stage LP-QAOA and block-XY QAOA baselines
- Lower estimated logical-resource cost (RTS99 x RU metric for 99% target probability)
- Stronger normalized gradients at depths 26/29/32 on N=30 instances (finite-depth trainability)
- Ablations: BOTH the optimized intermediate preparation AND its use as projector reference contribute to gains
- SBM (soft hierarchy): approximate structural information also improves optimum-finding probability

## Recipe

```
1. Decompose the problem into a constraint hierarchy: cheap structural objectives first, expensive final objective last (strict nesting ideal; soft enrichment acceptable)
2. Stage 1: standard QAOA with prescribed mixer on C_1; optimize angles, freeze circuit A_1
3. Stage j >= 2: build M_j = I - |Phi_{j-1}><Phi_{j-1}| via A_{j-1}, uncompute-select-phase-reprepare; drop constraint terms already concentrated by earlier stages from C_j
4. Budget eps_j per Theorem 2.1: weight accuracy toward stages with large prod_{k>j}(1+B_k) amplification
5. Optimize current-stage angles only (2*p_j dims), freeze, recurse
```

## Activation

Use when: running QAOA on problems with hierarchical/nested constraints (scheduling, frequency assignment, tiling, CSP with levels); designing nonlocal mixers; fighting small-gap/tunnelling-suppression or trainability (loss concentration) pathologies in variational quantum optimization; allocating circuit-accuracy budgets across staged quantum algorithms.

## Pitfalls

- LP mixer costs the frozen preparation + its inverse + a register-wide selective phase per layer — the trade is more mixer resources for fewer expensive cost-Hamiltonian applications; worth it only when the hierarchy is real
- Stability bound degrades multiplicatively: large optimized mixer angles (B_j) amplify earlier-stage errors through (1+B_k) products — cap angles or improve early-stage accuracy
- Strict nesting G_m subset ... subset G_1 must actually hold for constraint-dropping to be safe; with soft hierarchy verify the enrichment criterion before omitting constraint terms
- Learned-projector gap result (Theorem 2.2) is proven for the hierarchical EC3 construction — do not assume inverse-poly gaps transfer to arbitrary instances
- Simulations were state-vector on modest N (24-30); the RTS99 x RU logical-cost estimates are projections, not hardware demonstrations
