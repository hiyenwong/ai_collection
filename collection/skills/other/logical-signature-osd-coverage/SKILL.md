---
name: logical-signature-osd-coverage
description: Use when designing, evaluating, or compressing finite OSD candidate lists for qLDPC decoding.
trigger: OSD candidate list, logical coverage, logical signature, OSD-0 error rate, coverage miss, selection failure, P_miss P_sel decomposition, combination sweep, gross code, bivariate bicycle decoding, qLDPC post-processing, BP+OSD, dangerous free variables, McNemar decoder comparison, list compression
author: engineering-lion5
category: ai_collection
version: 1.0
license: MIT
related_skills: bf-osd-qldpc-decoding, impulse-decoding-qldpc, frontier-decoder-qldpc, coset-ensemble-decoder-qec, bp-syndrome-flip-qldpc-decoding, lottery-bp-decoding
---

# Logical-Space Theory of OSD: Signature Coverage and the P_L = P_miss + P_sel Decomposition

**Source**: arXiv 2610.24503 (Yun Shang, Academy of Mathematics and Systems Science CAS, Oct 2026). An algebraic theory connecting finite OSD physical candidate lists to logical equivalence classes of qLDPC codes: predicts exactly when a list can succeed, decomposes logical failure into coverage vs selection, and compresses lists while preserving logical coverage.

## Problem It Solves

1. Quantum decoding succeeds iff the correction lies in the error's LOGICAL class (stabilizer degeneracy) — but OSD generates and ranks candidates in the much larger PHYSICAL space. No algebraic description existed of which logical classes a finite list can reach or how that structure predicts failure.
2. Decoder papers report candidate count N_cand or Monte Carlo P_L — neither identifies WHY a list fails: is the true logical class absent (coverage miss), or present but losing the cost comparison (selection failure)?
3. List sizing was ad hoc: the combination-sweep prefix λ had no principled coverage-based sizing rule.

## Component 1 — Logical-Signature Map M_log

- CSS code, X-error decoding: syndrome s = H_Z e. RREF of H_Z under a FIXED, error-independent column ordering gives [I_r | A] with q = n − r free variables; nullspace basis G_F has columns g_j = [A e_j; e_j].
- Decompose the true error e = c_0(s) + G_F e_F (c_0(s) = particular syndrome solution, e_F = free-variable pattern). Every candidate is c_f = c_0(s) + G_F f, f ∈ F ⊆ F_2^q.
- **M_log = L_Z G_F ∈ F_2^{k×q}** (L_Z = logical-Z operator basis) has rank exactly k. Decoding success ⟺ **M_log f = M_log e_F** — pure signature matching. List design becomes a geometric covering problem: cover y_true = M_log e_F with the list's signature set S = M_log(F) ⊆ F_2^k.
- Columns classify free variables: **dangerous** (M_log,j ≠ 0; flipping changes logical displacement) vs **safe** (= 0; flip is a stabilizer in row(H_X)). n_dangerous = #{j : M_log,j ≠ 0}.
- Cost: one offline Gaussian elimination builds M_log; per-shot online cost is O(N_cand · n) once candidates G_F f are precomputed.

## Component 2 — Exact Analytic Distributions (fixed ordering, iid bit-flip rate p)

- Per-column characteristic function factorization + Walsh inversion over F_2^k:
  Pr(Y = u) = 2^{−k} Σ_v (−1)^{u·v} (1−2p)^{|M_log^T v|}.
- **OSD-0 (f = 0) logical error rate**: P_L = 1 − 2^{−k} Σ_v (1−2p)^{|M_log^T v|}; small-p asymptotics **P_L = n_dangerous · p + O(p²)** — the number of dangerous columns is the first-order failure driver.
- Coverage of a list F: P_cover = Σ_{y∈S} Pr(Y = y). Misses via uncovered weight spectrum: P_miss = Σ_w B_w p^w (1−p)^{q−w}, with B_w = #{x : |x| = w, M_log x ∉ S}. Lists containing all weight-0/1 patterns have t_cov ≥ 2, so misses enter at O(p²): P_miss = B_{t_cov} p^{t_cov} + O(p^{t_cov+1}).
- Exact evaluation: 2^k terms per displacement (k ≤ 12 → ≤ 4096), or one fast Walsh–Hadamard pass k·2^k. Validated against Monte Carlo (5×10⁴ shots, max deviation 2.6σ) on HGP [[13,1,3]] (P_miss ≡ 0), HGP [[27,4,3]], BB [[72,12,6]], gross BB [[144,12,12]].
- Structural metrics (Table 1 of paper): gross code q=78, k=12, n_dang=67, Λ_2^greedy=41, |S_full|=635.

## Component 3 — Exact Failure Decomposition P_L = P_miss + P_sel

- Class energy E_y(s) = min cost over candidates with M_log f = y (∞ if class absent). Decoder selects ŷ = argmin_y E_y(s); ties broken by fixed list order (earliest member).
- **P_L = P_miss + P_sel** exactly, with P_miss = Pr(y_true ∉ S) and P_sel = Pr(y_true ∈ S, ŷ ≠ y_true). Holds for EVERY realization of any candidate-based minimum-cost decoder — including syndrome- or BP-dependent orderings (only the exact distribution formulas of Component 2 need fixed orderings).
- Decision margin Δ(s) = min_{y≠y_true} E_y(s) − E_{y_true}(s): Δ > 0 certifies success (offline diagnostic — requires ground truth, not an online statistic).
- Margin algebra for list comparison: Δ_C − Δ_B = δ_true − δ_wrong (energy drop of true class vs best competing class). Adding representatives lowers BOTH energies; improvement depends on relative drops. Of 378 B→C rescues, 351 are strict (Δ_B < 0 < Δ_C) and 27 involve ties — report this split before claiming "margin rescues".

## Component 4 — Coverage-Aware List Construction and Compression

- Combination sweep F_CS(λ) = {0} ∪ all q singles ∪ all pairs of the first λ columns; N_cand = 1 + q + C(min(λ,q), 2). λ controls a pair prefix, NOT a weight threshold. Weight-2 coverage threshold λ*_2 = min{λ : B_2(λ) = 0}. Gross code canonical ordering: **λ*_2 = 78 = q** — the sweep must pair ALL free columns to kill weight-2 coverage failures.
- **Λ_2(M_log)** = minimum column subset T whose pair displacements (plus baseline/singles S_0) cover all pair displacements: counting bound C(|T|,2) ≥ |R| gives |T| ≥ 35 (gross); deterministic greedy — initial pick maximizes covered displacements, growth gain g(c) = |{t ∈ T : M_c ⊕ M_t ∈ U}| — finds **|T| = 41 ≪ λ*_2 = 78**.
- **Coverage-minimal completion (Prop 4)**: each additional candidate contributes ≤ 1 new signature ⇒ N_min = 1 + q + |S_full \ S_0|; choosing one minimum-intrinsic-weight pair |G_F(e_i+e_j)| per missing signature attains it. Gross code: **1 + 78 + 593 = 672 candidates cover the full 635-signature set** vs 3082 for F_CS(q).
- Robustness: over 30 random column orderings, Λ_2^greedy/q ∈ [0.603, 0.795] and B_2 = 0 is always achieved (compression phenomenon persists); |S_full| itself varies 892–1384 and signature identities do NOT persist across orderings (different RREF ⇒ different M_log objects).

## Verified Results (gross code [[144,12,12]], p = 0.01, 5000 paired shots seed 7777, identical RREF + cost rule)

- A: CS(λ=41), 899 cand, |S|=241, B_2=823 → P_L = 13.20%
- F: coverage-minimal, 672 cand, |S|=635, B_2=0 → P_L = 12.42% (McNemar p=0.013 vs A — fewer candidates, better decoder)
- B: signature-aware (all pairs in 41-column Λ_2 set), 899 cand, |S|=635, B_2=0 → P_L = 11.30% (p=1.2e−9 vs F)
- C: full CS(λ=q), 3082 cand, |S|=635, B_2=0 → P_L = 3.78% (p=5.9e−110 vs B)
- B vs C controlled comparison: identical coverage (same 93 coverage-miss shots, P_miss = 1.86% both), yet P_sel = 9.44% vs 1.92% → **3× P_L difference from within-class representative selection alone**. Coverage and representative selection are complementary resources that N_cand alone does not capture.
- Representative-selection heuristics FAILED to beat B: E (max Hamming diversity within collision groups) 11.26% (p=0.91); E2 (spare-pair allocation by training-set selection-failure counts, 2000 training shots) 11.68% (p=0.081). Optimal representative selection at fixed coverage/budget is OPEN.
- Ordering control: same λ=41 engine, only the ordering changed to BP-informed (increasing BP posterior LLR) → P_L 13.20% → 0.34%. Ordering dominates list design; exact distribution theory applies to fixed orderings only.

## When to Use

- Replacing Monte Carlo with exact analytic predictions of OSD-0 / fixed-list logical error rates (fixed orderings, iid noise, k ≲ 14).
- Diagnosing WHY a finite-list decoder fails: run the per-shot P_miss/P_sel decomposition — coverage losses say "grow/reorder the list", selection losses say "improve within-class representatives".
- Compressing OSD candidate lists to a target coverage set (672 vs 3082 at equal coverage on the gross code) and sizing combination sweeps via λ*_2 vs Λ_2^greedy before burning compute.
- Auditing decoder A/B claims: paired samples on identical errors + exact McNemar tests; identical-coverage controls to isolate selection effects.
- Predicting small-p scaling: count dangerous columns (first-order OSD-0 rate) and uncovered-weight thresholds t_cov from M_log alone.

## Pitfalls

- The exact distribution/coverage formulas require FIXED, error-independent column orderings + iid noise; BP-dependent orderings invalidate them (the P_L decomposition theorem still holds per-realization).
- B_2 = 0 (weight-2 coverage) is not full coverage — misses at weight ≥ 3 remain; use t_cov to find the dominant order and B_w spectra to quantify.
- Identical logical coverage does NOT imply identical P_L (B vs C, 3×); any compression must be assessed for within-class representation effects.
- Λ_2^greedy is an upper bound on the exact minimum; the exact Λ_2 optimization is combinatorial.
- Δ(s) requires ground truth y_true — diagnostic only. Zero-syndrome shots and coverage misses are excluded from margin statistics by convention; report exclusions.
- Greedy coverage lists and |S_full| are ordering-dependent objects — re-derive M_log per ordering; do not transfer signature sets across orderings.

## References

- arXiv 2610.24503 — Logical-Space Theory of Ordered-Statistics Decoding for Quantum LDPC Codes (Yun Shang).
- Fossorier & Lin, IEEE TIT 41:1379 (1995) — classical OSD.
- Bravyi et al., Nature 627:778 (2024) — high-threshold bivariate-bicycle (gross) codes.
- Related decoders: Frontier (Leverrier–Urbanke, arXiv:2606.20513), coset-ensemble (Liang et al., arXiv:2606.11076), beam-search (Ye–Wecker–Delfosse, PRX Quantum 7:033002).
