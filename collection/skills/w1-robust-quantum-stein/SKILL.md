---
name: w1-robust-quantum-stein
description: Stein exponent robust to W1 Wasserstein almost-iid sources (arXiv 2609.17309).
category: ai_collection
---

# W₁-Robust Generalised Quantum Stein's Lemma

**Source**: Girardi, Lee, Hayashi & Lami, "Generalised quantum Stein's lemma more robust than ever", arXiv:2609.17309 (Sep 2026). Extends GQSL from exact i.i.d. nulls to any source asymptotically close to i.i.d. in normalized quantum Wasserstein distance of order 1.

## Core Theorem (Theorem 11)

For composite alternatives S satisfying **Assumption 9** — (CC) convex+closed, (TR) tensor-closed, (REP) replacer-stable by full-rank state ⇒ (FR) — and any **W₁ almost-i.i.d. source** (ρ_n) along ρ (W₁(ρ_n, ρ^⊗n)/n → 0):

**lim (1/n) D_H^ε(F^(n) ‖ S^(n)) = D^∞(ρ‖S)** ∀ε∈(0,1), in two forms:
1. **Individual sources**: test may depend on the specific (ρ_n); exponent unchanged.
2. **Universal tests**: exponent attained even when the source sequence is unknown — test depends only on F^(n), S^(n), ε. Robust to noisy/correlated real-world sources.

## Source Hierarchy (strict)

A^CSD ⊂ A^MSR ⊂ A^W₁ ⊂ A^w. W₁ beats MSR (beyond defect-tail constraints); weakly almost-i.i.d. is too weak — converse impossible there ([11, Remark 15]).

## Applications

1. **Compound i.i.d. null** (Thm 16): exponent = inf_{ρ∈R₁} D^∞(ρ‖S).
2. **Arbitrarily varying null** (Thm 21): each site a different ρ^(i)∈R₁. Permutation twirl + **Prop 22**: ‖u_{t,n} − t^⊗n‖_{W₁} ≤ (1/n)√((N−1)log(n+1)/2) reduces arbitrary variation to compound testing; exponent = **inf_{ρ∈conv(R₁)} D^∞(ρ‖S)** — convex hull appears operationally. Requires S closed under permutation twirl.

## Reusable Proof Pattern (§4)

1. **W₁ information-spectrum stability** via dual formulation of W₁ (transport duality) + fattening/distance-cutoffs/blowing-up lemmas.
2. Converse: data processing + convex-combination reduction.
3. **Equiconvergence**: one theorem covers all sources converging to same ρ → universal test.

## Methodological Takeaways

- **Robustify by changing the metric, not the theorem**: express "close to i.i.d." as W₁/n → 0; exponent survives the largest reasonable class.
- **Convex hulls appear when adversaries vary per-site**: twirling + type statistics reduce AV to compound vs conv(R₁) — reusable in compound/AVQC security proofs.
- Assumption 9 (CC+TR+REP) is minimal on the alternative; combines Hayashi–Yamasaki weak-alternative setting with robust nulls ("best of both worlds").
- GQSL ⇒ resource-theory reversibility (incl. entanglement) under asymptotically non-generating ops — now certified for realistic noisy sources.

## Triggers

Robustness of Stein exponents; composite/asymmetric quantum hypothesis testing; arbitrarily varying or compound sources; Wasserstein continuity in quantum info; universal tests; resource theory reversibility; information spectrum methods. Keywords: generalised quantum Stein's lemma, W1 almost i.i.d., compound null, arbitrarily varying source, universal test, regularized relative entropy, permutation twirl.

## Related Skills

- `almost-iid-quantum-information` — foundational W₁ source definitions (arXiv:2605.15114, same first author lineage)
- `private-capacity-superactivation` — companion quantum Shannon result (arXiv:2609.10520)
- `conformal-e-process-changepoint-detection` — classical distribution-free robustness analogue
