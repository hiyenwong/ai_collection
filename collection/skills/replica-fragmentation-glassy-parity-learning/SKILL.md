---
name: replica-fragmentation-glassy-parity-learning
description: "Replica-overlap observables diagnose glassy fragmentation in trained Transformer ensembles."
category: ai_collection
trigger: replica fragmentation, glassy learning dynamics, self-cross gap, Nishimori gap, memorization vs generalization regimes, retreat-recovery cycles, parity learning Transformers, spin-glass overlap for neural nets, ensemble disagreement geometry, training-run replicas, χSG, learning frontier dynamics
---

# Replica Fragmentation and Glassy Dynamics in Parity Learning

**Source**: Han Ma (CPHT, CNRS, École Polytechnique), arXiv:2610.08503 (6 Oct 2026), cond-mat.stat-mech / cond-mat.dis-nn.
**Code**: https://github.com/HanMaPhy/two_learning_glasses

## Core Idea

Independently trained runs sharing the SAME training set, architecture, and optimizer can realize DIFFERENT functions. Treat runs as **replicas** and measure their learned functions with statistical-mechanics overlap observables. This exposes a finite-size "glass-like" fragmentation — confident but mutually inconsistent predictions — invisible to single-run accuracy curves. The framework cleanly separates three learning regimes: **memorization**, **retreat** (loss of acquired generalization), and **recovery**, each with a distinct overlap signature and residual geometry.

## The Task (gauge-fixed syndrome decoding)

Binary domain-wall string b ∈ {0,1}^D, L = D+1 outputs; target at position j is the running parity:
- `y_j^bit(b) = ⊕_{i≤j} b_i`, or in spins `σ_j^true(s) = ∏_{i≤j} s_i` (a degree-j Walsh character / open Z₂ Wilson line).
- Equivalent to repetition-code syndrome integration with fixed boundary: `e_{j+1} = e_1 ⊕ b_1 ⊕ ... ⊕ b_j`.
- Output position j = both string length and algebraic degree → position-resolved diagnostics of WHERE learning fails (the "learning frontier" separates aligned small-j from uncertain tail).

Transformer: 8 encoder layers, d=16, 4 heads, FFN width 64, GELU, no dropout; 2.7×10⁴ params; AdamW lr 2e-3, wd 1e-4, batch 128. Soft spin readout: `σ̂_{r,j}(b) = -tanh(z_{r,j}(b)/2) ∈ [-1,1]` (magnitude = confidence).

## The Observables (the reusable protocol)

Three overlaps, averaged over replicas r, inputs b, positions j:
- **Truth alignment**: `m = ⟨σ̂_{r,j} σ_j^true⟩` (correctness-weighted confidence)
- **Self-overlap / confidence**: `q_self = ⟨σ̂_{r,j}²⟩` (EA-like; checkpoint confidence)
- **Cross-replica overlap**: `q_cross = ⟨σ̂_{r,j} σ̂_{r',j}⟩_{r≠r'}` (ensemble consensus)

Two derived gaps:
- **Nishimori gap**: `ΔN = q_self − m` — confidence in excess of truth. On the Nishimori line (posterior-matched replicas) q_self = m; positive ΔN = confident misalignment.
- **Self–cross gap**: `χSG = q_self − q_cross` — EXACTLY the prediction variance across replicas; measures fragmentation of the learned-function ensemble.

### Regime classification table (m–q coordinates)

| Regime | m | q_self | q_cross | ΔN | χSG | SP analogue |
|---|---|---|---|---|---|---|
| Retrieval (generalization) | ≃1 | ≃1 | ≃1 | ≃0 | ≃0 | Ordered |
| Uncertain | ≃0 | ≃0 | ≃0 | ≃0 | ≃0 | Paramagnetic |
| Systematic error | ≪1 | ≃1 | ≃1 | >0 | ≃0 | Spurious retrieval |
| **Memorization** (fragmented non-retrieval) | ≃0 | ≃1 | < q_self | >0 | >0 | Spin-glass-like |
| **Retreat** (fragmented partial-retrieval) | 0<m<1 | O(1) | < q_self | — | >0 | Mixed order+glass |

## Key Empirical Findings

1. **Memorization (small N)**: All replicas interpolate the training set (train acc = 1, q_self ≈ 0.985) yet tail held-out accuracy = chance (0.5004) with χSG large. Training set has full GF(2) rank — the data DETERMINES the rule, but gradient descent doesn't recover it. Persistent over time.
2. **Retreat (large N)**: Runs first generalize (A_block ≥ 0.8) then FALL below 0.5 while confidence stays high — then often recover; repeated retreat-recovery cycles. Unlike grokking: train and test accuracy improve TOGETHER before reversal. 98% of retreat-time observations have |ΔN| ≤ 0.05 (brief confidence lags), vs. small-N where ΔN > 0.05 persists while block acc < 0.1.
3. **Position-resolved retreat**: Truth alignment is lost FIRST at large j (longer strings / higher degree); the truth frontier j_m* and confidence frontier j_q* recede then re-advance in step. At retreat onset j_q* > j_m* — confidence persists past lost alignment.
4. **Fragmentation is NOT tied to overparameterization**: appears in overparam (6–35×) small-data ensembles AND in the largest retreat ensemble (18× more supervised bits than params).
5. **Hidden progress**: aligning runs at first threshold crossing, m and q_self rise together 20+ epochs BEFORE block accuracy crosses 0.8 (at τ = −20: m = 0.741 while block acc = 0.394) — partial order invisible to hard-threshold accuracy.
6. **Architecture control**: 16-layer residual CNN generalizes with ~3× less data (N_c ≈ 349 vs 1111 at L=12) and does NOT retreat; Transformer learns abruptly, retreats, recovers. Crossover N_c grows with string length (1111 → 2585 → 9298 for L=12→16→20), width w also grows (0.26 → 0.57).

## Residual Geometry (decomposition + hierarchy tests)

Decompose truth-aligned outputs per replica: `u_{r,j}(b) = m_r + δµ_{r,j} + ε_{r,j}(b)` (scalar alignment / position-profile / input-dependent residual). Then `Q_raw = mm^T + C^prof + W` where W holds input-dependent residual covariance.

- **gap(A) = mean diag − mean off-diag**; connected gap and W's share: retreat keeps 77% of connected gap in W; memorization keeps 99% (scalar alignment explains almost nothing).
- **Normalized residual cosine** `R^W_{r,s} = W_{r,s}/√(W_{r,r}W_{s,s})`; distance d = 1 − R^W; average-linkage hierarchical tree.
- **Tree statistics**: cophenetic correlation r_coph, tree fit R²_tree, near-ultrametric fraction P(δ_um < 0.1) (δ_um = (q2−q1)/(q3−q1) per triple).
- **Obtuse-pair fraction** `P(R^W < 0)`: pairs whose residuals ANTI-correlate — where one replica is better than its average, the other is worse.

**Joint separation** (tail window j ≥ 2L/3): obtuse-pair fraction × near-ultrametric fraction plane puts memorization / retreat / recovery in three NON-OVERLAPPING regions. Retreat: obtuse fraction 0.058–0.259 (robust to split-half evaluation), anti-correlated residual component is its signature. Memorization: narrow equidistant off-diagonal (random-energy-like), lowest near-ultrametricity. Recovery: broad but non-negative R^W.

Controls: entry-permutation and row-centered matrix randomizations give (0.20, 0.04, 0.13) / (0.50, 0.25, 0.10) vs. observed (0.862, 0.743, 0.291) — tree structure is real, not an artifact.

## Targeted Intervention (diagnosis → action)

Retreat is an optimization-dynamics problem, not a data problem. **Learning-rate decay after acquisition**: hold η₀ until held-out block accuracy first reaches 0.8 at update t*, then cosine-decay to η_min = 0.02·η₀. In 84 matched pairs (identical data/init/batch stream through t*): retreat in 29+26+29 constant-arm runs vs. 5 intervention-only; 79/84 intervention runs end high-accuracy vs. 59/84 constant. Matched-pair design isolates the update-scale effect cleanly.

For memorization, the fix is data (crossover at N_c), not optimization.

## When to Use

- Auditing ensemble/model-soup/committee reliability: high q_cross is a NECESSARY condition for run-level determinism; χSG quantifies function-level seed sensitivity even when accuracies match.
- Diagnosing nonmonotonic test-loss ("loss of generalization") cycles: distinguish brief ΔN lags (retreat) from sustained confident misalignment (memorization).
- Position-graded tasks (sequence length, algebraic degree, distance): map the learning frontier j*(τ) to see WHERE knowledge lives and how it erodes.
- Model selection beyond accuracy: select checkpoints/times by low χSG + ΔN ≈ 0.
- Extensions: 2D surface-code neural decoders — define overlaps on stabilizer-equivalence classes; conserved-charge inference from measurement records.

## Implementation Notes

- Replica protocol: R runs (16–269 in paper), shared FIXED training set = quenched disorder; only init + minibatch order vary. Endpoint classes conditioned on history: retreat = reached 0.8, now < 0.5; recovery = fell then returned ≥ 0.8.
- Soft spin from logits via −tanh(z/2) makes overlaps scalar products; uncertainty fraction f_uncertain(ζ) = fraction |σ̂| < ζ is a threshold-free complement.
- Jackknife over replicas for errors on gap statistics (pair overlaps share replicas); bootstrap for gap CIs; n=47 matched subsets for tree statistics.
- Appendix A: at fixed epoch, retreat vs. stable replicas show NO significant difference in gradient norm / λ_min / λ_max (Hessian via Lanczos HVPs) — retreat is a trajectory phenomenon, not a detectable endpoint basin.

## Related (in collection)

- [[grokking-epoch-double-descent-qnn]] — delayed generalization in QNN; contrast: here train/test rise TOGETHER, and overlap observables (not accuracy) do the diagnosis.
- [[dense-auto-hetero-associative-disentanglement]] — overlap/magnetization machinery for Hopfield modules (memory side); this paper applies it to learned functions.
- [[statistical-mechanics-quantum-decoding]] — Nishimori-line thresholds for codes; here ΔN is the empirical learning-side analogue.
