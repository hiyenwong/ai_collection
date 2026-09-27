---
name: qldp-entanglement-breaking
description: Use when quantum privacy clashes with entanglement needs.
category: ai_collection
trigger_words: quantum local differential privacy, QLDP, entanglement-breaking, privacy threshold, private quantum learning, sample complexity lower bound, Gurvits-Barnum ball, depolarizing composition
arxiv: 2609.13418
---

# High Quantum Local Differential Privacy Breaks Entanglement

arXiv:2609.13418 (Bhalerao, Nuradha, Leditzky — UIUC/IQUIST, Sep 2026)

## Core Result: Privacy-Entanglement Incompatibility Threshold

Every ε-QLDP channel N: L(A)→L(B) with d = dim A is **entanglement-breaking** whenever:

```
ε ≤ log(d / (d−1))
```

- Qubit input (d=2): threshold is **ε ≤ log 2 ≈ 0.693**
- The constant is **optimal**: for every η>0 there exist non-entanglement-breaking channels with ε* < log(d/(d−1)) + η
- Interpretation: if a protocol must preserve entanglement with a reference system, choosing ε below this threshold is **impossible** — strong privacy and entanglement preservation are mutually exclusive at this boundary

## QLDP Definition (operator form)

Channel A is (ε,δ)-QLDP iff for all states ρ,σ and all POVM effects 0 ≤ M ≤ I:

```
Tr[M A(ρ)] ≤ e^ε · Tr[M A(σ)] + δ
```

**Privacy parameter computation (Lemma II.2)**: if m·I ≤ N(ρ) ≤ u·I for all ρ, and the bounds are attained by some (ρ0, σ0, P), then ε*(N) = log(u/m) exactly.

## Approximate Version

If N is (ε,δ)-QLDP with ε ≤ log(d/(d−1)), there exists entanglement-breaking M with:

```
∥N − M∥⋄ ≤ (d−1)·δ
```

High-privacy channels are diamond-close to measure-and-prepare channels.

## Bounded Reference Systems

Requiring only r-dimensional reference entanglement: every ε-QLDP channel is r-entanglement-breaking when ε ≤ log(r/(r−1)). ε ≤ log 2 breaks entanglement with any qubit reference regardless of input dimension.

## Composition with Entangled Inputs

Tensor products of high-privacy channels (εi < log(di/(di−1))) acting on **entangled** joint inputs with **global** measurements remain QLDP with:

```
ε_comp = Σᵢ log(γᵢ/βᵢ)
γᵢ = dᵢ[dᵢ − (dᵢ−1)e^(−εᵢ)] / [1 + (dᵢ−1)e^(−εᵢ)]
βᵢ = dᵢ[dᵢ − (dᵢ−1)e^(εᵢ)] / [1 + (dᵢ−1)e^(εᵢ)]
```

n identical qubit channels: ε_comp = n·log[(2e^ε−1)/(2−e^ε)] ≈ **3nε** for small ε.

## Dequantization via Privacy (Learning Theory)

**Simulation theorem**: any binary-output protocol using arbitrary quantum memory on outputs of an entanglement-breaking channel ≡ single-copy measurements + classical memory on unprocessed inputs.

Consequences (privacy noise kills quantum-memory advantage):
- Purity testing under local high-privacy noise: **T = Ω(2^{n/2})**
- Bipartite product testing (local dim q): **T = Ω(q^{n/4})**
- Single global private channel on entire input: **T = Ω(4^n)**, **T = Ω(q^{2n})**

Known single-copy lower bounds apply — quantum memory gains are eliminated by strong local privacy.

## Geometry (Gurvits-Barnum Connection)

The optimal threshold = where the transpose-depolarizing channel's Choi state crosses the **Gurvits-Barnum separable ball** around I_AB/(ab):

- GB ball radius: ∥ρ − I_D/D∥₂ ≤ 1/√(D(D−1)) ⇒ separable
- Channel N is entanglement-breaking if ∥J(N) − J(Δ)∥₂ ≤ 1/√(ab(ab−1))
- At threshold t₀ = −1/(d²−1): distance exactly equals GB radius, ε*(T_{t₀}) = log(d/(d−1))
- Depolarizing mix N_p = (1−p)Δ + pN is entanglement-breaking whenever **p ≤ 1/(ab−1)**, with ε*(N_p) ≤ log(1 + pb/(1−p))

## Methodology

1. Compute the channel's optimal privacy parameter via extremal eigenvalue ratio: ε* = log(u/m)
2. Compare ε* against log(d/(d−1)) — below ⇒ entanglement-breaking (no entanglement survives)
3. For protocols needing entanglement: enforce ε > log(d/(d−1)) as a hard design constraint
4. For n-fold composition with entangled inputs: use the γ/β formula, not naive ε·n sum (gives ~3nε)
5. To dequantize a quantum-memory learner: insert local high-privacy noise per copy, then invoke single-copy lower bounds
6. Geometric sanity check: verify Choi state stays outside the GB separable ball to preserve entanglement capability

## Use Cases

- Choosing ε in quantum DP deployments that must preserve entanglement resources
- Proving sample-complexity lower bounds for private quantum learning
- Privacy auditing of quantum channels: entanglement-breaking test ⇔ high-privacy test
- Designing noise levels that intentionally strip quantum memory advantages
- Channel architecture: separating privacy layer (EB) from entanglement layer

## Relationship to Complementary Result

Dual of [[entanglement-quantum-differential-privacy]] (arXiv:2601.19126): there, entanglement in INPUT states enhances privacy beyond thresholds (phase transition in privacy leakage vs entanglement entropy). Here, high privacy in the CHANNEL destroys entanglement. Together: entanglement can be a privacy resource at the state level, but strong privacy at the channel level forbids entanglement transmission — a fundamental asymmetry between state-level and channel-level privacy.

## Key Formulas Summary

| Quantity | Formula |
|----------|---------|
| EB threshold (input dim d) | ε ≤ log(d/(d−1)) |
| Qubit threshold | ε ≤ log 2 |
| Approximate EB distance | ∥N−M∥⋄ ≤ (d−1)δ |
| r-reference threshold | ε ≤ log(r/(r−1)) |
| n-qubit composition | ε_comp ≈ 3nε |
| GB separable ball | 1/√(D(D−1)) |
| Depolarizing EB point | p ≤ 1/(ab−1) |
| Privacy of mix | ε* ≤ log(1 + pb/(1−p)) |
