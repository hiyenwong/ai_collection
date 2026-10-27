---
name: proper-agnostic-learning-mps-ttn
description: Use when learning MPS or TTN states from arbitrary noisy states.
category: ai_collection
---

# Proper Agnostic Learning of Matrix Product States and Tree Tensor Networks

**Source**: Cedillo Vayson de Pradenne & Cotler (Caltech/Harvard), arXiv:2609.30148 (24 Sep 2026). Solves the open problem of **proper** agnostic learning of MPSs (previously only improper learners existed).

## Problem Definition

Given copies of an **arbitrary** density matrix ρ (no structural assumption!) and target bond dimension D, output a state ψ̂ ∈ MPS_D (proper = in the class) with:

⟨ψ̂|ρ|ψ̂⟩ ≥ OPT_D(ρ) − ε

where OPT_D(ρ) = max over bond-D MPS comparators. Copy complexity poly(n, d, D, 1/ε); runtime polynomial in n for fixed d, D, ε.

**Why proper matters**: an improper learner returns a bond-≫D MPS with near-optimal score — but truncating it to bond D can destroy the score. Properness guarantees a genuinely low-complexity description.

## Three-Stage Architecture

### Stage 1: Improper-to-Proper Reduction (relevant subspace)
- Repeatedly call the improper learner on the **residual** ρ_j = Q_j ρ Q_j / μ_j (postselected on the complement of found directions s_1..s_j).
- Each accepted direction carries Ω(ε²) ρ-weight; since tr(ρ)=1, at most m ≤ 2/θ = O(ε⁻²) directions exist.
- Result: compression A = PρP changes every comparator's score by ≤ 2√θ (Theorem 2.2). **The objective is compressed, not the hypotheses.**
- Diagonalize Â ≈ Σλ_j|u_j⟩⟨u_j|, spectral cutoff λ_j > τ reduces coefficient space to ℓ ≤ 1/(τ−ξ) = O(ε⁻¹) dimensions.
- Mixed-state score factorizes: ⟨φ|Â|φ⟩ = max_c |⟨v_c|φ⟩|², v_c = Σ√λ_j c_j u_j → discretize unit sphere in C^ℓ with a ζ/16-net ((80/ζ)^2ℓ points) → finitely many **explicit pure targets** w_c.

### Stage 2: Comparator-Dual Compression (the key innovation)

Define the comparator-dual norm: **∥x∥_{MPS(D)} := sup_{ψ∈MPS_D} |⟨ψ|x⟩|** — measures the largest overlap of x with any bond-D MPS. Two targets close in this norm define nearly the same optimization problem even if far apart in Euclidean norm.

**Theorem 2.4**: every u can be approximated by bond-K MPS ũ_K with

∥u − ũ_K∥_{MPS(D)} ≤ √D/(K+1) · ∥u∥₂

**error independent of chain length n** (no factor of n!). Mechanism — modified left-to-right SVD sweep:
- At each cut, instead of only discarding the singular-value tail (standard truncation), **uniformly shrink ALL retained squared singular values** by the first discarded one: b_j = √(σ_j² − Δ_i), Δ_i = σ²_{K+1}.
- The discarded part then has uniformly bounded singular values → per-cut dual-norm loss ≤ DΔ_i (von Neumann trace inequality, bond-D comparator has Schmidt rank ≤ D).
- Norm bookkeeping telescopes: (K+1)ΣΔ_i ≤ ∥u∥₂² → total error ≤ D·∥u∥₂²/(K+1).
- Trade-off: deliberately loses MORE Euclidean norm to gain system-size-independent comparator-dual control.
- Bonus (Euclidean relative error): bond K = O(D/α) gives squared error within factor 1+α of best bond-D approximation — **chain-length-independent variational compression**.

### Stage 3: Proper Pure-Target Optimization (dynamic program)
For target v (bond ≤ K), build candidate bond-D MPS left-to-right. Cross environment X_i = Σ_s V_i^s X_{i−1}(A_i^s)† captures the entire effect of the processed prefix on the final overlap (X_n = ⟨ψ|v⟩ scalar).
- Φ_A is contractive in trace norm (isometry conditions) → discretize local tensors (net radius h = η/4n) and environments (radius q = η/8n); merge prefixes whose environments share a cell.
- #retained prefixes bounded by **environment net size, not prefix dimension** — kills the exponential.
- Output proper **by construction** (assembled from bond-D isometries; no final rounding step).
- Runtime: (C√n D/η)^{O(KD+dD²)} · poly(d,B,D,1/η).

## Tree Tensor Network Extension
- Heavy-child-last preorder π: every rooted subtree = contiguous interval; every prefix cut crosses ≤ w_T = Δ_T(1+⌈log₂ n⌉) tree edges → bond-D TTN ⊆ MPS_{D^{w_T}} (polynomial bond for fixed D, Δ_T).
- Reverse conversion: MPS bond B → TTN bond ≤ B² (contiguous interval cuts ≤ 2 virtual bonds).
- Comparator-dual compression recurses leaves→root with the same one-step shrinkage; matrix identities (2.12)-(2.13) are graph-independent.

## Branch-Structure Learning
For states |Φ⟩ = Σc_a|ψ_a⟩ with bond-D MPS branches under local non-interference (k-local observables see the incoherent mixture): algorithm returns branches + coefficients with nearly optimal score, allowing interference to grow by prescribed amount only.

## Reusable Patterns
1. **Compress the objective, not the hypothesis** — build a small subspace preserving all comparator scores, then optimize classically inside it.
2. **Comparator-dual norms** — pick the norm induced by the comparison class (∥x∥_C = sup_{φ∈C}|⟨φ|x⟩|); approximations only need to be good in THIS norm, which can be far weaker (and easier) than Euclidean.
3. **Shrink-then-telescope** — uniform downward adjustment of retained spectrum + telescoping budget beats per-site truncation when error must be independent of system size.
4. **Contractive cross-environment DP** — sweep-based optimization retaining only a bounded-dimensional environment matrix; discretize the environment space, deduplicate prefixes by cell.
5. **Measurement reuse across model complexities** — one relevant-subspace construction at D_max answers all D ≤ D_max (bond-dimension sweep for free).
6. **Embedding via heavy-path orderings** — reduce tree-structured classes to chains with polynomial bond blowup D^{O(Δ log n)}.

## Cross-Domain Applications
- Quantum tomography under noise (agnostic = no model assumption on ρ, e.g. thermal/mixed states).
- MPO learning via vectorization (d → d² substitution, Hilbert-Schmidt normalization).
- Classical ML analogue: compress target distributions in a norm induced by a hypothesis class; improper→proper reduction for nets with bounded description length.
- Model selection: reuse one dataset to trace OPT_D(ρ) vs D curve (bond-dimension ablation without extra measurements).

## Key Formulas
| Object | Formula |
|---|---|
| Relevant subspace dim | m ≤ 2/θ, θ=(ε/16)² |
| Coefficient dim | ℓ ≤ 1/(τ−ξ), τ=ε/8, ξ=ε/32 |
| Dual compression | ∥u−ũ_K∥_{MPS(D)} ≤ √D ∥u∥₂/(K+1) |
| SVD shrinkage | b_j = √(σ_j² − Δ_i), Δ_i = σ²_{K+1} |
| Euclidean relative | ∥u−ũ_K∥₂² ≤ (K+1)/(K+1−D) e_D(u)² |
| Env update | X_i = Σ_s V_i^s X_{i−1}(A_i^s)† |
| Net sizes | h = η/4n, q = η/8n |
| Error budget | √(13ε/16) < ε (θ, ξ, τ, ζ split) |

## Pitfalls
- Truncating an improper learner's output to bond D **destroys the guarantee** — near-optimal score ≠ closeness to any bond-D MPS.
- Standard SVD truncation gives per-cut error σ_{K+1} with NO telescoping over n — the uniform shrinkage is essential for n-independent bounds.
- The spectral cutoff (λ_j > τ) is what reduces the net from exp(ε⁻²) to exp(ε⁻¹) targets; skipping it is exponentially slower.
