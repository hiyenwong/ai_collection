---
name: efe-iit-nonequivalence-permutation-networks
description: "EFE与IIT非等价性定理：局部surprisal对应存在，但全局上scalar EFE不能决定revised IIT φs。"
category: ai_collection
---

# EFE–IIT Nonequivalence: Expected Free Energy ≠ Revised IIT System Integrated Information

**Paper**: "Nonequivalence of expected free energy and revised system integrated information in noisy permutation networks" (arXiv: 2610.03735, Katsuaki Tanabe, Kyoto University, Sep 2026). Code/data: Zenodo DOI 10.5281/zenodo.22333135. Validated with PyPhi 2.1.dev (2026 IIT 4.0 formalism).

## Core Theorem (the one-sentence version)

**Predictive equivalence is not counterfactual causal equivalence.** Two binary networks can have *identical complete one-step predictive distributions* (hence identical expected free energy G under any common preference/observation model) yet *different* revised IIT system integrated information φs — because IIT additionally evaluates what happens under causal partition (intervention), which the intact predictive distribution cannot see. Therefore **no universal scalar function φs = f(G) exists**.

## Why This Matters

- Resolves a growing conflation in consciousness/neuro-AI literature (Safron's IWMT, Olesen et al. surprisal-covariation studies, active-inference-agent φ measures): local algebraic similarity between free-energy and IIT formulas does **not** imply quantity equivalence.
- Correlation ≠ identifiability: one counterexample pair (equal G, unequal φs) suffices to rule out any universal mapping, regardless of how well quantities covary empirically.
- Any IIT–FEP synthesis must carry counterfactual causal structure: schematically φs = F(G, 𝒯, s, …) where 𝒯 = causal topology, never φs = f(G) alone.

## The Construction (noisy permutation networks)

n binary units, dynamics indexed by a permutation σ ∈ S_n:
- **Y_i = X_{σ(i)} ⊕ N_i**, with P(N_i=0) = η, 1/2 ≤ η ≤ 1 — each node has exactly one incoming + one outgoing causal edge; changing σ only reroutes causality, keeping local channel noise fixed.
- **Homogeneous state x(b) = (b,…,b)** is permutation-invariant: every σ yields the *identical* predictive distribution Q_η(Y) = η^{m(y)}(1−η)^{n−m(y)} (m(y) = # of ones). Hence identical state-risk EFE: G_σ1 = G_σ2 (Eq. 23); with uniform preferences G₂(η) = n[1−h₂(η)] bits.

**Topology split** (cycle decomposition of permutations):
- Strong connectivity of the whole n-node graph ⟺ σ is a **single n-cycle**. Multicycle permutations (e.g. 2+1, identity 1+1+1) have **φs = 0** (no whole-system integration).
- Single noisy cycle has **φs > 0** for 1/2 < η < 1.
- Combinatorial amplification: only (n−1)! of n! permutations are single cycles → P(single cycle) = 1/n; the fraction of predictively-degenerate-but-zero-φs architectures → 1 as n grows.

## Closed-Form Result (principal analytical contribution)

For a noisy single n-cycle in state 1ⁿ under the 2026 IIT refinement:

**φs⁽ⁿ⁾(η) = min{ 2ηⁿlog₂(2η), −n·log₂η }**  (Eq. 43)

- **Branch A (partition-limited)**: A_n(η) = 2ηⁿlog₂(2η) — strictly increasing in η; from the MIP which severs exactly k=2 actual cycle edges, M = ⌊4n²/7⌋ possible connections (combinatorial theorem, Appendix A).
- **Branch D (differentiation-limited)**: D_n(η) = −n·log₂η — intrinsic differentiation, strictly decreasing; the 2026 refinement's key addition (pre-2026 IIT lacked this branch).
- φs = lower envelope of the two branches; zero at BOTH η=1/2 (pure randomness) and η=1 (determinism — zero differentiation even though partition irreducibility is maximal). This **non-monotonic interior maximum** is the signature of the 2026 differentiation–specification tradeoff.

**Key quantities in surprisal coordinates** (Sec. III local correspondence):
- Intrinsic differentiation: idiff = −log₂p (a pure surprisal, Eq. 14)
- Intrinsic specification: ispec = p(F_U − F_I) where F_I = −log₂p, F_U = −log₂q (Eq. 15)
- Effect irreducibility: φe(θ) = p(F_Pθ − F_I) with partitioned probability r_θ (Eq. 16)
- Under exact inference each surprisal = optimized VFE (F_min = −ln P(o)) → **genuine local free-energy representation exists for all three IIT terms**.

## Reliability Optimization & Asymptotics

- Unique interior optimum η*_n solves −n·log₂η* = 2(η*)ⁿ·log₂(2η*) (crossing of branches).
- Large-n: a·e^a = 2ln2 has positive solution a = ln2 exactly → **η*_n → 1** with first-order form η* = 1 − (ln2)/n + O(n⁻²); joint specified-state probability (η*)ⁿ → 1/2; **φs,max(n) = 1 − 1/[(1+ln2)n] + O(n⁻²) → 1 ibit**.
- Counterintuitive limit: each local causal transmission becomes nearly deterministic while the *joint* specified-state probability stays at ½ — retaining ~1 ibit of intrinsic differentiation near determinism.
- Table: n=2: η*≈0.7720, φs,max≈0.7468; n=3: 0.8271/0.8217; n=4: 0.8611/0.8627; n=5: 0.8841/0.8884; n=10: 0.9368 (φs,max→1).
- **EFE optimization mismatch**: with uniform preferences argmin G₂ = η=1/2 while argmax φs = η*_n > 1/2 — but this is preference-dependent, NOT universal opposition (choose preferred reliability c = η*_n in factorized preferences and the two optima coincide, Eq. 54–55). The real conclusion is *absence of preference-independent identification*.

## Validation (dual-track)

- PyPhi (2026 IIT 4.0): analytical formula reproduced to ≤1.55×10⁻¹⁵ for n=2–5 at 101 η-grid points; one-unit benchmark p*≈0.7440, i_max≈0.4266 ibits reproduced exactly.
- Exhaustive directed-partition enumeration (independent of PyPhi): n=2…8 audited 3→510,313 cut matrices; global min of k/M always = 2/⌊4n²/7⌋, confirming the combinatorial MIP theorem.
- 3-unit exhaustive check: all 6 permutations at η=0.75 — 4 multicycle topologies φs=0, both 3-cycles φs=0.4936 ibits; all 6 share identical G₂≈0.5662 bits.

## When to Use This Skill

- Comparing/connecting IIT with FEP/active-inference frameworks; interpreting claims that "free energy measures integration".
- Designing φ estimators for neural data: a predictive-model-only scalar (EFE, surprisal, MI) is *provably insufficient* — must include partition/intervention structure.
- Understanding the 2026 IIT intrinsic-differentiation refinement and why φs is non-monotonic in reliability.
- Benchmarking PyPhi 2026 formalism with closed-form test systems (noisy n-cycles are exact analytical testbeds).

## Limitations (from paper)

- Minimal analytically-tractable systems, not realistic neural models; homogeneous state chosen precisely for permutation invariance (generic states need not be predictively indistinguishable).
- One-step, system-level φs only (not full distinction/relation structure); no multi-step policies/learning/hierarchy; theorem does not adjudicate IIT vs FEP as theories — only the scalar-mapping constraint.

## Related Skills

- [[iit-infinite-family-exclusion]] — IIT substrate family with provable φ growth (XOR cycles, Lean-verified)
- [[iit-fep-maxcaliber-bridge]] — maximum-caliber bridge construction (this paper constrains such bridges)
- [[closed-form-izhikevich]] / [[mean-field-adaptation-oscillations]] — neural dynamics where EFE-style analyses are applied
