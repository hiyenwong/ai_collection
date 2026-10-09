---
name: entangled-hopfield-projector-memory
description: Use for entangled-state quantum Hopfield memory.
category: ai_collection
trigger_words: [entangled associative memory, quantum Hopfield, projector-sum Hamiltonian, dimer singlet covering, valence bond memory, truncated projector construction, quantum memory capacity, Mattis overlap quantum]
---

# Entangled Hopfield Projector Memory

**Paper**: arXiv:2609.28726 (23 Sep 2026) — Hu, Agarwal, Martin (UChicago / Argonne). "Associative Memory for Quantum Entangled States"

## Core Idea

Generalizes the Hopfield model so that stored memories are **intrinsically entangled many-body states** (dimer-singlet / valence-bond coverings) rather than classical bit strings. Quantum effects are not just in dynamics — the *stored information itself* is quantum. Key result: storage capacity scales as **O(N³/log N)**, far above the linear scaling a naive classical analogy would suggest — a quantum advantage from moderate entanglement.

## Method: Truncated Projector-Sum Construction

### Step 1 — Exact projector Hamiltonian (unworkable baseline)
Encode K orthogonal memories as degenerate ground states:

```
H = −Σ_μ |ψ_μ⟩⟨ψ_μ|  (energy −1 ground manifold, K-fold degenerate)
```

Problems: operator weight up to N; ground-state degeneracy means any superposition of memories is also a memory (un-selectable).

### Step 2 — Truncate at order p in local operators
Expand projectors into products of local spin operators and keep terms up to order p. This lifts degeneracy and bounds operator weight. Stored patterns become *approximate* ground states, but selection becomes possible.

**Classical case check**: applied to product states |ξ^μ⟩ = ⊗|ξ_i^μ⟩, truncation at order p_c reproduces exactly the **dense/modern Hopfield (p-spin) models** with capacity O(N^(p_c−1)). The full untruncated projector sum is the exponential-capacity limit of modern Hopfield networks.

### Step 3 — Quantum dimer memories
Each memory = a **perfect matching (dimer covering)** of N spins into singlet pairs:

```
|ψ_q^μ⟩ = Π_(ij)∈μ (1/√2)(|↑↓⟩_ij − |↓↑⟩_ij)

H_q = −Σ_μ Π_(ij)∈μ (1/4 − S_i·S_j)   [singlet projector Π_ij = 1/4 − S_i·S_j]
```

Expansion in products of (σ_i·σ_j) bonds:
- **p_q = 1**: antiferromagnetic Heisenberg terms on memory bonds — NO extensive capacity.
- **p_q = 2**: pairwise products (σ_i·σ_j)(σ_k·σ_l) — the quantum analogue of the pairwise Hopfield Hamiltonian; primary model of the paper.
- **General p_q**: capacity scales as **N^(2p_q−1)** (vs classical N^(p_c−1)); the quantum model matches the classical power when identifying 2p_q ↔ p_c — origin unclear (open question).

## Stability & Capacity Analysis

### Local energetic stability
Memory is stable against perturbation e^(−iεÔ) if:
1. ⟨ψ|[Ô, H]|ψ⟩ = 0 (stationary point)
2. ⟨ψ|[Ô, H, Ô]|ψ⟩ > 0 (local minimum; double commutator)

Perturbation classes for dimer memories:
- **Single-spin rotations**: ALWAYS stable for H²_q — rotation breaks the containing singlet into a triplet, raising energy; every term contributes positively. No destabilization possible.
- **Bond rearrangements (plaquette flips)**: swap two spins between two singlets (ik)(jl)→(il)(jk). The binding constraint. Energy analysis reduces to combinatorial counting:
  - Primary memory contributes O(N) stabilizing terms (unaffected singlets paired with an original singlet).
  - Each secondary memory contributes destabilizing terms only if it shares a swapped bond + an O(1) shared singlet — probability O(1/N), zero mean, so variance O(K/N).
  - Balance signal √(variance): **K_max = O(N³)**; careful analysis over ALL bond rearrangements adds the log correction → **K_max = O(N³/log N)** (fit coefficient ≈ 0.015 in simulations).

### Quantum hybridization (Anderson-localization analogy)

Classical stability analysis can't see tunneling. Define hybridization metric over single-flip neighbors μ̃:

```
W = max_μ̃ |⟨ψ_μ| H |φ_μ̃⟩| / |E_μ − E_μ̃|  (φ_μ̃ = Gram-Schmidt-orthogonalized neighbor)
```

Like Anderson's resonant-hybridization criterion, but with "sites" = points in dimer-covering Hilbert space. Simulations: W collapses vs K/N³; std-dev of W explodes beyond K_max ≈ 0.015 N³ — onset of resonant hybridization between memory and nearby coverings.

### Retrieval diagnostics
- **Singlet Mattis overlap**: m_q^μ = (2/N) Σ_(ij)∈μ ⟨P_ij⟩; = 1 for perfect memory, ≈ 1/4 for an unrelated covering (shared-bond count is O(1)). Curves for different N cross at K_C(N) → retrieval/non-retrieval transition. Beyond capacity, max overlap stays ≳ 0.7 — eigenstate retains singlet character of one memory even when retrieval fails (same happens classically).
- **Entanglement structure**: one-tangle τ_i = 4·det(ρ_i) = 1 for ALL spins in the S²_tot=0 sector (SU(2)-invariant states force ρ_i = I/2). Pairwise concurrence C_ij = max(0, 2p_ij − 1) — nonzero only when singlet weight p_ij > 1/2. Effective partner count N_eff (concurrence IPR) → 1 in the retrieval phase: each spin concentrates entanglement on its unique dimer partner, saturating the CKW inequality. Eigenstate → single covering structure in thermodynamic limit.

## Why It Matters

- Entanglement lets associative memory store **relational/graph structures** (perfect matchings) that are NOT reducible to local spin orientations — every single-spin expectation vanishes, so no classical encoding can represent the memory content.
- Signal-to-noise logic parallel to classical Hopfield: restoring signal O(N^(p−1)), noise variance O(K·N^(p−1)); the quantum model gains one extra power per interaction order because each bond term already carries two sites.
- Practical route: retrieval could be realized by coupling to a bath that implements the destabilizing/stabilizing operators; open systems (Lindblad) versions are the natural next step.

## Open Problems (from authors)

1. Extend beyond dimer coverings to richer entangled memories (e.g., random stabilizer graph states).
2. Dynamics/dissipation for actual storage+retrieval protocols (current work is static/closed-system).
3. Explain the 2p_q ↔ p_c classical-quantum power coincidence.

## Reusable Patterns

- **Truncated projector-sum encoding**: any set of target quantum states → approximate-ground-state k-local Hamiltonian; truncation order is the capacity/k-locality knob.
- **Combinatorial stability counting**: capacity = balance of O(N^signal) restoring terms vs √(O(K/N)) variance from secondary memories; apply to any pattern family with O(1) cross-pattern overlap.
- **Hybridization metric W**: resonant-hybridization diagnostic transferable to any quantum memory landscape (Anderson criterion in configuration space).
- **Singlet Mattis overlap**: retrieval-quality metric for non-orthogonal, non-product memory bases.
- **N_eff concurrence IPR**: verifies memories retain unique-partner entanglement structure.

## Key Equations (quick reference)

| Object | Formula |
---|---|n
| Singlet projector | Π_ij = 1/4 − S_i·S_j |
| Dimer memory | ψ = Π_bonds (|↑↓⟩−|↓↑⟩)_ij/√2 |
| p_q=2 Hamiltonian | H²_q = −(1/2^N) Σ_μ Σ_(ij)<(kl)∈μ (σ_i·σ_j)(σ_k·σ_l) |
| Capacity (p_q≥2) | K_max = O(N^(2p_q−1)/log N) |
| Hybridization metric | W = max |⟨ψ_μ|H|φ_μ̃⟩|/|E_μ−E_μ̃| |
| Singlet Mattis overlap | m_q^μ = (2/N)Σ_(ij)∈μ ⟨Π_ij⟩ |