---
name: renyi-spectrum-entanglement-assisted-graphs
description: Rényi information-radius family populates graph spectra.
category: ai_collection
source_title: "The Lovász number is not alone: a continuum of Rényi points in the entanglement-assisted spectrum of graphs"
source_arxiv: "2610.20775"
---

# Rényi Points in the Entanglement-Assisted Spectrum of Graphs

**Source**: Mghirbi & Douglas, arXiv:2610.20775 (quant-ph/math.CO, Oct 2026). Discovers a CONTINUUM of new elements (beyond the Lovász number ϑ) in Li-Zuiddam's entanglement-assisted asymptotic spectrum of graphs — a family ϑα indexed by Rényi divergence order α ∈ [0,2] — proving the Duan-Winter pentagon conjecture and separating Holevo capacity from no-signalling simulation cost.

## When to Use
- Bounding entanglement-assisted Shannon capacity Θ* of a confusability graph beyond the Lovász number
- Computing/relating zero-error quantities: minimal Holevo capacity C_min, no-signalling simulation cost Σ, fractional packing α*
- Multiplicativity proofs for channel quantities under strong products when representations need not factor as tensor products
- Rényi-divergence information-radius formulations of graph parameters (Petz α∈[0,2], sandwiched β∈[1/2,∞])

## Core Methodology

### 1. One family, three quantities
Define the order-α information radius for classical-quantum channels x↦ρ_x compatible with graph G, centered at state σ:

```
log2 ϑα(G) = inf_{(ρ_x), σ} max_x D_α(ρ_x ∥ σ)
```

Then ϑ0 = ϑ (Lovász; Schrijver/Dalai), ϑ1 = 2^{C_min} (Holevo min-max), ϑ2 = Σ (no-signalling simulation cost). The Duan-Winter chain log2 ϑ ≤ C_min ≤ S0,NS ≤ log2 Σ ≤ log2 α* is a chain of samples of ONE monotone family (nondecreasing in α since Dα is; continuous on [0,1)).

### 2. Tower identity for compressions (the multiplicativity engine)
Power compression: for projection P, state σ, s = 1−α ∈ [−1,1]: K_s(σ,P) is P σ^s P restricted to ran P (extended by zero); weight Z_s = its trace. **Tower identity**: for P ≤ Q with K_s(σ,Q) faithful, compressing in two steps = one step: K_s(K_s(σ,Q), P) = K_s(σ,P); weights scale: Z_s(K_s(σ,Q)/z, P) = Z_s(σ,P)/z. This splits the weight of each cell of a G⊠H representation into a row part × within-row part — proving multiplicativity ϑα(G⊠H) = ϑα(G)ϑα(H) WITHOUT requiring product representations to factor as tensors (the prior state of the art needed factorization).

### 3. Spectrum membership (Theorem A)
Every ϑα (0 ≤ α ≤ 2) is in the entanglement-assisted spectrum X(G, ≤*): normalization (ϑα(K1)=1), additivity under ⊔, multiplicativity under ⊠ (via tower identity), and monotonicity under entanglement-assisted cohomomorphisms (data-processing for Petz Rényi at α ≤ 2 — this is exactly WHY the argument stops at order 2: above it, Petz divergences lose data processing). Sandwiched Rényi radii of order β ∈ [1/2,∞] give the SAME family at α = 2−1/β.

### 4. Pentagon: continuum-many distinct points (Theorem B)
On C5: ϑα(C5) = 5/2 for α ∈ [1/2, 2]; for α ∈ [0, 1/2] the map α ↦ ϑα(C5) is continuous onto [√5, 5/2] (Sandwiched/bounded by explicit formula with p = 1/(1−α)). Since the spectrum is closed under these values, X(G,≤*) contains continuum-many distinct points. **Corollary (Duan-Winter conjecture, proved)**: log2√5 < C_min(C5) = S0,NS(C5) = log2Σ(C5) = log2 α*(C5) = log2(5/2) — a Hilbert-Schmidt inequality for the pentagon gives the missing lower bound.

### 5. Order 1 ≠ order 2 (Theorem C)
A 32-vertex graph G32 built from the Mermin-Peres magic square separates: 2C_min(G32) ≤ 32329248967670751/93824992214030 < 5225365592240894/15147154828811 ≤ log2... Σ(G32), certified in EXACT rational arithmetic. Both bounds lie inside (ϑ, α*) = (6, 32/5). Also: graph-level no-signalling simulation rate always equals its single-letter value log2Σ(G) (settles an open link); Σ never exceeds projective rank of the complement, strict on a 1440-vertex graph.

## Workflow
1. Express the target graph quantity as an information radius (choose Petz order α or sandwiched β)
2. For capacity upper bounds: pick α, solve the radius minimization (SDP at α=2, eigenvector-like at α=0)
3. For multiplicativity: group product-graph representations by row projections S_x (rows represent G, cells represent H) and apply the tower identity to split weights
4. For separations: construct magic-square-based graphs with known symmetry and certify bounds in exact rational arithmetic

## Pitfalls
- α > 2 fails: Petz Rényi loses data processing → monotonicity breaks (Remark 4.8); the family is genuinely capped at 2
- Do NOT assume optimal representations of strong products factor as tensor products — the tower identity exists precisely because they need not
- The quantum preorder spectrum X(G,≤q) ⊇ X(G,≤*): fractional clique cover / α* is NOT in either (Li-Zuiddam)
- C5 cannot separate order 1 from order 2 — both equal 5/2 there; use G32 instead

## References
- Mghirbi & Douglas, arXiv:2610.20775 (2026)
- Li & Zuiddam (entanglement-assisted asymptotic spectrum); Duan & Winter 2016 (chain (1)); Strassen duality; Vrana (uncountable ordinary spectrum)
