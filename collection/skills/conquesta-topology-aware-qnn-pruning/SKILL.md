---
name: conquesta-topology-aware-qnn-pruning
description: Use when pruning QNNs for NISQ. Compiler-aware mask search.
category: ai_collection
version: "1.0.0"
source: https://arxiv.org/abs/2610.23415
source_title: "ConQUESTA: Topology-Aware Post-Training Structural Pruning of Quantum Neural Networks"
authors: Saim Rehman, Muhammad Shafique
published: 2026-10-16
arxiv_id: "2610.23415"
categories: quant-ph, cs.AR, eess.SY
trigger_words: [QNN pruning, quantum neural network compression, compiler-aware pruning, entangler selection, mask search, NISQ deployment, transpilation cost, NSGA-II, structural pruning, post-training compression]
---

# ConQUESTA — Topology-Aware Post-Training Structural Pruning of QNNs

Post-training pruning of a **trained** quantum neural network (parameterized circuit) for
deployment on sparse-coupling hardware: remove whole trainable two-qubit entanglers so that
transpiled 2Q-gate count, SWAP count, and depth drop while validation accuracy stays within
an explicit constraint. Core idea: **pruning gains are non-additive** — removing a SET of
gates changes placement and routing in ways singleton scores cannot predict, so evaluate
complete masks after full transpilation, not summed per-gate savings.

## When to Use

- You have a trained PQC/QNN and must deploy it on hardware with sparse coupling (line, ring,
  heavy-hex, grid) where routing inserts SWAPs.
- You want compiled-resource savings (2Q gates / SWAPs / depth) at constrained accuracy —
  NOT a retraining-free accuracy gain.
- Do NOT use for design-time architecture search (use QuantumNAS-style QAS), for
  angle-threshold pruning with fine-tuning (NR-QNN), or as an error-mitigation technique.

## Pipeline (7 steps)

1. **Task saliency** per trainable entangler i:
   `I_i = E_(x,y)[ |theta_i * dL/dtheta_i| ]` — first-order importance of each gate parameter.
2. **Leave-one-gate-out transpilation**: transpile the circuit WITHOUT gate i on each scoring
   topology b and transpiler seed s; record normalized deltas Δ2Q/2Q0, ΔS/max(S0,1), ΔD/D0.
   Clip negative deltas to zero (removing a gate can INCREASE cost).
3. **Compiler cost**: `C_i = 0.60*d2Q + 0.25*dS + 0.15*dD` (weights = deployment policy).
   Robust aggregation: median across transpiler seeds, then **75th percentile across topologies**
   (pessimistic — cost must hold on the worst reasonable map).
4. **Joint pruning priority** after min–max normalization: `P_i = C_i * (1 - I_i)`.
   High P = physically expensive AND task-insensitive → prune candidate.
5. **Diversified screening pool** (cap K=20): union of four views — joint priority,
   high-cost-only, low-saliency-only, gradient-only joint view. Diversity prevents one
   heuristic from dominating the candidate set.
6. **Fixed-cardinality joint mask search** (NSGA-II) over objectives (validation accuracy,
   2Q reduction, depth reduction, SWAP reduction). Every candidate MASK is transpiled as a
   whole on line/ring/heavy-hex (opt level 3, several transpiler seeds); score
   `RT1(M) = mean_b [0.60*e_r2q + 0.25*e_rsb + 0.15*e_rdb]`.
7. **Constraint-first selection + fixed-mask recovery**: feasible means
   `A_val(M) >= A_val(dense) - 0.01`. Select max RT1 among feasible; if none, minimize
   violation first, then maximize RT1. Recover with direct fine-tuning of SURVIVING parameters
   only (8 epochs, lr 0.008, early stopping OFF) — the mask and its compiled savings are frozen.

## The Central Lesson

**Singleton savings do not sum.** A gate that looks cheap alone can be expensive in
combination (or vice versa) because placement/SWAP insertion is a global property of the
surviving circuit. One-shot ranking by `P_i` (the "one-shot comparator") is the right
baseline and is consistently beaten by joint search at matched sparsity and recovery budget:
+3.5/+1.7/+8.9 pp RT1 on 6q-BC/8q-Digits01/4q-Iris, 8 seeds, 55% pruning.

## Honest Claim Boundaries (adopt this scoping)

- Claim **resource efficiency at comparable accuracy**, never accuracy dominance (on some
  benchmarks simple baselines match search accuracy; Iris compiler-only is 0.42 pp HIGHER).
- Recovery restores the **validation constraint**, not test-set gains (test deltas were
  +0.88/-0.52/-1.25 pp — seed variance dominates).
- NSGA-II vs Beam search: 92.87±3.40 vs 92.54±3.35 acc (p=.56) — optimizer choice is an
  implementation detail, NOT an algorithmic claim.
- Unseen-topology transfer (grid) retains savings but is NOT topology invariance; noise
  effects are benchmark-dependent → this is a resource-efficiency method, not error mitigation.
- Held-out test data must never touch mask/optimizer/recovery/policy selection.

## Scaling Behavior

Screening caps the search: with fixed k=4 and N=12→132 prunable entanglers, raw mask space
C(N,4) grows 495→12.08M (24,400×) but evaluated masks grow only 189→305 (≈1.62×;
exactly 305/189=1.614). Explored fraction collapses 38.18%→0.0025%; per-mask compile time
becomes the next bottleneck (1.40→10.66 s/mask). Screening transpilations (leave-one-out:
N calls) are cheap next to search transpilations (~570→919 whole-mask calls).

## Pitfalls

- **Negative compiler deltas exist**: pruning a gate can worsen routing — clip Δ to [0,∞).
- **Non-additivity**: never predict mask savings by summing leave-one-out deltas; only
  whole-mask transpilation is ground truth.
- **Transpiler nondeterminism**: fix transpiler seeds and aggregate with median (across
  seeds) + 75th percentile (across topologies) or cost estimates will be noisy.
- **Fixed-ratio scaling is open**: at a fixed 55% pruning RATIO, k grows with N and the
  K=20 pool cap breaks past N≈56-132 — the paper's scaling claim is fixed-k only.
- **Compile-cache illusion**: zero cache hit rate in their scaling runs — growth containment
  comes from screening, not caching.
- **Policy weights are a knob, not an optimum**: re-scoring stored masks under uniform /
  depth-oriented (.40/.20/.40) / routing-oriented (.40/.40/.20) policies shifts which resource
  is saved (Δ up to ±3.8 pp on that axis) with ≤0.44 pp mean validation shift; masks are
  stable (Jaccard ≥ .93 at 55%).

## Verified Numbers (2026-10-20 session, arithmetic re-derivation)

All combinatorial table values re-derived exactly: C(12,4)=495, C(30,4)=27,405,
C(56,4)=367,290, C(90,4)=2,555,190, C(132,4)=12,082,785; explored fractions 38.18%/0.0025%;
feasibility 16/24=66.7%→22/24=91.7%; Digits01 near-miss 99.0−98.61=0.39 pp; RT1 weights sum
to 1. **One rounding nit:** abstract's "1.62×" for evaluated-mask growth is exactly
305/189=1.614 (rounds to 1.61×) — immaterial, underlying values consistent.

## Alternatives & Positioning

| Method | Start point | Distinction |
|---|---|---|
| CompVQC (ICCAD'22) | QNN | compiler-aware compression levels + ADMM |
| NR-QNN | QNN | angle-threshold pruning + fine-tune |
| QCP'26 (ISCAS) | circuit | routing-aware local controlled-rotation removal |
| QuantumNAS (HPCA'22) | design | architecture + mapping co-search |
| **ConQUESTA** | **trained QNN** | **task/compiler screening + joint fixed-cardinality mask search, whole-mask transpilation** |

Position it as a **post-training complement to QAS**, not a replacement: freeze the trained
model, search only masks over existing trainable entanglers, then one-time offline recovery.
